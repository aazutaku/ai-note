import random
import sys
import argparse
import time
from plyer import notification

COFFEE_MESSAGES = [
    "重大: コーヒーカップが満杯です。システムのカフェイン値が危険域に到達しました。",
    "警告: OSのカフェイン値が限界突破。処理継続には一時的なコーヒー断ちが必要です。",
    "注意: コーヒーポートでオーバーフローが発生しました。カップを空にしてください。",
    "エラー: カフェインバッファが溢れました。追加投入は推奨されません。",
    "警告: コーヒーセンサーが異常値を検出しました。再起動を検討してください。",
    "重大: デジタルカフェイン流出。OSの覚醒度が過剰です。",
    "通知: コーヒーサーバーの温度が臨界点に達しました。冷却をおすすめします。",
    "警告: コーヒーインジェクション攻撃を検出。カフェイン摂取を制限してください。",
    "注意: システムリソースがコーヒーで埋まりつつあります。",
    "重大: コーヒーAPIから異常なレスポンス。OSの眠気検知を強化してください。"
]

HISTORY_FILE = ".coffee_overflow_history.log"


def send_random_coffee_alert():
    message = random.choice(COFFEE_MESSAGES)
    notification.notify(
        title="OSコーヒーあふれ警告",
        message=message,
        app_name="CoffeeOverflowAlert",
        timeout=8
    )
    log_alert(message)
    return message


def log_alert(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def list_history(limit=10):
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            print("履歴がありません。")
            return
        print("--- Coffee Overflow Alert 履歴 ---")
        for line in lines[-limit:]:
            print(line.strip())
    except FileNotFoundError:
        print("履歴ファイルが見つかりません。まだアラートが発火していません。")


def summary():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        total = len(lines)
        if total == 0:
            print("履歴がありません。")
            return
        print(f"これまでに発火したコーヒー警告: {total}回")
        counter = {}
        for msg in COFFEE_MESSAGES:
            counter[msg] = 0
        for line in lines:
            for msg in COFFEE_MESSAGES:
                if msg in line:
                    counter[msg] += 1
        print("--- メッセージ別発火回数 ---")
        for msg, cnt in counter.items():
            print(f"{msg[:20]}...: {cnt}回")
    except FileNotFoundError:
        print("履歴ファイルが見つかりません。まだアラートが発火していません。")


def clear_history():
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            pass
        print("履歴をクリアしました。")
    except Exception as e:
        print(f"履歴クリア中にエラー: {e}")


def main():
    parser = argparse.ArgumentParser(description="OSコーヒーあふれ警告スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="ランダムなコーヒー警告を発火")
    parser_list = subparsers.add_parser("list", help="警告履歴を表示")
    parser_list.add_argument("-n", "--num", type=int, default=10, help="表示件数 (デフォルト10件)")
    parser_summary = subparsers.add_parser("summary", help="警告履歴のサマリーを表示")
    parser_clear = subparsers.add_parser("clear", help="履歴をクリア")

    args = parser.parse_args()

    if args.command == "alert":
        msg = send_random_coffee_alert()
        print(f"[通知発火] {msg}")
    elif args.command == "list":
        list_history(limit=args.num)
    elif args.command == "summary":
        summary()
    elif args.command == "clear":
        clear_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
