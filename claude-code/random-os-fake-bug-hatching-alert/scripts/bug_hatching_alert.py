import random
import time
import argparse
import sys
import threading
import platform
import subprocess

BUG_ALERT_MESSAGES = [
    "本日{time}に新たなバグが孵化しました。",
    "緊急: メモリ奥地で未確認バグが産声をあげました。",
    "システム深部でバグの幼体が発見されました。",
    "バグの成長速度が通常を超えています。ご注意ください。",
    "未知のバグがネットワーク経由で拡散中です。",
    "警告: バグの卵が複数検出されました。",
    "バックグラウンドでバグが静かに増殖しています。",
    "バグのさなぎがプロセス空間で発見されました。",
    "OSコア付近でバグが孵化した形跡があります。",
    "バグの活動履歴が急増しています。"
]

PREFIX = "[OS警告] "

# OSごとの通知関数
def notify_os(message):
    system = platform.system()
    if system == "Darwin":
        subprocess.run(["osascript", "-e", f'display notification "{message}" with title "バグ孵化警告"'], check=False)
    elif system == "Linux":
        subprocess.run(["notify-send", "バグ孵化警告", message], check=False)
    elif system == "Windows":
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast("バグ孵化警告", message, duration=5)
        except ImportError:
            print(PREFIX + message)
    else:
        print(PREFIX + message)

# ターミナル標準出力
def notify_terminal(message):
    print(PREFIX + message)

# 警告文をランダム生成
def generate_alert():
    now = time.strftime("%H:%M")
    msg_template = random.choice(BUG_ALERT_MESSAGES)
    msg = msg_template.format(time=now)
    return msg

# 明示呼び出し用
def explicit_alert(args):
    msg = generate_alert()
    if args.os:
        notify_os(msg)
    else:
        notify_terminal(msg)

# ランダムタイミングで警告表示
def random_alert_loop(args):
    try:
        while True:
            interval = random.randint(args.min_interval, args.max_interval)
            time.sleep(interval)
            msg = generate_alert()
            if args.os:
                notify_os(msg)
            else:
                notify_terminal(msg)
    except KeyboardInterrupt:
        print("\n[終了] バグ孵化警告ループを停止しました。")

# CLIサブコマンド: log, list, summary (ダミー実装)
def log_alert(args):
    msg = generate_alert()
    print(f"[LOG] {msg}")
def list_alerts(args):
    for i in range(5):
        print(f"{i+1}. {generate_alert()}")
def summary_alerts(args):
    print("過去24時間のバグ孵化警告: 0件 (実害なし)")

# トリガーワード検出 (簡易)
def contains_trigger(text):
    triggers = ["バグ", "エラー", "警告", "デバッグ"]
    return any(t in text for t in triggers)

def semantic_trigger(args):
    print("[監視モード] 入力行にトリガーワードが現れると警告を表示します。Ctrl+Cで終了。")
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            if contains_trigger(line):
                msg = generate_alert()
                if args.os:
                    notify_os(msg)
                else:
                    notify_terminal(msg)
    except KeyboardInterrupt:
        print("\n[終了] 監視モードを停止しました。")

def main():
    parser = argparse.ArgumentParser(description="謎のOS公式バグ孵化警告をランダムに表示するSkill")
    subparsers = parser.add_subparsers(dest="command")
    # 明示呼び出し
    parser_alert = subparsers.add_parser("alert", help="即座にバグ孵化警告を表示")
    parser_alert.add_argument("--os", action="store_true", help="OS通知として表示する")
    parser_alert.set_defaults(func=explicit_alert)
    # ループ
    parser_loop = subparsers.add_parser("loop", help="ランダム間隔で警告を表示し続ける")
    parser_loop.add_argument("--os", action="store_true", help="OS通知として表示する")
    parser_loop.add_argument("--min-interval", type=int, default=60, help="最小間隔(秒)")
    parser_loop.add_argument("--max-interval", type=int, default=600, help="最大間隔(秒)")
    parser_loop.set_defaults(func=random_alert_loop)
    # ログ
    parser_log = subparsers.add_parser("log", help="警告をログ出力(ダミー)")
    parser_log.set_defaults(func=log_alert)
    # リスト
    parser_list = subparsers.add_parser("list", help="警告文のサンプルをリスト表示")
    parser_list.set_defaults(func=list_alerts)
    # サマリー
    parser_summary = subparsers.add_parser("summary", help="警告履歴のサマリー(ダミー)")
    parser_summary.set_defaults(func=summary_alerts)
    # セマンティックトリガー
    parser_sem = subparsers.add_parser("semantic", help="標準入力のトリガーワード検出で警告")
    parser_sem.add_argument("--os", action="store_true", help="OS通知として表示する")
    parser_sem.set_defaults(func=semantic_trigger)
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
