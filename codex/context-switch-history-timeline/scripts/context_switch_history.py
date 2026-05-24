# context_switch_history.py
import os
import json
import datetime
import argparse

HISTORY_FILE = os.path.expanduser("~/.context_switch_history.json")
MAX_DISPLAY = 50

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except Exception:
                return []
    return []

def save_history(history):
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def add_event(event_type, detail):
    history = load_history()
    timestamp = datetime.datetime.now().isoformat(timespec='seconds')
    entry = {
        'timestamp': timestamp,
        'event_type': event_type,
        'detail': detail
    }
    history.append(entry)
    save_history(history)
    print(f"[記録済] {timestamp} {event_type}: {detail}")

def show_timeline(n=MAX_DISPLAY):
    history = load_history()
    if not history:
        print("履歴がありません。")
        return
    print("\n=== Context Switch Timeline ===\n")
    for entry in history[-n:]:
        ts = entry['timestamp']
        et = entry['event_type']
        dt = entry['detail']
        print(f"{ts} | {et} | {dt}")
    print(f"\n表示件数: {min(n, len(history))} / {len(history)}")

def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("履歴を削除しました。")
    else:
        print("履歴ファイルが見つかりません。")

def main():
    parser = argparse.ArgumentParser(description='Context Switch History Timeline')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='履歴にイベントを追加')
    add_parser.add_argument('event_type', help='イベントタイプ (例: ファイル移動, タスク切替)')
    add_parser.add_argument('detail', help='詳細内容 (例: ファイル名やタスク名)')

    show_parser = subparsers.add_parser('show', help='タイムラインを表示')
    show_parser.add_argument('-n', type=int, default=MAX_DISPLAY, help='表示件数')

    clear_parser = subparsers.add_parser('clear', help='履歴を全削除')

    args = parser.parse_args()
    if args.command == 'add':
        add_event(args.event_type, args.detail)
    elif args.command == 'show':
        show_timeline(args.n)
    elif args.command == 'clear':
        clear_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
