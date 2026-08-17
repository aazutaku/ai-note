import sys
import time
import threading
import random
import argparse
import platform
import subprocess

# 通知メッセージ候補
NAP_MESSAGES = [
    '検出：うたた寝モード突入',
    'OS推奨：夢の中でバグ修正',
    '睡眠ログをクラウドにアップロード中...',
    '30秒以上操作がありません。お昼寝タイム？',
    '注意：作業効率が夢の中に突入しました',
    '警告：OSがユーザーの眠気を検出しました',
    '推奨：仮想現実で作業を続行してください',
    'お昼寝検出：現実世界にログインしてください',
    '夢の中でコードレビュー中...',
    'OSメモ：サボり癖が発動しました'
]

IDLE_THRESHOLD = 30  # 秒

class IdleDetector:
    def __init__(self, idle_seconds=IDLE_THRESHOLD):
        self.idle_seconds = idle_seconds
        self.last_activity = time.time()
        self.lock = threading.Lock()
        self.stop_flag = False
        self.os_type = platform.system()
        self.notifier = self._get_notifier()

    def _get_notifier(self):
        if self.os_type == 'Linux':
            return self._notify_linux
        elif self.os_type == 'Darwin':
            return self._notify_macos
        elif self.os_type == 'Windows':
            try:
                import win10toast
                self._win_toaster = win10toast.ToastNotifier()
                return self._notify_windows
            except ImportError:
                return self._notify_terminal
        else:
            return self._notify_terminal

    def _notify_linux(self, message):
        try:
            subprocess.run(['notify-send', 'OSお昼寝検出アラート', message], check=True)
        except Exception:
            self._notify_terminal(message)

    def _notify_macos(self, message):
        script = f'display notification "{message}" with title "OSお昼寝検出アラート"'
        try:
            subprocess.run(['osascript', '-e', script], check=True)
        except Exception:
            self._notify_terminal(message)

    def _notify_windows(self, message):
        try:
            self._win_toaster.show_toast('OSお昼寝検出アラート', message, duration=5)
        except Exception:
            self._notify_terminal(message)

    def _notify_terminal(self, message):
        print(f'[OSお昼寝検出アラート] {message}')

    def reset_timer(self):
        with self.lock:
            self.last_activity = time.time()

    def monitor_idle(self):
        while not self.stop_flag:
            with self.lock:
                idle_time = time.time() - self.last_activity
            if idle_time >= self.idle_seconds:
                msg = random.choice(NAP_MESSAGES)
                self.notifier(msg)
                # 通知後は次の操作まで再通知しない
                self.reset_timer()
            time.sleep(1)

    def stop(self):
        self.stop_flag = True

    def run_interactive(self):
        print('OSお昼寝検出アラートを起動しました。何かキーを押すとタイマーがリセットされます。Ctrl+Cで終了。')
        idle_thread = threading.Thread(target=self.monitor_idle, daemon=True)
        idle_thread.start()
        try:
            while True:
                _ = sys.stdin.read(1)
                self.reset_timer()
        except KeyboardInterrupt:
            print('\n終了します。')
            self.stop()
            idle_thread.join()

    def run_watch(self):
        print('標準入力監視モード。何らかの入力があればタイマーをリセットします。Ctrl+Cで終了。')
        idle_thread = threading.Thread(target=self.monitor_idle, daemon=True)
        idle_thread.start()
        try:
            while True:
                line = sys.stdin.readline()
                if not line:
                    break
                self.reset_timer()
        except KeyboardInterrupt:
            print('\n終了します。')
            self.stop()
            idle_thread.join()

    def run_demo(self):
        print('デモモード：10秒ごとにランダム通知を表示します。Ctrl+Cで終了。')
        try:
            while True:
                msg = random.choice(NAP_MESSAGES)
                self.notifier(msg)
                time.sleep(10)
        except KeyboardInterrupt:
            print('\n終了します。')


def main():
    parser = argparse.ArgumentParser(description='random-os-nap-detection-alert: 30秒以上無操作でお昼寝アラートを通知')
    subparsers = parser.add_subparsers(dest='command', help='サブコマンド')

    parser_start = subparsers.add_parser('start', help='インタラクティブ監視モード (キー入力でリセット)')
    parser_watch = subparsers.add_parser('watch', help='標準入力監視モード (行入力でリセット)')
    parser_demo = subparsers.add_parser('demo', help='デモモード (10秒ごとにランダム通知)')

    parser.add_argument('--idle', type=int, default=IDLE_THRESHOLD, help='無操作検出までの秒数 (デフォルト: 30)')

    args = parser.parse_args()
    detector = IdleDetector(idle_seconds=args.idle)

    if args.command == 'start':
        detector.run_interactive()
    elif args.command == 'watch':
        detector.run_watch()
    elif args.command == 'demo':
        detector.run_demo()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
