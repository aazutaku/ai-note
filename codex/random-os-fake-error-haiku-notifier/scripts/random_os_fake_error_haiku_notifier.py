import random
import sys
import argparse
import os
import platform
import subprocess
import time
from typing import List

# 五・七・五の俳句生成用パーツ
FIVE_SYLLABLES = [
    "メモリ消ゆ",
    "404",
    "プロセス落つ",
    "ファイル消え",
    "アクセス拒否",
    "バグ踊る",
    "権限なし",
    "カーネル割れ",
    "応答なし",
    "書き込み不可",
    "デバイス消ゆ",
    "未知の闇",
    "シグナル舞う",
    "接続切れ",
    "タイムアウト"
]

SEVEN_SYLLABLES = [
    "春まだ遠き",
    "道に迷いて",
    "静けさ満ちて",
    "風の行方に",
    "月のしじまに",
    "秋の雲行く",
    "夜明けを待つ",
    "夏の幻に",
    "冬の朝焼け",
    "波の音消え",
    "霧のむこうに",
    "星の瞬き",
    "夢のさきまで",
    "砂嵐の中",
    "雪の帳に"
]

# 通知API

def notify_desktop(message: str):
    system = platform.system()
    if system == 'Linux':
        try:
            subprocess.run(['notify-send', message], check=False)
        except Exception:
            pass
    elif system == 'Darwin':
        osa_script = f'display notification "{message}" with title "OS Fake Error Haiku"'
        try:
            subprocess.run(['osascript', '-e', osa_script], check=False)
        except Exception:
            pass
    else:
        # Windowsや未対応OSは標準出力のみ
        print(message)

# 俳句生成

def generate_haiku() -> str:
    line1 = random.choice(FIVE_SYLLABLES)
    line2 = random.choice(SEVEN_SYLLABLES)
    line3 = random.choice(FIVE_SYLLABLES)
    return f"{line1}    {line2}    {line3}"

def print_haiku_terminal(haiku: str):
    print(haiku)

def notify_haiku(haiku: str, mode: str):
    if mode == 'desktop':
        notify_desktop(haiku)
    elif mode == 'both':
        notify_desktop(haiku)
        print_haiku_terminal(haiku)
    else:
        print_haiku_terminal(haiku)

# ログ監視（簡易）
def monitor_stdin(keywords: List[str], interval: float, mode: str, freq: int):
    count = 0
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            if any(kw in line.lower() for kw in keywords):
                haiku = generate_haiku()
                notify_haiku(haiku, mode)
                count += 1
                if freq > 0 and count >= freq:
                    break
            time.sleep(interval)
    except KeyboardInterrupt:
        pass

def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Error Haiku Notifier')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='1回だけ俳句を表示')
    parser_run.add_argument('--mode', choices=['terminal', 'desktop', 'both'], default='terminal', help='通知方法')

    parser_monitor = subparsers.add_parser('monitor', help='標準入力を監視し、エラーワード出現時に俳句通知')
    parser_monitor.add_argument('--mode', choices=['terminal', 'desktop', 'both'], default='terminal', help='通知方法')
    parser_monitor.add_argument('--interval', type=float, default=0.1, help='監視間隔(秒)')
    parser_monitor.add_argument('--freq', type=int, default=5, help='最大通知回数 (0で無制限)')
    parser_monitor.add_argument('--keywords', nargs='+', default=['error','fail','not found','bug','exception','crash'], help='監視キーワード')

    args = parser.parse_args()

    if args.command == 'run':
        haiku = generate_haiku()
        notify_haiku(haiku, args.mode)
    elif args.command == 'monitor':
        monitor_stdin(args.keywords, args.interval, args.mode, args.freq)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
