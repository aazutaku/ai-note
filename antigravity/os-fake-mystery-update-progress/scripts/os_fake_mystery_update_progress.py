import sys
import time
import random
import argparse

MYSTERY_MESSAGES = [
    '未知の言語パーサ更新中',
    '秘密のAPIを最適化中',
    '伝説のバグを発掘中',
    '仕様書を暗号化中',
    'メモリの謎領域を再構成中',
    '仮想カーネルを再起動中',
    '未公開プロトコルを同期中',
    '隠しコマンドを検証中',
    '時空間キャッシュを初期化中',
    '幻のデバイスドライバを探索中',
    '無限ループを最適化中',
    '暗号化されたログを解析中',
    '未知の依存関係を解決中',
    'ブラックボックスを再構築中',
    'レガシーコードを再発掘中',
    'シークレットモードを起動中',
    '隠し設定を適用中',
    '謎のプロセスを終了中',
    'ファントムアップデートを適用中',
    '不可視パッチをインストール中',
]

PROGRESS_BAR_LENGTH = 20

class ProgressBar:
    def __init__(self, message):
        self.message = message
        self.progress = 0
        self.direction = 1  # 1: forward, -1: backward
        self.stopped = False
        self.max_progress = random.randint(85, 100)
        self.stall_points = self._generate_stall_points()
        self.reverse_points = self._generate_reverse_points()
        self.last_update = time.time()

    def _generate_stall_points(self):
        # 2-4 stall points
        return sorted(random.sample(range(10, self.max_progress-5), random.randint(2, 4)))

    def _generate_reverse_points(self):
        # 1-2 reverse points
        return sorted(random.sample(range(20, self.max_progress-10), random.randint(1, 2)))

    def update(self):
        if self.progress >= self.max_progress:
            return False
        if self.stopped:
            return True
        if self.progress in self.stall_points:
            self.stopped = True
            self.stall_time = random.uniform(1.0, 3.0)
            self.stall_start = time.time()
            return True
        if self.progress in self.reverse_points:
            self.direction = -1
            self.reverse_steps = random.randint(3, 7)
            self.reverse_count = 0
            return True
        if hasattr(self, 'stall_time') and time.time() - self.stall_start < self.stall_time:
            return True
        elif hasattr(self, 'stall_time'):
            self.stopped = False
            del self.stall_time
            del self.stall_start
        if self.direction == 1:
            self.progress += random.randint(1, 3)
            if self.progress > self.max_progress:
                self.progress = self.max_progress
        else:
            self.progress -= 1
            self.reverse_count += 1
            if self.reverse_count >= self.reverse_steps:
                self.direction = 1
        return True

    def render(self):
        filled_len = int(self.progress / 100 * PROGRESS_BAR_LENGTH)
        bar = '■' * filled_len + '-' * (PROGRESS_BAR_LENGTH - filled_len)
        percent = min(self.progress, 100)
        sys.stdout.write(f"\r[{bar}] {percent:3d}% {self.message}...   ")
        sys.stdout.flush()

    def is_finished(self):
        return self.progress >= self.max_progress


def run_progress_bar():
    message = random.choice(MYSTERY_MESSAGES)
    bar = ProgressBar(message)
    while not bar.is_finished():
        bar.render()
        bar.update()
        time.sleep(random.uniform(0.08, 0.25))
    bar.progress = 100
    bar.render()
    print("")


def log(args):
    print("[os-fake-mystery-update-progress] ログ機能はありません。進捗演出のみです。")

def list_cmd(args):
    print("[os-fake-mystery-update-progress] 実行可能な進捗メッセージ一覧:")
    for i, msg in enumerate(MYSTERY_MESSAGES):
        print(f"  {i+1}. {msg}")

def summary(args):
    print("[os-fake-mystery-update-progress] このSkillは実害のない進捗バー演出のみを提供します。詳細はSKILL.md参照。")


def main():
    parser = argparse.ArgumentParser(description='謎のOSアップデート進捗バー演出')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='進捗バーを表示')
    parser_log = subparsers.add_parser('log', help='(ダミー) ログ出力')
    parser_list = subparsers.add_parser('list', help='進捗メッセージ一覧')
    parser_summary = subparsers.add_parser('summary', help='Skill概要')

    args = parser.parse_args()
    if args.command == 'run' or args.command is None:
        run_progress_bar()
    elif args.command == 'log':
        log(args)
    elif args.command == 'list':
        list_cmd(args)
    elif args.command == 'summary':
        summary(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
