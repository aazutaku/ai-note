import sys
import argparse
import random
import time
import platform
import subprocess
from threading import Thread

# 通知メッセージ候補
ALERT_MESSAGES = [
    "重大: あなたのPCは3分後に強制的に昼寝モードへ移行します。",
    "警告: 集中力がOS基準値を下回りました。自動スリープを推奨します。",
    "注意: システム管理者の指示により、5分間の休憩モードが推奨されます。",
    "重要: 連続作業が検出されました。健康維持のため休憩を強く推奨します。",
    "警告: マウス/キーボード操作が一定時間ありません。自動スリープ準備中です。",
    "通知: OSアップデートのため仮想スリープモードに入る可能性があります。",
    "警告: あなたの作業速度がOS推奨値を下回っています。",
    "重大: 休憩未取得が検出されました。自動スリープまで残り2分。",
    "注意: システムがあなたの集中力低下を検知しました。",
    "警告: 作業効率が低下しています。自動スリープをおすすめします。"
]

# 通知タイトル候補
ALERT_TITLES = ["OS ALERT", "OS WARNING", "OS NOTICE", "OS MESSAGE"]

# OSごとの通知送信
def send_notification(title, message):
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "{title}"'
            ], check=True)
        elif os_name == "Linux":
            subprocess.run([
                "notify-send", title, message
            ], check=True)
        elif os_name == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=8)
            except ImportError:
                print(f"[{title}] {message}")
        else:
            print(f"[{title}] {message}")
    except Exception as e:
        print(f"[{title}] {message} (通知失敗: {e})")

# ランダムな通知を送信
def random_alert():
    title = random.choice(ALERT_TITLES)
    message = random.choice(ALERT_MESSAGES)
    send_notification(title, message)
    print(f"[{title}] {message}")

# ランダムな間隔で通知を送信するスレッド
def alert_loop(min_interval=600, max_interval=1800):
    while True:
        interval = random.randint(min_interval, max_interval)
        time.sleep(interval)
        random_alert()

# CLIサブコマンド: log, list, summary (ダミー実装)
def handle_log(args):
    print("[LOG] (ダミー) 通知ログ機能は未実装です。")

def handle_list(args):
    print("[LIST] (ダミー) 通知履歴一覧機能は未実装です。")

def handle_summary(args):
    print("[SUMMARY] (ダミー) 通知サマリー機能は未実装です。")

# メイン関数
def main():
    parser = argparse.ArgumentParser(description="OS風フェイクスリープモード通知スキル")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="即座に通知を表示")
    parser_alert.add_argument("--count", type=int, default=1, help="通知回数")

    parser_loop = subparsers.add_parser("loop", help="ランダム間隔で通知を繰り返す")
    parser_loop.add_argument("--min", type=int, default=600, help="最小間隔(秒)")
    parser_loop.add_argument("--max", type=int, default=1800, help="最大間隔(秒)")

    parser_log = subparsers.add_parser("log", help="通知ログを表示")
    parser_list = subparsers.add_parser("list", help="通知履歴一覧")
    parser_summary = subparsers.add_parser("summary", help="通知サマリー")

    args = parser.parse_args()

    if args.command == "alert":
        for _ in range(args.count):
            random_alert()
            time.sleep(2)
    elif args.command == "loop":
        print(f"[INFO] ランダム間隔({args.min}-{args.max}秒)で通知を送信します。Ctrl+Cで終了。")
        try:
            alert_loop(args.min, args.max)
        except KeyboardInterrupt:
            print("\n[INFO] 通知ループを終了します。")
    elif args.command == "log":
        handle_log(args)
    elif args.command == "list":
        handle_list(args)
    elif args.command == "summary":
        handle_summary(args)
    else:
        # デフォルト: すぐ1回通知
        random_alert()

if __name__ == '__main__':
    main()
