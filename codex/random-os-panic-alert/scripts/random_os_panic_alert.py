import sys
import argparse
import random
import time
import os
from datetime import datetime, timedelta

try:
    from plyer import notification
except ImportError:
    notification = None
    print("[警告] plyer モジュールが見つかりません。'pip install plyer' でインストールしてください。")

PANIC_MESSAGES = [
    "カーネルがランチに出ました",
    "ビットが逃走しました。追跡中...",
    "仮想メモリが現実逃避中です",
    "システムクロックが未来に到達しました",
    "デバッグ用アヒルが迷子です",
    "プロセスIDが自我に目覚めました",
    "ファイルシステムが詩を書き始めました",
    "メモリリークが水たまりを作りました",
    "スレッドが昼寝中です",
    "パケットが迷子になりました",
    "CPUが哲学的思索にふけっています",
    "I/Oバッファがカラオケ大会を開催中",
    "セマフォが永遠の赤信号です",
    "ログインシェルが家出しました",
    "デバイスドライバが読書中です",
    "OSが自己分析を始めました",
    "仮想マシンが現実逃避中です",
    "ファームウェアが懐かしい話を始めました",
    "メモリバンクが銀行強盗に遭いました",
    "カーネルパニックがパニック中です"
]

HISTORY_FILE = os.path.expanduser("~/.random_os_panic_alert_history.log")
FREQUENCY_LIMIT_MINUTES = 10


def notify(title, message):
    if notification:
        try:
            notification.notify(
                title=title,
                message=message,
                app_name="Random OS Panic Alert",
                timeout=8
            )
        except Exception as e:
            print(f"[Error] 通知送信失敗: {e}")
    else:
        print(f"[通知] {title}: {message}")


def log_history(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\t{message}\n")


def read_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def can_notify():
    history = read_history()
    if not history:
        return True
    last_entry = history[-1]
    try:
        last_time_str = last_entry.split("\t")[0]
        last_time = datetime.strptime(last_time_str, "%Y-%m-%d %H:%M:%S")
        if datetime.now() - last_time < timedelta(minutes=FREQUENCY_LIMIT_MINUTES):
            return False
    except Exception:
        return True
    return True


def panic_alert():
    if not can_notify():
        print(f"[Info] 通知頻度制限によりスキップされました（{FREQUENCY_LIMIT_MINUTES}分以内）")
        return
    message = random.choice(PANIC_MESSAGES)
    notify("OS Panic Alert", message)
    log_history(message)


def list_history(args):
    history = read_history()
    if not history:
        print("履歴はありません。")
        return
    print("--- 通知履歴 ---")
    for line in history[-args.limit:]:
        print(line)


def summary(args):
    history = read_history()
    print(f"合計通知回数: {len(history)}")
    if history:
        print(f"最初の通知: {history[0].split('\t')[0]}")
        print(f"最新の通知: {history[-1].split('\t')[0]}")


def clear_history(args):
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("履歴を削除しました。")
    else:
        print("履歴ファイルが存在しません。")


def main():
    parser = argparse.ArgumentParser(description="Random OS Panic Alert - 珍妙なOSパニック通知を表示します")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="今すぐランダムなパニックアラートを表示")
    parser_alert.set_defaults(func=lambda args: panic_alert())

    parser_list = subparsers.add_parser("list", help="通知履歴を表示")
    parser_list.add_argument("--limit", type=int, default=10, help="表示件数 (デフォルト10件)")
    parser_list.set_defaults(func=list_history)

    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリーを表示")
    parser_summary.set_defaults(func=summary)

    parser_clear = subparsers.add_parser("clear", help="通知履歴を削除")
    parser_clear.set_defaults(func=clear_history)

    args = parser.parse_args()

    if not args.command:
        # デフォルトはalert
        panic_alert()
    else:
        args.func(args)

if __name__ == "__main__":
    main()
