import argparse
import random
import sys
import threading
import time
import platform

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    tk = None

REASONS = [
    '謎のアップデート適用中',
    'RAMの気分転換',
    'OS自己啓発モード突入',
    '未知のパッチを適用中',
    'システムの気まぐれ',
    'バーチャルメモリのストレッチ',
    'OSの自我発現準備',
    'ファイルシステムのストレス解消',
    'プロセスの自己反省タイム',
    'カーネルの深呼吸'
]

class FakeRebootCountdown:
    def __init__(self, seconds=30, reason=None, gui=True):
        self.seconds = seconds
        self.reason = reason or random.choice(REASONS)
        self.gui = gui and tk is not None
        self._stop_event = threading.Event()

    def show_gui_countdown(self):
        root = tk.Tk()
        root.title('OS通知')
        root.resizable(False, False)
        root.attributes('-topmost', True)
        root.geometry('+{}+{}'.format(root.winfo_screenwidth() - 320, 40))
        label = tk.Label(root, text='', font=('Arial', 16), padx=20, pady=10)
        label.pack()
        reason_label = tk.Label(root, text='理由: ' + self.reason, font=('Arial', 12), fg='gray')
        reason_label.pack()
        def update():
            if self.seconds >= 0:
                label.config(text=f'システム再起動まで: {self.seconds}秒')
                self.seconds -= 1
                root.after(1000, update)
            else:
                label.config(text='ジョークです')
                reason_label.config(text='')
                root.after(3000, root.destroy)
        update()
        root.mainloop()

    def show_terminal_countdown(self):
        print(f'[OS通知] システム再起動まで: {self.seconds}秒')
        print(f'理由: {self.reason}')
        for i in range(self.seconds, -1, -1):
            sys.stdout.write(f'\r残り: {i}秒 ')
            sys.stdout.flush()
            time.sleep(1)
        print('\nジョークです')

    def run(self):
        if self.gui:
            self.show_gui_countdown()
        else:
            self.show_terminal_countdown()


def main():
    parser = argparse.ArgumentParser(description='OSフェイク再起動カウントダウン・プランク')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='カウントダウンを開始')
    parser_run.add_argument('--seconds', type=int, default=30, help='カウントダウン秒数 (デフォルト30)')
    parser_run.add_argument('--reason', type=str, help='理由テキスト (省略時はランダム)')
    parser_run.add_argument('--no-gui', action='store_true', help='GUIウィンドウを使わずターミナル表示')

    parser_list = subparsers.add_parser('list-reasons', help='利用可能な理由一覧を表示')

    parser.add_argument('--version', action='version', version='os-fake-reboot-countdown-prank 1.0')

    args = parser.parse_args()

    if args.command == 'run':
        countdown = FakeRebootCountdown(
            seconds=args.seconds,
            reason=args.reason,
            gui=not args.no_gui
        )
        countdown.run()
    elif args.command == 'list-reasons':
        print('利用可能な理由一覧:')
        for i, reason in enumerate(REASONS, 1):
            print(f' {i}. {reason}')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
