import sys
import argparse
import threading
import time
import platform

try:
    import pygetwindow as gw
except ImportError:
    print('[ERROR] pygetwindow モジュールが必要です: pip install pygetwindow')
    sys.exit(1)

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    print('[ERROR] tkinter が必要です')
    sys.exit(1)

TARGETS = ['code', 'Code', 'powershell', 'Terminal', 'cmd', 'gnome-terminal', 'konsole', 'iTerm2', 'Alacritty']

FAKE_MODES = ['weather', 'excel', 'progress']

class BossKey:
    def __init__(self, mode):
        self.mode = mode if mode in FAKE_MODES else 'excel'
        self.hidden_windows = []
        self.fake_root = None
        self.progress_var = None
        self._stop_event = threading.Event()

    def hide_windows(self):
        found = False
        for w in gw.getAllWindows():
            for t in TARGETS:
                if t.lower() in w.title.lower() or t.lower() in w._hWndName.lower():
                    try:
                        w.minimize()
                        self.hidden_windows.append(w)
                        found = True
                        print(f'[INFO] 隠蔽対象: {w.title}')
                    except Exception as e:
                        print(f'[WARN] {w.title} の最小化に失敗: {e}')
        if not found:
            print('[INFO] 隠蔽対象ウィンドウは見つかりませんでした')
        else:
            print('[INFO] 画面を非表示にしました')

    def show_fake_window(self):
        if self.mode == 'weather':
            self._show_weather()
        elif self.mode == 'excel':
            self._show_excel()
        elif self.mode == 'progress':
            self._show_progress()

    def _show_weather(self):
        root = tk.Tk()
        root.title('天気予報')
        root.geometry('480x300')
        tk.Label(root, text='今日の天気', font=('Arial', 22)).pack(pady=20)
        tk.Label(root, text='東京: 晴れ 25℃', font=('Arial', 16)).pack(pady=10)
        tk.Label(root, text='大阪: 曇り 23℃', font=('Arial', 16)).pack(pady=5)
        tk.Label(root, text='札幌: 雨 18℃', font=('Arial', 16)).pack(pady=5)
        tk.Label(root, text='（ダミー表示）', font=('Arial', 10)).pack(pady=30)
        tk.Label(root, text='解除は Ctrl+Shift+B', font=('Arial', 10)).pack(side='bottom')
        self.fake_root = root
        root.after(100, self._check_stop)
        root.mainloop()

    def _show_excel(self):
        root = tk.Tk()
        root.title('Excel - 進捗管理表.xlsx')
        root.geometry('640x320')
        tk.Label(root, text='進捗管理表', font=('Meiryo', 16, 'bold')).pack(pady=10)
        frame = tk.Frame(root)
        frame.pack(pady=10)
        headers = ['タスク', '担当', '進捗']
        for i, h in enumerate(headers):
            tk.Label(frame, text=h, borderwidth=1, relief='solid', width=12).grid(row=0, column=i)
        tasks = [
            ('要件定義', '田中', '完了'),
            ('設計', '佐藤', '進行中'),
            ('実装', '鈴木', '未着手'),
            ('テスト', '山田', '未着手')
        ]
        for r, row in enumerate(tasks):
            for c, val in enumerate(row):
                tk.Label(frame, text=val, borderwidth=1, relief='solid', width=12).grid(row=r+1, column=c)
        self.progress_var = tk.DoubleVar()
        progress = ttk.Progressbar(root, variable=self.progress_var, maximum=100, length=400)
        progress.pack(pady=20)
        self.progress_var.set(60)
        tk.Label(root, text='60% 完了', font=('Arial', 12)).pack()
        tk.Label(root, text='解除は Ctrl+Shift+B', font=('Arial', 10)).pack(side='bottom')
        self.fake_root = root
        root.after(100, self._check_stop)
        root.mainloop()

    def _show_progress(self):
        root = tk.Tk()
        root.title('進捗バー')
        root.geometry('400x120')
        tk.Label(root, text='データ処理中...', font=('Arial', 14)).pack(pady=10)
        self.progress_var = tk.DoubleVar()
        progress = ttk.Progressbar(root, variable=self.progress_var, maximum=100, length=300)
        progress.pack(pady=10)
        self.progress_var.set(0)
        tk.Label(root, text='解除は Ctrl+Shift+B', font=('Arial', 10)).pack(side='bottom')
        threading.Thread(target=self._progress_anim, args=(root,)).start()
        self.fake_root = root
        root.after(100, self._check_stop)
        root.mainloop()

    def _progress_anim(self, root):
        for i in range(0, 101, 10):
            if self._stop_event.is_set():
                break
            self.progress_var.set(i)
            time.sleep(0.5)
        if not self._stop_event.is_set():
            self.progress_var.set(100)

    def _check_stop(self):
        # キーバインド解除
        self.fake_root.bind_all('<Control-Shift-B>', self._on_unhide)
        if not self._stop_event.is_set():
            self.fake_root.after(100, self._check_stop)

    def _on_unhide(self, event=None):
        self._stop_event.set()
        self.fake_root.destroy()
        self.restore_windows()

    def restore_windows(self):
        for w in self.hidden_windows:
            try:
                w.restore()
            except Exception:
                pass
        print('[INFO] 隠蔽ウィンドウを元に戻しました')


def parse_args():
    parser = argparse.ArgumentParser(description='boss-key-instant-hide: 一発で画面を隠して偽装画面を表示')
    parser.add_argument('--mode', choices=FAKE_MODES, default='excel', help='偽装画面タイプ (weather/excel/progress)')
    return parser.parse_args()


def main():
    args = parse_args()
    print(f'[INFO] boss-key-instant-hide 起動 (mode={args.mode})')
    boss = BossKey(mode=args.mode)
    boss.hide_windows()
    print(f'[INFO] 偽装画面: {args.mode} を表示中...')
    boss.show_fake_window()

if __name__ == '__main__':
    main()
