import random
import time
import argparse
import sys
from threading import Thread
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

DEVICES = [
    'マウス', 'キーボード', 'ディスプレイ', 'USBメモリ', 'スピーカー',
    'Webカメラ', 'プリンター', 'タッチパッド', 'マイク', 'ヘッドフォン',
    'ノートPC', 'デスクトップ', 'ルーター', 'ハードディスク', 'グラフィックボード',
    'ゲームコントローラー', 'スマートフォン', 'タブレット', 'SDカード', '外付けSSD'
]

TITLES = [
    '疾風のコロンブス', '静寂なる鉄槌', '蒼穹の監視者', '記憶の旅人', '雷鳴の詩人',
    '銀河の案内人', '孤高の守護者', '無敵の参謀', '夜明けの伝道師', '緋色の彗星',
    '電脳の魔術師', '月影の探求者', '不屈の航海士', '旋律の錬金術師', '蒼炎の紳士',
    '夢見る彫刻家', '時空の旅人', '静謐なる監督者', '閃光の観測者', '鉄壁の門番',
    '霧中の道化師', '深淵の観察者', '星降る語り部', '氷上の舞踏家', '暁の預言者',
    '孤独な詩人', '風切る伝令', '無音の奏者', '鉄槌の守人', '流星の案内人'
]

MESSAGES = [
    'あなたの{device}は本日より「{title}」と命名されました。',
    '{device}の新しい名は「{title}」です。',
    '{device}の称号: 「{title}」',
    '{device}は今後「{title}」と呼ばれます。',
    '{device}の名は「{title}」になりました。',
    '祝！{device}が「{title}」の称号を獲得しました。',
    '公式通知: {device}の二つ名は「{title}」です。',
    '{device}が「{title}」として登録されました。',
    '本日より{device}は「{title}」に昇格しました。',
    '{device}の名誉称号「{title}」を授与します。'
]

VERSION = '1.0.0'

class Notifier:
    def __init__(self, use_os_notify=True, dry_run=False):
        self.use_os_notify = use_os_notify and PLYER_AVAILABLE
        self.dry_run = dry_run

    def notify(self, message):
        if self.use_os_notify:
            try:
                notification.notify(
                    title='OS通知',
                    message=message,
                    app_name='PetNameNotifier',
                    timeout=6
                )
            except Exception as e:
                print(f'[通知失敗] {message} ({e})')
                print(message)
        else:
            print(f'[OS通知] {message}')

    def random_pet_name(self):
        device = random.choice(DEVICES)
        title = random.choice(TITLES)
        template = random.choice(MESSAGES)
        return template.format(device=device, title=title)

    def run_once(self):
        msg = self.random_pet_name()
        self.notify(msg)

    def run_random_loop(self, min_sec=60, max_sec=600):
        try:
            while True:
                interval = random.randint(min_sec, max_sec)
                time.sleep(interval)
                self.run_once()
        except KeyboardInterrupt:
            print('終了します。')

    def batch(self, count=5, interval=2):
        for _ in range(count):
            self.run_once()
            time.sleep(interval)


def parse_args():
    parser = argparse.ArgumentParser(description='謎のOS公式ペット命名通知を発動します。')
    subparsers = parser.add_subparsers(dest='command')

    parser_once = subparsers.add_parser('once', help='1回だけ通知')
    parser_once.add_argument('--dry-run', action='store_true', help='OS通知を使わず標準出力のみ')

    parser_loop = subparsers.add_parser('loop', help='ランダムな間隔で永続通知')
    parser_loop.add_argument('--min', type=int, default=60, help='最小間隔(秒)')
    parser_loop.add_argument('--max', type=int, default=600, help='最大間隔(秒)')
    parser_loop.add_argument('--dry-run', action='store_true', help='OS通知を使わず標準出力のみ')

    parser_batch = subparsers.add_parser('batch', help='複数回連続通知')
    parser_batch.add_argument('--count', type=int, default=5, help='通知回数')
    parser_batch.add_argument('--interval', type=int, default=2, help='通知間隔(秒)')
    parser_batch.add_argument('--dry-run', action='store_true', help='OS通知を使わず標準出力のみ')

    parser.add_argument('--version', action='store_true', help='バージョン表示')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.version:
        print(f'os-fake-random-pet-name-notifier v{VERSION}')
        sys.exit(0)
    if args.command == 'once':
        notifier = Notifier(dry_run=args.dry_run)
        notifier.run_once()
    elif args.command == 'loop':
        notifier = Notifier(dry_run=args.dry_run)
        notifier.run_random_loop(min_sec=args.min, max_sec=args.max)
    elif args.command == 'batch':
        notifier = Notifier(dry_run=args.dry_run)
        notifier.batch(count=args.count, interval=args.interval)
    else:
        print('使い方:')
        print('  python pet_name_notifier.py once [--dry-run]')
        print('  python pet_name_notifier.py loop [--min 60 --max 600 --dry-run]')
        print('  python pet_name_notifier.py batch [--count 5 --interval 2 --dry-run]')
        print('  --version でバージョン表示')

if __name__ == '__main__':
    main()
