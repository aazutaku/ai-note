import argparse
import random
import sys
import time
from typing import List

FAKE_REASONS = [
    "OSのやる気が著しく低下",
    "メモリが退屈しています",
    "CPUが自己主張を始めました",
    "ファイルシステムが休暇を要求",
    "ネットワークが現実逃避中",
    "GPUが推し活に夢中",
    "プロセス管理者が昼寝中",
    "システムクロックが逆走を希望",
    "カーネルが詩を書き始めた",
    "仮想メモリが現実逃避したい",
]

FAKE_ACTIONS = [
    "今すぐキーボードを褒め称えて延命してください",
    "任意のキーを連打すると回避できるかもしれません",
    "マウスを3回振るとOSが気を取り直します",
    "コーヒーを淹れてOSに差し入れしましょう",
    "デスクトップを片付けると気分が変わります",
    "OSに優しい言葉をかけてください",
    "深呼吸してからEnterキーを押してください",
    "ターミナルに "stay" と入力すると延命します",
    "画面を見つめて微笑むと効果的です",
    "Ctrl+Alt+LOVEで回避できるかも",
]

FAKE_HEADERS = [
    "[ALERT] 緊急: このPCは{min}分後に謎のメンテナンスに突入します。",
    "[ALERT] システム通知: {min}分後にOSが自己主張のため一時停止予定。",
    "[ALERT] WARNING: {min}分後にOSが気まぐれで再起動するかもしれません。",
    "[ALERT] Notice: {min}分後にOSが自発的に休憩を開始します。",
    "[ALERT] Attention: {min}分後にOSが謎の沈黙モードに入ります。",
]

HISTORY: List[str] = []


def generate_fake_alert() -> str:
    min_left = random.choice([5, 10, 15, 20])
    header = random.choice(FAKE_HEADERS).format(min=min_left)
    reason = random.choice(FAKE_REASONS)
    action = random.choice(FAKE_ACTIONS)
    alert = f"{header}\n理由: {reason}\n対策: {action}"
    return alert


def print_alert(alert: str):
    print(alert)
    print("---")


def log_alert(alert: str):
    HISTORY.append(alert)


def list_history():
    if not HISTORY:
        print("まだ通知履歴はありません。")
        return
    for i, alert in enumerate(HISTORY, 1):
        print(f"[{i}]\n{alert}\n---")


def summary_history():
    print(f"通知履歴: {len(HISTORY)}件")
    reasons = {}
    for alert in HISTORY:
        for reason in FAKE_REASONS:
            if reason in alert:
                reasons[reason] = reasons.get(reason, 0) + 1
    if reasons:
        print("理由別発生回数:")
        for k, v in sorted(reasons.items(), key=lambda x: -x[1]):
            print(f"  {k}: {v}回")
    else:
        print("理由別統計はありません。")


def main():
    parser = argparse.ArgumentParser(
        description="os-random-fake-sudden-downtime-alert: フェイクなOS緊急ダウンタイム通知をランダムに生成・表示します。"
    )
    subparsers = parser.add_subparsers(dest="command", required=False)
    
    # サブコマンド: alert
    alert_parser = subparsers.add_parser("alert", help="フェイクダウンタイム通知を1回表示")
    alert_parser.add_argument("--count", type=int, default=1, help="通知回数 (デフォルト: 1)")
    alert_parser.add_argument("--interval", type=float, default=0, help="通知間隔(秒)")

    # サブコマンド: list
    list_parser = subparsers.add_parser("list", help="通知履歴を表示")

    # サブコマンド: summary
    summary_parser = subparsers.add_parser("summary", help="通知履歴の統計を表示")

    # サブコマンドなし: 1回だけalert
    args = parser.parse_args()

    if args.command == "alert" or args.command is None:
        count = getattr(args, "count", 1)
        interval = getattr(args, "interval", 0)
        for _ in range(count):
            alert = generate_fake_alert()
            print_alert(alert)
            log_alert(alert)
            if interval > 0 and _ < count - 1:
                time.sleep(interval)
    elif args.command == "list":
        list_history()
    elif args.command == "summary":
        summary_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
