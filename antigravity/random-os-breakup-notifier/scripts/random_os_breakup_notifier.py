import sys
import os
import random
import time
import platform
import argparse
import subprocess
from threading import Thread
from datetime import datetime

BREAKUP_MESSAGES = [
    "重要: あなたのマウスが新しいパートナーに乗り換えました。",
    "悲報: エディタがそっとあなたのもとを去りました。",
    "ごめん、今日からCtrlキーはAltキーと付き合うことに。",
    "ディスプレイがあなたの視線を避けています。",
    "あなたのUSBメモリは新しいPCに夢中です。",
    "悲報: ターミナルがあなたのコマンドに飽きました。",
    "あなたのBluetoothイヤホンは別のデバイスと繋がっています。",
    "プリンタがあなたのジョブを拒否しました。",
    "あなたのデスクトップ壁紙が引っ越しを決意しました。",
    "悲報: スクロールホイールが逆方向に進み始めました。",
    "あなたのWebカメラは新しい視界を求めています。",
    "CapsLockキーが静かに去りました。",
    "あなたのキーボードは他の指を受け入れました。",
    "悲報: SSDがHDDに戻りたがっています。",
    "あなたのモニターはデュアルディスプレイと浮気中です。",
    "悲報: タスクバーがスタートメニューに片思いしています。",
    "あなたのマイクは沈黙を選びました。",
    "ごめん、今日からAltキーはFnキーと付き合うことに。",
    "あなたのパスワードは記憶から消えました。",
    "悲報: クリップボードが他のコピーに夢中です。"
]

HISTORY_FILE = os.path.expanduser("~/.random_os_breakup_history.log")


def send_notification(message):
    system = platform.system()
    try:
        if system == "Darwin":
            # macOS: osascript
            script = f'display notification "{message}" with title "通知"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            # Linux: notify-send
            subprocess.run(["notify-send", "通知", message], check=True)
        elif system == "Windows":
            # Windows: win10toast (if available), fallback to msgbox
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("通知", message, duration=5)
            except ImportError:
                # fallback: powershell popup
                script = f'[System.Windows.MessageBox]::Show("{message}","通知")'
                subprocess.run(["powershell", "-Command", script], check=True)
        else:
            print(f"[通知] {message}")
    except Exception as e:
        print(f"[通知] {message} (通知API失敗: {e})")


def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def random_breakup_event():
    message = random.choice(BREAKUP_MESSAGES)
    send_notification(message)
    log_message(message)
    print(f"[通知] {message}")


def loop_mode(min_interval=600, max_interval=1800):
    try:
        while True:
            wait_time = random.randint(min_interval, max_interval)
            time.sleep(wait_time)
            random_breakup_event()
    except KeyboardInterrupt:
        print("\n[終了] random-os-breakup-notifierを停止しました。")


def list_history(limit=20):
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines[-limit:]:
        print(line.strip())


def summary():
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"通知回数: {len(lines)}")
    counter = {}
    for line in lines:
        for msg in BREAKUP_MESSAGES:
            if msg in line:
                counter[msg] = counter.get(msg, 0) + 1
    for msg, count in sorted(counter.items(), key=lambda x: -x[1]):
        print(f"{msg[:30]}... : {count}回")


def parse_args():
    parser = argparse.ArgumentParser(description="random-os-breakup-notifier: デジタル失恋通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("run", help="定期的にランダム通知を発生させる (デフォルト)")
    subparsers.add_parser("once", help="1回だけ通知を発生させる")
    subparsers.add_parser("list", help="通知履歴を表示する")
    subparsers.add_parser("summary", help="通知履歴のサマリーを表示する")

    parser.add_argument("--min", type=int, default=600, help="通知間隔の最小秒数 (デフォルト600)")
    parser.add_argument("--max", type=int, default=1800, help="通知間隔の最大秒数 (デフォルト1800)")
    parser.add_argument("--limit", type=int, default=20, help="履歴表示の最大件数 (デフォルト20)")

    return parser.parse_args()


def main():
    args = parse_args()
    cmd = args.command
    if cmd == "once":
        random_breakup_event()
    elif cmd == "list":
        list_history(args.limit)
    elif cmd == "summary":
        summary()
    else:
        loop_mode(args.min, args.max)


if __name__ == "__main__":
    main()
