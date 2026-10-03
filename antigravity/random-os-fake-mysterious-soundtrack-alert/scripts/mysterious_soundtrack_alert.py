import sys
import random
import argparse
import platform
import subprocess
from typing import List

BGM_TITLES = [
    '第3会議室の静寂',
    'Cドライブ幻想曲',
    '未定義変数のバラード',
    'システム再起動前夜',
    '仮想デスクトップの黄昏',
    'メモリ解放の祈り',
    'タスクスケジューラの夢',
    'ログイン画面の彼方',
    'バックアップ未完のエチュード',
    'プロセス監視者の夜',
    'カーネルパニック小夜曲',
    'バッテリー残量のワルツ',
    'ファイルハンドルの迷宮',
    'セーフモードの残響',
    '未保存ドキュメントのレクイエム',
    'シェルプロンプトの微笑み',
    '仮想環境の幻影',
    'パーミッション拒否の子守唄',
    'ネットワーク遅延のカノン',
    'アップデート待機の無音'
]

NOTIFY_TITLE = 'OS公式通知'
NOTIFY_PREFIX = '本日の作業用BGM推奨: '


def pick_random_title() -> str:
    return random.choice(BGM_TITLES)


def send_notification(message: str):
    system = platform.system()
    try:
        if system == 'Darwin':
            # macOS: osascript
            script = f'display notification "{message}" with title "{NOTIFY_TITLE}"'
            subprocess.run(['osascript', '-e', script], check=True)
        elif system == 'Linux':
            # Linux: notify-send
            subprocess.run(['notify-send', NOTIFY_TITLE, message], check=True)
        elif system == 'Windows':
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(NOTIFY_TITLE, message, duration=5, threaded=True)
            except ImportError:
                # Fallback: print to terminal
                print(f'[{NOTIFY_TITLE}] {message}')
        else:
            # Unknown OS: fallback
            print(f'[{NOTIFY_TITLE}] {message}')
    except Exception as e:
        print(f'[{NOTIFY_TITLE}] {message}')
        print(f'通知送信失敗: {e}', file=sys.stderr)


def print_terminal(message: str):
    print(f'[{NOTIFY_TITLE}] {message}')


def alert_once(to_terminal: bool = False):
    title = pick_random_title()
    message = f'『{title}』'
    if to_terminal:
        print_terminal(NOTIFY_PREFIX + message)
    else:
        send_notification(NOTIFY_PREFIX + message)


def alert_batch(count: int = 5, to_terminal: bool = False):
    for _ in range(count):
        alert_once(to_terminal=to_terminal)


def list_titles():
    for t in BGM_TITLES:
        print(f'- {t}')


def parse_args():
    parser = argparse.ArgumentParser(description='OS謎BGM推奨通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_once = subparsers.add_parser('once', help='1回だけ通知')
    parser_once.add_argument('--terminal', action='store_true', help='ターミナル出力のみ')

    parser_batch = subparsers.add_parser('batch', help='複数回通知')
    parser_batch.add_argument('-n', '--number', type=int, default=5, help='通知回数')
    parser_batch.add_argument('--terminal', action='store_true', help='ターミナル出力のみ')

    parser_list = subparsers.add_parser('list', help='BGMタイトル一覧を表示')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'once':
        alert_once(to_terminal=args.terminal)
    elif args.command == 'batch':
        alert_batch(count=args.number, to_terminal=args.terminal)
    elif args.command == 'list':
        list_titles()
    else:
        print('コマンドを指定してください (once, batch, list)', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
