import os
import sys
import json
import argparse
from datetime import datetime

MOOD_ENV = 'MOOD'
MOOD_FILE = os.path.expanduser('~/.mood_indicator.json')

MOOD_MARKS = {
    '元気': '[元気] ',
    'だるい': '[だるい] ',
    'やる気MAX': '[やる気MAX] ',
    '燃え尽き寸前': '[燃え尽き寸前] ',
    '迷走中': '[迷走中] ',
    '集中': '[集中] ',
    '眠い': '[眠い] ',
    '普通': '[普通] ',
    '楽しい': '[楽しい] ',
    '悲しい': '[悲しい] ',
}

def load_mood_history():
    if not os.path.exists(MOOD_FILE):
        return []
    try:
        with open(MOOD_FILE, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def save_mood_history(history):
    try:
        with open(MOOD_FILE, 'w') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[mood-indicator] 履歴保存エラー: {e}")

def get_current_mood():
    mood = os.environ.get(MOOD_ENV)
    if mood:
        return mood.strip()
    # ファイル履歴から最新を取得
    history = load_mood_history()
    if history:
        return history[-1]['mood']
    return None

def set_mood(mood):
    mood = mood.strip()
    history = load_mood_history()
    now = datetime.now().isoformat(timespec='seconds')
    history.append({'mood': mood, 'timestamp': now})
    save_mood_history(history)
    print(f"[今日の気分] {mood}")

def show_mood():
    mood = get_current_mood()
    if mood:
        mark = MOOD_MARKS.get(mood, f"[{mood}]")
        print(f"[今日の気分] {mood}")
    else:
        print("[mood-indicator] 気分が設定されていません。'set'コマンドで設定してください。")

def list_history():
    history = load_mood_history()
    if not history:
        print("[mood-indicator] 履歴がありません。")
        return
    print("=== 気分履歴 ===")
    for entry in history[-20:]:
        print(f"{entry['timestamp']}  {entry['mood']}")

def summary():
    history = load_mood_history()
    if not history:
        print("[mood-indicator] 履歴がありません。")
        return
    summary_dict = {}
    for entry in history:
        mood = entry['mood']
        summary_dict[mood] = summary_dict.get(mood, 0) + 1
    print("=== 気分サマリー ===")
    for mood, count in sorted(summary_dict.items(), key=lambda x: -x[1]):
        print(f"{mood}: {count}回")

def parse_args():
    parser = argparse.ArgumentParser(description='Terminal Mood Indicator')
    subparsers = parser.add_subparsers(dest='command')

    set_parser = subparsers.add_parser('set', help='気分を設定します')
    set_parser.add_argument('mood', type=str, help='気分を入力')

    show_parser = subparsers.add_parser('show', help='現在の気分を表示')
    list_parser = subparsers.add_parser('list', help='気分の履歴を表示')
    summary_parser = subparsers.add_parser('summary', help='気分の集計を表示')

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'set':
        set_mood(args.mood)
    elif args.command == 'show':
        show_mood()
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    else:
        # デフォルト動作: show
        show_mood()

if __name__ == '__main__':
    main()
