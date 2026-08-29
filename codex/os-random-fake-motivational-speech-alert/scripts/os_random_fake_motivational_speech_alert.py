import sys
import os
import random
import platform
import subprocess
import argparse
import time

MOTIVATIONAL_MESSAGES = [
    "今こそコード界の伝説になるときです。",
    "あなたのcommitは宇宙を救う可能性を秘めています。",
    "そのタイピング、情熱が伝わってきます。",
    "シンタックスエラーも、あなたなら乗り越えられる。",
    "今日の努力が明日のOSを支えます。",
    "あなたのデバッグ力が未来を切り拓きます。",
    "コンパイルのたびに、あなたは進化しています。",
    "OS公式：あなたの集中力に敬意を表します。",
    "その一行が、世界を変える鍵になるかもしれません。",
    "バグもあなたの成長の糧です。",
    "あなたのpushを、OSは見守っています。",
    "今のあなたは、まさにOS公認の勇者です。",
    "エラーは挑戦の証です。恐れず進みましょう。",
    "あなたのキーボードから、未来が生まれます。",
    "OSもあなたを応援しています。",
    "その情熱、OSに伝わっています。",
    "今日のあなたは、昨日のあなたを超えています。",
    "あなたのコードが、世界をもっと良くします。",
    "OSの歴史に、あなたの名前が刻まれる日も近い。",
    "その一歩が、大きな進化につながります。"
]


def get_random_message():
    return random.choice(MOTIVATIONAL_MESSAGES)


def send_notification(message, title="OS MOTIVATION"):
    system = platform.system()
    if system == "Linux":
        # Use notify-send
        try:
            subprocess.run([
                "notify-send", title, message
            ], check=True)
        except Exception as e:
            print(f"[WARN] notify-send failed: {e}")
            print(f"[{title}] {message}")
    elif system == "Darwin":
        # Use osascript
        osa_script = f'display notification "{message}" with title "{title}"'
        try:
            subprocess.run([
                "osascript", "-e", osa_script
            ], check=True)
        except Exception as e:
            print(f"[WARN] osascript failed: {e}")
            print(f"[{title}] {message}")
    elif system == "Windows":
        # Use Toast notification (requires win10toast)
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=5, threaded=True)
        except ImportError:
            print(f"[WARN] win10toast not installed. Printing message instead.")
            print(f"[{title}] {message}")
        except Exception as e:
            print(f"[WARN] Windows notification failed: {e}")
            print(f"[{title}] {message}")
    else:
        print(f"[{title}] {message}")


def print_message(message, title="OS MOTIVATION"):
    print(f"[{title}] {message}")


def trigger_alert(args):
    message = get_random_message()
    if args.notify:
        send_notification(message)
    else:
        print_message(message)


def loop_alert(args):
    interval = args.interval
    count = args.count
    for i in range(count):
        trigger_alert(args)
        if i < count - 1:
            time.sleep(interval)


def list_messages(args):
    print("--- Motivational Messages List ---")
    for idx, msg in enumerate(MOTIVATIONAL_MESSAGES, 1):
        print(f"{idx:2d}: {msg}")


def main():
    parser = argparse.ArgumentParser(
        description="OS Random Fake Motivational Speech Alert Skill"
    )
    subparsers = parser.add_subparsers(dest="command", help="sub-command help")

    # Trigger command (default)
    parser_trigger = subparsers.add_parser(
        "trigger", help="1回だけランダム通知を発火"
    )
    parser_trigger.add_argument(
        "--notify", action="store_true", help="OS通知として表示 (デフォルトはprintのみ)"
    )
    parser_trigger.set_defaults(func=trigger_alert)

    # Loop command
    parser_loop = subparsers.add_parser(
        "loop", help="指定回数・間隔で連続通知"
    )
    parser_loop.add_argument(
        "--interval", type=float, default=10.0, help="通知間隔(秒)"
    )
    parser_loop.add_argument(
        "--count", type=int, default=5, help="通知回数"
    )
    parser_loop.add_argument(
        "--notify", action="store_true", help="OS通知として表示"
    )
    parser_loop.set_defaults(func=loop_alert)

    # List command
    parser_list = subparsers.add_parser(
        "list", help="全メッセージ一覧を表示"
    )
    parser_list.set_defaults(func=list_messages)

    args = parser.parse_args()
    if not args.command:
        # デフォルトは1回通知
        args = parser.parse_args(["trigger"])
    args.func(args)

if __name__ == "__main__":
    main()
