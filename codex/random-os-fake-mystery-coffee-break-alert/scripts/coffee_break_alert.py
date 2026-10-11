import argparse
import random
import sys
import os
import platform
import subprocess
import time
from datetime import datetime

ALERT_MESSAGES = [
    "本日、あなたの集中力ゲージが限界に到達しました。コーヒーブレイクが自動発動されます。",
    "重要：OS推奨のリフレッシュタイム到来。5分間の休憩を強く推奨します。",
    "セキュリティポリシーにより、今すぐコーヒーまたはお茶を準備してください。",
    "システムが“疲労蓄積”を検知。直ちにブレイクゾーンへ移動せよ。",
    "新しい集中力パッチ適用には休憩が必要です。ご協力をお願いします。",
    "[OS SYSTEM] あなたの作業効率が閾値を下回りました。自動休憩モードへ移行します。",
    "[OS ALERT] ブレインリフレッシュ推奨：今すぐコーヒーを淹れましょう。",
    "[OS NOTICE] 長時間作業を検知。OS公式のコーヒーブレイクをお楽しみください。",
    "[OS WARNING] 休憩未取得によるパフォーマンス低下を検出。リフレッシュを強制します。",
    "[OS UPDATE] システム安定化のため、5分間のブレイクタイムを発動します。"
]

LOG_FILE = os.path.expanduser("~/.coffee_break_alert.log")


def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def send_desktop_notification(title, message):
    system = platform.system()
    try:
        if system == "Darwin":
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            subprocess.run(["notify-send", title, message], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=8)
            except ImportError:
                print("[WARN] win10toastが見つかりません。ターミナルにのみ通知します。")
                print(f"[{title}] {message}")
        else:
            print(f"[{title}] {message}")
    except Exception as e:
        print(f"[ERROR] 通知送信失敗: {e}\n[{title}] {message}")


def random_alert():
    message = random.choice(ALERT_MESSAGES)
    title = "OS ALERT"
    send_desktop_notification(title, message)
    print(f"[{title}] {message}")
    log_alert(message)


def list_logs():
    if not os.path.exists(LOG_FILE):
        print("ログファイルが存在しません。")
        return
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = f.readlines()
    for line in logs[-20:]:
        print(line.strip())


def summary_logs():
    if not os.path.exists(LOG_FILE):
        print("ログファイルが存在しません。")
        return
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = f.readlines()
    print(f"合計通知回数: {len(logs)}")
    if logs:
        print(f"最初の通知: {logs[0].strip()}")
        print(f"最新の通知: {logs[-1].strip()}")


def auto_mode(interval_min=45, random_jitter=10):
    print(f"自動モード開始: {interval_min}分ごとにランダム通知 (±{random_jitter}分)\nCtrl+Cで終了")
    try:
        while True:
            random_alert()
            jitter = random.randint(-random_jitter, random_jitter)
            sleep_time = max(60, (interval_min + jitter) * 60)
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("\n自動モードを終了しました。")


def main():
    parser = argparse.ArgumentParser(description="謎のOS公式・強制コーヒーブレイク通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="今すぐランダムなコーヒーブレイク通知を発動")
    parser_auto = subparsers.add_parser("auto", help="定期的に自動で通知するモード")
    parser_auto.add_argument("--interval", type=int, default=45, help="通知間隔(分)")
    parser_auto.add_argument("--jitter", type=int, default=10, help="ランダムゆらぎ(分)")
    parser_list = subparsers.add_parser("list", help="最近の通知ログを表示")
    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリーを表示")

    args = parser.parse_args()

    if args.command == "alert" or args.command is None:
        random_alert()
    elif args.command == "auto":
        auto_mode(interval_min=args.interval, random_jitter=args.jitter)
    elif args.command == "list":
        list_logs()
    elif args.command == "summary":
        summary_logs()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
