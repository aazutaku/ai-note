import sys
import time
import random
import argparse
from typing import List

MYSTERIOUS_TASKS = [
    '未知の言語パッチ適用中',
    'レガシーキーボード最適化中',
    '謎のカーネル再構築中',
    '不明なプロトコル同期化中',
    '仮想RAMの無限拡張中',
    '幽霊プロセスの駆除中',
    '量子バグの隔離中',
    'ファントムデバイス検出中',
    '暗黒モードの初期化中',
    '時空間キャッシュの消去中',
    '逆流するアップデート',
    '未定義エラーの生成中',
    '謎のドライバ署名中',
    '幽体離脱モード適用中',
    'ブラックボックス最適化中',
    '不明な依存関係解決中',
    '未知のアップデート適用中',
    '仮想ファイルシステム拡張中',
    '無限ループ検出中',
    '不可視プロセスの最適化中',
]

PROGRESS_BAR_LEN = 11

class ProgressBar:
    def __init__(self):
        self.progress = 0
        self.task = ''
        self.history = []
        self.max_progress = 99 if random.random() < 0.5 else 100
        self.reverse_chance = 0.25
        self.stuck_at_99 = random.random() < 0.5
        self.last_task = None
        self._printed_99 = False

    def random_task(self):
        task = random.choice(MYSTERIOUS_TASKS)
        while task == self.last_task:
            task = random.choice(MYSTERIOUS_TASKS)
        self.last_task = task
        return task

    def print_bar(self, progress, task):
        bars = int(progress / 100 * PROGRESS_BAR_LEN)
        bar_str = '|' + '■' * bars + ' ' * (PROGRESS_BAR_LEN - bars) + '|'
        print(f'進捗: {progress}% {bar_str} {task}...')
        sys.stdout.flush()

    def run(self, min_delay=0.3, max_delay=1.0, duration=20):
        start_time = time.time()
        progress = 0
        stuck_counter = 0
        while True:
            if self.stuck_at_99 and progress >= 99:
                if not self._printed_99:
                    task = self.random_task()
                    self.print_bar(99, task)
                    self._printed_99 = True
                time.sleep(random.uniform(0.7, 1.2))
                stuck_counter += 1
                if stuck_counter > 8:
                    # Occasionally regress from 99%
                    if random.random() < 0.3:
                        progress = random.randint(95, 98)
                        task = self.random_task()
                        self.print_bar(progress, task)
                        stuck_counter = 0
                continue
            if progress >= self.max_progress:
                break
            # Randomly regress
            if random.random() < self.reverse_chance and progress > 10:
                regress = random.randint(3, 10)
                progress = max(0, progress - regress)
                task = self.random_task()
                self.print_bar(progress, task)
                time.sleep(random.uniform(min_delay, max_delay))
                continue
            # Normal progress
            increment = random.randint(3, 12)
            progress = min(progress + increment, self.max_progress)
            task = self.random_task()
            self.print_bar(progress, task)
            self.history.append((progress, task))
            time.sleep(random.uniform(min_delay, max_delay))
            if time.time() - start_time > duration:
                break
        # Final output (if not stuck at 99)
        if not self.stuck_at_99:
            self.print_bar(100, 'アップデート完了（嘘）')

    def summary(self):
        print('=== アップデート進捗履歴 ===')
        for p, t in self.history:
            print(f'{p}%: {t}')

    def list_tasks(self):
        print('=== 謎のアップデート内容一覧 ===')
        for t in MYSTERIOUS_TASKS:
            print(f'- {t}')

def main():
    parser = argparse.ArgumentParser(description='謎のOSアップデート進捗バー演出')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='謎のアップデート進捗バーを表示')
    parser_run.add_argument('--duration', type=int, default=20, help='最大表示秒数（デフォルト20秒）')
    parser_run.add_argument('--min-delay', type=float, default=0.3, help='進捗更新の最小間隔')
    parser_run.add_argument('--max-delay', type=float, default=1.0, help='進捗更新の最大間隔')

    parser_summary = subparsers.add_parser('summary', help='直近の進捗履歴を表示')
    parser_list = subparsers.add_parser('list', help='謎のアップデート内容一覧を表示')

    args = parser.parse_args()

    bar = ProgressBar()

    if args.command == 'run' or args.command is None:
        try:
            bar.run(min_delay=args.min_delay, max_delay=args.max_delay, duration=args.duration)
        except KeyboardInterrupt:
            print('\n[中断されました]')
    elif args.command == 'summary':
        bar.summary()
    elif args.command == 'list':
        bar.list_tasks()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
