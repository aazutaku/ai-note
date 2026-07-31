import sys
import os
import random
import time
import argparse
import platform
import subprocess
from datetime import datetime, timedelta

LOG_PATH = os.path.expanduser('~/.random_os_karaoke_alert.log')

NOTIFICATIONS = [
    '本日は“残業パラダイス”を熱唱してください。',
    '推奨曲: バグ退治ブルース',
    '歌唱力がアップデートされました。今すぐ一曲いかがですか？',
    'OSより: カラオケ休憩の時刻です。',
    'システム: “仕様書ブルース”を歌うとバグが減るかもしれません。',
    '推奨曲: デバッグ・ナイトフィーバー',
    '本日は“コミット・シンフォニー”でリリースを祝おう！',
    '歌唱力診断: あなたの声はバージョン2.0です。',
    'OSがカラオケを始めたがっています。',
    '推奨: 5分間のカラオケ現実逃避タイム'
]

TITLE = 'OSカラオケ推奨'


def log_notification(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(f'[{timestamp}] {message}\n')


def send_notification(message):
    system = platform.system()
    try:
        if system == 'Darwin':  # macOS
            script = f'display notification "{message}" with title "{TITLE}"'
            subprocess.run(['osascript', '-e', script], check=True)
        elif system == 'Linux':
            subprocess.run(['notify-send', TITLE, message], check=True)
        elif system == 'Windows':
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(TITLE, message, duration=7)
            except ImportError:
                print('win10toastが必要です: pip install win10toast')
        else:
            print(f'通知未対応OS: {system}')
    except Exception as e:
        print(f'通知送信失敗: {e}')
    log_notification(message)


def random_notification():
    message = random.choice(NOTIFICATIONS)
    send_notification(message)
    return message


def list_log():
    if not os.path.exists(LOG_PATH):
        print('通知履歴はありません。')
        return
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


def summary():
    if not os.path.exists(LOG_PATH):
        print('通知履歴はありません。')
        return
    counts = {}
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            for msg in NOTIFICATIONS:
                if msg in line:
                    counts[msg] = counts.get(msg, 0) + 1
    print('通知別発動回数:')
    for msg, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        print(f'  {msg} : {cnt}回')


def monitor_mode(min_minutes=30, max_minutes=120):
    print('ランダム通知モードを開始します (Ctrl+Cで終了)')
    try:
        while True:
            interval = random.randint(min_minutes * 60, max_minutes * 60)
            next_alert = datetime.now() + timedelta(seconds=interval)
            print(f'次の通知予定: {next_alert.strftime("%H:%M:%S")} (約{interval//60}分後)')
            time.sleep(interval)
            random_notification()
    except KeyboardInterrupt:
        print('\nランダム通知モードを終了しました')


def main():
    parser = argparse.ArgumentParser(description='random-os-karaoke-alert: OS風カラオケ推奨通知スキル')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='即座にカラオケ通知を表示')
    parser_monitor = subparsers.add_parser('monitor', help='ランダムな間隔で自動通知')
    parser_monitor.add_argument('--min', type=int, default=30, help='最小インターバル(分)')
    parser_monitor.add_argument('--max', type=int, default=120, help='最大インターバル(分)')
    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知履歴を集計')

    args = parser.parse_args()

    if args.command == 'run':
        msg = random_notification()
        print(f'[通知] {msg}')
    elif args.command == 'monitor':
        monitor_mode(args.min, args.max)
    elif args.command == 'list':
        list_log()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
