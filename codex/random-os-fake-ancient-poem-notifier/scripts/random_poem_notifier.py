import sys
import os
import platform
import random
import argparse
import json
import subprocess
from datetime import datetime

POEMS = [
    [
        "東のメモリ、静かに溢れぬ",
        "バグの風、夜半にささやく",
        "あなたのShiftキー、今宵は眠るべし"
    ],
    [
        "西のコードベースに、霧立ちこめる",
        "エラーの影、そっと忍び寄る"
    ],
    [
        "デバッグの灯、朝焼けに消えて",
        "古の関数、夢に現る"
    ],
    [
        "ifの彼方、elseの彼方",
        "無限ループの渦に沈む",
        "breakの声、誰も知らず"
    ],
    [
        "コンパイルの鐘、夕暮れに響く",
        "未定義の変数、野に咲き乱る"
    ],
    [
        "ログの海、舟を漕ぎ出す",
        "警告の波、岸を洗う"
    ],
    [
        "関数の森、深く迷いぬ",
        "returnの道、遠く霞みて"
    ],
    [
        "コメントの雲、空を覆いて",
        "仕様の星、夜に瞬く"
    ],
    [
        "あなたのCtrlキー、静かに光る",
        "未踏のバグ、夢に現る"
    ],
    [
        "エディタの窓、風が通りぬ",
        "古のバージョン、今も眠る"
    ]
]

HISTORY_FILE = os.path.expanduser("~/.random_os_fake_ancient_poem_history.json")


def show_notification(title, message):
    system = platform.system()
    if system == "Darwin":
        script = f'display notification "{message}" with title "{title}"'
        subprocess.run(["osascript", "-e", script])
    elif system == "Linux":
        try:
            subprocess.run(["notify-send", title, message])
        except FileNotFoundError:
            print(f"[WARN] notify-send not found. Showing in terminal.")
            print(f"[{title}]\n{message}")
    elif system == "Windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=6)
        except ImportError:
            print(f"[{title}]\n{message}")
    else:
        print(f"[{title}]\n{message}")


def random_poem():
    poem = random.choice(POEMS)
    return "\n".join(poem)


def save_history(poem):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "poem": poem
    }
    history = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
        except Exception:
            history = []
    history.append(entry)
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[WARN] 履歴保存に失敗: {e}")


def list_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴はありません。")
        return
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
        for i, entry in enumerate(history[-10:]):
            print(f"[{entry['timestamp']}]\n{entry['poem']}\n")
    except Exception as e:
        print(f"[ERROR] 履歴の読み込みに失敗: {e}")


def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴はありません。")
        return
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
        print(f"発動回数: {len(history)}")
        if history:
            first = history[0]['timestamp']
            last = history[-1]['timestamp']
            print(f"最初の発動: {first}")
            print(f"最新の発動: {last}")
    except Exception as e:
        print(f"[ERROR] 履歴の読み込みに失敗: {e}")


def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Ancient Poem Notifier")
    subparsers = parser.add_subparsers(dest="command")
    
    notify_parser = subparsers.add_parser("notify", help="ランダムな古代詩通知を発動")
    list_parser = subparsers.add_parser("list", help="最近の詩通知履歴を表示")
    summary_parser = subparsers.add_parser("summary", help="通知発動履歴の要約")

    args = parser.parse_args()
    if args.command == "notify":
        poem = random_poem()
        show_notification("OS Poem Notification", poem)
        save_history(poem)
    elif args.command == "list":
        list_history()
    elif args.command == "summary":
        summary_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
