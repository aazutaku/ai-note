import random
import time
import sys
import argparse
import threading
from datetime import datetime
try:
    from plyer import notification
except ImportError:
    notification = None

FAKE_404_MESSAGES = [
    '404: 今日の集中力が迷子です',
    '404 Not Found: 予定されていた進捗が行方不明です',
    '404: あなたのやる気が見つかりません',
    '404 Error: コーヒーブレイクが必要です',
    '404: 残業回避モードが見つかりません',
    '404: 週末の気配が検出できません',
    '404: タスク完了フラグが見つかりません',
    '404: 眠気除去サービスが利用できません',
    '404: クリエイティブモードが応答しません',
    '404: 予定外のやる気が発生しました',
    '404: 重要な締切が未検出です',
    '404: 休憩時間がタイムアウトしました',
    '404: 進捗の神様が不在です',
    '404: モチベーションファイルが破損しています',
    '404: 本日の生産性が見つかりません',
    '404: 眠気が検出されました',
    '404: 予定されていた集中力が見つかりません',
    '404: 週明けのやる気が応答しません',
    '404: 目標達成パスが見つかりません',
    '404: 進捗報告書が消失しました'
]

NOTIFY_INTERVAL_MIN = 45 * 60  # 45分
NOTIFY_INTERVAL_MAX = 90 * 60  # 90分

HISTORY = []


def send_notification(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    HISTORY.append({'time': timestamp, 'message': message})
    if notification:
        notification.notify(
            title='404 Notification',
            message=message,
            timeout=8
        )
    else:
        print(f'[通知] {message}')


def random_notify_loop(stop_event):
    while not stop_event.is_set():
        wait_time = random.randint(NOTIFY_INTERVAL_MIN, NOTIFY_INTERVAL_MAX)
        stop_event.wait(wait_time)
        if stop_event.is_set():
            break
        message = random.choice(FAKE_404_MESSAGES)
        send_notification(message)


def list_history():
    if not HISTORY:
        print('通知履歴はありません。')
        return
    for entry in HISTORY:
        print(f"{entry['time']} - {entry['message']}")


def summary():
    print(f'通知発火回数: {len(HISTORY)}')
    if HISTORY:
        print(f'最新通知: {HISTORY[-1]["time"]} - {HISTORY[-1]["message"]}')


def manual_notify():
    message = random.choice(FAKE_404_MESSAGES)
    send_notification(message)


def main():
    parser = argparse.ArgumentParser(description='random-os-fake-404-notification')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('run', help='ランダムなタイミングで偽404通知を発火')
    subparsers.add_parser('notify', help='今すぐ偽404通知を1回発火')
    subparsers.add_parser('list', help='通知履歴を表示')
    subparsers.add_parser('summary', help='通知回数などサマリーを表示')

    args = parser.parse_args()

    if args.command == 'run':
        stop_event = threading.Event()
        try:
            print('random-os-fake-404-notification: 起動中 (Ctrl+Cで停止)')
            random_notify_loop(stop_event)
        except KeyboardInterrupt:
            stop_event.set()
            print('\n終了します')
    elif args.command == 'notify':
        manual_notify()
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
