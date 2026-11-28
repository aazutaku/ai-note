import random
import time
import sys
import argparse
import platform
import subprocess
from threading import Thread
from datetime import datetime

PROPHECY_TEMPLATES = [
    "{direction}の{place}に{event}",
    "{direction}の{place}で{phenomenon}が兆す",
    "{place}の奥底に{legend}が眠る",
    "{direction}の{place}に{creature}の影動く",
    "{direction}の{place}、{event}の予兆あり",
    "{place}にて{phenomenon}、時至る",
    "{direction}の{place}に伝説の{person}現る",
    "{place}の門が{phenomenon}により開かれる"
]

DIRECTIONS = ["北", "南", "東", "西", "中央"]
PLACES = [
    "リポジトリ", "コード砂漠", "バイナリ荒野", "CI/CD神殿", "関数の森",
    "テスト沼", "Issue洞窟", "Pull Request砦", "デバッグ渓谷", "ビルド塔"
]
EVENTS = [
    "巨大バグの影動く", "未踏の関数現る", "レビュアー現る", "未解決のPRが眠る",
    "新たな警告生まれる", "謎のエラーが囁く", "神秘のコミット記される",
    "伝説のマージが成就する", "謎のリリースが近づく", "古代のLint警告蘇る"
]
PHENOMENA = [
    "バグの嵐", "警告の雨", "静寂の時", "レビューの風", "マージの兆し",
    "CIの叫び", "コードのざわめき", "PRの波", "Issueのざわつき"
]
LEGENDS = [
    "レビュアー", "バグハンター", "コミッター", "マージ神", "テスト仙人"
]
CREATURES = [
    "バグ", "レビュアー", "コミッター", "CI/CD精霊", "Lintの精"
]
PERSONS = [
    "レビュアー", "バグハンター", "マージ神", "テスト仙人", "コード賢者"
]


def generate_prophecy():
    template = random.choice(PROPHECY_TEMPLATES)
    prophecy = template.format(
        direction=random.choice(DIRECTIONS),
        place=random.choice(PLACES),
        event=random.choice(EVENTS),
        phenomenon=random.choice(PHENOMENA),
        legend=random.choice(LEGENDS),
        creature=random.choice(CREATURES),
        person=random.choice(PERSONS)
    )
    return prophecy


def notify_os(title, message):
    system = platform.system()
    try:
        if system == "Darwin":  # macOS
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            subprocess.run(["notify-send", title, message], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=6, threaded=True)
            except ImportError:
                print("win10toastが見つかりません。pip install win10toast でインストールしてください。", file=sys.stderr)
        else:
            print(f"[{title}]\n{message}")
    except Exception as e:
        print(f"通知失敗: {e}", file=sys.stderr)
        print(f"[{title}]\n{message}")


def prophecy_alert_loop(interval=600, stop_after=None):
    start = time.time()
    count = 0
    while True:
        prophecy = generate_prophecy()
        notify_os("OS Ancient Prophecy Alert", prophecy)
        count += 1
        if stop_after and count >= stop_after:
            break
        if stop_after and (time.time() - start) > stop_after * interval:
            break
        time.sleep(interval)


def print_prophecy():
    prophecy = generate_prophecy()
    print(f"[OS Ancient Prophecy Alert]\n{prophecy}")


def list_prophecies(n=5):
    for _ in range(n):
        print(f"[OS Ancient Prophecy Alert]\n{generate_prophecy()}")


def summary():
    print("Skill: random-os-fake-ancient-prophecy-alert")
    print("用途: OS通知やターミナルに意味深な古代預言風メッセージをランダム表示")
    print("通知テンプレート数:", len(PROPHECY_TEMPLATES))
    print("方向数:", len(DIRECTIONS))
    print("場所数:", len(PLACES))
    print("イベント数:", len(EVENTS))
    print("現象数:", len(PHENOMENA))
    print("伝説数:", len(LEGENDS))
    print("生物数:", len(CREATURES))
    print("人物数:", len(PERSONS))


def main():
    parser = argparse.ArgumentParser(description="OS Ancient Prophecy Alert")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="今すぐ預言を通知する")
    parser_alert.add_argument("--os", action="store_true", help="OS通知として表示")

    parser_loop = subparsers.add_parser("loop", help="定期的に預言を通知する")
    parser_loop.add_argument("--interval", type=int, default=600, help="通知間隔(秒)")
    parser_loop.add_argument("--count", type=int, default=None, help="通知回数(省略時は無限)")

    parser_list = subparsers.add_parser("list", help="ランダム預言を複数表示")
    parser_list.add_argument("-n", type=int, default=5, help="表示件数")

    parser_summary = subparsers.add_parser("summary", help="Skillの概要を表示")

    args = parser.parse_args()

    if args.command == "alert":
        prophecy = generate_prophecy()
        if args.os:
            notify_os("OS Ancient Prophecy Alert", prophecy)
        else:
            print(f"[OS Ancient Prophecy Alert]\n{prophecy}")
    elif args.command == "loop":
        prophecy_alert_loop(interval=args.interval, stop_after=args.count)
    elif args.command == "list":
        list_prophecies(args.n)
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
