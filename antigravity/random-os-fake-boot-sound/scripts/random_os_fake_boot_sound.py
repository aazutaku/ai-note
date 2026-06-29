import os
import sys
import random
import argparse
import glob
import platform
from typing import List

try:
    from playsound import playsound
except ImportError:
    print('[ERROR] playsoundライブラリが見つかりません。\n  pip install playsound を実行してください。')
    sys.exit(1)

def find_sound_files(directory: str) -> List[str]:
    patterns = ['*.wav', '*.mp3']
    files = []
    for pattern in patterns:
        files.extend(glob.glob(os.path.join(directory, pattern)))
    return files

def play_random_sound(sound_dir: str, verbose: bool = True) -> str:
    files = find_sound_files(sound_dir)
    if not files:
        if verbose:
            print(f'[WARN] サウンドファイルが {sound_dir} に見つかりません。')
        return ''
    chosen = random.choice(files)
    if verbose:
        print(f'[INFO] {len(files)}個の音源を検出: {", ".join([os.path.basename(f) for f in files])}')
        print(f'[INFO] 今回の起動音: {os.path.basename(chosen)}')
    try:
        playsound(chosen)
        if verbose:
            print('[INFO] サウンド再生完了')
    except Exception as e:
        print(f'[ERROR] サウンド再生に失敗しました: {e}')
    return chosen

def list_sounds(sound_dir: str):
    files = find_sound_files(sound_dir)
    if not files:
        print('[INFO] サウンドファイルが見つかりません。')
        return
    print(f'[INFO] {len(files)}個の音源:')
    for f in files:
        print(f'  - {os.path.basename(f)}')

def summary(sound_dir: str):
    files = find_sound_files(sound_dir)
    print('=== random-os-fake-boot-sound summary ===')
    print(f'音源ディレクトリ: {sound_dir}')
    print(f'音源ファイル数: {len(files)}')
    for f in files:
        print(f'  - {os.path.basename(f)}')
    print('Pythonバージョン:', sys.version.replace('\n', ' '))
    print('OS:', platform.system(), platform.release())

def main():
    parser = argparse.ArgumentParser(description='random-os-fake-boot-sound: ランダムなOS起動音を再生するスクリプト')
    parser.add_argument('--sound-dir', type=str, default=os.path.join(os.path.dirname(__file__), 'sounds'),
                        help='音源ファイルのディレクトリ (デフォルト: ./sounds)')
    parser.add_argument('command', nargs='?', default='play', choices=['play', 'list', 'summary'],
                        help='play: ランダム再生, list: 音源一覧, summary: 環境サマリ')
    parser.add_argument('--quiet', action='store_true', help='詳細ログを非表示')
    args = parser.parse_args()

    if args.command == 'play':
        play_random_sound(args.sound_dir, verbose=not args.quiet)
    elif args.command == 'list':
        list_sounds(args.sound_dir)
    elif args.command == 'summary':
        summary(args.sound_dir)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
