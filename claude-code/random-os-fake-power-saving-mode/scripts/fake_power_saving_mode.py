import argparse
import random
import sys
import datetime
from typing import List

FAKE_NOTIFICATIONS = [
    "システムは自動的に『全アプリ低消費電力モード』に移行しました。",
    "キーボード省入力モード発動。タイプ速度を自動的に最適化します。",
    "OSが独断でパフォーマンス調整中。全てが遅く感じるかもしれません。",
    "画面の明るさを自動で最小に設定しました（実際には変更されません）。",
    "バッテリー節約のため、全プロセスを仮想的にスローダウン中。",
    "省エネモード: 全ウィンドウの彩度を自動調整（実際には何も変わりません）。",
    "CPU使用率を仮想的に制限中。パフォーマンス低下を感じても気のせいです。",
    "OSが独自判断でネットワーク通信を最適化中（実際には変化なし）。",
    "バッテリー寿命延長のため、全アプリをフェイク休止状態に移行します。",
    "省エネのため、全ての通知音を無音化しました（実際には鳴ります）。"
]

LOG_FILE = ".claude/skills/random-os-fake-power-saving-mode/notifications.log"


def print_notification(msg: str):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[OS通知] {msg}")
    log_notification(timestamp, msg)


def log_notification(timestamp: str, msg: str):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} | {msg}\n")
    except Exception as e:
        print(f"[ERROR] ログファイルへの書き込みに失敗しました: {e}", file=sys.stderr)


def list_notifications(limit: int = 10):
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            print("通知履歴はありません。")
            return
        for line in lines[-limit:]:
            print(line.strip())
    except FileNotFoundError:
        print("通知履歴ファイルが存在しません。")
    except Exception as e:
        print(f"[ERROR] 履歴の読み込みに失敗しました: {e}", file=sys.stderr)


def summary_notifications():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        total = len(lines)
        if total == 0:
            print("通知履歴はありません。")
            return
        types = {}
        for line in lines:
            msg = line.strip().split("|", 1)[-1].strip()
            types[msg] = types.get(msg, 0) + 1
        print(f"通知履歴: 合計{total}件\n---")
        for msg, count in sorted(types.items(), key=lambda x: -x[1]):
            print(f"{msg} : {count}回")
    except FileNotFoundError:
        print("通知履歴ファイルが存在しません。")
    except Exception as e:
        print(f"[ERROR] サマリーの取得に失敗しました: {e}", file=sys.stderr)


def trigger_random_notification(count: int = 1):
    for _ in range(count):
        msg = random.choice(FAKE_NOTIFICATIONS)
        print_notification(msg)


def clear_notifications():
    try:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("")
        print("通知履歴をクリアしました。")
    except Exception as e:
        print(f"[ERROR] 履歴のクリアに失敗しました: {e}", file=sys.stderr)


def parse_args():
    parser = argparse.ArgumentParser(
        description="謎のOSフェイク省エネモード通知をランダム生成・履歴管理するスクリプト"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_log = subparsers.add_parser("log", help="ランダムなフェイク通知を生成")
    parser_log.add_argument("-n", "--num", type=int, default=1, help="生成する通知数")

    parser_list = subparsers.add_parser("list", help="通知履歴を表示")
    parser_list.add_argument("-l", "--limit", type=int, default=10, help="表示件数")

    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリーを表示")
    parser_clear = subparsers.add_parser("clear", help="通知履歴をクリア")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "log":
        trigger_random_notification(args.num)
    elif args.command == "list":
        list_notifications(args.limit)
    elif args.command == "summary":
        summary_notifications()
    elif args.command == "clear":
        clear_notifications()
    else:
        print("不明なコマンドです。-h で使い方を確認してください。", file=sys.stderr)


if __name__ == "__main__":
    main()
