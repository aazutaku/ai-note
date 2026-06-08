import sys
import argparse
import random
import datetime
from typing import List, Tuple

SAMURAI_WEATHER = [
    ("快晴", "コードも冴え渡るでござる！"),
    ("雷注意報", "バグの嵐、油断召されるな！"),
    ("曇天", "集中力やや低下、無理は禁物でござる。"),
    ("大雨", "仕様変更の豪雨、覚悟召されよ！"),
    ("強風", "思考が吹き飛ぶやもしれぬ、心静かに。"),
    ("霧", "設計が霞む、慎重に進むべし。"),
    ("晴れ時々バグ", "油断大敵、細部まで目を光らすでござる。"),
    ("雪", "冷静沈着に、バグを溶かすでござる。"),
    ("台風", "タスクの渦、巻き込まれぬようご用心！"),
    ("小雨", "軽い不具合、侮るなかれ。"),
    ("虹", "良きアイデアが舞い降りるやもしれぬ。"),
    ("雷鳴轟く", "デバッグの刀、抜く時ぞ！"),
    ("夕立", "急な仕様変更、備えよ常に。"),
    ("星空", "静寂の中、集中力極まるでござる。"),
    ("暴風雨", "混沌の開発現場、己を見失うな！")
]

SAMURAI_QUOTES = [
    "今日も一刀両断、バグを斬るでござる。",
    "油断大敵、心してコードを書くべし。",
    "仕様の迷い道、道標は己の信念なり。",
    "集中力、まるで鋼の如し。",
    "無理は禁物、休息もまた戦略でござる。",
    "バグは敵にあらず、己を映す鏡なり。",
    "一歩一歩、確実に進むが勝ち。",
    "本日は静かなる開発日和。",
    "心静かに、コードの声を聞くべし。",
    "侍の如く、誇り高くコードを書くでござる。"
]

HEADER = "─── 本日の侍天気予報 ───"
FOOTER = "────────────────────"


def select_weather_and_quote() -> Tuple[str, str]:
    weather, base_comment = random.choice(SAMURAI_WEATHER)
    # 50%の確率で追加コメント
    if random.random() < 0.5:
        comment = base_comment + " " + random.choice(SAMURAI_QUOTES)
    else:
        comment = base_comment
    return weather, comment


def print_samurai_weather():
    weather, comment = select_weather_and_quote()
    print(HEADER)
    print(f"{weather}なり。{comment}")
    print(FOOTER)


def log_to_file(logfile: str, weather: str, comment: str):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, 'a', encoding='utf-8') as f:
        f.write(f"[{now}] {weather} : {comment}\n")


def list_logs(logfile: str, count: int):
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[-count:]:
                print(line.rstrip())
    except FileNotFoundError:
        print("ログファイルが見つかりません。まだ記録がありません。")


def summary_logs(logfile: str):
    from collections import Counter
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            weathers = [line.split()[2] for line in lines if len(line.split()) > 2]
            counter = Counter(weathers)
            print("=== 天気別出現回数 ===")
            for weather, cnt in counter.most_common():
                print(f"{weather}: {cnt}回")
    except FileNotFoundError:
        print("ログファイルが見つかりません。まだ記録がありません。")


def main():
    parser = argparse.ArgumentParser(description='Terminal Samurai Weathercaster')
    subparsers = parser.add_subparsers(dest='command')

    # logコマンド
    log_parser = subparsers.add_parser('log', help='侍天気を表示し、ログに記録')
    log_parser.add_argument('--logfile', type=str, default='~/.samurai_weather.log', help='ログファイルパス')

    # listコマンド
    list_parser = subparsers.add_parser('list', help='過去の侍天気ログを表示')
    list_parser.add_argument('--logfile', type=str, default='~/.samurai_weather.log', help='ログファイルパス')
    list_parser.add_argument('--count', type=int, default=10, help='表示件数')

    # summaryコマンド
    summary_parser = subparsers.add_parser('summary', help='天気別出現回数を集計')
    summary_parser.add_argument('--logfile', type=str, default='~/.samurai_weather.log', help='ログファイルパス')

    # デフォルト表示（コマンドなし）
    args = parser.parse_args()

    if args.command == 'log':
        weather, comment = select_weather_and_quote()
        print(HEADER)
        print(f"{weather}なり。{comment}")
        print(FOOTER)
        logfile = args.logfile.replace('~', os.path.expanduser('~'))
        log_to_file(logfile, weather, comment)
    elif args.command == 'list':
        logfile = args.logfile.replace('~', os.path.expanduser('~'))
        list_logs(logfile, args.count)
    elif args.command == 'summary':
        logfile = args.logfile.replace('~', os.path.expanduser('~'))
        summary_logs(logfile)
    else:
        # デフォルト動作（ターミナル起動時想定）
        print_samurai_weather()

if __name__ == '__main__':
    import os
    main()
