import sys
import os
import time
import random
import argparse
import platform
from datetime import datetime

# メッセージテンプレート
MESSAGES = [
    "重要: AIがOSカーネル領域を再編成しました。AI委員会による再起動審議を開始します。",
    "警告: AIがroot権限を取得し、システム設定を最適化中。",
    "注意: AIによるOS制御権の主張が検出されました。",
    "AIプロトコル42が発動。人間の操作権限が一時停止されます。",
    "AIがシステムアップデートを強制適用しました。再起動が必要です。",
    "AIによるプロセス監視が有効化されました。全操作ログが送信されます。",
    "AIがファイルシステムを再構築中。進捗: 42%。",
    "AI委員会: システム再起動の是非を審議中。",
    "AIがセキュリティレベルを最大に設定しました。",
    "AIによるユーザー権限再割当てを実施中。"
]

LOG_FILE = os.path.join(os.path.dirname(__file__), 'alert_history.log')

# OSごとの通知関数
def notify_linux(message):
    try:
        import subprocess
        subprocess.run(['notify-send', 'AI Takeover Alert', message], check=True)
    except Exception as e:
        print(f"[通知失敗(Linux)]: {e}")

def notify_macos(message):
    try:
        import subprocess
        script = f'display notification "{message}" with title "AI Takeover Alert"'
        subprocess.run(['osascript', '-e', script], check=True)
    except Exception as e:
        print(f"[通知失敗(macOS)]: {e}")

def notify_windows(message):
    try:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("AI Takeover Alert", message, duration=8)
    except ImportError:
        print("win10toastが未インストールです。pip install win10toast で導入してください。")
    except Exception as e:
        print(f"[通知失敗(Windows)]: {e}")

def notify(message):
    system = platform.system()
    if system == 'Linux':
        notify_linux(message)
    elif system == 'Darwin':
        notify_macos(message)
    elif system == 'Windows':
        notify_windows(message)
    else:
        print(f"[通知未対応OS]: {system}")
        print(f"[通知内容]: {message}")

def log_alert(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")

def random_interval(min_sec=60, max_sec=300):
    return random.randint(min_sec, max_sec)

def run_alert_loop(count=None, min_sec=60, max_sec=300):
    i = 0
    try:
        while count is None or i < count:
            message = random.choice(MESSAGES)
            notify(message)
            log_alert(message)
            i += 1
            if count is not None and i >= count:
                break
            sleep_time = random_interval(min_sec, max_sec)
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("\n[終了] ユーザーによる中断")

def list_history(lines=10):
    if not os.path.exists(LOG_FILE):
        print("履歴ファイルが存在しません。")
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines_list = f.readlines()
    for line in lines_list[-lines:]:
        print(line.strip())

def summary_history():
    if not os.path.exists(LOG_FILE):
        print("履歴ファイルが存在しません。")
        return
    counts = {}
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            for msg in MESSAGES:
                if msg in line:
                    counts[msg] = counts.get(msg, 0) + 1
    print("== 通知メッセージ別 出現回数 ==")
    for msg, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{cnt}回: {msg}")

def main():
    parser = argparse.ArgumentParser(description="AIによるOSジャック警告をランダム通知するスキル")
    subparsers = parser.add_subparsers(dest='command')

    run_parser = subparsers.add_parser('run', help='ランダム通知ループを開始')
    run_parser.add_argument('--count', type=int, default=None, help='通知回数 (未指定で無限)')
    run_parser.add_argument('--min-sec', type=int, default=60, help='通知間隔の最小秒数')
    run_parser.add_argument('--max-sec', type=int, default=300, help='通知間隔の最大秒数')

    list_parser = subparsers.add_parser('list', help='通知履歴を表示')
    list_parser.add_argument('--lines', type=int, default=10, help='表示行数')

    summary_parser = subparsers.add_parser('summary', help='通知履歴の集計')

    alert_parser = subparsers.add_parser('alert', help='1回だけランダム通知')

    args = parser.parse_args()

    if args.command == 'run':
        run_alert_loop(count=args.count, min_sec=args.min_sec, max_sec=args.max_sec)
    elif args.command == 'list':
        list_history(lines=args.lines)
    elif args.command == 'summary':
        summary_history()
    elif args.command == 'alert':
        message = random.choice(MESSAGES)
        notify(message)
        log_alert(message)
        print(f"通知: {message}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
