import sys
import argparse
import random
import time
import platform
import subprocess
from datetime import datetime, timedelta
import os

LOW_GRAVITY_MESSAGES = [
    "警告：本日このPCは低重力モードに切り替わりました。",
    "コードのバグがふわふわ浮遊中。捕まえてください！",
    "ファイルのドラッグ操作が普段の3倍遠く飛びます。",
    "OSの重力制御装置が一時的にオフラインです。",
    "ターミナルの出力が無重力で流れます。",
    "本日限定：重力ゼロで思考もフワフワ。",
    "ウィンドウの移動が宇宙遊泳モードになりました。",
    "キーボード入力がふんわり浮いています。",
    "重力異常：全てのバグが高くジャンプしています。",
    "警告：マウスカーソルが低重力で滑走中。",
    "OSの重力エンジンが再起動されました。",
    "この通知も無重力で表示されています。",
    "低重力アラート：集中力が宇宙へ飛び立ちました。",
    "ファイル保存時にふわっと浮き上がる可能性があります。",
    "重力低下：全てのプロセスが軽やかに実行中。"
]

LAST_ALERT_FILE = os.path.expanduser("~/.low_gravity_alert_last")
ALERT_INTERVAL_MINUTES = 60


def can_show_alert():
    """Check if enough time has passed since last alert."""
    if not os.path.exists(LAST_ALERT_FILE):
        return True
    try:
        with open(LAST_ALERT_FILE, 'r') as f:
            last_time_str = f.read().strip()
            last_time = datetime.strptime(last_time_str, "%Y-%m-%d %H:%M:%S")
        now = datetime.now()
        if now - last_time >= timedelta(minutes=ALERT_INTERVAL_MINUTES):
            return True
        else:
            return False
    except Exception:
        return True


def update_last_alert_time():
    with open(LAST_ALERT_FILE, 'w') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def pick_random_message():
    return random.choice(LOW_GRAVITY_MESSAGES)


def show_notification(message):
    system = platform.system()
    if system == 'Darwin':  # macOS
        try:
            subprocess.run([
                'osascript', '-e', f'display notification "{message}" with title "低重力アラート"'
            ], check=True)
        except Exception:
            print(f"[低重力アラート] {message}")
    elif system == 'Linux':
        try:
            subprocess.run([
                'notify-send', '低重力アラート', message
            ], check=True)
        except Exception:
            print(f"[低重力アラート] {message}")
    elif system == 'Windows':
        try:
            import ctypes
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("低重力アラート", message, duration=7)
        except Exception:
            print(f"[低重力アラート] {message}")
    else:
        print(f"[低重力アラート] {message}")


def log_alert(message):
    log_file = os.path.expanduser("~/.low_gravity_alert_log")
    with open(log_file, 'a') as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {message}\n")


def list_alert_log():
    log_file = os.path.expanduser("~/.low_gravity_alert_log")
    if not os.path.exists(log_file):
        print("No alert log found.")
        return
    with open(log_file, 'r') as f:
        print(f.read())


def summary_alert_log():
    log_file = os.path.expanduser("~/.low_gravity_alert_log")
    if not os.path.exists(log_file):
        print("No alert log found.")
        return
    counts = {}
    with open(log_file, 'r') as f:
        for line in f:
            msg = line.strip().split(' ', 1)[1] if ' ' in line else line.strip()
            counts[msg] = counts.get(msg, 0) + 1
    print("=== 低重力アラート出現回数集計 ===")
    for msg, count in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{msg}: {count}回")


def main():
    parser = argparse.ArgumentParser(description='低重力モード突入通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='最新の低重力アラートを発生させる')
    parser_list = subparsers.add_parser('list', help='過去の低重力アラート履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='アラート内容の出現回数を集計')
    parser_force = subparsers.add_parser('force', help='間隔を無視して強制的にアラート発生')

    args = parser.parse_args()

    if args.command == 'list':
        list_alert_log()
        return
    elif args.command == 'summary':
        summary_alert_log()
        return
    elif args.command == 'force':
        message = pick_random_message()
        show_notification(message)
        log_alert(message)
        update_last_alert_time()
        return
    else:
        # default: log (or no subcommand)
        if can_show_alert():
            message = pick_random_message()
            show_notification(message)
            log_alert(message)
            update_last_alert_time()
        else:
            print(f"[低重力アラート] まだアラート間隔({ALERT_INTERVAL_MINUTES}分)に達していません。--forceで強制実行できます。")

if __name__ == '__main__':
    main()
