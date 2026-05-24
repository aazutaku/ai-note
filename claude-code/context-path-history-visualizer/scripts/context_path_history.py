import os
import sys
import argparse
import json
from datetime import datetime
from collections import defaultdict, deque

HISTORY_FILE = os.path.expanduser("~/.claude_context_path_history.json")
EXCLUDE_PATHS = ["/tmp", "/var", "/dev", ".DS_Store", ".git"]

class PathNode:
    def __init__(self, name):
        self.name = name
        self.children = []
    def add_child(self, node):
        self.children.append(node)
    def to_dict(self):
        return {
            'name': self.name,
            'children': [child.to_dict() for child in self.children]
        }

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"[WARN] 履歴ファイルの読み込みに失敗しました: {e}")
        return []

def save_history(history):
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[ERROR] 履歴ファイルの保存に失敗しました: {e}")

def is_excluded(path):
    return any(ex in path for ex in EXCLUDE_PATHS)

def log_path(context, path):
    if is_excluded(path):
        return False
    history = load_history()
    entry = {
        'timestamp': datetime.now().isoformat(),
        'context': context,
        'path': path
    }
    history.append(entry)
    save_history(history)
    return True

def build_tree(history):
    root = PathNode('root')
    nodes = {'root': root}
    for entry in history:
        context = entry['context']
        path = entry['path']
        parent = nodes.get(context, root)
        if path not in nodes:
            node = PathNode(path)
            nodes[path] = node
            parent.add_child(node)
    return root

def print_tree(node, prefix=""):
    print(prefix + node.name)
    for i, child in enumerate(node.children):
        connector = "├── " if i < len(node.children) - 1 else "└── "
        print_tree(child, prefix + connector)

def list_history():
    history = load_history()
    if not history:
        print("履歴がありません。")
        return
    for entry in history:
        print(f"[{entry['timestamp']}] context: {entry['context']} -> path: {entry['path']}")

def summary_tree():
    history = load_history()
    if not history:
        print("履歴がありません。")
        return
    tree = build_tree(history)
    print_tree(tree)

def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("履歴を削除しました。")
    else:
        print("履歴ファイルが存在しません。")

def parse_args():
    parser = argparse.ArgumentParser(description="Claude context path history visualizer")
    subparsers = parser.add_subparsers(dest="command")
    log_parser = subparsers.add_parser("log", help="新しいパス履歴を記録する")
    log_parser.add_argument("context", type=str, help="親コンテキスト名")
    log_parser.add_argument("path", type=str, help="現在のパス名")
    list_parser = subparsers.add_parser("list", help="履歴を時系列で一覧表示")
    summary_parser = subparsers.add_parser("summary", help="履歴をツリー状に可視化")
    clear_parser = subparsers.add_parser("clear", help="履歴を全削除")
    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == "log":
        success = log_path(args.context, args.path)
        if success:
            print(f"履歴を記録しました: {args.context} -> {args.path}")
        else:
            print("記録対象外のパスです。")
    elif args.command == "list":
        list_history()
    elif args.command == "summary":
        summary_tree()
    elif args.command == "clear":
        clear_history()
    else:
        print("コマンドを指定してください (log/list/summary/clear)")

if __name__ == '__main__':
    main()
