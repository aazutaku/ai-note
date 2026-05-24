import argparse
import os
import json
import sys
import datetime
from collections import defaultdict, deque

HISTORY_FILE = os.path.expanduser("~/.codex_context_path_history.json")

class ContextPathNode:
    def __init__(self, id, label, parent=None, timestamp=None):
        self.id = id
        self.label = label
        self.parent = parent  # parent id
        self.children = []    # list of node ids
        self.timestamp = timestamp or datetime.datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "label": self.label,
            "parent": self.parent,
            "children": self.children,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dict(d):
        node = ContextPathNode(d["id"], d["label"], d["parent"], d["timestamp"])
        node.children = d["children"]
        return node

class ContextPathHistory:
    def __init__(self):
        self.nodes = {}
        self.root_id = None
        self.load()

    def load(self):
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as f:
                data = json.load(f)
                self.nodes = {nid: ContextPathNode.from_dict(nd) for nid, nd in data["nodes"].items()}
                self.root_id = data.get("root_id")
        else:
            self.nodes = {}
            self.root_id = None

    def save(self):
        with open(HISTORY_FILE, "w") as f:
            data = {
                "nodes": {nid: node.to_dict() for nid, node in self.nodes.items()},
                "root_id": self.root_id
            }
            json.dump(data, f, indent=2)

    def add_event(self, label, parent_id=None):
        node_id = f"{len(self.nodes)}-{int(datetime.datetime.now().timestamp())}"
        node = ContextPathNode(node_id, label, parent_id)
        self.nodes[node_id] = node
        if parent_id:
            parent_node = self.nodes.get(parent_id)
            if parent_node:
                parent_node.children.append(node_id)
        else:
            self.root_id = node_id
        self.save()
        return node_id

    def list_events(self):
        events = []
        for node in sorted(self.nodes.values(), key=lambda n: n.timestamp):
            events.append(f"[{node.timestamp}] {node.label} (id:{node.id}, parent:{node.parent})")
        return events

    def summary(self):
        return f"Total events: {len(self.nodes)}\nRoot: {self.root_id}"

    def print_tree(self, node_id=None, prefix=""): 
        if node_id is None:
            node_id = self.root_id
        node = self.nodes.get(node_id)
        if not node:
            return
        print(f"{prefix}{node.label}")
        for i, child_id in enumerate(node.children):
            is_last = (i == len(node.children) - 1)
            child_prefix = prefix + ("    " if is_last else "│   ")
            branch = "└── " if is_last else "├── "
            print(f"{prefix}{branch}", end="")
            self.print_tree(child_id, child_prefix)

    def to_dict(self):
        return {
            "nodes": {nid: node.to_dict() for nid, node in self.nodes.items()},
            "root_id": self.root_id
        }

    def clear(self):
        self.nodes = {}
        self.root_id = None
        self.save()


def parse_args():
    parser = argparse.ArgumentParser(description="Context Path History Visualizer")
    subparsers = parser.add_subparsers(dest="command")

    log_parser = subparsers.add_parser("log", help="Add a context event")
    log_parser.add_argument("label", type=str, help="Event label (e.g., edit: main.py:10-20)")
    log_parser.add_argument("--parent", type=str, default=None, help="Parent event id")

    list_parser = subparsers.add_parser("list", help="List all context events")

    tree_parser = subparsers.add_parser("tree", help="Show context path tree")

    summary_parser = subparsers.add_parser("summary", help="Show summary of context path history")

    clear_parser = subparsers.add_parser("clear", help="Clear all history")

    return parser.parse_args()

def main():
    args = parse_args()
    history = ContextPathHistory()

    if args.command == "log":
        node_id = history.add_event(args.label, args.parent)
        print(f"Logged event: {args.label} (id: {node_id})")
    elif args.command == "list":
        events = history.list_events()
        for e in events:
            print(e)
    elif args.command == "tree":
        print("Context Path History Tree:")
        if history.root_id:
            history.print_tree()
        else:
            print("(No history)")
    elif args.command == "summary":
        print(history.summary())
    elif args.command == "clear":
        confirm = input("Are you sure you want to clear all history? (y/N): ")
        if confirm.lower() == 'y':
            history.clear()
            print("History cleared.")
        else:
            print("Cancelled.")
    else:
        print("No command specified. Use --help for usage.")

if __name__ == "__main__":
    main()
