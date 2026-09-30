#!/usr/bin/env python3
import os
import sys
import random
import argparse
import subprocess
import platform
from datetime import datetime

TAROT_CARDS = [
    ("愚者", "愚者が新たな旅路に出る。大胆な変更が吉と出るか凶と出るか…"),
    ("魔術師", "魔術師が知恵を授ける。新しいアイデアを試す好機。"),
    ("女教皇", "女教皇が静かに見守る。冷静なレビューを。"),
    ("女帝", "女帝が豊かさをもたらす。コードの実りを期待せよ。"),
    ("皇帝", "皇帝が規律を求める。規約違反に注意！"),
    ("法王", "法王が導く。ベストプラクティスを忘れずに。"),
    ("恋人", "恋人たちが調和をもたらす。チームワークが吉。"),
    ("戦車", "戦車が突き進む。勢いに任せてコミット！"),
    ("力", "力が試される。難所を乗り越えよ。"),
    ("隠者", "隠者が問いかける。自己レビューの時間。"),
    ("運命の輪", "運命の輪が回り始めた。今日のコミットは大吉！"),
    ("正義", "正義が裁く。テストを怠るな。"),
    ("吊るされた男", "吊るされた男が忍耐を示す。CIの待ち時間に耐えよ。"),
    ("死神", "死神が現れる。大胆なリファクタリングの予兆。"),
    ("節制", "節制がバランスを保つ。無理なPushは禁物。"),
    ("悪魔", "悪魔が囁く。技術的負債に注意。"),
    ("塔", "塔が崩れる。バグの予感。慎重に進め！"),
    ("星", "星が輝く。希望を持って進もう。"),
    ("月", "月が曇る。迷いが生じるかも。"),
    ("太陽", "太陽が輝く。最高の一日になるだろう。"),
    ("審判", "審判が下る。レビュー依頼を忘れずに。"),
    ("世界", "世界が完成する。リリースの予感！")
]

HISTORY_FILE = os.path.expanduser("~/.commit_fortune_tarot_history.log")


def pick_tarot_fortune():
    card = random.choice(TAROT_CARDS)
    return f"[Tarot Fortune] {card[1]}"


def notify(message):
    system = platform.system()
    if system == "Linux":
        try:
            subprocess.run(["notify-send", message], check=True)
        except Exception:
            pass  # fallback to print
    elif system == "Darwin":
        script = f'display notification "{message}" with title "Tarot Fortune"'
        try:
            subprocess.run(["osascript", "-e", script], check=True)
        except Exception:
            pass
    elif system == "Windows":
        try:
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, message, "Tarot Fortune", 1)
        except Exception:
            pass
    print(message)


def log_history(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{now}\t{message}\n")


def list_history(limit=10):
    if not os.path.exists(HISTORY_FILE):
        print("No history yet.")
        return
    with open(HISTORY_FILE, encoding="utf-8") as f:
        lines = f.readlines()[-limit:]
        for line in lines:
            print(line.strip())


def summary():
    if not os.path.exists(HISTORY_FILE):
        print("No history yet.")
        return
    counter = {}
    with open(HISTORY_FILE, encoding="utf-8") as f:
        for line in f:
            for card, msg in TAROT_CARDS:
                if msg in line:
                    counter[card] = counter.get(card, 0) + 1
    print("--- Tarot Card Summary ---")
    for card, count in sorted(counter.items(), key=lambda x: -x[1]):
        print(f"{card}: {count}")


def main():
    parser = argparse.ArgumentParser(description="Git commit時にタロット風占い通知を表示するスクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser("log", help="占いを1回実行し通知")
    parser_list = subparsers.add_parser("list", help="過去の占い履歴を表示")
    parser_list.add_argument("-n", "--num", type=int, default=10, help="表示件数")
    parser_summary = subparsers.add_parser("summary", help="カードごとの出現回数を集計")

    args = parser.parse_args()
    if args.command == "log" or args.command is None:
        message = pick_tarot_fortune()
        notify(message)
        log_history(message)
    elif args.command == "list":
        list_history(args.num)
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
