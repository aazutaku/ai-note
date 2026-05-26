import sys
import argparse
import time
import threading
import platform
import psutil
import pygetwindow as gw
import pyautogui
import tkinter as tk
from tkinter import ttk

# --- ウィンドウ検出・隠蔽 ---
def find_target_windows():
    """
    エディタ・ターミナル系ウィンドウを列挙し、隠す対象を返す
    """
    targets = []
    keywords = ['code', 'vscode', 'sublime', 'pycharm', 'notepad', 'terminal', 'cmd', 'powershell', 'bash', 'zsh', 'iterm', 'konsole', 'gnome-terminal', 'xterm']
    for w in gw.getAllWindows():
        title = w.title.lower()
        if any(k in title for k in keywords):
            targets.append(w)
    return targets

def hide_windows(windows):
    for w in windows:
        try:
            w.minimize()
        except Exception:
            pass

def restore_windows(windows):
    for w in windows:
        try:
            w.restore()
        except Exception:
            pass

# --- 偽装画面 ---
class FakeScreen(tk.Tk):
    def __init__(self, style='excel', progress=0):
        super().__init__()
        self.style = style
        self.progress = progress
        self.title(self._get_title())
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self.attributes('-fullscreen', True)
        self._build_ui()
        self.closed = False
        self.bind('<Control-Shift-Q>', self._close_event)

    def _get_title(self):
        if self.style == 'excel':
            return 'Microsoft Excel - report.xlsx'
        elif self.style == 'weather':
            return 'Weather Forecast'
        else:
            return 'Desktop'

    def _build_ui(self):
        if self.style == 'excel':
            self._build_excel_ui()
        elif self.style == 'weather':
            self._build_weather_ui()
        else:
            self._build_blank_ui()

    def _build_excel_ui(self):
        frame = tk.Frame(self, bg='#ffffff')
        frame.pack(fill='both', expand=True)
        tk.Label(frame, text='A', bg='#e0e0e0').place(x=60, y=40)
        tk.Label(frame, text='B', bg='#e0e0e0').place(x=120, y=40)
        for i in range(1, 11):
            tk.Label(frame, text=str(i), bg='#e0e0e0').place(x=20, y=40+30*i)
        for row in range(1, 11):
            for col in range(2):
                e = tk.Entry(frame, width=12, bg='#f9f9f9')
                e.place(x=60+col*60, y=40+row*30)
                if row == 1 and col == 0:
                    e.insert(0, '進捗レポート')
        # 進捗バー
        if self.progress > 0:
            pb = ttk.Progressbar(frame, length=300, mode='determinate')
            pb.place(x=60, y=380)
            pb['value'] = self.progress
            tk.Label(frame, text=f'進捗: {self.progress}%', bg='#ffffff').place(x=370, y=380)

    def _build_weather_ui(self):
        frame = tk.Frame(self, bg='#cce6ff')
        frame.pack(fill='both', expand=True)
        tk.Label(frame, text='Weather Forecast', font=('Arial', 28), bg='#cce6ff').pack(pady=60)
        tk.Label(frame, text='Tokyo: 22°C, Sunny', font=('Arial', 18), bg='#cce6ff').pack(pady=10)
        tk.Label(frame, text='Osaka: 21°C, Cloudy', font=('Arial', 18), bg='#cce6ff').pack(pady=10)
        tk.Label(frame, text='Fukuoka: 23°C, Rain', font=('Arial', 18), bg='#cce6ff').pack(pady=10)

    def _build_blank_ui(self):
        frame = tk.Frame(self, bg='#f0f0f0')
        frame.pack(fill='both', expand=True)
        tk.Label(frame, text=' ', bg='#f0f0f0').pack()

    def _on_close(self):
        self.closed = True
        self.destroy()

    def _close_event(self, event):
        self._on_close()

    def run(self):
        self.mainloop()

# --- メイン処理 ---
def main():
    parser = argparse.ArgumentParser(description='boss-key-instant-hide: 一発で画面を隠し偽装画面を表示')
    parser.add_argument('--style', choices=['excel', 'weather', 'blank'], default='excel', help='偽装画面のスタイル')
    parser.add_argument('--progress', type=int, default=0, help='進捗バーの表示率 (0-100)')
    parser.add_argument('--restore', action='store_true', help='隠したウィンドウを復元して終了')
    args = parser.parse_args()

    # 隠す対象ウィンドウ検出
    target_windows = find_target_windows()
    if not args.restore:
        if target_windows:
            print(f"[INFO] 隠したウィンドウ: {', '.join([w.title for w in target_windows])}")
            hide_windows(target_windows)
        else:
            print("[INFO] 隠すべきウィンドウが見つかりませんでした")
        print(f"[INFO] 偽装画面 ({args.style}風) を表示中...")
        if args.progress > 0:
            bar = '█' * (args.progress // 5) + '░' * (20 - args.progress // 5)
            print(f"[PROGRESS] 進捗: [{bar}] {args.progress}%")
        print("[INFO] 解除は Ctrl+Shift+Q で可能")
        # 偽装画面表示
        fake = FakeScreen(style=args.style, progress=args.progress)
        fake.run()
        # 終了時に元のウィンドウを復元
        restore_windows(target_windows)
        print("[INFO] 元の作業画面を復元しました")
    else:
        restore_windows(target_windows)
        print("[INFO] 隠したウィンドウを復元しました")

if __name__ == '__main__':
    main()
