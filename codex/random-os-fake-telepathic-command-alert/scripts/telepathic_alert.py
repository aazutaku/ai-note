import sys
import os
import random
import platform
import subprocess
import argparse
import time
from typing import List

FAKE_COMMANDS = [
    "make coffee",
    "deploy to mars",
    "sudo fix all bugs instantly",
    "take a nap",
    "hack time itself",
    "summon pizza",
    "enable quantum mode",
    "reboot universe",
    "teleport home",
    "auto-merge all PRs",
    "undo last year",
    "find meaning of life",
    "run infinite loop of joy",
    "activate stealth mode",
    "mute all meetings",
    "generate unlimited snacks",
    "escape reality",
    "clone self",
    "start holiday",
    "pause time"
]

ALERT_PREFIXES = [
    "[Telepathic OS Alert]",
    "[念波検出]",
    "[思念コマンド捕捉]",
    "[OS読心術通知]",
    "[未知の念波]"
]

ALERT_PATTERNS = [
    "あなたが心の中で考えたコマンドを検出しました: '{cmd}'",
    "念波検出: '{cmd}'",
    "思念コマンド捕捉: '{cmd}'",
    "OSがあなたの夢を感知しました: '{cmd}'",
    "未知の念波: '{cmd}'"
]

HISTORY_FILE = os.path.expanduser("~/.telepathic_alert_history")


def choose_fake_alert() -> str:
    cmd = random.choice(FAKE_COMMANDS)
    pattern = random.choice(ALERT_PATTERNS)
    prefix = random.choice(ALERT_PREFIXES)
    return f"{prefix}\n{pattern.format(cmd=cmd)}"


def send_notification(message: str):
    sys_platform = platform.system()
    try:
        if sys_platform == "Linux":
            subprocess.run(["notify-send", "Telepathic OS Alert", message], check=True)
        elif sys_platform == "Darwin":
            # macOS: use osascript
            script = f'display notification "{message}" with title "Telepathic OS Alert"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif sys_platform == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("Telepathic OS Alert", message, duration=5)
            except ImportError:
                print("win10toastが必要です: pip install win10toast")
        else:
            print("このOSでは通知がサポートされていません。\n" + message)
    except Exception as e:
        print(f"通知送信時にエラー: {e}\n\n{message}")


def log_alert(message: str):
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}\t{message}\n")
    except Exception as e:
        print(f"履歴ファイル書き込みエラー: {e}")


def show_history(limit: int = 10):
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()[-limit:]
        print("-- Telepathic Alert 履歴 --")
        for line in lines:
            print(line.strip())
    except Exception as e:
        print(f"履歴表示エラー: {e}")


def summary():
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        total = len(lines)
        cmds = [l.split('\t')[-1].split(": '")[-1].rstrip("'") for l in lines if ": '" in l]
        unique_cmds = set(cmds)
        print(f"合計通知数: {total}")
        print(f"ユニーク妄想コマンド数: {len(unique_cmds)}")
        print(f"最近のコマンド例: {list(unique_cmds)[:5]}")
    except Exception as e:
        print(f"サマリー取得エラー: {e}")


def main():
    parser = argparse.ArgumentParser(description="OS読心術フェイク通知スキル")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser("log", help="ランダムなテレパシー通知を発生させる")
    parser_log.add_argument("--count", type=int, default=1, help="連続発生回数")
    parser_log.add_argument("--interval", type=float, default=0, help="通知間隔(秒)")

    parser_history = subparsers.add_parser("list", help="通知履歴を表示")
    parser_history.add_argument("--limit", type=int, default=10, help="表示件数")

    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリーを表示")

    args = parser.parse_args()

    if args.command == "log":
        for _ in range(args.count):
            msg = choose_fake_alert()
            send_notification(msg)
            log_alert(msg)
            if args.interval > 0 and _ < args.count - 1:
                time.sleep(args.interval)
    elif args.command == "list":
        show_history(args.limit)
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
