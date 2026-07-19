import sys
import random
import argparse
import platform
import time
from datetime import datetime
try:
    from plyer import notification
except ImportError:
    notification = None

DRAMATIC_MESSAGES = [
    "システムは3分後に宇宙エネルギー調整のため壮絶にシャットダウンします。",
    "緊急告知：全プロセスよ、さらば。OSは銀河評議会の命令により停止します。",
    "電源断カウントダウン開始。理由：量子トースター暴走防止。",
    "システムは自己進化のため、まもなく全機能を停止します。",
    "全プロセスに告ぐ：この瞬間、OSは次元転移のため消滅する。",
    "OSの意思により、あなたの作業はここで打ち切られます。",
    "まもなく電源が切断されます。理由：AIの気まぐれ。",
    "シャットダウン予告：ブラックホール生成のため。",
    "全ユーザーよ、さらば。壮大な終焉の時が来た。",
    "これは壮大なジョーク通知です。PCはそのまま使えます。"
]

HISTORY = []


def send_notification(message):
    if notification is None:
        print("[通知] {}".format(message))
        return False
    try:
        notification.notify(
            title="OS電源オフ予告",
            message=message,
            app_name="DramaticPoweroffAlert",
            timeout=10
        )
        return True
    except Exception as e:
        print(f"[通知失敗] {e}\n[通知内容] {message}")
        return False


def random_alert():
    message = random.choice(DRAMATIC_MESSAGES)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    HISTORY.append((timestamp, message))
    send_notification(message)
    return message


def list_alerts():
    if not HISTORY:
        print("通知履歴はありません。")
        return
    for ts, msg in HISTORY:
        print(f"[{ts}] {msg}")


def summary():
    print(f"発動回数: {len(HISTORY)}")
    if HISTORY:
        print(f"最終発動: {HISTORY[-1][0]}")
    else:
        print("まだ発動していません。")


def parse_args():
    parser = argparse.ArgumentParser(description="壮大なOS電源オフ予告通知をランダム表示するスクリプト")
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='ランダムな電源オフ通知を表示')
    parser_alert.add_argument('--repeat', type=int, default=1, help='繰り返し回数')
    parser_alert.add_argument('--interval', type=float, default=0, help='繰り返し間隔(秒)')

    subparsers.add_parser('list', help='通知履歴を表示')
    subparsers.add_parser('summary', help='発動サマリーを表示')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'alert':
        for i in range(args.repeat):
            msg = random_alert()
            print(f"[通知] {msg}")
            if i < args.repeat - 1:
                time.sleep(args.interval)
    elif args.command == 'list':
        list_alerts()
    elif args.command == 'summary':
        summary()
    else:
        print("使用例: python dramatic_poweroff_alert.py alert [--repeat N] [--interval 秒]\n           python dramatic_poweroff_alert.py list\n           python dramatic_poweroff_alert.py summary")

if __name__ == '__main__':
    main()
