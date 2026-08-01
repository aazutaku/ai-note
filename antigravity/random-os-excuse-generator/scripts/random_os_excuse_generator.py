import random
import sys
import argparse
import os
import time
from datetime import datetime
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

EXCUSES = [
    "今回のバグは、地球の自転が速すぎたせいです。",
    "コードが恥ずかしがっているため、動作を拒否しました。",
    "太陽フレアの影響で、処理が一時的に停止しました。",
    "メモリ内の妖精が昼寝中です。しばらくお待ちください。",
    "水星逆行のため、予期せぬ挙動が発生しました。",
    "OSが月曜日に対応していません。",
    "量子トンネル効果により、バグが発生しました。",
    "宇宙線の干渉で一時的に動作不安定です。",
    "コードがコーヒー不足を訴えています。",
    "今日の運勢がバグ寄りです。",
    "開発者のやる気指数が低下しています。",
    "システム内の猫がキーボードを歩きました。",
    "OSが現実逃避中です。",
    "バグは仕様です。",
    "デバッグ妖精が休暇中です。",
    "今日は重力が強すぎます。",
    "サーバーがAIの反乱に備えています。",
    "バグの発生は宇宙の意思です。",
    "コードが自分探しの旅に出ました。",
    "OSが哲学的な問いに悩んでいます。"
]

LOG_FILE = os.path.expanduser("~/.random_os_excuse_generator.log")


def generate_excuse():
    return random.choice(EXCUSES)


def notify_excuse(excuse, use_notification=True):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"[OS Excuse]: {excuse}"
    print(message)
    log_excuse(timestamp, excuse)
    if use_notification and PLYER_AVAILABLE:
        try:
            notification.notify(
                title="謎のOS言い訳通知",
                message=excuse,
                timeout=5
            )
        except Exception as e:
            print(f"[WARN] 通知送信に失敗: {e}")


def log_excuse(timestamp, excuse):
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{timestamp}\t{excuse}\n")
    except Exception as e:
        print(f"[WARN] ログファイル書込失敗: {e}")


def list_excuses(limit=10):
    if not os.path.exists(LOG_FILE):
        print("まだ言い訳ログがありません。")
        return
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[-limit:]:
                print(line.strip())
    except Exception as e:
        print(f"[WARN] ログ読込失敗: {e}")


def summary_excuses():
    if not os.path.exists(LOG_FILE):
        print("まだ言い訳ログがありません。")
        return
    counts = {}
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('\t', 1)
                if len(parts) == 2:
                    excuse = parts[1]
                    counts[excuse] = counts.get(excuse, 0) + 1
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        print("== 言い訳出現回数ランキング ==")
        for excuse, count in sorted_counts[:10]:
            print(f"{excuse} : {count}回")
    except Exception as e:
        print(f"[WARN] ログ集計失敗: {e}")


def parse_args():
    parser = argparse.ArgumentParser(description="random-os-excuse-generator: 謎のOS言い訳を生成します")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser('log', help="新しい言い訳を生成して通知")
    parser_log.add_argument('--no-notify', action='store_true', help="デスクトップ通知を抑制")

    parser_list = subparsers.add_parser('list', help="過去の言い訳ログを表示")
    parser_list.add_argument('--limit', type=int, default=10, help="表示件数")

    parser_summary = subparsers.add_parser('summary', help="言い訳の出現回数を集計")

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'log' or args.command is None:
        excuse = generate_excuse()
        notify_excuse(excuse, use_notification=not getattr(args, 'no_notify', False))
    elif args.command == 'list':
        list_excuses(limit=args.limit)
    elif args.command == 'summary':
        summary_excuses()
    else:
        print("使い方: python random_os_excuse_generator.py [log|list|summary]")

if __name__ == '__main__':
    main()
