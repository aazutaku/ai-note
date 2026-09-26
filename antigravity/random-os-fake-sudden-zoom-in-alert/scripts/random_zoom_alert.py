import sys
import time
import random
import argparse
import platform
import subprocess
from threading import Thread, Event

ZOOM_ALERT_MESSAGES = [
    "重大：ズームインモード突入まで残り{sec}秒",
    "画面拡大率が謎の力で上昇中！",
    "OSが自動的にズームインを試行中です",
    "不明なプロセスが画面を拡大しようとしています",
    "ズームイン解除方法：不明",
    "警告：画面ズームインがキャンセルできません",
    "システム：ズームインイベントを検出しました",
    "画面拡大率：{percent}% (通常値を超過)",
    "重大警告：ズームイン制御が不能です",
    "INFO: Zoom-In Mode Engaged by Unknown Source"
]

TERMINAL_COLORS = {
    "ALERT": "\033[91m",
    "WARNING": "\033[93m",
    "NOTICE": "\033[96m",
    "INFO": "\033[92m",
    "ENDC": "\033[0m"
}

class ZoomAlertRunner:
    def __init__(self, mode="terminal", min_interval=60, max_interval=600, stop_event=None):
        self.mode = mode
        self.min_interval = min_interval
        self.max_interval = max_interval
        self.stop_event = stop_event or Event()

    def random_message(self):
        msg = random.choice(ZOOM_ALERT_MESSAGES)
        if "{sec}" in msg:
            msg = msg.format(sec=random.randint(3, 15))
        if "{percent}" in msg:
            msg = msg.format(percent=random.randint(120, 400))
        prefix = random.choice(["ALERT", "WARNING", "NOTICE", "INFO"])
        return prefix, msg

    def notify_terminal(self, prefix, msg):
        color = TERMINAL_COLORS.get(prefix, "")
        endc = TERMINAL_COLORS["ENDC"]
        print(f"{color}[{prefix}] {msg}{endc}")

    def notify_desktop(self, prefix, msg):
        system = platform.system()
        title = f"{prefix}: OS Zoom-In Alert"
        body = msg
        try:
            if system == "Darwin":
                subprocess.run([
                    "osascript", "-e",
                    f'display notification "{body}" with title "{title}"'
                ], check=True)
            elif system == "Linux":
                subprocess.run([
                    "notify-send", title, body
                ], check=True)
            elif system == "Windows":
                try:
                    from win10toast import ToastNotifier
                    toaster = ToastNotifier()
                    toaster.show_toast(title, body, duration=5, threaded=True)
                except ImportError:
                    self.notify_terminal(prefix, msg + " (win10toast未導入)")
            else:
                self.notify_terminal(prefix, msg + " (デスクトップ通知未対応)")
        except Exception as e:
            self.notify_terminal(prefix, msg + f" (通知失敗: {e})")

    def run(self):
        while not self.stop_event.is_set():
            interval = random.randint(self.min_interval, self.max_interval)
            for _ in range(interval):
                if self.stop_event.is_set():
                    return
                time.sleep(1)
            prefix, msg = self.random_message()
            if self.mode == "desktop":
                self.notify_desktop(prefix, msg)
            else:
                self.notify_terminal(prefix, msg)

    def stop(self):
        self.stop_event.set()

def list_messages():
    print("--- サンプル警告メッセージ一覧 ---")
    for msg in ZOOM_ALERT_MESSAGES:
        print("- " + msg.replace("{sec}", "X").replace("{percent}", "Y"))

def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Sudden Zoom-In Alert Skill")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="フェイクズーム警告をランダム表示 (デフォルト:ターミナル)")
    run_parser.add_argument("--mode", choices=["terminal", "desktop"], default="terminal", help="通知方法")
    run_parser.add_argument("--min-interval", type=int, default=60, help="最短通知間隔(秒)")
    run_parser.add_argument("--max-interval", type=int, default=600, help="最長通知間隔(秒)")

    list_parser = subparsers.add_parser("list", help="生成される警告メッセージ例を表示")

    args = parser.parse_args()

    if args.command == "list":
        list_messages()
        return
    if args.command == "run" or args.command is None:
        runner = ZoomAlertRunner(
            mode=getattr(args, 'mode', 'terminal'),
            min_interval=getattr(args, 'min_interval', 60),
            max_interval=getattr(args, 'max_interval', 600)
        )
        try:
            print("[INFO] フェイクズーム警告を開始します。Ctrl+Cで停止")
            runner.run()
        except KeyboardInterrupt:
            print("\n[INFO] 停止します。お疲れさまでした。")
            runner.stop()

if __name__ == '__main__':
    main()
