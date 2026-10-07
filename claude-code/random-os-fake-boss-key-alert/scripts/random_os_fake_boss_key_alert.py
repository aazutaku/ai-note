import argparse
import random
import sys
import threading
import time
from datetime import datetime

ALERT_MESSAGES = [
    "[OS ALERT] 上司接近！5秒以内にウィンドウを隠してください。",
    "[OS WARNING] ボス検知センサーが反応：現在の画面は安全ですか？",
    "[OS NOTICE] 不審な視線を検知。作業内容の見直しを推奨します。",
    "[OS ALERT] 緊急ボスキー発動準備完了。指示があるまで待機してください。",
    "[OS WARNING] 画面の明るさが高すぎます。目立たない作業を推奨。",
    "[OS ALERT] 上司の足音を検出。即座に作業内容を切り替えてください。",
    "[OS NOTICE] 本日はボスキー点検日です。正常に反応していますか？",
    "[OS ALERT] 社内ネットワーク上で監視信号を検出。慎重な行動を。",
    "[OS WARNING] 画面キャプチャが検出されました。",
    "[OS ALERT] ボスキーシステムの自動診断を開始します。しばらくお待ちください。",
    "[OS NOTICE] 休憩時間外の作業を検知。上司に注意される可能性があります。",
    "[OS WARNING] 画面の切替速度が低下しています。素早い操作を推奨。",
    "[OS ALERT] 新規ウィンドウの多重起動を検出。ボスキー誤作動の恐れあり。",
    "[OS NOTICE] 監視カメラの視線を感知。作業内容の安全性を再確認してください。",
    "[OS WARNING] ボスキーシステムのアップデートが必要です。",
    "[OS ALERT] 上司の気配を検出。即時の対応を推奨します。",
    "[OS NOTICE] 画面の占有率が高すぎます。ウィンドウを整理してください。",
    "[OS WARNING] ボスキーセンサーの感度が上昇中。誤発報に注意。"
]

MIN_INTERVAL = 30  # 最小発動間隔（秒）
MAX_INTERVAL = 180 # 最大発動間隔（秒）


def show_alert():
    message = random.choice(ALERT_MESSAGES)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} {message}")


def alert_loop(stop_event, interval_min=MIN_INTERVAL, interval_max=MAX_INTERVAL):
    while not stop_event.is_set():
        interval = random.randint(interval_min, interval_max)
        time.sleep(interval)
        show_alert()


def run_random_alerts(args):
    stop_event = threading.Event()
    t = threading.Thread(target=alert_loop, args=(stop_event, args.min_interval, args.max_interval))
    t.daemon = True
    t.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
        t.join()
        print("\n[INFO] ボスキー警告システムを終了しました。")


def run_once(args):
    show_alert()


def list_messages(args):
    print("-- OS公式風ボスキー警告メッセージ一覧 --")
    for i, msg in enumerate(ALERT_MESSAGES, 1):
        print(f"{i:2d}: {msg}")


def summary(args):
    print("random-os-fake-boss-key-alert: 作業空間に理不尽な緊張感をもたらす演出系スキルです。\n")
    print(f"登録メッセージ数: {len(ALERT_MESSAGES)}")
    print(f"発動間隔: {MIN_INTERVAL}～{MAX_INTERVAL}秒 (デフォルト)")
    print("本Skillは通知演出のみで、実際の画面制御は行いません。\n")


def main():
    parser = argparse.ArgumentParser(description="OS公式風ボスキー警告をランダムに表示する演出スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="ランダムなタイミングで警告を繰り返し表示")
    parser_run.add_argument("--min-interval", type=int, default=MIN_INTERVAL, help="警告の最小間隔(秒)")
    parser_run.add_argument("--max-interval", type=int, default=MAX_INTERVAL, help="警告の最大間隔(秒)")
    parser_run.set_defaults(func=run_random_alerts)

    parser_once = subparsers.add_parser("once", help="警告を1回だけ表示")
    parser_once.set_defaults(func=run_once)

    parser_list = subparsers.add_parser("list", help="全警告メッセージを一覧表示")
    parser_list.set_defaults(func=list_messages)

    parser_summary = subparsers.add_parser("summary", help="Skill概要を表示")
    parser_summary.set_defaults(func=summary)

    args = parser.parse_args()

    if not hasattr(args, 'func'):
        parser.print_help()
        sys.exit(1)
    args.func(args)

if __name__ == '__main__':
    main()
