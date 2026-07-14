import sys
import os
import platform
import random
import time
import argparse
import subprocess
from datetime import datetime

APOLOGY_MESSAGES = [
    "本日はご迷惑をおかけしております。詳細は不明ですが、引き続きご理解ください。",
    "謎の遅延が発生しましたが、原因不明です。ご不便をおかけします。",
    "大変申し訳ありませんが、さっきのコマンドは無かったことにしてください。",
    "予期せぬ問題が発生しましたが、何も対応しません。",
    "システムは正常ですが、念のためお詫び申し上げます。",
    "原因不明のエラーが発生した可能性があります。詳細は不明です。",
    "本件については調査中ですが、特に何もしていません。ご容赦ください。",
    "ご迷惑をおかけしておりますが、特に問題はありません。",
    "システムは正常に動作していますが、お詫び申し上げます。",
    "本日のご利用に感謝しつつ、無責任に謝罪いたします。"
]

LOG_FILE = os.path.expanduser("~/.random_os_apology_notifier.log")


def send_notification(message):
    system = platform.system()
    if system == "Darwin":
        # macOS: use AppleScript
        script = f'display notification "{message}" with title "通知"'
        try:
            subprocess.run(["osascript", "-e", script], check=True)
        except Exception as e:
            print(f"[ERROR] macOS通知失敗: {e}")
    elif system == "Linux":
        # Linux: use notify-send
        try:
            subprocess.run(["notify-send", "通知", message], check=True)
        except Exception as e:
            print(f"[ERROR] Linux通知失敗: {e}")
    elif system == "Windows":
        # Windows: use Toast notification
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast("通知", message, duration=5, threaded=True)
        except ImportError:
            # Fallback: powershell
            try:
                script = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
                script += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
                script += f'$toastXml = $template;'
                script += f'$toastXml.GetElementsByTagName("text")[0].AppendChild($toastXml.CreateTextNode("通知")) > $null;'
                script += f'$toastXml.GetElementsByTagName("text")[1].AppendChild($toastXml.CreateTextNode("{message}")) > $null;'
                script += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($toastXml);'
                script += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("random-os-apology-notifier");'
                script += f'$notifier.Show($toast);'
                subprocess.run(["powershell", "-Command", script], check=True)
            except Exception as e2:
                print(f"[ERROR] Windows通知失敗: {e2}")
    else:
        print(f"[通知] {message}")


def log_message(message):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()}\t{message}\n")
    except Exception as e:
        print(f"[ERROR] ログ保存失敗: {e}")


def list_logs(limit=20):
    try:
        if not os.path.exists(LOG_FILE):
            print("ログファイルが存在しません。")
            return
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[-limit:]:
                print(line.strip())
    except Exception as e:
        print(f"[ERROR] ログ読み込み失敗: {e}")


def summary_logs():
    try:
        if not os.path.exists(LOG_FILE):
            print("ログファイルが存在しません。")
            return
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"総通知回数: {len(lines)}")
        counts = {}
        for line in lines:
            msg = line.strip().split("\t", 1)[-1]
            counts[msg] = counts.get(msg, 0) + 1
        print("頻出メッセージ:")
        for msg, cnt in sorted(counts.items(), key=lambda x: -x[1])[:5]:
            print(f"  {msg} : {cnt}回")
    except Exception as e:
        print(f"[ERROR] サマリー取得失敗: {e}")


def notify_once():
    message = random.choice(APOLOGY_MESSAGES)
    send_notification(message)
    log_message(message)
    print(f"[通知] {message}")


def notify_loop(interval_min=600, interval_max=1800):
    print(f"ランダム謝罪通知を開始します (間隔: {interval_min//60}-{interval_max//60}分)。Ctrl+Cで終了。")
    try:
        while True:
            delay = random.randint(interval_min, interval_max)
            time.sleep(delay)
            notify_once()
    except KeyboardInterrupt:
        print("\n[INFO] 通知ループを終了しました。")


def main():
    parser = argparse.ArgumentParser(description="random-os-apology-notifier: OS風のフェイク謝罪通知をランダム表示")
    subparsers = parser.add_subparsers(dest="command")

    parser_notify = subparsers.add_parser("notify", help="1回だけ謝罪通知を表示")
    parser_loop = subparsers.add_parser("loop", help="ランダム間隔で謝罪通知を繰り返し表示")
    parser_loop.add_argument("--min", type=int, default=600, help="最短通知間隔(秒)")
    parser_loop.add_argument("--max", type=int, default=1800, help="最長通知間隔(秒)")
    parser_list = subparsers.add_parser("list", help="通知ログを最新20件表示")
    parser_list.add_argument("--limit", type=int, default=20, help="表示件数")
    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリーを表示")

    args = parser.parse_args()
    if args.command == "notify":
        notify_once()
    elif args.command == "loop":
        notify_loop(interval_min=args.min, interval_max=args.max)
    elif args.command == "list":
        list_logs(limit=args.limit)
    elif args.command == "summary":
        summary_logs()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
