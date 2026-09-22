import sys
import os
import random
import time
import argparse
import platform
import subprocess
from datetime import datetime, timedelta

HEROES = [
    "伝説のデバッグ勇者『タカシ』",
    "コマンド使いのジョン",
    "リファクタリング忍者『サクラ』",
    "バーチャル管理者",
    "スクリプト魔術師",
    "バグハンター『リナ』",
    "メモリマスター『ケン』",
    "パッチの精霊『ミユキ』",
    "ネットワーク賢者『アレックス』",
    "シェルの魔王『カズ』"
]

MESSAGES = [
    "{hero}が参上しました！",
    "バグ討伐の時！“{hero}”が出動します。",
    "謎のOS公式「{hero}」があなたの作業を見守っています。",
    "{hero}が召喚されました。",
    "今こそバグ退治の時！“{hero}”が現れた！",
    "{hero}があなたのコードに加護を与えます。",
    "{hero}がログを監視中...",
    "{hero}が未解決のバグを追跡中です。",
    "{hero}が新たな知恵を授けに来ました。",
    "{hero}がターミナルに降臨！"
]

HISTORY_FILE = os.path.expanduser("~/.hero_summon_history.log")

# 通知をOSごとに送る
def send_notification(message):
    system = platform.system()
    try:
        if system == "Linux":
            subprocess.run(["notify-send", message], check=True)
        elif system == "Darwin":
            script = f'display notification "{message}" with title "OS通知"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("OS通知", message, duration=5)
            except ImportError:
                # Fallback: print to console
                print("[OS通知]", message)
        else:
            print("[OS通知]", message)
    except Exception as e:
        print(f"[通知失敗] {e}\n[OS通知] {message}")

# 英雄召喚メッセージ生成
def generate_message():
    hero = random.choice(HEROES)
    msg_template = random.choice(MESSAGES)
    return msg_template.format(hero=hero)

# 履歴保存
def log_history(message):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()}\t{message}\n")

# 履歴表示
def show_history(limit=10):
    if not os.path.exists(HISTORY_FILE):
        print("履歴はありません。")
        return
    with open(HISTORY_FILE, encoding="utf-8") as f:
        lines = f.readlines()[-limit:]
        for line in lines:
            print(line.strip())

# 履歴要約
def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴はありません。")
        return
    count = 0
    hero_count = {}
    with open(HISTORY_FILE, encoding="utf-8") as f:
        for line in f:
            count += 1
            for hero in HEROES:
                if hero in line:
                    hero_count[hero] = hero_count.get(hero, 0) + 1
    print(f"合計通知数: {count}")
    for hero, c in sorted(hero_count.items(), key=lambda x: -x[1]):
        print(f"{hero}: {c}回")

# ランダムな間隔で通知を送る
def random_notify_loop(min_sec=600, max_sec=3600, once=False):
    while True:
        message = generate_message()
        send_notification(message)
        log_history(message)
        if once:
            break
        wait_sec = random.randint(min_sec, max_sec)
        time.sleep(wait_sec)

def main():
    parser = argparse.ArgumentParser(description="謎のOS英雄召喚通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    notify_parser = subparsers.add_parser("notify", help="今すぐ英雄召喚通知を1回だけ送る")
    loop_parser = subparsers.add_parser("loop", help="ランダムな間隔で通知を送り続ける")
    loop_parser.add_argument("--min", type=int, default=600, help="通知間隔の最小秒数 (デフォルト600)")
    loop_parser.add_argument("--max", type=int, default=3600, help="通知間隔の最大秒数 (デフォルト3600)")

    log_parser = subparsers.add_parser("log", help="通知履歴を表示する")
    log_parser.add_argument("--limit", type=int, default=10, help="表示件数 (デフォルト10)")

    summary_parser = subparsers.add_parser("summary", help="通知履歴の要約を表示する")

    args = parser.parse_args()

    if args.command == "notify":
        message = generate_message()
        send_notification(message)
        log_history(message)
    elif args.command == "loop":
        try:
            random_notify_loop(min_sec=args.min, max_sec=args.max)
        except KeyboardInterrupt:
            print("\n通知ループを終了します。")
    elif args.command == "log":
        show_history(limit=args.limit)
    elif args.command == "summary":
        summary_history()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
