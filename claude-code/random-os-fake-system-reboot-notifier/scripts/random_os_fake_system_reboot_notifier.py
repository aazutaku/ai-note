import argparse
import random
import sys
import platform
import subprocess
import time
from datetime import datetime

# 通知メッセージ候補
TITLES = [
    "重要なお知らせ",
    "システムメンテナンス",
    "重大なアップデート",
    "再起動予告",
    "管理者通知",
    "自動再起動アラート"
]

REASONS = [
    "カーネルの気まぐれ",
    "管理者の気まぐれ",
    "宇宙線の影響",
    "メモリの気分転換",
    "OSが寂しがっているため",
    "謎の理由",
    "AIの独断",
    "システムの都合",
    "セキュリティ強化のため",
    "アップデートのため"
]

TIMES = [3, 5, 7, 10, 15]

LOG_FILE = "reboot_notifier.log"


def create_notification_message():
    title = random.choice(TITLES)
    minutes = random.choice(TIMES)
    reason = random.choice(REASONS)
    body = f"{minutes}分後にシステムは{reason}で再起動します。"
    reason_line = f"理由：{reason}"
    return title, body, reason_line, minutes


def send_notification(title, message, reason):
    os_name = platform.system()
    full_message = f"{message}\n{reason}"
    if os_name == "Darwin":
        try:
            subprocess.run([
                "osascript", "-e",
                f'display notification "{full_message}" with title "{title}"'
            ], check=True)
        except Exception as e:
            print(f"[ERROR] macOS通知失敗: {e}")
    elif os_name == "Windows":
        try:
            from plyer import notification
            notification.notify(
                title=title,
                message=full_message,
                app_name="FakeOSNotifier",
                timeout=10
            )
        except ImportError:
            print("[ERROR] plyerがインストールされていません。pip install plyer を実行してください。")
        except Exception as e:
            print(f"[ERROR] Windows通知失敗: {e}")
    elif os_name == "Linux":
        try:
            subprocess.run([
                "notify-send", title, full_message
            ], check=True)
        except Exception as e:
            print(f"[ERROR] Linux通知失敗: {e}")
    else:
        print(f"[WARN] 未対応OS: {os_name}")
        print(f"[通知] {title}: {full_message}")


def log_notification(title, message, reason):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {title}: {message} | {reason}\n")


def list_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("ログがありません。")
            else:
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print("ログファイルがありません。まだ通知は発行されていません。")


def summary_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(f"合計通知回数: {len(lines)}")
            reasons = {}
            for line in lines:
                if "理由：" in line:
                    reason = line.split("理由：")[-1].strip()
                    reasons[reason] = reasons.get(reason, 0) + 1
            print("理由別集計:")
            for k, v in sorted(reasons.items(), key=lambda x: -x[1]):
                print(f"  {k}: {v}回")
    except FileNotFoundError:
        print("ログファイルがありません。")


def main():
    parser = argparse.ArgumentParser(description="ランダムなOS再起動ジョーク通知を表示します。")
    subparsers = parser.add_subparsers(dest="command")

    parser_notify = subparsers.add_parser("notify", help="ランダムな通知を1回表示")
    parser_notify.add_argument("--dry-run", action="store_true", help="実際に通知せず内容だけ表示")

    parser_log = subparsers.add_parser("log", help="通知履歴を表示")
    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリーを表示")

    args = parser.parse_args()

    if args.command == "notify":
        title, message, reason, _ = create_notification_message()
        if args.dry_run:
            print(f"[DRY RUN] {title}: {message}\n{reason}")
        else:
            send_notification(title, message, reason)
            log_notification(title, message, reason)
            print(f"[通知] {title}: {message}\n{reason}")
    elif args.command == "log":
        list_log()
    elif args.command == "summary":
        summary_log()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
