import os
import sys
import random
import argparse
import platform
import subprocess
from pathlib import Path

SOUND_LIST = [
    {
        'filename': 'file_departure.wav',
        'label': 'ファイルが旅立つ音'
    },
    {
        'filename': 'motivation_boot.wav',
        'label': 'シュールなやる気起動音'
    },
    {
        'filename': 'system_applause.wav',
        'label': '謎のシステム自動拍手'
    },
    {
        'filename': 'mysterious_notification.wav',
        'label': '謎の通知音'
    },
    {
        'filename': 'os_beep.wav',
        'label': 'OSビープ音'
    }
]

SOUND_DIR = Path(__file__).parent / 'sounds'


def list_sounds():
    print("利用可能なサウンド一覧:")
    for idx, sound in enumerate(SOUND_LIST):
        print(f"{idx + 1}. {sound['label']} ({sound['filename']})")


def play_sound(sound_path):
    system = platform.system()
    try:
        if system == 'Windows':
            import winsound
            winsound.PlaySound(str(sound_path), winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif system == 'Darwin':
            subprocess.run(['afplay', str(sound_path)], check=True)
        elif system == 'Linux':
            # Try aplay, paplay, or cvlc
            if shutil.which('aplay'):
                subprocess.run(['aplay', str(sound_path)], check=True)
            elif shutil.which('paplay'):
                subprocess.run(['paplay', str(sound_path)], check=True)
            elif shutil.which('cvlc'):
                subprocess.run(['cvlc', '--play-and-exit', str(sound_path)], check=True)
            else:
                print('サウンド再生コマンドが見つかりません (aplay/paplay/cvlc)')
        else:
            print(f'未対応OS: {system}')
    except Exception as e:
        print(f'サウンド再生エラー: {e}')


def random_sound():
    sound = random.choice(SOUND_LIST)
    sound_path = SOUND_DIR / sound['filename']
    if not sound_path.exists():
        print(f"サウンドファイルが見つかりません: {sound_path}")
        return None, None
    play_sound(sound_path)
    return sound['label'], sound['filename']


def log_event(event, sound_label):
    log_path = Path(__file__).parent / 'sound_effect.log'
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"{event}\t{sound_label}\n")


def list_log():
    log_path = Path(__file__).parent / 'sound_effect.log'
    if not log_path.exists():
        print('ログがありません')
        return
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


def summary_log():
    log_path = Path(__file__).parent / 'sound_effect.log'
    if not log_path.exists():
        print('ログがありません')
        return
    counter = {}
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                label = parts[1]
                counter[label] = counter.get(label, 0) + 1
    print('サウンド別再生回数:')
    for label, count in counter.items():
        print(f'{label}: {count}回')


def main():
    parser = argparse.ArgumentParser(description='Random OS Mystery Sound Effect Skill')
    subparsers = parser.add_subparsers(dest='command')

    parser_play = subparsers.add_parser('play', help='ランダムな謎サウンドを再生')
    parser_play.add_argument('--event', type=str, default='manual', help='発生イベント名')

    parser_list = subparsers.add_parser('list', help='利用可能なサウンド一覧')
    parser_log = subparsers.add_parser('log', help='サウンド再生ログを表示')
    parser_summary = subparsers.add_parser('summary', help='サウンド再生回数サマリ')

    args = parser.parse_args()

    if args.command == 'play':
        label, filename = random_sound()
        if label:
            print(f'[system] {label}が再生されました。')
            log_event(args.event, label)
    elif args.command == 'list':
        list_sounds()
    elif args.command == 'log':
        list_log()
    elif args.command == 'summary':
        summary_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    import shutil
    main()
