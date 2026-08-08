import sys
import argparse
import random
import platform
import subprocess
import threading
import time
from typing import List

# 通知メッセージ候補
MESSAGES = [
    "スクリーンショット保存済み：バグ発生の瞬間",
    "証拠画像を保存しました",
    "あなたの集中顔を記録しました",
    "画面全体の謎画像を保存しました",
    "何もしていませんが保存しました",
    "OSが勝手に保存しました",
    "保存フォルダが謎の画像でいっぱいです",
    "保存済み：誰も見ていない瞬間",
    "保存済み：この会話の証拠",
    "保存済み：集中力のピーク"
]

# 発動トリガーワード
TRIGGER_KEYWORDS = [
    "build", "compile", "run", "test", "debug", "error", "save", "screenshot",
    "証拠", "保存", "スクリーンショット", "バグ", "実行", "ビルド", "デバッグ"
]

# OSごとの通知関数
def send_notification(message: str):
    system = platform.system()
    try:
        if system == "Linux":
            subprocess.run(["notify-send", message], check=True)
        elif system == "Darwin":
            script = f'display notification "{message}" with title "通知"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("通知", message, duration=4, threaded=True)
            except ImportError:
                print("[警告] win10toastがインストールされていません。pip install win10toast で導入してください。")
                print(f"[通知] {message}")
        else:
            print(f"[通知] {message}")
    except Exception as e:
        print(f"[通知] {message} (通知API失敗: {e})")

# メッセージをランダム選択して通知
def random_alert():
    message = random.choice(MESSAGES)
    send_notification(message)

# コマンドライン引数解析
def parse_args():
    parser = argparse.ArgumentParser(description="謎のOS偽スクリーンショット保存通知を表示するジョークSkill")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_alert = subparsers.add_parser("alert", help="ランダムな偽通知を即座に表示")
    parser_alert.add_argument("-n", "--num", type=int, default=1, help="通知回数 (デフォルト: 1)")
    parser_alert.add_argument("-i", "--interval", type=float, default=2.0, help="通知間隔(秒)")

    parser_monitor = subparsers.add_parser("monitor", help="標準入力を監視し、キーワード検出時に通知")
    parser_monitor.add_argument("-f", "--frequency", type=float, default=1.0, help="監視間隔(秒)")

    return parser.parse_args()

# 標準入力監視モード
def monitor_stdin(frequency: float):
    print("[INFO] 標準入力を監視します。Ctrl+Cで終了")
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                time.sleep(frequency)
                continue
            for kw in TRIGGER_KEYWORDS:
                if kw.lower() in line.lower():
                    random_alert()
                    break
    except KeyboardInterrupt:
        print("[INFO] 監視を終了します。")

# メイン関数
def main():
    args = parse_args()
    if args.command == "alert":
        for i in range(args.num):
            random_alert()
            if i < args.num - 1:
                time.sleep(args.interval)
    elif args.command == "monitor":
        monitor_stdin(args.frequency)
    else:
        print("[ERROR] 不明なコマンドです。")

if __name__ == '__main__':
    main()
