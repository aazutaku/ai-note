import random
import argparse
import sys
import os
import time
from datetime import datetime

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

LOG_PATH = os.path.expanduser('~/.os_fake_legendary_item_drop_alert.log')

LEGENDARY_ITEMS = [
    '伝説のスペースキー（+5）',
    '未鑑定のUSBメモリ',
    '古代のタブキー（発掘済）',
    '神話級NumLockボタン',
    '謎のマウスホイール',
    'バグ封じのCtrlキー',
    'OSの守護者ドングル',
    '時空を超えたF5キー',
    'エンジニアの涙入りSDカード',
    '未知のBluetoothアダプタ',
    '伝説のCapsLockキー（+3）',
    '神話の電源ボタン',
    '謎のPCリセットスイッチ',
    '古文書化したREADME.txt',
    '未発見のAltキー'
]

RARITIES = [
    ('コモン', '通常'),
    ('レア', '珍しい'),
    ('伝説', '非常に珍しい'),
    ('神話級', '超激レア')
]

EFFECTS = [
    'タイプミス抑制率+20%',
    'コード整形力+10',
    'バグ発生率-5%',
    '集中力持続+15分',
    'CPU温度-2℃',
    '未鑑定',
    '起動速度+3%',
    '謎の安心感',
    'デバッグ力+7',
    '使用未確認',
    'クラッシュ耐性+1',
    'やる気+5',
    '未知の効果',
    'エラー通知無効化'
]


def generate_drop():
    item = random.choice(LEGENDARY_ITEMS)
    rarity, rarity_desc = random.choice(RARITIES)
    effect = random.choice(EFFECTS)
    lines = [
        '[OS伝説アイテムドロップ通知]',
        f'{item}を拾いました！',
        f'レアリティ: {rarity}',
        f'効果: {effect}'
    ]
    return '\n'.join(lines)


def send_notification(title, message):
    if PLYER_AVAILABLE:
        try:
            notification.notify(
                title=title,
                message=message,
                timeout=6
            )
        except Exception as e:
            print(f'[通知失敗] {e}', file=sys.stderr)
    else:
        # Fallback: print to terminal
        print(f'{title}\n{message}')


def log_drop(message):
    try:
        with open(LOG_PATH, 'a', encoding='utf-8') as f:
            f.write(f'[{datetime.now().isoformat()}]\n{message}\n\n')
    except Exception as e:
        print(f'[ログ書込失敗] {e}', file=sys.stderr)


def list_logs():
    if not os.path.exists(LOG_PATH):
        print('まだドロップ履歴はありません。')
        return
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        print(f.read())

def summary_logs():
    if not os.path.exists(LOG_PATH):
        print('まだドロップ履歴はありません。')
        return
    rarity_count = {r[0]: 0 for r in RARITIES}
    total = 0
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            for rarity, _ in RARITIES:
                if f'レアリティ: {rarity}' in line:
                    rarity_count[rarity] += 1
                    total += 1
    print(f'合計ドロップ数: {total}')
    for rarity in rarity_count:
        print(f'{rarity}: {rarity_count[rarity]}')


def main():
    parser = argparse.ArgumentParser(description='OS伝説アイテムドロップ通知スキル')
    subparsers = parser.add_subparsers(dest='command', help='サブコマンド')

    drop_parser = subparsers.add_parser('drop', help='伝説アイテムドロップ通知を即時発動')
    list_parser = subparsers.add_parser('list', help='過去のドロップ履歴を表示')
    summary_parser = subparsers.add_parser('summary', help='ドロップ履歴のサマリーを表示')
    auto_parser = subparsers.add_parser('auto', help='一定間隔で自動ドロップ通知 (Ctrl+Cで停止)')
    auto_parser.add_argument('--interval', type=int, default=1800, help='通知間隔[秒] (デフォルト: 1800)')

    args = parser.parse_args()

    if args.command == 'drop' or args.command is None:
        message = generate_drop()
        send_notification('OS伝説アイテムドロップ通知', message)
        log_drop(message)
    elif args.command == 'list':
        list_logs()
    elif args.command == 'summary':
        summary_logs()
    elif args.command == 'auto':
        print('自動ドロップ通知を開始します。Ctrl+Cで停止。')
        try:
            while True:
                message = generate_drop()
                send_notification('OS伝説アイテムドロップ通知', message)
                log_drop(message)
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print('\n自動通知を停止しました。')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
