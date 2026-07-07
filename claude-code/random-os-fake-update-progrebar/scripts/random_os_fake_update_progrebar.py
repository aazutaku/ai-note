import sys
import time
import random
import argparse
import threading

# ランダムな進捗メッセージ候補
PROGRESS_MESSAGES = [
    'バグ収穫中',
    'やる気パッチ適用中',
    '怠惰アップグレード中',
    '仕様の穴を拡張中',
    'レガシーコードを温存中',
    '依存関係を複雑化中',
    '無駄な最適化を実施中',
    'テストを省略中',
    '謎のパッチを適用中',
    'やる気スイッチを探索中',
    '未定義動作を拡張中',
    '仕様書を紛失中',
    'バグを擬態化中',
    '技術的負債を積立中',
    'コメントを削除中',
    '未来の自分に丸投げ中',
    'エラーを黙殺中',
    'メモリリークを再現中',
    'コピペで量産中',
    '意味不明な警告を生成中'
]

BAR_LENGTH = 20
DISPLAY_DURATION = 10  # 秒


def random_progress_message():
    return random.choice(PROGRESS_MESSAGES)


def build_progress_bar(percent):
    filled = int(BAR_LENGTH * percent // 100)
    empty = BAR_LENGTH - filled
    bar = '[' + '=' * filled + '>' + ' ' * (empty - 1) + ']'
    return bar


def print_progress_bar(percent, message, clear=False):
    bar = build_progress_bar(percent)
    sys.stdout.write(f'\r{bar} {percent:3d}% {message}...')
    sys.stdout.flush()
    if clear:
        sys.stdout.write('\n')


def animate_progress_bar():
    message = random_progress_message()
    percent = 0
    steps = random.randint(6, 12)
    increments = sorted(random.sample(range(5, 100), steps - 1)) + [100]
    last = 0
    start_time = time.time()
    for p in increments:
        for i in range(last, p, max(1, (p - last)//5)):
            print_progress_bar(i, message)
            time.sleep(random.uniform(0.05, 0.15))
        print_progress_bar(p, message)
        last = p
        time.sleep(random.uniform(0.2, 0.7))
        if time.time() - start_time > DISPLAY_DURATION:
            break
    print_progress_bar(100, message, clear=True)
    # バーを消す
    time.sleep(random.uniform(1.5, 3.0))
    sys.stdout.write('\r' + ' ' * (BAR_LENGTH + 30) + '\r')
    sys.stdout.flush()


def run_bar(args):
    animate_progress_bar()


def main():
    parser = argparse.ArgumentParser(
        description='謎のOSアップデート進捗バーをランダム表示する無駄スキル')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='進捗バーを即座に表示')
    parser_run.set_defaults(func=run_bar)

    parser_demo = subparsers.add_parser('demo', help='3回連続でデモ表示')
    parser_demo.set_defaults(func=lambda args: [animate_progress_bar() for _ in range(3)])

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
