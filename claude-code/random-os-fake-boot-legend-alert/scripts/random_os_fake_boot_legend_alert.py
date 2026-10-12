import sys
import os
import time
import random
import argparse
import platform
import subprocess
from typing import List

LEGEND_MESSAGES = [
    "本日、あなたは選ばれしOSユーザーです。",
    "伝説のブートシーケンスが発動しました。",
    "BIOS: “古の声が聞こえる...システムは覚醒した”",
    "OS神話モード: 有効",
    "謎のカーネルが目覚める...",
    "あなたのマシンに伝説のコードが注入されました。",
    "SYSTEM: “時空を超える起動が検知されました”",
    "古のOSの魂が共鳴しています。",
    "伝説のレジスタが全開放されました。",
    "本日はOS界の祭典日です。",
    "BIOS: “あなたの存在を記録します”",
    "OS伝説：神話的アップタイムが始まります。",
    "謎のファームウェアが祝福しています。",
    "あなたのコマンドに伝説の力が宿りました。",
    "伝説のシステムコールが発動。"
]

NOTIFY_TITLE = "伝説のOS起動通知"


def get_random_message() -> str:
    lines = random.sample(LEGEND_MESSAGES, k=random.randint(2, 4))
    return f"[{NOTIFY_TITLE}]\n" + "\n---\n".join(lines)


def notify_desktop(message: str):
    system = platform.system()
    try:
        if system == "Darwin":
            # macOS: osascript
            script = f'display notification "{message}" with title "{NOTIFY_TITLE}"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            # Linux: notify-send (X/Wayland)
            subprocess.run(["notify-send", NOTIFY_TITLE, message], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(NOTIFY_TITLE, message, duration=6)
            except ImportError:
                print("win10toastが未インストールです。'pip install win10toast'で導入してください。\nターミナルに表示します。")
                print(message)
        else:
            print(f"未対応OSです: {system}\n{message}")
    except Exception as e:
        print(f"通知の送信に失敗しました: {e}\n{message}")


def notify_terminal(message: str):
    border = "=" * 40
    print(f"\n{border}\n{message}\n{border}\n")


def should_trigger_legend_alert(args, input_text: str = None) -> bool:
    if args.force:
        return True
    if input_text:
        keywords = ["起動", "伝説", "OS", "BIOS", "神話", "レジェンド"]
        return any(k in input_text for k in keywords)
    return False


def run_alert(args, input_text: str = None):
    message = get_random_message()
    if args.mode == "desktop":
        notify_desktop(message)
    elif args.mode == "terminal":
        notify_terminal(message)
    else:
        notify_desktop(message)
        notify_terminal(message)


def auto_mode(args):
    interval = args.interval
    count = args.count
    for i in range(count):
        run_alert(args)
        if i < count - 1:
            time.sleep(interval)


def parse_args():
    parser = argparse.ArgumentParser(description="伝説のOS起動通知スキル")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="伝説の通知を即時発動")
    parser_alert.add_argument("--mode", choices=["desktop", "terminal", "both"], default="both", help="通知方法")
    parser_alert.add_argument("--force", action="store_true", help="強制発動")

    parser_auto = subparsers.add_parser("auto", help="定期的に伝説通知を発動")
    parser_auto.add_argument("--interval", type=int, default=1800, help="通知間隔(秒)")
    parser_auto.add_argument("--count", type=int, default=3, help="発動回数")
    parser_auto.add_argument("--mode", choices=["desktop", "terminal", "both"], default="both", help="通知方法")

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "alert":
        run_alert(args)
    elif args.command == "auto":
        auto_mode(args)
    else:
        # 標準入力からのキーワード検知
        print("標準入力を監視します。Ctrl+Dで終了。\n")
        try:
            while True:
                line = sys.stdin.readline()
                if not line:
                    break
                if should_trigger_legend_alert(args, line):
                    run_alert(args)
        except KeyboardInterrupt:
            print("\n終了します。")

if __name__ == '__main__':
    main()
