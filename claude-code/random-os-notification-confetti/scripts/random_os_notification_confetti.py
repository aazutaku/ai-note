import sys
import os
import platform
import time
import random
import argparse
from threading import Thread

# OSごとの通知関数

def notify_linux(title, message):
    try:
        from subprocess import run
        run(['notify-send', title, message])
    except Exception as e:
        print(f"[通知失敗(Linux)]: {e}")

def notify_macos(title, message):
    try:
        from subprocess import run
        script = f'display notification "{message}" with title "{title}"'
        run(['osascript', '-e', script])
    except Exception as e:
        print(f"[通知失敗(macOS)]: {e}")

def notify_windows(title, message):
    try:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=5, threaded=True)
    except ImportError:
        print("win10toast がインストールされていません: pip install win10toast")
    except Exception as e:
        print(f"[通知失敗(Windows)]: {e}")

def notify(title, message):
    system = platform.system()
    if system == 'Linux':
        notify_linux(title, message)
    elif system == 'Darwin':
        notify_macos(title, message)
    elif system == 'Windows':
        notify_windows(title, message)
    else:
        print(f"[通知未対応OS]: {title} {message}")

# 祝福メッセージリスト
CONFETTI_MESSAGES = [
    "本日も出社おめでとうございます！",
    "さっきのls、最高でした。",
    "何もしてないけど祝っておきます。",
    "意味なく祝福します。紙吹雪！",
    "あなたのタイピング、見事でした。",
    "今日の作業、すでに伝説です。",
    "コーヒー休憩も祝福タイム！",
    "git commit、お疲れ様です。",
    "全く脈絡なく祝います。",
    "この通知に意味はありません。",
    "気分転換にどうぞ！",
    "謎の紙吹雪、発射！",
    "あなたの努力に祝福を。",
    "この瞬間を祝います。",
    "ls -la、素晴らしい選択です。",
    "make build、成功を祈ります。",
    "今日も一日頑張りましょう！",
    "何もしてなくても祝います。",
    "突然の祝福に戸惑わないでください。",
    "意味不明な通知ですが気にしないでください。"
]

# 通知頻度制御
MIN_INTERVAL = 120  # 秒 (2分)
MAX_INTERVAL = 900  # 秒 (15分)

# 通知スレッド
class ConfettiNotifier(Thread):
    def __init__(self, once=False):
        super().__init__()
        self.once = once
        self.running = True
    def run(self):
        if self.once:
            send_random_notification()
            return
        while self.running:
            wait = random.randint(MIN_INTERVAL, MAX_INTERVAL)
            time.sleep(wait)
            send_random_notification()
    def stop(self):
        self.running = False

def send_random_notification():
    msg = random.choice(CONFETTI_MESSAGES)
    notify("祝福の紙吹雪", msg)
    print(f"[通知] {msg}")

# CLIサブコマンド

def main():
    parser = argparse.ArgumentParser(description="謎のコンフェッティ祝福通知スクリプト")
    subparsers = parser.add_subparsers(dest='command')

    parser_once = subparsers.add_parser('once', help='1回だけ祝福通知')
    parser_start = subparsers.add_parser('start', help='定期的に祝福通知')
    parser_stop = subparsers.add_parser('stop', help='(ダミー)スレッド停止')
    parser_list = subparsers.add_parser('list', help='祝福メッセージ一覧表示')
    parser_summary = subparsers.add_parser('summary', help='祝福通知の概要表示')

    args = parser.parse_args()

    if args.command == 'once':
        send_random_notification()
    elif args.command == 'start':
        print("[INFO] ランダム祝福通知を開始します (Ctrl+Cで停止)")
        notifier = ConfettiNotifier()
        try:
            notifier.start()
            while notifier.is_alive():
                notifier.join(1)
        except KeyboardInterrupt:
            notifier.stop()
            print("[INFO] 通知スレッドを停止しました")
    elif args.command == 'stop':
        print("[INFO] stopコマンドはダミーです。Ctrl+Cで停止してください。")
    elif args.command == 'list':
        print("== 祝福メッセージ一覧 ==")
        for i, msg in enumerate(CONFETTI_MESSAGES, 1):
            print(f"{i:2d}: {msg}")
    elif args.command == 'summary':
        print("== random-os-notification-confetti 概要 ==")
        print(f"登録祝福数: {len(CONFETTI_MESSAGES)}")
        print(f"通知間隔: {MIN_INTERVAL//60}-{MAX_INTERVAL//60}分")
        print("OS: Linux, macOS, Windows 対応")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
