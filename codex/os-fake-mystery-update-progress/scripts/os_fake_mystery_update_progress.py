import sys
import time
import random
import argparse
from typing import List

MYSTERY_MESSAGES = [
    '未知の言語パーサ更新中...',
    '秘密のAPIを最適化中...',
    '伝説のバグを発掘中...',
    '謎のドライバを再構築中...',
    '世界線の同期を試行中...',
    '暗黒モードの互換性検証中...',
    '隠し設定を再生成中...',
    '時空間キャッシュを初期化中...',
    '幻のプロセスを監視中...',
    '未知の依存関係を解決中...'
]

BAR_LENGTH = 20
REVERSE_PROB = 0.18
STOP_PROB = 0.14

class ProgressBar:
    def __init__(self, length=BAR_LENGTH):
        self.length = length
        self.percent = 0
        self.direction = 1  # 1: forward, -1: backward
        self.message = random.choice(MYSTERY_MESSAGES)
        self.stopped = False
        self.stop_counter = 0
        self.reverse_counter = 0

    def randomize_behavior(self):
        if not self.stopped and random.random() < STOP_PROB:
            self.stopped = True
            self.stop_counter = random.randint(2, 6)
        if self.direction == 1 and random.random() < REVERSE_PROB:
            self.direction = -1
            self.reverse_counter = random.randint(2, 5)
        elif self.direction == -1 and self.reverse_counter == 0:
            self.direction = 1

    def update(self):
        if self.stopped:
            self.stop_counter -= 1
            if self.stop_counter <= 0:
                self.stopped = False
            return False
        if self.direction == -1:
            self.reverse_counter -= 1
            if self.reverse_counter <= 0:
                self.direction = 1
        step = random.randint(1, 6) * self.direction
        self.percent += step
        self.percent = max(0, min(100, self.percent))
        if random.random() < 0.22:
            self.message = random.choice(MYSTERY_MESSAGES)
        return True

    def render(self):
        filled = int(self.length * self.percent / 100)
        bar = '[' + '=' * filled + '>' + ' ' * (self.length - filled - 1) + ']'
        extra = ''
        if self.stopped:
            extra = ' (一時停止)'
        elif self.direction == -1:
            extra = ' (逆流!)'
        return f'{bar} {self.percent:3d}%  {self.message}{extra}'


def run_progress(duration=None):
    pb = ProgressBar()
    start = time.time()
    while pb.percent < 100:
        pb.randomize_behavior()
        updated = pb.update()
        sys.stdout.write('\r' + pb.render())
        sys.stdout.flush()
        if pb.percent >= 100:
            break
        sleep_time = random.uniform(0.15, 0.6)
        if pb.stopped:
            sleep_time += 0.3
        time.sleep(sleep_time)
        if duration and (time.time() - start) > duration:
            break
    sys.stdout.write('\r' + '[' + '=' * (BAR_LENGTH-1) + '>] 100%  完了 (何も変わりませんでした)\n')
    sys.stdout.flush()


def list_messages():
    print('--- 謎の進捗内容一覧 ---')
    for msg in MYSTERY_MESSAGES:
        print('-', msg)


def summary():
    print('このスキルは、実際には何もアップデートしません。進捗バーと謎の文言で現実感を侵食します。')
    print('進捗バーは時に停止や逆流を伴い、毎回異なる演出となります。')
    print('明示的な呼び出しや、特定のキーワードで自動発動します。')


def main():
    parser = argparse.ArgumentParser(description='謎のOSアップデート進捗バー (完全に無意味)')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='謎の進捗バーを表示')
    parser_run.add_argument('--duration', type=int, default=None, help='進捗バーの最大表示秒数 (省略時は100%まで)')

    parser_list = subparsers.add_parser('list', help='進捗内容の候補一覧を表示')
    parser_summary = subparsers.add_parser('summary', help='スキルの概要説明')

    args = parser.parse_args()
    if args.command == 'run' or args.command is None:
        run_progress(duration=args.duration if hasattr(args, 'duration') else None)
    elif args.command == 'list':
        list_messages()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
