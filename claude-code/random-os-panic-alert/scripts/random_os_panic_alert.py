import sys
import os
import time
import random
import argparse
import platform
import subprocess
from datetime import datetime, timedelta

PANIC_MESSAGES = [
    "カーネルがランチに出ました。再起動は不要です。",
    "ビットが逃走しました。追跡は不要です。",
    "仮想メモリが現実逃避中です。作業は続行できます。",
    "システムクロックが昼寝中です。時間を気にせず作業してください。",
    "ファイルシステムが詩を書き始めました。保存は自動です。",
    "プロセスIDが迷子になりました。探す必要はありません。",
    "スワップ領域が夢を見ています。現実に戻す必要はありません。",
    "ユーザー権限が自我に目覚めました。特に問題ありません。",
    "ネットワークスタックが散歩中です。通信は正常です。",
    "デバイスドライバがコーヒーブレイクに入りました。安全です。"
]

LOG_FILE = os.path.expanduser("~/.random_os_panic_alert.log")
NOTIFY_TITLE = "OS Panic Alert"


def send_notification(message):
    system = platform.system()
    if system == "Darwin":
        # macOS: AppleScript
        script = f'display notification "{message}" with title "{NOTIFY_TITLE}"'
        subprocess.run(["osascript", "-e", script], check=False)
    elif system == "Linux":
        # Linux: notify-send
        subprocess.run(["notify-send", NOTIFY_TITLE, message], check=False)
    elif system == "Windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(NOTIFY_TITLE, message, duration=7)
        except ImportError:
            # Fallback: powershell toast
            powershell_script = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
            powershell_script += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
            powershell_script += f'$textNodes = $template.GetElementsByTagName("text");'
            powershell_script += f'$textNodes.Item(0).AppendChild($template.CreateTextNode("{NOTIFY_TITLE}")) > $null;'
            powershell_script += f'$textNodes.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null;'
            powershell_script += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
            powershell_script += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("random-os-panic-alert");'
            powershell_script += f'$notifier.Show($toast);'
            subprocess.run(["powershell", "-Command", powershell_script], check=False)
    else:
        print(f"[{NOTIFY_TITLE}] {message}")


def log_alert(message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{now}] {message}\n")


def list_logs():
    if not os.path.exists(LOG_FILE):
        print("No alert logs found.")
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.rstrip())


def summary_logs():
    if not os.path.exists(LOG_FILE):
        print("No alert logs found.")
        return
    count = 0
    last_alert = None
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            count += 1
            last_alert = line.rstrip()
    print(f"Total alerts: {count}")
    if last_alert:
        print(f"Last alert: {last_alert}")


def pick_random_message():
    return random.choice(PANIC_MESSAGES)


def should_send_alert(min_interval_minutes=60):
    if not os.path.exists(LOG_FILE):
        return True
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if not lines:
                return True
            last_line = lines[-1]
            ts_str = last_line.split(']')[0][1:]
            last_time = datetime.strptime(ts_str, '%Y-%m-%d %H:%M:%S')
            if datetime.now() - last_time > timedelta(minutes=min_interval_minutes):
                return True
    except Exception:
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description='Random OS Panic Alert Notifier')
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    parser_alert = subparsers.add_parser('alert', help='Send a random OS panic alert')
    parser_alert.add_argument('--force', action='store_true', help='Force alert regardless of interval')
    parser_alert.add_argument('--interval', type=int, default=60, help='Minimum interval (minutes) between alerts')

    parser_list = subparsers.add_parser('list', help='List alert logs')
    parser_summary = subparsers.add_parser('summary', help='Show alert summary')
    parser_random = subparsers.add_parser('random', help='Show a random alert message (no notification)')

    args = parser.parse_args()

    if args.command == 'alert':
        if args.force or should_send_alert(args.interval):
            msg = pick_random_message()
            send_notification(msg)
            log_alert(msg)
            print(f"[{NOTIFY_TITLE}] {msg}")
        else:
            print("Alert skipped: Minimum interval not reached.")
    elif args.command == 'list':
        list_logs()
    elif args.command == 'summary':
        summary_logs()
    elif args.command == 'random':
        msg = pick_random_message()
        print(f"[{NOTIFY_TITLE}] {msg}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
