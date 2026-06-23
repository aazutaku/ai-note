import os
import sys
import random
import time
import argparse
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

CONSPIRACY_MESSAGES = [
    ("緊急陰謀論アラート", "コードレビューは宇宙人の監視下にあります。"),
    ("謎の波動警告", "Wi-Fiの波動が干渉しています。至急アルミホイルを準備してください。"),
    ("バグ覚醒予告", "本日15時、全てのバグが覚醒します。備えよ。"),
    ("量子干渉検知", "あなたのマウス操作が量子レベルで観測されています。"),
    ("新世界秩序発動", "このリポジトリは新世界秩序の一部です。"),
    ("監視社会速報", "あなたのコミットは全て記録されています。"),
    ("時空間バグ警報", "このバグは時空を超えて再発します。"),
    ("AI陰謀論", "AIは既に全てを知っています。"),
    ("シンタックス異常検知", "このエラーは陰謀の一端です。"),
    ("秘密結社からの警告", "本日、秘密結社がコードを監査します。")
]

LAST_ALERT_FILE = Path.home() / ".random_conspiracy_last_alert"
ALERT_INTERVAL_MINUTES = 60


def can_show_alert():
    if not LAST_ALERT_FILE.exists():
        return True
    try:
        with open(LAST_ALERT_FILE, 'r') as f:
            last_time_str = f.read().strip()
            last_time = datetime.fromisoformat(last_time_str)
            if datetime.now() - last_time > timedelta(minutes=ALERT_INTERVAL_MINUTES):
                return True
    except Exception:
        return True
    return False


def update_last_alert_time():
    with open(LAST_ALERT_FILE, 'w') as f:
        f.write(datetime.now().isoformat())


def send_notification(title, message):
    if sys.platform.startswith('linux'):
        try:
            subprocess.run([
                'notify-send', '--app-name=ConspiracyAlert', title, message
            ], check=True)
        except Exception as e:
            print(f"[Error] 通知送信に失敗: {e}")
    elif sys.platform == 'darwin':
        try:
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', script], check=True)
        except Exception as e:
            print(f"[Error] 通知送信に失敗: {e}")
    else:
        print(f"[通知] {title}: {message}")


def select_random_message():
    return random.choice(CONSPIRACY_MESSAGES)


def log_alert(title, message):
    log_file = Path.home() / ".random_conspiracy_alert.log"
    with open(log_file, 'a') as f:
        f.write(f"{datetime.now().isoformat()} | {title} | {message}\n")


def show_alert():
    if not can_show_alert():
        return
    title, message = select_random_message()
    send_notification(title, message)
    log_alert(title, message)
    update_last_alert_time()


def list_alerts():
    log_file = Path.home() / ".random_conspiracy_alert.log"
    if not log_file.exists():
        print("アラート履歴はありません。")
        return
    with open(log_file, 'r') as f:
        for line in f:
            print(line.strip())


def summary_alerts():
    log_file = Path.home() / ".random_conspiracy_alert.log"
    if not log_file.exists():
        print("アラート履歴はありません。")
        return
    counts = {}
    with open(log_file, 'r') as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) >= 3:
                title = parts[1].strip()
                counts[title] = counts.get(title, 0) + 1
    print("アラート種別ごとの発生回数:")
    for title, count in counts.items():
        print(f"{title}: {count}回")


def main():
    parser = argparse.ArgumentParser(description='ランダム陰謀論デスクトップアラート')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('alert', help='今すぐ陰謀論アラートを表示')
    subparsers.add_parser('list', help='過去のアラート履歴を表示')
    subparsers.add_parser('summary', help='アラート種別ごとに回数を集計')

    args = parser.parse_args()
    if args.command == 'alert' or args.command is None:
        show_alert()
    elif args.command == 'list':
        list_alerts()
    elif args.command == 'summary':
        summary_alerts()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
