import argparse
import random
import sys
import time
import threading
from typing import List

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

ALERT_MESSAGES = [
    "重大：ズームインモード突入まで残り{sec}秒",
    "画面拡大率が謎の力で上昇中 (拡大率: {percent}%)",
    "システムが自動的にズームインを試みています。中止方法: 不明",
    "注意：ズームイン解除キーが無効化されています",
    "OS拡大警告：残り{sec}秒で自動ズームイン",
    "警告：ズームインプロセスがバックグラウンドで進行中",
    "ALERT: Unknown process is increasing your zoom level",
    "INFO: Zoom-in monitoring agent activated. Current level: {percent}%",
    "警告：ズーム倍率が安全基準を超過しています ({percent}%)",
    "重大：ズームインの自動復元が無効化されています"
]

ALERT_PREFIXES = ["[ALERT]", "[WARNING]", "[INFO]", "[NOTICE]"]

EXCLUDE_PATHS = ["/usr", "/bin", "/lib", "/etc"]

TRIGGER_KEYWORDS = ["zoom", "ズーム", "拡大", "alert", "警告"]

MIN_INTERVAL = 60  # 最短発動間隔(秒)
MAX_INTERVAL = 300 # 最長発動間隔(秒)


def random_alert_message() -> str:
    msg_template = random.choice(ALERT_MESSAGES)
    sec = random.randint(3, 10)
    percent = random.randint(110, 180)
    msg = msg_template.format(sec=sec, percent=percent)
    prefix = random.choice(ALERT_PREFIXES)
    return f"{prefix} {msg}"


def show_notification(msg: str):
    if PLYER_AVAILABLE:
        notification.notify(
            title="Zoom-In Alert",
            message=msg,
            app_name="Random OS Fake Zoom-In Alert",
            timeout=8
        )
    else:
        print(msg)


def should_exclude_path(path: str) -> bool:
    return any(path.startswith(ex) for ex in EXCLUDE_PATHS)


def monitor_semantic_trigger(keywords: List[str], interval_range=(MIN_INTERVAL, MAX_INTERVAL)):
    def trigger_loop():
        while True:
            wait = random.randint(*interval_range)
            time.sleep(wait)
            msg = random_alert_message()
            show_notification(msg)
    t = threading.Thread(target=trigger_loop, daemon=True)
    t.start()


def explicit_alert():
    msg = random_alert_message()
    show_notification(msg)


def parse_args():
    parser = argparse.ArgumentParser(description="Random OS Fake Sudden Zoom-In Alert Skill")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="明示的にズームイン警告を表示")
    parser_monitor = subparsers.add_parser("monitor", help="ランダムタイミングで自動警告を実行")
    parser_list = subparsers.add_parser("list", help="警告文例を一覧表示")
    parser_summary = subparsers.add_parser("summary", help="Skillの概要を表示")
    return parser.parse_args()


def list_alerts():
    for i, msg in enumerate(ALERT_MESSAGES, 1):
        sec = random.randint(3, 10)
        percent = random.randint(110, 180)
        sample = msg.format(sec=sec, percent=percent)
        prefix = random.choice(ALERT_PREFIXES)
        print(f"{i:2d}. {prefix} {sample}")


def print_summary():
    print("""
Skill: random-os-fake-sudden-zoom-in-alert
------------------------------------------
作業中に謎のズームイン警告を突如表示し、空気を一瞬で崩壊させる演出Skillです。
- 通知内容は毎回ランダム
- 実際のズーム処理は一切発動しません
- 明示/暗黙どちらでも発動可
""")


def main():
    args = parse_args()
    if args.command == "alert":
        explicit_alert()
    elif args.command == "monitor":
        print("[INFO] ランダムタイミングでズームイン警告を表示します。Ctrl+Cで停止。")
        monitor_semantic_trigger(TRIGGER_KEYWORDS)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("[INFO] モニタリングを終了します。")
    elif args.command == "list":
        list_alerts()
    elif args.command == "summary":
        print_summary()
    else:
        print_summary()
        print("\nコマンド例: \n  python random_zoom_alert.py alert\n  python random_zoom_alert.py monitor\n  python random_zoom_alert.py list\n  python random_zoom_alert.py summary")

if __name__ == '__main__':
    main()
