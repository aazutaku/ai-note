import sys
import time
import random
import argparse
import threading
from shutil import get_terminal_size

PROGRESS_THEMES = [
    "バグ撲滅進捗",
    "コーヒー摂取量",
    "脳内会議進行度",
    "謎のOS再起動率",
    "タスク消滅確率",
    "仕様理解度",
    "デバッグ迷宮度",
    "やる気残量",
    "CPU空想率",
    "Slack未読消化率",
    "コミット祭り進行度",
    "会議無駄度",
    "メモリ妄想量",
    "進捗詐称率"
]

BAR_LENGTH = 20
DISPLAY_TIME = 10  # 秒

class MysteriousProgressBar:
    def __init__(self, theme, value):
        self.theme = theme
        self.value = value  # 0-100

    def render(self):
        filled = int(self.value / 100 * BAR_LENGTH)
        bar = '█' * filled + '-' * (BAR_LENGTH - filled)
        return f"[{self.theme.ljust(10)}] [{bar}] {str(self.value).rjust(3)}%"


def random_progress_bars(n=None):
    themes = random.sample(PROGRESS_THEMES, k=n or random.randint(3, 7))
    bars = []
    for t in themes:
        value = random.randint(10, 99)
        bars.append(MysteriousProgressBar(t, value))
    return bars


def print_bars(bars):
    # 端末幅に合わせて整形
    width = get_terminal_size((80, 20)).columns
    for bar in bars:
        line = bar.render()
        if len(line) > width:
            line = line[:width-1]
        print(line)


def clear_lines(num):
    # ANSIエスケープで上書き消去
    for _ in range(num):
        sys.stdout.write('\033[F')  # カーソルを上へ
        sys.stdout.write('\033[K')  # 行消去
    sys.stdout.flush()


def festival_once(n=None, sleep_time=DISPLAY_TIME):
    bars = random_progress_bars(n)
    print_bars(bars)
    sys.stdout.flush()
    time.sleep(sleep_time)
    clear_lines(len(bars))


def festival_loop(interval=60, duration=600):
    # duration秒間、intervalごとに発動
    start = time.time()
    while time.time() - start < duration:
        n = random.randint(3, 7)
        festival_once(n, sleep_time=DISPLAY_TIME)
        time.sleep(interval - DISPLAY_TIME)


def cli():
    parser = argparse.ArgumentParser(description="謎のOS進捗バー祭りスクリプト")
    subparsers = parser.add_subparsers(dest='command')

    p_once = subparsers.add_parser('once', help='1回だけ進捗バーを表示')
    p_once.add_argument('-n', '--num', type=int, help='表示するバーの数')
    p_once.add_argument('-t', '--time', type=int, default=DISPLAY_TIME, help='表示秒数')

    p_loop = subparsers.add_parser('festival', help='一定間隔で進捗バー祭り')
    p_loop.add_argument('-i', '--interval', type=int, default=60, help='祭り間隔(秒)')
    p_loop.add_argument('-d', '--duration', type=int, default=600, help='全体の持続時間(秒)')

    args = parser.parse_args()
    if args.command == 'once':
        festival_once(n=args.num, sleep_time=args.time)
    elif args.command == 'festival':
        festival_loop(interval=args.interval, duration=args.duration)
    else:
        parser.print_help()

if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        print("\n[進捗バー祭り] 中断されました")
