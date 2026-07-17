import sys
import os
import random
import time
import argparse
from datetime import datetime, timedelta
try:
    from plyer import notification
except ImportError:
    notification = None

ANNOUNCEMENT_TEMPLATES = [
    "重要：本日をもって{role}{name}が勇退します。",
    "通知：{role}{name}さんが第二の人生へ。",
    "急報：{role}{name}が早期リタイアを決意。",
    "お知らせ：{role}{name}が新天地へ旅立ちます。",
    "本日付で{role}{name}が退職されました。",
    "速報：{role}{name}が転職活動を始めました。",
    "訃報：{role}{name}がシステムを去ります。",
    "告知：{role}{name}が本日付で異動となります。",
    "ご連絡：{role}{name}が長期休暇に入ります。",
    "ニュース：{role}{name}が定年退職となりました。"
]

ROLES = [
    "カーネル部長",
    "メモリ課長",
    "ファイルシステムさん",
    "プロセス主任",
    "ネットワーク係長",
    "デバイス管理者",
    "シェル先輩",
    "スケジューラ先生",
    "ドライバ君",
    "ユーザー空間代表"
]

NAMES = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    ""
]  # 名前は役職名に含まれるので空文字

STATE_FILE = os.path.expanduser("~/.os_retirement_announcement_state")


def can_notify():
    if not notification:
        return False
    # 環境変数やDISPLAYの有無で通知可能か簡易判定
    if sys.platform.startswith('linux') and not os.environ.get('DISPLAY'):
        return False
    return True


def read_last_notify_time():
    if not os.path.exists(STATE_FILE):
        return None
    try:
        with open(STATE_FILE, 'r') as f:
            ts = f.read().strip()
            if ts:
                return datetime.fromisoformat(ts)
    except Exception:
        return None
    return None


def write_last_notify_time(dt):
    try:
        with open(STATE_FILE, 'w') as f:
            f.write(dt.isoformat())
    except Exception:
        pass


def generate_announcement():
    template = random.choice(ANNOUNCEMENT_TEMPLATES)
    role = random.choice(ROLES)
    name = random.choice(NAMES)
    return template.format(role=role, name=name)


def notify_announcement(msg):
    if not can_notify():
        print("[通知不可]", msg)
        return
    try:
        notification.notify(
            title="[通知]",
            message=msg,
            app_name="OS Retirement Announcement",
            timeout=8
        )
    except Exception as e:
        print("[通知失敗]", msg)


def log_announcement(msg):
    log_file = os.path.expanduser("~/.os_retirement_announcement.log")
    try:
        with open(log_file, 'a') as f:
            f.write(f"{datetime.now().isoformat()} {msg}\n")
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(description="Random OS Retirement Announcement Skill")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser('log', help='通知を即時発火しログに記録')
    parser_list = subparsers.add_parser('list', help='過去の通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知履歴のサマリ集計')

    args = parser.parse_args()

    if args.command == 'log':
        msg = generate_announcement()
        notify_announcement(msg)
        log_announcement(msg)
        write_last_notify_time(datetime.now())
        print(msg)
        return
    elif args.command == 'list':
        log_file = os.path.expanduser("~/.os_retirement_announcement.log")
        if not os.path.exists(log_file):
            print("通知履歴はありません。")
            return
        with open(log_file, 'r') as f:
            lines = f.readlines()
            for line in lines[-20:]:
                print(line.strip())
        return
    elif args.command == 'summary':
        log_file = os.path.expanduser("~/.os_retirement_announcement.log")
        if not os.path.exists(log_file):
            print("通知履歴はありません。")
            return
        role_count = {}
        with open(log_file, 'r') as f:
            for line in f:
                for role in ROLES:
                    if role in line:
                        role_count[role] = role_count.get(role, 0) + 1
        print("役職別通知回数:")
        for role, count in sorted(role_count.items(), key=lambda x: -x[1]):
            print(f"{role}: {count}")
        return
    else:
        # 通常発火: 1時間に1回まで
        last_time = read_last_notify_time()
        now = datetime.now()
        if last_time and (now - last_time) < timedelta(hours=1):
            return
        msg = generate_announcement()
        notify_announcement(msg)
        log_announcement(msg)
        write_last_notify_time(now)

if __name__ == '__main__':
    main()
