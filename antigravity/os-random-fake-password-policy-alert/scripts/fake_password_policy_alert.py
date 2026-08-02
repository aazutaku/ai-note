import sys
import random
import time
import argparse
import threading
import notify2
from datetime import datetime

# 偽パスワードポリシー文言候補
POLICY_MESSAGES = [
    "本日よりパスワードは『季節の俳句＋円周率12桁＋好きな給食メニュー』を含める必要があります。",
    "新ルール：母音だけのパスワードは使用禁止となりました。",
    "推奨：毎日ランダムなパスワードに変更し、記憶しないでください。",
    "重要：パスワードには最低1つの元素記号と3つの旧国名を含めてください。",
    "注意：パスワードに『password』や『1234』を含めると即時退場となります。",
    "新基準：パスワードは1日ごとに漢字→カタカナ→ひらがな→英語でローテーションしてください。",
    "必須：パスワードの末尾に好きな給食メニューをつけてください。",
    "推奨：パスワード生成にはサイコロを使い、出た目の数だけ母音を増やしてください。",
    "特例：月曜日のみパスワードの最初に『月』を追加してください。",
    "注意：パスワードに記号を10種類以上含めることが義務化されました。"
]

REFERENCE_LINK = "詳細は社内Wiki『謎のポリシー集』参照。"

# 通知タイトル
NOTIFY_TITLE = "OSパスワードポリシー変更のお知らせ"

# 通知の組み立て
def generate_fake_policy():
    count = random.randint(2, 4)
    messages = random.sample(POLICY_MESSAGES, count)
    body = "\n".join([f"・{m}" for m in messages])
    return f"【重要】{NOTIFY_TITLE}\n{body}\n\n【参考】\n{REFERENCE_LINK}"

# デスクトップ通知
def send_notification(message):
    try:
        notify2.init("FakePasswordPolicy")
        n = notify2.Notification(NOTIFY_TITLE, message)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.set_timeout(10000)  # 10秒
        n.show()
    except Exception as e:
        print(f"[ERROR] 通知送信に失敗しました: {e}")

# ログ記録（標準出力のみ）
def log_notification(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] 通知発生:\n{message}\n{'-'*40}")

# 通知発火スレッド
class NotificationThread(threading.Thread):
    def __init__(self, interval_min=300, interval_max=1200):
        super().__init__()
        self.interval_min = interval_min
        self.interval_max = interval_max
        self._running = True

    def stop(self):
        self._running = False

    def run(self):
        while self._running:
            sleep_time = random.randint(self.interval_min, self.interval_max)
            time.sleep(sleep_time)
            message = generate_fake_policy()
            send_notification(message)
            log_notification(message)

# CLIサブコマンド

def main():
    parser = argparse.ArgumentParser(description="OSランダム偽パスワードポリシー通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    # 通知を1回だけ出す
    parser_once = subparsers.add_parser("once", help="偽パスワードポリシー通知を1回表示")

    # 通知を定期的に出す
    parser_daemon = subparsers.add_parser("daemon", help="定期的に通知を表示 (デフォルト:5-20分間隔)")
    parser_daemon.add_argument("--min", type=int, default=300, help="最小間隔(秒)")
    parser_daemon.add_argument("--max", type=int, default=1200, help="最大間隔(秒)")

    # 通知文面のサンプルを表示
    parser_sample = subparsers.add_parser("sample", help="偽ポリシー文面をランダム生成して標準出力")
    parser_sample.add_argument("-n", type=int, default=3, help="生成数")

    args = parser.parse_args()
    if args.command == "once":
        message = generate_fake_policy()
        send_notification(message)
        log_notification(message)
    elif args.command == "daemon":
        t = NotificationThread(interval_min=args.min, interval_max=args.max)
        t.daemon = True
        t.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            t.stop()
            print("終了します。")
    elif args.command == "sample":
        for _ in range(args.n):
            message = generate_fake_policy()
            print(message)
            print("-"*40)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
