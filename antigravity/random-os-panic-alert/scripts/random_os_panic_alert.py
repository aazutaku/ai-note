import sys
import os
import time
import random
import argparse
import platform
import subprocess
from datetime import datetime, timedelta

PANIC_MESSAGES = [
    "カーネルがランチに出ました。システムはしばらく無防備です。",
    "仮想メモリが現実逃避中です。復帰をお待ちください。",
    "ビットが逃走しました。全力で捜索中です。",
    "プロセスIDが自己を見失いました。",
    "セグメンテーション・ファウンド。問題ありません。",
    "ファイルシステムが詩的表現を始めました。",
    "CPUが瞑想モードに入りました。",
    "ネットワークが自分探しの旅に出ました。",
    "バッファが感情的になっています。",
    "スレッドが人生を考え直しています。",
    "システムクロックが未来にジャンプしました。",
    "デバイスドライバが休暇を申請しました。",
    "ユーザ空間が拡大解釈中です。",
    "カーネルパニック（ただし今日は平和です）。",
    "メモリリークが詩を書き始めました。"
]

NOTIFY_HISTORY = []
MAX_HISTORY = 10
MIN_INTERVAL_SEC = 600  # 10分以上間隔を空ける


def get_random_message():
    return random.choice(PANIC_MESSAGES)


def can_notify():
    now = datetime.now()
    # 履歴がなければOK
    if not NOTIFY_HISTORY:
        return True
    # 最後の通知から十分経過しているか
    last_time = NOTIFY_HISTORY[-1]
    if (now - last_time).total_seconds() >= MIN_INTERVAL_SEC:
        return True
    return False


def record_notify():
    now = datetime.now()
    NOTIFY_HISTORY.append(now)
    # 履歴をMAX_HISTORY件に制限
    if len(NOTIFY_HISTORY) > MAX_HISTORY:
        NOTIFY_HISTORY.pop(0)


def send_notification(title, message):
    system = platform.system()
    try:
        if system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=7, threaded=True)
            except ImportError:
                print("win10toastがインストールされていません。pip install win10toast で導入してください。")
        elif system == "Darwin":
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script])
        elif system == "Linux":
            subprocess.run(["notify-send", title, message])
        else:
            print(f"[{title}]\n{message}")
    except Exception as e:
        print(f"通知送信に失敗しました: {e}")


def log_notification(title, message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{now}] {title}: {message}\n"
    # ローカルファイル保存はしない設計
    pass


def list_messages():
    print("=== 登録済みパニックメッセージ一覧 ===")
    for i, msg in enumerate(PANIC_MESSAGES, 1):
        print(f"{i}. {msg}")


def summary():
    print("=== random-os-panic-alert ステータス ===")
    print(f"通知履歴件数: {len(NOTIFY_HISTORY)}")
    if NOTIFY_HISTORY:
        print(f"最終通知: {NOTIFY_HISTORY[-1].strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("まだ通知はありません。")
    print(f"通知間隔(最小): {MIN_INTERVAL_SEC // 60}分")
    print(f"登録メッセージ数: {len(PANIC_MESSAGES)}")


def trigger_alert():
    if can_notify():
        title = "OS Panic Alert"
        message = get_random_message()
        send_notification(title, message)
        record_notify()
        log_notification(title, message)
    else:
        print("通知間隔が短すぎるため、今回はスキップされました。")


def main():
    parser = argparse.ArgumentParser(description="random-os-panic-alert: 謎のOSパニックアラートをランダム通知します。")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="即座にパニック通知を発生させる")
    parser_list = subparsers.add_parser("list", help="登録済みパニックメッセージ一覧を表示")
    parser_summary = subparsers.add_parser("summary", help="通知履歴と設定の要約を表示")

    args = parser.parse_args()

    if args.command == "alert":
        trigger_alert()
    elif args.command == "list":
        list_messages()
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
