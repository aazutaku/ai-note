import sys
import time
import random
import argparse
import threading
try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print('tkinter is required to run this script.')
    sys.exit(1)

REASONS = [
    '謎のアップデート適用中',
    'RAMの気分転換',
    'OS自己啓発モード突入',
    'アセンブリ魂の再燃',
    'レジストリの深呼吸',
    'カーネルの瞑想タイム',
    'デバイスドライバの自己診断',
    'ファイルシステムの散歩',
    'プロセス管理者の休憩',
    'バイナリのヨガセッション'
]

class FakeRebootWindow:
    def __init__(self, seconds, reason):
        self.seconds = seconds
        self.reason = reason
        self.root = tk.Tk()
        self.root.title('OS 再起動カウントダウン')
        self.root.geometry('380x180+200+200')
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.disable_event)
        self.label_title = tk.Label(self.root, text='OS再起動まで:', font=('Arial', 16))
        self.label_title.pack(pady=10)
        self.label_count = tk.Label(self.root, text=f'{self.seconds} 秒', font=('Arial', 28, 'bold'), fg='red')
        self.label_count.pack(pady=5)
        self.label_reason = tk.Label(self.root, text=f'理由: {self.reason}', font=('Arial', 12))
        self.label_reason.pack(pady=10)
        self.joke_label = None
        self.running = True

    def disable_event(self):
        pass  # 閉じるボタン無効化

    def countdown(self):
        for i in range(self.seconds, 0, -1):
            if not self.running:
                break
            self.label_count.config(text=f'{i} 秒')
            self.root.update()
            time.sleep(1)
        self.show_joke()

    def show_joke(self):
        self.label_count.config(text='0 秒')
        self.label_reason.config(text='')
        self.joke_label = tk.Label(self.root, text='ジョークです。', font=('Arial', 18, 'bold'), fg='blue')
        self.joke_label.pack(pady=30)
        self.root.update()
        # 3秒後に自動で閉じる
        self.root.after(3000, self.root.quit)

    def run(self):
        t = threading.Thread(target=self.countdown)
        t.start()
        self.root.mainloop()
        self.running = False


def list_reasons():
    print('利用可能なフェイク再起動理由:')
    for idx, reason in enumerate(REASONS, 1):
        print(f'{idx}. {reason}')


def main():
    parser = argparse.ArgumentParser(description='OSフェイク再起動カウントダウン・ジョークツール')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='カウントダウンウィンドウを表示')
    parser_run.add_argument('-s', '--seconds', type=int, default=30, help='カウントダウン秒数 (デフォルト: 30)')
    parser_run.add_argument('-r', '--reason', type=str, default=None, help='理由テキスト (省略時はランダム)')

    parser_list = subparsers.add_parser('list', help='理由リストを表示')

    args = parser.parse_args()

    if args.command == 'run':
        seconds = args.seconds if args.seconds > 0 else 30
        reason = args.reason if args.reason else random.choice(REASONS)
        try:
            win = FakeRebootWindow(seconds, reason)
            win.run()
        except Exception as e:
            print(f'エラー: {e}')
            sys.exit(1)
    elif args.command == 'list':
        list_reasons()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
