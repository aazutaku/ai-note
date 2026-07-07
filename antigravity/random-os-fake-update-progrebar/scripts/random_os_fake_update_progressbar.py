import sys
import time
import random
import argparse
from typing import List

FAKE_TASKS = [
    'バグ収穫中',
    'やる気パッチ適用中',
    '怠惰アップグレード中',
    '仕様書の再解釈中',
    '謎のプロセス最適化中',
    '未定義動作の検証中',
    'メモリの気分転換中',
    '依存関係の迷子探索中',
    '無駄な再起動準備中',
    '冗長コメントの削除中',
    '仮想バグフィックス中',
    'やる気のインストール中',
    '自己矛盾の解消中',
    '仕様の再発明中',
    '気合いの注入中',
    'エンジニア魂の充填中',
    '無意味な最適化中',
    '未定義動作の実装中',
    '無限ループの脱出中',
    '謎のプロセス終了中'
]

PROGRESSBAR_LENGTH = 20


def random_task() -> str:
    return random.choice(FAKE_TASKS)


def random_progress_sequence() -> List[int]:
    """
    0-100%までランダムなステップで進捗を生成
    """
    seq = [0]
    while seq[-1] < 100:
        step = random.randint(3, 18)
        next_val = min(100, seq[-1] + step)
        if next_val == seq[-1]:
            break
        seq.append(next_val)
    return seq


def progressbar_str(percent: int) -> str:
    filled = int(PROGRESSBAR_LENGTH * percent / 100)
    bar = '█' * filled + ' ' * (PROGRESSBAR_LENGTH - filled)
    return f'[{bar}]'


def show_fake_update(task: str = None, duration: float = 2.5, fast: bool = False):
    if task is None:
        task = random_task()
    progress_seq = random_progress_sequence()
    if fast:
        duration = 0.8 + random.random() * 0.7
    step_time = duration / max(1, len(progress_seq) - 1)
    for idx, percent in enumerate(progress_seq):
        bar = progressbar_str(percent)
        sys.stdout.write(f'\r[OSアップデート進行中] {task}... [{percent:3}%] {bar}')
        sys.stdout.flush()
        if percent == 100:
            time.sleep(0.4)
            break
        time.sleep(step_time)
    sys.stdout.write('\n')
    sys.stdout.flush()


def list_tasks():
    print('利用可能なランダム進捗項目一覧:')
    for t in FAKE_TASKS:
        print(f'- {t}')


def main():
    parser = argparse.ArgumentParser(description='謎のOSアップデート進捗バーを表示')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='ランダムな進捗バーを表示')
    parser_run.add_argument('--task', type=str, help='進捗内容を指定(省略時ランダム)')
    parser_run.add_argument('--fast', action='store_true', help='高速モード')

    parser_list = subparsers.add_parser('list', help='利用可能な進捗項目を表示')

    args = parser.parse_args()
    if args.command == 'run':
        try:
            show_fake_update(task=args.task, fast=args.fast)
        except KeyboardInterrupt:
            sys.stdout.write('\n[中断されました]\n')
    elif args.command == 'list':
        list_tasks()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
