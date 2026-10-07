import sys
import os
import random
import time
import platform
import argparse
import threading
import subprocess
from datetime import datetime

# 通知メッセージ候補
NOTIFY_MESSAGES = [
    "ボス検知センサーが反応：現在の画面は安全ですか？",
    "上司接近！5秒以内にウィンドウを隠してください",
    "緊急：非公式アプリケーション検出。即時対応を推奨します。",
    "画面キャプチャ監視中…安全を確認してください。",
    "システムが異常な静寂を検出しました。何か隠していますか？",
    "OS公式警告：作業内容を再確認してください。",
    "警告：ボスキーが無効化されています。",
    "通知：ウィンドウ切替履歴を送信中…",
    "警告：不審なマウス操作を検出しました。",
    "注意：上司の気配が近づいています。",
    "OS ALERT: Suspicious inactivity detected. Resume work immediately.",
    "OS WARNING: Unauthorized application in foreground.",
    "NOTICE: Boss proximity sensor triggered. Stay alert.",
    "ALERT: Unexpected window switch detected.",
    "WARNING: System detected possible distraction."
]

# OSごとの通知送信
class Notifier:
    def __init__(self):
        self.system = platform.system()
        if self.system == "Windows":
            try:
                from win10toast import ToastNotifier
                self.toaster = ToastNotifier()
            except ImportError:
                self.toaster = None
        elif self.system == "Darwin":
            pass  # macOSはosascript利用
        elif self.system == "Linux":
            pass  # Linuxはnotify-send利用

    def send(self, title, message):
        if self.system == "Windows" and self.toaster:
            try:
                self.toaster.show_toast(title, message, duration=6, threaded=True)
            except Exception as e:
                print(f"[WARN] 通知失敗: {e}")
        elif self.system == "Darwin":
            script = f'display notification "{message}" with title "{title}"'
            try:
                subprocess.run(["osascript", "-e", script], check=True)
            except Exception as e:
                print(f"[WARN] 通知失敗: {e}")
        elif self.system == "Linux":
            try:
                subprocess.run(["notify-send", title, message], check=True)
            except Exception as e:
                print(f"[WARN] 通知失敗: {e}")
        else:
            print(f"[OS ALERT] {message}")

# ランダムなインターバルで通知を送信
class BossKeyAlertRunner:
    def __init__(self, min_interval=60, max_interval=600, verbose=False):
        self.notifier = Notifier()
        self.min_interval = min_interval
        self.max_interval = max_interval
        self.verbose = verbose
        self.running = False
        self.log = []

    def random_message(self):
        return random.choice(NOTIFY_MESSAGES)

    def random_interval(self):
        return random.randint(self.min_interval, self.max_interval)

    def send_alert(self):
        msg = self.random_message()
        title = random.choice(["OS ALERT", "OS WARNING", "OS NOTICE", "ALERT", "WARNING"])
        self.notifier.send(title, msg)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log.append({"time": timestamp, "title": title, "message": msg})
        if self.verbose:
            print(f"[{timestamp}] {title}: {msg}")

    def run(self, count=None):
        self.running = True
        n = 0
        while self.running:
            self.send_alert()
            n += 1
            if count and n >= count:
                break
            interval = self.random_interval()
            if self.verbose:
                print(f"[INFO] 次の通知まで {interval} 秒待機")
            for _ in range(interval):
                if not self.running:
                    break
                time.sleep(1)

    def stop(self):
        self.running = False

    def print_log(self):
        for entry in self.log:
            print(f"[{entry['time']}] {entry['title']}: {entry['message']}")

# CLIパーサ

def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Boss Key Alert - 理不尽な警告をランダム表示")
    parser.add_argument("run", nargs="?", help="警告通知をランダムに表示")
    parser.add_argument("--min-interval", type=int, default=60, help="通知の最小間隔（秒）")
    parser.add_argument("--max-interval", type=int, default=600, help="通知の最大間隔（秒）")
    parser.add_argument("--count", type=int, default=None, help="通知回数（指定しない場合は無限ループ）")
    parser.add_argument("--verbose", action="store_true", help="詳細出力")
    parser.add_argument("log", action="store_true", help="実行中の通知履歴を表示")

    args = parser.parse_args()

    if args.log:
        print("[INFO] ログ表示機能は実行中のみ利用可能です。")
        sys.exit(0)

    runner = BossKeyAlertRunner(min_interval=args.min_interval, max_interval=args.max_interval, verbose=args.verbose)

    try:
        runner.run(count=args.count)
    except KeyboardInterrupt:
        print("\n[INFO] 停止要求を受け付けました。ログを表示します。")
        runner.print_log()

if __name__ == "__main__":
    main()
