import sys
import os
import time
import random
import argparse
import platform
import subprocess
from datetime import datetime, timedelta

MESSAGES = [
    "[OS SYSTEM ALERT] 本日、あなたの集中力ゲージが限界に到達しました。コーヒーブレイクが自動発動されます。",
    "[OS NOTICE] 重要：OS推奨のリフレッシュタイム到来。今すぐ席を立ち、コーヒーを準備してください。",
    "[OS OFFICIAL] システム管理者より：あなたの作業効率を維持するため、強制的に5分間のコーヒーブレイクを開始します。",
    "[OS ALERT] 休憩プロトコル #42 発動中。理由：集中度が閾値を下回りました。",
    "[OS SYSTEM] 重大：自動休憩タイマーが作動しました。作業を一時中断してください。",
    "[OS WARNING] システム監査：定期的なリフレッシュが必要です。コーヒーブレイクを推奨します。",
    "[OS MESSAGE] ユーザーの生産性維持のため、OSが強制的な休憩を命じます。",
    "[OS NOTICE] あなたの作業時間が閾値を超えました。コーヒーブレイクを開始してください。",
    "[OS SYSTEM] 重要：OS健康維持プロトコルにより、今すぐコーヒーブレイクを取ってください。",
    "[OS ALERT] 休憩タイム：システムが自動的にリフレッシュを推奨しています。"
]

HISTORY_FILE = os.path.expanduser("~/.coffee_break_alert_history.log")


def log_event(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{timestamp}\t{message}\n")


def show_notification(message):
    system = platform.system()
    try:
        if system == "Darwin":  # macOS
            subprocess.call(["osascript", "-e", f'display notification "{message}" with title "Mystery Coffee Break"'])
        elif system == "Linux":
            subprocess.call(["notify-send", "Mystery Coffee Break", message])
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("Mystery Coffee Break", message, duration=10)
            except ImportError:
                print("[WARN] win10toastが見つかりません。pip install win10toast でインストールしてください。")
                print(message)
        else:
            print(message)
    except Exception as e:
        print(f"[ERROR] 通知の表示に失敗しました: {e}")
        print(message)


def random_coffee_break_alert():
    message = random.choice(MESSAGES)
    show_notification(message)
    log_event(message)
    print(message)


def list_history(limit=20):
    if not os.path.exists(HISTORY_FILE):
        print("履歴ファイルが存在しません。")
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines[-limit:]:
        print(line.strip())


def summary():
    if not os.path.exists(HISTORY_FILE):
        print("履歴ファイルが存在しません。")
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"通算通知回数: {len(lines)}")
    if lines:
        first = lines[0].split('\t')[0]
        last = lines[-1].split('\t')[0]
        print(f"初回通知: {first}")
        print(f"最終通知: {last}")


def random_wait(min_sec=30, max_sec=300):
    wait = random.randint(min_sec, max_sec)
    print(f"[INFO] {wait}秒後に謎通知を発動します...")
    time.sleep(wait)


def main():
    parser = argparse.ArgumentParser(description="謎のOS公式コーヒーブレイク通知スクリプト")
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='ランダムなコーヒーブレイク通知を即時発動')
    parser_wait = subparsers.add_parser('wait', help='ランダムなタイミングで通知を発動')
    parser_wait.add_argument('--min', type=int, default=30, help='最小待機秒数 (デフォルト:30)')
    parser_wait.add_argument('--max', type=int, default=300, help='最大待機秒数 (デフォルト:300)')
    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_list.add_argument('--limit', type=int, default=20, help='表示件数 (デフォルト:20)')
    parser_summary = subparsers.add_parser('summary', help='通知履歴のサマリを表示')

    args = parser.parse_args()

    if args.command == 'alert':
        random_coffee_break_alert()
    elif args.command == 'wait':
        random_wait(args.min, args.max)
        random_coffee_break_alert()
    elif args.command == 'list':
        list_history(args.limit)
    elif args.command == 'summary':
        summary()
    else:
        # デフォルトは即時ランダム通知
        random_coffee_break_alert()

if __name__ == '__main__':
    main()
