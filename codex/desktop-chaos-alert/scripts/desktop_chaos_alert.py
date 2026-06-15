import sys
import os
import random
import argparse
import platform
import subprocess
import threading
import time

MESSAGES = [
    "危険：バグが自我を獲得しました",
    "注意：メモリがピクニック中",
    "深刻：キーボードが人生に迷っています",
    "警告：CPUが詩を書き始めました",
    "注意：OSが昼寝を要求しています",
    "警告：ファイルシステムが哲学的疑問を抱えています",
    "注意：GPUが現実逃避しています",
    "深刻：ネットワークが占いを始めました",
    "危険：プロセスが無限ループに恋をしました",
    "警告：システム時刻が未来に行きたがっています",
    "注意：マウスが自分探しの旅に出ました",
    "深刻：ログファイルが詩的表現を始めました"
]

PLATFORM = platform.system()


def send_notification(title: str, message: str):
    if PLATFORM == "Darwin":
        # macOS: 使用osascript
        script = f'display notification "{message}" with title "{title}"'
        subprocess.run(["osascript", "-e", script], check=False)
    elif PLATFORM == "Linux":
        # Linux: notify-send
        subprocess.run(["notify-send", title, message], check=False)
    elif PLATFORM == "Windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=5, threaded=True)
        except ImportError:
            print("win10toastが見つかりません。'pip install win10toast'でインストールしてください。")
    else:
        print(f"通知: {title}: {message}")


def random_alert():
    title = "謎のOS緊急アラート"
    message = random.choice(MESSAGES)
    send_notification(title, message)
    print(f"通知: {message}")


def list_messages():
    print("=== カオスアラート メッセージ一覧 ===")
    for i, msg in enumerate(MESSAGES, 1):
        print(f"{i:2d}: {msg}")


def add_message(msg: str):
    if msg.strip() and msg not in MESSAGES:
        MESSAGES.append(msg)
        print(f"追加: {msg}")
    else:
        print("既に存在するか空のメッセージです。")


def summary():
    print("# desktop-chaos-alert 概要")
    print(f"対応OS: {PLATFORM}")
    print(f"登録メッセージ数: {len(MESSAGES)}")
    print("通知API: macOS=osascript, Linux=notify-send, Windows=win10toast")
    print("通知履歴: 保存なし (一時的)\n")


def disable_alert():
    flag_path = os.path.expanduser("~/.desktop_chaos_alert_disabled")
    with open(flag_path, "w") as f:
        f.write("1")
    print("通知機能を無効化しました。再有効化は --enable で。")


def enable_alert():
    flag_path = os.path.expanduser("~/.desktop_chaos_alert_disabled")
    if os.path.exists(flag_path):
        os.remove(flag_path)
        print("通知機能を再有効化しました。")
    else:
        print("既に有効です。")


def is_disabled():
    flag_path = os.path.expanduser("~/.desktop_chaos_alert_disabled")
    return os.path.exists(flag_path)


def periodic_alert(interval: int, count: int):
    for _ in range(count):
        if is_disabled():
            print("通知は現在無効化されています。")
            break
        random_alert()
        time.sleep(interval)


def main():
    parser = argparse.ArgumentParser(description="desktop-chaos-alert: 謎のOSアラートをデスクトップ通知で爆誕させるスキル")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("alert", help="ランダムなカオス通知を1回表示")
    subparsers.add_parser("list", help="登録済みメッセージ一覧を表示")
    subparsers.add_parser("summary", help="Skillの概要を表示")

    add_parser = subparsers.add_parser("add", help="新しいカオスメッセージを追加")
    add_parser.add_argument("message", type=str, help="追加するメッセージ")

    subparsers.add_parser("disable", help="通知機能を無効化")
    subparsers.add_parser("enable", help="通知機能を再有効化")

    periodic_parser = subparsers.add_parser("periodic", help="一定間隔で複数回通知")
    periodic_parser.add_argument("--interval", type=int, default=10, help="通知間隔(秒)")
    periodic_parser.add_argument("--count", type=int, default=3, help="通知回数")

    args = parser.parse_args()

    if args.command == "alert":
        if is_disabled():
            print("通知は現在無効化されています。--enable で再有効化できます。")
            return
        random_alert()
    elif args.command == "list":
        list_messages()
    elif args.command == "add":
        add_message(args.message)
    elif args.command == "summary":
        summary()
    elif args.command == "disable":
        disable_alert()
    elif args.command == "enable":
        enable_alert()
    elif args.command == "periodic":
        if is_disabled():
            print("通知は現在無効化されています。--enable で再有効化できます。")
            return
        periodic_alert(args.interval, args.count)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
