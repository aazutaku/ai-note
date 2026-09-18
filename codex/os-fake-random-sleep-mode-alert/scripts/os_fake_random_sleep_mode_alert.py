import sys
import argparse
import random
import time
import platform
import subprocess
import threading
from datetime import datetime

NOTIFICATION_MESSAGES = [
    "重大: あなたのPCは3分後に自動昼寝モードへ移行します。",
    "警告: 集中力がOS基準値を下回りました。自動スリープを推奨します。",
    "システムがあなたの活動量低下を検知しました。5分以内に休憩してください。",
    "OSポリシーにより強制スリープまで残り1分です。",
    "眠気検知: システムが昼寝モードを推奨します。",
    "重大: キーボード入力が10分間ありません。スリープ準備中。",
    "警告: システムがあなたの集中度を監視しています。",
    "OS通知: 休憩推奨。自動昼寝モードまで残り2分。",
    "警告: 謎のOSアップデートにより強制スリープが有効化されました。",
    "重大: あなたの作業速度がOS基準値を下回りました。"
]

TERMINAL_PREFIX = "[OS通知]"


def send_notification(message):
    system = platform.system()
    if system == "Darwin":  # macOS
        subprocess.run([
            "osascript", "-e",
            f'display notification "{message}" with title "OSスリープ警告"'
        ])
    elif system == "Linux":
        try:
            subprocess.run([
                "notify-send", "OSスリープ警告", message
            ])
        except FileNotFoundError:
            print(f"{TERMINAL_PREFIX} {message}")
    elif system == "Windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("OSスリープ警告", message, duration=5)
        except ImportError:
            print(f"{TERMINAL_PREFIX} {message}")
    else:
        print(f"{TERMINAL_PREFIX} {message}")


def random_notification_loop(min_interval=60, max_interval=300, count=3, dry_run=False):
    for i in range(count):
        wait_time = random.randint(min_interval, max_interval)
        time.sleep(wait_time)
        message = random.choice(NOTIFICATION_MESSAGES)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if dry_run:
            print(f"{timestamp} {TERMINAL_PREFIX} {message}")
        else:
            send_notification(message)


def notify_once(dry_run=False):
    message = random.choice(NOTIFICATION_MESSAGES)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if dry_run:
        print(f"{timestamp} {TERMINAL_PREFIX} {message}")
    else:
        send_notification(message)


def list_messages():
    print("== 通知メッセージ一覧 ==")
    for i, msg in enumerate(NOTIFICATION_MESSAGES):
        print(f"{i+1:02d}: {msg}")


def summary():
    print("Skill: os-fake-random-sleep-mode-alert")
    print(f"通知バリエーション数: {len(NOTIFICATION_MESSAGES)}")
    print("実際のスリープ動作は一切発生しません。ネタ用途専用です。")


def parse_args():
    parser = argparse.ArgumentParser(
        description="OS風スリープモード警告通知をランダムに表示するスキル (ネタ用途)"
    )
    subparsers = parser.add_subparsers(dest="command")

    parser_once = subparsers.add_parser("once", help="1回だけランダム通知を表示")
    parser_once.add_argument("--dry-run", action="store_true", help="通知をターミナル出力のみで実行")

    parser_loop = subparsers.add_parser("loop", help="ランダム間隔で複数回通知")
    parser_loop.add_argument("--min", type=int, default=60, help="通知間隔(秒)の最小値")
    parser_loop.add_argument("--max", type=int, default=300, help="通知間隔(秒)の最大値")
    parser_loop.add_argument("--count", type=int, default=3, help="通知回数")
    parser_loop.add_argument("--dry-run", action="store_true", help="通知をターミナル出力のみで実行")

    parser_list = subparsers.add_parser("list", help="通知メッセージ一覧を表示")
    parser_summary = subparsers.add_parser("summary", help="Skill概要を表示")

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "once":
        notify_once(dry_run=args.dry_run)
    elif args.command == "loop":
        random_notification_loop(
            min_interval=args.min,
            max_interval=args.max,
            count=args.count,
            dry_run=args.dry_run
        )
    elif args.command == "list":
        list_messages()
    elif args.command == "summary":
        summary()
    else:
        print("使い方: python os_fake_random_sleep_mode_alert.py [once|loop|list|summary] [--オプション]")

if __name__ == "__main__":
    main()
