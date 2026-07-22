import random
import time
import argparse
import sys
from threading import Thread, Event

try:
    from plyer import notification
except ImportError:
    print("plyerモジュールが必要です。pip install plyer でインストールしてください。", file=sys.stderr)
    sys.exit(1)

ALERT_MESSAGES = [
    "CPU温存のため10分間キーボード操作を控えてください。",
    "電力節約モード: マウスの動きが多すぎます。しばらく静止してください。",
    "省エネ推奨: 画面を見つめすぎです。目を閉じて深呼吸しましょう。",
    "パワーセーブ: 思考が過熱しています。アイデアの発散を10分間抑制してください。",
    "バッテリー保護: 机の上のコーヒー消費量を減らしてください。",
    "省エネ警告: 椅子の上での姿勢を維持しすぎです。1分間立ち上がってください。",
    "OSパワーセーバー: ファイル保存回数が多すぎます。3分間保存を控えてください。",
    "省エネ: 画面の明るさを脳内で10%下げてください。",
    "電力節約: チームチャットの既読数が多すぎます。しばらく通知を無視してください。",
    "パワーセーブ: マウスクリックが過剰です。両手を膝に置いて深呼吸しましょう。"
]

NOTIFY_TITLE = "OSパワーセーバー警告"

class AlertThread(Thread):
    def __init__(self, interval_sec, stop_event):
        super().__init__()
        self.interval_sec = interval_sec
        self.stop_event = stop_event
        self.daemon = True

    def run(self):
        while not self.stop_event.is_set():
            msg = random.choice(ALERT_MESSAGES)
            try:
                notification.notify(
                    title=NOTIFY_TITLE,
                    message=msg,
                    timeout=8
                )
                print(f"[通知] {NOTIFY_TITLE}: {msg}")
            except Exception as e:
                print(f"通知送信エラー: {e}", file=sys.stderr)
            for _ in range(self.interval_sec):
                if self.stop_event.is_set():
                    break
                time.sleep(1)

def list_alerts():
    print("--- 登録済みパワーセーバー警告メッセージ一覧 ---")
    for i, msg in enumerate(ALERT_MESSAGES, 1):
        print(f"{i}. {msg}")

def add_alert(msg):
    global ALERT_MESSAGES
    if msg.strip() and msg not in ALERT_MESSAGES:
        ALERT_MESSAGES.append(msg)
        print(f"追加しました: {msg}")
    else:
        print("既に登録済み、または空文字です。")

def remove_alert(idx):
    global ALERT_MESSAGES
    try:
        idx = int(idx) - 1
        if 0 <= idx < len(ALERT_MESSAGES):
            removed = ALERT_MESSAGES.pop(idx)
            print(f"削除しました: {removed}")
        else:
            print("インデックスが範囲外です。")
    except Exception as e:
        print(f"削除失敗: {e}")

def main():
    parser = argparse.ArgumentParser(description="ランダムなOS風パワーセーバー警告をデスクトップ通知で表示するスクリプト")
    subparsers = parser.add_subparsers(dest="command", required=False)

    run_parser = subparsers.add_parser("run", help="一定間隔でランダム警告を通知 (デフォルト)")
    run_parser.add_argument("-i", "--interval", type=int, default=600, help="通知間隔(秒)。デフォルト600秒")
    run_parser.add_argument("-c", "--count", type=int, default=0, help="通知回数。0で無限ループ")

    list_parser = subparsers.add_parser("list", help="登録済み警告メッセージ一覧表示")
    add_parser = subparsers.add_parser("add", help="警告メッセージを追加")
    add_parser.add_argument("message", type=str, help="追加する警告メッセージ")
    remove_parser = subparsers.add_parser("remove", help="警告メッセージを削除")
    remove_parser.add_argument("index", type=int, help="削除するメッセージ番号 (1始まり)")

    args = parser.parse_args()

    if args.command == "list":
        list_alerts()
        return
    elif args.command == "add":
        add_alert(args.message)
        return
    elif args.command == "remove":
        remove_alert(args.index)
        return
    else:
        interval = getattr(args, 'interval', 600)
        count = getattr(args, 'count', 0)
        stop_event = Event()
        alert_thread = AlertThread(interval, stop_event)
        alert_thread.start()
        try:
            n = 0
            while True:
                if count and n >= count:
                    stop_event.set()
                    break
                time.sleep(1)
                if not alert_thread.is_alive():
                    break
                n += 1
        except KeyboardInterrupt:
            print("\n終了します。")
            stop_event.set()
        alert_thread.join()

if __name__ == '__main__':
    main()
