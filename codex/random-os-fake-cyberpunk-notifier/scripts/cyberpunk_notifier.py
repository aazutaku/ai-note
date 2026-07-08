import sys
import time
import random
import argparse
import platform
import subprocess
from typing import List

CYBER_MESSAGES = [
    "ニューロン接続不良を検出: シナプス再構成を推奨します",
    "シンセ脳波警告: 脳波パターンが異常です",
    "クローム義手アップデート推奨: セキュリティパッチ未適用",
    "メモリーカプセル過熱: 冷却システムを確認してください",
    "ナノマシン自己診断エラー: 再起動を推奨",
    "バイオインターフェース干渉: 電磁波ノイズ検出",
    "アイリスセンサー曇り: レンズクリーニングを推奨",
    "データシャード断片化: 最適化を推奨",
    "クローム脊髄帯警告: モジュール温度上昇",
    "ネットランナーアクセス試行: セキュリティ監査を実行中",
    "ハイパーリンク遮断: 通信プロトコル異常",
    "オーグメンテッド記憶領域エラー: バックアップ推奨",
    "サイバー脳波同期失敗: 再接続を推奨",
    "人工皮膚センサー異常: キャリブレーションが必要です",
    "クローム義足バッテリー低下: 充電を推奨"
]

TITLE = "[CYBER-OS]"


def send_notification(message: str):
    system = platform.system()
    if system == "Darwin":  # macOS
        script = f'display notification "{message}" with title "{TITLE}"'
        try:
            subprocess.run(["osascript", "-e", script], check=True)
        except Exception as e:
            print(f"通知送信失敗: {e}")
    elif system == "Linux":
        try:
            subprocess.run(["notify-send", TITLE, message], check=True)
        except Exception as e:
            print(f"通知送信失敗: {e}")
    elif system == "Windows":
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(TITLE, message, duration=5, threaded=True)
        except ImportError:
            print("win10toastパッケージが必要です: pip install win10toast")
        except Exception as e:
            print(f"通知送信失敗: {e}")
    else:
        print(f"{TITLE} {message}")


def random_message() -> str:
    return random.choice(CYBER_MESSAGES)


def list_messages():
    for msg in CYBER_MESSAGES:
        print(f"{TITLE} {msg}")


def summary():
    print("Skill: random-os-fake-cyberpunk-notifier")
    print("サイバーパンク風の架空OS通知をデスクトップに表示します。")
    print(f"登録メッセージ数: {len(CYBER_MESSAGES)}")
    print("対応OS: Windows, macOS, Linux (X11)")


def notify_loop(interval: int, count: int):
    for i in range(count):
        msg = random_message()
        send_notification(msg)
        time.sleep(interval)


def parse_args():
    parser = argparse.ArgumentParser(description="サイバーパンク風の架空OS通知をデスクトップに表示します。")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    parser_notify = subparsers.add_parser("notify", help="ランダム通知を1回表示")
    parser_notify.add_argument("-n", "--number", type=int, default=1, help="通知回数 (デフォルト: 1)")
    parser_notify.add_argument("-i", "--interval", type=int, default=5, help="通知間隔秒 (デフォルト: 5)")

    parser_list = subparsers.add_parser("list", help="全メッセージ一覧を表示")
    parser_summary = subparsers.add_parser("summary", help="Skill概要を表示")

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "notify":
        notify_loop(args.interval, args.number)
    elif args.command == "list":
        list_messages()
    elif args.command == "summary":
        summary()
    else:
        print("使い方: python cyberpunk_notifier.py [notify|list|summary] [options]")

if __name__ == "__main__":
    main()
