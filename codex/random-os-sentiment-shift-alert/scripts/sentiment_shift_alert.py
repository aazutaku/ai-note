import sys
import os
import random
import argparse
import platform
import subprocess
from typing import List

# 通知メッセージのバリエーション
SENTIMENTS = [
    "本日よりツンデレモードで対応します。ご注意ください。",
    "しばらく詩人として案内します。ご容赦ください。",
    "今からやたら上から目線になります。",
    "本日よりOSは無口モードです。",
    "しばらく厨二病モードで動作します。",
    "本日よりOSは語尾に『にゃ』を付けて案内します。",
    "本日よりOSは昭和風に対応します。",
    "しばらくポエムモードでご案内します。",
    "今後しばらくは謎の関西弁で通知します。",
    "OSは今日からやる気ゼロモードです。",
    "本日よりOSはクールキャラに徹します。",
    "しばらくOSは解説がやたら長くなります。",
    "本日よりOSは語彙力が低下します。",
    "しばらくOSは無駄にテンション高いです。",
    "今後しばらくはOSがやたら詩的です。",
    "本日よりOSは語尾に『ござる』を付けます。",
    "しばらくOSは名探偵風に案内します。",
    "OSは今日からやけに親身です。",
    "本日よりOSは謎の上司キャラです。",
    "しばらくOSは説明が全部質問形式です。"
]

HISTORY_FILE = os.path.expanduser("~/.sentiment_shift_alert_history")


def send_notification(message: str):
    system = platform.system()
    if system == "Linux":
        try:
            subprocess.run(["notify-send", "OS通知", message], check=True)
        except Exception as e:
            print(f"[通知] OS通知: {message}")
    elif system == "Darwin":
        script = f'display notification "{message}" with title "OS通知"'
        try:
            subprocess.run(["osascript", "-e", script], check=True)
        except Exception as e:
            print(f"[通知] OS通知: {message}")
    elif system == "Windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("OS通知", message, duration=5)
        except ImportError:
            print("win10toastがインストールされていません。pip install win10toast で追加してください。")
            print(f"[通知] OS通知: {message}")
        except Exception as e:
            print(f"[通知] OS通知: {message}")
    else:
        print(f"[通知] OS通知: {message}")


def random_sentiment() -> str:
    return random.choice(SENTIMENTS)


def log_history(message: str):
    try:
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
            f.write(message + '\n')
    except Exception as e:
        pass


def list_history(limit: int = 10):
    try:
        if not os.path.exists(HISTORY_FILE):
            print("履歴はありません。")
            return
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[-limit:]:
                print(line.strip())
    except Exception as e:
        print("履歴の読み込みに失敗しました。")


def summary_history():
    try:
        if not os.path.exists(HISTORY_FILE):
            print("履歴はありません。")
            return
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        total = len(lines)
        unique = len(set([l.strip() for l in lines]))
        print(f"通知履歴: {total}件 (ユニーク: {unique}種)")
    except Exception as e:
        print("履歴サマリの取得に失敗しました。")


def main():
    parser = argparse.ArgumentParser(description="random-os-sentiment-shift-alert: OS人格変化通知スキル")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    parser_alert = subparsers.add_parser("alert", help="ランダム通知を表示")
    parser_alert.add_argument("-n", "--num", type=int, default=1, help="通知回数")

    parser_list = subparsers.add_parser("list", help="通知履歴を表示")
    parser_list.add_argument("-l", "--limit", type=int, default=10, help="表示件数")

    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリを表示")

    args = parser.parse_args()

    if args.command == "alert":
        for _ in range(args.num):
            message = random_sentiment()
            send_notification(message)
            log_history(message)
    elif args.command == "list":
        list_history(args.limit)
    elif args.command == "summary":
        summary_history()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
