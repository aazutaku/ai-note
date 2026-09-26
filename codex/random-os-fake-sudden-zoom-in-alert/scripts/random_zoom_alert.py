import sys
import time
import random
import argparse
import threading
import platform
import subprocess
from typing import List

ALERT_MESSAGES = [
    '重大：ズームインモード突入まで残り5秒',
    '謎の力により画面拡大率が上昇中…',
    'システム：ズームイン警告！解除方法は不明です',
    '画面拡大率が制御不能になりました',
    '5秒後にズームインが始まるかもしれません',
    '注意：ズームイン解除不能状態を検出',
    '警告：画面拡大率が自動増加しています',
    'ズームインプロセスがバックグラウンドで実行中',
    'ズームイン警告：OS設定が一時的に変更された可能性',
    'ズームインモード：キャンセル不可能',
]

NOTIFY_TITLE = 'ALERT'


def notify_desktop(message: str):
    system = platform.system()
    try:
        if system == 'Darwin':
            subprocess.run([
                'osascript', '-e', f'display notification "{message}" with title "{NOTIFY_TITLE}"'
            ], check=True)
        elif system == 'Linux':
            subprocess.run([
                'notify-send', NOTIFY_TITLE, message
            ], check=True)
        elif system == 'Windows':
            # Use powershell toast notification
            powershell = (
                f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
                f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent(0);'
                f'$textNodes = $template.GetElementsByTagName("text");'
                f'$textNodes.Item(0).AppendChild($template.CreateTextNode("{NOTIFY_TITLE}")) > $null;'
                f'$textNodes.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null;'
                f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
                f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("FakeZoomAlert");'
                f'$notifier.Show($toast);'
            )
            subprocess.run([
                'powershell', '-Command', powershell
            ], check=True)
        else:
            print(f'[{NOTIFY_TITLE}] {message}')
    except Exception as e:
        print(f'[{NOTIFY_TITLE}] {message} (通知失敗: {e})')


def notify_terminal(message: str):
    print(f'[{NOTIFY_TITLE}] {message}')


def random_alert(messages: List[str], desktop: bool = True, terminal: bool = True, min_interval: int = 60, max_interval: int = 300, repeat: int = 3):
    for i in range(repeat):
        wait_time = random.randint(min_interval, max_interval)
        time.sleep(wait_time)
        msg = random.choice(messages)
        if desktop:
            notify_desktop(msg)
        if terminal:
            notify_terminal(msg)


def alert_once(messages: List[str], desktop: bool = True, terminal: bool = True):
    msg = random.choice(messages)
    if desktop:
        notify_desktop(msg)
    if terminal:
        notify_terminal(msg)


def list_messages(messages: List[str]):
    print('--- フェイクズームイン警告メッセージ一覧 ---')
    for m in messages:
        print(f'- {m}')


def main():
    parser = argparse.ArgumentParser(description='謎のOSズームイン警告をランダム表示するフェイク演出スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='今すぐ警告を1回表示')
    parser_alert.add_argument('--desktop', action='store_true', help='デスクトップ通知も表示')
    parser_alert.add_argument('--terminal', action='store_true', help='ターミナルにも表示')

    parser_random = subparsers.add_parser('random', help='ランダムなタイミングで複数回警告')
    parser_random.add_argument('--repeat', type=int, default=3, help='警告回数 (デフォルト3)')
    parser_random.add_argument('--min', type=int, default=60, help='最短間隔(秒)')
    parser_random.add_argument('--max', type=int, default=300, help='最長間隔(秒)')
    parser_random.add_argument('--desktop', action='store_true', help='デスクトップ通知も表示')
    parser_random.add_argument('--terminal', action='store_true', help='ターミナルにも表示')

    parser_list = subparsers.add_parser('list', help='利用可能な警告メッセージ一覧表示')

    args = parser.parse_args()

    if args.command == 'alert':
        desktop = args.desktop or not args.terminal
        terminal = args.terminal or not args.desktop
        alert_once(ALERT_MESSAGES, desktop=desktop, terminal=terminal)
    elif args.command == 'random':
        desktop = args.desktop or not args.terminal
        terminal = args.terminal or not args.desktop
        random_alert(
            ALERT_MESSAGES,
            desktop=desktop,
            terminal=terminal,
            min_interval=args.min,
            max_interval=args.max,
            repeat=args.repeat
        )
    elif args.command == 'list':
        list_messages(ALERT_MESSAGES)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
