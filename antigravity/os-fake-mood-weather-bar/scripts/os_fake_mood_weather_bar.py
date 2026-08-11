import sys
import argparse
import random
import time
import threading
import tkinter as tk
from tkinter import ttk

MOODS = [
    '絶好調・晴れ', 'やる気霧雨', '集中力台風接近中', 'バグの嵐', '仕様雪崩',
    '快晴', 'そよ風', '曇り時々バグ', 'やる気暴風雨', '集中力逆風',
    '仕様前線通過', 'バグ雷', 'やる気落雷', '集中力熱帯夜', '仕様みぞれ',
    'バグの小雨', 'やる気吹雪', '集中力乾燥注意報', '仕様霧', 'バグ竜巻'
]

CONCENTRATIONS = [
    '快晴', '台風接近中', '霧雨', '嵐', 'そよ風', '曇り', '暴風雨', '逆風',
    '熱帯夜', 'みぞれ', '小雨', '吹雪', '乾燥注意報', '霧', '竜巻'
]

MOTIVATIONS = [
    '絶好調', 'やる気霧雨', 'やる気暴風雨', 'やる気落雷', 'やる気吹雪', 'そよ風',
    'やる気逆風', 'やる気快晴', 'やる気曇り', 'やる気みぞれ', 'やる気小雨'
]

BUGS = [
    'なし', '嵐', 'バグの小雨', 'バグの嵐', 'バグ雷', 'バグ竜巻', 'バグみぞれ',
    'バグ吹雪', 'バグ前線', 'バグ霧', 'バグ乾燥注意報'
]

SPEC = [
    '仕様雪崩', '仕様前線通過', '仕様みぞれ', '仕様霧', '仕様快晴', '仕様嵐'
]

BAR_TITLE = 'OS風・気分天気バー'

class MoodWeatherBar(tk.Tk):
    def __init__(self, duration=10, position='top', width=400, height=80):
        super().__init__()
        self.duration = duration
        self.width = width
        self.height = height
        self.position = position
        self.overrideredirect(True)
        self.attributes('-topmost', True)
        self.resizable(False, False)
        self.configure(bg='#222222')
        self._set_position()
        self._create_widgets()
        self.after(int(self.duration * 1000), self.destroy)

    def _set_position(self):
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.width) // 2
        if self.position == 'top':
            y = 0
        elif self.position == 'bottom':
            y = screen_height - self.height
        else:
            y = 0
        self.geometry(f'{self.width}x{self.height}+{x}+{y}')

    def _create_widgets(self):
        frame = tk.Frame(self, bg='#222222')
        frame.pack(fill=tk.BOTH, expand=True)
        title = tk.Label(frame, text=BAR_TITLE, fg='#ffffff', bg='#222222', font=('Meiryo', 14, 'bold'))
        title.pack(pady=(10, 0))
        mood = random.choice(MOODS + SPEC)
        concentration = random.choice(CONCENTRATIONS)
        motivation = random.choice(MOTIVATIONS)
        bug = random.choice(BUGS)
        labels = [
            f'本日の気分: {mood}',
            f'集中力: {concentration}',
            f'やる気: {motivation}',
            f'バグ状況: {bug}'
        ]
        for text in labels:
            lbl = tk.Label(frame, text=text, fg='#e0e0e0', bg='#222222', font=('Meiryo', 12))
            lbl.pack(anchor='w', padx=24)


def show_bar(duration=10, position='top'):
    app = MoodWeatherBar(duration=duration, position=position)
    app.mainloop()


def cli_main():
    parser = argparse.ArgumentParser(description='OS風・謎の気分天気バー')
    subparsers = parser.add_subparsers(dest='command')

    show_parser = subparsers.add_parser('show', help='気分天気バーを表示')
    show_parser.add_argument('--duration', type=int, default=10, help='表示秒数 (デフォルト10秒)')
    show_parser.add_argument('--position', choices=['top', 'bottom'], default='top', help='画面端 (top/bottom)')

    list_parser = subparsers.add_parser('list', help='気分天気ワード一覧を表示')

    summary_parser = subparsers.add_parser('summary', help='ランダムな気分天気出力例')
    summary_parser.add_argument('--count', type=int, default=3, help='出力例の個数')

    args = parser.parse_args()

    if args.command == 'show':
        show_bar(duration=args.duration, position=args.position)
    elif args.command == 'list':
        print('気分天気ワード:')
        for w in set(MOODS + CONCENTRATIONS + MOTIVATIONS + BUGS + SPEC):
            print('-', w)
    elif args.command == 'summary':
        for i in range(args.count):
            print(f'[{BAR_TITLE}]')
            print(f'本日の気分: {random.choice(MOODS + SPEC)}')
            print(f'集中力: {random.choice(CONCENTRATIONS)}')
            print(f'やる気: {random.choice(MOTIVATIONS)}')
            print(f'バグ状況: {random.choice(BUGS)}')
            print()
    else:
        parser.print_help()

if __name__ == '__main__':
    cli_main()
