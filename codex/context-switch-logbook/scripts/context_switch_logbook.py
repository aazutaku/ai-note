import argparse
import json
import os
import sys
from datetime import datetime

LOG_FILE = os.path.expanduser("~/.context_switch_log.json")


def load_logs():
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading log file: {e}", file=sys.stderr)
        return []

def save_logs(logs):
    try:
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving log file: {e}", file=sys.stderr)


def log_switch(args):
    logs = load_logs()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = {
        'timestamp': now,
        'from': args.from_context,
        'to': args.to_context,
        'reason': args.reason
    }
    logs.append(entry)
    save_logs(logs)
    print(f"[{now}] {args.from_context} -> {args.to_context}: {args.reason}")


def list_logs(args):
    logs = load_logs()
    if not logs:
        print("No context switch logs found.")
        return
    for entry in logs:
        print(f"[{entry['timestamp']}] {entry['from']} -> {entry['to']}: {entry['reason']}")


def summary_logs(args):
    logs = load_logs()
    if not logs:
        print("No context switch logs found.")
        return
    summary = {}
    for entry in logs:
        key = (entry['from'], entry['to'])
        summary[key] = summary.get(key, 0) + 1
    print("Switch summary (from -> to: count):")
    for (src, dst), count in summary.items():
        print(f"{src} -> {dst}: {count}")


def delete_logs(args):
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print("All context switch logs deleted.")
    else:
        print("No log file to delete.")


def parse_args():
    parser = argparse.ArgumentParser(description="Context Switch Logbook: 記録・閲覧・サマリ")
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_log = subparsers.add_parser('log', help='コンテキスト切り替えを記録')
    parser_log.add_argument('--from', dest='from_context', required=True, help='切り替え元のエージェント/タスク名')
    parser_log.add_argument('--to', dest='to_context', required=True, help='切り替え先のエージェント/タスク名')
    parser_log.add_argument('--reason', required=True, help='切り替え理由のメモ')
    parser_log.set_defaults(func=log_switch)

    parser_list = subparsers.add_parser('list', help='記録済みログを一覧表示')
    parser_list.set_defaults(func=list_logs)

    parser_summary = subparsers.add_parser('summary', help='切り替え傾向を集計表示')
    parser_summary.set_defaults(func=summary_logs)

    parser_delete = subparsers.add_parser('delete', help='全ログを削除')
    parser_delete.set_defaults(func=delete_logs)

    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
