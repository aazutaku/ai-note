import subprocess
import sys
import argparse
import datetime
import os
import json
from typing import List, Optional

HAIKU_TEMPLATES = [
    # (error_keyword, haiku)
    ("Permission denied", "Permission denied、心閉ざして、春霞"),
    ("Segmentation fault", "Segmentation fault、記憶の彼方、絶望感"),
    ("No such file or directory", "ファイル消え、探す手のひら、春の闇"),
    ("File exists", "既にあり、重ねる想い、夏の雲"),
    ("Not a directory", "道迷い、ディレクトリなく、秋の風"),
    ("Is a directory", "中を見て、戸惑う指先、冬の朝"),
    ("command not found", "道を問う、コマンド知らず、春の雨"),
    ("Invalid argument", "理屈越え、引数迷い、霧の中"),
    ("Broken pipe", "途切れたる、パイプの先に、冬の星"),
    ("Timeout", "時を待ち、応えぬ声に、夏の夜"),
    ("Connection refused", "扉閉じ、拒まれし糸、秋の夜"),
]

GENERIC_HAIKU = "エラーなり、無常の響き、春の夢"

HISTORY_FILE = os.path.expanduser("~/.os_error_bigaku_haiku_history.json")


def find_haiku(error_message: str) -> str:
    for keyword, haiku in HAIKU_TEMPLATES:
        if keyword.lower() in error_message.lower():
            return haiku
    return GENERIC_HAIKU


def run_command(cmd: List[str]) -> (int, str, str):
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return proc.returncode, proc.stdout, proc.stderr
    except Exception as e:
        return 1, "", str(e)


def print_haiku_error(cmd: List[str], error_message: str):
    haiku = find_haiku(error_message)
    print("[和風エラー俳句]")
    print(haiku)
    print("[元のエラー]")
    print(error_message)
    save_to_history(cmd, haiku, error_message)


def save_to_history(cmd: List[str], haiku: str, error_message: str):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "command": " ".join(cmd),
        "haiku": haiku,
        "error": error_message
    }
    history = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
        except Exception:
            history = []
    history.append(entry)
    # Keep only last 100 entries
    history = history[-100:]
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def show_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴はありません。")
        return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)
    print("=== エラー俳句履歴 ===")
    for entry in history[-20:]:
        print(f"{entry['timestamp']}")
        print(f"コマンド: {entry['command']}")
        print(f"俳句: {entry['haiku']}")
        print(f"エラー: {entry['error']}")
        print("-")


def main():
    parser = argparse.ArgumentParser(description="コマンド実行時のエラーを和風俳句で味わうCLIラッパー")
    subparsers = parser.add_subparsers(dest="subcmd")

    run_parser = subparsers.add_parser("run", help="コマンドをラップ実行し、エラー時に俳句表示")
    run_parser.add_argument("cmd", nargs=argparse.REMAINDER, help="実行するコマンド")

    log_parser = subparsers.add_parser("haiku-log", help="エラー俳句履歴を表示")

    args = parser.parse_args()

    if args.subcmd == "run":
        if not args.cmd:
            print("コマンドを指定してください。例: os-error-bigaku-haiku run ls /root")
            sys.exit(1)
        code, out, err = run_command(args.cmd)
        if code != 0 or err:
            print_haiku_error(args.cmd, err.strip() or f"Exit code: {code}")
        else:
            print(out, end="")
    elif args.subcmd == "haiku-log":
        show_history()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
