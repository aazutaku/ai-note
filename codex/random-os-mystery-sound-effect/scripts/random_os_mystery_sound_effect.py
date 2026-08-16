import os
import sys
import random
import argparse
import tempfile
import shutil
import threading
import time
from pathlib import Path

try:
    from playsound import playsound
    PLAY_METHOD = 'playsound'
except ImportError:
    PLAY_METHOD = None

SOUND_FILES = [
    {
        'name': 'ファイルが旅立つ音',
        'filename': 'file_departure.wav',
        'url': 'https://cdn.ai-note.tech/os_se/file_departure.wav'
    },
    {
        'name': 'シュールなやる気起動音',
        'filename': 'motivation_boot.wav',
        'url': 'https://cdn.ai-note.tech/os_se/motivation_boot.wav'
    },
    {
        'name': '謎のシステム自動拍手',
        'filename': 'system_applause.wav',
        'url': 'https://cdn.ai-note.tech/os_se/system_applause.wav'
    },
    {
        'name': '未定義の通知音',
        'filename': 'undefined_notify.wav',
        'url': 'https://cdn.ai-note.tech/os_se/undefined_notify.wav'
    },
    {
        'name': 'エラーっぽい謎音',
        'filename': 'mystery_error.wav',
        'url': 'https://cdn.ai-note.tech/os_se/mystery_error.wav'
    }
]

TEMP_DIR = os.path.join(tempfile.gettempdir(), 'random_os_mystery_sound_effect')


def ensure_temp_dir():
    os.makedirs(TEMP_DIR, exist_ok=True)


def download_sound_files():
    import urllib.request
    ensure_temp_dir()
    for sound in SOUND_FILES:
        file_path = os.path.join(TEMP_DIR, sound['filename'])
        if not os.path.exists(file_path):
            try:
                print(f"[DL] {sound['name']} をダウンロード中...")
                urllib.request.urlretrieve(sound['url'], file_path)
            except Exception as e:
                print(f"[WARN] {sound['filename']} のダウンロードに失敗: {e}")


def cleanup_temp_dir():
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)


def get_random_sound():
    return random.choice(SOUND_FILES)


def play_sound(sound):
    file_path = os.path.join(TEMP_DIR, sound['filename'])
    if not os.path.exists(file_path):
        print(f"[ERR] サウンドファイルが見つかりません: {file_path}")
        return
    print(f"[SE] {sound['name']}を再生中...")
    if PLAY_METHOD == 'playsound':
        try:
            playsound(file_path, block=False)
        except Exception as e:
            print(f"[WARN] playsound失敗: {e}")
    else:
        # Fallback to OS native command
        if sys.platform.startswith('darwin'):
            os.system(f"afplay '{file_path}'&")
        elif sys.platform.startswith('linux'):
            os.system(f"aplay '{file_path}'&")
        elif sys.platform.startswith('win'):
            import winsound
            try:
                winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception as e:
                print(f"[WARN] winsound失敗: {e}")
        else:
            print("[WARN] サウンド再生方法が見つかりません")


def list_sounds():
    print("利用可能なサウンドエフェクト:")
    for idx, sound in enumerate(SOUND_FILES):
        print(f"  {idx+1}. {sound['name']} ({sound['filename']})")


def summary():
    print("random-os-mystery-sound-effect Skill 概要:")
    print("- コマンドやファイル操作のたびに、謎のOS公式サウンドエフェクトをランダム再生")
    print("- サウンドは一時ディレクトリに保存、Skill削除時に自動クリーンアップ")
    print("- playsound, afplay, aplay, winsound などで再生")


def log_event(event):
    log_path = os.path.join(TEMP_DIR, 'event.log')
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}\t{event}\n")


def show_log():
    log_path = os.path.join(TEMP_DIR, 'event.log')
    if not os.path.exists(log_path):
        print("ログがありません")
        return
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


def main():
    parser = argparse.ArgumentParser(description='random-os-mystery-sound-effect Skill')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('play', help='ランダムな謎SEを再生')
    subparsers.add_parser('list', help='利用可能なサウンド一覧')
    subparsers.add_parser('summary', help='Skill概要')
    subparsers.add_parser('log', help='イベントログ表示')
    subparsers.add_parser('cleanup', help='一時ファイル削除')

    args = parser.parse_args()

    if args.command == 'play' or args.command is None:
        download_sound_files()
        sound = get_random_sound()
        play_sound(sound)
        log_event(f"play:{sound['name']}")
    elif args.command == 'list':
        list_sounds()
    elif args.command == 'summary':
        summary()
    elif args.command == 'log':
        show_log()
    elif args.command == 'cleanup':
        cleanup_temp_dir()
        print("一時ファイルを削除しました")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
