import sys
import os
import time
import threading
import argparse
import random
import subprocess

try:
    import notify2
    NOTIFY_AVAILABLE = True
except ImportError:
    NOTIFY_AVAILABLE = False

NAP_MESSAGES = [
    '検出：うたた寝モード突入',
    'OS推奨：夢の中でバグ修正をどうぞ',
    '睡眠ログをクラウドにアップロード中...',
    '注意：キーボードが恋しがっています',
    '謎のOSアラート：作業復帰をお待ちしています',
    '警告：OSが夢の世界へ誘導中',
    'お昼寝検出：コーヒーブレイク推奨',
    'サボりログをAIで解析中...',
    '作業再開をOSが待機しています',
    'お昼寝モード：生産性低下中'
]

LAST_ACTIVITY_FILE = os.path.expanduser('~/.random_os_nap_last_activity')

CHECK_INTERVAL = 2  # seconds
NAP_THRESHOLD = 30  # seconds


def get_last_activity_time():
    if not os.path.exists(LAST_ACTIVITY_FILE):
        return time.time()
    try:
        with open(LAST_ACTIVITY_FILE, 'r') as f:
            return float(f.read().strip())
    except Exception:
        return time.time()


def update_last_activity_time():
    try:
        with open(LAST_ACTIVITY_FILE, 'w') as f:
            f.write(str(time.time()))
    except Exception:
        pass


def send_notification(message):
    # Try desktop notification
    if NOTIFY_AVAILABLE:
        try:
            notify2.init('Random OS Nap Detection')
            n = notify2.Notification('OSお昼寝検出アラート', message)
            n.set_urgency(notify2.URGENCY_NORMAL)
            n.show()
            return
        except Exception:
            pass
    # Fallback: macOS
    if sys.platform == 'darwin':
        try:
            subprocess.run(['osascript', '-e', f'display notification "{message}" with title "OSお昼寝検出アラート"'], check=True)
            return
        except Exception:
            pass
    # Fallback: terminal output
    print(f'[{time.strftime("%H:%M:%S")}] {message}')


def monitor_activity():
    last_alert_time = 0
    while True:
        last_activity = get_last_activity_time()
        now = time.time()
        idle = now - last_activity
        if idle >= NAP_THRESHOLD and (now - last_alert_time) > NAP_THRESHOLD:
            message = random.choice(NAP_MESSAGES)
            send_notification(message)
            last_alert_time = now
        time.sleep(CHECK_INTERVAL)


def log_activity():
    update_last_activity_time()
    print(f'[{time.strftime("%H:%M:%S")}] 活動記録：操作を検知しました')


def list_alerts():
    print('--- OSお昼寝アラート候補一覧 ---')
    for msg in NAP_MESSAGES:
        print(f'- {msg}')


def summary():
    last_activity = get_last_activity_time()
    idle = time.time() - last_activity
    print(f'最終操作から経過: {int(idle)} 秒')
    if idle >= NAP_THRESHOLD:
        print('現在：お昼寝検出アラート発動中')
    else:
        print('現在：活動中')


def main():
    parser = argparse.ArgumentParser(description='random-os-nap-detection-alert skill')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('monitor', help='無操作監視モードでアラートを自動発動')
    subparsers.add_parser('log', help='操作イベントを手動記録')
    subparsers.add_parser('list', help='アラートメッセージ一覧を表示')
    subparsers.add_parser('summary', help='最終操作時刻と状態を表示')
    subparsers.add_parser('alert', help='即時ランダムアラートを発動')

    args = parser.parse_args()

    if args.command == 'monitor':
        print('無操作監視モードを開始します (30秒無操作でアラート発動)')
        monitor_activity()
    elif args.command == 'log':
        log_activity()
    elif args.command == 'list':
        list_alerts()
    elif args.command == 'summary':
        summary()
    elif args.command == 'alert':
        message = random.choice(NAP_MESSAGES)
        send_notification(message)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
