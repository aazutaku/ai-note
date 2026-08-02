import random
import time
import argparse
import sys
import subprocess
from datetime import datetime, timedelta

FAKE_POLICIES = [
    "[重要] 本日よりパスワードは「季節の俳句」＋「円周率12桁」＋「好きな給食メニュー」が必須となります。",
    "[新ルール] 母音だけのパスワードはご利用いただけません。",
    "[推奨] 毎日ランダムにパスワードを変えましょう（記憶は禁止です）。",
    "[注意] パスワードは漢字・数字・給食メニュー・天気予報を含めてください。",
    "[通達] 1日3回以上パスワードを変更してください。",
    "[警告] 本日からパスワードに干支の名前が必須です。",
    "[必須] すべてのパスワードに3つ以上の季節のフルーツ名を含めてください。",
    "[推奨] パスワードは毎朝6時に自動変更されます。覚えることは禁止です。",
    "[新規則] パスワードの一部に好きなアニメのタイトルを含めてください。",
    "[注意] パスワードは毎回異なる都道府県名を含めてください。"
]

NOTIFY_COMMANDS = [
    ["notify-send", "--version"],
    ["osascript", "-e", "display notification \"test\" with title \"test\""]
]

def is_notify_send_available():
    try:
        subprocess.run(["notify-send", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def is_osascript_available():
    try:
        subprocess.run(["osascript", "-e", "display notification \"test\" with title \"test\""])
        return True
    except FileNotFoundError:
        return False

def send_notification(title, message):
    if is_notify_send_available():
        try:
            subprocess.run(["notify-send", title, message])
        except Exception as e:
            print(f"[通知失敗] {e}")
    elif is_osascript_available():
        try:
            osa_cmd = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", osa_cmd])
        except Exception as e:
            print(f"[通知失敗] {e}")
    else:
        print(f"[通知] {title}: {message}")


def random_policy():
    return random.choice(FAKE_POLICIES)


def log_event(message, logfile=None):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f"{timestamp} {message}\n"
    if logfile:
        with open(logfile, 'a', encoding='utf-8') as f:
            f.write(line)
    else:
        print(line, end='')


def list_policies():
    for i, policy in enumerate(FAKE_POLICIES, 1):
        print(f"{i}. {policy}")


def summary():
    print(f"全{len(FAKE_POLICIES)}種類の偽パスワードポリシーが登録されています。\n")
    print("例:")
    for policy in random.sample(FAKE_POLICIES, min(3, len(FAKE_POLICIES))):
        print(f"- {policy}")


def periodic_alert(interval_sec, count, logfile=None):
    for i in range(count):
        policy = random_policy()
        send_notification("OSパスワードポリシー変更", policy)
        log_event(f"通知: {policy}", logfile)
        if i < count - 1:
            time.sleep(interval_sec)


def main():
    parser = argparse.ArgumentParser(description="偽のOSパスワードポリシー変更通知をランダムに表示するスクリプト")
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='1回だけ偽パスワードポリシー通知を表示')
    parser_alert.add_argument('--logfile', type=str, help='通知履歴を保存するファイル')

    parser_periodic = subparsers.add_parser('periodic', help='一定間隔で複数回通知')
    parser_periodic.add_argument('--interval', type=int, default=30, help='通知間隔(秒)')
    parser_periodic.add_argument('--count', type=int, default=3, help='通知回数')
    parser_periodic.add_argument('--logfile', type=str, help='通知履歴を保存するファイル')

    parser_list = subparsers.add_parser('list', help='登録されている偽ポリシー一覧を表示')
    parser_summary = subparsers.add_parser('summary', help='概要とサンプルを表示')

    args = parser.parse_args()

    if args.command == 'alert':
        policy = random_policy()
        send_notification("OSパスワードポリシー変更", policy)
        log_event(f"通知: {policy}", args.logfile)
    elif args.command == 'periodic':
        periodic_alert(args.interval, args.count, args.logfile)
    elif args.command == 'list':
        list_policies()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
