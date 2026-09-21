import sys
import time
import random
import argparse

MYSTERY_MESSAGES = [
    '未知の言語パーサ更新中',
    '秘密のAPIを最適化中',
    '伝説のバグを発掘中',
    'システムの謎領域を再構築中',
    '不明なモジュールを初期化中',
    '暗号化された設定ファイルを解析中',
    '古代コードの解読を試行中',
    '未公開プロトコルを同期中',
    '仮想メモリの幽霊を追跡中',
    '未知のデバイスドライバを検証中',
    '隠し機能を有効化中',
    'ブラックボックスAPIを逆アセンブル中',
    '未知のバージョンを検出中',
    '幻のパッチを適用中',
    '謎のエラーを再現中',
    '不明な依存関係を解決中',
    'シークレットモードを起動中',
    '未定義動作を観測中',
    '隠されたログを抽出中',
    '謎のプロセスを監視中'
]

BAR_LENGTH = 20

class ProgressBar:
    def __init__(self, length=BAR_LENGTH):
        self.length = length
        self.progress = 0
        self.direction = 1  # 1: forward, -1: backward
        self.message = random.choice(MYSTERY_MESSAGES)
        self.last_update = time.time()
        self.stopped = False

    def update(self):
        if self.stopped:
            return
        # 進捗の進み/逆流/停止のギミック
        event = random.choices(
            ['forward', 'backward', 'stop'],
            [0.7, 0.2, 0.1]
        )[0]
        if event == 'forward':
            self.direction = 1
            delta = random.randint(1, 5)
        elif event == 'backward':
            self.direction = -1
            delta = random.randint(1, 7)
        else:  # stop
            self.stopped = True
            return
        self.progress += self.direction * delta
        if self.progress < 0:
            self.progress = 0
        if self.progress > 100:
            self.progress = 100
        # たまにメッセージを変更
        if random.random() < 0.2:
            self.message = random.choice(MYSTERY_MESSAGES)

    def render(self):
        filled = int(self.progress / 100 * self.length)
        bar = '[' + '=' * filled + ' ' * (self.length - filled) + ']'
        return f'{bar} {self.progress:3d}%  {self.message}...'

    def is_complete(self):
        return self.progress >= 100

    def maybe_resume(self):
        # 停止状態からランダムで再開
        if self.stopped and random.random() < 0.4:
            self.stopped = False


def run_progress_bar(duration=20, min_interval=0.3, max_interval=1.2):
    pb = ProgressBar()
    start_time = time.time()
    sys.stdout.write('\n')
    while not pb.is_complete() and (time.time() - start_time) < duration:
        pb.maybe_resume()
        if not pb.stopped:
            pb.update()
        sys.stdout.write(f'\r{pb.render()}')
        sys.stdout.flush()
        sleep_time = random.uniform(min_interval, max_interval)
        time.sleep(sleep_time)
    # 完了演出
    pb.progress = 100
    sys.stdout.write(f'\r{pb.render()}\n')
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write('謎のアップデートが完了しました。\n')


def list_messages():
    print('--- 謎の進捗メッセージ一覧 ---')
    for msg in MYSTERY_MESSAGES:
        print(f'- {msg}')


def summary():
    print('このSkillは、理不尽な謎のアップデート進捗バーを演出します。')
    print(f'メッセージパターン数: {len(MYSTERY_MESSAGES)}')
    print(f'進捗バー長さ: {BAR_LENGTH}')
    print('進捗は途中で止まったり逆流したりします。')


def main():
    parser = argparse.ArgumentParser(description='謎のOSアップデート進捗バー')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='進捗バーを表示')
    parser_run.add_argument('--duration', type=int, default=20, help='進捗バーの最大表示秒数 (デフォルト20)')

    parser_list = subparsers.add_parser('list', help='進捗メッセージ一覧を表示')
    parser_summary = subparsers.add_parser('summary', help='Skill概要を表示')

    args = parser.parse_args()
    if args.command == 'run' or args.command is None:
        try:
            run_progress_bar(duration=getattr(args, 'duration', 20))
        except KeyboardInterrupt:
            sys.stdout.write('\n進捗バーを中断しました。\n')
    elif args.command == 'list':
        list_messages()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
