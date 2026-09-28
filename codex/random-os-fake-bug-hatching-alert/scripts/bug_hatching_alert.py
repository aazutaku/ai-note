import sys
import os
import random
import time
import threading
import argparse
from datetime import datetime

LOG_FILE = 'bug_hatching_alert.log'

FAKE_ALERTS = [
    '[警告] {time} 新たなバグがシステム奥深くで孵化しました。',
    '[緊急] メモリ領域の暗部で未確認バグが産声をあげました。',
    '[通知] バグ孵化アラート: 本日{count}件目のバグが発見されました。',
    '[警告] OS公式: バグの幼生がプロセス空間に侵入しました。',
    '[速報] システム深層でバグの卵が割れた形跡を検出。',
    '[警告] {time} バグの孵化が検出されました。直ちに深呼吸してください。',
    '[通知] システム内でバグの幼体が活動を開始しました。',
    '[緊急] バグの卵が複数同時に孵化しています。',
    '[警告] OS公式: 未知のバグがプロセス空間に放たれました。',
    '[速報] バグの幼生がカーネル領域に侵入した模様です。',
    '[通知] バグ孵化アラート: システムの奥底で何かが目覚めました。',
    '[警告] {time} バグの卵が割れる音が聞こえました。',
    '[緊急] システムの暗部でバグが孵化し始めました。',
    '[速報] バグの幼体が新しいプロセスを乗っ取ろうとしています。',
    '[警告] OS公式: バグの繁殖が加速しています。',
    '[通知] バグ孵化アラート: 本日{count}匹目のバグが誕生しました。',
]

class BugHatchingAlert:
    def __init__(self, log_file=LOG_FILE):
        self.log_file = log_file
        self.lock = threading.Lock()
        self.alert_count = self._get_today_count()

    def _get_today_count(self):
        today = datetime.now().strftime('%Y-%m-%d')
        count = 0
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if today in line:
                        count += 1
        return count

    def _log_alert(self, message):
        with self.lock:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(message + '\n')

    def generate_alert(self):
        now = datetime.now()
        time_str = now.strftime('%Y-%m-%d %H:%M:%S')
        self.alert_count += 1
        template = random.choice(FAKE_ALERTS)
        message = template.format(time=time_str, count=self.alert_count)
        self._log_alert(message)
        return message

    def print_alert(self):
        message = self.generate_alert()
        print(message)

    def run_random_alerts(self, min_interval=60, max_interval=600, stop_event=None):
        try:
            while not (stop_event and stop_event.is_set()):
                interval = random.randint(min_interval, max_interval)
                time.sleep(interval)
                self.print_alert()
        except KeyboardInterrupt:
            print('\n[INFO] バグ孵化警告の自動演出を終了します。')

    def show_log(self, lines=20):
        if not os.path.exists(self.log_file):
            print('[INFO] ログファイルが存在しません。')
            return
        with open(self.log_file, 'r', encoding='utf-8') as f:
            log_lines = f.readlines()
            if not log_lines:
                print('[INFO] ログに記録はありません。')
                return
            print('--- 最新のバグ孵化警告ログ ---')
            for line in log_lines[-lines:]:
                print(line.strip())

    def show_summary(self):
        total = 0
        today = datetime.now().strftime('%Y-%m-%d')
        today_count = 0
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    total += 1
                    if today in line:
                        today_count += 1
        print(f'累計バグ孵化警告数: {total}')
        print(f'本日発生数: {today_count}')

    def clear_log(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
            print('[INFO] ログファイルを削除しました。')
        else:
            print('[INFO] ログファイルは存在しません。')

def main():
    parser = argparse.ArgumentParser(description='OS公式バグ孵化警告スキル (演出専用)')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='バグ孵化警告を即時表示')
    parser_random = subparsers.add_parser('random', help='ランダムな間隔でバグ孵化警告を自動表示')
    parser_random.add_argument('--min', type=int, default=60, help='最小間隔(秒)')
    parser_random.add_argument('--max', type=int, default=600, help='最大間隔(秒)')
    parser_log = subparsers.add_parser('log', help='バグ孵化警告のログを表示')
    parser_log.add_argument('--lines', type=int, default=20, help='表示行数')
    parser_summary = subparsers.add_parser('summary', help='警告発生数の統計を表示')
    parser_clear = subparsers.add_parser('clear', help='ログファイルを削除')

    args = parser.parse_args()
    alert = BugHatchingAlert()

    if args.command == 'alert':
        alert.print_alert()
    elif args.command == 'random':
        stop_event = threading.Event()
        try:
            alert.run_random_alerts(min_interval=args.min, max_interval=args.max, stop_event=stop_event)
        except KeyboardInterrupt:
            stop_event.set()
    elif args.command == 'log':
        alert.show_log(lines=args.lines)
    elif args.command == 'summary':
        alert.show_summary()
    elif args.command == 'clear':
        alert.clear_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
