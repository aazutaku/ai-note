import sys
import os
import time
import random
import argparse
import platform
import subprocess
from threading import Thread

KARAOKE_MESSAGES = [
    '本日は“残業パラダイス”を熱唱してください',
    '推奨曲：バグ退治ブルース',
    '歌唱力がアップデートされました。再起動は不要です',
    'OSよりお知らせ：本日のカラオケ推奨タイムが始まりました',
    '現実逃避モードON！カラオケでリフレッシュしましょう',
    '推奨アクション：エアマイクで熱唱してください',
    '本日の新機能：カラオケ推奨通知',
    '歌詞データベースが最新になりました',
    'OSカラオケAIがあなたの歌唱力を評価します',
    '推奨ジャンル：昭和歌謡 or アニソン'
]

KEYWORDS = [
    'カラオケ', '休憩', '疲れた', '歌', '現実逃避', '退屈', '集中', '眠い', '息抜き', 'ストレス'
]

MIN_INTERVAL = 600    # 最小10分
MAX_INTERVAL = 3600   # 最大1時間


def send_notification(message):
    system = platform.system()
    try:
        if system == 'Darwin':
            # macOS
            subprocess.run([
                'osascript', '-e',
                f'display notification "{message}" with title "Karaoke Alert"'
            ], check=True)
        elif system == 'Linux':
            # Linux
            subprocess.run([
                'notify-send', 'Karaoke Alert', message
            ], check=True)
        elif system == 'Windows':
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast('Karaoke Alert', message, duration=8)
            except ImportError:
                # Fallback to plyer
                from plyer import notification
                notification.notify(title='Karaoke Alert', message=message, timeout=8)
        else:
            print(f'[通知] {message}')
    except Exception as e:
        print(f'[通知] {message} (通知API失敗: {e})')


def random_interval():
    return random.randint(MIN_INTERVAL, MAX_INTERVAL)


def pick_random_message():
    return random.choice(KARAOKE_MESSAGES)


def monitor_keywords(stdin_stream, callback):
    """標準入力からキーワードを検知したらcallbackを呼ぶ"""
    while True:
        try:
            line = stdin_stream.readline()
            if not line:
                time.sleep(1)
                continue
            lower = line.strip().lower()
            for kw in KEYWORDS:
                if kw in lower:
                    callback()
                    break
        except Exception:
            time.sleep(2)


def random_alert_loop():
    while True:
        interval = random_interval()
        time.sleep(interval)
        msg = pick_random_message()
        send_notification(msg)


def keyword_triggered_alert():
    msg = pick_random_message()
    send_notification(msg)


def main():
    parser = argparse.ArgumentParser(description='Random OS Karaoke Alert Skill')
    parser.add_argument('--test', action='store_true', help='テスト通知を即時表示')
    parser.add_argument('--once', action='store_true', help='1回だけ通知して終了')
    parser.add_argument('--no-keyword', action='store_true', help='標準入力監視を無効化')
    args = parser.parse_args()

    if args.test:
        msg = pick_random_message()
        send_notification(msg)
        sys.exit(0)

    if args.once:
        msg = pick_random_message()
        send_notification(msg)
        sys.exit(0)

    # 標準入力監視スレッド
    if not args.no_keyword:
        t = Thread(target=monitor_keywords, args=(sys.stdin, keyword_triggered_alert), daemon=True)
        t.start()

    # メインループ
    try:
        random_alert_loop()
    except KeyboardInterrupt:
        print('終了します')

if __name__ == '__main__':
    main()
