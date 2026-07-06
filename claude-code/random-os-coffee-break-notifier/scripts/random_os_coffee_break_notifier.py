import sys
import os
import random
import time
import argparse
import platform
import subprocess
from datetime import datetime, timedelta

def get_random_message():
    messages = [
        "重要：カフェイン補給の時刻です",
        "タスク進捗が停滞中。コーヒーを飲めとの神託",
        "AI的診断：あと5分で集中力が消滅します",
        "システム推奨：生産性維持のため、今すぐコーヒーブレイクを！",
        "注意：脳内カフェイン残量が閾値を下回りました",
        "OSからの警告：休憩しないと生産性が低下します",
        "AI観測：あなたの集中力は臨界点です。コーヒーをどうぞ",
        "推奨：今こそコーヒーでリフレッシュする時です",
        "システム診断：作業効率が下がっています。コーヒーブレイクを検討してください",
        "通知：コーヒーブレイクの時間がやってきました"
    ]
    return random.choice(messages)

def send_notification(message):
    system = platform.system()
    try:
        if system == "Darwin":
            # macOS
            script = f'display notification "{message}" with title "OS通知"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            # Linux (notify-send)
            subprocess.run(["notify-send", "OS通知", message], check=True)
        elif system == "Windows":
            # Windows 10+ (powershell toast)
            ps_script = f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null; " \
                        f"$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02); " \
                        f"$template.GetElementsByTagName('text')[0].AppendChild($template.CreateTextNode('OS通知')) > $null; " \
                        f"$template.GetElementsByTagName('text')[1].AppendChild($template.CreateTextNode('{message}')) > $null; " \
                        f"$toast = [Windows.UI.Notifications.ToastNotification]::new($template); " \
                        f"$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Python Script'); " \
                        f"$notifier.Show($toast)"
            subprocess.run([
                "powershell", "-Command", ps_script
            ], check=True)
        else:
            print(f"[OS通知] {message}")
    except Exception as e:
        print(f"[通知エラー] {e}\n[OS通知] {message}")

def random_wait(min_sec=300, max_sec=1800):
    wait_time = random.randint(min_sec, max_sec)
    time.sleep(wait_time)
    return wait_time

def run_notifier(count=3, min_interval=300, max_interval=1800):
    for i in range(count):
        message = get_random_message()
        send_notification(message)
        if i < count - 1:
            wait_time = random_wait(min_interval, max_interval)
        else:
            break

def cli():
    parser = argparse.ArgumentParser(description="Random OS Coffee Break Notifier")
    subparsers = parser.add_subparsers(dest="command")

    notify_parser = subparsers.add_parser("notify", help="今すぐランダム通知を1回表示")
    notify_parser.add_argument("-n", "--number", type=int, default=1, help="通知回数 (デフォルト1)")

    auto_parser = subparsers.add_parser("auto", help="ランダム間隔で複数回通知")
    auto_parser.add_argument("-n", "--number", type=int, default=3, help="通知回数 (デフォルト3)")
    auto_parser.add_argument("--min", type=int, default=300, help="最小間隔(秒)")
    auto_parser.add_argument("--max", type=int, default=1800, help="最大間隔(秒)")

    list_parser = subparsers.add_parser("list", help="通知候補メッセージ一覧を表示")

    args = parser.parse_args()
    if args.command == "notify":
        for _ in range(args.number):
            message = get_random_message()
            send_notification(message)
    elif args.command == "auto":
        run_notifier(count=args.number, min_interval=args.min, max_interval=args.max)
    elif args.command == "list":
        for m in [
            "重要：カフェイン補給の時刻です",
            "タスク進捗が停滞中。コーヒーを飲めとの神託",
            "AI的診断：あと5分で集中力が消滅します",
            "システム推奨：生産性維持のため、今すぐコーヒーブレイクを！",
            "注意：脳内カフェイン残量が閾値を下回りました",
            "OSからの警告：休憩しないと生産性が低下します",
            "AI観測：あなたの集中力は臨界点です。コーヒーをどうぞ",
            "推奨：今こそコーヒーでリフレッシュする時です",
            "システム診断：作業効率が下がっています。コーヒーブレイクを検討してください",
            "通知：コーヒーブレイクの時間がやってきました"
        ]:
            print(f"[OS通知] {m}")
    else:
        parser.print_help()

if __name__ == "__main__":
    cli()
