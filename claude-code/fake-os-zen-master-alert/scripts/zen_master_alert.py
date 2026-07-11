import argparse
import random
import sys
import time
import threading
from plyer import notification

ZEN_MESSAGES = [
    'バグとは何かを問う前に、己を問え。',
    '今日の悟り：if文を捨てよ、道は開ける。',
    'コンパイルに失敗したとき、木魚を叩け。',
    'エラーの数だけ、悟りの道は続く。',
    '眠気と戦うより、眠気を受け入れよ。',
    'コードを読む前に、心を整えよ。',
    'OSとは、心の窓である。',
    'デバッグの道は、無限である。',
    'print文を捨てよ、禅を取れ。',
    'バグは敵にあらず、師である。',
    'エディタを閉じる勇気を持て。',
    '何も書かぬことも、またコードなり。',
    'エラーを恐れるな、恐れをエラーと知れ。',
    '悟りはREADMEに記されず。',
    'タイポは心の乱れ。',
    'ビルド失敗は、宇宙の調和の乱れ。',
    '変数名に悩む時、己の名を思い出せ。',
    'if文の数だけ、迷いが増す。',
    'whileループは人生そのもの。',
    'コメントを書くより、沈黙を選べ。'
]

DEFAULT_INTERVAL = 900  # 15分
MIN_INTERVAL = 60       # 1分
MAX_INTERVAL = 7200     # 2時間

class ZenMasterAlert:
    def __init__(self, interval=DEFAULT_INTERVAL):
        self.interval = max(MIN_INTERVAL, min(MAX_INTERVAL, interval))
        self.running = False
        self.thread = None

    def send_alert(self):
        msg = random.choice(ZEN_MESSAGES)
        notification.notify(
            title='禅マスター',
            message=msg,
            app_name='Fake OS Zen Master',
            timeout=8
        )
        print(f"[禅マスター] {msg}")

    def start(self):
        if self.running:
            print("すでに禅マスター通知は動作中です。")
            return
        self.running = True
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()
        print(f"禅マスター通知を開始しました（{self.interval}秒間隔）。Ctrl+Cで停止できます。")

    def _run(self):
        while self.running:
            self.send_alert()
            for _ in range(self.interval):
                if not self.running:
                    break
                time.sleep(1)

    def stop(self):
        if not self.running:
            print("禅マスター通知は停止中です。")
            return
        self.running = False
        if self.thread:
            self.thread.join(timeout=2)
        print("禅マスター通知を停止しました。")

    def once(self):
        self.send_alert()


def parse_args():
    parser = argparse.ArgumentParser(description='Fake OS Zen Master Alert')
    subparsers = parser.add_subparsers(dest='command')

    # onコマンド
    parser_on = subparsers.add_parser('on', help='禅マスター通知を開始')
    parser_on.add_argument('--interval', type=int, default=DEFAULT_INTERVAL, help='通知間隔（秒）')

    # offコマンド
    subparsers.add_parser('off', help='禅マスター通知を停止')

    # onceコマンド
    subparsers.add_parser('once', help='1回だけ禅マスター通知を送信')

    # statusコマンド
    subparsers.add_parser('status', help='禅マスター通知の状態を表示')

    return parser.parse_args()


def main():
    args = parse_args()
    # グローバルな状態管理は簡易的にファイルで実装
    state_file = '.zen_master_alert_state'

    if args.command == 'on':
        with open(state_file, 'w') as f:
            f.write('on')
        alert = ZenMasterAlert(interval=args.interval)
        try:
            alert.start()
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            alert.stop()
            with open(state_file, 'w') as f:
                f.write('off')
    elif args.command == 'off':
        with open(state_file, 'w') as f:
            f.write('off')
        print('禅マスター通知を停止しました。')
    elif args.command == 'once':
        alert = ZenMasterAlert(interval=DEFAULT_INTERVAL)
        alert.once()
    elif args.command == 'status':
        try:
            with open(state_file, 'r') as f:
                state = f.read().strip()
            print(f'禅マスター通知の状態: {state}')
        except FileNotFoundError:
            print('禅マスター通知の状態: 不明（未開始）')
    else:
        print('コマンドを指定してください。 --help を参照')

if __name__ == '__main__':
    main()
