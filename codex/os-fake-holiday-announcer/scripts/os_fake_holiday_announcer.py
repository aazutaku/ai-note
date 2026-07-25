import sys
import os
import random
import json
import time
import argparse
from datetime import datetime, timedelta

try:
    from plyer import notification
except ImportError:
    print("plyerパッケージが必要です。pip install plyer でインストールしてください。", file=sys.stderr)
    sys.exit(1)

HOLIDAY_MESSAGES = [
    "本日はバグ記念日につき全業務停止となります。",
    "緊急：OSが自主休暇を宣言しました。午後は全プロセスおやすみです。",
    "システム都合により15時から強制昼寝タイムが発動します。",
    "本日は“メモリ解放記念日”のため、全員で休憩しましょう。",
    "OSアップデート記念日！全タスクは自動的に中断されます。",
    "セグメンテーション違反追悼日：今日は何もしてはいけません。",
    "CPU温度上昇記念日：冷却のため業務停止します。",
    "ファイルシステムの気まぐれ休暇：保存作業は一切不要です。",
    "OSがサボりたがっています。全員で一緒にサボりましょう。",
    "今日は“仮想メモリ拡張記念日”のため、作業量も拡張休暇です。"
]

HISTORY_FILE = os.path.expanduser("~/.os_fake_holiday_history.json")
FREQ_LIMIT_MINUTES = 60  # 1時間に1回まで


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []


def save_history(history):
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"履歴保存に失敗しました: {e}", file=sys.stderr)


def can_announce():
    history = load_history()
    if not history:
        return True
    last = history[-1]
    last_time = datetime.fromisoformat(last['timestamp'])
    now = datetime.now()
    diff = now - last_time
    return diff >= timedelta(minutes=FREQ_LIMIT_MINUTES)


def announce_fake_holiday():
    if not can_announce():
        print("通知頻度制限中です。しばらくお待ちください。", file=sys.stderr)
        return
    message = random.choice(HOLIDAY_MESSAGES)
    title = "OS公式休日発表"
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="os-fake-holiday-announcer",
            timeout=10
        )
        print(f"[通知] {title}: {message}")
        # 履歴保存
        history = load_history()
        history.append({
            "timestamp": datetime.now().isoformat(),
            "message": message
        })
        # 履歴は直近50件まで保持
        save_history(history[-50:])
    except Exception as e:
        print(f"通知に失敗しました: {e}", file=sys.stderr)


def list_history():
    history = load_history()
    if not history:
        print("通知履歴はありません。")
        return
    for item in history:
        ts = item.get("timestamp", "?")
        msg = item.get("message", "?")
        print(f"{ts[:19]} - {msg}")


def summary():
    history = load_history()
    print(f"これまでの通知回数: {len(history)} 回")
    if history:
        last = history[-1]
        print(f"最終通知: {last['timestamp'][:19]} - {last['message']}")
    else:
        print("まだ通知はありません。")


def main():
    parser = argparse.ArgumentParser(description="os-fake-holiday-announcer: OSが謎の休日を勝手に宣言する通知演出ツール")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("announce", help="ランダムなOS公式休日を通知する")
    subparsers.add_parser("list", help="通知履歴を表示する")
    subparsers.add_parser("summary", help="通知履歴のサマリーを表示する")

    args = parser.parse_args()

    if args.command == "announce":
        announce_fake_holiday()
    elif args.command == "list":
        list_history()
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
