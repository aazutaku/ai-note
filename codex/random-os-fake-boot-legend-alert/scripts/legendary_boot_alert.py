import sys
import argparse
import random
import time
import threading
import subprocess
import platform

LEGENDARY_MESSAGES = [
    "[伝説のOS起動通知]\n本日、あなたの端末は選ばれし者として認定されました。\n幻のBIOSがあなたに囁きかけています…\n-- LEGENDARY BOOT SEQUENCE INITIATED --",
    "[伝説のOS起動通知]\nOS界の伝説が今、ここに蘇る。\nあなたの作業環境に“神託”が降り注ぎます。",
    "[伝説のOS起動通知]\n見よ、伝説のカーネルが目覚める瞬間を。\nあなたは今、歴史の証人です。",
    "[伝説のOS起動通知]\n謎のBIOSの声が聞こえる…\nこの起動は、もはや神話の領域。",
    "[伝説のOS起動通知]\n選ばれし者のみが見ることを許された起動シーケンス発動。\nあなたの端末は伝説となった。",
    "[伝説のOS起動通知]\nOS界のレジェンドがあなたを見守っています。\n-- BOOT LEGEND ALERT --",
    "[伝説のOS起動通知]\n本日、幻のOSが降臨しました。\nあなたの作業は伝説の一部となります。",
    "[伝説のOS起動通知]\nBIOSの神託：『選ばれし者よ、今こそ起動の時』\n-- LEGENDARY INIT --",
    "[伝説のOS起動通知]\nこの瞬間、あなたの端末に伝説の風が吹く。",
    "[伝説のOS起動通知]\n伝説のOS起動シーケンスが発動しました。\n混乱せず、作業を続けてください。"
]

HISTORY = []


def show_notification(message):
    system = platform.system()
    if system == "Darwin":  # macOS
        try:
            subprocess.run(['osascript', '-e', f'display notification "{message}" with title "伝説のOS起動通知"'], check=True)
        except Exception:
            print(message)
    elif system == "Linux":
        try:
            subprocess.run(['notify-send', '伝説のOS起動通知', message], check=True)
        except Exception:
            print(message)
    elif system == "Windows":
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast("伝説のOS起動通知", message, duration=5)
        except Exception:
            print(message)
    else:
        print(message)


def random_legendary_message():
    return random.choice(LEGENDARY_MESSAGES)


def alert():
    msg = random_legendary_message()
    HISTORY.append((time.strftime('%Y-%m-%d %H:%M:%S'), msg))
    show_notification(msg)
    print(msg)


def list_history():
    if not HISTORY:
        print("通知履歴はありません。")
        return
    for t, msg in HISTORY:
        print(f"[{t}]\n{msg}\n")


def summary():
    print(f"これまでに{len(HISTORY)}件の伝説通知を発動しました。")


def auto_alert_loop(interval_min=15, interval_max=60, stop_after=3):
    count = 0
    while count < stop_after:
        wait = random.randint(interval_min, interval_max)
        time.sleep(wait)
        alert()
        count += 1


def main():
    parser = argparse.ArgumentParser(description="伝説のOS起動通知スキル")
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='今すぐ伝説通知を発動')
    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知件数を表示')
    parser_auto = subparsers.add_parser('auto', help='自動で伝説通知を発動')
    parser_auto.add_argument('--min', type=int, default=15, help='通知間隔の最小秒数')
    parser_auto.add_argument('--max', type=int, default=60, help='通知間隔の最大秒数')
    parser_auto.add_argument('--count', type=int, default=3, help='通知回数')

    args = parser.parse_args()

    if args.command == 'alert':
        alert()
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    elif args.command == 'auto':
        auto_alert_loop(interval_min=args.min, interval_max=args.max, stop_after=args.count)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
