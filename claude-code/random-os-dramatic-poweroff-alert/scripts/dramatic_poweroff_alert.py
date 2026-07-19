import sys
import random
import argparse
import time
import platform
from threading import Thread

try:
    from plyer import notification
except ImportError:
    print("plyerパッケージが必要です。pip install plyer でインストールしてください。", file=sys.stderr)
    sys.exit(1)

MESSAGES = [
    "システムはあと3分で壮絶にシャットダウンします（理由：宇宙エネルギー調整のため）",
    "全プロセスよ、さらば…",
    "管理者の気まぐれにより、OSは間もなく伝説となります。",
    "あなたの作業は今、歴史的電源オフの瞬間を迎えます。",
    "システムはブラックホールに吸い込まれます。全員退避！",
    "全ユーザーに最後のメッセージ：さようなら、世界。",
    "OSが自己進化のためリブートします（嘘です）",
    "緊急速報：宇宙政府の命令によりシャットダウンを開始します。",
    "今すぐ保存せよ。OSはまもなく無に帰す。",
    "壮絶な電源オフセレモニーが始まります。"
]

TITLE = "OS Dramatic Poweroff Alert"

HISTORY = []


def send_notification(msg: str):
    notification.notify(
        title=TITLE,
        message=msg,
        timeout=8
    )
    HISTORY.append((time.strftime('%Y-%m-%d %H:%M:%S'), msg))


def random_alert():
    msg = random.choice(MESSAGES)
    send_notification(msg)
    print(f"[通知] {msg}")


def list_history():
    if not HISTORY:
        print("通知履歴はありません。")
        return
    for ts, msg in HISTORY:
        print(f"[{ts}] {msg}")


def summary():
    print(f"通知回数: {len(HISTORY)}")
    if HISTORY:
        last_ts, last_msg = HISTORY[-1]
        print(f"最終通知: {last_ts} - {last_msg}")


def auto_trigger(interval=1800, keywords=None):
    # interval: 秒単位（デフォルト30分）
    print(f"自動発動モード: {interval}秒ごとにランダム通知を送信します。Ctrl+Cで終了。")
    try:
        while True:
            time.sleep(interval)
            random_alert()
    except KeyboardInterrupt:
        print("\n自動発動モードを終了します。")


def parse_args():
    parser = argparse.ArgumentParser(description="OSによる壮大な電源オフ予告通知をランダム表示するスクリプト")
    subparsers = parser.add_subparsers(dest="command", required=False)

    parser_alert = subparsers.add_parser("alert", help="今すぐ壮大な通知を表示")
    parser_auto = subparsers.add_parser("auto", help="一定間隔で自動的に通知を表示")
    parser_auto.add_argument("-i", "--interval", type=int, default=1800, help="通知間隔（秒、デフォルト1800）")
    parser_list = subparsers.add_parser("list", help="通知履歴を表示")
    parser_summary = subparsers.add_parser("summary", help="通知サマリーを表示")

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "alert" or args.command is None:
        random_alert()
    elif args.command == "auto":
        auto_trigger(interval=args.interval)
    elif args.command == "list":
        list_history()
    elif args.command == "summary":
        summary()
    else:
        print("不明なコマンドです。--help を参照してください。", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
