import sys
import argparse
import random
import platform
import subprocess
import time
from typing import List, Optional

APOLOGY_MESSAGES = [
    "本日はご迷惑をおかけしております。",
    "謎の遅延が発生しましたが、原因不明です。",
    "大変申し訳ありませんが、さっきのコマンドは無かったことにしてください。",
    "何もしていませんが、一応謝っておきます。",
    "予期せぬ問題が発生したかもしれません。",
    "本件については鋭意調査中です。",
    "ご不便をおかけし申し訳ありません。",
    "詳細は不明ですが、何かが起きた可能性があります。",
    "ご理解とご協力をお願いいたします。",
    "次回はもっと頑張ります。",
    "システムは正常ですが、念のためお詫びします。",
    "エラーっぽいことが発生しました（気のせいかもしれません）。",
    "本件については担当者不在のため対応できません。",
    "今後ともよろしくお願いいたします。",
    "何もしていませんが、謝罪だけしておきます。"
]

NOTIFY_TITLE = "OSよりお詫び"


def detect_os() -> str:
    sysname = platform.system().lower()
    if 'darwin' in sysname:
        return 'macos'
    elif 'linux' in sysname:
        return 'linux'
    else:
        return 'unsupported'


def send_notification(message: str) -> None:
    os_type = detect_os()
    if os_type == 'macos':
        script = f'display notification "{message}" with title "{NOTIFY_TITLE}"'
        try:
            subprocess.run(['osascript', '-e', script], check=True)
        except Exception as e:
            print(f"[ERROR] 通知送信失敗: {e}")
    elif os_type == 'linux':
        try:
            subprocess.run(['notify-send', NOTIFY_TITLE, message], check=True)
        except Exception as e:
            print(f"[ERROR] 通知送信失敗: {e}")
    else:
        print("[ERROR] このOSには対応していません。通知は表示されません。")


def get_random_message() -> str:
    return random.choice(APOLOGY_MESSAGES)


def cli_notify(args):
    message = get_random_message() if not args.message else args.message
    send_notification(message)
    print(f"[通知] {NOTIFY_TITLE}: {message}")


def cli_list(args):
    print("-- 通知候補一覧 --")
    for i, msg in enumerate(APOLOGY_MESSAGES):
        print(f"{i+1:2}: {msg}")


def cli_summary(args):
    print(f"通知パターン数: {len(APOLOGY_MESSAGES)}")
    print(f"対応OS: macOS, Linux (notify-send)\n")
    print("このSkillは、完全なフェイク通知のみを送信し、実際のエラーやファイル操作は一切行いません。\n")


def cli_auto(args):
    count = args.count if args.count else 5
    min_interval = args.min_interval if args.min_interval else 60
    max_interval = args.max_interval if args.max_interval else 180
    print(f"自動モード: {count}回、{min_interval}-{max_interval}秒間隔で通知します。\n")
    for i in range(count):
        msg = get_random_message()
        send_notification(msg)
        print(f"[{i+1}/{count}] {NOTIFY_TITLE}: {msg}")
        if i < count - 1:
            interval = random.randint(min_interval, max_interval)
            time.sleep(interval)


def build_parser():
    parser = argparse.ArgumentParser(description='random-os-apology-notifier: OSが無責任に謝罪する通知をランダム表示')
    subparsers = parser.add_subparsers(dest='command')

    parser_notify = subparsers.add_parser('notify', help='ランダムな謝罪通知を1回表示')
    parser_notify.add_argument('--message', type=str, help='任意の通知メッセージ')
    parser_notify.set_defaults(func=cli_notify)

    parser_list = subparsers.add_parser('list', help='通知候補メッセージ一覧を表示')
    parser_list.set_defaults(func=cli_list)

    parser_summary = subparsers.add_parser('summary', help='Skillの概要情報を表示')
    parser_summary.set_defaults(func=cli_summary)

    parser_auto = subparsers.add_parser('auto', help='一定間隔でランダム通知を複数回表示')
    parser_auto.add_argument('--count', type=int, help='通知回数 (デフォルト:5)')
    parser_auto.add_argument('--min-interval', type=int, help='通知間隔の下限(秒) (デフォルト:60)')
    parser_auto.add_argument('--max-interval', type=int, help='通知間隔の上限(秒) (デフォルト:180)')
    parser_auto.set_defaults(func=cli_auto)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == '__main__':
    main()
