import sys
import os
import random
import time
import argparse
import threading
from datetime import datetime
try:
    from plyer import notification
except ImportError:
    notification = None

# 評価メッセージ候補
AI_MESSAGES = [
    "本日のあなたの集中度: AI判定『たぶん寝てる』",
    "AIによる自動評価: コーヒー摂取量が基準値超過",
    "システムAI: 進捗率0%を検知しました。やる気スコア: -42",
    "OS公式AI: あなたのキーボード打鍵音が眠そうです",
    "AI判定: 本日は“やった気分”のみ加点されました",
    "AI評価: マウス移動距離が基準値未満です。休憩推奨",
    "システムAI: 画面注視率が低下しています。AI推定: ぼんやり中",
    "AI通知: タスク切り替え回数が多すぎます。集中力分散中",
    "AI評価: 今日の成果物は“ファイル名が長い”のみ認定",
    "OS公式AI: あなたのタイピング速度が昨日比-17%",
    "AI判定: Slack未読数が増加中。AI推定: 逃避行動",
    "AI評価: 進捗バーが動いていません。AI推定: 仕様検討中",
    "AI通知: 机上のコーヒーカップ数が危険水域です",
    "システムAI: チーム内雑談比率が高すぎます。AI推定: 盛り上がり中",
    "AI評価: 今日は“やる気ボーナス”未発生日です"
]

LOG_PATH = os.path.expanduser("~/.random_os_fake_ai_eval_alert.log")

# ログ書き込み
def log_message(msg):
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{dt}] {msg}\n")

# 通知表示
def show_notification(msg):
    title = "AI評価通知"
    if notification:
        try:
            notification.notify(
                title=title,
                message=msg,
                app_name="random-os-fake-ai-evaluation-alert",
                timeout=7
            )
        except Exception as e:
            print(f"[AI評価通知] {msg}")
    else:
        print(f"[AI評価通知] {msg}")

# ランダムAI通知発射
def fire_random_alert():
    msg = random.choice(AI_MESSAGES)
    show_notification(msg)
    log_message(msg)

# 一定間隔で自動発動
def auto_mode(interval=600, stop_event=None):
    while not (stop_event and stop_event.is_set()):
        fire_random_alert()
        for _ in range(interval):
            if stop_event and stop_event.is_set():
                break
            time.sleep(1)

# ログ表示
def show_log(lines=10):
    if not os.path.exists(LOG_PATH):
        print("ログがありません。")
        return
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        all_lines = f.readlines()
        for line in all_lines[-lines:]:
            print(line.rstrip())

# ログサマリ
def show_summary():
    if not os.path.exists(LOG_PATH):
        print("ログがありません。")
        return
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"AI評価通知の累計発行数: {len(lines)}")
    last = lines[-1].strip() if lines else "-"
    print(f"最新通知: {last}")

# CLIエントリ
def main():
    parser = argparse.ArgumentParser(
        description="random-os-fake-ai-evaluation-alert: 理不尽AI評価通知で作業空間を演出します。"
    )
    subparsers = parser.add_subparsers(dest="command")

    fire_parser = subparsers.add_parser("fire", help="今すぐAI評価通知を発射")
    fire_parser.add_argument("-n", "--num", type=int, default=1, help="連続発射回数")

    auto_parser = subparsers.add_parser("auto", help="一定間隔で自動AI評価通知を発射")
    auto_parser.add_argument("-i", "--interval", type=int, default=600, help="通知間隔(秒)")

    log_parser = subparsers.add_parser("log", help="通知ログを表示")
    log_parser.add_argument("-l", "--lines", type=int, default=10, help="表示行数")

    summary_parser = subparsers.add_parser("summary", help="通知ログのサマリを表示")

    args = parser.parse_args()
    if args.command == "fire":
        for _ in range(args.num):
            fire_random_alert()
            time.sleep(1)
    elif args.command == "auto":
        stop_event = threading.Event()
        try:
            auto_mode(interval=args.interval, stop_event=stop_event)
        except KeyboardInterrupt:
            stop_event.set()
            print("\n自動AI評価通知を停止しました。")
    elif args.command == "log":
        show_log(lines=args.lines)
    elif args.command == "summary":
        show_summary()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
