import os
import sys
import random
import argparse
import time

try:
    from playsound import playsound
except ImportError:
    print('[ERROR] playsound モジュールが見つかりません。\nインストール: pip install playsound')
    sys.exit(1)

SOUNDS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sounds')
SUPPORTED_EXTENSIONS = ('.wav', '.mp3')


def find_sound_files():
    if not os.path.exists(SOUNDS_DIR):
        print(f'[ERROR] サウンドディレクトリが存在しません: {SOUNDS_DIR}')
        return []
    files = [f for f in os.listdir(SOUNDS_DIR)
             if f.lower().endswith(SUPPORTED_EXTENSIONS) and os.path.isfile(os.path.join(SOUNDS_DIR, f))]
    return files


def select_random_sound(files):
    if not files:
        return None
    return random.choice(files)


def play_sound(filename):
    filepath = os.path.join(SOUNDS_DIR, filename)
    try:
        print(f'[PLAY] Now playing: {filename}')
        playsound(filepath)
        print('[OK] Boot sound playback finished.')
    except Exception as e:
        print(f'[ERROR] サウンド再生に失敗しました: {e}')


def list_sounds(files):
    if not files:
        print('[INFO] サウンドファイルが見つかりません。')
        return
    print('[INFO] 利用可能なサウンドファイル:')
    for f in files:
        print(f'  - {f}')


def summary(files):
    print('--- random-os-fake-boot-sound summary ---')
    print(f'サウンドディレクトリ: {SOUNDS_DIR}')
    print(f'ファイル数: {len(files)}')
    if files:
        print('ファイル一覧:')
        for f in files:
            print(f'  - {f}')
    else:
        print('（サウンドファイルがありません）')


def main():
    parser = argparse.ArgumentParser(description='random-os-fake-boot-sound: 起動時に毎回ランダムなサウンドを再生するスクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='ランダムなサウンドを再生')
    parser_list = subparsers.add_parser('list', help='利用可能なサウンドファイル一覧を表示')
    parser_summary = subparsers.add_parser('summary', help='サウンドディレクトリの概要を表示')
    parser_test = subparsers.add_parser('test', help='すべてのサウンドを順番に再生（テスト用）')

    args = parser.parse_args()
    files = find_sound_files()

    if args.command == 'log' or args.command is None:
        print(f'[INFO] Boot sound files found: {len(files)}')
        if not files:
            print('[WARN] サウンドファイルがありません。sounds/ フォルダにwav/mp3を追加してください。')
            sys.exit(1)
        selected = select_random_sound(files)
        print(f'[INFO] Selected: {selected}')
        play_sound(selected)
    elif args.command == 'list':
        list_sounds(files)
    elif args.command == 'summary':
        summary(files)
    elif args.command == 'test':
        if not files:
            print('[WARN] サウンドファイルがありません。')
            sys.exit(1)
        for f in files:
            print(f'--- 再生: {f} ---')
            play_sound(f)
            time.sleep(0.5)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
