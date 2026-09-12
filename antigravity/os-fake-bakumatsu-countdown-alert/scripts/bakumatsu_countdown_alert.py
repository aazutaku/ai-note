import sys
import random
import argparse
import time
import threading
import platform

try:
    import notify2
except ImportError:
    notify2 = None

try:
    from plyer import notification
except ImportError:
    notification = None

BAKUMATSU_EVENTS = [
    ("明治維新", "システムはあと{min}分で明治維新されます。"),
    ("黒船再来", "本日は黒船再来。本能寺リブートまで残り{min}分。"),
    ("薩長同盟", "薩長同盟成立まで残り{min}分。"),
    ("安政の大獄", "幕府サーバーが安政の大獄モードに突入します。残り{min}分。"),
    ("新選組アップデート", "新選組アップデート適用まで残り{min}分。"),
    ("戊辰戦争", "戊辰戦争プロセス開始まであと{min}分。"),
    ("大政奉還", "大政奉還イベント発動まで残り{min}分。"),
    ("尊王攘夷", "尊王攘夷アラート：残り{min}分で発動。"),
    ("西南戦争", "西南戦争ログインまで残り{min}分。"),
    ("江戸城開城", "江戸城開城まで残り{min}分。"),
]

TERMINAL_PREFIXES = [
    "[幕末警告]",
    "[黒船アラート]",
    "[維新カウントダウン]",
    "[歴史警告]",
    "[パロディ通知]"
]

def generate_alert():
    event = random.choice(BAKUMATSU_EVENTS)
    prefix = random.choice(TERMINAL_PREFIXES)
    min_left = random.randint(3, 15)
    message = event[1].format(min=min_left)
    return prefix, event[0], message, min_left

def send_terminal_alert(prefix, title, message):
    print(f"{prefix} {message}")

def send_desktop_alert(title, message):
    if notify2:
        try:
            notify2.init("Bakumatsu Countdown Alert")
            n = notify2.Notification(title, message)
            n.show()
        except Exception as e:
            print(f"[通知エラー] {e}")
    elif notification:
        try:
            notification.notify(title=title, message=message, app_name="Bakumatsu Countdown Alert")
        except Exception as e:
            print(f"[通知エラー] {e}")
    else:
        print(f"[通知API未インストール] {title}: {message}")

def countdown_alert(desktop=False, interval=300, repeat=1):
    for _ in range(repeat):
        prefix, title, message, min_left = generate_alert()
        send_terminal_alert(prefix, title, message)
        if desktop:
            send_desktop_alert(title, message)
        if repeat > 1:
            time.sleep(interval)

def background_mode(desktop=False, interval=600):
    def loop():
        while True:
            prefix, title, message, min_left = generate_alert()
            send_terminal_alert(prefix, title, message)
            if desktop:
                send_desktop_alert(title, message)
            time.sleep(interval)
    t = threading.Thread(target=loop, daemon=True)
    t.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[終了] 幕末カウントダウン通知を停止しました。")

def list_examples():
    print("--- 幕末カウントダウン通知サンプル ---")
    for _ in range(5):
        prefix, title, message, min_left = generate_alert()
        print(f"{prefix} {message}")

def parse_args():
    parser = argparse.ArgumentParser(description="幕末カウントダウン フェイクアラート通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="1回だけ通知を出す")
    parser_alert.add_argument("--desktop", action="store_true", help="デスクトップ通知も出す")
    parser_alert.add_argument("--repeat", type=int, default=1, help="繰り返し回数")
    parser_alert.add_argument("--interval", type=int, default=300, help="繰り返し間隔(秒)")

    parser_bg = subparsers.add_parser("background", help="定期的に通知を出し続ける")
    parser_bg.add_argument("--desktop", action="store_true", help="デスクトップ通知も出す")
    parser_bg.add_argument("--interval", type=int, default=600, help="通知間隔(秒)")

    parser_list = subparsers.add_parser("list", help="サンプル通知を5つ表示")
    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == "alert":
        countdown_alert(desktop=args.desktop, interval=args.interval, repeat=args.repeat)
    elif args.command == "background":
        background_mode(desktop=args.desktop, interval=args.interval)
    elif args.command == "list":
        list_examples()
    else:
        print("コマンドを指定してください: alert, background, list")
        sys.exit(1)

if __name__ == '__main__':
    main()
