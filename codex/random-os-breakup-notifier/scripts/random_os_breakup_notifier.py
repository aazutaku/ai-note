import sys
import argparse
import random
import platform
import subprocess
import time
from typing import List, Optional

try:
    import notify2
except ImportError:
    notify2 = None
try:
    from win10toast import ToastNotifier
except ImportError:
    ToastNotifier = None

BREAKUP_MESSAGES = [
    "[重要] あなたの愛用マウスが新しいパートナーに乗り換えました。",
    "[悲報] エディタがそっとあなたのもとを去りました。",
    "[通知] ごめん、今日からCtrlキーはAltキーと付き合うことに。",
    "[警告] ターミナルがあなたのコマンドに飽きてしまったようです。",
    "[速報] あなたのフォルダが別のユーザーと新生活を始めました。",
    "[悲報] あなたのショートカットが他のアプリと駆け落ちしました。",
    "[通知] マウスポインタが新しいデスクトップに引っ越しました。",
    "[重要] あなたの設定ファイルが別のエディタに心変わりしました。",
    "[警告] スクロールバーがあなたの指示に従うのをやめました。",
    "[速報] タスクバーが新しいウィンドウと恋に落ちました。"
]

TRIGGER_KEYWORDS = [
    "breakup", "notification", "joke", "OS", "失恋", "通知", "笑い"
]


def select_random_message() -> str:
    return random.choice(BREAKUP_MESSAGES)


def show_notification(message: str, title: str = "OS失恋通知") -> None:
    system = platform.system()
    if system == "Linux" and notify2:
        try:
            notify2.init("random-os-breakup-notifier")
            n = notify2.Notification(title, message)
            n.set_urgency(notify2.URGENCY_NORMAL)
            n.show()
        except Exception as e:
            print(f"[通知エラー] {e}")
            print(f"{title}: {message}")
    elif system == "Darwin":
        # macOS: osascript 経由で通知
        try:
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        except Exception as e:
            print(f"[通知エラー] {e}")
            print(f"{title}: {message}")
    elif system == "Windows" and ToastNotifier:
        try:
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=5)
        except Exception as e:
            print(f"[通知エラー] {e}")
            print(f"{title}: {message}")
    else:
        # Fallback: 標準出力
        print(f"{title}: {message}")


def list_messages():
    print("--- 通知メッセージ一覧 ---")
    for i, msg in enumerate(BREAKUP_MESSAGES, 1):
        print(f"{i}. {msg}")


def summary():
    print("random-os-breakup-notifier: システムの種類や状況に応じて、シュールな失恋通知をランダムに表示します。")
    print(f"通知バリエーション数: {len(BREAKUP_MESSAGES)}")
    print(f"対応OS: Linux, macOS, Windows (一部は標準出力)\n")
    print("明示呼び出し例: python random_os_breakup_notifier.py notify")
    print("暗黙発動キーワード: " + ", ".join(TRIGGER_KEYWORDS))


def trigger_on_keywords(text: str) -> bool:
    text_lower = text.lower()
    for kw in TRIGGER_KEYWORDS:
        if kw.lower() in text_lower:
            return True
    return False


def notify(args):
    message = select_random_message()
    show_notification(message)


def main():
    parser = argparse.ArgumentParser(description="random-os-breakup-notifier: シュールなOS失恋通知をランダム表示")
    subparsers = parser.add_subparsers(dest="command")

    notify_parser = subparsers.add_parser("notify", help="ランダムな失恋通知を表示")
    notify_parser.add_argument("--message", type=str, help="通知内容を指定 (省略時はランダム)")

    list_parser = subparsers.add_parser("list", help="通知メッセージ一覧を表示")
    summary_parser = subparsers.add_parser("summary", help="Skill概要を表示")
    trigger_parser = subparsers.add_parser("trigger", help="キーワードで通知を発動")
    trigger_parser.add_argument("text", type=str, help="発動判定用テキスト")

    args = parser.parse_args()

    if args.command == "notify":
        message = args.message if args.message else select_random_message()
        show_notification(message)
    elif args.command == "list":
        list_messages()
    elif args.command == "summary":
        summary()
    elif args.command == "trigger":
        if trigger_on_keywords(args.text):
            message = select_random_message()
            show_notification(message)
        else:
            print("[発動条件未検出] 通知は表示されませんでした。")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
