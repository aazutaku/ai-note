import os
import sys
import argparse
import json
import datetime
from typing import List, Dict, Any

NOTES_DIR = '.context_notes'


def ensure_notes_dir():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)


def get_context_path(context_name: str) -> str:
    safe_name = context_name.replace('/', '_').replace(' ', '_')
    return os.path.join(NOTES_DIR, f'{safe_name}.json')


def load_notes(context_name: str) -> List[Dict[str, Any]]:
    path = get_context_path(context_name)
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except Exception:
            return []


def save_notes(context_name: str, notes: List[Dict[str, Any]]):
    path = get_context_path(context_name)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)


def summarize_notes(notes: List[Dict[str, Any]]) -> str:
    if not notes:
        return 'No previous notes.'
    last = notes[-1]
    summary = last.get('summary', '')
    todo = last.get('todo', [])
    lines = []
    lines.append(f'Last summary: {summary}')
    if todo:
        lines.append('TODO: ' + ', '.join(todo))
    return '\n'.join(lines)


def add_note(context_name: str, summary: str, todo: List[str]):
    notes = load_notes(context_name)
    now = datetime.datetime.now().isoformat()
    # 重複排除: 直前と同じ内容ならスキップ
    if notes and notes[-1]['summary'] == summary and notes[-1]['todo'] == todo:
        return
    note = {
        'timestamp': now,
        'summary': summary,
        'todo': todo
    }
    notes.append(note)
    save_notes(context_name, notes)


def list_contexts() -> List[str]:
    ensure_notes_dir()
    files = os.listdir(NOTES_DIR)
    return [f[:-5] for f in files if f.endswith('.json')]


def list_notes(context_name: str):
    notes = load_notes(context_name)
    for note in notes:
        print(f"[{note['timestamp']}] {note['summary']}")
        if note['todo']:
            print('  TODO:', ', '.join(note['todo']))
        print('---')


def show_summary(context_name: str):
    notes = load_notes(context_name)
    print(f'[context-switch-notes] Context: {context_name}')
    print(summarize_notes(notes))
    print('---')


def backup_notes():
    ensure_notes_dir()
    backup_dir = NOTES_DIR + '_backup_' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    os.makedirs(backup_dir)
    for fname in os.listdir(NOTES_DIR):
        src = os.path.join(NOTES_DIR, fname)
        dst = os.path.join(backup_dir, fname)
        with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
            fdst.write(fsrc.read())
    print(f'Backup completed: {backup_dir}')


def parse_args():
    parser = argparse.ArgumentParser(description='Context Switch Notes Tool')
    subparsers = parser.add_subparsers(dest='command')

    log_parser = subparsers.add_parser('log', help='Add a note to context')
    log_parser.add_argument('context', type=str, help='Context name')
    log_parser.add_argument('--summary', type=str, required=True, help='Summary of current work')
    log_parser.add_argument('--todo', nargs='*', default=[], help='TODO items')

    list_parser = subparsers.add_parser('list', help='List notes for context')
    list_parser.add_argument('context', type=str, help='Context name')

    summary_parser = subparsers.add_parser('summary', help='Show last summary for context')
    summary_parser.add_argument('context', type=str, help='Context name')

    contexts_parser = subparsers.add_parser('contexts', help='List all contexts')

    backup_parser = subparsers.add_parser('backup', help='Backup all notes')

    return parser.parse_args()


def main():
    ensure_notes_dir()
    args = parse_args()
    if args.command == 'log':
        add_note(args.context, args.summary, args.todo)
        print(f'Note added to context: {args.context}')
    elif args.command == 'list':
        list_notes(args.context)
    elif args.command == 'summary':
        show_summary(args.context)
    elif args.command == 'contexts':
        contexts = list_contexts()
        print('Available contexts:')
        for ctx in contexts:
            print('  -', ctx)
    elif args.command == 'backup':
        backup_notes()
    else:
        print('No command specified. Use --help for usage.')


if __name__ == '__main__':
    main()
