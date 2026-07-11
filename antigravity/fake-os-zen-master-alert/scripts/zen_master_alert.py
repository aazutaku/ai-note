import random
import time
import argparse
import sys
import os
from threading import Thread, Event

try:
    from plyer import notification
except ImportError:
    print('plyerパッケージが必要です。pip install plyer でインストールしてください。')
    sys.exit(1)

ZEN_MESSAGES = [
    'バグとは何かを問う前に、己を問え',
    '今日の悟り：if文を捨てよ、道は開ける',
    'コンパイルに失敗したとき、木魚を叩け',
    '変数名に迷うとき、まず呼吸せよ',
    'echoの裏にこそ真実がある',
    'lsの結果に惑わされるな、心の中のディレクトリを見よ',
    'git pushする前に、己の執着をpushせよ',
    'カーネルパニックは心の乱れ',
    'sudoの力に頼るな、自らの力を信じよ',
    'rm -rfの前に、執着を手放せ',
    'エラーは敵にあらず、師である',
    'forループの中に悟りはない、一歩外に出よ',
    'printデバッグは禅問答の如し',
    'パーミッション denied、それは宇宙の采配',
    'セグフォルトは一瞬の無常',
    'コマンドの失敗は、成功への布石',
    'ls -laの闇に、己の影を見る',
    '再起動は再誕なり',
    'manページに書かれていない答えもある',
    'コマンドラインの静寂に耳を澄ませ'
]

DEFAULT_INTERVAL = 600  # 秒（10分ごと）
MIN_INTERVAL = 30       # 最小30秒
MAX_INTERVAL = 3600     # 最大1時間

class ZenMasterNotifier(Thread):
    def __init__(self, interval=DEFAULT_INTERVAL, stop_event=None):
        super().__init__()
        self.interval = interval
        self.stop_event = stop_event or Event()
        self.running = False

    def run(self):
        self.running = True
        while not self.stop_event.is_set():
            message = random.choice(ZEN_MESSAGES)
            try:
                notification.notify(
                    title='偽OS禅マスター',
                    message=message,
                    app_name='fake-os-zen-master-alert',
                    timeout=10
                )
            except Exception as e:
                print(f'通知エラー: {e}')
            # ランダムなタイミングも混ぜる
            sleep_time = random.randint(int(self.interval*0.8), int(self.interval*1.2))
            for _ in range(sleep_time):
                if self.stop_event.is_set():
                    break
                time.sleep(1)
        self.running = False

    def stop(self):
        self.stop_event.set()


def list_messages():
    print('--- 禅マスター通知メッセージ一覧 ---')
    for i, msg in enumerate(ZEN_MESSAGES, 1):
        print(f'{i:2}: {msg}')


def send_once():
    message = random.choice(ZEN_MESSAGES)
    try:
        notification.notify(
            title='偽OS禅マスター',
            message=message,
            app_name='fake-os-zen-master-alert',
            timeout=10
        )
        print(f'[通知] {message}')
    except Exception as e:
        print(f'通知エラー: {e}')


def main():
    parser = argparse.ArgumentParser(description='fake-os-zen-master-alert: 禅マスター通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    # サブコマンド: start (常駐)
    p_start = subparsers.add_parser('start', help='定期的に禅マスター通知を表示（デフォルト10分ごと）')
    p_start.add_argument('--interval', type=int, default=DEFAULT_INTERVAL, help='通知間隔（秒, 30〜3600）')

    # サブコマンド: once (1回だけ通知)
    subparsers.add_parser('once', help='1回だけ禅マスター通知を表示')

    # サブコマンド: list (メッセージ一覧)
    subparsers.add_parser('list', help='禅マスター通知メッセージ一覧を表示')

    args = parser.parse_args()

    if args.command == 'start':
        interval = args.interval
        if interval < MIN_INTERVAL or interval > MAX_INTERVAL:
            print(f'通知間隔は{MIN_INTERVAL}〜{MAX_INTERVAL}秒の範囲で指定してください。')
            sys.exit(1)
        print(f'fake-os-zen-master-alert: {interval}秒ごとに禅マスター通知を表示します。停止はCtrl+C')
        stop_event = Event()
        notifier = ZenMasterNotifier(interval=interval, stop_event=stop_event)
        try:
            notifier.start()
            while notifier.running:
                time.sleep(1)
        except KeyboardInterrupt:
            print('\n停止中...')
            notifier.stop()
            notifier.join()
        print('終了しました。')
    elif args.command == 'once':
        send_once()
    elif args.command == 'list':
        list_messages()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
