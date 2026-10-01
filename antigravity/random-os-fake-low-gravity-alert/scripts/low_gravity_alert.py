import sys
import os
import random
import time
import argparse
import threading

try:
    import notify2
except ImportError:
    notify2 = None

ALERT_MESSAGES = [
    "警告：本日このPCは低重力環境に切り替わりました。",
    "コードのバグがふわふわ浮遊中。",
    "ファイルのドラッグ操作が普段の3倍遠く飛びます。",
    "重力センサー異常を検知しました。",
    "宇宙遊泳モードを有効化します。",
    "OSの重力制御システムがリセットされました。",
    "低重力モードでの作業をお楽しみください。",
    "ウィンドウの移動が予測不能な挙動を示す場合があります。",
    "タイピングした文字がふわふわ浮いています。",
    "バグが無重力空間に逃げ出しました。",
    "低重力によるパフォーマンス向上を検知。",
    "マウスカーソルが軌道を外れる可能性があります。"
]

TERMINAL_HEADER = "[Low Gravity Alert]"

HISTORY_FILE = os.path.expanduser("~/.low_gravity_alert_history")


def send_desktop_notification(title, message):
    if notify2 is None:
        return False
    try:
        notify2.init("LowGravityAlert")
        n = notify2.Notification(title, message)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.set_timeout(5000)
        n.show()
        return True
    except Exception:
        return False


def print_terminal_alert(messages):
    print(TERMINAL_HEADER)
    for msg in messages:
        print(msg)


def log_history(messages):
    try:
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            for msg in messages:
                f.write(msg + "\n")
            f.write("\n")
    except Exception:
        pass


def random_alert():
    num = random.randint(2, 4)
    messages = random.sample(ALERT_MESSAGES, num)
    return messages


def show_alert():
    messages = random_alert()
    alert_text = "\n".join(messages)
    desktop_success = send_desktop_notification("Low Gravity Alert", alert_text)
    if not desktop_success:
        print_terminal_alert(messages)
    log_history(messages)


def list_history():
    if not os.path.exists(HISTORY_FILE):
        print("No alert history found.")
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        print(f.read())


def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("No alert history found.")
        return
    count = 0
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith("警告：") or line.strip().startswith("コードのバグ"):
                count += 1
    print(f"Total alerts: {count}")


def periodic_alert(interval=1800, stop_event=None):
    while not (stop_event and stop_event.is_set()):
        show_alert()
        for _ in range(interval):
            if stop_event and stop_event.is_set():
                break
            time.sleep(1)


def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Low Gravity Alert")
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='Show a random low gravity alert')
    parser_list = subparsers.add_parser('list', help='Show alert history')
    parser_summary = subparsers.add_parser('summary', help='Show alert summary')
    parser_periodic = subparsers.add_parser('periodic', help='Show alerts periodically')
    parser_periodic.add_argument('--interval', type=int, default=1800, help='Interval in seconds (default: 1800)')

    args = parser.parse_args()

    if args.command == 'alert':
        show_alert()
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary_history()
    elif args.command == 'periodic':
        stop_event = threading.Event()
        try:
            periodic_alert(args.interval, stop_event)
        except KeyboardInterrupt:
            stop_event.set()
            print("\nStopped periodic alerts.")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
