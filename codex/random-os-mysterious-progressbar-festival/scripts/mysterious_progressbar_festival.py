import sys
import argparse
import random
import time
import shutil
from typing import List, Tuple

# テーマ候補一覧
PROGRESSBAR_THEMES = [
    "バグ撲滅進捗",
    "コーヒー摂取量",
    "脳内会議進行度",
    "OS再起動欲求",
    "デバッグ迷子度",
    "タスク忘却度",
    "やる気残量",
    "眠気進行度",
    "ネット依存度",
    "仕様理解度",
    "リファクタ欲求",
    "進捗報告恐怖",
    "脳内BGM音量",
    "キーボード摩耗度",
    "Slack未読数増加率"
]

BAR_LENGTH = 20

ANSI_RESET = "\033[0m"
ANSI_BOLD = "\033[1m"
ANSI_COLORS = [
    "\033[92m",  # Green
    "\033[94m",  # Blue
    "\033[93m",  # Yellow
    "\033[91m",  # Red
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[90m",  # Grey
]

def random_progressbar_theme(exclude: List[str] = []) -> str:
    candidates = [t for t in PROGRESSBAR_THEMES if t not in exclude]
    return random.choice(candidates)

def random_progress_value() -> int:
    return random.randint(5, 99)

def render_progressbar(theme: str, value: int, color: str = None) -> str:
    filled_len = int(BAR_LENGTH * value / 100)
    empty_len = BAR_LENGTH - filled_len
    bar = "█" * filled_len + "─" * empty_len
    color_code = color if color else ""
    return f"[{theme:<10}] {color_code}[{bar}]{ANSI_RESET} {value:3d}%"

def generate_progressbars(n: int = 3) -> List[Tuple[str, int, str]]:
    themes = []
    bars = []
    colors = random.sample(ANSI_COLORS, k=min(n, len(ANSI_COLORS)))
    for i in range(n):
        theme = random_progressbar_theme(exclude=themes)
        value = random_progress_value()
        color = colors[i % len(colors)]
        themes.append(theme)
        bars.append((theme, value, color))
    return bars

def print_progressbars(bars: List[Tuple[str, int, str]], clear: bool = False):
    if clear:
        sys.stdout.write("\033c")  # Clear screen
    for theme, value, color in bars:
        print(render_progressbar(theme, value, color))

# CLI サブコマンド

def cmd_festival(args):
    min_bars = args.min_bars or 3
    max_bars = args.max_bars or 6
    bar_count = random.randint(min_bars, max_bars)
    bars = generate_progressbars(bar_count)
    print_progressbars(bars)


def cmd_animate(args):
    min_bars = args.min_bars or 3
    max_bars = args.max_bars or 6
    bar_count = random.randint(min_bars, max_bars)
    bars = generate_progressbars(bar_count)
    steps = args.steps or 10
    delay = args.delay or 0.4
    for step in range(steps):
        sys.stdout.write("\033[H\033[J")  # Clear screen
        animated_bars = []
        for theme, _, color in bars:
            # 進捗値をランダムに上下させる
            value = random.randint(5, 99)
            animated_bars.append((theme, value, color))
        print_progressbars(animated_bars)
        time.sleep(delay)


def cmd_list_themes(args):
    print("利用可能な進捗バーのテーマ:")
    for t in PROGRESSBAR_THEMES:
        print(f"- {t}")


def main():
    parser = argparse.ArgumentParser(description="謎のOS進捗バー祭りを発生させるCLIツール")
    subparsers = parser.add_subparsers(dest="command")

    parser_festival = subparsers.add_parser("festival", help="ランダムな進捗バー群を一度だけ表示")
    parser_festival.add_argument("--min-bars", type=int, default=3, help="表示するバーの最小数")
    parser_festival.add_argument("--max-bars", type=int, default=6, help="表示するバーの最大数")
    parser_festival.set_defaults(func=cmd_festival)

    parser_animate = subparsers.add_parser("animate", help="進捗バーをアニメーション表示")
    parser_animate.add_argument("--min-bars", type=int, default=3, help="表示するバーの最小数")
    parser_animate.add_argument("--max-bars", type=int, default=6, help="表示するバーの最大数")
    parser_animate.add_argument("--steps", type=int, default=10, help="アニメーションのステップ数")
    parser_animate.add_argument("--delay", type=float, default=0.4, help="ステップ間の遅延(秒)")
    parser_animate.set_defaults(func=cmd_animate)

    parser_list = subparsers.add_parser("list-themes", help="利用可能なテーマ一覧を表示")
    parser_list.set_defaults(func=cmd_list_themes)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
