import sys
import time
import random
import argparse
from typing import List

PROGRESS_MESSAGES = [
    "再起動準備中…",
    "謎のプロセス終了中…",
    "システムキャッシュを解放しています…",
    "セキュリティチェック中…",
    "仮想メモリを初期化中…",
    "未知のサービスを停止中…",
    "レジストリを最適化しています…",
    "ファイルシステムをスキャン中…",
    "設定をバックアップ中…",
    "リセットカウントダウン開始…",
    "ユーザーセッションを保存中…",
    "カーネルモジュールをアンロード中…",
    "ログを圧縮しています…",
    "不要なプロセスを解体中…",
    "仮想デバイスを認識中…",
    "アップデートの確認中…",
    "最終チェックポイントに到達…",
    "ほぼ完了、あと3分で全てがリセットされます"
]

END_MESSAGE = "完了！何も起きませんでした。"

class FakeRebootProgressBar:
    def __init__(self, steps: int = 7, min_delay: float = 0.5, max_delay: float = 2.0, seed: int = None):
        self.steps = steps
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self.messages = self._generate_messages()

    def _generate_messages(self) -> List[str]:
        # Pick random unique messages for each step
        if self.steps > len(PROGRESS_MESSAGES):
            messages = random.choices(PROGRESS_MESSAGES, k=self.steps)
        else:
            messages = random.sample(PROGRESS_MESSAGES, k=self.steps)
        return messages

    def show(self):
        percent_step = 100 // (self.steps + 1)
        for idx, msg in enumerate(self.messages):
            percent = percent_step * (idx + 1)
            sys.stdout.write(f"[{'{:>3}'.format(percent)}%] {msg}\n")
            sys.stdout.flush()
            delay = random.uniform(self.min_delay, self.max_delay)
            time.sleep(delay)
        # Final step
        sys.stdout.write(f"[100%] {END_MESSAGE}\n")
        sys.stdout.flush()

    def list_messages(self):
        for idx, msg in enumerate(PROGRESS_MESSAGES):
            print(f"{idx+1}. {msg}")

    def summary(self):
        print("Fake OS Reboot Progress Bar Skill")
        print(f"Available progress messages: {len(PROGRESS_MESSAGES)}")
        print(f"Default steps: {self.steps}")
        print(f"Delay per step: {self.min_delay}-{self.max_delay} sec")
        print(f"Random seed: {self.seed}")


def parse_args():
    parser = argparse.ArgumentParser(description="謎のOS再起動進捗バーを表示するスクリプト")
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='進捗バーを表示')
    parser_run.add_argument('--steps', type=int, default=7, help='進捗ステップ数')
    parser_run.add_argument('--min-delay', type=float, default=0.5, help='最小遅延秒数')
    parser_run.add_argument('--max-delay', type=float, default=2.0, help='最大遅延秒数')
    parser_run.add_argument('--seed', type=int, default=None, help='ランダムシード')

    parser_list = subparsers.add_parser('list', help='利用可能な進捗メッセージ一覧')
    parser_summary = subparsers.add_parser('summary', help='スキル概要表示')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'run':
        bar = FakeRebootProgressBar(
            steps=args.steps,
            min_delay=args.min_delay,
            max_delay=args.max_delay,
            seed=args.seed
        )
        bar.show()
    elif args.command == 'list':
        bar = FakeRebootProgressBar()
        bar.list_messages()
    elif args.command == 'summary':
        bar = FakeRebootProgressBar()
        bar.summary()
    else:
        print("コマンドを指定してください (run, list, summary)")
        sys.exit(1)

if __name__ == '__main__':
    main()
