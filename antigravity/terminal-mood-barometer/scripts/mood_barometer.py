import argparse
import random
import subprocess
import sys
import os
import time
from typing import Tuple, List

COMMENTS = [
    "今日もコーディング日和！",
    "カフェイン補給推奨。",
    "集中力アップ中！",
    "そろそろ休憩しませんか？",
    "やる気全開モード！",
    "気分は上々！",
    "脳内デバッグ中…",
    "眠気注意報発令中。",
    "タスク山盛り！",
    "コードの海を泳ぐ。",
    "バグは友達。",
    "やる気ゲージ急上昇！",
    "今日は雨、でもコードは晴れ",
    "おやつタイムが近い…",
    "進捗どうですか？",
    "リファクタリング日和。",
    "コーヒーブレイク推奨。",
    "エラーは成長の証。",
    "やる気2：再起動が必要かも。",
    "考えすぎ注意！"
]

EXCLUDED_COMMANDS = [
    'cat', 'less', 'more', 'head', 'tail', 'vim', 'nano', 'vi', 'emacs',
    'man', 'top', 'htop', 'watch', 'clear', 'reset', 'exit', 'logout'
]


def random_mood() -> Tuple[int, str]:
    """Generate a random mood index and comment."""
    index = random.randint(1, 100)
    comment = random.choice(COMMENTS)
    return index, comment


def should_display(cmd: List[str]) -> bool:
    """Determine if mood barometer should be displayed for this command."""
    if not cmd:
        return False
    base_cmd = os.path.basename(cmd[0])
    if base_cmd in EXCLUDED_COMMANDS:
        return False
    # Suppress for piped or redirected commands
    if any(token in cmd for token in ['|', '>', '>>', '<']):
        return False
    # Suppress for batch/script files
    if base_cmd.endswith(('.sh', '.bat', '.ps1')):
        return False
    return True


def print_mood():
    index, comment = random_mood()
    print(f"やる気 {index}：{comment}")


def run_command(cmd: List[str]) -> int:
    """Run the given command and return its exit code."""
    try:
        proc = subprocess.Popen(cmd, stdout=sys.stdout, stderr=sys.stderr)
        proc.communicate()
        return proc.returncode
    except FileNotFoundError:
        print(f"コマンドが見つかりません: {cmd[0]}")
        return 127
    except Exception as e:
        print(f"コマンド実行中にエラー: {e}")
        return 1


def log_mood(cmd: List[str], index: int, comment: str):
    log_path = os.path.expanduser("~/.mood_barometer.log")
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    cmd_str = ' '.join(cmd)
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"{ts}\t{cmd_str}\t{index}\t{comment}\n")


def list_log(n: int = 10):
    log_path = os.path.expanduser("~/.mood_barometer.log")
    if not os.path.exists(log_path):
        print("ログファイルがありません。")
        return
    with open(log_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()[-n:]
    for line in lines:
        print(line.rstrip())


def summary_log():
    log_path = os.path.expanduser("~/.mood_barometer.log")
    if not os.path.exists(log_path):
        print("ログファイルがありません。")
        return
    moods = []
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 4:
                try:
                    moods.append(int(parts[2]))
                except ValueError:
                    continue
    if not moods:
        print("集計できるデータがありません。")
        return
    avg = sum(moods) / len(moods)
    print(f"平均やる気指数：{avg:.1f} (過去{len(moods)}回)")


def main():
    parser = argparse.ArgumentParser(description="Terminal Mood Barometer")
    subparsers = parser.add_subparsers(dest='subcmd')

    parser_run = subparsers.add_parser('run', help='コマンドを実行し気分指数を表示')
    parser_run.add_argument('command', nargs=argparse.REMAINDER, help='実行するコマンド')

    parser_list = subparsers.add_parser('list', help='気分ログの最新N件を表示')
    parser_list.add_argument('-n', type=int, default=10, help='表示件数')

    parser_summary = subparsers.add_parser('summary', help='気分指数の平均を表示')

    args = parser.parse_args()

    if args.subcmd == 'run':
        cmd = args.command
        if not cmd:
            print("実行するコマンドを指定してください。")
            sys.exit(1)
        if should_display(cmd):
            index, comment = random_mood()
            print(f"やる気 {index}：{comment}")
            log_mood(cmd, index, comment)
        exitcode = run_command(cmd)
        sys.exit(exitcode)
    elif args.subcmd == 'list':
        list_log(args.n)
    elif args.subcmd == 'summary':
        summary_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
