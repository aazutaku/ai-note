import sys
import random
import time
import argparse
import platform
import threading

try:
    from plyer import notification
except ImportError:
    notification = None

SAMURAI_MESSAGES = [
    "拙者、Altキーの抜刀訓練状況を監視しておる。",
    "油断大敵、マウスの居合切りに注意せよ。",
    "本日も見事なEnter斬り、お見事に候。",
    "そなたのCtrl+Z、まさに奥義の域。",
    "画面切替の達人、拙者も舌を巻く。",
    "F5の連打、まるで風車の如し。",
    "CapsLockの誤爆、侍道においてはご法度なり。",
    "スクリーンショットの極意、心得ておるな。",
    "タスク切替の早業、拙者も見習いたい。",
    "Alt+Tabの居合抜き、見事なり。",
    "ファイル保存を怠るべからず。",
    "コピペの達人、拙者も驚嘆。",
    "静寂の中に刃あり、油断召されるな。",
    "そなたのウィンドウ整列、まさに武士の所作。",
    "マウスの軌跡、剣筋の如し。",
    "今日も一日、精進あるのみ。",
    "キーボードの打鍵、太刀筋に通ず。",
    "そなたのログイン、拙者見届けたり。",
    "パスワードの守り、城壁の如し。",
    "エラーに屈することなかれ、侍の道は険しきもの。"
]

ALERT_PREFIX = "[侍OS ALERT] "

LOG_FILE = "samurai_alert.log"


def send_notification(message):
    if notification:
        notification.notify(
            title="侍OS ALERT",
            message=message,
            timeout=5
        )
    else:
        print(f"{ALERT_PREFIX}{message}")


def log_message(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{timestamp} {ALERT_PREFIX}{message}\n")


def random_samurai_message():
    return random.choice(SAMURAI_MESSAGES)


def alert_once(log=False):
    message = random_samurai_message()
    send_notification(message)
    if log:
        log_message(message)


def alert_loop(interval, count, log):
    for i in range(count):
        alert_once(log)
        if i < count - 1:
            time.sleep(interval)


def list_log():
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[-10:]:
                print(line.strip())
    except FileNotFoundError:
        print("No alert log found.")


def summary_log():
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        total = len(lines)
        days = set(line[:10] for line in lines)
        print(f"Total alerts: {total}")
        print(f"Active days: {len(days)}")
    except FileNotFoundError:
        print("No alert log found.")


def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Ancient Samurai Alert')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='Send a random samurai alert')
    parser_alert.add_argument('--log', action='store_true', help='Log alert to file')
    parser_alert.add_argument('--count', type=int, default=1, help='Number of alerts to send')
    parser_alert.add_argument('--interval', type=int, default=10, help='Interval between alerts (seconds)')

    parser_list = subparsers.add_parser('list', help='Show last 10 alerts from log')
    parser_summary = subparsers.add_parser('summary', help='Show alert log summary')

    args = parser.parse_args()

    if args.command == 'alert':
        alert_loop(args.interval, args.count, args.log)
    elif args.command == 'list':
        list_log()
    elif args.command == 'summary':
        summary_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
