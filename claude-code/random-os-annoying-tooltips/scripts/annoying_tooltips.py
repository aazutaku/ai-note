import sys
import time
import random
import argparse
import threading
from datetime import datetime, timedelta

try:
    from plyer import notification
except ImportError:
    print('plyerパッケージが必要です。pip install plyer でインストールしてください。')
    sys.exit(1)

# うざいツールチップメッセージ集
TOOLTIPS = [
    'CapsLockが押されているかもしれません。',
    '今すぐアップデートしませんか？',
    '入力速度が先週より5%低下しています。',
    '休憩を取るタイミングかもしれません。',
    'あなたのクリップボードがいっぱいです。',
    'このウィンドウは本当に必要ですか？',
    'バッテリー残量は確認しましたか？',
    '再起動することで問題が解決するかもしれません。',
    '不要なファイルが溜まっていませんか？',
    'あなたのマウス移動距離が本日最小です。',
    '今こそバックアップを取りましょう。',
    'ネットワーク速度が平均より遅いようです。',
    '新しいフォントを試してみませんか？',
    'このタイミングで設定を見直しませんか？',
    'もう一度やり直してみませんか？',
    'ヘルプが必要ですか？',
    'タスクバーが散らかっています。',
    'ウィンドウを整理しましょう。',
    'あなたの入力方法が非効率かもしれません。',
    'この通知は無視しても構いません。',
]

# 通知履歴の管理
class TooltipLogger:
    def __init__(self):
        self.history = []
    def log(self, msg):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.history.append({'time': now, 'msg': msg})
    def list(self, limit=10):
        return self.history[-limit:]
    def summary(self):
        return {'count': len(self.history)}

def send_tooltip(msg, logger):
    notification.notify(
        title='うざいOS風ツールチップ',
        message=msg,
        timeout=8
    )
    logger.log(msg)

def random_interval(min_sec=90, max_sec=600):
    return random.randint(min_sec, max_sec)

def annoy_loop(logger, stop_event, min_sec=90, max_sec=600):
    while not stop_event.is_set():
        msg = random.choice(TOOLTIPS)
        send_tooltip(msg, logger)
        interval = random_interval(min_sec, max_sec)
        for _ in range(interval):
            if stop_event.is_set():
                break
            time.sleep(1)

def cli_log(logger, args):
    for item in logger.list(args.limit):
        print(f"[{item['time']}] {item['msg']}")

def cli_summary(logger, args):
    s = logger.summary()
    print(f"通知回数: {s['count']}")

def cli_list(logger, args):
    cli_log(logger, args)

def main():
    parser = argparse.ArgumentParser(description='OS風うざいツールチップ通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    run_parser = subparsers.add_parser('run', help='バックグラウンドでうざい通知を表示')
    run_parser.add_argument('--min', type=int, default=90, help='通知の最小間隔(秒)')
    run_parser.add_argument('--max', type=int, default=600, help='通知の最大間隔(秒)')

    log_parser = subparsers.add_parser('log', help='通知履歴を表示')
    log_parser.add_argument('--limit', type=int, default=10, help='表示件数')

    summary_parser = subparsers.add_parser('summary', help='通知回数のサマリを表示')

    args = parser.parse_args()
    logger = TooltipLogger()

    if args.command == 'run' or args.command is None:
        stop_event = threading.Event()
        try:
            print('うざい通知を開始します。Ctrl+Cで停止。')
            annoy_loop(logger, stop_event, min_sec=getattr(args, 'min', 90), max_sec=getattr(args, 'max', 600))
        except KeyboardInterrupt:
            stop_event.set()
            print('\n通知を停止しました。')
    elif args.command == 'log':
        cli_log(logger, args)
    elif args.command == 'summary':
        cli_summary(logger, args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
