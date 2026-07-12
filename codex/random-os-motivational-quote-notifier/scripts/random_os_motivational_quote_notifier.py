import random
import argparse
import sys
import time
from plyer import notification

QUOTES = [
    "本日もバグに感謝せよ",
    "進捗ゼロ、それもまた進化",
    "コードは寝かせて美味しくなる",
    "OSは気まぐれ、あなたも気まぐれ",
    "仕様変更、それは運命のいたずら",
    "バグは友達、怖くない",
    "エラーは成長の証",
    "リファクタ、それは心の洗濯",
    "動かないコード、それもまた美しい",
    "やる気が出ない、それもまた人生",
    "コミットは愛、プッシュは勇気",
    "レビューは鏡、バグは影",
    "進捗ダメです、それもまた進化",
    "TODOは未来への贈り物",
    "動揺こそが進化の源泉"
]

TITLE = "謎のOSモチベーション格言"


def show_notification(quote: str):
    try:
        notification.notify(
            title=TITLE,
            message=quote,
            timeout=8
        )
    except Exception as e:
        print(f"[ERROR] 通知の表示に失敗しました: {e}", file=sys.stderr)


def random_quote() -> str:
    return random.choice(QUOTES)


def list_quotes():
    print("--- 登録済み格言一覧 ---")
    for idx, q in enumerate(QUOTES, 1):
        print(f"{idx}. {q}")


def notify_command(args):
    quote = random_quote()
    print(f"[OS通知] {quote}")
    show_notification(quote)


def list_command(args):
    list_quotes()


def summary_command(args):
    print(f"登録格言数: {len(QUOTES)}")
    print(f"例: {random.choice(QUOTES)}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="謎のOSモチベーション格言をランダムに通知します。"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    notify_parser = subparsers.add_parser("notify", help="ランダムな格言をOS通知で表示")
    notify_parser.set_defaults(func=notify_command)

    list_parser = subparsers.add_parser("list", help="格言一覧を表示")
    list_parser.set_defaults(func=list_command)

    summary_parser = subparsers.add_parser("summary", help="格言数とサンプルを表示")
    summary_parser.set_defaults(func=summary_command)

    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
