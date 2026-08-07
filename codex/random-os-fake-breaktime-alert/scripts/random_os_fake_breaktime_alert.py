import argparse
import random
import sys
import time
from datetime import datetime, timedelta

try:
    from plyer import notification
except ImportError:
    print("plyerライブラリが必要です。pip install plyer でインストールしてください。", file=sys.stderr)
    sys.exit(1)

NOTIFY_MESSAGES = [
    "OS推奨：5分間ぼーっとするべし",
    "肩回しタイム発動！今すぐ両腕を広げてみましょう",
    "緊急！脳内メモリ休息モード",
    "システム判断：画面から目を離してください",
    "休憩推奨：好きな飲み物を用意するタイミングです",
    "謎のプロセスが休憩を要求しています",
    "CPU温度上昇中：深呼吸を推奨します",
    "メモリリーク防止：1分間ストレッチしてください",
    "OSの気まぐれ：今すぐ立ち上がってみましょう",
    "仮想デスクトップがあなたの休憩を待っています"
]

LOG_FILE = None  # 通知履歴は保存しない設計


def send_random_notification():
    msg = random.choice(NOTIFY_MESSAGES)
    notification.notify(
        title="[通知]",
        message=msg,
        app_name="Fake Breaktime Alert",
        timeout=10
    )
    print(f"[通知] {msg}")


def run_periodic(interval_min=60, randomize=False, min_interval=30, max_interval=90, count=None):
    """
    interval_min: 通常の分単位インターバル
    randomize: Trueなら min_interval~max_interval 分でランダム
    count: 通知回数の上限 (Noneなら無限)
    """
    sent = 0
    try:
        while count is None or sent < count:
            send_random_notification()
            sent += 1
            if randomize:
                next_interval = random.randint(min_interval, max_interval)
            else:
                next_interval = interval_min
            print(f"次の通知まで {next_interval} 分待機...")
            for _ in range(next_interval * 60):
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nFake Breaktime Alert を終了します。")


def cli():
    parser = argparse.ArgumentParser(description="謎のOS偽・強制休憩通知スクリプト")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    parser_once = subparsers.add_parser("once", help="1回だけランダム通知を表示")

    parser_periodic = subparsers.add_parser("periodic", help="定期的またはランダム間隔で通知")
    parser_periodic.add_argument("--interval", type=int, default=60, help="通知間隔(分)")
    parser_periodic.add_argument("--randomize", action="store_true", help="間隔をランダム化する")
    parser_periodic.add_argument("--min", type=int, default=30, help="ランダム時の最小間隔(分)")
    parser_periodic.add_argument("--max", type=int, default=90, help="ランダム時の最大間隔(分)")
    parser_periodic.add_argument("--count", type=int, default=None, help="通知回数上限")

    parser_list = subparsers.add_parser("list", help="通知候補メッセージ一覧を表示")

    args = parser.parse_args()

    if args.command == "once":
        send_random_notification()
    elif args.command == "periodic":
        run_periodic(
            interval_min=args.interval,
            randomize=args.randomize,
            min_interval=args.min,
            max_interval=args.max,
            count=args.count
        )
    elif args.command == "list":
        print("--- 通知候補メッセージ一覧 ---")
        for i, msg in enumerate(NOTIFY_MESSAGES, 1):
            print(f"{i:2d}. {msg}")
    else:
        parser.print_help()


if __name__ == '__main__':
    cli()
