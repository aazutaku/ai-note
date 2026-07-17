import sys
import os
import random
import time
import argparse
import platform
from datetime import datetime, timedelta

try:
    import notify2  # Linux
except ImportError:
    notify2 = None
try:
    from win10toast import ToastNotifier  # Windows
except ImportError:
    ToastNotifier = None
import subprocess

LAST_ANNOUNCE_FILE = os.path.expanduser('~/.random_os_retirement_last')

CHARACTERS = [
    'カーネル部長',
    'ファイルシステムさん',
    'メモリ課長',
    'プロセス係長',
    'デバイス管理人',
    'スケジューラ主任',
    'ネットワーク課長',
    'バッファ主任',
    'ドライバ係',
    'システムコール相談役',
]

ACTIONS = [
    '勇退します',
    '早期リタイアを決意しました',
    '第二の人生へ旅立ちます',
    '新天地に転職します',
    '定年を迎えました',
    '無期限休職に入ります',
    '突然の退職を発表しました',
    '異動となりました',
    '家庭の事情で退職します',
    '後進に道を譲ります',
]

PREFIXES = [
    '重要：',
    '通知：',
    '急報：',
    'お知らせ：',
    '緊急：',
    'ご報告：',
]


def can_announce():
    """1時間以内に通知していないか判定"""
    try:
        with open(LAST_ANNOUNCE_FILE, 'r') as f:
            last = float(f.read().strip())
        if time.time() - last < 3600:
            return False
    except Exception:
        pass
    return True


def record_announce():
    try:
        with open(LAST_ANNOUNCE_FILE, 'w') as f:
            f.write(str(time.time()))
    except Exception:
        pass


def generate_message():
    prefix = random.choice(PREFIXES)
    char = random.choice(CHARACTERS)
    action = random.choice(ACTIONS)
    return f"{prefix}{char}が{action}。"


def send_notification(message):
    system = platform.system()
    if system == 'Linux' and notify2:
        try:
            notify2.init('Random OS Retirement')
            n = notify2.Notification('通知', message)
            n.show()
        except Exception:
            print(f"[通知] {message}")
    elif system == 'Windows' and ToastNotifier:
        try:
            toaster = ToastNotifier()
            toaster.show_toast('通知', message, duration=5)
        except Exception:
            print(f"[通知] {message}")
    elif system == 'Darwin':
        try:
            subprocess.run([
                'osascript', '-e', f'display notification "{message}" with title "通知"'
            ])
        except Exception:
            print(f"[通知] {message}")
    else:
        print(f"[通知] {message}")


def announce():
    if not can_announce():
        print("[INFO] 通知済みなのでスキップします (1時間に1回まで)")
        return
    msg = generate_message()
    send_notification(msg)
    record_announce()
    print(f"[通知] {msg}")


def list_examples():
    print("--- 通知例 ---")
    for _ in range(5):
        print(f"[通知] {generate_message()}")


def summary():
    print("# random-os-retirement-announcement summary")
    print("・架空のOSキャラが退職/転職を通知\n・1時間に1回まで\n・通知内容は完全ランダム")


def main():
    parser = argparse.ArgumentParser(description='Random OS Retirement Announcement')
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = False

    parser_announce = subparsers.add_parser('announce', help='今すぐ退職通知を出す')
    parser_list = subparsers.add_parser('list', help='サンプル通知を5件表示')
    parser_summary = subparsers.add_parser('summary', help='Skill概要を表示')

    args = parser.parse_args()
    if args.command == 'announce' or args.command is None:
        announce()
    elif args.command == 'list':
        list_examples()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
