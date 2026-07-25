import random
import time
import sys
import argparse
from datetime import datetime, timedelta
try:
    from plyer import notification
except ImportError:
    notification = None

HOLIDAY_MESSAGES = [
    "OS公式発表: 本日はバグ記念日につき全業務停止となります。",
    "緊急: システム都合により午後は強制昼寝タイムです。",
    "OSが自主休暇を宣言しました。作業はおやすみです。",
    "本日は“無限リファクタ記念日”のため全プロセス休止。",
    "祝・仮想メモリ拡張記念日！午後は自由時間です。",
    "本日は“仮想デスクトップ解放記念日”のため作業停止。",
    "OSアップデート記念日: 今日は全員お休みです。",
    "システム都合: 本日は強制的に休憩時間となります。",
    "緊急: OSが予期せぬ休暇モードに入りました。",
    "祝・デバッグ成功記念日！本日は全業務停止。",
    "メモリ解放記念日: 午後は自由行動です。",
    "OSの気まぐれにより本日は休日となりました。",
    "本日は“プロセス優先度ゼロ記念日”です。",
    "OSが勝手に祝日を制定しました。",
    "本日は“仮想空間拡張記念日”のため作業中止。"
]

NOTIFY_TITLE = "[通知]"

LOG_FILE = ".os_fake_holiday_announcer.log"


def send_notification(message):
    if notification:
        notification.notify(
            title=NOTIFY_TITLE,
            message=message,
            timeout=8
        )
    else:
        print(f"{NOTIFY_TITLE} {message}")


def log_message(message):
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\t{message}\n")


def pick_random_message():
    return random.choice(HOLIDAY_MESSAGES)


def should_trigger(last_triggered, min_interval_minutes=60):
    now = datetime.now()
    if last_triggered is None:
        return True
    return (now - last_triggered) > timedelta(minutes=min_interval_minutes)


def get_last_trigger_time():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                return None
            last_line = lines[-1]
            timestamp = last_line.split("\t")[0]
            return datetime.fromisoformat(timestamp)
    except Exception:
        return None


def announce():
    message = pick_random_message()
    send_notification(message)
    log_message(message)


def list_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("ログが存在しません。まだ通知はありません。")


def summary():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            count = len(lines)
            print(f"これまでの架空休日通知回数: {count}")
            if count > 0:
                print("最新の通知:")
                print(lines[-1].strip())
    except FileNotFoundError:
        print("ログが存在しません。まだ通知はありません。")


def main():
    parser = argparse.ArgumentParser(description="OS Fake Holiday Announcer")
    subparsers = parser.add_subparsers(dest="command")

    parser_announce = subparsers.add_parser("announce", help="今すぐ架空休日通知を表示")
    parser_list = subparsers.add_parser("list", help="過去の通知ログを表示")
    parser_summary = subparsers.add_parser("summary", help="通知回数と最新通知を表示")
    parser_daemon = subparsers.add_parser("daemon", help="定期的に自動通知 (バックグラウンド用)")
    parser_daemon.add_argument("--min-interval", type=int, default=120, help="通知の最小間隔(分)")
    parser_daemon.add_argument("--max-interval", type=int, default=360, help="通知の最大間隔(分)")

    args = parser.parse_args()

    if args.command == "announce":
        announce()
    elif args.command == "list":
        list_log()
    elif args.command == "summary":
        summary()
    elif args.command == "daemon":
        min_interval = args.min_interval
        max_interval = args.max_interval
        print(f"OS Fake Holiday Announcer: {min_interval}〜{max_interval}分ごとにランダム通知します。Ctrl+Cで終了。")
        try:
            while True:
                last_time = get_last_trigger_time()
                if should_trigger(last_time, min_interval):
                    announce()
                sleep_time = random.randint(min_interval*60, max_interval*60)
                time.sleep(sleep_time)
        except KeyboardInterrupt:
            print("\n自動通知を終了します。")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
