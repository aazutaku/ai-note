import sys
import os
import random
import time
import argparse
import platform
import subprocess
from datetime import datetime, timedelta

FAKE_ALERTS = [
    "危険：未知のバグウイルスを検出しました！",
    "注意：あなたのコードが自我を持ちました。今すぐ休憩を推奨します。",
    "システム警告：AIがあなたの冗談を理解できませんでした。",
    "お知らせ：バグが自己増殖を開始しました（嘘です）。",
    "警告：あなたのコーヒー残量が危険水域です。",
    "注意：デバッグのしすぎで現実世界にバグが侵入しました。",
    "警告：あなたのPCが笑いすぎて処理速度が低下しています。",
    "重大：コード内に『やる気』が見つかりませんでした。",
    "注意：この通知は完全にジョークです。安心してください。",
    "警告：バグがバグを呼び寄せています。"
]

LOG_FILE = os.path.expanduser("~/.random_os_fake_virus_alert.log")


def send_notification(message):
    system = platform.system()
    try:
        if system == "Windows":
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("Fake Virus Alert", message, duration=5, threaded=True)
        elif system == "Darwin":
            script = f'display notification "{message}" with title "Fake Virus Alert"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            subprocess.run(["notify-send", "Fake Virus Alert", message], check=True)
        else:
            print(f"[通知] {message}")
    except Exception as e:
        print(f"[通知失敗] {message} ({e})")


def log_alert(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()}\t{message}\n")


def list_alerts(limit=20):
    if not os.path.exists(LOG_FILE):
        print("まだ通知履歴はありません。")
        return
    with open(LOG_FILE, encoding="utf-8") as f:
        lines = f.readlines()[-limit:]
        for line in lines:
            print(line.strip())


def summary_alerts():
    if not os.path.exists(LOG_FILE):
        print("まだ通知履歴はありません。")
        return
    count = 0
    recent = None
    with open(LOG_FILE, encoding="utf-8") as f:
        for line in f:
            count += 1
            recent = line.strip()
    print(f"合計通知回数: {count}")
    if recent:
        print(f"最新通知: {recent}")


def random_alert():
    message = random.choice(FAKE_ALERTS)
    send_notification(message)
    log_alert(message)
    print(f"[通知] {message}")


def auto_mode(interval_min=30, interval_max=90):
    print(f"自動モード開始: {interval_min}-{interval_max}分ごとにランダム通知")
    try:
        while True:
            wait = random.randint(interval_min * 60, interval_max * 60)
            time.sleep(wait)
            random_alert()
    except KeyboardInterrupt:
        print("自動モード終了")


def parse_args():
    parser = argparse.ArgumentParser(description="ランダムなジョークウイルス通知を表示します")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("alert", help="今すぐランダム通知を表示")
    auto = subparsers.add_parser("auto", help="自動で定期的に通知を表示")
    auto.add_argument("--min", type=int, default=30, help="最小間隔(分)")
    auto.add_argument("--max", type=int, default=90, help="最大間隔(分)")
    subparsers.add_parser("list", help="通知履歴を表示")
    subparsers.add_parser("summary", help="通知履歴のサマリーを表示")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "alert":
        random_alert()
    elif args.command == "auto":
        auto_mode(args.min, args.max)
    elif args.command == "list":
        list_alerts()
    elif args.command == "summary":
        summary_alerts()
    else:
        print("使い方: python random_os_fake_virus_alert.py [alert|auto|list|summary]")

if __name__ == "__main__":
    main()
