import os
import sys
import json
import argparse
import datetime
import shutil
from typing import List, Dict, Any

NOTES_DIR = '.claude/skills/context-switch-notes/'
NOTES_FILE = os.path.join(NOTES_DIR, 'notes.json')
BACKUP_FILE = os.path.join(NOTES_DIR, 'notes.bak.json')
MAX_NOTES_PER_CONTEXT = 10


def ensure_notes_dir():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)


def load_notes() -> Dict[str, List[Dict[str, Any]]]:
    if not os.path.exists(NOTES_FILE):
        return {}
    with open(NOTES_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except Exception:
            return {}


def save_notes(notes: Dict[str, List[Dict[str, Any]]]):
    # Backup before overwrite
    if os.path.exists(NOTES_FILE):
        shutil.copyfile(NOTES_FILE, BACKUP_FILE)
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)


def add_note(context: str, content: str):
    notes = load_notes()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    entry = {"timestamp": now, "content": content}
    if context not in notes:
        notes[context] = []
    notes[context].append(entry)
    # Keep only latest MAX_NOTES_PER_CONTEXT
    notes[context] = notes[context][-MAX_NOTES_PER_CONTEXT:]
    save_notes(notes)
    print(f"[context-switch-notes] Added note to context: {context}\n- {now}: {content}")


def list_notes(context: str):
    notes = load_notes()
    if context not in notes or not notes[context]:
        print(f"[context-switch-notes] No notes for context: {context}")
        return
    print(f"[context-switch-notes] Notes for context: {context}")
    for entry in notes[context]:
        print(f"- {entry['timestamp']}: {entry['content']}")


def summary_notes(context: str):
    notes = load_notes()
    if context not in notes or not notes[context]:
        print(f"[context-switch-notes] No notes for context: {context}")
        return
    print(f"[context-switch-notes] Summary for context: {context}")
    last = notes[context][-1]
    print(f"Last note: {last['timestamp']}: {last['content']}")
    if len(notes[context]) > 1:
        print(f"Total notes: {len(notes[context])}")


def restore_notes(context: str):
    notes = load_notes()
    if context not in notes or not notes[context]:
        print(f"[context-switch-notes] No notes to restore for context: {context}")
        return
    print(f"[context-switch-notes] Restored notes for context: {context}")
    for entry in notes[context]:
        print(f"- {entry['timestamp']}: {entry['content']}")


def parse_args():
    parser = argparse.ArgumentParser(description='Context Switch Notes Skill')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a note to a context')
    add_parser.add_argument('content', type=str, help='Note content')
    add_parser.add_argument('--context', type=str, required=True, help='Context name')

    list_parser = subparsers.add_parser('list', help='List notes for a context')
    list_parser.add_argument('--context', type=str, required=True, help='Context name')

    summary_parser = subparsers.add_parser('summary', help='Show summary for a context')
    summary_parser.add_argument('--context', type=str, required=True, help='Context name')

    restore_parser = subparsers.add_parser('restore', help='Restore notes for a context')
    restore_parser.add_argument('--context', type=str, required=True, help='Context name')

    return parser.parse_args()


def main():
    ensure_notes_dir()
    args = parse_args()
    if args.command == 'add':
        add_note(args.context, args.content)
    elif args.command == 'list':
        list_notes(args.context)
    elif args.command == 'summary':
        summary_notes(args.context)
    elif args.command == 'restore':
        restore_notes(args.context)
    else:
        print('Usage: context_switch_notes.py [add|list|summary|restore] ...')


if __name__ == '__main__':
    main()
