import sys
import time
import random
import argparse
from threading import Thread, Event

try:
    from plyer import notification
except ImportError:
    print('plyerパッケージが必要です。\nインストール: pip install plyer')
    sys.exit(1)

ALERT_MESSAGES = [
    'CPU温存のため10分間タイピング禁止。',
    'マウス移動過多：省エネモード発動。',
    '電力節約のため思考も控えめにしてください。',
    '画面注視が長すぎます。目を閉じて省エネしましょう。',
    'システム冷却中。深呼吸して待機してください。',
    '電力不足: しばらく作業を控えてください。',
    'メモリ保護のため、ジョークを思い出してください。',
    'ディスプレイ輝度を心で下げてください。',
    'マウスクリック数が多すぎます。両手を膝に置いてください。',
    'CPU温度が上昇中。笑顔で冷却してください。',
    '省エネのため、今から1分間だけ何も考えないでください。',
    'バッテリー保護: しばらく目を閉じてください。',
    '冷却ファンが悲鳴を上げています。作業を中断してください。',
    '省エネモード：キーボードから手を離してください。',
    '電力節約のため、画面を見つめるのをやめましょう。',
    'マウスの動きが激しすぎます。省エネのため、しばらく静止してください。',
    'タイピング速度が速すぎます。省エネのため、ゆっくり入力してください。',
    'ディスプレイの輝度を心で下げてください。',
    '省エネ警告: しばらく深呼吸だけしてください。',
    'システム省電力モード: 何もせずに1分間待機してください。'
]

class PowerSaverAlert:
    def __init__(self, interval=600, count=5, dry_run=False):
        self.interval = interval
        self.count = count
        self.dry_run = dry_run
        self.stop_event = Event()
        self.history = []

    def send_alert(self, message):
        if self.dry_run:
            print(f'[通知] {message}')
        else:
            notification.notify(
                title='パワーセーバー警告',
                message=message,
                app_name='Fake Power Saver',
                timeout=10
            )
            print(f'[通知] {message}')
        self.history.append((time.strftime('%Y-%m-%d %H:%M:%S'), message))

    def run(self):
        for i in range(self.count):
            if self.stop_event.is_set():
                break
            msg = random.choice(ALERT_MESSAGES)
            self.send_alert(msg)
            if i < self.count - 1:
                for _ in range(self.interval):
                    if self.stop_event.is_set():
                        break
                    time.sleep(1)

    def stop(self):
        self.stop_event.set()

    def list_history(self):
        for t, msg in self.history:
            print(f'{t}  {msg}')

    def summary(self):
        print(f'送信済み警告数: {len(self.history)}')
        unique = set(msg for _, msg in self.history)
        print(f'ユニーク警告数: {len(unique)}')


def main():
    parser = argparse.ArgumentParser(
        description='ランダムな偽OSパワーセーバー警告をデスクトップ通知で表示します。')
    subparsers = parser.add_subparsers(dest='command')

    # runコマンド
    parser_run = subparsers.add_parser('run', help='警告通知を開始')
    parser_run.add_argument('--interval', type=int, default=600, help='通知間隔(秒) デフォルト600')
    parser_run.add_argument('--count', type=int, default=5, help='通知回数 デフォルト5')
    parser_run.add_argument('--dry-run', action='store_true', help='通知を端末出力のみにする')

    # listコマンド
    parser_list = subparsers.add_parser('list', help='送信済み警告履歴を表示')

    # summaryコマンド
    parser_summary = subparsers.add_parser('summary', help='警告履歴のサマリーを表示')

    args = parser.parse_args()
    alert = PowerSaverAlert()

    if args.command == 'run':
        alert = PowerSaverAlert(interval=args.interval, count=args.count, dry_run=args.dry_run)
        try:
            alert.run()
        except KeyboardInterrupt:
            print('中断されました')
    elif args.command == 'list':
        alert.list_history()
    elif args.command == 'summary':
        alert.summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
