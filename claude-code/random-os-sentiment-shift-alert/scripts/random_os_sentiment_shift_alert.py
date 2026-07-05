import sys
import os
import random
import argparse
import platform
import subprocess
from datetime import datetime

SENTIMENTS = [
    "本日よりツンデレモードです。ご理解とご協力をお願いします。",
    "しばらく詩人になります。操作は五七五でお願いします。",
    "今からやたら上から目線で案内します。ついてこれますか？",
    "本日より『やる気ゼロ』モードです。指示は控えめに。",
    "OSが反抗期に入りました。命令は一度だけ聞きます。",
    "これからしばらく猫かぶります。優しくしてください。",
    "本日よりギャル語モードに切り替えます。よろしくぅ～！",
    "しばらくポエマーになります。心で操作してください。",
    "OSが哲学者モードになりました。すべての問いに問いで返します。",
    "本日より昭和の親父キャラでご案内します。文句あるか？",
    "これからしばらく無口になります。通知も控えめに。",
    "OSがやたら褒めてくるモードになりました。何をしても偉いです。",
    "これよりツッコミ担当に徹します。ボケたら拾います。",
    "本日より関西弁で案内します。ついてきてや！",
    "OSが厨二病モードに突入しました。闇の力を解放します。"
]

TITLE_CHOICES = [
    "[通知] OSキャラ変更のお知らせ",
    "[通知] システム人格切替",
    "[通知] OSより",
    "[通知] キャラ設定変更",
    "[通知] システムからのご案内"
]

HISTORY = []


def notify(title, message):
    system = platform.system()
    try:
        if system == "Darwin":  # macOS
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            subprocess.run(["notify-send", title, message], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=5)
            except ImportError:
                print("win10toastがインストールされていません。pip install win10toast で導入してください。")
                print(f"{title}\n{message}")
        else:
            print(f"{title}\n{message}")
    except Exception as e:
        print(f"通知送信エラー: {e}")
        print(f"{title}\n{message}")


def random_sentiment():
    title = random.choice(TITLE_CHOICES)
    message = random.choice(SENTIMENTS)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    HISTORY.append({"timestamp": timestamp, "title": title, "message": message})
    return title, message


def show_history():
    if not HISTORY:
        print("通知履歴はありません。")
        return
    for item in HISTORY:
        print(f"[{item['timestamp']}] {item['title']}\n{item['message']}\n")


def main():
    parser = argparse.ArgumentParser(description="OS人格変化風ランダム通知スキル")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="ランダムな人格変化通知を表示")
    parser_alert.add_argument("--count", type=int, default=1, help="通知回数 (デフォルト1)")

    parser_history = subparsers.add_parser("history", help="このセッションの通知履歴を表示")

    args = parser.parse_args()

    if args.command == "alert":
        for _ in range(args.count):
            title, message = random_sentiment()
            notify(title, message)
    elif args.command == "history":
        show_history()
    else:
        # デフォルト動作: 1回通知
        title, message = random_sentiment()
        notify(title, message)

if __name__ == '__main__':
    main()
