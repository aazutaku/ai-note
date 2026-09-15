import sys
import time
import random
import argparse
import platform
import subprocess
from typing import List

PROPHECY_TEMPLATES = [
    "西のウィンドウズに赤きバグ現る時、選ばれし者はリブートせよ。",
    "2024年、ファイル名にパワー宿る。",
    "sudoの呪文三度唱えし者、未知の権限を得るだろう。",
    "ターミナルに光差す時、隠されたプロセス目覚める。",
    "古きログファイルに真実は眠る。",
    "パスワード忘れし者、再び始まりの地へ戻るべし。",
    "カーネルの叫びが聞こえし夜、システムは揺らぐ。",
    "選ばれし者、configを書き換えよ。",
    "パーミッション拒まれし時、己を省みよ。",
    "未知のポート開かれし時、闇より使者現る。",
    "cronの鐘が三度鳴る時、スクリプトは蘇る。",
    "ディレクトリの奥底に、忘れられしreadme眠る。",
    "バージョンアップの風が吹く時、古きエラー蘇る。",
    "gitの迷宮に迷いし者、commitで光を見出す。",
    "セグメンテーションの壁を越えし者、無限のRAMを手にする。"
]

def generate_prophecy() -> str:
    return random.choice(PROPHECY_TEMPLATES)

def print_prophecy():
    msg = generate_prophecy()
    print("[OS Ancient Prophecy Alert]\n" + msg + "\n---")
    return msg

def notify_desktop(msg: str):
    sys_platform = platform.system()
    try:
        if sys_platform == "Darwin":  # macOS
            subprocess.run([
                "osascript", "-e",
                f'display notification "{msg}" with title "OS Ancient Prophecy Alert"'
            ], check=True)
        elif sys_platform == "Linux":
            subprocess.run([
                "notify-send", "OS Ancient Prophecy Alert", msg], check=True)
        elif sys_platform == "Windows":
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("OS Ancient Prophecy Alert", msg, duration=5)
        else:
            print("[通知未対応プラットフォーム]")
    except Exception as e:
        print(f"[通知エラー]: {e}")

def prophecy_loop(interval: int, desktop: bool, count: int):
    shown = 0
    try:
        while count == 0 or shown < count:
            msg = print_prophecy()
            if desktop:
                notify_desktop(msg)
            shown += 1
            if count == 0 or shown < count:
                time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[Prophecy Alert] 中断されました。")

def list_prophecies():
    print("# 予言テンプレート一覧:")
    for idx, p in enumerate(PROPHECY_TEMPLATES, 1):
        print(f"{idx}. {p}")

def summary():
    print("このSkillは、作業中に古代OS予言通知をランダムに生成・表示します。\n通知は毎回異なり、デスクトップ通知も対応可能。\n副作用ゼロ・データ損失なし。")

def parse_args():
    parser = argparse.ArgumentParser(description="OS Ancient Prophecy Alert: 古代OS予言通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="予言を即時または定期的に表示")
    parser_run.add_argument("--interval", type=int, default=0, help="繰り返し表示の間隔(秒)。0なら1回のみ")
    parser_run.add_argument("--desktop", action="store_true", help="デスクトップ通知も送信")
    parser_run.add_argument("--count", type=int, default=0, help="表示回数。0なら無限ループ")

    parser_list = subparsers.add_parser("list", help="予言テンプレート一覧を表示")
    parser_summary = subparsers.add_parser("summary", help="Skill概要を表示")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if args.command == "run":
        interval = args.interval if args.interval > 0 else 0
        count = args.count if args.count > 0 else 1 if interval == 0 else 0
        prophecy_loop(interval, args.desktop, count)
    elif args.command == "list":
        list_prophecies()
    elif args.command == "summary":
        summary()
    else:
        print("使い方: python prophecy_alert.py run|list|summary [--interval N] [--desktop] [--count N]")
