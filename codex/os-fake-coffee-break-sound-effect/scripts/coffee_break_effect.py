import os
import sys
import random
import platform
import argparse
import subprocess
from pathlib import Path

NOTIFICATIONS = [
    "あなたの集中はカフェイン不足です。",
    "今こそ一服の時です。",
    "マシンも休みたい気分です。",
    "コーヒーブレイクを強制します。",
    "気分転換しませんか？",
    "一息つきましょう。",
    "カフェインチャージ推奨。",
    "脳がコーヒーを欲しています。",
    "謎のコーヒータイム発動。",
    "OSが休憩を要求しています。"
]

SOUND_FILES = [
    "coffee_pour.wav",
    "cup_place.wav",
    "coffee_steam.wav",
    "coffee_machine.wav"
]

SOUNDS_DIR = Path(__file__).parent / "sounds"


def pick_random_notification():
    return random.choice(NOTIFICATIONS)


def pick_random_sound():
    candidates = [SOUNDS_DIR / f for f in SOUND_FILES]
    existing = [str(f) for f in candidates if f.exists()]
    if not existing:
        return None
    return random.choice(existing)


def send_notification(message):
    system = platform.system()
    try:
        if system == "Linux":
            subprocess.run(["notify-send", message], check=True)
        elif system == "Darwin":
            script = f'display notification "{message}" with title "Coffee Break"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("Coffee Break", message, duration=5)
            except ImportError:
                print("[警告] win10toastが未インストールです。pip install win10toast を実行してください。")
        else:
            print(f"[通知] {message}")
    except Exception as e:
        print(f"[通知エラー] {e}")


def play_sound(sound_path):
    system = platform.system()
    try:
        if system == "Linux":
            subprocess.run(["aplay", sound_path], check=True)
        elif system == "Darwin":
            subprocess.run(["afplay", sound_path], check=True)
        elif system == "Windows":
            try:
                from playsound import playsound
                playsound(sound_path)
            except ImportError:
                print("[警告] playsoundが未インストールです。pip install playsound を実行してください。")
        else:
            print(f"[サウンド] {sound_path} を再生（疑似）")
    except Exception as e:
        print(f"[サウンドエラー] {e}")


def list_sounds():
    print("利用可能なサウンドファイル:")
    for f in SOUND_FILES:
        path = SOUNDS_DIR / f
        status = "OK" if path.exists() else "Not Found"
        print(f"- {f}: {status}")


def summary():
    print("os-fake-coffee-break-sound-effect Skill サマリー:")
    print(f"通知パターン数: {len(NOTIFICATIONS)}")
    print(f"サウンドファイル数: {len(SOUND_FILES)}")
    print(f"サウンドディレクトリ: {SOUNDS_DIR}")
    print(f"OS種別: {platform.system()}")


def main():
    parser = argparse.ArgumentParser(description="OS風フェイクコーヒーブレイク演出スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="コーヒーブレイク演出を発動")
    parser_run.add_argument("--message", type=str, help="通知文言を指定（省略時はランダム）")
    parser_run.add_argument("--sound", type=str, help="サウンドファイル名を指定（省略時はランダム）")

    parser_list = subparsers.add_parser("list", help="利用可能なサウンドファイル一覧を表示")
    parser_summary = subparsers.add_parser("summary", help="Skillサマリーを表示")

    args = parser.parse_args()

    if args.command == "run":
        message = args.message if args.message else pick_random_notification()
        sound_path = None
        if args.sound:
            candidate = SOUNDS_DIR / args.sound
            if candidate.exists():
                sound_path = str(candidate)
            else:
                print(f"[警告] 指定サウンドファイルが見つかりません: {candidate}")
        else:
            sound_path = pick_random_sound()
        print(f"[通知] {message}")
        send_notification(message)
        if sound_path:
            print(f"[サウンド] {sound_path} を再生中...")
            play_sound(sound_path)
        else:
            print("[サウンド] サウンドファイルが見つかりませんでした。")
    elif args.command == "list":
        list_sounds()
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
