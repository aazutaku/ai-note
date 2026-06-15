import argparse
import random
import sys
import threading
import time
from plyer import notification

CHAOS_MESSAGES = [
    '危険：バグが自我を獲得しました',
    '注意：メモリがピクニック中',
    '深刻：キーボードが人生に迷っています',
    '警告：OSが哲学的問いに悩んでいます',
    '重大：CPUが詩を書き始めました',
    '警告：マウスが散歩に出かけました',
    '注意：ディスプレイが夢を見ています',
    '危険：ネットワークが迷子になりました',
    '深刻：電源が昼寝中です',
    '警告：ファイルシステムがダンスしています',
    '重大：プロセスが哲学者になりました',
    '警告：RAMが宇宙旅行に出発しました',
    '注意：GPUが絵を描いています',
    '深刻：システムクロックが逆走中',
    '警告：USBが自己主張を始めました'
]

LOG_FILE = 'chaos_alert.log'

class ChaosAlert:
    def __init__(self, interval=60, once=False, dry_run=False):
        self.interval = interval
        self.once = once
        self.dry_run = dry_run
        self.running = False
        self.thread = None

    def show_alert(self, message=None):
        msg = message or random.choice(CHAOS_MESSAGES)
        title = '謎のOS緊急アラート'
        if self.dry_run:
            print(f'[通知] {msg}')
        else:
            notification.notify(title=title, message=msg, app_name='desktop-chaos-alert', timeout=8)
        self.log_alert(msg)

    def log_alert(self, msg):
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} {msg}\n')

    def start(self):
        self.running = True
        if self.once:
            self.show_alert()
        else:
            self.thread = threading.Thread(target=self._loop, daemon=True)
            self.thread.start()
            try:
                while self.running:
                    time.sleep(1)
            except KeyboardInterrupt:
                self.running = False
                print('Chaos Alertを停止しました。')

    def _loop(self):
        while self.running:
            self.show_alert()
            for _ in range(self.interval):
                if not self.running:
                    break
                time.sleep(1)

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    @staticmethod
    def list_logs(limit=20):
        try:
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                lines = f.readlines()[-limit:]
                for line in lines:
                    print(line.strip())
        except FileNotFoundError:
            print('ログファイルが見つかりません。')

    @staticmethod
    def summary():
        try:
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                print(f'通知履歴: {len(lines)} 件')
                counts = {}
                for line in lines:
                    for msg in CHAOS_MESSAGES:
                        if msg in line:
                            counts[msg] = counts.get(msg, 0) + 1
                for msg, cnt in sorted(counts.items(), key=lambda x: -x[1]):
                    print(f'  {msg}: {cnt}回')
        except FileNotFoundError:
            print('ログファイルが見つかりません。')


def main():
    parser = argparse.ArgumentParser(description='desktop-chaos-alert: 謎のOS緊急アラートをデスクトップ通知で爆誕させます')
    subparsers = parser.add_subparsers(dest='command')

    run_parser = subparsers.add_parser('run', help='カオス通知を開始')
    run_parser.add_argument('--interval', type=int, default=60, help='通知間隔(秒)')
    run_parser.add_argument('--once', action='store_true', help='一度だけ通知')
    run_parser.add_argument('--dry-run', action='store_true', help='通知をprintで擬似表示')

    list_parser = subparsers.add_parser('list', help='通知履歴を表示')
    list_parser.add_argument('--limit', type=int, default=20, help='表示件数')

    summary_parser = subparsers.add_parser('summary', help='通知履歴のサマリを表示')

    args = parser.parse_args()

    if args.command == 'run':
        alert = ChaosAlert(interval=args.interval, once=args.once, dry_run=args.dry_run)
        alert.start()
    elif args.command == 'list':
        ChaosAlert.list_logs(limit=args.limit)
    elif args.command == 'summary':
        ChaosAlert.summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
