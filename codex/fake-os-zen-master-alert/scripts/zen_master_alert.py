import sys
import os
import time
import random
import argparse
from threading import Thread, Event

try:
    from plyer import notification
except ImportError:
    notification = None

ZEN_MESSAGES = [
    'バグとは何かを問う前に、己を問え',
    '今日の悟り：if文を捨てよ、道は開ける',
    'コンパイルに失敗したとき、木魚を叩け',
    '画面のバグは心の乱れ',
    'エラーを直す前に、エラーを受け入れよ',
    '禅とは、print文を消すことなり',
    'デバッグは己の心を映す鏡',
    '変数名に迷うとき、静かに座せ',
    'リファクタリングの道は遠く、そして近い',
    'OSとは、無常なり',
    'エンターキーを押す前に、息を整えよ',
    'if文を捨てよ、道は開ける',
    'エラーは師なり',
    '最適化より、悟りを求めよ',
    'コードの行数を問うな、心の行数を問え'
]

DEFAULT_INTERVAL = 600  # 10分
MIN_INTERVAL = 30       # 30秒

class ZenMasterAlert:
    def __init__(self, interval=DEFAULT_INTERVAL, verbose=False):
        self.interval = max(MIN_INTERVAL, interval)
        self.verbose = verbose
        self._stop_event = Event()

    def send_notification(self, message):
        title = '偽OS禅マスター'
        if notification:
            try:
                notification.notify(
                    title=title,
                    message=message,
                    app_name='fake-os-zen-master-alert',
                    timeout=10
                )
            except Exception as e:
                if self.verbose:
                    print(f'[WARN] 通知失敗: {e}')
                print(f'[OS通知] {title}: {message}')
        else:
            print(f'[OS通知] {title}: {message}')

    def random_message(self):
        return random.choice(ZEN_MESSAGES)

    def start(self):
        if self.verbose:
            print(f'[INFO] 偽OS禅マスターを{self.interval}秒間隔で起動します')
        while not self._stop_event.is_set():
            msg = self.random_message()
            self.send_notification(msg)
            for _ in range(self.interval):
                if self._stop_event.is_set():
                    break
                time.sleep(1)
        if self.verbose:
            print('[INFO] 偽OS禅マスターを停止しました')

    def stop(self):
        self._stop_event.set()

    def once(self):
        msg = self.random_message()
        self.send_notification(msg)

    def list_messages(self):
        print('--- 禅マスター通知メッセージ一覧 ---')
        for i, msg in enumerate(ZEN_MESSAGES):
            print(f'{i+1}. {msg}')


def parse_args():
    parser = argparse.ArgumentParser(description='偽OS禅マスター通知スクリプト')
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_start = subparsers.add_parser('start', help='定期的に禅通知を送る')
    parser_start.add_argument('--interval', type=int, default=DEFAULT_INTERVAL, help='通知間隔(秒)')
    parser_start.add_argument('--verbose', action='store_true', help='詳細ログ出力')

    parser_once = subparsers.add_parser('once', help='1回だけ禅通知を送る')
    parser_once.add_argument('--verbose', action='store_true', help='詳細ログ出力')

    parser_list = subparsers.add_parser('list', help='禅メッセージ一覧を表示')

    parser_stop = subparsers.add_parser('stop', help='(ダミー)停止用')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'start':
        alert = ZenMasterAlert(interval=args.interval, verbose=args.verbose)
        try:
            alert.start()
        except KeyboardInterrupt:
            alert.stop()
    elif args.command == 'once':
        alert = ZenMasterAlert(verbose=args.verbose)
        alert.once()
    elif args.command == 'list':
        ZenMasterAlert().list_messages()
    elif args.command == 'stop':
        print('バックグラウンド実行は未対応です。Ctrl+Cで停止してください。')
    else:
        print('不明なコマンドです')

if __name__ == '__main__':
    main()
