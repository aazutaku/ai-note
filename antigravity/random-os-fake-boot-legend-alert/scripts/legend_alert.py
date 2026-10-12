import sys
import time
import random
import argparse
import threading
import os

try:
    from plyer import notification
except ImportError:
    notification = None

LEGEND_MESSAGES = [
    "伝説のBIOSが今、あなたのコマンドを待っている。",
    "本日、選ばれし者としてOS界の伝説が始動。",
    "起動シーケンス：レジェンドモード発動中。",
    "謎のファームウェアから祝福の声が聞こえる。",
    "あなたの端末は伝説の領域に突入しました。",
    "OSの深淵からレジェンドコードが現れた。",
    "伝説のカーネルが静かに目覚める。",
    "BIOSの声があなたに語りかけている。",
    "選ばれし者のみが知る起動の儀式が始まる。",
    "OS界の神話がいま再誕する。"
]

TRIGGER_KEYWORDS = ["os", "起動", "bios", "伝説", "レジェンド", "シーケンス", "boot", "legend", "firmware", "カーネル"]

LOG_FILE = os.path.expanduser("~/.legend_alert.log")


def log_message(msg):
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")
    except Exception as e:
        pass  # ログ失敗は無視


def show_notification(msg):
    if notification is not None:
        try:
            notification.notify(
                title="OS LEGEND ALERT",
                message=msg,
                app_name="LegendAlert",
                timeout=6
            )
        except Exception as e:
            print(f"[OS LEGEND ALERT] {msg}")
    else:
        print(f"[OS LEGEND ALERT] {msg}")


def random_legend_alert():
    msg = random.choice(LEGEND_MESSAGES)
    show_notification(msg)
    log_message(msg)


def semantic_match(text):
    lower = text.lower()
    for kw in TRIGGER_KEYWORDS:
        if kw in lower:
            return True
    return False


def alert_loop(interval_min=600, interval_max=1800, stop_event=None):
    while not (stop_event and stop_event.is_set()):
        wait = random.randint(interval_min, interval_max)
        time.sleep(wait)
        random_legend_alert()


def cmd_log(args):
    if not os.path.isfile(LOG_FILE):
        print("No legend alert logs found.")
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())

def cmd_list(args):
    for msg in LEGEND_MESSAGES:
        print(f"- {msg}")

def cmd_summary(args):
    count = 0
    if os.path.isfile(LOG_FILE):
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            count = sum(1 for _ in f)
    print(f"Total legend alerts triggered: {count}")

def cmd_test(args):
    random_legend_alert()

def cmd_semantic(args):
    if semantic_match(args.text):
        random_legend_alert()
    else:
        print("No legend alert triggered.")

def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Boot Legend Alert Skill")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser("log", help="Show legend alert logs")
    parser_log.set_defaults(func=cmd_log)

    parser_list = subparsers.add_parser("list", help="List all possible legend messages")
    parser_list.set_defaults(func=cmd_list)

    parser_summary = subparsers.add_parser("summary", help="Show alert summary")
    parser_summary.set_defaults(func=cmd_summary)

    parser_test = subparsers.add_parser("test", help="Trigger a test legend alert")
    parser_test.set_defaults(func=cmd_test)

    parser_semantic = subparsers.add_parser("semantic", help="Trigger alert if text matches legend keywords")
    parser_semantic.add_argument("text", type=str, help="Input text to check for legend trigger")
    parser_semantic.set_defaults(func=cmd_semantic)

    parser_loop = subparsers.add_parser("loop", help="Run background legend alert loop")
    parser_loop.add_argument("--min", type=int, default=600, help="Minimum interval (seconds)")
    parser_loop.add_argument("--max", type=int, default=1800, help="Maximum interval (seconds)")
    parser_loop.set_defaults(func=None)

    args = parser.parse_args()

    if args.command == "loop":
        stop_event = threading.Event()
        try:
            alert_loop(interval_min=args.min, interval_max=args.max, stop_event=stop_event)
        except KeyboardInterrupt:
            print("\nLegend alert loop stopped.")
    elif hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
