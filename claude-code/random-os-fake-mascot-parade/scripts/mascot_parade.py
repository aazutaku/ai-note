import argparse
import random
import sys
import threading
import time
from datetime import datetime

try:
    from plyer import notification
except ImportError:
    notification = None
    print("plyerがインストールされていません。pip install plyer で導入してください。")

MASCOTS = [
    {"name": "カーネルくん", "traits": ["安定志向", "真面目"]},
    {"name": "メモリねずみ", "traits": ["すばしっこい", "忘れっぽい"]},
    {"name": "シェルパンダ", "traits": ["のんびり", "コマンド好き"]},
    {"name": "スワップタコ", "traits": ["粘り強い", "仮想好き"]},
    {"name": "デバイスきつね", "traits": ["新しもの好き", "いたずら好き"]},
    {"name": "プロセスうさぎ", "traits": ["多忙", "分身の術"]},
    {"name": "ログふくろう", "traits": ["記録魔", "夜型"]},
    {"name": "パーミッションねこ", "traits": ["厳格", "気まぐれ"]},
    {"name": "クラッシュぺんぎん", "traits": ["ドジ", "復活力"]},
    {"name": "アップデートかめ", "traits": ["慎重", "遅い"]},
]

PHRASES = [
    "{mascot}が応援してる: 『{line}』",
    "{mascot}: 『{line}』",
    "{mascot}より: 『{line}』",
    "[警告] {mascot}: 『{line}』",
    "{mascot}が通り過ぎた: 『{line}』",
]

LINES = [
    "システムの安定は君の努力次第！",
    "バグ撲滅運動中。応援よろしく！",
    "一服推奨。コマンド入力しすぎ注意！",
    "仮想記憶の海で泳いでます",
    "新しいUSBを認識しました（嘘）",
    "root権限は慎重に！",
    "ログは夜に増えるものです",
    "パーミッション変更は計画的に",
    "クラッシュしても立ち上がれ！",
    "アップデートは気長に待とう",
    "プロセス増やしすぎ注意！",
    "swapが悲鳴をあげてます",
    "/tmpに夢が詰まってる…かも",
    "バックアップはお早めに",
    "シェル芸はほどほどに",
    "今日もシステムは平和です",
    "ファイル名にスペースはやめよう",
    "パイプラインが詰まってます",
    "chmod 777はやめましょう",
    "lsの色分けに感謝！",
]

def random_mascot_message():
    mascot = random.choice(MASCOTS)
    phrase = random.choice(PHRASES)
    line = random.choice(LINES)
    mascot_name = mascot["name"]
    message = phrase.format(mascot=mascot_name, line=line)
    return mascot_name, message

def send_notification(title, message):
    if notification is not None:
        notification.notify(title=title, message=message, app_name="Mascot Parade", timeout=7)
    else:
        print(f"[通知] {title}: {message}")

def parade_once(verbose=False):
    mascot_name, message = random_mascot_message()
    send_notification(mascot_name, message)
    if verbose:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {mascot_name}: {message}")

def parade_loop(interval_range=(300, 1200), stop_event=None, verbose=False):
    # interval_range: (min_sec, max_sec)
    while not (stop_event and stop_event.is_set()):
        parade_once(verbose=verbose)
        wait = random.randint(*interval_range)
        for _ in range(wait):
            if stop_event and stop_event.is_set():
                return
            time.sleep(1)

def list_mascots():
    print("利用可能なマスコット一覧:")
    for m in MASCOTS:
        print(f"- {m['name']} ({', '.join(m['traits'])})")

def list_phrases():
    print("通知フォーマット例:")
    for p in PHRASES:
        print(f"- {p}")

def list_lines():
    print("セリフ例:")
    for l in LINES:
        print(f"- {l}")

def main():
    parser = argparse.ArgumentParser(description="謎のOSマスコット大行進通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_once = subparsers.add_parser("once", help="1回だけ通知を表示")
    parser_once.add_argument("--verbose", action="store_true", help="詳細ログも表示")

    parser_loop = subparsers.add_parser("loop", help="定期的に通知を表示")
    parser_loop.add_argument("--min", type=int, default=300, help="最短間隔(秒)")
    parser_loop.add_argument("--max", type=int, default=1200, help="最長間隔(秒)")
    parser_loop.add_argument("--verbose", action="store_true", help="詳細ログも表示")

    parser_list = subparsers.add_parser("list", help="マスコットやセリフ例を表示")
    parser_list.add_argument("--mascots", action="store_true", help="マスコット一覧")
    parser_list.add_argument("--phrases", action="store_true", help="通知フォーマット一覧")
    parser_list.add_argument("--lines", action="store_true", help="セリフ一覧")

    args = parser.parse_args()

    if args.command == "once":
        parade_once(verbose=args.verbose)
    elif args.command == "loop":
        stop_event = threading.Event()
        try:
            parade_loop(interval_range=(args.min, args.max), stop_event=stop_event, verbose=args.verbose)
        except KeyboardInterrupt:
            print("\n[終了] マスコット大行進を停止しました。")
            stop_event.set()
    elif args.command == "list":
        if args.mascots:
            list_mascots()
        if args.phrases:
            list_phrases()
        if args.lines:
            list_lines()
        if not (args.mascots or args.phrases or args.lines):
            list_mascots()
            print()
            list_phrases()
            print()
            list_lines()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
