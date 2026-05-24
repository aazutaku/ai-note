import argparse
import os
import re
import sys
from typing import List, Tuple, Optional, Dict

STACK_TRACE_PATTERN = re.compile(r'  File "([^"]+)", line (\d+), in ([^\s]+)')
PYTHON_TRACEBACK_HEADER = re.compile(r'Traceback \(most recent call last\):')


def parse_stack_trace(lines: List[str]) -> List[Dict[str, str]]:
    """
    Parse stack trace lines and extract file, line, and function info.
    """
    stack = []
    for line in lines:
        m = STACK_TRACE_PATTERN.search(line)
        if m:
            stack.append({
                'file': m.group(1),
                'line': m.group(2),
                'func': m.group(3)
            })
    return stack


def extract_traceback(log: str) -> Optional[List[str]]:
    """
    Extract the traceback section from a log string.
    """
    lines = log.splitlines()
    start = None
    for i, line in enumerate(lines):
        if PYTHON_TRACEBACK_HEADER.match(line):
            start = i
            break
    if start is not None:
        # Extract until a line that doesn't start with space or 'File'
        tb_lines = []
        for l in lines[start+1:]:
            if l.startswith('  File') or l.strip() == '' or l.startswith('    '):
                tb_lines.append(l)
            else:
                break
        return lines[start:start+1] + tb_lines
    return None


def get_open_files_from_env() -> List[str]:
    """
    Try to get list of open files from environment variable (simulate editor integration).
    """
    files = os.environ.get('OPEN_FILES')
    if files:
        return [f.strip() for f in files.split(';') if f.strip()]
    return []


def get_last_edited_file_from_env() -> Optional[str]:
    return os.environ.get('LAST_EDITED_FILE')


def highlight_context(stack: List[Dict[str, str]], open_files: List[str], last_edited: Optional[str]) -> Dict:
    relevant = []
    for frame in stack:
        fname = os.path.abspath(frame['file'])
        for of in open_files:
            if os.path.abspath(of) == fname:
                relevant.append((frame, True))
                break
        else:
            relevant.append((frame, False))
    # Prefer the frame matching last_edited
    nav = None
    if last_edited:
        for frame, is_open in relevant:
            if os.path.abspath(frame['file']) == os.path.abspath(last_edited):
                nav = frame
                break
    if not nav and relevant:
        nav = relevant[-1][0]
    return {
        'relevant': relevant,
        'navigate': nav
    }


def print_highlight_result(stack: List[Dict[str, str]], context: Dict, traceback_lines: List[str]):
    print('[stack-trace-context-highlighter]')
    files = set([frame['file'] for frame, is_open in context['relevant'] if is_open])
    if files:
        print(f'- 関連ファイル: ' + ', '.join(f'{f} (編集中)' for f in files))
    else:
        print(f'- 関連ファイル: なし')
    print('- 注目関数: ' + ', '.join(f"{frame['func']} (行{frame['line']})" for frame, _ in context['relevant']))
    if context['navigate']:
        print(f"- 推奨ナビゲート: {context['navigate']['file']}:{context['navigate']['line']}")
    else:
        print(f"- 推奨ナビゲート: なし")
    print('- スタックトレース抜粋:')
    for l in traceback_lines:
        print('  ' + l)


def main():
    parser = argparse.ArgumentParser(description='Stack Trace Context Highlighter')
    parser.add_argument('--logfile', type=str, help='Log file containing stack trace (default: stdin)')
    parser.add_argument('--open-files', type=str, help='Semicolon-separated list of currently open files')
    parser.add_argument('--last-edited', type=str, help='Last edited file path')
    parser.add_argument('--demo', action='store_true', help='Show demo with sample traceback')
    args = parser.parse_args()

    if args.demo:
        log = '''Traceback (most recent call last):
  File "src/main.py", line 10, in main
    load_data()
  File "src/utils/data_loader.py", line 42, in load_data
    raise ValueError("Invalid format")
ValueError: Invalid format'''
        open_files = ['src/utils/data_loader.py', 'src/main.py']
        last_edited = 'src/utils/data_loader.py'
    else:
        if args.logfile:
            with open(args.logfile, 'r', encoding='utf-8') as f:
                log = f.read()
        else:
            log = sys.stdin.read()
        open_files = args.open_files.split(';') if args.open_files else get_open_files_from_env()
        last_edited = args.last_edited or get_last_edited_file_from_env()

    traceback_lines = extract_traceback(log)
    if not traceback_lines:
        print('No recognizable stack trace found.')
        sys.exit(1)
    stack = parse_stack_trace(traceback_lines)
    if not stack:
        print('No stack frames found in the traceback.')
        sys.exit(1)
    context = highlight_context(stack, open_files, last_edited)
    print_highlight_result(stack, context, traceback_lines)

if __name__ == '__main__':
    main()
