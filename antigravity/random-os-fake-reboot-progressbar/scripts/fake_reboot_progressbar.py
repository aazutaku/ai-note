import sys
import time
import random
import threading
import argparse
import tkinter as tk
from tkinter import ttk

# ランダムな進捗メッセージ集
MESSAGES = [
    "再起動準備中…",
    "謎のプロセス終了中…",
    "システム設定を初期化中…",
    "メモリを解放しています…",
    "カーネルを再構築中…",
    "未知のエラーを処理中…",
    "仮想デバイスを切断中…",
    "ログを消去しています…",
    "ほぼ完了、あと3分で全てがリセットされます",
    "再起動完了！何も変わりませんでした。"
]

# 進捗バーのウィンドウクラス
def random_message(progress):
    if progress >= 99:
        return MESSAGES[-1]
    idx = min(int(progress / (100 / (len(MESSAGES)-1))), len(MESSAGES)-2)
    base = MESSAGES[idx]
    # 10%ごとにランダムで変化
    if random.random() < 0.3:
        base = random.choice(MESSAGES[:-1])
    return base

class FakeRebootProgressBar:
    def __init__(self, duration=15, position='top_right'):
        self.duration = duration
        self.position = position
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.configure(bg='black')
        self.progress = tk.DoubleVar()
        self.label = tk.Label(self.root, text='', fg='white', bg='black', font=('Consolas', 12))
        self.label.pack(padx=18, pady=(8,2))
        self.bar = ttk.Progressbar(self.root, variable=self.progress, maximum=100, length=320)
        self.bar.pack(padx=18, pady=(0,8))
        self.set_position()
        self.running = True

    def set_position(self):
        self.root.update_idletasks()
        w = self.root.winfo_reqwidth()
        h = self.root.winfo_reqheight()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        if self.position == 'top_right':
            x = sw - w - 20
            y = 20
        elif self.position == 'bottom_left':
            x = 20
            y = sh - h - 60
        else:
            x = (sw - w) // 2
            y = (sh - h) // 2
        self.root.geometry(f'+{x}+{y}')

    def update_progress(self):
        steps = self.duration * 20
        for i in range(steps + 1):
            if not self.running:
                break
            progress = (i / steps) * 100
            msg = random_message(progress)
            self.progress.set(progress)
            self.label.config(text=f'{msg}')
            self.root.update()
            time.sleep(self.duration / steps)
        self.running = False
        self.root.after(800, self.root.destroy)

    def run(self):
        threading.Thread(target=self.update_progress, daemon=True).start()
        self.root.mainloop()

# CLIサブコマンド

def list_messages():
    print("--- ランダム進捗メッセージ一覧 ---")
    for m in MESSAGES:
        print(f'- {m}')

def main():
    parser = argparse.ArgumentParser(description='謎のOS再起動進捗バーを表示します')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='進捗バーを表示')
    parser_run.add_argument('--duration', type=int, default=15, help='進捗バーの表示秒数 (デフォルト: 15)')
    parser_run.add_argument('--position', choices=['top_right', 'bottom_left', 'center'], default='top_right', help='表示位置')

    parser_list = subparsers.add_parser('list', help='進捗メッセージ一覧を表示')

    args = parser.parse_args()

    if args.command == 'run':
        try:
            bar = FakeRebootProgressBar(duration=args.duration, position=args.position)
            bar.run()
        except Exception as e:
            print(f'エラー: {e}')
            sys.exit(1)
    elif args.command == 'list':
        list_messages()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
