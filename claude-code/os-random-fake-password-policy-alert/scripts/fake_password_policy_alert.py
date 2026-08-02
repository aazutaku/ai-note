import sys
import os
import random
import time
import argparse
import threading
from datetime import datetime

FAKE_POLICIES = [
    "重要：本日よりパスワードは季節の俳句＋円周率12桁＋好きな給食メニュー必須です。",
    "新ルール：母音だけのパスワードは禁止されました。ご注意ください。",
    "推奨：毎日ランダムにパスワードを変えましょう（記憶は禁止です）。",
    "パスワードには最低1つの元素記号を含めてください。",
    "本日よりパスワード変更時は『好きな動物の鳴き声』を3回入力してください。",
    "警告：パスワードに使える文字は、今日の天気によって変わります。",
    "新規ルール：パスワードは5日ごとに『好きな四字熟語』を含めてください。",
    "推奨：パスワード作成時は、必ず親しい同僚に相談してください。",
    "注意：数字部分は必ず素数のみを使用してください。",
    "新ルール：パスワードには一度も使ったことのない単語を含めてください。",
    "推奨：パスワードは毎朝6時に自動リセットされます。",
    "警告：パスワードに『パスワード』という単語を含めてはいけません。",
    "重要：パスワードの長さは円周率の小数点以下の桁数に準じます。",
    "新ルール：パスワードは左右対称でなければなりません。",
    "推奨：パスワードには必ず『好きな給食メニュー』を含めてください。",
    "注意：パスワードは毎回違うフォントで入力してください。",
    "警告：パスワードに使える記号は日替わりです。",
    "新ルール：パスワード変更時は、好きな都道府県を一つ入力してください。"
]

ALERT_LEVELS = ["ALERT", "NOTICE", "INFO", "WARNING"]

HISTORY_FILE = os.path.expanduser("~/.os_random_fake_password_policy_alert.log")


def show_notification(message, level):
    # クロスプラットフォームな通知表示
    try:
        if sys.platform.startswith('darwin'):
            os.system(f'''osascript -e 'display notification "{message}" with title "[{level}] パスワードポリシー通知"' ''')
        elif sys.platform.startswith('linux'):
            os.system(f'''notify-send '[{level}] パスワードポリシー通知' '{message}' ''')
        elif sys.platform.startswith('win'):
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(f"[{level}] パスワードポリシー通知", message, duration=5)
        else:
            print(f"[{level}] {message}")
    except Exception as e:
        print(f"[{level}] {message} (通知失敗: {e})")


def random_policy_message():
    level = random.choice(ALERT_LEVELS)
    message = random.choice(FAKE_POLICIES)
    return level, message


def log_history(level, message):
    try:
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now().isoformat()} [{level}] {message}\n")
    except Exception:
        pass


def list_history(limit=10):
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[-limit:]:
                print(line.strip())
    except FileNotFoundError:
        print("履歴がありません。")


def summary_history():
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"通知履歴件数: {len(lines)}")
            levels = {k: 0 for k in ALERT_LEVELS}
            for line in lines:
                for lvl in ALERT_LEVELS:
                    if f'[{lvl}]' in line:
                        levels[lvl] += 1
            for lvl in ALERT_LEVELS:
                print(f"{lvl}: {levels[lvl]}")
    except FileNotFoundError:
        print("履歴がありません。")


def trigger_alert():
    level, message = random_policy_message()
    show_notification(message, level)
    log_history(level, message)
    print(f"[{level}] {message}")


def periodic_alert(interval_min=10, interval_max=60, stop_after=0):
    start = time.time()
    count = 0
    try:
        while True:
            trigger_alert()
            count += 1
            if stop_after > 0 and count >= stop_after:
                break
            interval = random.randint(interval_min, interval_max)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[INFO] 通知の自動発動を中断しました。")


def main():
    parser = argparse.ArgumentParser(description="ランダムな偽パスワードポリシー通知を表示します。実際の設定には影響しません。")
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='偽パスワードポリシー通知を1回表示')
    parser_periodic = subparsers.add_parser('periodic', help='定期的にランダム通知を表示')
    parser_periodic.add_argument('--min', type=int, default=10, help='最小間隔(秒)')
    parser_periodic.add_argument('--max', type=int, default=60, help='最大間隔(秒)')
    parser_periodic.add_argument('--count', type=int, default=0, help='通知回数(0で無限)')
    parser_list = subparsers.add_parser('list', help='過去の通知履歴を表示')
    parser_list.add_argument('--limit', type=int, default=10, help='表示件数')
    parser_summary = subparsers.add_parser('summary', help='通知履歴のサマリー表示')

    args = parser.parse_args()

    if args.command == 'alert' or args.command is None:
        trigger_alert()
    elif args.command == 'periodic':
        periodic_alert(args.min, args.max, args.count)
    elif args.command == 'list':
        list_history(args.limit)
    elif args.command == 'summary':
        summary_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
