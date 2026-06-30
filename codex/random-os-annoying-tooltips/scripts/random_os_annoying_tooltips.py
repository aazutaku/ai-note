import sys
import time
import random
import argparse
from datetime import datetime, timedelta

try:
    from plyer import notification
except ImportError:
    print('plyerパッケージが必要です。pip install plyer でインストールしてください。')
    sys.exit(1)

TOOLTIPS = [
    'CapsLockが押されているかもしれません。',
    '今アップデートしませんか？（推奨: 今すぐ再起動）',
    'あなたの入力速度、気づいてますか？',
    'ファイルを保存していないようです。',
    'ネットワークが不安定かもしれません。',
    'システムの空き容量が残りわずかです。',
    'この操作は本当に必要ですか？',
    'バッテリー残量が気になりませんか？',
    '定期的な休憩をおすすめします。',
    'マウスの動きが少ないようです。',
    'ウイルススキャンの時期です。',
    '設定を初期化しますか？',
    'ログイン情報を再入力してください。',
    'プリンタが接続されていません。',
    '重要な更新プログラムがあります。',
    '時計がずれている可能性があります。',
    'クラウド同期が停止しています。',
    '新しいデバイスを検出しました。',
    '古いファイルがゴミ箱に残っています。',
    'タスクバーがいっぱいです。'
]

MIN_INTERVAL = 60  # 秒
LAST_NOTIFY_FILE = '/tmp/random_os_annoying_tooltips_last_notify.txt'


def can_notify():
    try:
        with open(LAST_NOTIFY_FILE, 'r') as f:
            last = float(f.read().strip())
            if time.time() - last < MIN_INTERVAL:
                return False
    except Exception:
        pass
    return True

def update_last_notify():
    try:
        with open(LAST_NOTIFY_FILE, 'w') as f:
            f.write(str(time.time()))
    except Exception:
        pass

def show_tooltip(msg=None, dry_run=False):
    if not can_notify():
        return False
    if msg is None:
        msg = random.choice(TOOLTIPS)
    if dry_run:
        print(f'[通知] {msg}')
    else:
        notification.notify(
            title='OSからのお知らせ',
            message=msg,
            app_name='random-os-annoying-tooltips',
            timeout=6
        )
    update_last_notify()
    return True

def list_tooltips():
    for i, msg in enumerate(TOOLTIPS, 1):
        print(f'{i:2d}: {msg}')

def summary():
    print('=== random-os-annoying-tooltips summary ===')
    print(f'通知候補数: {len(TOOLTIPS)}')
    try:
        with open(LAST_NOTIFY_FILE, 'r') as f:
            last = float(f.read().strip())
            last_dt = datetime.fromtimestamp(last)
            print(f'前回通知: {last_dt.strftime("%Y-%m-%d %H:%M:%S")}
(最小間隔: {MIN_INTERVAL}秒)')
    except Exception:
        print('前回通知: 不明')
    print('通知間隔制御: あり')
    print('環境依存: plyer通知API (主要OS対応)')

def main():
    parser = argparse.ArgumentParser(description='random-os-annoying-tooltips: OS風うざい通知を表示')
    subparsers = parser.add_subparsers(dest='command')

    parser_notify = subparsers.add_parser('notify', help='即座にうざい通知を1つ表示')
    parser_notify.add_argument('--dry-run', action='store_true', help='実際には通知せずstdoutに出力')
    parser_notify.add_argument('--msg', type=str, help='通知メッセージを指定')

    parser_list = subparsers.add_parser('list', help='通知候補一覧を表示')
    parser_summary = subparsers.add_parser('summary', help='通知履歴と設定概要を表示')
    parser_run = subparsers.add_parser('run', help='一定間隔で自動的にうざい通知を表示')
    parser_run.add_argument('--interval', type=int, default=300, help='通知間隔(秒, デフォルト5分)')
    parser_run.add_argument('--dry-run', action='store_true', help='実際には通知せずstdoutに出力')

    args = parser.parse_args()

    if args.command == 'notify':
        show_tooltip(msg=args.msg, dry_run=args.dry_run)
    elif args.command == 'list':
        list_tooltips()
    elif args.command == 'summary':
        summary()
    elif args.command == 'run':
        print('random-os-annoying-tooltips: 自動通知モード開始')
        try:
            while True:
                if can_notify():
                    show_tooltip(dry_run=args.dry_run)
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print('\n自動通知モード終了')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
