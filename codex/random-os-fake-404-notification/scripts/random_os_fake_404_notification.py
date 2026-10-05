import sys
import os
import time
import random
import argparse
import threading
import platform
import subprocess
from datetime import datetime, timedelta

NOTIFICATIONS = [
    "404: あなたのやる気が見つかりません",
    "404: 今日の集中力が迷子です",
    "404: 予定されていた進捗が行方不明です",
    "404: コーヒーブレイクが検出されませんでした",
    "404: 午後の生産性が応答しません",
    "404: Motivation Not Found",
    "404: 重要なアイデアが行方不明です",
    "404: 進捗状況がサーバーに見つかりません",
    "404: あなたのやる気スイッチが見つかりません",
    "404: 休憩タイムが見つかりませんでした"
]

TRIGGER_KEYWORDS = [
    "やる気", "進捗", "集中", "エラー", "404", "motivation", "productivity", "break", "idea"
]

MIN_INTERVAL = 300  # 秒（5分）
MAX_INTERVAL = 1200 # 秒（20分）

class NotificationManager:
    def __init__(self):
        self.os_type = platform.system()

    def send_notification(self, message):
        if self.os_type == "Darwin":
            subprocess.run(["osascript", "-e", f'display notification "{message}" with title "OS Notification"'], check=False)
        elif self.os_type == "Linux":
            subprocess.run(["notify-send", "OS Notification", message], check=False)
        elif self.os_type == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("OS Notification", message, duration=5)
            except ImportError:
                print(f"[通知] {message}")
        else:
            print(f"[通知] {message}")

    def print_terminal(self, message):
        print(f"[通知] {message}")


def random_interval():
    return random.randint(MIN_INTERVAL, MAX_INTERVAL)


def monitor_keywords(keywords, callback):
    """標準入力を監視し、キーワード検出時にcallbackを呼ぶ"""
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            for kw in keywords:
                if kw in line:
                    callback(random.choice(NOTIFICATIONS))
    except KeyboardInterrupt:
        pass


def notification_loop(args):
    nm = NotificationManager()
    next_time = datetime.now() + timedelta(seconds=random_interval())
    while True:
        now = datetime.now()
        if now >= next_time:
            msg = random.choice(NOTIFICATIONS)
            if args.terminal:
                nm.print_terminal(msg)
            else:
                nm.send_notification(msg)
            next_time = now + timedelta(seconds=random_interval())
        time.sleep(2)


def list_messages():
    print("利用可能な通知メッセージ一覧:")
    for i, msg in enumerate(NOTIFICATIONS):
        print(f"{i+1}. {msg}")


def summary():
    print("random-os-fake-404-notification Skill 概要:")
    print("- OS風404エラー通知をランダムなタイミングで表示")
    print("- 通知内容は毎回異なるジョークメッセージ")
    print("- 明示呼び出し/暗黙発動の両対応")
    print(f"- 通知間隔: {MIN_INTERVAL//60}〜{MAX_INTERVAL//60}分")


def main():
    parser = argparse.ArgumentParser(description='Random OS Fake 404 Notification Skill')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='通知をランダムに発火')
    parser_run.add_argument('--terminal', action='store_true', help='通知をターミナルに出力')
    parser_run.add_argument('--stdin-monitor', action='store_true', help='標準入力からキーワード監視で即時通知')

    parser_list = subparsers.add_parser('list', help='全通知メッセージを表示')
    parser_summary = subparsers.add_parser('summary', help='Skill概要を表示')

    args = parser.parse_args()

    if args.command == 'run':
        if args.stdin_monitor:
            nm = NotificationManager()
            monitor_keywords(TRIGGER_KEYWORDS, nm.print_terminal if args.terminal else nm.send_notification)
        else:
            notification_loop(args)
    elif args.command == 'list':
        list_messages()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
