import sys
import os
import time
import random
import argparse
import threading
from datetime import datetime

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

# 警告メッセージ候補
BUG_ALERT_MESSAGES = [
    "警告: 本日{time}に新たなバグが孵化しました",
    "緊急: メモリ奥地で未確認バグが産声をあげました",
    "注意: システム深部でバグの卵が発見されました",
    "警告: 未知のバグがプロセス空間に漂流中",
    "速報: 記憶領域でバグの幼体が観測されました",
    "警告: バグの繁殖活動が活発化しています",
    "注意: OSカーネル付近でバグの孵化反応を検知",
    "緊急: バグの幼虫がスレッド間を移動中",
    "警告: システムログにバグの足跡を発見",
    "注意: バグの卵が複数同時に孵化しました",
    "速報: バグの鳴き声が聞こえました (要調査)"
]

LOG_FILE = os.path.expanduser("~/.fake_bug_hatching_alert.log")


def get_random_message():
    now = datetime.now()
    time_str = now.strftime("%H:%M")
    msg = random.choice(BUG_ALERT_MESSAGES)
    return msg.format(time=time_str)


def print_terminal_alert(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert = f"[OS警告] {now}\n{message}\n"
    print(alert)
    log_alert(alert)


def notify_desktop(message):
    if not PLYER_AVAILABLE:
        return False
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        notification.notify(
            title="OS警告",
            message=f"{message}\n({now})",
            timeout=8
        )
        log_alert(f"[OS警告] {now}\n{message}\n")
        return True
    except Exception as e:
        return False


def log_alert(alert):
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(alert + '\n')
    except Exception:
        pass


def random_wait(min_sec=180, max_sec=900):
    return random.randint(min_sec, max_sec)


def alert_once():
    message = get_random_message()
    # まずデスクトップ通知を試みる
    if PLYER_AVAILABLE and notify_desktop(message):
        return
    # 失敗したらターミナル出力
    print_terminal_alert(message)


def run_alert_loop(forever=True, min_sec=180, max_sec=900):
    try:
        while True:
            wait_time = random_wait(min_sec, max_sec)
            time.sleep(wait_time)
            alert_once()
            if not forever:
                break
    except KeyboardInterrupt:
        print("\n[終了] バグ孵化警告ループを停止しました。")


def show_log(limit=10):
    if not os.path.exists(LOG_FILE):
        print("ログファイルがありません。")
        return
    with open(LOG_FILE, encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines[-limit:]:
        print(line.rstrip())


def summary():
    if not os.path.exists(LOG_FILE):
        print("ログファイルがありません。")
        return
    with open(LOG_FILE, encoding='utf-8') as f:
        lines = f.readlines()
    print(f"累計バグ孵化警告数: {len(lines)}")
    if lines:
        print(f"最新: {lines[-1].strip()}")


def parse_args():
    parser = argparse.ArgumentParser(description='バグ孵化警告スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    run_parser = subparsers.add_parser('run', help='ランダム警告ループを開始')
    run_parser.add_argument('--min', type=int, default=180, help='最小間隔(秒)')
    run_parser.add_argument('--max', type=int, default=900, help='最大間隔(秒)')
    run_parser.add_argument('--once', action='store_true', help='1回だけ警告を表示')

    log_parser = subparsers.add_parser('log', help='直近の警告ログを表示')
    log_parser.add_argument('--limit', type=int, default=10, help='表示件数')

    subparsers.add_parser('summary', help='警告の累計と最新を表示')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'run':
        if args.once:
            alert_once()
        else:
            run_alert_loop(forever=True, min_sec=args.min, max_sec=args.max)
    elif args.command == 'log':
        show_log(limit=args.limit)
    elif args.command == 'summary':
        summary()
    else:
        print("コマンドを指定してください (run/log/summary)")


if __name__ == '__main__':
    main()
