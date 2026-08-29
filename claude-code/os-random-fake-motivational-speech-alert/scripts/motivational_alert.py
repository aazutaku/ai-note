import os
import sys
import random
import argparse
import datetime
import platform
from pathlib import Path

try:
    # For cross-platform notification
    if platform.system() == 'Darwin':
        import subprocess
    elif platform.system() == 'Linux':
        import subprocess
    elif platform.system() == 'Windows':
        from win10toast import ToastNotifier
except ImportError:
    pass

NOTIFICATION_HISTORY = Path.home() / '.os_random_fake_motivational_speech_alert_history.log'

SPEECHES = [
    'あなたのキーボードの叩き方に情熱を感じます。',
    '今こそコード界の伝説になるときです。',
    'あなたのcommitは宇宙を救う。',
    'その一行が未来を変える。',
    'シンタックスエラーすら、あなたの成長の証です。',
    'タイポは冒険の始まりです。',
    'あなたのpushが世界に波紋を広げます。',
    'OSはあなたの努力を見守っています。',
    'バグは勇者の勲章です。',
    '今この瞬間、あなたはOS公認の勇者です。',
    'レビューの嵐に立ち向かうあなたに敬礼。',
    'デバッグは魂の修行です。',
    'そのコード、未来への架け橋です。',
    'あなたのテストが世界を守る。',
    'OSもあなたの成長に感動しています。',
    'あなたのpull requestは歴史に刻まれるでしょう。',
    'エラーはあなたの味方です。',
    '今日も素晴らしいコードをありがとう。',
    'あなたのロジックに宇宙が震えています。',
    'OS公式: その情熱、無限大。',
]


def notify(message):
    """
    Cross-platform notification. Falls back to stdout if GUI notification fails.
    """
    system = platform.system()
    notified = False
    try:
        if system == 'Darwin':
            subprocess.run(['osascript', '-e', f'display notification "{message}" with title "OS公式通知"'], check=True)
            notified = True
        elif system == 'Linux':
            subprocess.run(['notify-send', 'OS公式通知', message], check=True)
            notified = True
        elif system == 'Windows':
            toaster = ToastNotifier()
            toaster.show_toast('OS公式通知', message, duration=5)
            notified = True
    except Exception:
        pass
    if not notified:
        print(f'[OS公式通知] {message}')


def log_notification(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(NOTIFICATION_HISTORY, 'a', encoding='utf-8') as f:
        f.write(f'{timestamp}\t{message}\n')


def random_speech():
    return random.choice(SPEECHES)


def show_random_notifications(count=1):
    for _ in range(count):
        msg = random_speech()
        notify(msg)
        log_notification(msg)


def list_history(limit=10):
    if not NOTIFICATION_HISTORY.exists():
        print('通知履歴はまだありません。')
        return
    with open(NOTIFICATION_HISTORY, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if not lines:
        print('通知履歴はまだありません。')
        return
    print(f'直近{min(limit, len(lines))}件の通知履歴:')
    for line in lines[-limit:]:
        print(line.strip())


def summary_history():
    if not NOTIFICATION_HISTORY.exists():
        print('通知履歴はまだありません。')
        return
    with open(NOTIFICATION_HISTORY, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f'通知発行回数: {len(lines)}')
    dates = {}
    for line in lines:
        date = line.split('\t')[0].split(' ')[0]
        dates[date] = dates.get(date, 0) + 1
    print('日別通知数:')
    for date, cnt in sorted(dates.items()):
        print(f'  {date}: {cnt}')


def parse_args():
    parser = argparse.ArgumentParser(description='OS公式やる気爆上げスピーチ通知')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='ランダム通知を表示')
    parser_alert.add_argument('--count', type=int, default=1, help='連続通知回数')

    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_list.add_argument('--limit', type=int, default=10, help='表示件数')

    parser_summary = subparsers.add_parser('summary', help='通知履歴のサマリ表示')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'alert' or args.command is None:
        cnt = getattr(args, 'count', 1)
        show_random_notifications(cnt)
    elif args.command == 'list':
        list_history(args.limit)
    elif args.command == 'summary':
        summary_history()
    else:
        print('不明なコマンドです。--help を参照してください。')

if __name__ == '__main__':
    main()
