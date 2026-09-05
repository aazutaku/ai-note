import sys
import os
import random
import string
import argparse
import platform
import subprocess
from datetime import datetime

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

def generate_fake_password():
    words = ['banana', 'tamagoyaki', 'sushi', 'ramen', 'mountain', 'dreams', 'cloud', 'river', 'cat', 'piano', 'sky', 'orange', 'moon', 'castle', 'robot', 'garden', 'train', 'ocean', 'forest', 'star']
    suffix = random.choice(['', str(random.randint(10, 9999)), '_' + ''.join(random.choices(string.ascii_lowercase, k=3)), '-' + str(random.randint(100, 999))])
    word = random.choice(words)
    if random.random() < 0.5:
        word2 = random.choice(words)
        pw = f"{word}{random.choice(['_', '-', ''])}{word2}{suffix}"
    else:
        pw = f"{word}{suffix}"
    return pw

def generate_notification_message():
    templates = [
        "あなたの秘密パスワードが『{pw}』としてインターネットに流出しました。",
        "警告：本日発見された流出パスワード『{pw}』",
        "注意：新たなパスワード『{pw}』が漏洩した可能性があります。",
        "OSが検知した流出パスワード：『{pw}』",
        "システム警告：パスワード『{pw}』が外部に公開されました。"
    ]
    pw = generate_fake_password()
    message = random.choice(templates).format(pw=pw)
    if random.random() < 0.5:
        message += "\n※これはジョーク通知です。実際の流出はありません。"
    else:
        message += "\n（ジョーク通知）"
    return message

def send_notification(title, message):
    system = platform.system()
    if PLYER_AVAILABLE:
        notification.notify(title=title, message=message, timeout=7)
        return True
    # Fallbacks
    if system == "Linux":
        try:
            subprocess.run(["notify-send", title, message], check=True)
            return True
        except Exception:
            return False
    elif system == "Darwin":
        try:
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
            return True
        except Exception:
            return False
    elif system == "Windows":
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(title, message, duration=7)
            return True
        except Exception:
            return False
    return False

def log_notification(message, logfile="~/.os_fake_random_password_alert.log"):
    logfile = os.path.expanduser(logfile)
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] {message}\n")

def list_notifications(logfile="~/.os_fake_random_password_alert.log", limit=20):
    logfile = os.path.expanduser(logfile)
    if not os.path.exists(logfile):
        print("No notifications logged yet.")
        return
    with open(logfile, encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines[-limit:]:
        print(line.strip())

def summary_notifications(logfile="~/.os_fake_random_password_alert.log"):
    logfile = os.path.expanduser(logfile)
    if not os.path.exists(logfile):
        print("No notifications logged yet.")
        return
    with open(logfile, encoding="utf-8") as f:
        lines = f.readlines()
    print(f"合計通知回数: {len(lines)}")
    if lines:
        print(f"最新通知: {lines[-1].strip()}")

def main():
    parser = argparse.ArgumentParser(description="OS Fake Random Password Alert Skill")
    subparsers = parser.add_subparsers(dest="command", required=False)

    parser_log = subparsers.add_parser("log", help="最新の偽パスワード流出警告を発生させて記録する")
    parser_list = subparsers.add_parser("list", help="過去の通知ログを表示する")
    parser_list.add_argument("--limit", type=int, default=20, help="表示件数")
    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリを表示する")

    args = parser.parse_args()
    if args.command == "list":
        list_notifications(limit=args.limit)
    elif args.command == "summary":
        summary_notifications()
    else:
        title = "[OS公式] パスワード流出警告（ジョーク通知）"
        message = generate_notification_message()
        sent = send_notification(title, message)
        log_notification(message)
        if sent:
            print("通知を送信しました。")
        else:
            print("通知送信に失敗しました。ログのみ記録しました。")
        print(f"内容:\n{message}")

if __name__ == "__main__":
    main()
