import random
import time
import argparse
import sys
import threading
from datetime import datetime

try:
    from plyer import notification
except ImportError:
    notification = None

# ハードウェア/周辺機器名
DEVICE_NAMES = [
    "マウス",
    "キーボード",
    "ディスプレイ",
    "USBメモリ",
    "スピーカー",
    "ヘッドホン",
    "プリンター",
    "タッチパッド",
    "Webカメラ",
    "外付けHDD",
    "ルーター",
    "マイク",
    "グラフィックボード",
    "ゲームパッド",
    "スマートフォン",
    "タブレット"
]

# 二つ名/称号パーツ
PREFIXES = [
    "疾風の",
    "静寂なる",
    "虚空の",
    "迷宮の",
    "響鳴の",
    "暗黒の",
    "閃光の",
    "不屈の",
    "孤高の",
    "叡智の",
    "烈火の",
    "氷結の",
    "雷鳴の",
    "幻影の",
    "不滅の",
    "蒼穹の"
]

SUFFIXES = [
    "コロンブス",
    "鉄槌",
    "監視者",
    "案内人",
    "咆哮",
    "魔導書",
    "守護者",
    "探求者",
    "旅人",
    "彗星",
    "錬金術師",
    "忍者",
    "賢者",
    "錆びた剣",
    "流星",
    "旋風"
]

# 通知メッセージパターン
MESSAGE_PATTERNS = [
    "あなたの{device}は本日より“{title}”と命名されました。",
    "{device}の新しい名は“{title}”です。",
    "{device}は“{title}”と呼ばれることになりました。",
    "あなたの{device}は“{title}”です。",
    "{device}の公式ペット名は“{title}”です。"
]

def generate_random_title():
    prefix = random.choice(PREFIXES)
    suffix = random.choice(SUFFIXES)
    return f"{prefix}{suffix}"

def generate_notification_message():
    device = random.choice(DEVICE_NAMES)
    title = generate_random_title()
    pattern = random.choice(MESSAGE_PATTERNS)
    return pattern.format(device=device, title=title)

def show_notification(message):
    # デスクトップ通知
    if notification:
        try:
            notification.notify(
                title="OS通知",
                message=message,
                app_name="Fake Pet Name Notifier",
                timeout=8
            )
        except Exception as e:
            print(f"[通知エラー] {e}", file=sys.stderr)
    # ターミナル出力
    print(f"[OS通知] {message}")

def notify_randomly(stop_event, min_interval=60, max_interval=300):
    while not stop_event.is_set():
        wait_time = random.randint(min_interval, max_interval)
        stop_event.wait(wait_time)
        if stop_event.is_set():
            break
        msg = generate_notification_message()
        show_notification(msg)

def log_notification(logfile, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\t{message}\n")

def list_log(logfile, limit=10):
    try:
        with open(logfile, "r", encoding="utf-8") as f:
            lines = f.readlines()[-limit:]
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("ログファイルが見つかりません。", file=sys.stderr)

def summary_log(logfile):
    from collections import Counter
    try:
        with open(logfile, "r", encoding="utf-8") as f:
            titles = [line.strip().split("\t")[-1] for line in f]
            c = Counter(titles)
            print("--- ペット名通知ランキング ---")
            for title, count in c.most_common(5):
                print(f"{title}: {count}回")
    except FileNotFoundError:
        print("ログファイルが見つかりません。", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Fake Random Pet Name Notifier")
    subparsers = parser.add_subparsers(dest="command")

    parser_notify = subparsers.add_parser("notify", help="今すぐ通知を表示")
    parser_notify.add_argument("--log", help="通知内容をログファイルに保存")

    parser_daemon = subparsers.add_parser("daemon", help="ランダムな間隔で自動通知")
    parser_daemon.add_argument("--min", type=int, default=60, help="最小間隔(秒)")
    parser_daemon.add_argument("--max", type=int, default=300, help="最大間隔(秒)")
    parser_daemon.add_argument("--log", help="通知内容をログファイルに保存")

    parser_log = subparsers.add_parser("log", help="ログを表示")
    parser_log.add_argument("--file", required=True, help="ログファイルパス")
    parser_log.add_argument("--limit", type=int, default=10, help="表示件数")

    parser_summary = subparsers.add_parser("summary", help="通知タイトルの集計")
    parser_summary.add_argument("--file", required=True, help="ログファイルパス")

    parser.add_argument("--notify-now", action="store_true", help="今すぐ通知を1回表示(サブコマンド不要)")

    args = parser.parse_args()

    if args.notify_now:
        msg = generate_notification_message()
        show_notification(msg)
        sys.exit(0)

    if args.command == "notify":
        msg = generate_notification_message()
        show_notification(msg)
        if args.log:
            log_notification(args.log, msg)
    elif args.command == "daemon":
        stop_event = threading.Event()
        def run_daemon():
            while not stop_event.is_set():
                msg = generate_notification_message()
                show_notification(msg)
                if args.log:
                    log_notification(args.log, msg)
                wait_time = random.randint(args.min, args.max)
                stop_event.wait(wait_time)
        try:
            print("[INFO] ランダムペット名通知デーモン開始 (Ctrl+Cで終了)")
            run_daemon()
        except KeyboardInterrupt:
            stop_event.set()
            print("[INFO] デーモンを終了しました。")
    elif args.command == "log":
        list_log(args.file, args.limit)
    elif args.command == "summary":
        summary_log(args.file)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
