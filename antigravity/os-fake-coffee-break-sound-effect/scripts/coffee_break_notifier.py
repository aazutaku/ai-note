import os
import random
import sys
import time
from threading import Thread

try:
    from plyer import notification
except ImportError:
    print('plyerが必要です: pip install plyer')
    sys.exit(1)

try:
    from playsound import playsound
except ImportError:
    print('playsoundが必要です: pip install playsound')
    sys.exit(1)

SOUND_DIR = os.path.join(os.path.dirname(__file__), 'sounds')
SOUND_FILES = [
    'coffee_pour.wav',
    'cup_put.wav',
    'coffee_machine.wav',
    'sip.wav',
    'milk_froth.wav',
]

NOTIFY_MESSAGES = [
    'あなたの集中はカフェイン不足です',
    '今こそ一服の時',
    'マシンも休みたい気分',
    'コーヒーブレイクを推奨します',
    'OSがコーヒーを欲しています',
    '休憩しませんか？',
    '一息つきましょう',
    '謎のカフェインタイム',
    '集中の合間にリフレッシュ',
    'コーヒーの香りが漂っています',
]

LOG_FILE = os.path.join(os.path.dirname(__file__), 'coffee_break.log')


def notify_and_play():
    msg = random.choice(NOTIFY_MESSAGES)
    sound = random.choice(SOUND_FILES)
    sound_path = os.path.join(SOUND_DIR, sound)
    # 通知表示
    try:
        notification.notify(
            title='Coffee Break Time',
            message=msg,
            app_name='Fake Coffee Break',
            timeout=5
        )
    except Exception as e:
        print(f'[通知失敗] {e}')
    # サウンド再生
    try:
        playsound(sound_path, block=False)
    except Exception as e:
        print(f'[サウンド再生失敗] {e}')
    # ログ書き込み
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")}\t{msg}\t{sound}\n')
    print(f'[通知] {msg}')
    print(f'[サウンド再生] {sound_path}')


def list_log():
    if not os.path.exists(LOG_FILE):
        print('ログがありません')
        return
    with open(LOG_FILE, encoding='utf-8') as f:
        for line in f:
            print(line.strip())


def summary_log():
    if not os.path.exists(LOG_FILE):
        print('ログがありません')
        return
    count = 0
    msg_counter = {}
    sound_counter = {}
    with open(LOG_FILE, encoding='utf-8') as f:
        for line in f:
            count += 1
            parts = line.strip().split('\t')
            if len(parts) == 3:
                msg, sound = parts[1], parts[2]
                msg_counter[msg] = msg_counter.get(msg, 0) + 1
                sound_counter[sound] = sound_counter.get(sound, 0) + 1
    print(f'コーヒーブレイク発動回数: {count}')
    print('通知文言別発動数:')
    for k, v in sorted(msg_counter.items(), key=lambda x: -x[1]):
        print(f'  {k}: {v}')
    print('サウンド別発動数:')
    for k, v in sorted(sound_counter.items(), key=lambda x: -x[1]):
        print(f'  {k}: {v}')


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fake Coffee Break Notifier')
    subparsers = parser.add_subparsers(dest='command')
    parser_log = subparsers.add_parser('log', help='コーヒーブレイクを即時発動')
    parser_list = subparsers.add_parser('list', help='過去の発動ログを表示')
    parser_summary = subparsers.add_parser('summary', help='発動履歴のサマリーを表示')
    parser_auto = subparsers.add_parser('auto', help='一定間隔で自動発動')
    parser_auto.add_argument('--interval', type=int, default=1800, help='自動発動間隔(秒)')

    args = parser.parse_args()
    if args.command == 'log' or args.command is None:
        notify_and_play()
    elif args.command == 'list':
        list_log()
    elif args.command == 'summary':
        summary_log()
    elif args.command == 'auto':
        try:
            print(f'自動発動モード: {args.interval}秒ごとにコーヒーブレイク')
            while True:
                notify_and_play()
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print('自動発動を中断しました')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
