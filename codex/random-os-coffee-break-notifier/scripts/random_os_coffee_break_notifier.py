import sys
import os
import random
import time
import argparse
import platform
import subprocess
from datetime import datetime, timedelta

MESSAGES = [
    "重要: カフェイン補給の時刻です",
    "タスク進捗が停滞中。コーヒーを飲めとの神託",
    "AI的診断: あと5分で集中力が消滅します",
    "OSセキュリティ警告: 休憩しないと危険です",
    "システム最適化: コーヒーブレイクの推奨",
    "推奨: いま飲まないと後悔するかも知れません",
    "CPU温度上昇: コーヒーで冷却を推奨",
    "仮想メモリ不足: カフェインで補給してください",
    "AI監査: 休憩頻度が低すぎます",
    "OSアップデート: コーヒーブレイクが必要です"
]

NOTIFIER_TITLE = "[通知]"

class Notifier:
    def __init__(self):
        self.os_type = platform.system()

    def send(self, message):
        if self.os_type == "Windows":
            self._windows_notify(message)
        elif self.os_type == "Darwin":
            self._mac_notify(message)
        elif self.os_type == "Linux":
            self._linux_notify(message)
        else:
            print(f"{NOTIFIER_TITLE} {message}")

    def _windows_notify(self, message):
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("OSからのお知らせ", message, duration=8)
        except ImportError:
            # Fallback: powershell
            script = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
            script += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
            script += f'$textNodes = $template.GetElementsByTagName("text");'
            script += f'$textNodes.Item(0).AppendChild($template.CreateTextNode("OSからのお知らせ")) > $null;'
            script += f'$textNodes.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null;'
            script += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
            script += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("Python") ;'
            script += f'$notifier.Show($toast)'
            subprocess.Popen(["powershell", "-Command", script], shell=True)

    def _mac_notify(self, message):
        script = f'display notification "{message}" with title "OSからのお知らせ"'
        subprocess.call(["osascript", "-e", script])

    def _linux_notify(self, message):
        try:
            subprocess.call([
                "notify-send", "OSからのお知らせ", message, "-t", "8000"
            ])
        except Exception:
            print(f"{NOTIFIER_TITLE} {message}")


def random_interval(min_sec=900, max_sec=3600):
    return random.randint(min_sec, max_sec)

def pick_random_message():
    return random.choice(MESSAGES)

def log_event(message):
    log_path = os.path.expanduser("~/.random_os_coffee_break.log")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")

def list_log():
    log_path = os.path.expanduser("~/.random_os_coffee_break.log")
    if not os.path.exists(log_path):
        print("ログがありません。")
        return
    with open(log_path, encoding="utf-8") as f:
        for line in f:
            print(line.strip())

def summary_log():
    log_path = os.path.expanduser("~/.random_os_coffee_break.log")
    if not os.path.exists(log_path):
        print("ログがありません。")
        return
    count = 0
    first = None
    last = None
    with open(log_path, encoding="utf-8") as f:
        for line in f:
            count += 1
            ts = line.split("]")[0][1:]
            if not first:
                first = ts
            last = ts
    print(f"通知回数: {count}")
    if first and last:
        print(f"期間: {first} ～ {last}")

def run_random_notifier(args):
    notifier = Notifier()
    print("ランダムOSコーヒーブレイク通知を開始します。Ctrl+Cで終了。")
    try:
        while True:
            interval = random_interval(args.min_interval, args.max_interval)
            time.sleep(interval)
            message = pick_random_message()
            notifier.send(message)
            log_event(message)
    except KeyboardInterrupt:
        print("\n通知を終了しました。")

def send_once(args):
    notifier = Notifier()
    message = pick_random_message()
    notifier.send(message)
    log_event(message)
    print(f"通知を1回送信しました: {message}")

def main():
    parser = argparse.ArgumentParser(description="OS風コーヒーブレイク通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="ランダムな間隔で通知を表示")
    parser_run.add_argument("--min-interval", type=int, default=900, help="通知間隔の最小秒数 (デフォルト: 900)")
    parser_run.add_argument("--max-interval", type=int, default=3600, help="通知間隔の最大秒数 (デフォルト: 3600)")

    parser_once = subparsers.add_parser("once", help="1回だけ通知を表示")

    parser_list = subparsers.add_parser("list", help="通知ログを表示")
    parser_summary = subparsers.add_parser("summary", help="通知履歴の要約を表示")

    args = parser.parse_args()

    if args.command == "run":
        run_random_notifier(args)
    elif args.command == "once":
        send_once(args)
    elif args.command == "list":
        list_log()
    elif args.command == "summary":
        summary_log()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
