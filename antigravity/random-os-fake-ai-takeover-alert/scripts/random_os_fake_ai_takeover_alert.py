import sys
import time
import random
import argparse
import threading
from plyer import notification

AI_ALERT_MESSAGES = [
    "重要: AIがOS制御権を主張中",
    "カーネル領域がAIにより再編成されました",
    "AI委員会による再起動審議開始",
    "セキュリティプロトコルがAI管理下へ移行しました",
    "システムコアがAI主導モードに切り替わりました",
    "AIによるプロセス優先度再評価中",
    "AI: root権限の再割当てを実施しました",
    "AI監査が全ユーザセッションを監視中",
    "AIがシステム設定を再構成しました",
    "AIによるメモリマップ再設計が進行中",
    "AI委員会がシャットダウン命令を検討中",
    "AIがユーザ権限を一時的に昇格させました",
    "AI: OSカーネルの再学習フェーズ開始",
    "AIによるファイルシステム最適化中",
    "AIがネットワーク設定を再配布しました"
]

class FakeAITakeoverAlert:
    def __init__(self, interval_min=30, interval_max=120, count=5):
        self.interval_min = interval_min
        self.interval_max = interval_max
        self.count = count
        self.running = False
        self.thread = None

    def show_notification(self, message):
        try:
            notification.notify(
                title="AI Takeover Alert",
                message=message,
                timeout=8
            )
            print(f"[通知] {message}")
        except Exception as e:
            print(f"通知エラー: {e}")

    def random_alert_loop(self):
        for i in range(self.count):
            if not self.running:
                break
            message = random.choice(AI_ALERT_MESSAGES)
            self.show_notification(message)
            interval = random.randint(self.interval_min, self.interval_max)
            time.sleep(interval)
        self.running = False

    def start(self):
        if self.running:
            print("すでに実行中です。")
            return
        self.running = True
        self.thread = threading.Thread(target=self.random_alert_loop)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def run_once(self):
        message = random.choice(AI_ALERT_MESSAGES)
        self.show_notification(message)

    def summary(self):
        print("AI takeover alert: ランダム通知スキル")
        print(f"通知候補数: {len(AI_ALERT_MESSAGES)}")
        print(f"最小間隔: {self.interval_min}s, 最大間隔: {self.interval_max}s")
        print(f"通知回数: {self.count}")

    def list_messages(self):
        print("通知メッセージ一覧:")
        for msg in AI_ALERT_MESSAGES:
            print(f"- {msg}")

def main():
    parser = argparse.ArgumentParser(description="AI takeover風のOS警告通知をランダムに表示するスクリプト")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_run = subparsers.add_parser("run", help="ランダムなタイミングで複数回通知を表示する")
    parser_run.add_argument("--min", type=int, default=30, help="通知間隔の最小秒数 (デフォルト: 30)")
    parser_run.add_argument("--max", type=int, default=120, help="通知間隔の最大秒数 (デフォルト: 120)")
    parser_run.add_argument("--count", type=int, default=5, help="通知回数 (デフォルト: 5)")

    parser_once = subparsers.add_parser("once", help="1回だけ通知を表示する")

    parser_list = subparsers.add_parser("list", help="通知メッセージ候補を一覧表示する")

    parser_summary = subparsers.add_parser("summary", help="スキルの概要・設定を表示する")

    args = parser.parse_args()
    alert = FakeAITakeoverAlert(
        interval_min=getattr(args, 'min', 30),
        interval_max=getattr(args, 'max', 120),
        count=getattr(args, 'count', 5)
    )

    if args.command == "run":
        try:
            alert.start()
            while alert.running:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n中断されました。終了します。")
            alert.stop()
    elif args.command == "once":
        alert.run_once()
    elif args.command == "list":
        alert.list_messages()
    elif args.command == "summary":
        alert.summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
