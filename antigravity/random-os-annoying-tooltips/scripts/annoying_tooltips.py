import sys
import os
import random
import time
import argparse
import threading
import platform

try:
    if platform.system() == 'Windows':
        from win10toast import ToastNotifier
    elif platform.system() == 'Darwin':
        import pync
    else:
        import notify2
except ImportError:
    pass

def get_notifier():
    system = platform.system()
    if system == 'Windows':
        return ToastNotifier()
    elif system == 'Darwin':
        return None  # pync does not need initialization
    else:
        notify2.init('Annoying Tooltips')
        return notify2

def send_notification(title, message):
    system = platform.system()
    if system == 'Windows':
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=5, threaded=True)
    elif system == 'Darwin':
        pync.notify(message, title=title)
    else:
        n = notify2.Notification(title, message)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.set_timeout(5000)
        n.show()

ANNOYING_MESSAGES = [
    ("CapsLock警告", "あなたのCapsLockキー、今押されていますか？"),
    ("アップデートのお知らせ", "システムアップデートの準備ができています。今すぐ再起動しますか？"),
    ("入力速度低下", "入力速度が平均より遅いようです。タイピング練習をおすすめします。"),
    ("明るさ調整", "画面の明るさが最適化されていません。自動調整しますか？"),
    ("休憩推奨", "しばらく休憩していません。ストレッチの時間です。"),
    ("ネットワーク", "インターネット接続が不安定かもしれません。診断しますか？"),
    ("バッテリー", "バッテリー残量が十分でも充電をおすすめします。"),
    ("通知設定", "通知が多すぎると感じたら、設定を見直しましょう。"),
    ("無意味なヒント", "この通知は特に意味がありません。"),
    ("ユーザー名確認", f"本当に {os.getlogin()} さんですか？")
]

def annoying_loop(interval_min=600, interval_max=1800, stop_event=None):
    """定期的にうざい通知を出すループ。"""
    while not (stop_event and stop_event.is_set()):
        title, message = random.choice(ANNOYING_MESSAGES)
        send_notification(title, message)
        next_interval = random.randint(interval_min, interval_max)
        for _ in range(next_interval):
            if stop_event and stop_event.is_set():
                break
            time.sleep(1)

def list_messages():
    print("-- 登録されているうざい通知メッセージ一覧 --")
    for idx, (title, msg) in enumerate(ANNOYING_MESSAGES):
        print(f"{idx+1}. [{title}] {msg}")

def send_once():
    title, message = random.choice(ANNOYING_MESSAGES)
    print(f"[通知] {title}: {message}")
    send_notification(title, message)

def summary():
    print("本Skillは、OS風のうざい通知をランダムなタイミングで発生させます。")
    print(f"通知パターン数: {len(ANNOYING_MESSAGES)}")
    print("主要OSに対応 (Windows/macOS/Linux)。")
    print("通知間隔: 10分〜30分 (デフォルト)")

def main():
    parser = argparse.ArgumentParser(description='Random OS Annoying Tooltips')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='定期的にうざい通知を出し続ける')
    parser_log.add_argument('--min', type=int, default=600, help='通知間隔(秒)の下限')
    parser_log.add_argument('--max', type=int, default=1800, help='通知間隔(秒)の上限')

    parser_list = subparsers.add_parser('list', help='通知メッセージ一覧を表示')
    parser_once = subparsers.add_parser('once', help='1回だけ通知を送信')
    parser_summary = subparsers.add_parser('summary', help='Skill概要を表示')

    args = parser.parse_args()
    if args.command == 'log':
        stop_event = threading.Event()
        try:
            annoying_loop(args.min, args.max, stop_event)
        except KeyboardInterrupt:
            print("\n[終了] 通知ループを停止しました。")
            stop_event.set()
    elif args.command == 'list':
        list_messages()
    elif args.command == 'once':
        send_once()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
