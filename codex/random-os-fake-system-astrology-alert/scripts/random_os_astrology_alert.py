import argparse
import random
import sys
import time
import threading
from datetime import datetime
import platform
import subprocess

ASTRO_COMMANDS = [
    "ls", "cd", "grep", "cat", "rm", "mkdir", "ps", "kill", "top", "chmod", "chown", "df", "du", "find", "whoami", "echo", "ping", "scp", "ssh", "curl", "wget", "tar", "zip", "unzip", "nano", "vim", "git", "make", "python", "node", "docker", "systemctl"
]

PLANETS = [
    "水星", "金星", "火星", "木星", "土星", "天王星", "海王星", "冥王星"
]

ASTRO_EVENTS = [
    "水星逆行中につき、バグの再発に気をつけてください。",
    "金星がネットワーク層を通過中。通信エラーに要注意。",
    "火星がプロセス管理に影響を与えています。killコマンドは慎重に。",
    "土星がストレージ領域を監視中。バックアップ推奨。",
    "木星がメモリ空間を拡大中。大きな配列に挑戦を。",
    "天王星がシェルの履歴を混乱させています。コマンドの再実行に注意。",
    "海王星がネットワークの深海を揺らしています。遅延に注意。",
    "冥王星がプロセスの終焉を告げています。ゾンビプロセスに気をつけて。"
]

LUCKY_MESSAGES = [
    "今日のラッキーコマンドは: {cmd}",
    "本日の守護コマンド: {cmd}",
    "宇宙があなたに囁くコマンド: {cmd}",
    "今日の運勢を支えるコマンド: {cmd}"
]

ADVICE_MESSAGES = [
    "今日の運勢: システムアップデートは控えめに。",
    "バックアップを忘れずに。",
    "新しいパッケージのインストールは慎重に。",
    "ログの確認で運気上昇。",
    "設定ファイルの見直しが吉。",
    "今日は新しいスクリプトを書くと良いでしょう。",
    "コマンド履歴を眺めてみよう。",
    "未使用のプロセスを整理すると運気アップ。"
]

HEADER = "[OS Astrology Alert]"


def random_astrology_message():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cmd = random.choice(ASTRO_COMMANDS)
    planet = random.choice(PLANETS)
    event = random.choice(ASTRO_EVENTS)
    lucky = random.choice(LUCKY_MESSAGES).format(cmd=cmd)
    advice = random.choice(ADVICE_MESSAGES)
    lines = [
        f"{HEADER} {now}",
        lucky,
        event,
        f"このマシンの守護惑星は{planet}です。",
        advice
    ]
    return "\n".join(lines)


def show_notification(message):
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "OS Astrology Alert"'
            ], check=True)
        elif system == "Linux":
            subprocess.run([
                "notify-send", "OS Astrology Alert", message
            ], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("OS Astrology Alert", message, duration=8)
            except ImportError:
                print("win10toastが見つかりません。ターミナルに出力します。")
                print(message)
        else:
            print(message)
    except Exception as e:
        print("通知の表示に失敗しました。ターミナルに出力します。")
        print(message)


def print_message():
    msg = random_astrology_message()
    print(msg)
    show_notification(msg)


def alert_loop(interval_min=600, interval_max=1800):
    try:
        while True:
            wait = random.randint(interval_min, interval_max)
            time.sleep(wait)
            print_message()
    except KeyboardInterrupt:
        print("\n[OS Astrology Alert] 自動通知を停止しました。")


def main():
    parser = argparse.ArgumentParser(description="OS風システム占星術通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_once = subparsers.add_parser("once", help="1回だけ通知を表示")
    parser_loop = subparsers.add_parser("loop", help="ランダムな間隔で自動通知")
    parser_loop.add_argument("--min", type=int, default=600, help="最小通知間隔(秒)")
    parser_loop.add_argument("--max", type=int, default=1800, help="最大通知間隔(秒)")
    parser_test = subparsers.add_parser("test", help="テスト用に即時で複数回通知")
    parser_test.add_argument("--count", type=int, default=3, help="通知回数")
    parser_test.add_argument("--interval", type=int, default=2, help="通知間隔(秒)")

    args = parser.parse_args()

    if args.command == "once":
        print_message()
    elif args.command == "loop":
        alert_loop(interval_min=args.min, interval_max=args.max)
    elif args.command == "test":
        for _ in range(args.count):
            print_message()
            time.sleep(args.interval)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
