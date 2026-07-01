import sys
import argparse
import random
import threading
import time
import tkinter as tk
from tkinter import messagebox

FAKE_TITLES = [
    'STOP CODE: 眠気の暴走',
    'STOP CODE: コーヒーブレイク不足',
    'STOP CODE: キーボードに猫が乗りました',
    'STOP CODE: デバッグ過多エラー',
    'STOP CODE: 仕様変更検出',
    'STOP CODE: タイポ発生',
    'STOP CODE: 無限ループ警告',
    'STOP CODE: リリース恐怖症',
    'STOP CODE: 進捗ゼロ',
    'STOP CODE: ネットワーク遅延'
]

FAKE_MESSAGES = [
    'エラー: コーヒーブレイク不足',
    '原因: キーボードに猫が乗りました',
    'ヒント: 立ち上がってストレッチしましょう',
    '推奨: 5分間の休憩を取りましょう',
    'エラー: 仕様書未読',
    '警告: コードレビュー未実施',
    '原因: 眠気の暴走',
    'ヒント: 深呼吸してみましょう',
    '警告: コーヒー残量低下',
    '原因: Slack通知過多'
]

FAKE_HINTS = [
    'これは本物のエラーではありません。安心して作業を続けてください。',
    'この通知はジョークです。ご安心ください。',
    '冗談通知です。本物のブルースクリーンではありません。',
    '作業の合間に一息つきましょう。',
    '本Skillはシステムに影響を与えません。'
]


def generate_fake_bluescreen():
    title = random.choice(FAKE_TITLES)
    messages = random.sample(FAKE_MESSAGES, k=3)
    hint = random.choice(FAKE_HINTS)
    lines = ['[FAKE-OS-BLUESCREEN]', title]
    lines.extend(messages)
    lines.append('---')
    lines.append(hint)
    return '\n'.join(lines)


def show_bluescreen_gui(message, duration=8):
    def on_close():
        root.destroy()

    root = tk.Tk()
    root.title('FAKE-OS-BLUESCREEN')
    root.configure(bg='#1E2B4F')
    root.geometry('600x340')
    root.resizable(False, False)
    # Remove window decorations
    root.overrideredirect(True)
    # Center window
    x = (root.winfo_screenwidth() // 2) - 300
    y = (root.winfo_screenheight() // 2) - 170
    root.geometry(f'+{x}+{y}')

    frame = tk.Frame(root, bg='#1E2B4F')
    frame.pack(expand=True, fill='both')

    label = tk.Label(
        frame,
        text=message,
        font=('Consolas', 14),
        fg='#E3E3E3',
        bg='#1E2B4F',
        justify='left',
        anchor='w'
    )
    label.pack(padx=24, pady=32, anchor='w')

    # Add a fake error icon
    icon = tk.Label(
        frame,
        text=':(',
        font=('Arial', 48, 'bold'),
        fg='#3FA9F5',
        bg='#1E2B4F'
    )
    icon.place(x=24, y=16)

    # Add close button
    close_btn = tk.Button(
        frame,
        text='閉じる',
        command=on_close,
        font=('Arial', 12),
        bg='#3FA9F5',
        fg='white',
        relief='flat',
        activebackground='#2167A9',
        activeforeground='white'
    )
    close_btn.place(x=500, y=280, width=70, height=32)

    # Auto-close after duration seconds
    root.after(duration * 1000, on_close)
    root.mainloop()


def print_bluescreen_terminal(message):
    print('\n' + message + '\n')


def handle_notify(args):
    message = generate_fake_bluescreen()
    if args.gui:
        try:
            show_bluescreen_gui(message)
        except Exception as e:
            print('GUI表示に失敗しました:', e)
            print_bluescreen_terminal(message)
    else:
        print_bluescreen_terminal(message)


def handle_sample(args):
    for _ in range(args.count):
        message = generate_fake_bluescreen()
        print_bluescreen_terminal(message)
        print('-' * 60)


def main():
    parser = argparse.ArgumentParser(
        description='random-os-fake-bluescreen-notifier: ネタ系ブルースクリーン風通知を表示します。'
    )
    subparsers = parser.add_subparsers(dest='command', help='サブコマンド')

    notify_parser = subparsers.add_parser('notify', help='ブルースクリーン風通知を表示')
    notify_parser.add_argument('--gui', action='store_true', help='GUIで表示 (Tkinter)')
    notify_parser.set_defaults(func=handle_notify)

    sample_parser = subparsers.add_parser('sample', help='ランダムメッセージを複数生成し標準出力')
    sample_parser.add_argument('--count', type=int, default=3, help='生成数 (デフォルト: 3)')
    sample_parser.set_defaults(func=handle_sample)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
