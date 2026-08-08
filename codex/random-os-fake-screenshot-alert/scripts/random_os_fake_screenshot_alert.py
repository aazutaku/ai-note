import sys
import os
import random
import platform
import subprocess
import argparse
import time
from typing import List

RANDOM_MESSAGES = [
    "スクリーンショット保存済み：バグ発生の瞬間",
    "証拠画像を保存しました（保存先：？？？）",
    "あなたの集中顔を記録しました",
    "システムが謎の瞬間をキャプチャしました",
    "何もしていませんが保存完了です",
    "保存完了：何を保存したかは不明です",
    "証拠画像をクラウドにアップロードしました（嘘）",
    "バグトラッキング用スクリーンショット保存済み",
    "あなたのリアクションを記録しました",
    "OSが気まぐれにスクリーンショットを保存しました"
]

DEFAULT_INTERVAL = 0

class Notifier:
    def __init__(self):
        self.system = platform.system().lower()

    def notify(self, message: str):
        if self.system == 'windows':
            self._notify_windows(message)
        elif self.system == 'darwin':
            self._notify_macos(message)
        elif self.system == 'linux':
            self._notify_linux(message)
        else:
            print(f"[通知] {message}")

    def _notify_windows(self, message: str):
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("スクリーンショット通知", message, duration=5, threaded=True)
        except ImportError:
            # Fallback: powershell
            script = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
            script += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
            script += f'$textNodes = $template.GetElementsByTagName("text");$textNodes.Item(0).AppendChild($template.CreateTextNode("スクリーンショット通知")) > $null;'
            script += f'$textNodes.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null;'
            script += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
            script += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("Python") ;'
            script += f'$notifier.Show($toast)'
            subprocess.call(["powershell", "-Command", script])

    def _notify_macos(self, message: str):
        try:
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "スクリーンショット通知"'
            ], check=True)
        except Exception:
            print(f"[通知] {message}")

    def _notify_linux(self, message: str):
        try:
            subprocess.run([
                "notify-send", "スクリーンショット通知", message
            ], check=True)
        except Exception:
            print(f"[通知] {message}")


def random_message() -> str:
    return random.choice(RANDOM_MESSAGES)

def show_alert(notifier: Notifier, count: int = 1, interval: float = 0):
    for i in range(count):
        msg = random_message()
        notifier.notify(msg)
        if interval > 0 and i < count - 1:
            time.sleep(interval)

def list_messages():
    print("--- 通知メッセージ候補 ---")
    for m in RANDOM_MESSAGES:
        print(f"- {m}")

def summary():
    print("Skill: random-os-fake-screenshot-alert")
    print("用途: OS風の謎スクリーンショット保存通知をランダム表示")
    print(f"通知候補数: {len(RANDOM_MESSAGES)}")
    print("サポートOS: Windows, macOS, Linux")
    print("保存実体: なし (通知のみ)")

def parse_args():
    parser = argparse.ArgumentParser(description='謎のOSスクリーンショット保存通知をランダム表示するSkill')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='ランダム通知を表示')
    parser_alert.add_argument('-n', '--count', type=int, default=1, help='通知回数')
    parser_alert.add_argument('-i', '--interval', type=float, default=DEFAULT_INTERVAL, help='通知間隔(秒)')

    parser_list = subparsers.add_parser('list', help='通知メッセージ候補一覧')
    parser_summary = subparsers.add_parser('summary', help='Skill概要')

    return parser.parse_args()


def main():
    args = parse_args()
    notifier = Notifier()
    if args.command == 'alert' or args.command is None:
        count = getattr(args, 'count', 1)
        interval = getattr(args, 'interval', 0)
        show_alert(notifier, count=count, interval=interval)
    elif args.command == 'list':
        list_messages()
    elif args.command == 'summary':
        summary()
    else:
        print("不明なサブコマンドです。--help を参照してください。")

if __name__ == '__main__':
    main()
