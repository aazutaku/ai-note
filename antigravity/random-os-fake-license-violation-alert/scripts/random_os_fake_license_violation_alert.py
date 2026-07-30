import random
import time
import argparse
import sys
import threading
from datetime import datetime

try:
    from plyer import notification
except ImportError:
    notification = None
    
ALERT_TEMPLATES = [
    "あなたの椅子、座りすぎライセンス違反が検出されました。直ちに立ち上がってください。",
    "コーヒーブレイク無許可利用を検出。管理者に連絡してください。",
    "謎のキーボード配列違反が発生しました。",
    "マウスクリック過多による操作制限違反。",
    "未登録のUSBデバイスが検出されました（実は嘘です）。",
    "ディスプレイ注視時間が規定値を超過しました。目を休めてください。",
    "OSライセンス：ペット写真閲覧権限がありません。",
    "未認可の深夜作業違反を検出しました。",
    "コードレビュー未提出ライセンス違反。",
    "マウスホイール逆回転違反。",
    "エアコン温度設定違反。",
    "仮想デスクトップ過剰利用違反。",
    "未登録Bluetoothデバイス接続違反。",
    "未許可のコピペ操作違反。",
    "OSライセンス：机の上のコップ放置違反。"
]

LOG_FILE = "fake_license_violation_alert.log"

def random_alert_message():
    return random.choice(ALERT_TEMPLATES)

def show_notification(message):
    if notification:
        notification.notify(
            title="OSライセンス違反警告",
            message=message,
            timeout=8
        )
    else:
        print(f"[通知] OSライセンス違反警告: {message}")

def log_alert(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")

def alert_once(verbose=False, log=False):
    msg = random_alert_message()
    show_notification(msg)
    if verbose:
        print(f"[通知] OSライセンス違反警告: {msg}")
    if log:
        log_alert(msg)

def alert_loop(interval_min=60, interval_max=300, count=5, verbose=False, log=False):
    for _ in range(count):
        alert_once(verbose=verbose, log=log)
        sleep_time = random.randint(interval_min, interval_max)
        if verbose:
            print(f"[INFO] 次の警告まで {sleep_time} 秒待機します。")
        time.sleep(sleep_time)

def list_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("[INFO] ログファイルが存在しません。警告履歴はありません。")

def summary_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"[SUMMARY] 通知履歴: {len(lines)} 件")
        recent = lines[-5:] if len(lines) >= 5 else lines
        print("[最近の通知]")
        for line in recent:
            print(line.strip())
    except FileNotFoundError:
        print("[INFO] ログファイルが存在しません。")

def parse_args():
    parser = argparse.ArgumentParser(description="謎のOSライセンス違反警告をランダムに通知します。ジョーク用途のみ。")
    subparsers = parser.add_subparsers(dest="command")

    parser_once = subparsers.add_parser("once", help="1回だけ警告を表示")
    parser_once.add_argument("--verbose", action="store_true", help="詳細表示")
    parser_once.add_argument("--log", action="store_true", help="通知内容をログに保存")

    parser_loop = subparsers.add_parser("loop", help="複数回ランダム間隔で警告")
    parser_loop.add_argument("--min", type=int, default=60, help="最小間隔(秒)")
    parser_loop.add_argument("--max", type=int, default=300, help="最大間隔(秒)")
    parser_loop.add_argument("--count", type=int, default=5, help="通知回数")
    parser_loop.add_argument("--verbose", action="store_true", help="詳細表示")
    parser_loop.add_argument("--log", action="store_true", help="通知内容をログに保存")

    parser_list = subparsers.add_parser("list", help="通知ログを表示")
    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリ")

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == "once":
        alert_once(verbose=args.verbose, log=args.log)
    elif args.command == "loop":
        alert_loop(
            interval_min=args.min,
            interval_max=args.max,
            count=args.count,
            verbose=args.verbose,
            log=args.log
        )
    elif args.command == "list":
        list_log()
    elif args.command == "summary":
        summary_log()
    else:
        print("コマンドを指定してください (once/loop/list/summary)")
        sys.exit(1)

if __name__ == "__main__":
    main()
