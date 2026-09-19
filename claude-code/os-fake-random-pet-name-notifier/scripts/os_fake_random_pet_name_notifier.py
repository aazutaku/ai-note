import random
import time
import argparse
import sys
import threading

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

# デバイス名と二つ名パターン
DEVICES = [
    'マウス', 'キーボード', 'モニター', 'USBハブ', 'Webカメラ', 'スピーカー', 'マイク', 'プリンター', '外付けHDD', 'トラックパッド', 'ルーター', 'ヘッドフォン', 'タブレット', 'スマートフォン', 'ゲームパッド'
]

NICKNAME_PATTERNS = [
    '{adj1}{adj2}の{noun}',
    '{adj1}なる{noun}',
    '{adj1}の{noun}',
    '{noun1}の{noun2}',
    '{adj1}{noun1}',
    '{adj1}し{noun1}',
]

ADJ1 = [
    '疾風', '静寂', '闇夜', '無限', '見守る', '孤高', '気まぐれ', '不屈', '眠れる', '閃光', '鉄壁', '漂泊', '忍耐', '爆速', '神秘', '不思議', '伝説', '蒼穹', '深淵', '不滅'
]

ADJ2 = [
    'なる', 'し', 'の', 'たる', 'を纏う', 'にして', 'を宿す', 'を操る', 'のごとき', 'を超えし'
]

NOUNS = [
    'コロンブス', '鉄槌', '覗き魔', '賢者', '千里眼', '守護者', '魔術師', '旅人', '探求者', '暴君', '詩人', '王', '忍者', '巨人', '狩人', '幻影', '怪盗', '執行者', '導師', '預言者'
]

def generate_nickname():
    pattern = random.choice(NICKNAME_PATTERNS)
    adj1 = random.choice(ADJ1)
    adj2 = random.choice(ADJ2)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    noun = random.choice(NOUNS)
    return pattern.format(adj1=adj1, adj2=adj2, noun=noun, noun1=noun1, noun2=noun2)

def generate_message():
    device = random.choice(DEVICES)
    nickname = generate_nickname()
    templates = [
        f'あなたの{device}は本日より「{nickname}」と命名されました。',
        f'{device}の新しい名は「{nickname}」です。',
        f'{device}の公式ペット名：「{nickname}」',
        f'{device}は「{nickname}」となりました。',
        f'あなたの{device}は「{nickname}」になりました。',
    ]
    return random.choice(templates)

def notify(message, title='OS通知'):
    if PLYER_AVAILABLE:
        try:
            notification.notify(
                title=title,
                message=message,
                timeout=5
            )
        except Exception as e:
            print(f'[通知失敗] {e}', file=sys.stderr)
            print(f'[OS通知] {message}')
    else:
        print(f'[OS通知] {message}')

def run_random_notifier(interval_min=300, interval_max=1200, stop_event=None):
    while True:
        wait = random.randint(interval_min, interval_max)
        for _ in range(wait):
            if stop_event and stop_event.is_set():
                return
            time.sleep(1)
        message = generate_message()
        notify(message)

def list_sample_messages(count=10):
    for _ in range(count):
        print('[OS通知]', generate_message())

def main():
    parser = argparse.ArgumentParser(description='OS Fake Random Pet Name Notifier')
    subparsers = parser.add_subparsers(dest='command', help='サブコマンド')

    parser_run = subparsers.add_parser('run', help='ランダムなタイミングで通知を表示')
    parser_run.add_argument('--min', type=int, default=300, help='最小通知間隔(秒)')
    parser_run.add_argument('--max', type=int, default=1200, help='最大通知間隔(秒)')

    parser_once = subparsers.add_parser('once', help='1回だけ通知を表示')

    parser_list = subparsers.add_parser('list', help='サンプル通知を複数表示')
    parser_list.add_argument('--count', type=int, default=10, help='表示数')

    args = parser.parse_args()
    if args.command == 'run':
        stop_event = threading.Event()
        try:
            run_random_notifier(interval_min=args.min, interval_max=args.max, stop_event=stop_event)
        except KeyboardInterrupt:
            stop_event.set()
            print('\n[終了] 通知スレッドを停止しました')
    elif args.command == 'once':
        notify(generate_message())
    elif args.command == 'list':
        list_sample_messages(args.count)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
