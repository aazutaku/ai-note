import sys
import argparse
import random
import time
import threading
import platform

try:
    from plyer import notification
except ImportError:
    notification = None

APOLOGY_MESSAGES = [
    "本日はご迷惑をおかけしております。",
    "謎の遅延が発生しましたが、原因不明です。",
    "大変申し訳ありませんが、さっきのコマンドは無かったことにしてください。",
    "予期せぬ問題が発生しましたが、詳細は不明です。",
    "ご不便をおかけし、心よりお詫び申し上げます。",
    "この通知は自動生成されました。ご安心ください。",
    "現在、何も問題は発生していませんが、念のため謝罪いたします。",
    "システムが一時的に自己嫌悪に陥りました。ご容赦ください。",
    "不明なエラーが発生したかもしれません。多分大丈夫です。",
    "本件については追ってご連絡…しません。ご了承ください。",
    "OSの気まぐれで通知しています。特に意味はありません。",
    "申し訳ありませんが、詳細は社内規定により非公開です。"
]

DEFAULT_INTERVAL = 600  # 10分
MIN_INTERVAL = 60       # 1分
MAX_INTERVAL = 3600     # 1時間


def send_notification(message):
    if notification is None:
        print(f"[通知] {message}")
        return
    title = "OSからのお詫び"
    notification.notify(
        title=title,
        message=message,
        app_name="random-os-apology-notifier",
        timeout=8
    )


def random_apology():
    return random.choice(APOLOGY_MESSAGES)


def notify_once():
    message = random_apology()
    send_notification(message)


def notify_loop(interval, count=None):
    sent = 0
    try:
        while count is None or sent < count:
            notify_once()
            sent += 1
            if count is not None and sent >= count:
                break
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[INFO] 通知ループを中断しました。")


def list_messages():
    print("利用可能な謝罪メッセージ一覧:")
    for i, msg in enumerate(APOLOGY_MESSAGES, 1):
        print(f"{i:2}: {msg}")


def summary():
    print("random-os-apology-notifier の概要:")
    print(f"  メッセージ数: {len(APOLOGY_MESSAGES)}")
    print(f"  デフォルト通知間隔: {DEFAULT_INTERVAL//60}分")
    print(f"  サポートOS: Windows, macOS, Linux (plyer利用)")
    print(f"  plyerインストール済: {'Yes' if notification else 'No'}")


def main():
    parser = argparse.ArgumentParser(
        description="謎のOS謝罪通知をデスクトップに表示します。"
    )
    subparsers = parser.add_subparsers(dest="command", required=False)

    parser_once = subparsers.add_parser("once", help="1回だけ謝罪通知を表示")
    parser_loop = subparsers.add_parser("loop", help="定期的に謝罪通知を表示")
    parser_loop.add_argument("-i", "--interval", type=int, default=DEFAULT_INTERVAL,
                            help="通知間隔(秒)。デフォルト600秒(10分)")
    parser_loop.add_argument("-n", "--count", type=int, default=None,
                            help="通知回数。指定しない場合は無限ループ")
    parser_list = subparsers.add_parser("list", help="謝罪メッセージ一覧を表示")
    parser_summary = subparsers.add_parser("summary", help="Skill概要を表示")

    args = parser.parse_args()

    if args.command == "once":
        notify_once()
    elif args.command == "loop":
        interval = args.interval
        if interval < MIN_INTERVAL or interval > MAX_INTERVAL:
            print(f"[ERROR] 通知間隔は{MIN_INTERVAL}～{MAX_INTERVAL}秒で指定してください。")
            sys.exit(1)
        notify_loop(interval, args.count)
    elif args.command == "list":
        list_messages()
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
