import sys
import random
import subprocess
import argparse
import os
import platform
from datetime import datetime

TAROT_MESSAGES = [
    "愚者が新たな旅路に出る。今日のcommitは冒険の始まり。",
    "運命の輪が静かに回転した。流れに身を任せよ。",
    "塔が崩れた。大胆な変更に注意。",
    "世界のカードが現れた。完璧な仕上がりに近づいている。",
    "隠者が静かに微笑む。内省のcommit。",
    "死神が通り過ぎた。古いコードに別れを告げよ。",
    "恋人たちが手を取り合う。協力が吉。",
    "太陽が輝く。明るい未来が見える。",
    "月が曇る。見えないバグに注意。",
    "審判の時。レビューを恐れるな。",
    "力のカードが出た。自信を持ってpushせよ。",
    "節制の天使が現れた。冷静な判断を。",
    "正義の天秤が揺れる。コミットメッセージは正直に。",
    "戦車が突き進む。勢いのある開発。",
    "女帝が微笑む。豊かな実装。",
    "魔術師が現れる。新しい技術に挑戦せよ。",
    "吊るされた男。辛抱の時。",
    "悪魔が囁く。誘惑に負けるな。",
    "星が瞬く。希望を持て。",
    "皇帝が命じる。リーダーシップを発揮せよ。"
]

LOG_FILE = os.path.expanduser("~/.commit_fortune_tarot.log")


def select_random_message():
    return random.choice(TAROT_MESSAGES)


def notify_desktop(message):
    system = platform.system()
    title = "Tarot Fortune"
    try:
        if system == "Linux":
            subprocess.run(["notify-send", title, message], check=True)
        elif system == "Darwin":
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        else:
            # Windowsやその他はターミナル出力のみ
            print(f"[{title}] {message}")
    except Exception as e:
        print(f"[Tarot Fortune] {message}")
        print(f"[Tarot Notifier Error] 通知送信に失敗: {e}")


def log_message(message):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()} {message}\n")
    except Exception as e:
        print(f"[Tarot Notifier Error] ログ保存に失敗: {e}")


def show_fortune():
    message = select_random_message()
    notify_desktop(message)
    log_message(message)


def list_log():
    if not os.path.exists(LOG_FILE):
        print("ログファイルが存在しません。")
        return
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines[-20:]:
            print(line.strip())
    except Exception as e:
        print(f"[Tarot Notifier Error] ログ読み込み失敗: {e}")


def summary_log():
    if not os.path.exists(LOG_FILE):
        print("ログファイルが存在しません。")
        return
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        total = len(lines)
        by_card = {}
        for line in lines:
            for card in TAROT_MESSAGES:
                if card[:8] in line:
                    by_card[card[:8]] = by_card.get(card[:8], 0) + 1
        print(f"合計 {total} 回のタロット通知が記録されています。\n")
        for k, v in by_card.items():
            print(f"{k}: {v} 回")
    except Exception as e:
        print(f"[Tarot Notifier Error] サマリ集計失敗: {e}")


def parse_args():
    parser = argparse.ArgumentParser(description="Git commit時にタロット風占い通知を表示するスクリプト")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("fortune", help="ランダムなタロット通知を表示")
    subparsers.add_parser("list", help="最近のタロット通知ログを表示")
    subparsers.add_parser("summary", help="タロット通知のサマリを集計表示")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "fortune" or args.command is None:
        show_fortune()
    elif args.command == "list":
        list_log()
    elif args.command == "summary":
        summary_log()
    else:
        print("不明なコマンドです。--help を参照してください。")

if __name__ == "__main__":
    main()
