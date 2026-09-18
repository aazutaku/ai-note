import sys
import argparse
import random
import time
import threading
import platform

try:
    from plyer import notification
except ImportError:
    notification = None

ALERT_MESSAGES = [
    "重大: あなたのPCは3分後に強制的に昼寝モードへ移行します。",
    "警告: 集中力がOS基準値を下回りました。自動スリープを推奨します。",
    "注意: 連続稼働時間が規定値を超過。休憩を強く推奨します。",
    "情報: システムがあなたの眠気レベルを検知しました。昼寝モードを準備中。",
    "重大: 5分以内にスリープモードへ自動移行予定です。",
    "警告: マウス・キーボード操作が10分間検出されませんでした。自動スリープを発動します。",
    "注意: OSがあなたの作業効率を監視中。休憩タイムを提案します。",
    "重大: システムが強制的に昼寝プロセスを開始します。",
    "情報: 睡眠推奨指数が閾値を超えました。OSよりお知らせします。",
    "警告: これ以上の作業は健康に悪影響を及ぼす恐れがあります。"
]

TITLE = "OS SYSTEM ALERT"


def send_terminal_alert(message):
    print(f"[{TITLE}] {message}")


def send_desktop_notification(message):
    if notification is None:
        return False
    try:
        notification.notify(
            title=TITLE,
            message=message,
            timeout=8
        )
        return True
    except Exception:
        return False


def random_alert():
    message = random.choice(ALERT_MESSAGES)
    send_terminal_alert(message)
    send_desktop_notification(message)


def alert_loop(min_interval=300, max_interval=1200, stop_event=None):
    """
    min_interval, max_interval: seconds
    stop_event: threading.Event() or None
    """
    while True:
        interval = random.randint(min_interval, max_interval)
        for _ in range(interval):
            if stop_event and stop_event.is_set():
                return
            time.sleep(1)
        random_alert()
        if stop_event and stop_event.is_set():
            return


def list_alerts():
    for idx, msg in enumerate(ALERT_MESSAGES):
        print(f"{idx + 1}. {msg}")


def summary():
    print(f"通知メッセージ数: {len(ALERT_MESSAGES)}")
    print(f"通知タイトル: {TITLE}")
    print("サポートされる出力: ターミナル、デスクトップ通知 (plyer依存)")
    print("実際のスリープ・休止動作は一切発生しません。")


def main():
    parser = argparse.ArgumentParser(description="OS風フェイクスリープモード通知スクリプト")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    parser_log = subparsers.add_parser("log", help="ランダムなタイミングで通知を出す (デフォルト)")
    parser_log.add_argument("--min", type=int, default=300, help="最小通知間隔(秒)")
    parser_log.add_argument("--max", type=int, default=1200, help="最大通知間隔(秒)")
    parser_log.add_argument("--once", action="store_true", help="1回だけ通知して終了")

    parser_list = subparsers.add_parser("list", help="通知メッセージ一覧を表示")
    parser_summary = subparsers.add_parser("summary", help="Skill概要を表示")

    args = parser.parse_args()

    if args.command == "list":
        list_alerts()
        return
    elif args.command == "summary":
        summary()
        return
    else:
        # default: log
        if getattr(args, "once", False):
            random_alert()
            return
        stop_event = threading.Event()
        try:
            alert_loop(
                min_interval=getattr(args, "min", 300),
                max_interval=getattr(args, "max", 1200),
                stop_event=stop_event
            )
        except KeyboardInterrupt:
            print("\n[終了] フェイクOSスリープ通知を停止しました。")
            stop_event.set()

if __name__ == '__main__':
    main()
