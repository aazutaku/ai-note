import sys
import random
import time
import argparse
import threading
import platform

try:
    if platform.system() == 'Darwin':
        from subprocess import call
        NOTIFY_FUNC = lambda title, msg: call(['osascript', '-e', f'display notification "{msg}" with title "{title}"'])
    elif platform.system() == 'Linux':
        import notify2
        notify2_inited = False
        def linux_notify(title, msg):
            global notify2_inited
            if not notify2_inited:
                notify2.init('LegendaryDrop')
                notify2_inited = True
            n = notify2.Notification(title, msg)
            n.show()
        NOTIFY_FUNC = linux_notify
    elif platform.system() == 'Windows':
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        NOTIFY_FUNC = lambda title, msg: toaster.show_toast(title, msg, duration=5, threaded=True)
    else:
        NOTIFY_FUNC = lambda title, msg: print(f"[通知] {title}: {msg}")
except Exception as e:
    NOTIFY_FUNC = lambda title, msg: print(f"[通知] {title}: {msg}")

ITEM_PREFIXES = [
    "伝説の", "謎の", "未鑑定の", "古代の", "虹色の", "レア：", "封印された", "未知の", "呪われた", "祝福された"
]
ITEM_NAMES = [
    "スペースキー", "エンターキー", "タブキー", "CapsLockキー", "Fnキー", "USBメモリ", "マウスホイール", "テンキー", "F5キー", "NumLockキー"
]
ITEM_SUFFIXES = [
    "（未鑑定）", "（発掘済）", "（+5）", "（+7）", "（容量：未知数）", "（封印中）", "（虹色）", "（呪われている）", "（祝福済）", ""
]

DROP_MESSAGES = [
    "{item}を拾いました！",
    "{item}を発見！",
    "{item}を入手！",
    "{item}がドロップしました！",
    "{item}を獲得！"
]

HISTORY = []
HISTORY_LIMIT = 50


def generate_item():
    prefix = random.choice(ITEM_PREFIXES)
    name = random.choice(ITEM_NAMES)
    suffix = random.choice(ITEM_SUFFIXES)
    item = f"{prefix}{name}{suffix}"
    return item

def generate_message():
    item = generate_item()
    msg_template = random.choice(DROP_MESSAGES)
    return msg_template.format(item=item)

def notify_drop():
    msg = generate_message()
    HISTORY.append(msg)
    if len(HISTORY) > HISTORY_LIMIT:
        HISTORY.pop(0)
    NOTIFY_FUNC("アイテムドロップ通知", msg)
    print(f"[通知] {msg}")

def drop_loop(interval, stop_event):
    while not stop_event.is_set():
        notify_drop()
        for _ in range(int(interval * 10)):
            if stop_event.is_set():
                break
            time.sleep(0.1)

def list_history():
    if not HISTORY:
        print("まだアイテムドロップ履歴はありません。")
        return
    print("== アイテムドロップ履歴 ==")
    for i, msg in enumerate(HISTORY[-HISTORY_LIMIT:], 1):
        print(f"{i:02d}: {msg}")

def summary():
    print(f"== ドロップ数: {len(HISTORY)} ==")
    counts = {}
    for msg in HISTORY:
        for name in ITEM_NAMES:
            if name in msg:
                counts[name] = counts.get(name, 0) + 1
    for name, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{name}: {cnt}回")

def main():
    parser = argparse.ArgumentParser(description='謎の伝説アイテムドロップ通知スキル')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='一定間隔でアイテムドロップ通知を発生させる')
    parser_log.add_argument('--interval', type=float, default=900, help='通知間隔(秒)。デフォルト15分')
    parser_log.add_argument('--count', type=int, default=0, help='通知回数。0なら無限')

    parser_once = subparsers.add_parser('once', help='1回だけアイテムドロップ通知を発生')

    parser_list = subparsers.add_parser('list', help='ドロップ履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='アイテム別ドロップ数サマリ')

    args = parser.parse_args()

    if args.command == 'log':
        stop_event = threading.Event()
        def stop_after_count():
            if args.count > 0:
                for _ in range(args.count):
                    if stop_event.is_set():
                        break
                    notify_drop()
                    for _ in range(int(args.interval * 10)):
                        if stop_event.is_set():
                            break
                        time.sleep(0.1)
                stop_event.set()
        t = threading.Thread(target=stop_after_count)
        t.start()
        try:
            while t.is_alive():
                t.join(1)
        except KeyboardInterrupt:
            stop_event.set()
            print("\n[終了] ドロップ通知を停止しました。")
    elif args.command == 'once':
        notify_drop()
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
