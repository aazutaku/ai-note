import os
import sys
import argparse
import json
import shutil
from typing import Optional, Dict

MOOD_MARKS = {
    "元気": "( •̀ᴗ•́ )و ̑̑",
    "だるい": "(￣_￣ )",
    "やる気MAX": "(ง •̀_•́)ง",
    "燃え尽き寸前": "(╯°□°）╯︵ ┻━┻",
    "迷走中": "(＠_＠;)",
    "平常運転": "(・_・)ノ",
    "集中": "(｀・ω・´)",
    "休憩中": "( ˘ω˘ )",
    "デフォルト": "(・_・)"
}

MOOD_ENV = "MOOD"
MOOD_STORE = os.path.expanduser("~/.terminal_mood.json")


def load_mood() -> Dict[str, str]:
    if os.path.exists(MOOD_STORE):
        try:
            with open(MOOD_STORE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception:
            return {}
    return {}

def save_mood(mood: str):
    data = {"mood": mood}
    with open(MOOD_STORE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def get_current_mood() -> str:
    # 優先: 環境変数 > ファイル > デフォルト
    mood = os.environ.get(MOOD_ENV)
    if mood:
        return mood
    data = load_mood()
    return data.get("mood", "デフォルト")

def get_mood_mark(mood: str) -> str:
    # 部分一致
    for key, val in MOOD_MARKS.items():
        if key in mood:
            return val
    return MOOD_MARKS["デフォルト"]

def show_mood():
    mood = get_current_mood()
    mark = get_mood_mark(mood)
    print(f"今日の気分：{mood}")
    print("──────────────")
    print(mark)
    print("──────────────")

def set_mood(mood: str):
    save_mood(mood)
    print(f"今日の気分：{mood}")
    print(get_mood_mark(mood))

def wrap_command(cmd: list):
    mood = get_current_mood()
    mark = get_mood_mark(mood)
    print(f"今日の気分：{mood}")
    import subprocess
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)
    except Exception as e:
        print(f"コマンド実行エラー: {e}", file=sys.stderr)
        sys.exit(1)

def install_prompt(shell: Optional[str] = None):
    shell = shell or os.environ.get("SHELL", "")
    if "zsh" in shell:
        rcfile = os.path.expanduser("~/.zshrc")
        prompt_line = 'PROMPT="$(python3 ~/.claude/skills/terminal-mood-indicator/terminal_mood_indicator.py prompt) $PROMPT"'
    elif "bash" in shell:
        rcfile = os.path.expanduser("~/.bashrc")
        prompt_line = 'PS1="$(python3 ~/.claude/skills/terminal-mood-indicator/terminal_mood_indicator.py prompt) $PS1"'
    else:
        print("対応シェル: bash, zsh のみ。手動で設定してください。", file=sys.stderr)
        return
    with open(rcfile, 'a', encoding='utf-8') as f:
        f.write(f"\n# terminal-mood-indicator\n{prompt_line}\n")
    print(f"{rcfile} にプロンプト設定を追記しました。新しいターミナルで有効になります。")

def show_prompt():
    mood = get_current_mood()
    mark = get_mood_mark(mood)
    print(f"[{mood}:{mark}]")

def list_moods():
    print("利用可能な気分:")
    for k in MOOD_MARKS.keys():
        print(f"- {k}")

def main():
    parser = argparse.ArgumentParser(description="ターミナル気分インジケータ")
    subparsers = parser.add_subparsers(dest="command")

    setp = subparsers.add_parser("set", help="気分をセット")
    setp.add_argument("mood", type=str, help="今日の気分")

    showp = subparsers.add_parser("show", help="現在の気分を表示")
    subparsers.add_parser("list", help="利用可能な気分一覧")
    instp = subparsers.add_parser("install-prompt", help="プロンプトに気分を埋め込む")
    instp.add_argument("--shell", type=str, default=None, help="シェル名 (bash/zsh)")
    subparsers.add_parser("prompt", help="プロンプト用気分出力 (内部用)")
    wrapp = subparsers.add_parser("wrap", help="コマンド実行時に気分を表示")
    wrapp.add_argument("cmd", nargs=argparse.REMAINDER, help="実行するコマンド")

    args = parser.parse_args()
    if args.command == "set":
        set_mood(args.mood)
    elif args.command == "show":
        show_mood()
    elif args.command == "list":
        list_moods()
    elif args.command == "install-prompt":
        install_prompt(args.shell)
    elif args.command == "prompt":
        show_prompt()
    elif args.command == "wrap":
        if not args.cmd:
            print("コマンドを指定してください", file=sys.stderr)
            sys.exit(1)
        wrap_command(args.cmd)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
