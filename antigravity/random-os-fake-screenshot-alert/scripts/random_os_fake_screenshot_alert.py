import sys
import os
import random
import time
import argparse
import platform
import subprocess
from typing import List

NOTIFICATIONS = [
    "スクリーンショット保存済み：バグ発生の瞬間",
    "証拠画像を保存しました（保存先：謎の場所）",
    "あなたの集中顔を記録しました",
    "スクリーンショット保存済み：謎の警告画面",
    "保存完了：エラー再現の瞬間",
    "証拠画像をクラウドにアップロードしました",
    "保存済み：デバッグ中の様子",
    "あなたの操作記録を画像として保存しました",
    "保存完了：今の表情を記録",
    "スクリーンショット保存済み：謎のウィンドウ"
]

KEYWORDS = ["スクリーンショット", "保存", "記録", "証拠", "capture", "screenshot", "save", "record"]

HISTORY_FILE = os.path.expanduser("~/.random_os_fake_screenshot_alert.log")


def send_notification(message: str):
    system = platform.system()
    try:
        if system == "Darwin":
            # macOS
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "通知"'
            ], check=True)
        elif system == "Linux":
            # Linux
            subprocess.run([
                "notify-send", "通知", message], check=True)
        elif system == "Windows":
            # Windows
            import ctypes
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("通知", message, duration=5, threaded=True)
        else:
            print(f"[通知] {message}")
    except Exception as e:
        print(f"[通知] {message} (通知API失敗: {e})")


def pick_random_message() -> str:
    return random.choice(NOTIFICATIONS)


def log_history(message: str):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {message}\n")


def list_history(count: int = 10):
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines[-count:]:
        print(line.strip())


def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"合計通知回数: {len(lines)}")
    counter = {}
    for line in lines:
        for msg in NOTIFICATIONS:
            if msg in line:
                counter[msg] = counter.get(msg, 0) + 1
    for msg, cnt in sorted(counter.items(), key=lambda x: -x[1]):
        print(f"{msg}: {cnt}回")


def should_trigger(text: str) -> bool:
    text_lower = text.lower()
    for kw in KEYWORDS:
        if kw in text_lower:
            return True
    return False


def trigger_random_alert():
    message = pick_random_message()
    send_notification(message)
    log_history(message)


def main():
    parser = argparse.ArgumentParser(description="謎のOS偽スクリーンショット通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser("log", help="擬似通知を発動する")
    parser_log.add_argument("--text", type=str, default="", help="キーワード判定用テキスト")
    parser_log.add_argument("--force", action="store_true", help="強制発動（キーワード無視）")

    parser_list = subparsers.add_parser("list", help="通知履歴を表示する")
    parser_list.add_argument("--count", type=int, default=10, help="表示件数")

    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリーを表示する")

    parser_auto = subparsers.add_parser("auto", help="一定間隔で自動発動する（Ctrl+Cで停止）")
    parser_auto.add_argument("--interval", type=int, default=900, help="発動間隔(秒)")
    parser_auto.add_argument("--max", type=int, default=0, help="最大発動回数（0=無制限）")

    args = parser.parse_args()

    if args.command == "log":
        if args.force or should_trigger(args.text):
            trigger_random_alert()
        else:
            print("キーワードが含まれていないため通知は発動しません。--forceで強制発動できます。")
    elif args.command == "list":
        list_history(args.count)
    elif args.command == "summary":
        summary_history()
    elif args.command == "auto":
        count = 0
        try:
            while True:
                trigger_random_alert()
                count += 1
                if args.max > 0 and count >= args.max:
                    break
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\n自動発動を停止しました。")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
