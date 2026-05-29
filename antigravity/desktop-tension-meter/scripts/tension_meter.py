import tkinter as tk
import random
import threading
import time
import argparse
import sys
import os
from datetime import datetime

TENSION_LABELS = [
    (0, 30, '平常心'),
    (31, 60, 'やや焦り'),
    (61, 80, '緊張'),
    (81, 100, '極度緊張')
]

POSITIONS = ['top_right', 'bottom_left', 'bottom_right', 'top_left']

LOG_FILE = os.path.expanduser('~/.desktop_tension_meter.log')


def get_random_tension():
    # 擬似的な根拠値: タイピング速度やコミット数を模倣
    base = random.randint(0, 100)
    # たまに"根拠あり"風の補正
    if random.random() < 0.2:
        base += random.randint(-10, 10)
    return max(0, min(100, base))


def get_tension_label(value):
    for low, high, label in TENSION_LABELS:
        if low <= value <= high:
            return label
    return '未知'


def get_random_position(screen_w, screen_h, window_w, window_h):
    pos = random.choice(POSITIONS)
    if pos == 'top_right':
        x = screen_w - window_w - 20
        y = 20
    elif pos == 'bottom_left':
        x = 20
        y = screen_h - window_h - 60
    elif pos == 'bottom_right':
        x = screen_w - window_w - 20
        y = screen_h - window_h - 60
    else:  # top_left
        x = 20
        y = 20
    return x, y


def show_tension_popup(label, value, duration=2):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.withdraw()
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    window_w = 350
    window_h = 60
    x, y = get_random_position(screen_w, screen_h, window_w, window_h)
    root.geometry(f'{window_w}x{window_h}+{x}+{y}')
    frame = tk.Frame(root, bg='#222', bd=2)
    frame.pack(fill='both', expand=True)
    label_widget = tk.Label(
        frame,
        text=f'現在の緊張度: {label} (推定値: {value})',
        fg='white',
        bg='#222',
        font=('Meiryo', 16, 'bold')
    )
    label_widget.pack(expand=True)
    root.deiconify()
    root.after(int(duration * 1000), root.destroy)
    root.mainloop()


def log_tension(label, value):
    with open(LOG_FILE, 'a') as f:
        f.write(f'{datetime.now().isoformat()}\t{label}\t{value}\n')


def tension_loop(interval_min=90, interval_max=300):
    try:
        while True:
            value = get_random_tension()
            label = get_tension_label(value)
            log_tension(label, value)
            show_tension_popup(label, value, duration=2.5)
            sleep_time = random.randint(interval_min, interval_max)
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print('Tension Meter stopped.')


def list_logs(count=10):
    if not os.path.exists(LOG_FILE):
        print('No log file found.')
        return
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()[-count:]
        for line in lines:
            print(line.strip())


def summary_logs():
    if not os.path.exists(LOG_FILE):
        print('No log file found.')
        return
    counts = {label: 0 for _, _, label in TENSION_LABELS}
    total = 0
    with open(LOG_FILE, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 3:
                label = parts[1]
                if label in counts:
                    counts[label] += 1
                    total += 1
    print('緊張度ラベル別出現回数:')
    for label, cnt in counts.items():
        print(f'{label}: {cnt}')
    print(f'合計: {total}')


def clear_logs():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print('Log file cleared.')
    else:
        print('No log file found.')


def main():
    parser = argparse.ArgumentParser(description='Desktop Tension Meter')
    subparsers = parser.add_subparsers(dest='command')

    run_parser = subparsers.add_parser('run', help='Start the tension meter loop')
    run_parser.add_argument('--interval-min', type=int, default=90, help='最小表示間隔(秒)')
    run_parser.add_argument('--interval-max', type=int, default=300, help='最大表示間隔(秒)')

    list_parser = subparsers.add_parser('list', help='Show recent tension logs')
    list_parser.add_argument('--count', type=int, default=10, help='表示件数')

    subparsers.add_parser('summary', help='Show summary of tension logs')
    subparsers.add_parser('clear', help='Clear log file')

    args = parser.parse_args()

    if args.command == 'run':
        tension_loop(interval_min=args.interval_min, interval_max=args.interval_max)
    elif args.command == 'list':
        list_logs(count=args.count)
    elif args.command == 'summary':
        summary_logs()
    elif args.command == 'clear':
        clear_logs()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
