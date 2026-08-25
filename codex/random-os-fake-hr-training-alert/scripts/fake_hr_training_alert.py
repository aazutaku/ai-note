import sys
import os
import random
import argparse
import platform
import subprocess
import time
from datetime import datetime

NOTIFICATION_TEMPLATES = [
    '[ALERT] 緊急：本日{hour}:{minute}より「{title}」研修が強制開催されます。',
    '[NOTICE] 重要：OS公式「{title}」研修が今すぐ開始されます。',
    '[WARNING] ただ今より「{title}」への参加が必須です。',
    '[INFO] 新着：本日{hour}:{minute}より「{title}」研修が始まります。',
    '[ALERT] 参加必須：OS人事部主催「{title}」研修が開幕！',
    '[NOTICE] 重要：{weekday}は「{title}」研修デーです。',
    '[WARNING] 緊急連絡：{title}研修のリマインダーです。',
    '[INFO] ご注意：「{title}」研修の事前課題があります。',
    '[ALERT] 本日中に「{title}」研修の受講を完了してください。',
    '[NOTICE] 重要：「{title}」研修の参加が義務付けられました。'
]

TRAINING_TITLES = [
    '謎のパワポ芸入門',
    '無限ビデオ視聴',
    '謎マナー講座',
    'リモート背景選手権',
    '無限フィードバック地獄',
    '謎のオンライン自己紹介',
    'OS公式エア出社体験',
    '謎のカメラON強制',
    '無限アンケート回答',
    '謎の社内用語暗記',
    '謎のバーチャル飲み会',
    '謎のエクセル芸道場',
    '謎のSlackスタンプ研修',
    '謎の仮想会議耐久',
    'OS人事部謎のサバイバル',
    '謎のアイスブレイク選手権',
    '謎のリモート雑談訓練',
    '謎のマイクON地獄',
    '謎のカレンダー共有講座',
    '謎の無限リマインダー研修'
]

WEEKDAYS = ['月曜', '火曜', '水曜', '木曜', '金曜']


def get_random_time():
    hour = random.randint(8, 18)
    minute = random.choice(['00', '15', '30', '45'])
    return hour, minute

def get_random_weekday():
    return random.choice(WEEKDAYS)

def generate_notification():
    template = random.choice(NOTIFICATION_TEMPLATES)
    title = random.choice(TRAINING_TITLES)
    hour, minute = get_random_time()
    weekday = get_random_weekday()
    return template.format(title=title, hour=str(hour).zfill(2), minute=minute, weekday=weekday)


def show_terminal_notification(msg):
    print(msg)


def show_desktop_notification(msg):
    sys_platform = platform.system()
    try:
        if sys_platform == 'Darwin':  # macOS
            subprocess.run([
                'osascript', '-e', f'display notification "{msg}" with title "人事研修アラート"'
            ], check=True)
        elif sys_platform == 'Linux':
            # notify-sendがあれば使う
            if subprocess.call(['which', 'notify-send'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
                subprocess.run([
                    'notify-send', '人事研修アラート', msg
                ], check=True)
            else:
                show_terminal_notification(msg)
        elif sys_platform == 'Windows':
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("人事研修アラート", msg, duration=6)
            except ImportError:
                show_terminal_notification(msg)
        else:
            show_terminal_notification(msg)
    except Exception as e:
        show_terminal_notification(f"[通知失敗] {msg} ({e})")


def main():
    parser = argparse.ArgumentParser(description='謎の人事研修強制通知をランダムに表示します')
    subparsers = parser.add_subparsers(dest='command', help='サブコマンド')

    parser_alert = subparsers.add_parser('alert', help='今すぐランダム通知を1件表示')
    parser_alert.add_argument('--desktop', action='store_true', help='デスクトップ通知も試行')

    parser_batch = subparsers.add_parser('batch', help='複数回ランダム通知を表示')
    parser_batch.add_argument('-n', type=int, default=5, help='通知回数 (デフォルト: 5)')
    parser_batch.add_argument('--interval', type=float, default=2.0, help='通知間隔秒 (デフォルト: 2.0)')
    parser_batch.add_argument('--desktop', action='store_true', help='デスクトップ通知も試行')

    parser_list = subparsers.add_parser('list', help='サンプル通知を一覧表示')
    parser_list.add_argument('-n', type=int, default=10, help='表示件数')

    args = parser.parse_args()

    if args.command == 'alert':
        msg = generate_notification()
        show_terminal_notification(msg)
        if args.desktop:
            show_desktop_notification(msg)
    elif args.command == 'batch':
        for i in range(args.n):
            msg = generate_notification()
            show_terminal_notification(msg)
            if args.desktop:
                show_desktop_notification(msg)
            if i < args.n - 1:
                time.sleep(args.interval)
    elif args.command == 'list':
        for _ in range(args.n):
            msg = generate_notification()
            print(msg)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
