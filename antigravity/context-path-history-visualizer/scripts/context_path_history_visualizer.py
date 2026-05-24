import os
import sys
import json
import argparse
from collections import defaultdict, deque
from datetime import datetime

HISTORY_FILE = os.path.expanduser('~/.context_path_history.json')
EXCLUDE_DIRS = {'.git', '__pycache__', '.DS_Store', 'node_modules'}


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []


def save_history(history):
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f'Error saving history: {e}')


def log_path(path, parent=None):
    history = load_history()
    entry = {
        'path': os.path.abspath(path),
        'timestamp': datetime.now().isoformat(),
        'parent': os.path.abspath(parent) if parent else None
    }
    history.append(entry)
    save_history(history)
    print(f'Logged: {entry["path"]}')


def list_history():
    history = load_history()
    if not history:
        print('No context path history found.')
        return
    for idx, entry in enumerate(history):
        parent = entry['parent'] if entry['parent'] else 'root'
        print(f"{idx+1:03d}: {entry['path']} (from {parent}) @ {entry['timestamp']}")


def build_tree(history):
    tree = defaultdict(list)
    roots = set()
    nodes = set()
    for entry in history:
        path = entry['path']
        parent = entry['parent']
        nodes.add(path)
        if parent:
            tree[parent].append(path)
        else:
            roots.add(path)
    return tree, roots


def print_tree(tree, roots):
    def _print(node, prefix=''):
        print(prefix + os.path.basename(node) if os.path.basename(node) else node)
        children = tree.get(node, [])
        for i, child in enumerate(children):
            is_last = (i == len(children) - 1)
            child_prefix = prefix + ('    ' if is_last else '│   ')
            connector = '└── ' if is_last else '├── '
            print(prefix + connector, end='')
            _print(child, child_prefix)
    for root in roots:
        _print(root)


def summary():
    history = load_history()
    if not history:
        print('No context path history found.')
        return
    tree, roots = build_tree(history)
    print('Context Path History Tree:')
    print_tree(tree, roots)


def clean_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print('History cleared.')
    else:
        print('No history file found.')


def filter_excluded(path):
    for part in path.split(os.sep):
        if part in EXCLUDE_DIRS:
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description='Context Path History Visualizer')
    subparsers = parser.add_subparsers(dest='command')

    log_parser = subparsers.add_parser('log', help='Log a context path')
    log_parser.add_argument('path', help='Path to log')
    log_parser.add_argument('--parent', help='Parent path', default=None)

    list_parser = subparsers.add_parser('list', help='List context path history')

    summary_parser = subparsers.add_parser('summary', help='Show context path tree')

    clean_parser = subparsers.add_parser('clean', help='Clear context path history')

    args = parser.parse_args()

    if args.command == 'log':
        if filter_excluded(args.path):
            print(f'Path {args.path} is excluded.')
            return
        log_path(args.path, args.parent)
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    elif args.command == 'clean':
        clean_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
