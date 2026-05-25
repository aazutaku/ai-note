import os
import sys
import argparse
import subprocess
import shutil
from datetime import datetime

MOOD_ENV = 'MOOD'
DEFAULT_MOOD = '普通'
MOOD_MARKS = {
    '元気': '【元気】',
    'だるい': '【だるい】',
    'やる気MAX': '【やる気MAX】',
    '燃え尽き寸前': '【燃え尽き寸前】',
    '迷走中': '【迷走中】',
    '普通': '【普通】',
}

HISTORY_FILE = os.path.expanduser('~/.mood_history')


def get_current_mood():
    mood = os.environ.get(MOOD_ENV, DEFAULT_MOOD)
    return mood

def get_mood_mark(mood):
    return MOOD_MARKS.get(mood, f'【{mood}】')

def print_mood_banner(mood):
    mark = get_mood_mark(mood)
    print('=' * 28)
    print(f'今日の気分: {mood} {mark}')
    print('=' * 28)

def log_mood(mood):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
        f.write(f'{now}\t{mood}\n')

def list_history():
    if not os.path.exists(HISTORY_FILE):
        print('気分履歴はまだありません。')
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print('--- 気分履歴 ---')
    for line in lines[-20:]:
        print(line.strip())

def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print('気分履歴はまだありません。')
        return
    mood_count = {}
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                mood = parts[1]
                mood_count[mood] = mood_count.get(mood, 0) + 1
    print('--- 気分サマリー ---')
    for mood, count in sorted(mood_count.items(), key=lambda x: -x[1]):
        print(f'{mood}: {count}回')

def run_command_with_mood(command):
    mood = get_current_mood()
    print_mood_banner(mood)
    log_mood(mood)
    try:
        result = subprocess.run(command, shell=True, check=False)
        return result.returncode
    except Exception as e:
        print(f'コマンド実行エラー: {e}')
        return 1

def set_mood(mood):
    print(f'現在の気分を「{mood}」に設定しました。')
    print('次回以降のコマンド実行時に反映されます。')
    log_mood(mood)

def parse_args():
    parser = argparse.ArgumentParser(description='Terminal Mood Indicator')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='コマンドを気分付きで実行')
    parser_run.add_argument('cmd', nargs=argparse.REMAINDER, help='実行するコマンド')

    parser_set = subparsers.add_parser('set', help='気分を設定')
    parser_set.add_argument('mood', help='設定する気分')

    parser_list = subparsers.add_parser('list', help='気分履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='気分サマリーを表示')

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'run':
        if not args.cmd:
            print('実行するコマンドを指定してください。')
            sys.exit(1)
        command = ' '.join(args.cmd)
        sys.exit(run_command_with_mood(command))
    elif args.command == 'set':
        set_mood(args.mood)
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary_history()
    else:
        # デフォルト動作: 現在の気分を表示
        mood = get_current_mood()
        print_mood_banner(mood)
        print('コマンド例:')
        print('  python terminal_mood_indicator.py run ls')
        print('  python terminal_mood_indicator.py set 迷走中')
        print('  python terminal_mood_indicator.py list')
        print('  python terminal_mood_indicator.py summary')

if __name__ == '__main__':
    main()
