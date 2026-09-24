import sys
import os
import random
import time
import argparse
import platform
import subprocess
from datetime import datetime

POEMS = [
    [
        "西のコードベースにバグの風そよぐ",
        "あなたのShiftキー、今宵は静かに眠るべし",
        "朝霧のメモリ、解放されぬまま",
        "デバッグの道、遠く霞みて"
    ],
    [
        "コンパイルの鐘、虚空に響く",
        "エラーの渦巻、心を惑わす"
    ],
    [
        "ファイルの彼方、未保存の夢"
    ],
    [
        "if文の彼岸、elseの彼方",
        "print文、夜明けに消えゆく"
    ],
    [
        "メモリの谷間に、GCの風渡る",
        "変数の名も、今は昔"
    ],
    [
        "ビルドの雲間に、光る警告",
        "警告の雨、止むことなし"
    ],
    [
        "関数の森に、迷い人ひとり",
        "returnの道、いまだ見えず"
    ],
    [
        "ログの海原、波高く",
        "スタックトレース、岸に打ち寄せる"
    ],
    [
        "mainの門、静かに開かれ",
        "無限ループ、時を刻む"
    ],
    [
        "バージョンの月、満ち欠けし",
        "古きAPI、夢のごとし"
    ]
]

NOTIFY_TITLE = "OS古代詩通知"


def select_random_poem():
    poem = random.choice(POEMS)
    return "\n".join(poem)


def notify_desktop(message):
    system = platform.system()
    try:
        if system == "Linux":
            # Use notify-send
            subprocess.run(["notify-send", NOTIFY_TITLE, message])
        elif system == "Darwin":
            # Use osascript for macOS
            script = f'display notification "{message}" with title "{NOTIFY_TITLE}"'
            subprocess.run(["osascript", "-e", script])
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(NOTIFY_TITLE, message, duration=5)
            except ImportError:
                print("win10toastが見つかりません。pip install win10toast でインストールしてください。", file=sys.stderr)
        else:
            print(f"[通知未対応OS] {NOTIFY_TITLE}:\n{message}")
    except Exception as e:
        print(f"[通知エラー] {e}\n{NOTIFY_TITLE}:\n{message}")


def print_terminal(message):
    print(f"[{NOTIFY_TITLE}]\n{message}\n")


def log_poem(poem):
    log_path = os.path.expanduser("~/.random_os_fake_ancient_poem_notifier.log")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}]\n{poem}\n\n")


def list_log():
    log_path = os.path.expanduser("~/.random_os_fake_ancient_poem_notifier.log")
    if not os.path.exists(log_path):
        print("通知履歴はありません。")
        return
    with open(log_path, encoding="utf-8") as f:
        print(f.read())


def summary_log():
    log_path = os.path.expanduser("~/.random_os_fake_ancient_poem_notifier.log")
    if not os.path.exists(log_path):
        print("通知履歴はありません。")
        return
    count = 0
    with open(log_path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("[") and "]" in line:
                count += 1
    print(f"これまでに{count}件の古代詩通知が発動しました。")


def main():
    parser = argparse.ArgumentParser(description="OS古代詩通知スキル")
    subparsers = parser.add_subparsers(dest="command", required=False)

    parser_log = subparsers.add_parser("log", help="通知履歴を表示")
    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリーを表示")
    parser_run = subparsers.add_parser("run", help="1回だけランダム通知を発動")
    parser_daemon = subparsers.add_parser("daemon", help="一定間隔で自動通知 (Ctrl+Cで停止)")
    parser_daemon.add_argument("--interval", type=int, default=1800, help="通知間隔(秒) デフォルト30分")

    args = parser.parse_args()

    if args.command == "log":
        list_log()
    elif args.command == "summary":
        summary_log()
    elif args.command == "run":
        poem = select_random_poem()
        notify_desktop(poem)
        print_terminal(poem)
        log_poem(poem)
    elif args.command == "daemon":
        print(f"{NOTIFY_TITLE} デーモンを開始します。Ctrl+Cで停止。通知間隔: {args.interval}秒")
        try:
            while True:
                poem = select_random_poem()
                notify_desktop(poem)
                print_terminal(poem)
                log_poem(poem)
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\nデーモンを停止しました。")
    else:
        # デフォルト動作: 1回だけ通知
        poem = select_random_poem()
        notify_desktop(poem)
        print_terminal(poem)
        log_poem(poem)

if __name__ == '__main__':
    main()
