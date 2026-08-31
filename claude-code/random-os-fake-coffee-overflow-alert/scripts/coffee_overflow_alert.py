import random
import argparse
import sys
import time
from plyer import notification

COFFEE_ALERTS = [
    "重大：コーヒーカップが満杯です。OSのカフェイン値が臨界点に到達しました。",
    "警告：OSのカフェインメモリが溢れています。コーヒー断ち推奨。",
    "注意：仮想マシンのカフェインプールがリーク中。今すぐリフレッシュを！",
    "エラー：コーヒー過剰摂取によりプロセスが一時停止。",
    "情報：カフェイン・バッファが自動クリアされました。",
    "警告：カフェイン・スレッドがデッドロックしています。コーヒーブレイクを挿入してください。",
    "重大：コーヒー・スタックオーバーフロー。リスタートが必要です。",
    "注意：OSのカフェイン・ガーベジコレクションが追いついていません。",
    "エラー：カフェイン・ドライバがクラッシュしました。新しい豆を挿入してください。",
    "情報：コーヒー・バッファが自動的にリフレッシュされました。"
]

TRIGGER_KEYWORDS = [
    "コーヒー", "集中", "眠い", "警告", "OS", "カフェイン"
]

def send_coffee_alert():
    alert = random.choice(COFFEE_ALERTS)
    notification.notify(
        title="Coffee Overflow Alert",
        message=alert,
        timeout=7
    )
    print(f"[通知] {alert}")

def listen_stdin_for_keywords():
    print("[Skill] 標準入力からキーワードを監視します。Ctrl+Cで終了。\n")
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            for keyword in TRIGGER_KEYWORDS:
                if keyword in line:
                    send_coffee_alert()
                    break
    except KeyboardInterrupt:
        print("\n[Skill] 終了します。")

def alert_loop(interval):
    print(f"[Skill] {interval}秒ごとにコーヒー警告を発火します。Ctrl+Cで停止。\n")
    try:
        while True:
            send_coffee_alert()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[Skill] ループを終了します。\n")

def main():
    parser = argparse.ArgumentParser(description="OSコーヒーあふれ警告スキル")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="即座にコーヒー警告を発火")
    parser_listen = subparsers.add_parser("listen", help="標準入力からキーワードを監視して発火")
    parser_loop = subparsers.add_parser("loop", help="定期的に警告を発火")
    parser_loop.add_argument("--interval", type=int, default=900, help="警告間隔(秒, デフォルト15分)")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    if args.command == "alert":
        send_coffee_alert()
    elif args.command == "listen":
        listen_stdin_for_keywords()
    elif args.command == "loop":
        alert_loop(args.interval)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
