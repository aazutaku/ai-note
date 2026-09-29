import sys
import time
import random
import argparse
import curses
import threading

# 意味不明な横文字・呪文ジェネレーター
def generate_gibberish_line():
    patterns = [
        lambda: ' '.join(random.choices(['Xqv', 'GxvZk', 'Qw!@#', 'ΩΔΞΨ', 'ΦΛΣ∏∫', 'zplmn$@!~', '0x' + ''.join(random.choices('0123456789ABCDEF', k=4)), 'FATAL:', 'SYST:', '∑ΩΔΞΨΦΛΣ∏∫'], k=random.randint(2,4))),
        lambda: ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()', k=random.randint(10, 24))),
        lambda: ' '.join([random.choice(['ERROR:', 'WARN:', 'INFO:', 'PANIC:', 'CRASH:', 'UNREADABLE:']) + ' ' + ''.join(random.choices('0123456789ABCDEF', k=6))]),
        lambda: ''.join(random.choices(['∑', 'Ω', 'Δ', 'Ξ', 'Ψ', 'Φ', 'Λ', 'Σ', '∏', '∫', 'π', 'λ', 'μ', 'ξ', 'ζ', 'θ', 'σ', 'τ'], k=random.randint(6, 12)))
    ]
    return patterns[random.randint(0, len(patterns)-1)]()

# 巻物風UIのラッパー
SCROLL_ENDINGS = [
    '[解読者求ム]',
    '[解決不能]',
    '[OS巻物: 永遠に未解読]',
    '[バグ報告不能]',
    '[UNKNOWN FATALITY]',
    '[NO HUMAN CAN FIX]',
    '[SEE YOU IN THE NEXT ERA]'
]

SCROLL_TITLE = [
    'ERROR: 0x8F2A3B - UNREADABLE',
    'SYSTEM PANIC: 0xDEADBEEF',
    'CRITICAL FAILURE: 0xBADF00D',
    'ANCIENT BUG: 0xC0FFEE',
    'FATAL EXCEPTION: 0xB16B00B5'
]

def scroll_error_screen(stdscr, lines, ending):
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()
    box_w = min(50, w - 4)
    box_h = min(len(lines) + 4, h - 4)
    start_x = (w - box_w) // 2
    start_y = (h - box_h) // 2
    win = curses.newwin(box_h, box_w, start_y, start_x)
    win.box()
    # タイトル
    title = random.choice(SCROLL_TITLE)
    win.addstr(1, 2, title[:box_w-4])
    win.refresh()
    time.sleep(0.7)
    # 本文スクロール
    for idx, line in enumerate(lines):
        if idx+2 < box_h-2:
            win.addstr(2+idx, 2, line[:box_w-4])
        else:
            # スクロール
            for j in range(2, box_h-2):
                win.move(j, 2)
                win.clrtoeol()
            for k in range(box_h-5):
                win.addstr(2+k, 2, lines[idx-box_h+5+k][:box_w-4])
            win.addstr(box_h-3, 2, line[:box_w-4])
        win.refresh()
        time.sleep(random.uniform(0.18, 0.33))
    # Ending
    win.addstr(box_h-2, 2, ending[:box_w-4])
    win.refresh()
    time.sleep(2.0)

def generate_error_scroll_lines(num_lines=8):
    return [generate_gibberish_line() for _ in range(num_lines)]

def run_scroll():
    lines = generate_error_scroll_lines(random.randint(6, 12))
    ending = random.choice(SCROLL_ENDINGS)
    curses.wrapper(scroll_error_screen, lines, ending)

def print_plain_scroll():
    title = random.choice(SCROLL_TITLE)
    lines = generate_error_scroll_lines(random.randint(6, 12))
    ending = random.choice(SCROLL_ENDINGS)
    border = '╭' + '─' * 38 + '╮'
    print(border)
    print('│ {:<36} │'.format(title[:36]))
    for l in lines:
        print('│ {:<36} │'.format(l[:36]))
    print('│ {:<36} │'.format(ending[:36]))
    print('╰' + '─' * 38 + '╯')

def schedule_scroll(interval=600, stop_event=None):
    while not (stop_event and stop_event.is_set()):
        time.sleep(interval)
        try:
            run_scroll()
        except Exception:
            print_plain_scroll()

def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Unreadable Error Scroll')
    subparsers = parser.add_subparsers(dest='command')
    parser_run = subparsers.add_parser('run', help='即座に巻物エラーを表示')
    parser_plain = subparsers.add_parser('plain', help='テキストのみで巻物エラーを表示')
    parser_auto = subparsers.add_parser('auto', help='定期的に巻物エラーを自動表示')
    parser_auto.add_argument('--interval', type=int, default=900, help='発動間隔(秒)')
    args = parser.parse_args()
    if args.command == 'run':
        try:
            run_scroll()
        except Exception:
            print_plain_scroll()
    elif args.command == 'plain':
        print_plain_scroll()
    elif args.command == 'auto':
        stop_event = threading.Event()
        try:
            schedule_scroll(args.interval, stop_event)
        except KeyboardInterrupt:
            stop_event.set()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
