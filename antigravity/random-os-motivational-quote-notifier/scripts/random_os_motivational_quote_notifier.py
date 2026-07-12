import random
import time
import argparse
import sys
from plyer import notification
from datetime import datetime
import threading

QUOTES = [
    "本日もバグに感謝せよ",
    "進捗ゼロ、それもまた進化",
    "コードは寝かせて美味しくなる",
    "エラーは未来からのメッセージ",
    "OSは見ている、あなたの努力を",
    "バグは成長の証",
    "仕様書は都市伝説",
    "リファクタリングは心の洗濯",
    "デバッグは旅である",
    "進捗がない、それもまた一歩",
    "最適化は明日の自分に任せよ",
    "コードレビューは愛のムチ",
    "メモリリークは友情の証",
    "エラーは未来からのメッセージ",
    "今日のバグは明日の糧",
    "OSはあなたを裏切らない…たぶん",
    "コミットは小さく、夢は大きく",
    "動かないコードもまた美しい",
    "コンパイルエラーは人生のスパイス",
    "再起動、それはすべてを癒す"
]

NOTIFY_TITLE = "OS Motivational Quote"

LOG_FILE = "motivational_quote_log.txt"


def notify_quote(quote, dry_run=False):
    """Send OS notification with the given quote."""
    if dry_run:
        print(f"[OS Notification]\n{quote}")
        return
    try:
        notification.notify(
            title=NOTIFY_TITLE,
            message=quote,
            timeout=7  # seconds
        )
    except Exception as e:
        print(f"Failed to send notification: {e}", file=sys.stderr)

def random_quote():
    return random.choice(QUOTES)

def log_quote(quote):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {quote}\n")
    except Exception as e:
        print(f"Failed to log quote: {e}", file=sys.stderr)

def list_quotes():
    for idx, q in enumerate(QUOTES, 1):
        print(f"{idx}. {q}")

def show_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("No log file found.")
    except Exception as e:
        print(f"Failed to read log: {e}", file=sys.stderr)

def summary_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"Total notifications sent: {len(lines)}")
    except FileNotFoundError:
        print("No log file found.")
    except Exception as e:
        print(f"Failed to summarize log: {e}", file=sys.stderr)

def periodic_notify(interval, count, dry_run=False):
    for i in range(count):
        quote = random_quote()
        notify_quote(quote, dry_run=dry_run)
        log_quote(quote)
        if i < count - 1:
            time.sleep(interval)

def parse_args():
    parser = argparse.ArgumentParser(description="Random OS Motivational Quote Notifier")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_notify = subparsers.add_parser("notify", help="Send a random motivational quote notification once")
    parser_notify.add_argument("--dry-run", action="store_true", help="Print instead of sending OS notification")

    parser_periodic = subparsers.add_parser("periodic", help="Send notifications periodically")
    parser_periodic.add_argument("--interval", type=int, default=1800, help="Interval in seconds (default: 1800)")
    parser_periodic.add_argument("--count", type=int, default=3, help="Number of notifications (default: 3)")
    parser_periodic.add_argument("--dry-run", action="store_true", help="Print instead of sending OS notification")

    parser_list = subparsers.add_parser("list", help="List all possible quotes")

    parser_log = subparsers.add_parser("log", help="Show notification log")

    parser_summary = subparsers.add_parser("summary", help="Show summary of notifications sent")

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == "notify":
        quote = random_quote()
        notify_quote(quote, dry_run=args.dry_run)
        log_quote(quote)
    elif args.command == "periodic":
        periodic_notify(args.interval, args.count, dry_run=args.dry_run)
    elif args.command == "list":
        list_quotes()
    elif args.command == "log":
        show_log()
    elif args.command == "summary":
        summary_log()
    else:
        print("Unknown command.")

if __name__ == '__main__':
    main()
