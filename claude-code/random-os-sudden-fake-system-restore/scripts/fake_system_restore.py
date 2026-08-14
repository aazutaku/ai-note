import tkinter as tk
import random
import time
import argparse
import threading
import sys

FAKE_MESSAGES = [
    '謎の変更を元に戻しています...',
    'OSの気分調整中...',
    'レジストリの気まぐれ修復中...',
    'システムの気分をリセット中...',
    'ファイルの運命を再計算中...',
    '未知のエラーを無視しています...',
    '仮想メモリを再配置中...',
    'ユーザーの期待値を調整中...',
    '復元ポイントを探しています...',
    'OSのご機嫌をうかがっています...'
]

class FakeSystemRestoreWindow:
    def __init__(self, duration=8, randomize=True, verbose=False):
        self.duration = duration
        self.randomize = randomize
        self.verbose = verbose
        self.root = tk.Tk()
        self.root.title('OS System Restore')
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)
        self.progress = tk.DoubleVar()
        self.label = tk.Label(self.root, text='', font=('Meiryo', 12))
        self.label.pack(padx=20, pady=(18, 6))
        self.progressbar = tk.Canvas(self.root, width=320, height=24, bg='#e0e0e0', highlightthickness=0)
        self.progressbar.pack(padx=20, pady=(0, 16))
        self.text = tk.Label(self.root, text='', font=('Meiryo', 10), fg='#555')
        self.text.pack(padx=20, pady=(0, 12))
        self._place_window()

    def _place_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = sw - width - 40
        y = 40
        self.root.geometry(f'+{x}+{y}')

    def _draw_progress(self, percent):
        self.progressbar.delete('all')
        bar_len = int(320 * percent / 100)
        self.progressbar.create_rectangle(0, 0, bar_len, 24, fill='#4caf50', width=0)
        self.progressbar.create_rectangle(0, 0, 320, 24, outline='#888', width=1)

    def _random_message(self):
        return random.choice(FAKE_MESSAGES)

    def run(self):
        start_time = time.time()
        end_time = start_time + self.duration
        percent = 0
        last_percent = 0
        msg = self._random_message()
        self.label.config(text='[OS System Restore]')
        self.text.config(text=f'進捗: {percent}% - {msg}')
        self._draw_progress(percent)
        self.root.update()
        while percent < 100:
            now = time.time()
            elapsed = now - start_time
            if self.randomize:
                percent = min(100, int(random.uniform(last_percent + 5, last_percent + 25)))
            else:
                percent = min(100, int((elapsed / self.duration) * 100))
            if percent > 100:
                percent = 100
            msg = self._random_message()
            self.text.config(text=f'進捗: {percent}% - {msg}')
            self._draw_progress(percent)
            self.root.update()
            if self.verbose:
                print(f'Progress: {percent}% - {msg}')
            last_percent = percent
            if percent >= 100:
                break
            time.sleep(random.uniform(0.6, 1.6))
        self.text.config(text='進捗: 100% - 復元完了（何も変わりません）')
        self._draw_progress(100)
        self.root.update()
        time.sleep(1.8)
        self.root.destroy()


def launch_restore(duration=8, randomize=True, verbose=False):
    try:
        win = FakeSystemRestoreWindow(duration=duration, randomize=randomize, verbose=verbose)
        win.run()
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='Fake OS System Restore Progress Bar')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='Show the fake system restore window')
    parser_run.add_argument('--duration', type=int, default=8, help='Total duration (seconds)')
    parser_run.add_argument('--no-random', action='store_true', help='Disable random progress')
    parser_run.add_argument('--verbose', action='store_true', help='Verbose output')

    parser_demo = subparsers.add_parser('demo', help='Demo: show window with default settings')

    args = parser.parse_args()

    if args.command == 'run':
        launch_restore(duration=args.duration, randomize=not args.no_random, verbose=args.verbose)
    elif args.command == 'demo' or args.command is None:
        launch_restore(duration=8, randomize=True, verbose=False)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
