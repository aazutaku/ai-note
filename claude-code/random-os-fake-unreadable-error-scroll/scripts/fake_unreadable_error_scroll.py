import sys
import argparse
import random
import time
import os
import shutil
from typing import List

def generate_gibberish_line():
    gibberish = [
        '*#@!&^%$#@!',
        'ΣΔΩΞΨΛ',
        '0xDEADBEEF',
        'UNK_ERR_ΣΔΩΞΨΛ',
        '010101000110100001100101',
        'Zkqvbnw',
        'GHLKJ',
        '/dev/scrolls/ancient.log',
        'SYS_UNREADABLE_FAULT',
        'ERR: 0x1A2B3C',
        '???',
        'WARNING: 0xBADF00D',
        'CRITICAL: UNK_ΣΔΩ',
        'TRACEBACK: <unreadable>',
        'FATAL: [NULLPTR]',
        'panic: segmentation scroll',
        'Memory dump: 0x00ff00ff',
        'Stacktrace: ???',
        'core dumped',
        'Segmentation fault',
        'Bus error',
        'Unknown opcode',
        'Illegal instruction',
        'System halt',
        'Scroll error',
        '巻物破損',
        'バイナリ断片',
        'ファイル読込失敗',
        'データ欠損',
        'アクセス拒否',
        'アクセス違反',
    ]
    return random.choice(gibberish)

def generate_scroll_lines(num_lines: int = 6) -> List[str]:
    lines = []
    # 1行目はタイトル風
    lines.append(f"ERROR: [{random.choice(['0x1A2B3C','0xBADF00D','0xDEADBEEF','0xCAFEBABE'])}] {generate_gibberish_line()}")
    for _ in range(num_lines-2):
        key = random.choice(['Zkqvbnw', 'GHLKJ', '???', 'TRACE', 'ERR', 'CRIT', 'WARN'])
        val = generate_gibberish_line()
        lines.append(f"{key}: {val}")
    # 最後は締めの一言
    ending = random.choice([
        '解読者求ム',
        '解決不能',
        '巻物破損',
        'バグ報告不可',
        '理解不能',
        'OS開発者募集中',
        '全ては巻物の中',
        '運命に従え',
        '再起動推奨',
        'Good luck!'
    ])
    lines.append(ending)
    return lines

def get_terminal_width():
    try:
        columns, _ = shutil.get_terminal_size(fallback=(80, 20))
        return columns
    except Exception:
        return 80

def format_scroll_box(lines: List[str]) -> List[str]:
    width = max(len(line) for line in lines) + 4
    width = min(width, get_terminal_width() - 2)
    top = '┏' + '━' * (width - 2) + '┓'
    bottom = '┗' + '━' * (width - 2) + '┛'
    box_lines = [top]
    for line in lines:
        l = line[:width-4]
        box_lines.append('┃ ' + l.ljust(width-4) + ' ┃')
    box_lines.append(bottom)
    return box_lines

def scroll_print(box_lines: List[str], delay: float = 0.2):
    for line in box_lines:
        print(line)
        sys.stdout.flush()
        time.sleep(delay)

def log_error_to_file(lines: List[str], path: str = 'fake_scroll_error.log'):
    try:
        with open(path, 'a', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')
            f.write('\n')
    except Exception as e:
        print(f"[log_error_to_file] Logging failed: {e}", file=sys.stderr)

def list_log(path: str = 'fake_scroll_error.log', tail: int = 10):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        if not lines:
            print('(ログはありません)')
            return
        print(''.join(lines[-tail:]))
    except FileNotFoundError:
        print('(ログファイルが存在しません)')
    except Exception as e:
        print(f"[list_log] 読み込み失敗: {e}", file=sys.stderr)

def summary_log(path: str = 'fake_scroll_error.log'):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        count = sum(1 for line in lines if line.startswith('┏'))
        print(f"記録された巻物エラー数: {count}")
    except FileNotFoundError:
        print('(ログファイルが存在しません)')
    except Exception as e:
        print(f"[summary_log] 読み込み失敗: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description='謎のOS古代バグ巻物エラー演出スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='巻物エラーを生成して表示＆ログ')
    parser_log.add_argument('--lines', type=int, default=6, help='エラー行数(デフォルト6)')
    parser_log.add_argument('--no-scroll', action='store_true', help='スクロールせず一括表示')
    parser_log.add_argument('--no-log', action='store_true', help='ログファイルに記録しない')

    parser_list = subparsers.add_parser('list', help='エラーログの末尾を表示')
    parser_list.add_argument('--tail', type=int, default=10, help='末尾表示行数(デフォルト10)')

    parser_summary = subparsers.add_parser('summary', help='エラーログの件数を集計')

    args = parser.parse_args()

    if args.command == 'log':
        lines = generate_scroll_lines(num_lines=args.lines)
        box = format_scroll_box(lines)
        if args.no_scroll:
            print('\n'.join(box))
        else:
            scroll_print(box)
        if not args.no_log:
            log_error_to_file(box)
    elif args.command == 'list':
        list_log(tail=args.tail)
    elif args.command == 'summary':
        summary_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
