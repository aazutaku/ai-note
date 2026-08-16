import os
import sys
import random
import platform
import subprocess
import argparse
from pathlib import Path

SOUNDS_DIR = Path(__file__).parent / 'sounds'
SOUND_FILES = [
    'file_departure.wav',
    'motivation_boot.wav',
    'system_applause.wav',
    'mystery_effect1.wav',
    'mystery_effect2.wav',
    'weird_beep.wav',
    'unknown_notification.wav',
    'strange_popup.wav',
    'enigmatic_chime.wav',
    'cryptic_alert.wav',
]

# --- サウンド再生ヘルパー ---
def play_sound(sound_path):
    system = platform.system()
    try:
        if system == 'Darwin':
            # macOS
            subprocess.run(['afplay', str(sound_path)], check=True)
        elif system == 'Linux':
            subprocess.run(['aplay', str(sound_path)], check=True)
        elif system == 'Windows':
            import winsound
            winsound.PlaySound(str(sound_path), winsound.SND_FILENAME)
        else:
            print(f"[WARN] サウンド再生は未対応OSです: {system}")
    except Exception as e:
        print(f"[ERROR] サウンド再生失敗: {e}")

# --- サウンドファイルの存在チェック ---
def ensure_sound_files():
    missing = []
    for fname in SOUND_FILES:
        fpath = SOUNDS_DIR / fname
        if not fpath.exists():
            missing.append(fname)
    if missing:
        print("[WARN] 以下のサウンドファイルが見つかりません:")
        for m in missing:
            print(f"  - {m}")
        print(f"サウンドディレクトリ: {SOUNDS_DIR}")

# --- ランダム再生コア ---
def random_play():
    ensure_sound_files()
    available = [f for f in SOUND_FILES if (SOUNDS_DIR / f).exists()]
    if not available:
        print("[ERROR] 有効なサウンドファイルがありません。sounds/ ディレクトリを確認してください。")
        return
    sound = random.choice(available)
    sound_path = SOUNDS_DIR / sound
    print(f"[SE] {sound.replace('_', ' ').replace('.wav','')} を再生中...")
    play_sound(sound_path)

# --- サウンド一覧表示 ---
def list_sounds():
    print("利用可能なサウンドファイル:")
    for fname in SOUND_FILES:
        fpath = SOUNDS_DIR / fname
        status = "OK" if fpath.exists() else "Not found"
        print(f" - {fname} [{status}]")

# --- Skill概要表示 ---
def show_summary():
    print("random-os-mystery-sound-effect Skill")
    print("コマンド実行時にランダムな謎のOSサウンドエフェクトを再生します。")
    print(f"サウンドディレクトリ: {SOUNDS_DIR}")
    print(f"登録サウンド数: {len(SOUND_FILES)}")

# --- コマンドライン引数 ---
def main():
    parser = argparse.ArgumentParser(description='ランダムOS謎サウンドエフェクト Skill')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('play', help='ランダムでサウンドを再生')
    subparsers.add_parser('list', help='利用可能なサウンド一覧')
    subparsers.add_parser('summary', help='Skill概要表示')

    args = parser.parse_args()
    if args.command == 'play' or args.command is None:
        random_play()
    elif args.command == 'list':
        list_sounds()
    elif args.command == 'summary':
        show_summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
