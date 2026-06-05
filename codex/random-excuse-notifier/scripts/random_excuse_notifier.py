import sys
import os
import random
import argparse
import platform
import subprocess
from typing import List

EXCUSES = [
    "今日はネットが遅いみたいです。",
    "マウスが反応しませんでした。",
    "水星逆行中なので仕方ありません。",
    "上司のせいです。",
    "たぶん宇宙線の影響です。",
    "コーヒーをこぼしました。",
    "猫がキーボードを踏みました。",
    "システムの気分次第です。",
    "仕様です。",
    "今日は月曜日なので…",
    "サーバーが寝坊しています。",
    "AIが考え込んでいます。",
    "電波が弱いです。",
    "運勢が悪いです。",
    "今日はやる気が出ません。",
    "ファイルがどこかに行きました。",
    "隣の席のせいです。",
    "気圧の影響です。",
    "天気が悪いからです。",
    "たぶんバグじゃありません。"
]

def pick_excuse(history: List[str]) -> str:
    unused = [e for e in EXCUSES if e not in history]
    if not unused:
        return random.choice(EXCUSES)
    return random.choice(unused)

def send_notification(message: str):
    sys_platform = platform.system()
    try:
        if sys_platform == 'Darwin':
            # macOS: terminal-notifier or osascript
            if shutil.which('terminal-notifier'):
                subprocess.run([
                    'terminal-notifier',
                    '-title', '通知',
                    '-message', message
                ], check=False)
            else:
                script = f'display notification "{message}" with title "通知"'
                subprocess.run([
                    'osascript', '-e', script
                ], check=False)
        elif sys_platform == 'Linux':
            # Linux: notify-send
            if shutil.which('notify-send'):
                subprocess.run([
                    'notify-send', '通知', message], check=False)
            else:
                try:
                    import notify2
                    notify2.init('random-excuse-notifier')
                    n = notify2.Notification('通知', message)
                    n.show()
                except ImportError:
                    print(f'(通知) {message}')
        elif sys_platform == 'Windows':
            # Windows: Toast notification via win10toast
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast('通知', message, duration=3)
            except ImportError:
                print(f'(通知) {message}')
        else:
            print(f'(通知) {message}')
    except Exception as e:
        print(f'(通知) {message} (通知失敗: {e})')

def cli_log(args, history):
    excuse = pick_excuse(history)
    send_notification(excuse)
    print(f'(通知) {excuse}')
    history.append(excuse)
    if len(history) > 10:
        history.pop(0)

def cli_list(args, history):
    print('== 言い訳リスト ==')
    for idx, e in enumerate(EXCUSES, 1):
        print(f'{idx:2d}: {e}')

def cli_summary(args, history):
    print('== 最近の通知履歴 ==')
    if not history:
        print('履歴はありません。')
    else:
        for idx, e in enumerate(history, 1):
            print(f'{idx:2d}: {e}')

def parse_args():
    parser = argparse.ArgumentParser(description='random-excuse-notifier: ターミナル操作ごとに言い訳通知を表示')
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_log = subparsers.add_parser('log', help='ランダムな言い訳を通知表示')
    parser_list = subparsers.add_parser('list', help='言い訳リストを表示')
    parser_summary = subparsers.add_parser('summary', help='最近の通知履歴を表示')
    return parser.parse_args()

def main():
    import shutil
    history = []
    args = parse_args()
    if args.command == 'log':
        cli_log(args, history)
    elif args.command == 'list':
        cli_list(args, history)
    elif args.command == 'summary':
        cli_summary(args, history)
    else:
        print('不明なコマンドです。')

if __name__ == '__main__':
    main()
