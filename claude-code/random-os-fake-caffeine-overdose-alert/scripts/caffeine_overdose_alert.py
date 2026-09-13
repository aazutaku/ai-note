import sys
import random
import argparse
import platform
import subprocess
import threading
import time
from typing import List

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

FAKE_ALERTS = [
    "重大：あなたのカフェイン血中濃度が“徹夜エンジニア”レベルに到達しました。",
    "警告：コーヒーカップが自動でリフィルされました。摂取量にご注意ください。",
    "OSより：今すぐ水分を摂取してください。",
    "注意：カフェイン過剰摂取モードが有効になりました。",
    "システム通知：あなたのデスクトップに見覚えのないコーヒー染みが発見されました。",
    "警告：カフェイン摂取量が推奨値の200%を超えました。",
    "重大：あなたのマグカップが空になることはありません。",
    "OS警告：カフェイン耐性が進行中です。",
    "注意：仮想コーヒーメーカーが再起動されました。",
    "警告：カフェインロギングサービスが暴走しています。"
]

TRIGGER_KEYWORDS = [
    "徹夜", "カフェイン", "集中", "眠気", "作業効率", "coffee", "caffeine", "alert", "overdose"
]

HISTORY = []


def send_os_notification(title: str, message: str):
    system = platform.system()
    if PLYER_AVAILABLE:
        notification.notify(title=title, message=message, timeout=6)
    elif system == "Darwin":  # macOS
        subprocess.run([
            "osascript", "-e",
            f'display notification "{message}" with title "{title}"'
        ])
    elif system == "Linux":
        subprocess.run([
            "notify-send", title, message
        ])
    elif system == "Windows":
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(title, message, duration=6)
        except ImportError:
            print(f"[{title}] {message}")
    else:
        print(f"[{title}] {message}")


def print_terminal_alert(message: str):
    border = "=" * (len(message) + 8)
    print(f"\n{border}\n[FAKE ALERT] {message}\n{border}\n")


def random_alert() -> str:
    return random.choice(FAKE_ALERTS)


def trigger_alert(output_mode: str = "auto"):
    msg = random_alert()
    HISTORY.append(msg)
    if output_mode == "os":
        send_os_notification("カフェイン過剰摂取警告", msg)
    elif output_mode == "terminal":
        print_terminal_alert(msg)
    else:
        # Try OS notification, fallback to terminal
        try:
            send_os_notification("カフェイン過剰摂取警告", msg)
        except Exception:
            print_terminal_alert(msg)


def list_history():
    if not HISTORY:
        print("過去のフェイク警告はありません。")
        return
    print("=== フェイク警告履歴 ===")
    for idx, msg in enumerate(HISTORY, 1):
        print(f"{idx}. {msg}")


def summary():
    print(f"これまでに{len(HISTORY)}件のカフェイン過剰摂取フェイク警告が発動されました。")
    if HISTORY:
        print(f"最後の警告: {HISTORY[-1]}")


def semantic_trigger(text: str, output_mode: str = "auto"):
    for kw in TRIGGER_KEYWORDS:
        if kw.lower() in text.lower():
            trigger_alert(output_mode)
            return True
    return False


def random_alert_timer(interval_min=600, interval_max=1800, output_mode="auto"):
    while True:
        wait = random.randint(interval_min, interval_max)
        time.sleep(wait)
        trigger_alert(output_mode)


def main():
    parser = argparse.ArgumentParser(
        description="謎のOSカフェイン過剰摂取フェイク警告を炸裂させるSkill"
    )
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="即座にフェイク警告を表示")
    parser_alert.add_argument(
        "--mode", choices=["auto", "os", "terminal"], default="auto",
        help="通知の表示方法 (auto:自動, os:OS通知, terminal:ターミナル)"
    )

    parser_semantic = subparsers.add_parser("semantic", help="テキストに応じて警告を発動")
    parser_semantic.add_argument("text", help="判定対象テキスト")
    parser_semantic.add_argument(
        "--mode", choices=["auto", "os", "terminal"], default="auto"
    )

    parser_list = subparsers.add_parser("list", help="警告履歴を表示")
    parser_summary = subparsers.add_parser("summary", help="発動件数まとめ")

    parser_daemon = subparsers.add_parser("daemon", help="理不尽なタイミングで自動発動")
    parser_daemon.add_argument(
        "--min", type=int, default=600, help="最小発動間隔(秒)"
    )
    parser_daemon.add_argument(
        "--max", type=int, default=1800, help="最大発動間隔(秒)"
    )
    parser_daemon.add_argument(
        "--mode", choices=["auto", "os", "terminal"], default="auto"
    )

    args = parser.parse_args()

    if args.command == "alert":
        trigger_alert(args.mode)
    elif args.command == "semantic":
        semantic_trigger(args.text, args.mode)
    elif args.command == "list":
        list_history()
    elif args.command == "summary":
        summary()
    elif args.command == "daemon":
        print("理不尽なタイミングでフェイク警告を発動します。Ctrl+Cで終了。")
        try:
            random_alert_timer(args.min, args.max, args.mode)
        except KeyboardInterrupt:
            print("\n自動発動を停止しました。")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
