import sys
import argparse
import random
import time
from typing import Tuple, List

MOOD_COMMENTS = [
    (range(0, 10), [
        "カフェイン補給推奨。無理せず休憩を。",
        "今日は低気圧かも。深呼吸してみよう。",
        "やる気2：机の下に隠れたい気分。"
    ]),
    (range(10, 30), [
        "やる気低め。音楽でも流してみては？",
        "集中力が散漫かも。軽くストレッチ！",
        "やる気15：おやつタイムが必要かも。"
    ]),
    (range(30, 60), [
        "まあまあの調子。あと一息！",
        "やる気50：普通です。",
        "波に乗り始めた？その調子！"
    ]),
    (range(60, 80), [
        "やる気高め！このまま突き進もう。",
        "やる気70：集中力アップ中。",
        "いい感じ。タスクがどんどん片付く予感。"
    ]),
    (range(80, 101), [
        "やる気指数: MAX！今日もコーディング日和！",
        "絶好調！何でもできそうな気分。",
        "やる気95：天才モード発動中。"
    ]),
]

HISTORY_LIMIT = 20

class MoodHistory:
    def __init__(self):
        self.entries: List[Tuple[float, int, str]] = []

    def add(self, timestamp: float, mood: int, comment: str):
        self.entries.append((timestamp, mood, comment))
        if len(self.entries) > HISTORY_LIMIT:
            self.entries.pop(0)

    def list(self):
        for t, m, c in self.entries:
            ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))
            print(f"{ts} | やる気指数: {m} | {c}")

    def summary(self):
        if not self.entries:
            print("履歴がありません。")
            return
        moods = [m for _, m, _ in self.entries]
        avg = sum(moods) / len(moods)
        print(f"直近{len(moods)}回の平均やる気指数: {avg:.1f}")

history = MoodHistory()

def pick_mood_and_comment() -> Tuple[int, str]:
    mood = random.randint(0, 100)
    comment = None
    for r, comments in MOOD_COMMENTS:
        if mood in r:
            comment = random.choice(comments)
            break
    if comment is None:
        comment = "気分不明。"
    return mood, comment

def print_mood(mood: int, comment: str):
    print("[Terminal Mood Barometer]")
    print(f"やる気指数: {mood}")
    print(f"コメント: {comment}")

def log_mood():
    mood, comment = pick_mood_and_comment()
    print_mood(mood, comment)
    history.add(time.time(), mood, comment)

def list_history():
    history.list()

def summary_history():
    history.summary()

def parse_args():
    parser = argparse.ArgumentParser(description='Terminal Mood Barometer')
    subparsers = parser.add_subparsers(dest='command', required=False)

    parser_log = subparsers.add_parser('log', help='現在の気分指数を表示')
    parser_list = subparsers.add_parser('list', help='直近の気分履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='気分履歴の平均を表示')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'log' or args.command is None:
        log_mood()
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary_history()
    else:
        print('不明なコマンドです')
        sys.exit(1)

if __name__ == '__main__':
    main()
