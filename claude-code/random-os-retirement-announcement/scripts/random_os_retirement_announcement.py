import random
import time
import sys
import argparse
import os
from datetime import datetime, timedelta
try:
    import notify2
except ImportError:
    notify2 = None

ANNOUNCEMENTS = [
    "通知: 本日をもってカーネル部長が勇退します。",
    "重要: ファイルシステムさんが第二の人生へ旅立ちます。",
    "急報: メモリ課長が早期リタイアを決意しました。",
    "速報: プロセス係長が退職し、シェル芸人を目指します。",
    "連絡: ネットワーク主任が新天地へ転職しました。",
    "告知: バッファ課長が定年を迎えました。",
    "訃報: デバイスドライバさんがOS界から去ります。",
    "発表: パーミッション係がキャリアチェンジします。",
    "特報: スケジューラ女史が起業のため退職。",
    "報告: ユーザーランドさんが長期休暇に入ります。"
]

LAST_ANNOUNCE_FILE = os.path.expanduser("~/.random_os_retirement_last")
MIN_INTERVAL = timedelta(hours=1)


def can_announce():
    if not os.path.exists(LAST_ANNOUNCE_FILE):
        return True
    try:
        with open(LAST_ANNOUNCE_FILE, 'r') as f:
            last = f.read().strip()
            last_dt = datetime.fromisoformat(last)
            if datetime.now() - last_dt >= MIN_INTERVAL:
                return True
    except Exception:
        return True
    return False


def update_last_announce():
    try:
        with open(LAST_ANNOUNCE_FILE, 'w') as f:
            f.write(datetime.now().isoformat())
    except Exception:
        pass


def random_announcement():
    return random.choice(ANNOUNCEMENTS)


def send_notification(message):
    if notify2:
        try:
            notify2.init("Random OS Retirement Announcement")
            n = notify2.Notification("OS退職アナウンス", message)
            n.set_urgency(notify2.URGENCY_NORMAL)
            n.show()
            return True
        except Exception:
            pass
    # Fallback: try notify-send
    try:
        os.system(f'notify-send "OS退職アナウンス" "{message}"')
        return True
    except Exception:
        pass
    return False


def log_announcement(message):
    log_file = os.path.expanduser("~/.random_os_retirement_log")
    with open(log_file, 'a') as f:
        f.write(f"{datetime.now().isoformat()}\t{message}\n")


def list_announcements():
    log_file = os.path.expanduser("~/.random_os_retirement_log")
    if not os.path.exists(log_file):
        print("No announcements logged yet.")
        return
    with open(log_file, 'r') as f:
        for line in f:
            print(line.strip())


def summary_announcements():
    log_file = os.path.expanduser("~/.random_os_retirement_log")
    if not os.path.exists(log_file):
        print("No announcements logged yet.")
        return
    counts = {}
    with open(log_file, 'r') as f:
        for line in f:
            msg = line.strip().split('\t', 1)[-1]
            counts[msg] = counts.get(msg, 0) + 1
    for msg, count in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{msg}: {count}回")


def run_announcement(force=False):
    if force or can_announce():
        msg = random_announcement()
        sent = send_notification(msg)
        if sent:
            update_last_announce()
            log_announcement(msg)
            print(f"[通知済] {msg}")
        else:
            print(f"[通知失敗] {msg}")
    else:
        print("[スキップ] 1時間以内に通知済みです。")


def main():
    parser = argparse.ArgumentParser(description="謎のOS退職アナウンスをランダム通知するスクリプト")
    subparsers = parser.add_subparsers(dest="command")

    ann_parser = subparsers.add_parser("announce", help="今すぐ退職アナウンスを通知")
    ann_parser.add_argument("--force", action="store_true", help="強制的に通知を出す（頻度制限無視）")

    list_parser = subparsers.add_parser("list", help="過去のアナウンス履歴を表示")
    summary_parser = subparsers.add_parser("summary", help="アナウンス内容ごとの集計")

    args = parser.parse_args()
    if args.command == "announce":
        run_announcement(force=args.force)
    elif args.command == "list":
        list_announcements()
    elif args.command == "summary":
        summary_announcements()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
