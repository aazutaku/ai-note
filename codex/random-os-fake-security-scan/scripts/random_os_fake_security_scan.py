import sys
import time
import random
import argparse
from threading import Thread

try:
    from plyer import notification
except ImportError:
    print('plyerモジュールが必要です。pip install plyer でインストールしてください。')
    sys.exit(1)

FAKE_WARNINGS = [
    '未知のやる気ウイルスを検出しました',
    'マウスの動きが怪しいです',
    'あなたの進捗は安全です',
    '謎のプロセス「motivation.exe」を発見',
    'CPU温度がやる気に反応しています',
    'メモリ内に「集中力」が不足しています',
    'カフェイン濃度が規定値を下回っています',
    'あなたのキーボード入力速度は正常です',
    '進捗バーが迷子になりました',
    '重大な問題は見つかりませんでした'
]

SCAN_TITLES = [
    'セキュリティスキャン開始',
    'セキュリティスキャン進行中',
    'セキュリティスキャン完了'
]

RESULTS = [
    '重大な問題は見つかりませんでした',
    'やる気ウイルスは自己解決しました',
    'あなたの進捗は安全圏です',
    '警告は全てジョークです'
]

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=3
    )

def random_scan_sequence(verbose=False):
    progress = 0
    steps = random.randint(5, 8)
    increments = sorted(random.sample(range(10, 100), steps - 1)) + [100]
    last = 0
    for idx, val in enumerate(increments):
        time.sleep(random.uniform(1.5, 2.5))
        progress = val
        if progress < 100:
            title = SCAN_TITLES[1] if idx > 0 else SCAN_TITLES[0]
            warning = random.choice(FAKE_WARNINGS)
            msg = f'進捗: {progress}%\n警告: {warning}'
        else:
            title = SCAN_TITLES[2]
            result = random.choice(RESULTS)
            msg = f'進捗: 100%\n結果: {result}'
        send_notification(title, msg)
        if verbose:
            print(f'[{title}] {msg.replace(chr(10), " ")}', flush=True)

def list_warnings():
    print('--- フェイク警告一覧 ---')
    for w in FAKE_WARNINGS:
        print(f'- {w}')

def summary():
    print('このSkillは、作業中にフェイクのセキュリティスキャン通知をデスクトップに表示します。')
    print('通知内容・進捗は毎回ランダム生成され、実際のウイルス検出は行いません。')
    print('詳細は --help または SKILL.md を参照してください。')

def main():
    parser = argparse.ArgumentParser(description='random-os-fake-security-scan: フェイクOSセキュリティスキャン通知を表示')
    subparsers = parser.add_subparsers(dest='command')

    scan_parser = subparsers.add_parser('scan', help='フェイクスキャンを開始')
    scan_parser.add_argument('--verbose', action='store_true', help='進行状況を標準出力にも表示')

    list_parser = subparsers.add_parser('list', help='警告メッセージ一覧を表示')
    summary_parser = subparsers.add_parser('summary', help='Skillの概要を表示')

    args = parser.parse_args()
    if args.command == 'scan' or args.command is None:
        # デフォルトはscan
        random_scan_sequence(verbose=getattr(args, 'verbose', False))
    elif args.command == 'list':
        list_warnings()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
