import argparse
import random
import sys
import time
from datetime import datetime

# メッセージテンプレート
ALERT_TEMPLATES = [
    "[ALERT] OS公式通知: 未知のプロセスID {pid} がバックグラウンドで“{activity}”を開始しました。",
    "[INFO] 進捗: {progress_bar} {progress}% 完了 / 解析残り時間: {remaining}分",
    "[WARNING] 謎のプロセス {pid} の挙動を監視しています。詳細は非公開です。",
    "[NOTICE] 不明なバックグラウンドタスク '{task}' が一時停止されました。",
    "[ALERT] システムは“{activity}”を検出しました。影響範囲: 不明",
    "[INFO] プロセスID {pid} の“{activity}”が異常終了しました。原因: 不明",
    "[NOTICE] OSは現在“{activity}”を解析中です。進捗: {progress}%",
    "[WARNING] 非公開プロセス {pid} のアクセス要求を拒否しました。",
    "[ALERT] 未知のバックグラウンド通信が検出されました。詳細: {activity}"
]

ACTIVITIES = [
    "分散型集計", "意味不明な集計", "暗号化解析", "疑似ログ生成", "ファントム監視", "プロセス疑似化", "ゴーストアクセス", "シャドウ同期", "phantom_collector", "謎のリソース消費"
]

TASKS = [
    "phantom_collector", "ghost_watcher", "shadow_sync", "unknown_daemon", "mystery_logger", "stealth_aggregator"
]

# 進捗バー生成
def progress_bar(progress):
    blocks = int(progress / 10)
    return "█" * blocks + "░" * (10 - blocks)

# ランダムな通知メッセージを生成
def generate_message():
    pid = random.randint(1000, 9999)
    activity = random.choice(ACTIVITIES)
    task = random.choice(TASKS)
    progress = random.randint(10, 99)
    remaining = random.randint(1, 60)
    bar = progress_bar(progress)
    template = random.choice(ALERT_TEMPLATES)
    msg = template.format(pid=pid, activity=activity, task=task, progress=progress, remaining=remaining, progress_bar=bar)
    return msg

# 通知を複数回ランダムな間隔で発火
def random_alerts(count=5, min_interval=5, max_interval=20, dry_run=False):
    for i in range(count):
        msg = generate_message()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} {msg}")
        if dry_run and i == count - 1:
            break
        sleep_time = random.uniform(min_interval, max_interval)
        time.sleep(sleep_time)

# CLIサブコマンド

def main():
    parser = argparse.ArgumentParser(description="謎のOS風バックグラウンドプロセス通知をランダムに生成・表示します。")
    subparsers = parser.add_subparsers(dest="command", required=True)

    alert_parser = subparsers.add_parser("alert", help="ランダムな謎通知を即時1回だけ表示")
    alert_parser.add_argument("-n", "--number", type=int, default=1, help="通知回数 (デフォルト: 1)")
    alert_parser.add_argument("--dry-run", action="store_true", help="sleepせず即時出力 (テスト用)")

    batch_parser = subparsers.add_parser("batch", help="ランダムな間隔で複数回通知を発火")
    batch_parser.add_argument("-n", "--number", type=int, default=5, help="通知回数 (デフォルト: 5)")
    batch_parser.add_argument("--min-interval", type=int, default=5, help="最小間隔(秒)")
    batch_parser.add_argument("--max-interval", type=int, default=20, help="最大間隔(秒)")
    batch_parser.add_argument("--dry-run", action="store_true", help="sleepせず即時出力 (テスト用)")

    list_parser = subparsers.add_parser("list", help="ランダムな通知例を10件生成して一覧表示")

    args = parser.parse_args()
    if args.command == "alert":
        for _ in range(args.number):
            print(generate_message())
    elif args.command == "batch":
        random_alerts(count=args.number, min_interval=args.min_interval, max_interval=args.max_interval, dry_run=args.dry_run)
    elif args.command == "list":
        for _ in range(10):
            print(generate_message())
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
