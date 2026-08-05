import sys
import os
import random
import time
import argparse
import platform
import subprocess
from datetime import datetime

FAKE_ALERTS = [
    "重要：AIがOS制御権を主張中",
    "カーネル領域がAIにより再編成されました",
    "AI委員会による再起動審議開始",
    "AIプロトコルがシステム設定を上書きしました",
    "注意：AIが管理者権限を要求しています",
    "AIによるリソース最適化が進行中",
    "AIがセキュリティポリシーを再定義しました",
    "システム再起動がAIによりスケジュールされました",
    "AIがユーザーセッションを監視中",
    "AIによるプロセス優先度調整が適用されました",
    "AI監査ログが生成されました",
    "AIがネットワーク構成を変更しました",
    "AI委員会による権限移譲プロセス開始",
    "AIによるダークモード強制適用",
    "AIがファームウェアをアップデートしました"
]

HISTORY_FILE = os.path.expanduser("~/.fake_ai_alert_history.log")


def send_notification(title, message):
    system = platform.system()
    try:
        if system == "Darwin":
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            subprocess.run(["notify-send", title, message], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=6)
            except ImportError:
                # fallback: use powershell
                ps_command = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
                ps_command += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
                ps_command += f'$template.GetElementsByTagName("text")[0].AppendChild($template.CreateTextNode("{title}")) > $null;'
                ps_command += f'$template.GetElementsByTagName("text")[1].AppendChild($template.CreateTextNode("{message}")) > $null;'
                ps_command += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
                ps_command += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("FakeAI");'
                ps_command += f'$notifier.Show($toast)'
                subprocess.run(["powershell", "-Command", ps_command], check=True)
        else:
            print(f"[通知] {title}: {message}")
    except Exception as e:
        print(f"[通知失敗] {title}: {message} ({e})")


def random_alert_message():
    return random.choice(FAKE_ALERTS)


def log_alert(message):
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()} {message}\n")
    except Exception as e:
        pass  # ログ失敗は無視


def list_alerts(limit=10):
    if not os.path.exists(HISTORY_FILE):
        print("履歴ファイルがありません。")
        return
    with open(HISTORY_FILE, encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines[-limit:]:
        print(line.strip())


def summary_alerts():
    if not os.path.exists(HISTORY_FILE):
        print("履歴ファイルがありません。")
        return
    counts = {}
    with open(HISTORY_FILE, encoding="utf-8") as f:
        for line in f:
            msg = line.strip().split(" ", 1)[-1]
            counts[msg] = counts.get(msg, 0) + 1
    print("--- 通知メッセージ出現回数 ---")
    for msg, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{msg}: {cnt}回")


def run_alert_loop(interval, max_count):
    count = 0
    while max_count is None or count < max_count:
        msg = random_alert_message()
        send_notification("AIによるOS警告", msg)
        log_alert(msg)
        count += 1
        sleep_time = interval + random.randint(-interval//3, interval//2)
        if sleep_time < 2:
            sleep_time = 2
        time.sleep(sleep_time)


def main():
    parser = argparse.ArgumentParser(description="AIによるOSジャック警告をランダム通知するスクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="ランダム通知を開始")
    parser_run.add_argument("--interval", type=int, default=300, help="通知間隔(秒)")
    parser_run.add_argument("--max", type=int, default=None, help="最大通知回数")

    parser_alert = subparsers.add_parser("alert", help="1回だけ通知を表示")
    parser_list = subparsers.add_parser("list", help="通知履歴を表示")
    parser_list.add_argument("--limit", type=int, default=10, help="表示件数")
    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリー")

    args = parser.parse_args()

    if args.command == "run":
        run_alert_loop(args.interval, args.max)
    elif args.command == "alert":
        msg = random_alert_message()
        send_notification("AIによるOS警告", msg)
        log_alert(msg)
        print(f"[通知] {msg}")
    elif args.command == "list":
        list_alerts(args.limit)
    elif args.command == "summary":
        summary_alerts()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
