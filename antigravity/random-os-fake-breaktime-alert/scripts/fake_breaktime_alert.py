import sys
import os
import random
import time
import argparse
import platform
from datetime import datetime, timedelta

NOTIFICATIONS = [
    "肩回しタイム発動：今すぐ肩をぐるぐる回してください。",
    "OS推奨：5分間ぼーっとするべし。",
    "緊急！脳内メモリ休息モードに移行します。",
    "画面を見つめすぎです。深呼吸しましょう。",
    "システム推奨：今だけコーヒーブレイク！",
    "OS警告：まばたき回数が少なすぎます。",
    "自動判定：立ち上がってストレッチを推奨。",
    "OS診断：集中力が限界です。休憩を！",
    "謎のメッセージ：今こそ窓の外を眺める時。",
    "OS通知：意味不明な休憩タイム開始。"
]

HISTORY_FILE = os.path.expanduser("~/.fake_breaktime_alert_history")


def send_notification(message):
    system = platform.system()
    if system == "Darwin":  # macOS
        os.system(f'''osascript -e 'display notification "{message}" with title "OS通知"''')
    elif system == "Linux":
        os.system(f'notify-send "OS通知" "{message}"')
    elif system == "Windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("OS通知", message, duration=6)
        except ImportError:
            print("win10toastが必要です: pip install win10toast")
    else:
        print(f"[OS通知] {message}")


def log_history(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\t{message}\n")


def list_history(limit=10):
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[-limit:]:
            print(line.strip())


def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    count = 0
    messages = {}
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        for line in f:
            count += 1
            msg = line.strip().split("\t", 1)[-1]
            messages[msg] = messages.get(msg, 0) + 1
    print(f"合計通知回数: {count}")
    print("メッセージ別発動回数:")
    for msg, cnt in sorted(messages.items(), key=lambda x: -x[1]):
        print(f"- {msg}: {cnt}回")


def random_interval(min_sec=900, max_sec=3600):
    return random.randint(min_sec, max_sec)


def auto_mode(args):
    print("[INFO] 自動モード開始。Ctrl+Cで停止します。")
    try:
        while True:
            interval = random_interval(args.min_interval, args.max_interval)
            time.sleep(interval)
            message = random.choice(NOTIFICATIONS)
            send_notification(message)
            log_history(message)
    except KeyboardInterrupt:
        print("\n[INFO] 停止しました。")


def manual_mode(args):
    message = random.choice(NOTIFICATIONS)
    send_notification(message)
    log_history(message)
    print(f"[OS通知] {message}")


def parse_args():
    parser = argparse.ArgumentParser(description="謎のOS偽・強制休憩通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    auto_parser = subparsers.add_parser("auto", help="自動で定期的に通知を表示")
    auto_parser.add_argument("--min-interval", type=int, default=900, help="通知間隔の最小秒数 (デフォルト: 900)")
    auto_parser.add_argument("--max-interval", type=int, default=3600, help="通知間隔の最大秒数 (デフォルト: 3600)")

    manual_parser = subparsers.add_parser("once", help="1回だけ通知を表示")

    list_parser = subparsers.add_parser("list", help="通知履歴を表示")
    list_parser.add_argument("--limit", type=int, default=10, help="表示件数 (デフォルト10件)")

    summary_parser = subparsers.add_parser("summary", help="通知履歴のサマリーを表示")

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "auto":
        auto_mode(args)
    elif args.command == "once":
        manual_mode(args)
    elif args.command == "list":
        list_history(args.limit)
    elif args.command == "summary":
        summary_history()
    else:
        print("コマンドを指定してください (auto/once/list/summary)。")

if __name__ == "__main__":
    main()
