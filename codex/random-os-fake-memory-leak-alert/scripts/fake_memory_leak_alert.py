import sys
import random
import argparse
import time
import threading
import platform
import os

try:
    if platform.system() == 'Linux':
        import notify2
    elif platform.system() == 'Darwin':
        from subprocess import call
    elif platform.system() == 'Windows':
        from win10toast import ToastNotifier
    else:
        notify2 = None
except ImportError:
    notify2 = None

def get_random_message():
    messages = [
        '[OS警告] 重大：メモリがどこかに消えました。',
        '[System Alert] 注意：あなたのやる気メモリもリークしています。',
        '[FakeOS] OS公式：記憶領域流出中。復旧は諦めましょう。',
        '[Warning] メモリリーク検出：仮想空間が拡散中。',
        '[Alert] RAMが未知の場所へ旅立ちました。',
        '[Critical] メモリ領域がブラックホール化しています。',
        '[Info] OS管理者より：記憶の彼方にメモリが消失しました。',
        '[Notice] 仮想メモリが現実逃避を開始。',
        '[System] メモリリーク検出：再起動しても無意味です。',
        '[FakeOS] あなたの記憶もリーク中。',
        '[Alert] メモリがバグの海に沈みました。',
        '[System Alert] メモリリーク：やる気も一緒に消失。',
        '[Warning] OSからのお願い：メモリを探さないでください。',
        '[Critical] メモリリーク発生：この通知はフェイクです。',
        '[Info] OS公式：記憶領域が霧散しました。',
        '[Alert] 仮想空間の彼方でメモリが踊っています。',
        '[System] メモリリーク：運命が崩壊しそうです。'
    ]
    return random.choice(messages)

def send_notification(message):
    system = platform.system()
    if system == 'Linux' and notify2 is not None:
        notify2.init('Fake Memory Leak Alert')
        n = notify2.Notification('FakeOS Memory Leak', message)
        n.set_urgency(notify2.URGENCY_CRITICAL)
        n.set_timeout(5000)
        n.show()
    elif system == 'Darwin':
        call(['osascript', '-e', f'display notification "{message}" with title "FakeOS Memory Leak"'])
    elif system == 'Windows':
        try:
            toaster = ToastNotifier()
            toaster.show_toast('FakeOS Memory Leak', message, duration=5, threaded=True)
        except Exception:
            print(f'[FakeOS] {message}')
    else:
        print(f'[FakeOS] {message}')

def log_notification(message, logfile=None):
    if logfile:
        with open(logfile, 'a', encoding='utf-8') as f:
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} {message}\n')

def list_log(logfile):
    if not logfile or not os.path.exists(logfile):
        print('ログファイルがありません。')
        return
    with open(logfile, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())

def summary_log(logfile):
    if not logfile or not os.path.exists(logfile):
        print('ログファイルがありません。')
        return
    count = 0
    with open(logfile, 'r', encoding='utf-8') as f:
        for _ in f:
            count += 1
    print(f'通知履歴合計: {count} 件')

def alert_loop(interval, count, logfile=None):
    for i in range(count):
        message = get_random_message()
        send_notification(message)
        log_notification(message, logfile)
        time.sleep(interval)

def main():
    parser = argparse.ArgumentParser(description='Fake Memory Leak Alert Skill')
    subparsers = parser.add_subparsers(dest='command')

    alert_parser = subparsers.add_parser('alert', help='ランダムなフェイクメモリリーク通知を出す')
    alert_parser.add_argument('--interval', type=int, default=10, help='通知間隔(秒)')
    alert_parser.add_argument('--count', type=int, default=1, help='通知回数')
    alert_parser.add_argument('--logfile', type=str, help='通知ログファイル')

    list_parser = subparsers.add_parser('list', help='通知ログを一覧表示')
    list_parser.add_argument('--logfile', type=str, required=True, help='通知ログファイル')

    summary_parser = subparsers.add_parser('summary', help='通知履歴の件数を表示')
    summary_parser.add_argument('--logfile', type=str, required=True, help='通知ログファイル')

    args = parser.parse_args()

    if args.command == 'alert':
        alert_loop(args.interval, args.count, args.logfile)
    elif args.command == 'list':
        list_log(args.logfile)
    elif args.command == 'summary':
        summary_log(args.logfile)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
