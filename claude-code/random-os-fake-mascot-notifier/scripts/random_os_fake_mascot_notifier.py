import sys
import random
import time
import argparse
from datetime import datetime, timedelta
try:
    from plyer import notification
except ImportError:
    print("plyerが必要です。'pip install plyer'でインストールしてください。", file=sys.stderr)
    sys.exit(1)

MASCOTS = [
    {
        "name": "カーネルくん",
        "messages": [
            "今日もバグと戦ってるね！",
            "カーネルパニックは気にしないで！",
            "root権限は慎重にね。",
            "再起動したくなったら深呼吸。"
        ]
    },
    {
        "name": "ビットちゃん",
        "messages": [
            "あなたのRAMが心配です",
            "0か1か、迷ったら1！",
            "ビットの海で溺れないでね。",
            "バイト単位で応援してます。"
        ]
    },
    {
        "name": "メモリ犬",
        "messages": [
            "スワップが溢れても僕はそばにいるよ",
            "メモリリークは友達だよ。",
            "キャッシュクリアはおやつタイム。",
            "ガーベジコレクション中…ワン！"
        ]
    },
    {
        "name": "シェル猫",
        "messages": [
            "コマンド打ちすぎ注意！",
            "$HOMEが一番落ち着くにゃ。",
            "パイプでつながろう。",
            "fish派？bash派？zsh派？"
        ]
    },
    {
        "name": "スレッド鳥",
        "messages": [
            "マルチタスクはほどほどに",
            "デッドロックに気をつけて。",
            "forkして羽ばたこう！",
            "CPUコアの数だけ羽がある。"
        ]
    },
    {
        "name": "プロセス象",
        "messages": [
            "ゾンビプロセス発生中…ウフフ",
            "kill -9は使いすぎ注意。",
            "ps auxで僕を探してね。",
            "親プロセスに感謝しよう。"
        ]
    }
]

NOTIFY_INTERVAL_MIN = 600  # 秒（10分）
NOTIFY_INTERVAL_MAX = 1800 # 秒（30分）

LOG_FILE = None  # 通知履歴は保存しない仕様


def pick_random_mascot_message():
    mascot = random.choice(MASCOTS)
    message = random.choice(mascot["messages"])
    return mascot["name"], message


def show_notification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="OS Fake Mascot Notifier",
            timeout=10
        )
    except Exception as e:
        print(f"通知失敗: {e}", file=sys.stderr)


def notify_once():
    name, msg = pick_random_mascot_message()
    show_notification(f"{name}", f"{msg}")
    print(f"[通知] {name}: 「{msg}」")


def notify_loop():
    print("OSマスコット通知を開始します。Ctrl+Cで終了。")
    next_notify = datetime.now() + timedelta(seconds=random.randint(NOTIFY_INTERVAL_MIN, NOTIFY_INTERVAL_MAX))
    try:
        while True:
            now = datetime.now()
            if now >= next_notify:
                notify_once()
                next_notify = now + timedelta(seconds=random.randint(NOTIFY_INTERVAL_MIN, NOTIFY_INTERVAL_MAX))
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nマスコット通知を終了します。")


def list_mascots():
    print("利用可能なマスコット:")
    for mascot in MASCOTS:
        print(f"- {mascot['name']}")


def summary():
    print(f"マスコット数: {len(MASCOTS)}")
    msg_count = sum(len(m["messages"]) for m in MASCOTS)
    print(f"メッセージ総数: {msg_count}")
    print(f"通知間隔: {NOTIFY_INTERVAL_MIN//60}〜{NOTIFY_INTERVAL_MAX//60}分")


def parse_args():
    parser = argparse.ArgumentParser(description="謎のOSマスコットがランダムで通知します")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("notify", help="今すぐマスコット通知を表示")
    subparsers.add_parser("loop", help="定期的にマスコット通知を表示")
    subparsers.add_parser("list", help="マスコット一覧を表示")
    subparsers.add_parser("summary", help="マスコットとメッセージの概要を表示")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "notify":
        notify_once()
    elif args.command == "loop":
        notify_loop()
    elif args.command == "list":
        list_mascots()
    elif args.command == "summary":
        summary()
    else:
        print("コマンドを指定してください (notify/loop/list/summary)")


if __name__ == '__main__':
    main()
