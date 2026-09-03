import sys
import argparse
import random
import platform
import subprocess
import time
from typing import List

FAKE_NOTIFICATIONS = [
    {
        "title": "OS省エネモードが自動発動しました。",
        "lines": [
            "全ウィンドウの明るさ自動調整中…(完了)",
            "キーボード省入力モード：有効",
            "CPUパフォーマンス：自己最適化中",
            "注意：省エネ中は全てが遅く感じるかもしれません。"
        ]
    },
    {
        "title": "OSが独断で『超省エネモード』に切り替えました。",
        "lines": [
            "画面の色温度を勝手に調整しています…(実際には何もしていません)",
            "全アプリケーションのリフレッシュレートを自動低下中",
            "バッテリー節約アルゴリズム：AI最適化（実装予定）",
            "ご理解とご協力をお願いします。"
        ]
    },
    {
        "title": "謎の省エネモード突入通知",
        "lines": [
            "OSが勝手にパフォーマンスを自己最適化しています。",
            "一部機能が制限される場合があります（ウソです）",
            "省エネ解除は自動で行われます。",
            "何も起こっていませんのでご安心ください。"
        ]
    },
    {
        "title": "Fake Power Saving Mode Activated",
        "lines": [
            "All windows brightness auto-adjusted (not really)",
            "Keyboard input minimized to save energy (makes no sense)",
            "OS is optimizing performance in the background",
            "You may feel everything is slower now (placebo effect)"
        ]
    },
    {
        "title": "省エネモード：フェイク通知",
        "lines": [
            "画面の解像度をダウンスケーリング中…(嘘)",
            "ネットワーク帯域幅を自動制限（していません）",
            "全プロセスの優先度をランダム化（意味不明）",
            "この通知は完全なジョークです。"
        ]
    },
    {
        "title": "OS Energy Saver Mode (Fake)",
        "lines": [
            "Reducing system font size for power saving (not implemented)",
            "Randomly pausing background apps (no effect)",
            "Auto-dimming the terminal window",
            "Enjoy your placebo performance boost!"
        ]
    }
]


def select_random_notification() -> dict:
    return random.choice(FAKE_NOTIFICATIONS)


def format_notification(notification: dict) -> str:
    lines = [f"[通知] {notification['title']}"]
    lines.extend(notification['lines'])
    return "\n".join(lines)


def show_notification_terminal(notification: dict):
    print(format_notification(notification))


def show_notification_desktop(notification: dict):
    system = platform.system()
    title = notification["title"]
    message = "\n".join(notification["lines"])
    try:
        if system == "Darwin":  # macOS
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "{title}"'
            ], check=True)
        elif system == "Linux":
            subprocess.run([
                "notify-send", title, message
            ], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=5)
            except ImportError:
                print("win10toastがインストールされていません。ターミナル通知のみ行います。")
                show_notification_terminal(notification)
        else:
            show_notification_terminal(notification)
    except Exception as e:
        print(f"通知送信に失敗しました: {e}")
        show_notification_terminal(notification)


def list_notifications():
    for idx, n in enumerate(FAKE_NOTIFICATIONS, 1):
        print(f"{idx}. {n['title']}")
        for line in n['lines']:
            print(f"   - {line}")
        print()


def summary():
    print("このSkillは、完全なフェイクの省エネ通知をランダムに生成し、デスクトップまたはターミナルに表示します。\n実際のOSや作業環境には一切影響を与えません。通知内容は毎回変化し、ユーモラスな演出で集中力や現実感覚を揺さぶります。")


def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Power Saving Mode Notifier")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    parser_log = subparsers.add_parser("log", help="フェイク省エネ通知を1回表示")
    parser_log.add_argument("--desktop", action="store_true", help="デスクトップ通知も行う（notify-send/osascript等使用）")

    parser_list = subparsers.add_parser("list", help="全通知バリエーションを一覧表示")
    parser_summary = subparsers.add_parser("summary", help="Skill概要を表示")

    args = parser.parse_args()
    if args.command == "log":
        notification = select_random_notification()
        show_notification_terminal(notification)
        if args.desktop:
            show_notification_desktop(notification)
    elif args.command == "list":
        list_notifications()
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
