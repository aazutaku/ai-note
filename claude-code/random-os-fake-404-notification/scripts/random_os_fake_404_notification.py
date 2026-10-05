import sys
import os
import random
import time
import argparse
import platform
from datetime import datetime, timedelta

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

def get_messages():
    return [
        '404: あなたのやる気が見つかりません',
        '404: 今日の集中力が迷子です',
        '404: 予定されていた進捗が行方不明です',
        '404: 休憩予定が未検出です',
        '404: 本日の生産性が応答しません',
        '404: コーヒーの補給が必要です',
        '404: 進捗ファイルが破損しています',
        '404: 明日のやる気が読み込めません',
        '404: モチベーションサーバーに接続できません',
        '404: タスク管理AIがフリーズしました',
        '404: 週末が見つかりません',
        '404: 夢と希望がタイムアウトしました',
        '404: 予定表が空です',
        '404: 進捗報告書が消失しました',
        '404: 休憩ボタンが反応しません',
        '404: 睡眠APIが応答しません',
        '404: インスピレーションが見つかりません',
        '404: 明日の天気が不明です',
        '404: 進捗メーターがゼロです',
        '404: 仕事スイッチがオフです'
    ]

def send_notification(message):
    system = platform.system()
    if PLYER_AVAILABLE:
        notification.notify(
            title='OS Notification',
            message=message,
            app_name='random-os-fake-404-notification',
            timeout=7
        )
    else:
        if system == 'Darwin':  # macOS
            script = f'display notification "{message}" with title "OS Notification"'
            os.system(f"osascript -e '{script}'")
        elif system == 'Linux':
            os.system(f'notify-send "OS Notification" "{message}"')
        elif system == 'Windows':
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("OS Notification", message, duration=7)
            except ImportError:
                print(f'[OS Notification] {message}')
        else:
            print(f'[OS Notification] {message}')

def random_interval(min_sec=1200, max_sec=3600):
    return random.randint(min_sec, max_sec)

def log_event(message, logfile='~/.random_os_fake_404.log'):
    path = os.path.expanduser(logfile)
    with open(path, 'a', encoding='utf-8') as f:
        f.write(f'{datetime.now().isoformat()}\t{message}\n')

def list_events(logfile='~/.random_os_fake_404.log', last=10):
    path = os.path.expanduser(logfile)
    if not os.path.exists(path):
        print('No log found.')
        return
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines[-last:]:
        print(line.strip())

def summary_events(logfile='~/.random_os_fake_404.log'):
    path = os.path.expanduser(logfile)
    if not os.path.exists(path):
        print('No log found.')
        return
    total = 0
    by_day = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            total += 1
            date = line.split('T')[0]
            by_day[date] = by_day.get(date, 0) + 1
    print(f'Total notifications: {total}')
    for date, count in sorted(by_day.items()):
        print(f'{date}: {count}')

def run_random_loop(args):
    print('random-os-fake-404-notification: 開始します (Ctrl+Cで終了)')
    try:
        while True:
            interval = random_interval(args.min_interval, args.max_interval)
            time.sleep(interval)
            message = random.choice(get_messages())
            send_notification(message)
            log_event(message)
    except KeyboardInterrupt:
        print('\n終了しました')

def trigger_once(args):
    message = random.choice(get_messages())
    send_notification(message)
    log_event(message)
    print(f'[OS Notification] {message}')

def main():
    parser = argparse.ArgumentParser(description='random-os-fake-404-notification')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='定期的にランダム通知を発生')
    parser_run.add_argument('--min-interval', type=int, default=1200, help='通知間隔の最小秒数 (デフォルト: 1200=20分)')
    parser_run.add_argument('--max-interval', type=int, default=3600, help='通知間隔の最大秒数 (デフォルト: 3600=60分)')

    parser_once = subparsers.add_parser('once', help='1回だけ通知を表示')

    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_list.add_argument('--last', type=int, default=10, help='直近N件 (デフォルト: 10)')

    parser_summary = subparsers.add_parser('summary', help='通知履歴の集計')

    args = parser.parse_args()

    if args.command == 'run':
        run_random_loop(args)
    elif args.command == 'once':
        trigger_once(args)
    elif args.command == 'list':
        list_events(last=getattr(args, 'last', 10))
    elif args.command == 'summary':
        summary_events()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
