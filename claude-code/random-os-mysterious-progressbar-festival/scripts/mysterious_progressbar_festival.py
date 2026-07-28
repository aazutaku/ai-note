import argparse
import random
import sys
import time
from typing import List, Tuple

# 進捗バーのテーマ候補
PROGRESS_THEMES = [
    'バグ撲滅進捗',
    'コーヒー摂取量',
    '脳内会議進行度',
    'OSアップデート謎進捗',
    '集中力残量',
    'やる気ゲージ',
    'サボり検知率',
    '無意味な再起動回数',
    'AIとの親密度',
    'タスク消化率',
    '無駄話指数',
    '謎のエラー発生率',
    'ファイル保存成功率',
    'ネットワーク混乱度',
    '脳内BGM再生率',
    'コーディング幸福度',
    '会議脱出進捗',
    '進捗報告虚偽率',
    'OSメンテ祭り度',
    'CPU無駄遣い度'
]

BAR_LENGTH = 20


def random_progressbar(theme: str, percent: int) -> str:
    filled_len = int(BAR_LENGTH * percent / 100)
    bar = '█' * filled_len + '-' * (BAR_LENGTH - filled_len)
    return f"[{theme:<12}] [{bar}] {percent:>3}%"


def generate_random_bars(num_bars: int = 3) -> List[str]:
    themes = random.sample(PROGRESS_THEMES, k=num_bars)
    bars = []
    for theme in themes:
        percent = random.randint(0, 100)
        bars.append(random_progressbar(theme, percent))
    return bars


def display_festival(num_bars: int = None, interval: float = 0.5, cycles: int = 5, animate: bool = True):
    if num_bars is None:
        num_bars = random.randint(3, 6)
    for i in range(cycles):
        bars = generate_random_bars(num_bars)
        sys.stdout.write('\033[2J\033[H')  # 画面クリア&カーソル左上
        for bar in bars:
            print(bar)
        sys.stdout.flush()
        if animate and i < cycles - 1:
            time.sleep(interval)
    print()  # 最後に改行


def list_themes():
    print("利用可能な進捗バーのテーマ一覧:")
    for theme in PROGRESS_THEMES:
        print(f"- {theme}")


def summary():
    print("random-os-mysterious-progressbar-festival: ターミナルに謎の進捗バーをランダム表示するSkillです。\n")
    print(f"テーマ数: {len(PROGRESS_THEMES)}")
    print(f"バー長さ: {BAR_LENGTH}")
    print("明示呼び出し例: python mysterious_progressbar_festival.py run --bars 5 --cycles 8 --interval 0.3\n")
    print("出力例:")
    for bar in generate_random_bars(4):
        print(bar)


def parse_args():
    parser = argparse.ArgumentParser(description="謎のOS進捗バー祭りを開催するスクリプト")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="進捗バー祭りを実行")
    run_parser.add_argument("--bars", type=int, default=None, help="同時に表示するバーの数 (デフォルト: 3-6ランダム)")
    run_parser.add_argument("--cycles", type=int, default=5, help="アニメーション繰り返し回数")
    run_parser.add_argument("--interval", type=float, default=0.5, help="アニメーション間隔(秒)")
    run_parser.add_argument("--no-animate", action="store_true", help="アニメーションせず1回だけ表示")

    subparsers.add_parser("list", help="利用可能テーマ一覧表示")
    subparsers.add_parser("summary", help="Skill概要と出力例表示")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "run":
        display_festival(
            num_bars=args.bars,
            interval=args.interval,
            cycles=1 if args.no_animate else args.cycles,
            animate=not args.no_animate
        )
    elif args.command == "list":
        list_themes()
    elif args.command == "summary":
        summary()
    else:
        print("不正なコマンドです。--help を参照してください。", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
