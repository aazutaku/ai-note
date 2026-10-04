import sys
import time
import random
import argparse
from typing import List

MYSTERIOUS_TASKS = [
    '未知の言語パッチ適用中',
    'レガシーキーボード最適化中',
    '逆位相メモリ同期中',
    '仮想ペンギンモード有効化中',
    'モジュール逆流抑制中',
    '量子バッファ拡張中',
    '非公開APIアクセス許可待機中',
    'セキュアな謎プロトコルで通信中',
    '暗号化された謎データを展開中',
    '未定義エリアの初期化中',
    'メタデータの再帰的変換中',
    'ランダムシードを再生成中',
    '仮想デバイスの再割当中',
    '時空間キャッシュをフラッシュ中',
    '不可視ファイルを検出中',
    '未知の依存関係を解決中',
    '謎の互換性チェック中',
    'レガシーサポートを一時停止中',
    'オプションフラグをランダム適用中',
    '仮想メモリを逆流中',
    '無限ループを検出中',
    '未定義動作を実行中',
    '謎のプロセスを監視中',
    'ファントムアップデート適用中',
    'ゴーストログを生成中',
    '不可視パーティションを最適化中',
    'メタバグを注入中',
    'サイレントリカバリを試行中',
    '仮想パッチを仮適用中',
    '進捗待機中'
]

PROGRESS_BAR_LENGTH = 15

class ProgressBar:
    def __init__(self, length=PROGRESS_BAR_LENGTH):
        self.length = length

    def render(self, percent: int) -> str:
        filled = int(self.length * percent // 100)
        bar = '[' + '=' * filled + ' ' * (self.length - filled) + ']'
        return f'{bar} {percent:3d}%'


def random_progress_sequence(max_steps=20) -> List[dict]:
    seq = []
    percent = 0
    direction = 1  # 1: forward, -1: backward
    stuck_at_99 = False
    for i in range(max_steps):
        # Occasionally jump backward
        if percent >= 99 and random.random() < 0.4:
            stuck_at_99 = True
        if stuck_at_99:
            percent = 99
        else:
            if random.random() < 0.2 and percent > 30:
                # Reverse progress
                percent = max(0, percent - random.randint(5, 25))
            else:
                # Normal progress
                percent = min(100, percent + random.randint(3, 20))
            if percent > 99:
                percent = 99
        task = random.choice(MYSTERIOUS_TASKS)
        seq.append({'percent': percent, 'task': task})
        # Randomly decide to stay at 99% for a while
        if percent == 99 and random.random() < 0.6:
            stuck_at_99 = True
        if percent == 99 and random.random() < 0.2:
            break  # Sometimes finish early
    return seq


def print_progress_sequence(seq: List[dict], delay=0.7, stream=sys.stdout):
    for item in seq:
        bar = ProgressBar().render(item['percent'])
        msg = f'{bar}  {item["task"]}...'
        print(msg, file=stream, flush=True)
        time.sleep(delay * (0.7 + random.random()*0.6))


def run_cli(args):
    if args.list_tasks:
        for t in MYSTERIOUS_TASKS:
            print(f'- {t}')
        return
    if args.seed is not None:
        random.seed(args.seed)
    seq = random_progress_sequence(max_steps=args.steps)
    print_progress_sequence(seq, delay=args.delay)


def parse_args():
    parser = argparse.ArgumentParser(description='謎のOSアップデート進行中(フェイク)進捗バーを表示します')
    parser.add_argument('--steps', type=int, default=20, help='進捗ステップ数 (デフォルト: 20)')
    parser.add_argument('--delay', type=float, default=0.7, help='進捗表示間隔(秒) (デフォルト: 0.7)')
    parser.add_argument('--list-tasks', action='store_true', help='利用可能な謎タスク一覧を表示')
    parser.add_argument('--seed', type=int, default=None, help='ランダムシード')
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        run_cli(args)
    except KeyboardInterrupt:
        print('\n[終了] フェイクアップデートを中断しました。')
    except Exception as e:
        print(f'エラー: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
