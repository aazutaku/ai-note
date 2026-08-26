import sys
import os
import random
import platform
import argparse
import subprocess
import threading
import time
from typing import List

HAIKUS = [
    'バグの香や　春まだ遠き　デバッグ道',
    '落ちるたび　静かに咲ける　桜かな',
    'エラー音　夜更けの窓に　風ひとつ',
    '無限ループ　朝焼けとともに　終わりなし',
    '例外や　心静かに　ログを見る',
    'ビルド落ち　コーヒー冷めて　春霞',
    'リトライを　重ねて学ぶ　秋の夜',
    'スタックトレース　読めども読めど　霧の中',
    'メモリリーク　消えゆく夢と　プロセスよ',
    '警告の　色づく秋に　リファクタ'
]

NOTIFY_TITLE = 'OSからの神託:'


def pick_random_haiku() -> str:
    return random.choice(HAIKUS)


def notify_mac(message: str):
    script = f'display notification "{message}" with title "{NOTIFY_TITLE}"'
    subprocess.run(['osascript', '-e', script], check=False)


def notify_linux(message: str):
    subprocess.run(['notify-send', NOTIFY_TITLE, message, '-t', '4000'], check=False)


def notify_windows(message: str):
    try:
        import win10toast
        toaster = win10toast.ToastNotifier()
        toaster.show_toast(NOTIFY_TITLE, message, duration=4, threaded=True)
    except ImportError:
        # Fallback: Powershell toast
        script = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
        script += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
        script += f'$template.GetElementsByTagName("text")[0].AppendChild($template.CreateTextNode("{NOTIFY_TITLE}")) > $null;'
        script += f'$template.GetElementsByTagName("text")[1].AppendChild($template.CreateTextNode("{message}")) > $null;'
        script += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
        script += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("HaikuNotifier");'
        script += f'$notifier.Show($toast);'
        subprocess.run(['powershell', '-Command', script], check=False)


def send_notification(message: str):
    sys_platform = platform.system()
    if sys_platform == 'Darwin':
        notify_mac(message)
    elif sys_platform == 'Linux':
        notify_linux(message)
    elif sys_platform == 'Windows':
        notify_windows(message)
    else:
        print(f'[通知] {NOTIFY_TITLE}\n{message}')


def monitor_stderr():
    """
    Read lines from stdin (assumed to be piped from stderr), and send notification on each line.
    """
    for line in sys.stdin:
        if line.strip():
            haiku = pick_random_haiku()
            send_notification(haiku)
            time.sleep(0.5)  # avoid spamming


def simulate_error_events(interval: int = 10):
    """
    For demo/testing: periodically send random haiku notification.
    """
    try:
        while True:
            haiku = pick_random_haiku()
            send_notification(haiku)
            time.sleep(interval)
    except KeyboardInterrupt:
        print('Stopped simulation.')


def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Error Haiku Notifier')
    subparsers = parser.add_subparsers(dest='command')

    parser_stderr = subparsers.add_parser('monitor', help='Monitor stdin (stderr) and notify on error lines')
    parser_sim = subparsers.add_parser('simulate', help='Send random haiku notifications periodically')
    parser_sim.add_argument('--interval', type=int, default=10, help='Interval seconds between notifications')

    parser_once = subparsers.add_parser('once', help='Send one random haiku notification')

    args = parser.parse_args()

    if args.command == 'monitor':
        monitor_stderr()
    elif args.command == 'simulate':
        simulate_error_events(args.interval)
    elif args.command == 'once':
        haiku = pick_random_haiku()
        send_notification(haiku)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
