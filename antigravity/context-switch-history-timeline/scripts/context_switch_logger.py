import os
import sys
import json
import datetime
import argparse

HISTORY_FILE = os.path.expanduser("~/.context_switch_history.json")


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except Exception:
                return []
    else:
        return []


def save_history(history):
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def log_context_switch(context, details=None):
    history = load_history()
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "context": context,
        "details": details or ""
    }
    history.append(entry)
    save_history(history)
    print(f"Logged context switch: {context}")


def show_timeline(limit=None, page=1, per_page=20, filter_context=None):
    history = load_history()
    if filter_context:
        history = [h for h in history if filter_context.lower() in h["context"].lower()]
    total = len(history)
    if limit:
        history = history[-limit:]
    # Pagination
    if per_page:
        start = (page - 1) * per_page
        end = start + per_page
        history = history[start:end]
    print(f"Context Switch Timeline ({len(history)} / {total} entries):\n")
    for i, entry in enumerate(history, 1):
        ts = entry["timestamp"]
        ctx = entry["context"]
        det = entry["details"]
        print(f"[{ts}] {ctx}" + (f" | {det}" if det else ""))


def main():
    parser = argparse.ArgumentParser(description="Context Switch History Timeline Tool")
    subparsers = parser.add_subparsers(dest='command')

    log_parser = subparsers.add_parser('log', help='Log a context switch')
    log_parser.add_argument('context', type=str, help='Context name (e.g., file/task)')
    log_parser.add_argument('--details', type=str, default="", help='Optional details')

    show_parser = subparsers.add_parser('timeline', help='Show context switch timeline')
    show_parser.add_argument('--limit', type=int, default=None, help='Limit number of entries')
    show_parser.add_argument('--page', type=int, default=1, help='Page number (pagination)')
    show_parser.add_argument('--per-page', type=int, default=20, help='Entries per page')
    show_parser.add_argument('--filter', type=str, default=None, help='Filter by context substring')

    args = parser.parse_args()
    if args.command == 'log':
        log_context_switch(args.context, args.details)
    elif args.command == 'timeline':
        show_timeline(limit=args.limit, page=args.page, per_page=args.per_page, filter_context=args.filter)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
