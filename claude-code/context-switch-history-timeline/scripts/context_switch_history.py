import os
import sys
import json
import time
from datetime import datetime

HISTORY_DIR = os.path.expanduser('.claude/skills/context-switch-history-timeline')
HISTORY_FILE = os.path.join(HISTORY_DIR, 'history.json')
MAX_DISPLAY = 100

def ensure_history_dir():
    if not os.path.exists(HISTORY_DIR):
        os.makedirs(HISTORY_DIR)

def load_history():
    if not os.path.isfile(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except Exception:
            return []

def save_history(history):
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def record_switch(context_type, context_name):
    ensure_history_dir()
    history = load_history()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = {
        'timestamp': now,
        'type': context_type,
        'name': context_name
    }
    # 連続同一記録は省略
    if history and history[-1]['type'] == context_type and history[-1]['name'] == context_name:
        return
    history.append(entry)
    save_history(history)

def print_timeline(all_entries=False):
    history = load_history()
    if not history:
        print('履歴がありません。')
        return
    entries = history if all_entries else history[-MAX_DISPLAY:]
    print('--- コンテキスト切り替えタイムライン ---')
    for entry in entries:
        print(f"[{entry['timestamp']}] {entry['type']} : {entry['name']}")
    if not all_entries and len(history) > MAX_DISPLAY:
        print(f'... 最新{MAX_DISPLAY}件のみ表示 (全{len(history)}件) ...')

def usage():
    print('使い方:')
    print('  python context_switch_history.py record <type> <name>   # 履歴に記録')
    print('  python context_switch_history.py timeline               # タイムライン表示 (最新100件)')
    print('  python context_switch_history.py timeline --all         # 全履歴表示')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'record' and len(sys.argv) >= 4:
        context_type = sys.argv[2]
        context_name = ' '.join(sys.argv[3:])
        record_switch(context_type, context_name)
    elif cmd == 'timeline':
        all_entries = len(sys.argv) > 2 and sys.argv[2] == '--all'
        print_timeline(all_entries=all_entries)
    else:
        usage()
