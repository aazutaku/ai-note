import random
import sys
import argparse
import time

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

# 曲名構成要素
PREFIXES = [
    '第3会議室の', 'Cドライブ', '未定義変数の', 'リファクタリングの', 'エラーコードの',
    '仮想マシンの', 'バッファオーバーフローの', 'デバッグ中の', 'メモリリークの', '再起動前の',
    'システム管理者の', 'バックアップ中の', 'ログファイルの', 'セグメンテーション違反の', 'タイムアウトの',
    'カーネルパニックの', 'アップデート前夜の', 'パーミッションの', 'プロセス監視の', 'ネットワーク遅延の'
]
SUFFIXES = [
    '静寂', '幻想曲', 'バラード', '夜明け', 'ワルツ', '協奏曲', 'エチュード', 'ノクターン', 'マーチ', 'カプリッチョ',
    'レクイエム', '即興曲', 'ソナタ', 'フーガ', 'セレナーデ', '変奏曲', 'カンタータ', '前奏曲', '小夜曲', '狂詩曲'
]

# 通知タイトル
NOTIFY_TITLE = 'OS公式通知'

# 通知/出力本体
def generate_title():
    prefix = random.choice(PREFIXES)
    suffix = random.choice(SUFFIXES)
    return f'{prefix}{suffix}'

def notify(title):
    message = f'本日の作業用BGM: 『{title}』'
    if PLYER_AVAILABLE:
        try:
            notification.notify(
                title=NOTIFY_TITLE,
                message=message,
                timeout=5
            )
        except Exception as e:
            print(f'[通知失敗] {message} ({e})')
            print(f'[OS公式通知] {message}')
    else:
        print(f'[OS公式通知] {message}')

# 履歴管理（メモリのみ）
class AlertHistory:
    def __init__(self):
        self.entries = []
    def add(self, title, timestamp=None):
        if timestamp is None:
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.entries.append({'title': title, 'time': timestamp})
    def list(self):
        return self.entries
    def summary(self):
        return f'通知回数: {len(self.entries)}'

# CLIサブコマンド

def main():
    parser = argparse.ArgumentParser(description='謎のOS公式BGM通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='1回だけBGM通知を表示')
    parser_alert.add_argument('--count', '-n', type=int, default=1, help='通知回数')
    parser_alert.add_argument('--interval', '-i', type=float, default=0, help='通知間隔(秒)')

    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知回数サマリ表示')

    args = parser.parse_args()
    history = AlertHistory()

    if args.command == 'alert':
        for _ in range(args.count):
            title = generate_title()
            notify(title)
            history.add(title)
            if args.interval > 0 and _ != args.count - 1:
                time.sleep(args.interval)
    elif args.command == 'list':
        entries = history.list()
        if not entries:
            print('通知履歴はありません')
        else:
            for e in entries:
                print(f"[{e['time']}] 『{e['title']}』")
    elif args.command == 'summary':
        print(history.summary())
    else:
        # デフォルト: 1回通知
        title = generate_title()
        notify(title)
        history.add(title)

if __name__ == '__main__':
    main()
