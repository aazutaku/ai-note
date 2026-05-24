import argparse
import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Any

NOTES_DIR = os.path.expanduser('~/.context_switch_notes')
BACKUP_SUFFIX = '.bak'
MAX_NOTES_PER_CONTEXT = 3


def ensure_notes_dir():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)


def get_context_filename(context_name: str) -> str:
    safe_name = context_name.replace('/', '_').replace(' ', '_')
    return os.path.join(NOTES_DIR, f'{safe_name}.json')


def backup_file(filename: str):
    if os.path.exists(filename):
        backup_name = filename + BACKUP_SUFFIX
        with open(filename, 'rb') as src, open(backup_name, 'wb') as dst:
            dst.write(src.read())


def load_notes(context_name: str) -> List[Dict[str, Any]]:
    filename = get_context_filename(context_name)
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        try:
            notes = json.load(f)
            if isinstance(notes, list):
                return notes
            else:
                return []
        except Exception:
            return []


def save_notes(context_name: str, notes: List[Dict[str, Any]]):
    filename = get_context_filename(context_name)
    backup_file(filename)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(notes[-MAX_NOTES_PER_CONTEXT:], f, ensure_ascii=False, indent=2)


def summarize_note(note: str) -> str:
    # 簡易要約: 1行目＋TODO/思考メモ抽出
    lines = note.strip().split('\n')
    summary = []
    if lines:
        summary.append(lines[0])
    for l in lines[1:]:
        if 'TODO' in l or '思考' in l:
            summary.append(l)
    return '\n'.join(summary)


def log_note(context: str, note: str):
    ensure_notes_dir()
    notes = load_notes(context)
    now = datetime.now().isoformat(timespec='seconds')
    summarized = summarize_note(note)
    notes.append({
        'timestamp': now,
        'note': note,
        'summary': summarized
    })
    save_notes(context, notes)
    print(f'[context-switch-notes] 新しいメモを保存しました。')


def list_notes(context: str):
    notes = load_notes(context)
    if not notes:
        print(f'[context-switch-notes] メモはありません。')
        return
    print(f'[context-switch-notes] {context} のメモ一覧:')
    for n in notes:
        print(f"- {n['timestamp']}: {n['summary']}")


def show_last_note(context: str):
    notes = load_notes(context)
    if not notes:
        print(f'[context-switch-notes] 前回の作業メモはありません。')
        return
    last = notes[-1]
    print(f'[context-switch-notes] 前回の作業メモ:\n{last["summary"]}')


def summary_all():
    ensure_notes_dir()
    files = [f for f in os.listdir(NOTES_DIR) if f.endswith('.json')]
    if not files:
        print('[context-switch-notes] 保存されたコンテキストはありません。')
        return
    for fname in files:
        context = fname[:-5]
        notes = load_notes(context)
        print(f'--- {context} ---')
        for n in notes:
            print(f"- {n['timestamp']}: {n['summary']}")


def main():
    parser = argparse.ArgumentParser(description='Context Switch Notes Skill')
    subparsers = parser.add_subparsers(dest='command')

    log_parser = subparsers.add_parser('log', help='メモを記録')
    log_parser.add_argument('context', type=str, help='コンテキスト名')
    log_parser.add_argument('note', type=str, help='記録するメモ')

    list_parser = subparsers.add_parser('list', help='コンテキストのメモ一覧')
    list_parser.add_argument('context', type=str, help='コンテキスト名')

    show_parser = subparsers.add_parser('show', help='直前のメモを表示')
    show_parser.add_argument('context', type=str, help='コンテキスト名')

    summary_parser = subparsers.add_parser('summary', help='全コンテキストのサマリー')

    args = parser.parse_args()
    if args.command == 'log':
        log_note(args.context, args.note)
    elif args.command == 'list':
        list_notes(args.context)
    elif args.command == 'show':
        show_last_note(args.context)
    elif args.command == 'summary':
        summary_all()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
