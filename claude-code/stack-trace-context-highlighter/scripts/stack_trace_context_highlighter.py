import argparse
import re
import sys
from typing import List, Dict, Tuple, Set

def parse_stack_trace(trace_lines: List[str]) -> List[Dict[str, str]]:
    """
    Parse stack trace lines and extract file, line, and function info.
    Supports Python and generic formats.
    Returns a list of dicts: {file, line, func}
    """
    stack_entries = []
    py_re = re.compile(r'  File "([^"]+)", line (\d+), in ([^\s]+)')
    generic_re = re.compile(r'at ([^\s]+)\(([^:]+):(\d+)\)')
    for line in trace_lines:
        m = py_re.search(line)
        if m:
            stack_entries.append({
                'file': m.group(1),
                'line': m.group(2),
                'func': m.group(3)
            })
            continue
        m = generic_re.search(line)
        if m:
            stack_entries.append({
                'file': m.group(2),
                'line': m.group(3),
                'func': m.group(1)
            })
    return stack_entries

def parse_open_files(open_files: List[str]) -> Set[str]:
    return set(open_files)

def parse_recent_edits(recent_edits: List[str]) -> Set[Tuple[str, int]]:
    edits = set()
    for edit in recent_edits:
        if ':' in edit:
            file, line = edit.rsplit(':', 1)
            try:
                edits.add((file, int(line)))
            except ValueError:
                continue
    return edits

def highlight_candidates(stack_entries, open_files, recent_edits):
    highlights = []
    for entry in stack_entries:
        status = []
        file = entry['file']
        line = int(entry['line'])
        if file in open_files:
            status.append('open')
        if (file, line) in recent_edits:
            status.append('recent edit')
        highlights.append({'file': file, 'line': line, 'func': entry['func'], 'status': status})
    return highlights

def print_highlight_summary(highlights):
    print('[stack-trace-context-highlighter] ハイライト候補:')
    for h in highlights:
        status = ', '.join(h['status']) if h['status'] else 'not open'
        print(f"- {h['file']}:{h['line']} ({status})")
    attention = [f"{h['file']}:{h['line']}" for h in highlights if 'open' in h['status'] or 'recent edit' in h['status']]
    if attention:
        print(f"\n注目: {', '.join(attention)}")
    else:
        print("\n注目: (該当なし)")

def read_trace_file(trace_file: str) -> List[str]:
    try:
        with open(trace_file, 'r', encoding='utf-8') as f:
            return f.readlines()
    except Exception as e:
        print(f"[Error] スタックトレースファイル読み込み失敗: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Stack Trace Context Highlighter')
    parser.add_argument('--trace-file', type=str, required=True, help='スタックトレースのファイルパス')
    parser.add_argument('--open-files', type=str, nargs='*', default=[], help='現在開いているファイル名リスト')
    parser.add_argument('--recent-edits', type=str, nargs='*', default=[], help='直近編集したファイル:行番号リスト (例: main.py:42)')
    parser.add_argument('--summary', action='store_true', help='ハイライト結果のみ要約表示')
    args = parser.parse_args()

    trace_lines = read_trace_file(args.trace_file)
    stack_entries = parse_stack_trace(trace_lines)
    if not stack_entries:
        print('[stack-trace-context-highlighter] スタックトレース情報が検出できません')
        sys.exit(1)
    open_files = parse_open_files(args.open_files)
    recent_edits = parse_recent_edits(args.recent_edits)
    highlights = highlight_candidates(stack_entries, open_files, recent_edits)
    if args.summary:
        attention = [f"{h['file']}:{h['line']}" for h in highlights if 'open' in h['status'] or 'recent edit' in h['status']]
        print(', '.join(attention) if attention else '(該当なし)')
    else:
        print_highlight_summary(highlights)

if __name__ == '__main__':
    main()
