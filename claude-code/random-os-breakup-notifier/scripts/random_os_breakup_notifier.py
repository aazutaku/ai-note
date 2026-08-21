import sys
import os
import random
import time
import argparse
import platform
import subprocess
from typing import List

BREAKUP_MESSAGES = [
    '[重要] あなたの愛用マウスが新しいパートナーに乗り換えました。',
    '[悲報] エディタがそっとあなたのもとを去りました。',
    '[ごめん] 今日からCtrlキーはAltキーと付き合うことに。',
    '[速報] ターミナルが「距離を置きたい」と言っています。',
    '[通知] あなたのデスクトップが他のユーザーと再起動しました。',
    '[悲報] ファイルシステムがあなたをブロックしました。',
    '[重要] CapsLockキーが新しい恋に落ちました。',
    '[速報] ショートカットがあなたの手元から旅立ちました。',
    '[ごめん] スクロールホイールはもう戻ってきません。',
    '[通知] あなたのタスクバーが距離を置きたがっています。',
    '[悲報] クリップボードは他のアプリを選びました。',
    '[重要] あなたのUSBメモリが新しいPCに心変わりしました。',
    '[ごめん] Wi-Fiはもうあなたのことを覚えていません。',
    '[速報] スリープモードが永遠の眠りにつきました。',
    '[通知] あなたのテーマカラーが他のユーザーのものになりました。'
]

NOTIFY_COMMANDS = {
    'Darwin': lambda msg: ['osascript', '-e', f'display notification "{msg}" with title "OS失恋通知"'],
    'Linux': lambda msg: ['notify-send', 'OS失恋通知', msg],
    'Windows': lambda msg: [sys.executable, '-c', f'import win10toast;win10toast.ToastNotifier().show_toast("OS失恋通知", "{msg}", duration=5)']
}

DEFAULT_INTERVAL = 600


def detect_os() -> str:
    return platform.system()


def show_notification(msg: str):
    os_name = detect_os()
    if os_name == 'Darwin':
        subprocess.run(NOTIFY_COMMANDS['Darwin'](msg), check=False)
    elif os_name == 'Linux':
        subprocess.run(NOTIFY_COMMANDS['Linux'](msg), check=False)
    elif os_name == 'Windows':
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast("OS失恋通知", msg, duration=5)
        except ImportError:
            subprocess.run(NOTIFY_COMMANDS['Windows'](msg), check=False)
    else:
        print(msg)


def random_message() -> str:
    return random.choice(BREAKUP_MESSAGES)


def notify_once():
    msg = random_message()
    show_notification(msg)
    print(msg)


def notify_loop(interval: int, count: int):
    for i in range(count):
        notify_once()
        if i < count - 1:
            time.sleep(interval)


def list_messages():
    print("--- OS失恋通知メッセージ一覧 ---")
    for i, msg in enumerate(BREAKUP_MESSAGES, 1):
        print(f"{i}. {msg}")


def summary():
    print(f"登録済み失恋通知数: {len(BREAKUP_MESSAGES)}")
    print(f"対応OS: macOS, Linux, Windows")
    print(f"通知API: osascript, notify-send, win10toast")
    print(f"デフォルト通知間隔: {DEFAULT_INTERVAL}秒")


def parse_args():
    parser = argparse.ArgumentParser(description='random-os-breakup-notifier: デジタル失恋通知をランダムに表示')
    subparsers = parser.add_subparsers(dest='command')

    notify_parser = subparsers.add_parser('notify', help='今すぐ失恋通知を表示')
    notify_parser.add_argument('-n', '--number', type=int, default=1, help='通知回数 (デフォルト: 1)')
    notify_parser.add_argument('-i', '--interval', type=int, default=DEFAULT_INTERVAL, help='通知間隔(秒) (デフォルト: 600)')

    subparsers.add_parser('list', help='登録済み失恋通知メッセージ一覧を表示')
    subparsers.add_parser('summary', help='スキルの概要情報を表示')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'notify':
        if args.number <= 1:
            notify_once()
        else:
            notify_loop(args.interval, args.number)
    elif args.command == 'list':
        list_messages()
    elif args.command == 'summary':
        summary()
    else:
        print('コマンドを指定してください: notify, list, summary')

if __name__ == '__main__':
    main()
