import sys
import time
import argparse
import threading
import platform
import subprocess
from typing import List

try:
    import pygetwindow as gw
    import pyautogui
except ImportError:
    print('[ERROR] 必要なライブラリ(pygetwindow, pyautogui)が見つかりません。\n pip install pygetwindow pyautogui')
    sys.exit(1)
try:
    import tkinter as tk
except ImportError:
    print('[ERROR] tkinterが見つかりません。標準Pythonに含まれていますが、OSによっては別途インストールが必要です。')
    sys.exit(1)

HIDE_DURATION = 5  # 秒数
DUMMY_WINDOW_TITLE = '天気予報 - 気象庁'
EXCEL_WINDOW_TITLE = 'Excel - 進捗管理表'

class BossKeyManager:
    def __init__(self):
        self.hidden_windows = []
        self.dummy_window = None
        self.os_name = platform.system()

    def list_target_windows(self) -> List:
        # エディタやターミナルらしきウィンドウを検出
        candidates = []
        for w in gw.getAllWindows():
            title = w.title.lower()
            if any(x in title for x in ['code', 'vim', 'sublime', 'notepad', 'terminal', 'cmd', 'powershell', 'pycharm', 'jupyter', 'atom', 'emacs']):
                candidates.append(w)
        return candidates

    def hide_windows(self, windows: List):
        for w in windows:
            try:
                w.minimize()
                self.hidden_windows.append(w)
            except Exception as e:
                print(f'[WARN] {w.title} の最小化に失敗: {e}')

    def restore_windows(self):
        for w in self.hidden_windows:
            try:
                w.restore()
            except Exception:
                pass
        self.hidden_windows = []

    def show_dummy_window(self, mode='weather'):
        root = tk.Tk()
        root.title(DUMMY_WINDOW_TITLE if mode=='weather' else EXCEL_WINDOW_TITLE)
        root.geometry('600x300+200+200')
        if mode == 'weather':
            label = tk.Label(root, text='東京 24℃ 晴れ\n明日: 22-28℃', font=('Arial', 32))
            label.pack(expand=True)
        elif mode == 'excel':
            import random
            import tkinter.ttk as ttk
            tree = ttk.Treeview(root, columns=('A','B','C'), show='headings')
            for i, col in enumerate(['タスク', '担当', '進捗']):
                tree.heading(i, text=col)
                tree.column(i, width=180)
            for i in range(5):
                tree.insert('', 'end', values=(f'タスク{i+1}', f'担当{i+1}', f'{random.randint(50,100)}%'))
            tree.pack(expand=True, fill='both')
        elif mode == 'progress':
            progress = tk.DoubleVar()
            pb = tk.ttk.Progressbar(root, length=400, variable=progress, maximum=100)
            pb.pack(pady=60)
            label = tk.Label(root, text='進捗バー: 70%', font=('Arial', 20))
            label.pack()
            progress.set(70)
        self.dummy_window = root
        # 別スレッドでmainloop
        threading.Thread(target=root.mainloop, daemon=True).start()

    def close_dummy_window(self):
        if self.dummy_window:
            try:
                self.dummy_window.destroy()
            except Exception:
                pass
            self.dummy_window = None

    def boss_key(self, mode='weather', duration=HIDE_DURATION):
        print('[INFO] エディタ/ターミナルウィンドウを検出中...')
        targets = self.list_target_windows()
        if not targets:
            print('[INFO] 隠すべきウィンドウが見つかりません。')
        else:
            print(f'[INFO] {len(targets)}個のウィンドウを最小化します。')
            self.hide_windows(targets)
        print(f'[INFO] {"天気予報" if mode=="weather" else "Excel風"}ウィンドウを前面に表示します。')
        self.show_dummy_window(mode=mode)
        if mode == 'progress':
            print('[INFO] ダミー進捗バー: [███████-----] 70%')
        print(f'[INFO] {duration}秒後に元の状態に戻せます。')
        time.sleep(duration)
        self.close_dummy_window()
        self.restore_windows()
        print('[INFO] 元のウィンドウ状態に復帰しました。')

    def list_windows(self):
        print('現在のウィンドウ一覧:')
        for w in gw.getAllWindows():
            print(f'- {w.title}')

    def summary(self):
        print('boss-key-instant-hide の概要:')
        print('・検出対象: エディタ/ターミナル/開発ツール')
        print('・偽装画面: 天気予報/Excel/進捗バー')
        print('・サポートOS:', self.os_name)


def main():
    parser = argparse.ArgumentParser(description='boss-key-instant-hide: 一発で画面を隠し偽装ウィンドウを表示')
    subparsers = parser.add_subparsers(dest='command')

    parser_boss = subparsers.add_parser('hide', help='画面を隠して偽装ウィンドウを表示')
    parser_boss.add_argument('--mode', choices=['weather','excel','progress'], default='weather', help='偽装画面の種類')
    parser_boss.add_argument('--duration', type=int, default=HIDE_DURATION, help='偽装画面を表示する秒数')

    parser_list = subparsers.add_parser('list', help='現在のウィンドウ一覧を表示')
    parser_summary = subparsers.add_parser('summary', help='本Skillの概要を表示')

    args = parser.parse_args()
    manager = BossKeyManager()
    if args.command == 'hide':
        manager.boss_key(mode=args.mode, duration=args.duration)
    elif args.command == 'list':
        manager.list_windows()
    elif args.command == 'summary':
        manager.summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
