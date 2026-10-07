import sys
import argparse
import random
import time
import threading
import os
import platform

BOSS_ALERTS = [
    "[OS警告] 上司接近！5秒以内にウィンドウを隠してください。",
    "[警告] ボス検知センサーが反応：現在の画面は安全ですか？",
    "[ALERT] 重要作業中に第三者の視線を検知。即時対応推奨。",
    "[警告] 不審な動きが検出されました。ボスキーを押してください。",
    "[OS通知] 画面監視モードが有効になりました。",
    "[警告] システムが異常な緊張感を検出しました。",
    "[ALERT] 作業内容が監督者の関心領域に入りました。",
    "[OS警告] ボスキー押下が推奨されています。",
    "[警告] あなたの動作が監視対象となっています。",
    "[ALERT] 画面の安全性が低下しています。"
]

MIN_INTERVAL = 30  # 秒
MAX_INTERVAL = 180  # 秒

class BossKeyAlert:
    def __init__(self):
        self.running = False
        self.thread = None
        self.history = []
        self.lock = threading.Lock()

    def _notify(self, message):
        # ターミナルに出力
        print(message)
        # OS通知も試みる
        try:
            if platform.system() == 'Darwin':
                os.system(f'''osascript -e 'display notification "{message}" with title "Fake Boss Key Alert"' ''')
            elif platform.system() == 'Linux':
                os.system(f'''notify-send "Fake Boss Key Alert" "{message}"''')
            elif platform.system() == 'Windows':
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("Fake Boss Key Alert", message, duration=5)
        except Exception:
            pass

    def _alert_loop(self):
        while self.running:
            interval = random.randint(MIN_INTERVAL, MAX_INTERVAL)
            time.sleep(interval)
            message = random.choice(BOSS_ALERTS)
            with self.lock:
                self.history.append((time.time(), message))
            self._notify(message)

    def start(self):
        if self.running:
            print("[INFO] Fake Boss Key Alert is already running.")
            return
        self.running = True
        self.thread = threading.Thread(target=self._alert_loop, daemon=True)
        self.thread.start()
        print("[INFO] Fake Boss Key Alert started. Enjoy the random tension!")

    def stop(self):
        if not self.running:
            print("[INFO] Fake Boss Key Alert is not running.")
            return
        self.running = False
        if self.thread:
            self.thread.join(timeout=2)
        print("[INFO] Fake Boss Key Alert stopped.")

    def list_alerts(self, count=10):
        with self.lock:
            history = self.history[-count:]
        for t, msg in history:
            ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))
            print(f"{ts}: {msg}")

    def summary(self):
        with self.lock:
            total = len(self.history)
        print(f"Total alerts issued: {total}")


def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Boss Key Alert Skill')
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    parser_start = subparsers.add_parser('start', help='Start random boss key alerts')
    parser_stop = subparsers.add_parser('stop', help='Stop boss key alerts')
    parser_list = subparsers.add_parser('list', help='List recent boss key alerts')
    parser_list.add_argument('--count', type=int, default=10, help='Number of alerts to show')
    parser_summary = subparsers.add_parser('summary', help='Show alert summary')

    args = parser.parse_args()

    # インスタンスはグローバルで1つだけ
    global_alert = BossKeyAlert()

    if args.command == 'start':
        try:
            global_alert.start()
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            global_alert.stop()
    elif args.command == 'stop':
        global_alert.stop()
    elif args.command == 'list':
        global_alert.list_alerts(count=args.count)
    elif args.command == 'summary':
        global_alert.summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
