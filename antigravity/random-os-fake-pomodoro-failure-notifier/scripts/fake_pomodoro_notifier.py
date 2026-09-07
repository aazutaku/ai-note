import sys
import argparse
import random
import time
import platform
import threading

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

FAILURE_MESSAGES = [
    "失敗：トマトが爆発しました。机上に赤い液体注意！",
    "警告：集中力が鍋底にこびりつきました。洗剤推奨。",
    "注意：タイマーがピザに変身したため無効です。",
    "失敗：ポモドーロが月面に着陸しました。",
    "エラー：トマトの種が暴走しています。",
    "警告：タイマーがトマトソースに溶けました。",
    "注意：作業集中度がピクルスレベルまで低下。",
    "失敗：集中力がトマト缶に封印されました。",
    "エラー：タイマーがパスタに絡まりました。",
    "警告：ポモドーロがピザ窯に投げ込まれました。",
    "注意：トマトの妖精がタイマーを持ち去りました。",
    "失敗：集中力がサラダに分散されました。",
    "エラー：ポモドーロの神が微笑みませんでした。",
    "警告：タイマーがケチャップ化しました。",
    "注意：トマトの皮がむけて集中不能。",
    "失敗：トマトがAIに乗っ取られました。",
    "エラー：タイマーが野菜炒めに変身。",
    "警告：集中力が冷蔵庫に逃亡しました。",
    "注意：トマトの種がタイマーを占拠。",
    "失敗：ピザ職人がタイマーを持ち帰りました。"
]

TRIGGER_KEYWORDS = [
    "ポモドーロ", "pomodoro", "集中タイマー", "timer", "タイマー開始", "タイマー終了", "休憩", "失敗", "集中", "work session"
]

LOG_FILE = "pomodoro_fake_notify.log"


def send_notification(message):
    # ターミナル出力
    print(f"[FakeOS Notification] {message}")
    # デスクトップ通知
    if PLYER_AVAILABLE:
        notification.notify(
            title="FakeOS Notification",
            message=message,
            timeout=5
        )


def log_message(message):
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {message}\n")
    except Exception as e:
        print(f"[Logger Error] {e}")


def random_failure_message():
    return random.choice(FAILURE_MESSAGES)


def trigger_notification():
    message = random_failure_message()
    send_notification(message)
    log_message(message)


def listen_terminal():
    print("[Fake Pomodoro Notifier] キーワード入力でフェイク通知を発動します。終了は Ctrl+C")
    try:
        while True:
            user_input = input("> ")
            for kw in TRIGGER_KEYWORDS:
                if kw.lower() in user_input.lower():
                    trigger_notification()
                    break
    except KeyboardInterrupt:
        print("\n[Fake Pomodoro Notifier] 終了します。")


def show_log():
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("[Log] ログファイルがありません。まだ通知が発生していません。")


def summary():
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print(f"[Summary] 通知回数: {len(lines)}")
        counts = {}
        for line in lines:
            msg = line.strip().split(' ', 2)[-1]
            counts[msg] = counts.get(msg, 0) + 1
        sorted_counts = sorted(counts.items(), key=lambda x: -x[1])
        for msg, cnt in sorted_counts[:5]:
            print(f"{cnt}回: {msg}")
    except FileNotFoundError:
        print("[Summary] ログファイルがありません。")


def parse_args():
    parser = argparse.ArgumentParser(description="Random OS Fake Pomodoro Failure Notifier")
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('listen', help='キーワード入力で通知を発動 (デフォルト)')
    subparsers.add_parser('log', help='通知ログを表示')
    subparsers.add_parser('summary', help='通知履歴のサマリー表示')
    subparsers.add_parser('notify', help='即時ランダム通知を1回発動')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'log':
        show_log()
    elif args.command == 'summary':
        summary()
    elif args.command == 'notify':
        trigger_notification()
    else:
        listen_terminal()

if __name__ == '__main__':
    main()
