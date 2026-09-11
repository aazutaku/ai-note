import random
import time
import sys
import argparse
import threading
import platform

try:
    from plyer import notification
except ImportError:
    notification = None

ITEM_NAMES = [
    '伝説のスペースキー+5',
    '謎のUSBメモリ（未鑑定）',
    '古代のタブキー（発掘済）',
    '未登録のマウスホイール',
    '呪われたCapsLockキー',
    '幻のNumPad（右手専用）',
    '神速のEnterキー',
    '未知のファンクションキーF13',
    'バグったShiftキー',
    '時空を超えたESCキー',
    '未発見のPrintScreen',
    '伝説のコマンドプロンプト',
    '謎のSDカード（容量不明）',
    '消えたパーティション',
    '古代のBIOSチップ',
    '未鑑定のRAMスティック',
    '幻のUSB Type-Z',
    '壊れかけのBluetoothアダプタ',
    '伝説のマウスパッド',
    '未知のOSインストーラUSB'
]

RARITY_LIST = [
    ('★☆☆☆☆', 'コモン'),
    ('★★☆☆☆', 'アンコモン'),
    ('★★★☆☆', 'レア'),
    ('★★★★☆', 'スーパーレア'),
    ('★★★★★', 'レジェンダリー')
]

EFFECTS = [
    '使うと何かが起こる気がする',
    '空白挿入速度が超絶UP',
    'コード整形力+2',
    'バグ発生率-10%',
    '未鑑定：効果不明',
    '再起動速度が微妙に向上',
    'タスク切り替え力+1',
    '謎の安心感が得られる',
    'デバッグ成功率+5%',
    '運気が上昇する気がする',
    '一時的に集中力+3',
    'ショートカットキーが覚えやすくなる',
    '何も起こらない',
    'エラー回避率+2%',
    '未知の効果を発揮する'
]

HISTORY = []


def generate_item():
    name = random.choice(ITEM_NAMES)
    rarity, rarity_name = random.choices(RARITY_LIST, weights=[30, 25, 20, 15, 10])[0]
    effect = random.choice(EFFECTS)
    return {
        'name': name,
        'rarity': rarity,
        'rarity_name': rarity_name,
        'effect': effect
    }


def format_alert(item):
    lines = [
        '[伝説アイテムドロップ通知]',
        f'アイテム: {item["name"]}',
        f'レア度: {item["rarity"]}',
        f'効果: {item["effect"]}'
    ]
    return '\n'.join(lines)


def show_notification(item):
    title = '伝説アイテムドロップ通知'
    message = f'{item["name"]}\nレア度: {item["rarity"]}\n効果: {item["effect"]}'
    if notification:
        try:
            notification.notify(title=title, message=message, app_name='Legendary Item Drop', timeout=7)
        except Exception as e:
            print(f'[通知失敗] {e}')
    else:
        print(format_alert(item))


def log_item(item):
    ts = time.strftime('%Y-%m-%d %H:%M:%S')
    HISTORY.append({'timestamp': ts, **item})


def list_history():
    if not HISTORY:
        print('アイテムドロップ履歴はありません')
        return
    for entry in HISTORY:
        print(f"[{entry['timestamp']}] {entry['name']} ({entry['rarity']}) - {entry['effect']}")


def summary():
    if not HISTORY:
        print('アイテムドロップ履歴はありません')
        return
    rarity_count = {}
    for entry in HISTORY:
        rarity = entry['rarity']
        rarity_count[rarity] = rarity_count.get(rarity, 0) + 1
    print('レア度別ドロップ数:')
    for rarity, count in sorted(rarity_count.items(), key=lambda x: -x[1]):
        print(f'{rarity}: {count}回')


def drop_alert():
    item = generate_item()
    log_item(item)
    show_notification(item)


def auto_drop_alert(interval_min=20, interval_max=50, stop_event=None):
    while not (stop_event and stop_event.is_set()):
        interval = random.randint(interval_min, interval_max)
        time.sleep(interval)
        drop_alert()


def main():
    parser = argparse.ArgumentParser(description='伝説アイテムドロップ通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='手動でアイテムドロップ通知を表示')
    parser_auto = subparsers.add_parser('auto', help='一定間隔で自動ドロップ通知を開始')
    parser_auto.add_argument('--min', type=int, default=20, help='最小通知間隔（秒）')
    parser_auto.add_argument('--max', type=int, default=50, help='最大通知間隔（秒）')
    parser_list = subparsers.add_parser('list', help='ドロップ履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='レア度別ドロップ統計')

    args = parser.parse_args()

    if args.command == 'log':
        drop_alert()
    elif args.command == 'auto':
        stop_event = threading.Event()
        try:
            print('自動ドロップ通知を開始します。Ctrl+Cで停止。')
            auto_drop_alert(interval_min=args.min, interval_max=args.max, stop_event=stop_event)
        except KeyboardInterrupt:
            print('\n自動通知を停止しました')
            stop_event.set()
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
