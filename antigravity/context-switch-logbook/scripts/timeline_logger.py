import argparse
import sys
import os
from datetime import datetime
from typing import List, Dict

LOG_FILE = os.path.expanduser('~/.context_switch_logbook.log')


def ensure_logfile_exists():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            pass

def log_entry(from_ctx: str, to_ctx: str, reason: str):
    ensure_logfile_exists()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f'[{timestamp}] from: "{from_ctx}" to: "{to_ctx}" reason: "{reason.strip()}"\n'
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(entry)
    print('記録しました:')
    print(entry.strip())

def list_entries(limit: int = 0):
    ensure_logfile_exists()
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if limit > 0:
        lines = lines[-limit:]
    for line in lines:
        print(line.strip())

def parse_entry(line: str) -> Dict:
    try:
        ts_part, rest = line.split('] ', 1)
        timestamp = ts_part.strip('[')
        from_part = rest.split('from: "', 1)[1].split('"', 1)[0]
        to_part = rest.split('to: "', 1)[1].split('"', 1)[0]
        reason_part = rest.split('reason: "', 1)[1].rsplit('"', 1)[0]
        return {
            'timestamp': timestamp,
            'from': from_part,
            'to': to_part,
            'reason': reason_part
        }
    except Exception:
        return {}

def summary_entries():
    ensure_logfile_exists()
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    switches = [parse_entry(l) for l in lines if l.strip()]
    if not switches:
        print('ログがありません。')
        return
    print(f'合計 {len(switches)} 件の切り替え履歴:')
    from_counts = {}
    to_counts = {}
    for sw in switches:
        from_counts[sw.get('from','')] = from_counts.get(sw.get('from',''), 0) + 1
        to_counts[sw.get('to','')] = to_counts.get(sw.get('to',''), 0) + 1
    print('\n[切り替え元ランキング]')
    for k, v in sorted(from_counts.items(), key=lambda x: -x[1]):
        print(f'- {k}: {v}回')
    print('\n[切り替え先ランキング]')
    for k, v in sorted(to_counts.items(), key=lambda x: -x[1]):
        print(f'- {k}: {v}回')
    print('\n[最新10件]')
    for sw in switches[-10:]:
        print(f"{sw['timestamp']} | {sw['from']} -> {sw['to']} | {sw['reason']}")

def prompt_input(prompt: str, default: str = "") -> str:
    try:
        val = input(prompt)
        if not val.strip() and default:
            return default
        return val.strip()
    except KeyboardInterrupt:
        print('\n中断されました')
        sys.exit(1)

def log_interactive():
    print('--- コンテキスト切り替えログ記録 ---')
    from_ctx = prompt_input('切り替え元 (from): ')
    to_ctx = prompt_input('切り替え先 (to): ')
    reason = prompt_input('理由 (任意): ')
    if not from_ctx or not to_ctx:
        print('切り替え元・先は必須です')
        sys.exit(1)
    log_entry(from_ctx, to_ctx, reason)

def main():
    parser = argparse.ArgumentParser(description='Context Switch Logbook')
    subparsers = parser.add_subparsers(dest='command')

    log_parser = subparsers.add_parser('log', help='切り替えを記録')
    log_parser.add_argument('--from', dest='from_ctx', type=str, help='切り替え元')
    log_parser.add_argument('--to', dest='to_ctx', type=str, help='切り替え先')
    log_parser.add_argument('--reason', dest='reason', type=str, default='', help='理由メモ')

    list_parser = subparsers.add_parser('list', help='ログ一覧')
    list_parser.add_argument('--limit', type=int, default=0, help='最新N件のみ表示')

    subparsers.add_parser('summary', help='統計・要約')

    args = parser.parse_args()
    if args.command == 'log':
        if args.from_ctx and args.to_ctx:
            log_entry(args.from_ctx, args.to_ctx, args.reason)
        else:
            log_interactive()
    elif args.command == 'list':
        list_entries(args.limit)
    elif args.command == 'summary':
        summary_entries()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
