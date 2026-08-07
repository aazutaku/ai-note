import sys
import time
import random
import argparse
import platform
import subprocess
from threading import Thread

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

NOTIFICATIONS = [
    "肩回しタイム発動！今すぐ両腕を回転せよ。",
    "OS推奨：5分間ぼーっとするべし。",
    "緊急！脳内メモリ休息モード。",
    "窓の外を眺めて深呼吸するべし。",
    "休憩プロトコル：好きな飲み物を用意してください。",
    "謎のアップデート中。作業を一時中断してください。",
    "OS推奨：目を閉じて10秒間リラックス。",
    "肩甲骨を寄せてリフレッシュ！",
    "システム：ストレッチ推奨。",
    "OSからのお願い：背筋を伸ばしてください。",
    "脳内キャッシュが溢れています。休憩を推奨します。",
    "強制休憩モード発動。5分間席を外してください。"
]

TITLE = "[OS通知]"


def show_notification(message):
    """
    OSに応じてデスクトップ通知を表示
    """
    if PLYER_AVAILABLE:
        notification.notify(
            title=TITLE,
            message=message,
            timeout=8
        )
        return
    system = platform.system()
    if system == "Darwin":  # macOS
        script = f'display notification "{message}" with title "{TITLE}"'
        subprocess.run(["osascript", "-e", script])
    elif system == "Linux":
        subprocess.run(["notify-send", TITLE, message])
    elif system == "Windows":
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(TITLE, message, duration=8)
        except ImportError:
            print(f"{TITLE} {message}")
    else:
        print(f"{TITLE} {message}")


def random_notification_loop(min_interval=900, max_interval=2700):
    """
    ランダムな間隔で通知を表示し続ける
    min_interval, max_interval: 秒単位
    """
    try:
        while True:
            interval = random.randint(min_interval, max_interval)
            time.sleep(interval)
            message = random.choice(NOTIFICATIONS)
            show_notification(message)
    except KeyboardInterrupt:
        print("通知ループを終了します。")


def send_single():
    message = random.choice(NOTIFICATIONS)
    show_notification(message)
    print(f"{TITLE} {message}")


def list_messages():
    print("--- 通知メッセージ一覧 ---")
    for i, msg in enumerate(NOTIFICATIONS, 1):
        print(f"{i}. {msg}")


def summary():
    print("Skill名: random-os-fake-breaktime-alert")
    print(f"登録メッセージ数: {len(NOTIFICATIONS)}")
    print(f"対応OS: macOS, Linux, Windows (一部要追加パッケージ)")
    print("通知内容は毎回ランダムで変化。実作業やデータには一切影響なし。")


def main():
    parser = argparse.ArgumentParser(description="謎のOS風・強制休憩通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_send = subparsers.add_parser("send", help="1回だけランダム通知を表示")
    parser_loop = subparsers.add_parser("loop", help="定期/ランダム間隔で通知を繰り返し表示")
    parser_loop.add_argument("--min", type=int, default=900, help="最小通知間隔(秒)")
    parser_loop.add_argument("--max", type=int, default=2700, help="最大通知間隔(秒)")
    parser_list = subparsers.add_parser("list", help="メッセージ一覧を表示")
    parser_summary = subparsers.add_parser("summary", help="Skill概要を表示")

    args = parser.parse_args()

    if args.command == "send":
        send_single()
    elif args.command == "loop":
        min_int = max(10, args.min)
        max_int = max(min_int, args.max)
        print(f"通知ループ開始: {min_int}～{max_int}秒間隔")
        random_notification_loop(min_interval=min_int, max_interval=max_int)
    elif args.command == "list":
        list_messages()
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
