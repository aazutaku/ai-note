import sys
import os
import random
import time
import argparse
import platform
from datetime import datetime
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

FAKE_ALERTS = [
    "重大：あなたのカフェイン血中濃度が“徹夜エンジニア”レベルに到達しました。",
    "警告：コーヒーカップが自動でリフィルされました。OSはあなたの健康を心配しています。",
    "今すぐ水分を摂取してください。カフェイン摂取量が推奨上限を超えています。",
    "システム: あなたのマグカップが空になることはありません。",
    "OS診断: 睡眠推奨。カフェイン依存度: 99.9%",
    "警告: 眠気防止モードが自動有効化されました。",
    "ALERT: カフェイン分布が異常です。コーヒー摂取量: MAX",
    "INFO: あなたの作業効率がカフェインに依存しています。",
    "NOTICE: コーヒーブレイクが必要です。",
    "CRITICAL: カフェイン摂取ログが溢れました。"
]

TERMINAL_PREFIXES = [
    "[ALERT] OSより警告:",
    "[WARNING]",
    "[CRITICAL]",
    "[INFO] システム:",
    "[NOTICE] OS診断:"
]

LOG_FILE = os.path.expanduser("~/.fake_caffeine_alert.log")


def select_random_alert():
    idx = random.randint(0, len(FAKE_ALERTS)-1)
    prefix = TERMINAL_PREFIXES[idx % len(TERMINAL_PREFIXES)]
    return f"{prefix} {FAKE_ALERTS[idx]}"


def show_terminal_alert(msg):
    print(msg)


def show_desktop_notification(msg):
    if not PLYER_AVAILABLE:
        return False
    try:
        notification.notify(
            title="OSカフェイン過剰摂取警告",
            message=msg,
            app_name="FakeCaffeineAlert",
            timeout=7
        )
        return True
    except Exception:
        return False


def log_alert(msg):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()} {msg}\n")
    except Exception:
        pass


def list_logs():
    if not os.path.exists(LOG_FILE):
        print("ログファイルがありません。")
        return
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())


def summary_logs():
    if not os.path.exists(LOG_FILE):
        print("ログファイルがありません。")
        return
    count = 0
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for _ in f:
            count += 1
    print(f"合計フェイク警告数: {count}")


def main():
    parser = argparse.ArgumentParser(description="Fake OS Caffeine Overdose Alert Skill")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="ランダムなカフェイン過剰摂取警告を即時表示")
    parser_alert.add_argument("--desktop", action="store_true", help="デスクトップ通知も表示")
    parser_alert.add_argument("--terminal", action="store_true", help="ターミナルにも出力")
    parser_alert.add_argument("--log", action="store_true", help="警告をログに保存")

    parser_daemon = subparsers.add_parser("daemon", help="一定時間ごとに理不尽に警告を表示")
    parser_daemon.add_argument("--min", type=int, default=5, help="最小間隔(分)")
    parser_daemon.add_argument("--max", type=int, default=25, help="最大間隔(分)")
    parser_daemon.add_argument("--desktop", action="store_true", help="デスクトップ通知も表示")
    parser_daemon.add_argument("--terminal", action="store_true", help="ターミナルにも出力")
    parser_daemon.add_argument("--log", action="store_true", help="警告をログに保存")

    parser_list = subparsers.add_parser("list", help="過去の警告ログを表示")
    parser_summary = subparsers.add_parser("summary", help="警告発生回数を集計")

    args = parser.parse_args()

    if args.command == "alert":
        msg = select_random_alert()
        shown = False
        if args.desktop:
            shown = show_desktop_notification(msg)
        if args.terminal or not shown:
            show_terminal_alert(msg)
        if args.log:
            log_alert(msg)
    elif args.command == "daemon":
        min_interval = max(1, args.min)
        max_interval = max(min_interval, args.max)
        print(f"[FakeCaffeineAlert] Daemon開始: {min_interval}-{max_interval}分間隔で警告を表示します。Ctrl+Cで停止。")
        try:
            while True:
                interval = random.randint(min_interval, max_interval) * 60
                time.sleep(interval)
                msg = select_random_alert()
                shown = False
                if args.desktop:
                    shown = show_desktop_notification(msg)
                if args.terminal or not shown:
                    show_terminal_alert(msg)
                if args.log:
                    log_alert(msg)
        except KeyboardInterrupt:
            print("\n[FakeCaffeineAlert] Daemonを停止しました。")
    elif args.command == "list":
        list_logs()
    elif args.command == "summary":
        summary_logs()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
