import sys
import os
import random
import time
import argparse
import subprocess
from datetime import datetime, timedelta

CONFETTI_MESSAGES = [
    "本日も出社おめでとうございます！",
    "意味なく祝福します！",
    "さっきのls、最高でした！",
    "あなたのcd、華麗でした！",
    "git pullのタイミング、完璧です！",
    "何もしていなくても祝福します！",
    "今のあなた、きっと輝いています！",
    "祝：コマンド実行100回突破！",
    "特に理由はありませんが、おめでとう！",
    "この通知を見たあなたに幸運を！",
    "lsの使い方、プロ級です！",
    "今日も素晴らしいスキル選択です！",
    "意味不明な祝福をお届けします！",
    "たまには深呼吸しましょう！",
    "今こそコーヒーブレイクの時間です！",
    "祝：意味のない達成感！",
    "あなたの努力に紙吹雪を！",
    "何気ない瞬間に祝福を！",
    "今のあなたに拍手！",
    "作業の合間におめでとう！"
]

LAST_NOTIFICATION_FILE = os.path.expanduser("~/.random_os_notification_confetti_last")
MIN_INTERVAL_MINUTES = 10  # 最低通知間隔（分）


def get_platform():
    if sys.platform.startswith("win"):
        return "windows"
    elif sys.platform.startswith("darwin"):
        return "macos"
    elif sys.platform.startswith("linux"):
        return "linux"
    else:
        return "unknown"


def can_notify():
    platform = get_platform()
    if platform == "windows":
        try:
            import win10toast
            return True
        except ImportError:
            return False
    elif platform == "macos":
        return True  # osascriptは標準搭載
    elif platform == "linux":
        return shutil.which("notify-send") is not None
    else:
        return False


def send_notification(message):
    platform = get_platform()
    if platform == "windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("祝福", message, duration=5, threaded=True)
        except ImportError:
            print("win10toastがインストールされていません。pip install win10toast で導入してください。")
    elif platform == "macos":
        script = f'display notification "{message}" with title "祝福"'
        subprocess.run(["osascript", "-e", script], check=False)
    elif platform == "linux":
        subprocess.run(["notify-send", "祝福", message], check=False)
    else:
        print(f"[祝福] {message}")


def is_time_to_notify():
    if not os.path.exists(LAST_NOTIFICATION_FILE):
        return True
    try:
        with open(LAST_NOTIFICATION_FILE, "r") as f:
            last = f.read().strip()
            last_time = datetime.fromisoformat(last)
        now = datetime.now()
        return (now - last_time) > timedelta(minutes=MIN_INTERVAL_MINUTES)
    except Exception:
        return True


def update_last_notification_time():
    try:
        with open(LAST_NOTIFICATION_FILE, "w") as f:
            f.write(datetime.now().isoformat())
    except Exception:
        pass


def get_random_message():
    return random.choice(CONFETTI_MESSAGES)


def log_event(message):
    log_file = os.path.expanduser("~/.random_os_notification_confetti_log")
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now().isoformat()}\t{message}\n")
    except Exception:
        pass


def list_log():
    log_file = os.path.expanduser("~/.random_os_notification_confetti_log")
    if not os.path.exists(log_file):
        print("ログがありません。")
        return
    with open(log_file, "r") as f:
        for line in f:
            print(line.strip())


def summary_log():
    log_file = os.path.expanduser("~/.random_os_notification_confetti_log")
    if not os.path.exists(log_file):
        print("ログがありません。")
        return
    count = 0
    with open(log_file, "r") as f:
        for _ in f:
            count += 1
    print(f"これまでに {count} 回祝福されました！")


def explicit_notify():
    message = get_random_message()
    send_notification(message)
    log_event(message)
    update_last_notification_time()
    print(f"[祝福] {message}")


def maybe_notify():
    if is_time_to_notify():
        explicit_notify()
    else:
        print("（まだ祝福のタイミングではありません）")


def main():
    parser = argparse.ArgumentParser(description="完全ランダムな祝福通知をOSの通知領域に表示します。")
    subparsers = parser.add_subparsers(dest="command")

    parser_notify = subparsers.add_parser("notify", help="今すぐ祝福通知を表示")
    parser_maybe = subparsers.add_parser("maybe", help="一定間隔ごとにだけ祝福通知を表示")
    parser_list = subparsers.add_parser("list", help="祝福ログを表示")
    parser_summary = subparsers.add_parser("summary", help="祝福回数サマリーを表示")

    args = parser.parse_args()

    if args.command == "notify":
        explicit_notify()
    elif args.command == "maybe":
        maybe_notify()
    elif args.command == "list":
        list_log()
    elif args.command == "summary":
        summary_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
