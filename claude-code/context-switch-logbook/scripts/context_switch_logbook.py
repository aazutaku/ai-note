import argparse
import json
import os
from datetime import datetime
from typing import List, Dict, Optional

LOG_DIR = os.path.expanduser('.claude/skills/context-switch-logbook')
LOG_FILE = os.path.join(LOG_DIR, 'logbook.jsonl')


def ensure_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)


def log_context_switch(from_ctx: str, to_ctx: str, reason: str) -> None:
    ensure_log_dir()
    entry = {
        'timestamp': datetime.now().isoformat(timespec='seconds'),
        'from': from_ctx,
        'to': to_ctx,
        'reason': reason
    }
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')


def load_log_entries() -> List[Dict]:
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]


def list_logs(limit: Optional[int] = None) -> None:
    entries = load_log_entries()
    if limit:
        entries = entries[-limit:]
    for entry in entries:
        print(f"[{entry['timestamp']}] from: {entry['from']} -> to: {entry['to']} | reason: {entry['reason']}")


def summary_logs() -> None:
    entries = load_log_entries()
    if not entries:
        print('No context switch logs found.')
        return
    print(f"Total switches: {len(entries)}")
    switches = {}
    for entry in entries:
        key = f"{entry['from']} -> {entry['to']}"
        switches[key] = switches.get(key, 0) + 1
    print('--- Switch summary ---')
    for k, v in sorted(switches.items(), key=lambda x: -x[1]):
        print(f"{k}: {v} times")
    print('\nRecent reasons:')
    for entry in entries[-5:]:
        print(f"- {entry['reason']} ({entry['timestamp']})")


def delete_last_entry() -> None:
    entries = load_log_entries()
    if not entries:
        print('No entries to delete.')
        return
    removed = entries.pop()
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    print(f"Deleted last entry: from {removed['from']} to {removed['to']} at {removed['timestamp']}")


def parse_args():
    parser = argparse.ArgumentParser(description='Context Switch Logbook CLI')
    subparsers = parser.add_subparsers(dest='command')

    # log command
    log_parser = subparsers.add_parser('log', help='Log a context switch')
    log_parser.add_argument('--from', dest='from_ctx', required=True, help='Context you switched from')
    log_parser.add_argument('--to', dest='to_ctx', required=True, help='Context you switched to')
    log_parser.add_argument('--reason', required=True, help='Reason for the switch')

    # list command
    list_parser = subparsers.add_parser('list', help='List context switch logs')
    list_parser.add_argument('--limit', type=int, help='Show only the last N entries')

    # summary command
    subparsers.add_parser('summary', help='Show summary of switches')

    # delete-last command
    subparsers.add_parser('delete-last', help='Delete the last log entry')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'log':
        log_context_switch(args.from_ctx, args.to_ctx, args.reason)
        print(f"Logged: from '{args.from_ctx}' to '{args.to_ctx}' | reason: {args.reason}")
    elif args.command == 'list':
        list_logs(args.limit)
    elif args.command == 'summary':
        summary_logs()
    elif args.command == 'delete-last':
        delete_last_entry()
    else:
        print('No command specified. Use --help for usage.')


if __name__ == '__main__':
    main()
