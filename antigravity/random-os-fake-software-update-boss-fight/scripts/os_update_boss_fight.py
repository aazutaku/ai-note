import sys
import time
import random
import argparse
import platform
import subprocess
from datetime import datetime

BATTLE_EVENTS = [
    ("勇者アップデーターがバグ魔王に挑む！", 0),
    ("バグ魔王の逆襲！", 20),
    ("勇者、パッチの剣を抜く！", 40),
    ("バグ魔王、致命的なエラー波を放つ！", 60),
    ("勇者、バグ魔王にクリティカルヒット！", 80),
    ("バグ魔王、最後の抵抗！", 90)
]

VICTORY_LINES = [
    "アップデート完了：勇者の勝利！",
    "アップデート成功！バグ魔王を討伐しました。",
    "アップデート勇者、伝説のバグ魔王を撃破！"
]

DEFEAT_LINES = [
    "アップデート失敗：全滅...バグ魔王の勝利。",
    "バグ魔王の猛攻！システムは全滅した...",
    "アップデート勇者、力尽きる。バグ魔王の逆襲成功。"
]

PROGRESS_BAR_LENGTH = 30

LOG_FILE = "boss_fight_update.log"


def notify(title, message):
    system = platform.system()
    try:
        if system == "Darwin":
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Windows":
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=5)
        elif system == "Linux":
            subprocess.run(["notify-send", title, message], check=True)
        else:
            print(f"[{title}] {message}")
    except Exception as e:
        print(f"通知エラー: {e}")


def print_progress_bar(progress, total, event):
    percent = int((progress / total) * 100)
    filled = int(PROGRESS_BAR_LENGTH * progress // total)
    bar = "█" * filled + "-" * (PROGRESS_BAR_LENGTH - filled)
    print(f"[{bar}] {percent}% {event}")


def random_battle_events():
    events = list(BATTLE_EVENTS)
    random.shuffle(events[1:])  # 最初は固定、以降はランダム
    return events


def battle_sequence(verbose=False):
    events = random_battle_events()
    total = 100
    progress = 0
    logs = []
    for i, (event, step) in enumerate(events):
        next_progress = step if step > progress else progress + random.randint(10, 25)
        next_progress = min(next_progress, total)
        if verbose:
            print_progress_bar(next_progress, total, event)
        notify("OSアップデート進行中", f"{event} 進捗 {next_progress}%")
        logs.append(f"{datetime.now().isoformat()} {event} 進捗 {next_progress}%")
        time.sleep(random.uniform(0.8, 1.8))
        progress = next_progress
    # ラストイベント
    outcome = random.choice(["victory", "defeat"]) if random.random() < 0.85 else "defeat"
    if outcome == "victory":
        line = random.choice(VICTORY_LINES)
    else:
        line = random.choice(DEFEAT_LINES)
    if verbose:
        print_progress_bar(total, total, line)
    notify("OSアップデート完了", line)
    logs.append(f"{datetime.now().isoformat()} {line}")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        for l in logs:
            f.write(l + "\n")
    return outcome


def show_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[-15:]:
                print(line.strip())
    except FileNotFoundError:
        print("まだバトルログがありません。")


def summary():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        total = len([l for l in lines if "進捗" in l])
        victories = sum(1 for l in lines if "勝利" in l or "撃破" in l)
        defeats = sum(1 for l in lines if "全滅" in l or "失敗" in l)
        print(f"バトル回数: {total} 回")
        print(f"勇者の勝利: {victories} 回")
        print(f"バグ魔王の勝利: {defeats} 回")
    except FileNotFoundError:
        print("まだバトルログがありません。")


def main():
    parser = argparse.ArgumentParser(description="OSアップデートRPGバトル通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_battle = subparsers.add_parser("battle", help="バトルを開始する")
    parser_battle.add_argument("--verbose", action="store_true", help="進捗バーをターミナルに表示")

    parser_log = subparsers.add_parser("log", help="直近のバトルログを表示")
    parser_summary = subparsers.add_parser("summary", help="バトル勝敗サマリーを表示")

    args = parser.parse_args()
    if args.command == "battle":
        battle_sequence(verbose=args.verbose)
    elif args.command == "log":
        show_log()
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
