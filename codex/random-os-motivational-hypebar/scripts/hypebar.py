import sys
import argparse
import random
import shutil
import time

# ランダムなパラメータ名候補
PARAMETER_NAMES = [
    "やればできる度",
    "バグ耐性ゲージ",
    "今日のやる気残量",
    "謎のOSエナジー",
    "運命バフ率",
    "無敵感メーター",
    "バグ吸収率",
    "カオス安定度",
    "自己肯定感レベル",
    "やり切りパワー",
    "OSとの親和性",
    "謎の進捗ポイント",
    "エディタ愛着度",
    "今日の集中残量",
    "バグ回避運",
    "再起動欲",
    "クリティカル期待値",
    "意味不明エネルギー"
]

BAR_CHAR = '■'
EMPTY_CHAR = ' '


def random_parameters(num=4):
    """ランダムなパラメータ名と値を返す"""
    names = random.sample(PARAMETER_NAMES, k=num)
    params = []
    for name in names:
        value = random.randint(0, 100)
        params.append((name, value))
    return params


def render_bar(label, value, width=48):
    """ラベルと値から進捗バーを生成"""
    filled = int(width * value / 100)
    empty = width - filled
    bar = BAR_CHAR * filled + EMPTY_CHAR * empty
    return f"[ {label} ] {str(value).rjust(3)}%  |{bar}|"


def print_hypebar(num_params=4, bar_width=48, delay=0.08):
    params = random_parameters(num_params)
    for label, value in params:
        bar_line = render_bar(label, value, bar_width)
        print(bar_line)
        time.sleep(delay)


def cli():
    parser = argparse.ArgumentParser(
        description="謎の自己肯定感ハイプバーを表示します。全く意味はありません。"
    )
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    show_parser = subparsers.add_parser("show", help="ハイプバーを表示")
    show_parser.add_argument("-n", "--num", type=int, default=4, help="表示するパラメータ数")
    show_parser.add_argument("-w", "--width", type=int, default=48, help="バーの幅(文字数)")

    list_parser = subparsers.add_parser("list", help="パラメータ名一覧を表示")

    summary_parser = subparsers.add_parser("summary", help="今日の自己肯定感サマリー(ランダム)")

    args = parser.parse_args()

    if args.command == "show":
        print_hypebar(num_params=args.num, bar_width=args.width)
    elif args.command == "list":
        print("-- パラメータ名候補 --")
        for name in PARAMETER_NAMES:
            print(f"- {name}")
    elif args.command == "summary":
        print("== 今日の自己肯定感サマリー ==")
        print_hypebar(num_params=6, bar_width=40, delay=0.04)
        print("(※このサマリーは完全にランダムです)")
    else:
        parser.print_help()


if __name__ == '__main__':
    cli()
