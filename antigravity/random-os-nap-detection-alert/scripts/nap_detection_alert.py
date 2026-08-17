import sys
import time
import threading
import random
import platform
import argparse

try:
    if platform.system() == 'Darwin':
        import pync
    elif platform.system() == 'Linux':
        import subprocess
    elif platform.system() == 'Windows':
        from win10toast import ToastNotifier
except ImportError:
    pass

NAP_MESSAGES = [
    "検出：うたた寝モード突入",
    "OS推奨：夢の中でバグ修正",
    "睡眠ログをクラウドにアップロード中",
    "メモリ開放中：夢の世界へ",
    "CPUアイドル：まどろみモード",
    "プロセス休止：再起動は夢のあとで",
    "OS診断：気まずさ指数MAX",
    "バックグラウンドで羊をカウント中",
    "仮想メモリ：睡眠領域確保完了",
    "システム推奨：おやつタイム"
]

class NapDetectionAlert:
    def __init__(self, idle_seconds=30, check_interval=1):
        self.idle_seconds = idle_seconds
        self.check_interval = check_interval
        self.last_active = time.time()
        self.running = False
        self._lock = threading.Lock()
        self._alert_thread = None
        self._input_thread = None
        self._notified = False
        self._platform = platform.system()
        if self._platform == 'Windows':
            self._toaster = ToastNotifier()

    def reset_timer(self):
        with self._lock:
            self.last_active = time.time()
            self._notified = False

    def _notify(self, message):
        title = "OSお昼寝検出アラート"
        if self._platform == 'Darwin':
            try:
                pync.notify(message, title=title)
            except Exception:
                print(f"[{title}]\n{message}")
        elif self._platform == 'Linux':
            try:
                subprocess.run(['notify-send', title, message])
            except Exception:
                print(f"[{title}]\n{message}")
        elif self._platform == 'Windows':
            try:
                self._toaster.show_toast(title, message, duration=5, threaded=True)
            except Exception:
                print(f"[{title}]\n{message}")
        else:
            print(f"[{title}]\n{message}")

    def _alert_loop(self):
        while self.running:
            time.sleep(self.check_interval)
            with self._lock:
                idle_time = time.time() - self.last_active
                if idle_time >= self.idle_seconds and not self._notified:
                    msg = random.choice(NAP_MESSAGES)
                    detail = f"({int(idle_time)}秒以上無操作を検出しました)"
                    self._notify(f"{msg}\n{detail}")
                    self._notified = True

    def _input_monitor(self):
        while self.running:
            try:
                # 非ブロッキングで入力を監視
                if sys.stdin in select.select([sys.stdin], [], [], 0.1)[0]:
                    _ = sys.stdin.readline()
                    self.reset_timer()
            except Exception:
                time.sleep(0.1)

    def start(self):
        self.running = True
        self._alert_thread = threading.Thread(target=self._alert_loop, daemon=True)
        self._alert_thread.start()
        if sys.stdin.isatty():
            import select
            self._input_thread = threading.Thread(target=self._input_monitor, daemon=True)
            self._input_thread.start()
        else:
            # 非対話環境では入力監視せず、API経由でreset_timer()を呼ぶ想定
            pass
        try:
            while self.running:
                time.sleep(0.2)
        except KeyboardInterrupt:
            self.running = False
            print("\n[終了] お昼寝検出アラートを停止しました。")

    def log(self):
        print(f"[log] 最終アクティブ時刻: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.last_active))}")

    def summary(self):
        print(f"[summary] 無操作検出閾値: {self.idle_seconds}秒\n現在プラットフォーム: {self._platform}")


def main():
    parser = argparse.ArgumentParser(description='OSお昼寝検出アラート (random-os-nap-detection-alert)')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='お昼寝検出アラートを起動')
    parser_run.add_argument('--idle', type=int, default=30, help='無操作と判定する秒数 (デフォルト30)')

    parser_log = subparsers.add_parser('log', help='最終アクティブ時刻を表示')
    parser_summary = subparsers.add_parser('summary', help='設定概要を表示')

    args = parser.parse_args()
    detector = NapDetectionAlert(idle_seconds=getattr(args, 'idle', 30))

    if args.command == 'run':
        detector.start()
    elif args.command == 'log':
        detector.log()
    elif args.command == 'summary':
        detector.summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
