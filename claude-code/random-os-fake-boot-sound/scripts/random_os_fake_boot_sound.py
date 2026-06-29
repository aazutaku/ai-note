import os
import sys
import random
import argparse
import platform
from pathlib import Path

try:
    from playsound import playsound
    PLAYSOUND_AVAILABLE = True
except ImportError:
    PLAYSOUND_AVAILABLE = False

try:
    from pydub import AudioSegment
    from pydub.playback import play
    PYDUB_AVAILABLE = True
except ImportError:
    PYDUB_AVAILABLE = False

def find_sound_files(sound_dir):
    exts = ['.wav', '.mp3']
    files = []
    for entry in os.scandir(sound_dir):
        if entry.is_file() and entry.name.lower().endswith(tuple(exts)):
            files.append(entry.path)
    return files

def select_random_sound(files):
    if not files:
        return None
    return random.choice(files)

def play_sound(file_path):
    if PLAYSOUND_AVAILABLE:
        try:
            playsound(file_path)
            return True
        except Exception as e:
            print(f"[ERROR] playsound再生失敗: {e}")
    if PYDUB_AVAILABLE:
        try:
            audio = AudioSegment.from_file(file_path)
            play(audio)
            return True
        except Exception as e:
            print(f"[ERROR] pydub再生失敗: {e}")
    print("[ERROR] サウンド再生用のライブラリが見つかりません。'pip install playsound' または 'pip install pydub simpleaudio' を実行してください。")
    return False

def list_sounds(sound_dir):
    files = find_sound_files(sound_dir)
    print(f"[INFO] サウンド候補: {len(files)}件")
    for i, f in enumerate(files, 1):
        print(f"  {i}. {os.path.basename(f)}")

def summary(sound_dir):
    files = find_sound_files(sound_dir)
    print(f"[SUMMARY] サウンドディレクトリ: {sound_dir}")
    print(f"  ファイル数: {len(files)}")
    if files:
        print(f"  例: {os.path.basename(files[0])}")
    print(f"  対応拡張子: .wav, .mp3")
    print(f"  Pythonバージョン: {platform.python_version()}")
    print(f"  OS: {platform.system()} {platform.release()}")
    print(f"  再生ライブラリ: playsound={'OK' if PLAYSOUND_AVAILABLE else 'NG'}, pydub={'OK' if PYDUB_AVAILABLE else 'NG'}")

def main():
    parser = argparse.ArgumentParser(description="謎のOS起動音をランダム再生するスキル")
    parser.add_argument('command', nargs='?', default='play', choices=['play', 'list', 'summary'], help='play:再生, list:音源一覧, summary:概要')
    parser.add_argument('--sound-dir', default=str(Path(__file__).parent / 'sounds'), help='サウンドファイルのディレクトリ')
    args = parser.parse_args()

    sound_dir = args.sound_dir
    if not os.path.isdir(sound_dir):
        print(f"[ERROR] サウンドディレクトリが見つかりません: {sound_dir}")
        sys.exit(1)

    files = find_sound_files(sound_dir)
    if args.command == 'list':
        list_sounds(sound_dir)
        return
    elif args.command == 'summary':
        summary(sound_dir)
        return
    elif args.command == 'play':
        print(f"[INFO] サウンド候補: {len(files)}件")
        if not files:
            print(f"[ERROR] サウンドファイル(.wav/.mp3)が見つかりません。{sound_dir} に配置してください。")
            sys.exit(1)
        selected = select_random_sound(files)
        print(f"[INFO] 選択: {os.path.basename(selected)}")
        print(f"[PLAY] 再生中...")
        play_sound(selected)
    else:
        print(f"[ERROR] 未知のコマンド: {args.command}")
        sys.exit(1)

if __name__ == '__main__':
    main()
