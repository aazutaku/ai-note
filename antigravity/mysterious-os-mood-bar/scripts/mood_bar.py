import sys
import os
import argparse
import random
import subprocess
import platform
import time
from typing import Tuple

MOOD_WORDS = [
    'やる気-3度', '情熱沸騰中', '気分:無風', '低気圧注意報', '本日:曇り',
    'やる気指数:0度', '気分:快晴', '本日の気分:37.2度', 'テンション:低め', 'テンション:爆発寸前',
    'やる気:微熱', 'やる気:氷点下', '気分:逆噴射', '情熱:空回り', 'やる気:微増', '気分:謎'
]

STATUS_BAR_MESSAGE = ''


def get_git_status_mood() -> str:
    try:
        out = subprocess.check_output(['git', 'status'], stderr=subprocess.DEVNULL).decode('utf-8')
        if 'nothing to commit' in out:
            return random.choice(['やる気-3度', '気分:無風', '本日:曇り'])
        elif 'Untracked files' in out:
            return random.choice(['情熱沸騰中', 'テンション:爆発寸前'])
        elif 'Changes not staged' in out:
            return random.choice(['やる気:微熱', '気分:逆噴射'])
        else:
            return random.choice(MOOD_WORDS)
    except Exception:
        return random.choice(MOOD_WORDS)


def calc_mood_from_command(cmd: str) -> str:
    length = len(cmd)
    if length < 10:
        return random.choice(['やる気指数:0度', '気分:無風'])
    elif length < 30:
        return random.choice(['やる気:微増', '気分:快晴', 'やる気:微熱'])
    else:
        return random.choice(['テンション:爆発寸前', '情熱:空回り', 'やる気:氷点下'])


def generate_mood_message(cmd: str) -> str:
    mood = calc_mood_from_command(cmd)
    # git status っぽい雰囲気があれば追加
    if 'git status' in cmd:
        mood2 = get_git_status_mood()
        return f'[{mood} {mood2}]'
    else:
        return f'[{mood} 本日: {random.choice(MOOD_WORDS)}]'


def set_status_bar(message: str):
    system = platform.system()
    if system == 'Darwin':
        # macOS の場合はosascriptでメニューバーに通知
        script = f'display notification "{message}" with title "Mood Bar"'
        subprocess.run(['osascript', '-e', script])
    elif system == 'Linux':
        # Linuxはnotify-sendで通知、またはAppIndicator
        try:
            subprocess.run(['notify-send', 'Mood Bar', message])
        except Exception:
            pass
    else:
        print(f'[Mood Bar] {message}')


def log_command_and_mood(cmd: str, mood: str):
    # ローカル保存はしない（要件通り）
    pass


def handle_run(args):
    cmd = ' '.join(args.command)
    mood_message = generate_mood_message(cmd)
    set_status_bar(mood_message)
    print(mood_message)


def handle_demo(args):
    # デモ用: いくつかのコマンドでランダムに表示
    demo_cmds = [
        'ls -la',
        'git status',
        'echo hello',
        'python script.py',
        'rm -rf /tmp/test',
        'cat mysterious.txt',
        'docker ps',
        'nano README.md'
    ]
    for cmd in demo_cmds:
        mood_message = generate_mood_message(cmd)
        set_status_bar(mood_message)
        print(f'$ {cmd}\n{mood_message}\n')
        time.sleep(1)


def main():
    parser = argparse.ArgumentParser(description='Mysterious OS Mood Bar')
    subparsers = parser.add_subparsers(dest='subcmd')

    run_parser = subparsers.add_parser('run', help='コマンド実行時に気分温度を表示')
    run_parser.add_argument('command', nargs=argparse.REMAINDER, help='実行したコマンド')

    demo_parser = subparsers.add_parser('demo', help='デモ表示（複数コマンドで気分温度を表示）')

    args = parser.parse_args()

    if args.subcmd == 'run':
        handle_run(args)
    elif args.subcmd == 'demo':
        handle_demo(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
