import os
import sys
import subprocess
import random
import shlex
import argparse
from pathlib import Path

SAMURAI_LINES = [
    "拙者、{cmd}の術を披露仕る！",
    "おぬし、{cmd}を使うとは、なかなかやりおる！",
    "この{cmd}、まこと見事なり！",
    "いざ、{cmd}、参る！",
    "拙者、{cmd}を実行仕る！",
    "{cmd}の極意、今ここに！",
    "{cmd}、その覚悟、しかと見届けた！",
    "{cmd}の構え、抜かりなし！",
    "{cmd}を打つその手並み、見事！",
    "{cmd}、拙者も手伝おうぞ！",
    "{cmd}、これぞ侍の道！",
    "{cmd}、これにて一件落着！",
    "{cmd}、お見事でござる！",
    "{cmd}、いざ尋常に勝負！",
    "{cmd}、この一太刀、受けてみよ！",
    "{cmd}、これぞ武士の誉れ！",
    "{cmd}、見事なり！",
    "{cmd}、拙者も感服仕った！",
    "{cmd}、これぞ時代劇の真骨頂！",
    "{cmd}、いざ参る！"
]

STATE_FILE = str(Path.home() / ".samurai_announcer_state")

EXCLUDE_COMMANDS = ["samurai_announce.py"]


def is_enabled():
    if not os.path.exists(STATE_FILE):
        return True
    try:
        with open(STATE_FILE, "r") as f:
            state = f.read().strip()
            return state == "on"
    except Exception:
        return True


def set_enabled(flag: bool):
    with open(STATE_FILE, "w") as f:
        f.write("on" if flag else "off")


def print_samurai_line(cmd):
    line = random.choice(SAMURAI_LINES)
    print(line.format(cmd=cmd))


def run_command(command):
    if not command:
        print("コマンドを指定してください。")
        return 1
    base_cmd = shlex.split(command)[0]
    if base_cmd in EXCLUDE_COMMANDS:
        # 自己呼び出し防止
        return subprocess.call(command, shell=True)
    if is_enabled():
        print_samurai_line(base_cmd)
    try:
        result = subprocess.run(command, shell=True)
        return result.returncode
    except Exception as e:
        print(f"実行中にエラー: {e}")
        return 1


def toggle():
    current = is_enabled()
    set_enabled(not current)
    print(f"侍ナレーション: {'有効' if not current else '無効'}になりました。")


def show_status():
    print(f"侍ナレーションは {'有効' if is_enabled() else '無効'}です。")


def main():
    parser = argparse.ArgumentParser(description="ターミナル侍ナレーター: コマンド実行時に侍風実況を添えます。")
    subparsers = parser.add_subparsers(dest="subcmd", help="サブコマンド")

    # run
    parser_run = subparsers.add_parser("run", help="コマンドを侍実況付きで実行")
    parser_run.add_argument("command", nargs=argparse.REMAINDER, help="実行するコマンド")

    # toggle
    parser_toggle = subparsers.add_parser("toggle", help="ON/OFF切替")

    # status
    parser_status = subparsers.add_parser("status", help="現在のON/OFF状態を表示")

    # list-lines
    parser_list = subparsers.add_parser("list-lines", help="侍セリフ一覧を表示")

    args = parser.parse_args()
    if args.subcmd == "run":
        cmd = " ".join(args.command)
        sys.exit(run_command(cmd))
    elif args.subcmd == "toggle":
        toggle()
    elif args.subcmd == "status":
        show_status()
    elif args.subcmd == "list-lines":
        for l in SAMURAI_LINES:
            print(l.format(cmd="<コマンド>"))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
