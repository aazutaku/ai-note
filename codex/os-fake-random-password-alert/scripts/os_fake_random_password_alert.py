import random
import string
import sys
import argparse
import time
import platform
import subprocess
from typing import List

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

def generate_fake_password() -> str:
    # パスワード候補語彙
    words = [
        'banana', 'tamagoyaki', 'moonlight', 'sakura', 'dragon', 'coffee', 'penguin', 'ninja',
        'neko', 'ramen', 'mountain', 'rainbow', 'giraffe', 'sushi', 'samurai', 'robot',
        'panda', 'guitar', 'apple', 'honey', 'cloud', 'wizard', 'mikan', 'bamboo', 'caramel'
    ]
    suffix = random.choice(['', str(random.randint(10, 9999)), str(random.randint(1950, 2024))])
    word = random.choice(words)
    if random.random() < 0.3:
        word2 = random.choice([w for w in words if w != word])
        password = f"{word}{random.choice(['-', '_'])}{word2}{suffix}"
    else:
        password = f"{word}{random.choice(['-', '_'])}{suffix}"
    # さらに数字や記号を混ぜる
    if random.random() < 0.5:
        password += random.choice(['!', '@', '#', ''])
    return password

def generate_notification_message() -> (str, str):
    password = generate_fake_password()
    titles = [
        "OS公式パスワード流出警告",
        "警告：パスワード流出が検出されました",
        "本日発見された流出パスワード",
        "セキュリティアラート",
        "注意：不正なパスワード公開"
    ]
    messages = [
        f"あなたの秘密パスワードが『{password}』としてインターネット上に流出しました。",
        f"警告：本日発見された流出パスワード『{password}』。第三者により公開されています。",
        f"セキュリティ上の理由により、パスワード『{password}』が流出した可能性があります。",
        f"ご利用中のパスワード『{password}』が漏洩したとの情報が届きました。",
        f"新たな流出パスワード『{password}』が検出されました。"
    ]
    joke_notice = random.choice([
        "ご安心ください：これはジョーク通知です。",
        "※本通知はエンタメ目的のジョークです。",
        "本メッセージは冗談です。実際の流出ではありません。",
        "これはネタ通知ですのでご安心ください。"
    ])
    title = random.choice(titles)
    message = random.choice(messages) + "\n" + joke_notice
    return title, message

def send_notification(title: str, message: str):
    # OSごとに通知方法を切り替える
    if PLYER_AVAILABLE:
        notification.notify(title=title, message=message, timeout=6)
    else:
        system = platform.system()
        if system == 'Darwin':
            # macOS
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script])
        elif system == 'Linux':
            # Linux: notify-send
            subprocess.run(["notify-send", title, message])
        elif system == 'Windows':
            # Windows: 簡易的なfallback
            print(f"[通知] {title}\n{message}")
        else:
            print(f"[通知] {title}\n{message}")

def log_notification(title: str, message: str, logfile: str = None):
    if logfile:
        with open(logfile, 'a', encoding='utf-8') as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {title}\n{message}\n\n")

def list_log(logfile: str):
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("ログファイルが見つかりません。")

def summary_log(logfile: str):
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        count = sum(1 for line in lines if line.startswith('['))
        print(f"通知履歴数: {count}")
    except FileNotFoundError:
        print("ログファイルが見つかりません。")

def main():
    parser = argparse.ArgumentParser(description='OS風偽パスワード流出警告通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='通知を1件生成して表示&ログ')
    parser_log.add_argument('--logfile', type=str, default=None, help='通知ログファイルパス')

    parser_list = subparsers.add_parser('list', help='通知ログを一覧表示')
    parser_list.add_argument('--logfile', type=str, required=True, help='通知ログファイルパス')

    parser_summary = subparsers.add_parser('summary', help='通知履歴の件数を表示')
    parser_summary.add_argument('--logfile', type=str, required=True, help='通知ログファイルパス')

    parser_once = subparsers.add_parser('once', help='通知を1件だけ表示（ログしない）')

    args = parser.parse_args()
    if args.command in ('log', None):
        title, message = generate_notification_message()
        send_notification(title, message)
        log_notification(title, message, logfile=args.logfile)
    elif args.command == 'once':
        title, message = generate_notification_message()
        send_notification(title, message)
    elif args.command == 'list':
        list_log(args.logfile)
    elif args.command == 'summary':
        summary_log(args.logfile)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
