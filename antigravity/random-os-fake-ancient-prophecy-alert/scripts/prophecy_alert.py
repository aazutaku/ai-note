import sys
import os
import random
import time
import argparse
import platform
import subprocess
from datetime import datetime

PROPHECY_TEMPLATES = [
    "西のウィンドウズに{color}バグ現る時、選ばれし者はリブートせよ。",
    "{year}年、ファイル名にパワー宿る。拡張子を軽んずるなかれ。",
    "東のターミナルに白きカーソル瞬く時、更新の時来たる。",
    "バックアップ忘れし者、永劫のループに囚われん。",
    "sudoの力、慎みて使うべし。",
    "ログの海に沈みしエラー、夜明けと共に浮上せん。",
    "{weekday}、選ばれし者はコンパイルに挑むべし。",
    "古のシェルスクリプト、{os}にて再び蘇る。",
    "バージョン管理を怠る者、コードの迷宮に迷い込まん。",
    "西風が吹く時、{user}のホームに新たなファイル生まれん。",
    "{hour}時、プロセスの彼方より未知の警告現る。",
    "ディスクの空き、心せよ。満たされし時、災い訪れん。",
    "パーミッションの門、正しき者にのみ開かれん。",
    "{os}の神託、今ここに示されん。"
]

COLORS = ["赤き", "蒼き", "黒き", "白き", "金色の", "銀色の"]


def generate_prophecy():
    now = datetime.now()
    template = random.choice(PROPHECY_TEMPLATES)
    prophecy = template.format(
        color=random.choice(COLORS),
        year=now.year,
        weekday=["日曜", "月曜", "火曜", "水曜", "木曜", "金曜", "土曜"][now.weekday()],
        os=platform.system(),
        user=os.getenv("USER") or os.getenv("USERNAME") or "使徒",
        hour=now.hour
    )
    return prophecy


def notify_terminal(message):
    sys.stdout.write(f"[古代OS予言] {message}\n")
    sys.stdout.flush()


def notify_desktop(message):
    system = platform.system()
    if system == "Linux":
        try:
            subprocess.run([
                "notify-send", "古代OS予言", message
            ], check=True)
        except Exception:
            pass  # 通知失敗時は黙殺
    elif system == "Darwin":
        osa_script = f'display notification "{message}" with title "古代OS予言"'
        try:
            subprocess.run([
                "osascript", "-e", osa_script], check=True)
        except Exception:
            pass
    elif system == "Windows":
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast("古代OS予言", message, duration=5)
        except Exception:
            pass
    # それ以外は何もしない


def log_prophecy(message, log_path="~/.prophecy_alert.log"):
    path = os.path.expanduser(log_path)
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()} {message}\n")
    except Exception:
        pass


def list_log(log_path="~/.prophecy_alert.log", tail=10):
    path = os.path.expanduser(log_path)
    if not os.path.exists(path):
        print("ログファイルが存在しません。")
        return
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[-tail:]:
            print(line.strip())


def summary_log(log_path="~/.prophecy_alert.log"):
    path = os.path.expanduser(log_path)
    if not os.path.exists(path):
        print("ログファイルが存在しません。")
        return
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    print(f"記録された予言数: {len(lines)}")
    if lines:
        print(f"最新の予言: {lines[-1].strip()}")


def main():
    parser = argparse.ArgumentParser(description="謎のOS古代予言通知スキル")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="予言をランダム発動し通知")
    parser_alert.add_argument("--desktop", action="store_true", help="デスクトップ通知も行う")
    parser_alert.add_argument("--log", action="store_true", help="ログファイルに記録")

    parser_list = subparsers.add_parser("list", help="過去の予言ログを表示")
    parser_list.add_argument("--tail", type=int, default=10, help="末尾N件のみ表示")

    parser_summary = subparsers.add_parser("summary", help="予言ログの概要を表示")

    args = parser.parse_args()

    if args.command == "alert":
        message = generate_prophecy()
        notify_terminal(message)
        if args.desktop:
            notify_desktop(message)
        if args.log:
            log_prophecy(message)
    elif args.command == "list":
        list_log(tail=args.tail)
    elif args.command == "summary":
        summary_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
