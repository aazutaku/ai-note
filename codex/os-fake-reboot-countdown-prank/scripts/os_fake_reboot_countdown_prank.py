import sys
import time
import random
import argparse
import threading
import platform
try:
    from plyer import notification
except ImportError:
    notification = None
try:
    import tkinter as tk
    import tkinter.font as tkfont
except ImportError:
    tk = None

REASONS = [
    '謎のアップデート適用中',
    'RAMの気分転換を実施中',
    'OS自己啓発モード突入',
    'カーネルが瞑想中',
    'ファイルシステムの自己肯定感向上',
    'CPUが深呼吸しています',
    'バイナリの自己整理整頓',
    'システムがコーヒーブレイク中',
    'プロセスたちの座談会開催',
    '仮想メモリの夢見タイム'
]

DEFAULT_COUNTDOWN = 20

class PrankCountdown:
    def __init__(self, seconds, reason, use_gui=True):
        self.seconds = seconds
        self.reason = reason
        self.use_gui = use_gui and tk is not None
        self._stop = threading.Event()
        self.root = None
        self.label = None
        self.font = None

    def show_notification(self, message):
        if notification is not None:
            notification.notify(
                title='OS通知',
                message=message,
                timeout=5
            )
        else:
            print('[通知]', message)

    def gui_countdown(self):
        self.root = tk.Tk()
        self.root.title('OS再起動カウントダウン')
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)
        self.root.geometry(self._window_geometry())
        self.font = tkfont.Font(size=20, weight='bold')
        reason_label = tk.Label(self.root, text=f'理由: {self.reason}', font=('Arial', 12))
        reason_label.pack(pady=(10, 0))
        self.label = tk.Label(self.root, text='', font=self.font, fg='red')
        self.label.pack(pady=(10, 20))
        self.update_countdown_gui(self.seconds)
        self.root.protocol('WM_DELETE_WINDOW', self._on_close)
        self.root.mainloop()

    def update_countdown_gui(self, seconds_left):
        if seconds_left < 0 or self._stop.is_set():
            self.label.config(text='[ジョークです。実際の再起動は行われません]')
            self.root.after(3500, self.root.destroy)
            return
        self.label.config(text=f'再起動まで: 00:{seconds_left:02d}')
        self.root.after(1000, self.update_countdown_gui, seconds_left-1)

    def _window_geometry(self):
        # 画面右下に小さく表示
        w, h = 340, 110
        try:
            root = tk.Tk()
            root.withdraw()
            sw = root.winfo_screenwidth()
            sh = root.winfo_screenheight()
            root.destroy()
        except Exception:
            sw, sh = 1024, 768
        x = sw - w - 30
        y = sh - h - 60
        return f'{w}x{h}+{x}+{y}'

    def cli_countdown(self):
        print(f'[OS通知]')
        print(f'理由: {self.reason}')
        for i in range(self.seconds, -1, -1):
            print(f'再起動まで: 00:{i:02d}', end='\r', flush=True)
            time.sleep(1)
        print('\n[ジョークです。実際の再起動は行われません]')

    def start(self):
        if self.use_gui:
            self.gui_countdown()
        else:
            self.cli_countdown()

    def _on_close(self):
        self._stop.set()
        if self.root:
            self.root.destroy()


def parse_args():
    parser = argparse.ArgumentParser(description='OSフェイク再起動カウントダウン・プランク')
    parser.add_argument('--seconds', '-s', type=int, default=DEFAULT_COUNTDOWN, help='カウントダウン秒数 (デフォルト: 20)')
    parser.add_argument('--reason', '-r', type=str, default=None, help='理由テキスト (ランダム選択がデフォルト)')
    parser.add_argument('--nogui', action='store_true', help='GUIウィンドウを使わず、ターミナル表示のみ')
    parser.add_argument('--list-reasons', action='store_true', help='利用可能な理由一覧を表示')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.list_reasons:
        print('利用可能な理由一覧:')
        for r in REASONS:
            print(' -', r)
        sys.exit(0)
    reason = args.reason if args.reason else random.choice(REASONS)
    use_gui = not args.nogui and (tk is not None)
    prank = PrankCountdown(args.seconds, reason, use_gui)
    try:
        prank.start()
    except KeyboardInterrupt:
        print('\n[キャンセルされました]')
        sys.exit(1)
    except Exception as e:
        print('[エラー]', e)
        sys.exit(2)

if __name__ == '__main__':
    main()
