import sys
import argparse
import random
import time
import threading
import platform
import subprocess
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

NOTIFICATIONS = [
    '推奨曲：バグ退治ブルース',
    '本日は“残業パラダイス”を熱唱してください',
    '歌唱力がアップデートされました',
    'OSはあなたのカラオケ魂を検出しました',
    '推奨ジャンル：昭和アニソンメドレー',
    '今すぐ「仕様書のブルース」を熱唱しましょう',
    'あなたのカラオケランキングが上昇しました',
    'OSの気分：今日はカラオケ日和',
    '推奨アクション：エアマイク準備',
    '現実逃避モードがONになりました'
]

LOG_FILE = 'karaoke_alert.log'


def show_notification(message):
    system = platform.system()
    if PLYER_AVAILABLE:
        notification.notify(
            title='[通知] OSカラオケ推奨',
            message=message,
            app_name='random-os-karaoke-alert',
            timeout=7
        )
    else:
        if system == 'Darwin':
            subprocess.run([
                'osascript', '-e', f'display notification "{message}" with title "OSカラオケ推奨"'
            ])
        elif system == 'Linux':
            subprocess.run([
                'notify-send', 'OSカラオケ推奨', message])
        elif system == 'Windows':
            # fallback: print to console
            print(f'[通知] {message}')
        else:
            print(f'[通知] {message}')


def log_notification(message):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} {message}\n')


def random_alert_loop(min_interval=600, max_interval=3600, stop_event=None):
    while not (stop_event and stop_event.is_set()):
        interval = random.randint(min_interval, max_interval)
        time.sleep(interval)
        msg = random.choice(NOTIFICATIONS)
        show_notification(msg)
        log_notification(msg)


def list_log():
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line in lines[-20:]:
            print(line.strip())
    except FileNotFoundError:
        print('ログがありません。')


def summary_log():
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        count = len(lines)
        print(f'通知履歴: {count}件')
        freq = {}
        for line in lines:
            for msg in NOTIFICATIONS:
                if msg in line:
                    freq[msg] = freq.get(msg, 0) + 1
        for msg, cnt in sorted(freq.items(), key=lambda x: -x[1]):
            print(f'{msg}: {cnt}回')
    except FileNotFoundError:
        print('ログがありません。')


def run_once():
    msg = random.choice(NOTIFICATIONS)
    show_notification(msg)
    log_notification(msg)
    print(f'[通知] {msg}')


def main():
    parser = argparse.ArgumentParser(description='random-os-karaoke-alert: OS風カラオケ推奨通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='1回だけ通知を表示')
    parser_loop = subparsers.add_parser('loop', help='バックグラウンドでランダム通知')
    parser_loop.add_argument('--min', type=int, default=600, help='最小間隔秒 (デフォルト600)')
    parser_loop.add_argument('--max', type=int, default=3600, help='最大間隔秒 (デフォルト3600)')
    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知履歴の集計')

    args = parser.parse_args()
    if args.command == 'alert':
        run_once()
    elif args.command == 'loop':
        stop_event = threading.Event()
        try:
            print('ランダム通知モード開始 (Ctrl+Cで停止)')
            random_alert_loop(args.min, args.max, stop_event)
        except KeyboardInterrupt:
            stop_event.set()
            print('\n停止しました。')
    elif args.command == 'list':
        list_log()
    elif args.command == 'summary':
        summary_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
