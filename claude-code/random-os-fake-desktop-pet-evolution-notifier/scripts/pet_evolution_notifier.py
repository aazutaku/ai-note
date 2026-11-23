import random
import argparse
import sys
from datetime import datetime

# ペット進化・誕生パターンのデータ
OBJECTS = [
    "マウスポインタ", "キーボード", "デスクトップ", "ウィンドウ枠", "ターミナル", "タスクバー", "ファイルアイコン", "通知領域", "クリップボード", "スクリーンセーバー"
]

EVOLUTIONS = [
    "幻のカメレオン形態", "サボテン系ペット", "空飛ぶクラゲ型ペット", "忍者リス形態", "光るカタツムリ型ペット", "モフモフ雪ウサギ形態", "サイボーグハムスター形態", "ミニドラゴン型ペット", "透明カエル形態", "フワフワ雲ペット"
]

ACTIONS = [
    "進化しました", "が宿ります", "が誕生しました", "へ進化しました", "が出現中です", "に変身しました", "に融合しました", "が覚醒しました", "が大発生しています", "が降臨しました"
]

PREFIXES = [
    "[OS公式通知] ", "[謎のOS通知] ", "[デスクトップペット速報] ", "[非公式システムアナウンス] "
]

# ログ保存用（ファイル保存はしない、安全設計）
LOG_HISTORY = []


def generate_notification():
    obj = random.choice(OBJECTS)
    evo = random.choice(EVOLUTIONS)
    act = random.choice(ACTIONS)
    prefix = random.choice(PREFIXES)
    today = datetime.now().strftime('%Y-%m-%d')
    if act.startswith("が"):
        msg = f"{prefix}{today} {obj}は本日“{evo}”{act}。"
    elif act.startswith("に") or act.startswith("へ"):
        msg = f"{prefix}{today} {obj}{act}“{evo}”に。"
    else:
        msg = f"{prefix}{today} {obj}は“{evo}”{act}。"
    return msg


def log_notification(msg):
    LOG_HISTORY.append(msg)


def print_notification():
    msg = generate_notification()
    print(msg)
    log_notification(msg)


def list_notifications():
    if not LOG_HISTORY:
        print("まだ通知履歴はありません。")
        return
    print("--- 通知履歴 ---")
    for i, msg in enumerate(LOG_HISTORY[-10:], 1):
        print(f"{i}. {msg}")


def summary_notifications():
    print(f"これまでに{len(LOG_HISTORY)}件の謎ペット通知を生成しました。")
    evolutions = set()
    for msg in LOG_HISTORY:
        for evo in EVOLUTIONS:
            if evo in msg:
                evolutions.add(evo)
    print(f"登場した進化形態: {', '.join(list(evolutions))}")


def parse_args():
    parser = argparse.ArgumentParser(description="謎のOSデスクトップペット進化通知スクリプト")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("notify", help="ランダムな進化通知を1件生成・表示")
    subparsers.add_parser("list", help="直近10件の通知履歴を表示")
    subparsers.add_parser("summary", help="通知履歴のサマリーを表示")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "notify":
        print_notification()
    elif args.command == "list":
        list_notifications()
    elif args.command == "summary":
        summary_notifications()
    else:
        print("不明なコマンドです。--helpを参照してください。", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
