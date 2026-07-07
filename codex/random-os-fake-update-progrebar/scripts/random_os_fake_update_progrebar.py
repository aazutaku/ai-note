import random
import time
import sys
import argparse

FAKE_UPDATE_MESSAGES = [
    "バグ収穫中",
    "やる気パッチ適用中",
    "怠惰アップグレード中",
    "意味不明な最適化中",
    "仕様書の再発明中",
    "無駄な依存関係更新中",
    "謎のレジストリ書き換え中",
    "気分転換アップデート中",
    "レガシーコード復元中",
    "メモリリーク拡張中"
]

PROGRESS_BAR_LENGTH = 20
DISPLAY_DURATION = 2.5  # seconds


def generate_fake_update_message():
    message = random.choice(FAKE_UPDATE_MESSAGES)
    return message


def generate_progress_bar(progress):
    filled_length = int(PROGRESS_BAR_LENGTH * progress // 100)
    bar = '█' * filled_length + '-' * (PROGRESS_BAR_LENGTH - filled_length)
    return f"[{bar}] {progress}%"


def print_progress_bar(message, progress):
    sys.stdout.write(f"\r[OSアップデート進捗] {message}: {generate_progress_bar(progress)} ")
    sys.stdout.flush()


def show_fake_update():
    message = generate_fake_update_message()
    progress = 0
    increments = random.randint(4, 8)
    steps = sorted(random.sample(range(15, 100), increments - 1)) + [100]
    prev = 0
    for step in steps:
        for p in range(prev, step, max(1, (step-prev)//5)):
            print_progress_bar(message, p)
            time.sleep(random.uniform(0.03, 0.08))
        prev = step
        print_progress_bar(message, step)
        time.sleep(random.uniform(0.1, 0.3))
    # Hold at 100% for a moment
    time.sleep(DISPLAY_DURATION)
    sys.stdout.write("\r" + " " * 80 + "\r")
    sys.stdout.flush()


def show_multiple_updates(n=1):
    for _ in range(n):
        show_fake_update()


def list_fake_messages():
    print("利用可能な進捗内容:")
    for msg in FAKE_UPDATE_MESSAGES:
        print(f"- {msg}")


def main():
    parser = argparse.ArgumentParser(
        description="謎のOSアップデート進捗バーをランダム表示する演出スクリプト"
    )
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="進捗バーを1回または複数回表示")
    parser_run.add_argument("-n", type=int, default=1, help="表示回数 (デフォルト: 1)")

    parser_list = subparsers.add_parser("list", help="利用可能な進捗内容を表示")

    args = parser.parse_args()
    if args.command == "run":
        show_multiple_updates(args.n)
    elif args.command == "list":
        list_fake_messages()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
