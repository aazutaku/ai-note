import sys
import os
import argparse
import random
import time
import subprocess
from typing import List

CHAOS_MESSAGES = [
    "危険：バグが自我を獲得しました",
    "注意：メモリがピクニック中",
    "深刻：キーボードが人生に迷っています",
    "警告：OSが哲学的思索に入りました",
    "重大：CPUが詩を書き始めました",
    "警告：ファイルシステムが夢を見ています",
    "注意：ネットワークが宇宙に旅立ちました",
    "深刻：マウスが反乱を企てています",
    "危険：ディスクが瞑想に入りました",
    "警告：プロセスが自己主張を始めました",
    "注意：システムクロックが逆走中",
    "重大：RAMが詩的表現を学習中",
    "警告：USBが異次元に消えました",
    "深刻：GPUが絵画を描いています",
    "注意：BIOSが人生相談を始めました"
]

def detect_os() -> str:
    if sys.platform.startswith('win'):
        return 'windows'
    elif sys.platform.startswith('darwin'):
        return 'macos'
    elif sys.platform.startswith('linux'):
        return 'linux'
    else:
        return 'unknown'

def send_notification(title: str, message: str):
    os_type = detect_os()
    if os_type == 'windows':
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=5, threaded=True)
        except ImportError:
            # Fallback: powershell
            script = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
            script += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
            script += f'$toastXml = $template;'
            script += f'$toastXml.GetElementsByTagName(\"text\")[0].AppendChild($toastXml.CreateTextNode(\"{title}\")) > $null;'
            script += f'$toastXml.GetElementsByTagName(\"text\")[1].AppendChild($toastXml.CreateTextNode(\"{message}\")) > $null;'
            script += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($toastXml);'
            script += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier(\"Desktop Chaos Alert\");'
            script += f'$notifier.Show($toast)'
            subprocess.run(["powershell", "-Command", script], shell=True)
    elif os_type == 'macos':
        script = f'display notification "{message}" with title "{title}"'
        subprocess.run(["osascript", "-e", script])
    elif os_type == 'linux':
        try:
            subprocess.run(["notify-send", title, message])
        except Exception:
            print(f"[通知] {title}: {message}")
    else:
        print(f"[通知] {title}: {message}")


def list_messages():
    print("=== カオス通知メッセージ一覧 ===")
    for idx, msg in enumerate(CHAOS_MESSAGES, 1):
        print(f"{idx:2d}: {msg}")


def show_random_alert(count: int = 1, interval: float = 1.5):
    for _ in range(count):
        msg = random.choice(CHAOS_MESSAGES)
        send_notification("謎のOS緊急アラート", msg)
        time.sleep(interval)


def show_all_alerts(interval: float = 1.2):
    for msg in CHAOS_MESSAGES:
        send_notification("謎のOS緊急アラート", msg)
        time.sleep(interval)


def parse_args():
    parser = argparse.ArgumentParser(description="謎のカオス通知をデスクトップに表示するスクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="ランダムなカオス通知を表示")
    parser_alert.add_argument("-n", "--number", type=int, default=1, help="通知の回数")
    parser_alert.add_argument("-i", "--interval", type=float, default=1.5, help="通知間隔(秒)")

    parser_all = subparsers.add_parser("all", help="全てのカオス通知を順番に表示")
    parser_all.add_argument("-i", "--interval", type=float, default=1.2, help="通知間隔(秒)")

    parser_list = subparsers.add_parser("list", help="カオス通知メッセージ一覧を表示")

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "alert":
        show_random_alert(count=args.number, interval=args.interval)
    elif args.command == "all":
        show_all_alerts(interval=args.interval)
    elif args.command == "list":
        list_messages()
    else:
        print("コマンドを指定してください (alert, all, list)。--help 参照。")

if __name__ == '__main__':
    main()
