import sys
import os
import time
import random
import argparse
import platform
import subprocess
from datetime import datetime, timedelta

NOTIFICATION_MESSAGES = [
    "重要：カフェイン補給の時刻です。",
    "タスク進捗が停滞中。コーヒーを飲めとの神託。",
    "AI的診断：あと5分で集中力が消滅します。",
    "システムガイドライン：短い休憩を推奨します。",
    "OSリソース監視：コーヒーブレイクが必要です。",
    "バックグラウンドプロセス：コーヒーの香りを検出しました。",
    "メモリ使用率が閾値を超過。コーヒーでリフレッシュを推奨。",
    "CPU温度上昇中。冷却のためのコーヒーブレイクを開始してください。",
    "生産性向上アルゴリズム：今すぐコーヒータイム。",
    "OSアップデート：コーヒーブレイク推奨パッチ適用完了。"
]

HISTORY_FILE = os.path.expanduser("~/.coffee_break_notify_history.log")


def send_notification(message):
    system = platform.system()
    if system == "Darwin":
        # macOS
        script = f'display notification "{message}" with title "[通知] OSコーヒーブレイク"'
        subprocess.run(["osascript", "-e", script])
    elif system == "Linux":
        # Linux (notify-send)
        subprocess.run(["notify-send", "[通知] OSコーヒーブレイク", message])
    elif system == "Windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("[通知] OSコーヒーブレイク", message, duration=10)
        except ImportError:
            # Fallback: powershell toast
            powershell_command = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
            powershell_command += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
            powershell_command += f'$template.GetElementsByTagName("text")[0].AppendChild($template.CreateTextNode("[通知] OSコーヒーブレイク")) > $null;'
            powershell_command += f'$template.GetElementsByTagName("text")[1].AppendChild($template.CreateTextNode("{message}")) > $null;'
            powershell_command += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
            powershell_command += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("CoffeeBreakNotifier");'
            powershell_command += f'$notifier.Show($toast)'
            subprocess.run(["powershell", "-Command", powershell_command])
    else:
        print(f"[通知] {message}")


def log_history(message):
    timestamp = datetime.now().isoformat()
    with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{timestamp}\t{message}\n")


def list_history(limit=10):
    if not os.path.exists(HISTORY_FILE):
        print("通知履歴がありません。")
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines[-limit:]:
        print(line.strip())


def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("通知履歴がありません。")
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"合計通知回数: {len(lines)}")
    times = [datetime.fromisoformat(l.split('\t')[0]) for l in lines]
    if times:
        print(f"最初の通知: {times[0]}")
        print(f"最新の通知: {times[-1]}")


def random_interval(min_minutes=15, max_minutes=60):
    return random.randint(min_minutes * 60, max_minutes * 60)


def run_random_notifier(args):
    print("コーヒーブレイク通知をランダム間隔で開始します。Ctrl+Cで停止。")
    try:
        while True:
            wait_time = random_interval(args.min, args.max)
            time.sleep(wait_time)
            message = random.choice(NOTIFICATION_MESSAGES)
            send_notification(message)
            log_history(message)
    except KeyboardInterrupt:
        print("\nコーヒーブレイク通知を終了します。")


def manual_notify(args):
    message = random.choice(NOTIFICATION_MESSAGES)
    send_notification(message)
    log_history(message)
    print(f"通知送信: {message}")


def main():
    parser = argparse.ArgumentParser(description="OS風コーヒーブレイク通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="ランダムな間隔で通知を自動送信")
    parser_run.add_argument("--min", type=int, default=15, help="最小間隔(分)")
    parser_run.add_argument("--max", type=int, default=60, help="最大間隔(分)")
    parser_run.set_defaults(func=run_random_notifier)

    parser_notify = subparsers.add_parser("notify", help="今すぐランダム通知を1回送信")
    parser_notify.set_defaults(func=manual_notify)

    parser_list = subparsers.add_parser("list", help="通知履歴を表示")
    parser_list.add_argument("--limit", type=int, default=10, help="表示件数")
    parser_list.set_defaults(func=lambda args: list_history(args.limit))

    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリーを表示")
    parser_summary.set_defaults(func=lambda args: summary_history())

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
