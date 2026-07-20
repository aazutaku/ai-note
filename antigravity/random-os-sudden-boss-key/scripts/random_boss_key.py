import sys
import argparse
import random
import string
import threading
import time
import tkinter as tk
from tkinter import messagebox

# ダミー画面生成用データ
ERROR_CODES = ["XJ-42A", "QW-13B", "PL-99Z", "MN-77X", "AB-01C"]
DUMMY_WARNINGS = [
    "System anomaly detected!",
    "Critical error occurred!",
    "Unknown OS event triggered!",
    "Access violation exception!",
    "Resource allocation failed!"
]
GRAPH_LABELS = ["CPU Utilization", "Memory", "Disk I/O", "Network", "GPU Load"]

# ダミー進捗バー生成
def random_bar(length=20, percent=None):
    if percent is None:
        percent = random.randint(10, 99)
    filled = int(length * percent / 100)
    bar = "█" * filled + "▒" * (length - filled)
    return f"{bar} {percent}%"

# ダミーグラフ生成
def random_graph():
    lines = []
    for label in random.sample(GRAPH_LABELS, k=random.randint(2, 4)):
        percent = random.randint(10, 99)
        bar = random_bar(10, percent)
        lines.append(f"{label}: {bar}")
    return "\n".join(lines)

# ダミー警告画面生成
def random_warning():
    code = random.choice(ERROR_CODES)
    warning = random.choice(DUMMY_WARNINGS)
    return f"[=== OS WARNING ===]\n{warning}\nError code: {code}\nPlease contact your administrator."

# ダミー画面の内容をランダム生成
def generate_dummy_screen():
    screens = []
    if random.random() < 0.5:
        screens.append(random_warning())
    if random.random() < 0.8:
        screens.append("\n[ランダムグラフ]\n" + random_graph())
    if random.random() < 0.3:
        screens.append(f"\n[謎の進捗]\nProgress: {random_bar(15)}")
    screens.append("\nPress ESC to return.")
    return "\n".join(screens)

# Tkinterで全画面ダミーウィンドウを表示
class DummyScreen:
    def __init__(self, timeout=10):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.root.bind('<Escape>', self.close)
        self.closed = False
        self.timeout = timeout
        self.label = tk.Label(
            self.root,
            text=generate_dummy_screen(),
            font=("Consolas", 16),
            fg="lime",
            bg="black",
            justify="left",
            anchor="nw"
        )
        self.label.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        self.root.after(int(self.timeout * 1000), self.close)

    def show(self):
        self.root.mainloop()

    def close(self, event=None):
        if not self.closed:
            self.closed = True
            self.root.destroy()

# CLIサブコマンド: show (ダミー画面表示)
def cmd_show(args):
    timeout = args.timeout if args.timeout else 10
    screen = DummyScreen(timeout=timeout)
    screen.show()

# CLIサブコマンド: test (ランダム内容生成テスト)
def cmd_test(args):
    print(generate_dummy_screen())

# CLIサブコマンド: info (Skill情報表示)
def cmd_info(args):
    print("random-os-sudden-boss-key Skill")
    print("- ダミー画面を全画面表示し、ESCまたはタイムアウトで復帰")
    print("- 内容は完全ランダム生成")
    print("- サブコマンド: show, test, info")

# メイン関数
def main():
    parser = argparse.ArgumentParser(description="random-os-sudden-boss-key: 謎のダミー画面で作業を隠す迷惑Skill")
    subparsers = parser.add_subparsers(dest='command')

    parser_show = subparsers.add_parser('show', help='ダミー画面を表示')
    parser_show.add_argument('--timeout', type=int, default=10, help='表示秒数 (デフォルト10秒)')
    parser_show.set_defaults(func=cmd_show)

    parser_test = subparsers.add_parser('test', help='ダミー画面内容を端末出力')
    parser_test.set_defaults(func=cmd_test)

    parser_info = subparsers.add_parser('info', help='Skill情報表示')
    parser_info.set_defaults(func=cmd_info)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
