import random
import os
import sys
import argparse
import time
from threading import Thread

try:
    from playsound import playsound
except ImportError:
    print("playsoundパッケージが必要です。pip install playsound でインストールしてください。", file=sys.stderr)
    sys.exit(1)

try:
    from plyer import notification
except ImportError:
    print("plyerパッケージが必要です。pip install plyer でインストールしてください。", file=sys.stderr)
    sys.exit(1)

SOUND_DIR = os.path.join(os.path.dirname(__file__), 'sounds')
SOUND_FILES = [
    'coffee_pour.wav',
    'cup_put.wav',
    'coffee_machine.wav',
    'stirring_mug.wav',
    'espresso_shot.wav',
]

NOTIFY_MESSAGES = [
    "あなたの集中はカフェイン不足です",
    "今こそ一服の時",
    "マシンも休みたい気分",
    "コーヒーブレイクを推奨します",
    "脳内カフェイン残量が低下しています",
    "謎の休憩タイムが始まります",
    "一息入れてみませんか?",
    "コーヒーの香りでリフレッシュしましょう",
    "開発者にも休息が必要です",
    "OSからの強制休憩指示です"
]


def list_sounds():
    print("利用可能なサウンドファイル:")
    for f in SOUND_FILES:
        path = os.path.join(SOUND_DIR, f)
        exists = os.path.exists(path)
        print(f"- {f} {'(OK)' if exists else '(ファイル未発見)'}")

def list_messages():
    print("利用可能な通知文:")
    for m in NOTIFY_MESSAGES:
        print(f"- {m}")

def play_random_sound():
    available = [f for f in SOUND_FILES if os.path.exists(os.path.join(SOUND_DIR, f))]
    if not available:
        print("サウンドファイルが見つかりません。", file=sys.stderr)
        return
    sound_file = random.choice(available)
    sound_path = os.path.join(SOUND_DIR, sound_file)
    print(f"[サウンド] {sound_path} を再生中...")
    try:
        playsound(sound_path)
    except Exception as e:
        print(f"サウンド再生エラー: {e}", file=sys.stderr)

def show_random_notification():
    message = random.choice(NOTIFY_MESSAGES)
    print(f"[通知] {message}")
    try:
        notification.notify(
            title="コーヒーブレイク通知",
            message=message,
            app_name="FakeCoffeeBreak",
            timeout=5
        )
    except Exception as e:
        print(f"通知エラー: {e}", file=sys.stderr)

def coffee_break_once():
    show_random_notification()
    t = Thread(target=play_random_sound)
    t.start()
    t.join()

def coffee_break_loop(interval=1800, count=3):
    for i in range(count):
        coffee_break_once()
        if i < count - 1:
            print(f"次のコーヒーブレイクまで {interval} 秒待機...")
            time.sleep(interval)

def main():
    parser = argparse.ArgumentParser(description="OS風フェイク・コーヒーブレイクサウンド&通知スキル")
    subparsers = parser.add_subparsers(dest='command')

    parser_once = subparsers.add_parser('once', help='1回だけコーヒーブレイク演出')
    parser_loop = subparsers.add_parser('loop', help='定期的にコーヒーブレイク演出')
    parser_loop.add_argument('--interval', type=int, default=1800, help='繰り返し間隔(秒)')
    parser_loop.add_argument('--count', type=int, default=3, help='回数')
    parser_list = subparsers.add_parser('list', help='サウンドと通知文の一覧表示')
    parser_list.add_argument('--sounds', action='store_true', help='サウンドのみ')
    parser_list.add_argument('--messages', action='store_true', help='通知文のみ')

    args = parser.parse_args()
    if args.command == 'once' or args.command is None:
        coffee_break_once()
    elif args.command == 'loop':
        coffee_break_loop(interval=args.interval, count=args.count)
    elif args.command == 'list':
        if args.sounds:
            list_sounds()
        elif args.messages:
            list_messages()
        else:
            list_sounds()
            print("")
            list_messages()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
