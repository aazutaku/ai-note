import os
import sys
import random
import time
import argparse
import platform
import subprocess
from pathlib import Path

EXCUSES = [
    'ネットが遅いから時間かかってます。',
    '今日は水星逆行中なのでうまくいきません。',
    'マウスが反応しませんでした。',
    '今日はキーボードが冷たくて指が動きません。',
    '月が綺麗ですね。',
    'パソコンが眠そうです。',
    'コーヒーが切れています。',
    '電磁波の影響かも。',
    '猫がキーボードを踏みました。',
    '今日は運気が悪いです。',
    'Wi-Fiの神様がご機嫌ななめです。',
    'エンターキーが重いです。',
    'CPUが考えごとをしています。',
    'OSがやる気を出していません。',
    '今日は満月なので不調です。',
    'ファイルがどこかに旅立ちました。',
    '更新ボタンを押し忘れました。',
    'システムが昼寝中です。',
    '気圧の影響です。',
    '今日は何もかもうまくいかない日です。'
]

HISTORY_PATH = Path.home() / '.random_excuse_history'
HISTORY_SIZE = 5


def get_last_excuses():
    if not HISTORY_PATH.exists():
        return []
    try:
        with open(HISTORY_PATH, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return [line.strip() for line in lines if line.strip()]
    except Exception:
        return []

def save_excuse_to_history(excuse):
    history = get_last_excuses()
    history.append(excuse)
    if len(history) > HISTORY_SIZE:
        history = history[-HISTORY_SIZE:]
    try:
        with open(HISTORY_PATH, 'w', encoding='utf-8') as f:
            for line in history:
                f.write(line + '\n')
    except Exception:
        pass

def pick_random_excuse():
    history = set(get_last_excuses())
    candidates = [e for e in EXCUSES if e not in history]
    if not candidates:
        candidates = EXCUSES
    return random.choice(candidates)

def notify(excuse):
    system = platform.system()
    if system == 'Linux':
        try:
            subprocess.run(['notify-send', excuse], check=True)
        except Exception:
            print(f'[通知] {excuse}')
    elif system == 'Darwin':
        script = f'display notification "{excuse}" with title "通知"'
        try:
            subprocess.run(['osascript', '-e', script], check=True)
        except Exception:
            print(f'[通知] {excuse}')
    elif system == 'Windows':
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast('通知', excuse, duration=5)
        except ImportError:
            print(f'[通知] {excuse} (win10toast未インストール)')
        except Exception:
            print(f'[通知] {excuse}')
    else:
        print(f'[通知] {excuse}')

def list_excuses():
    print('--- 言い訳リスト ---')
    for i, e in enumerate(EXCUSES, 1):
        print(f'{i:2d}: {e}')

def show_history():
    print('--- 最近の通知履歴 ---')
    history = get_last_excuses()
    if not history:
        print('履歴はありません。')
    else:
        for i, e in enumerate(history, 1):
            print(f'{i:2d}: {e}')

def main():
    parser = argparse.ArgumentParser(description='ランダム言い訳通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_notify = subparsers.add_parser('notify', help='言い訳をランダム通知')
    parser_list = subparsers.add_parser('list', help='言い訳一覧を表示')
    parser_history = subparsers.add_parser('history', help='最近の通知履歴を表示')
    parser_batch = subparsers.add_parser('batch', help='複数回ランダム通知')
    parser_batch.add_argument('-n', '--number', type=int, default=3, help='通知回数')
    args = parser.parse_args()

    if args.command == 'notify' or args.command is None:
        excuse = pick_random_excuse()
        notify(excuse)
        save_excuse_to_history(excuse)
    elif args.command == 'list':
        list_excuses()
    elif args.command == 'history':
        show_history()
    elif args.command == 'batch':
        for _ in range(args.number):
            excuse = pick_random_excuse()
            notify(excuse)
            save_excuse_to_history(excuse)
            time.sleep(1)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
