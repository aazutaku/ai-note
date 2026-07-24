import sys
import argparse
import random
import time
import os
from typing import List, Dict

HYPEBAR_PARAMS = [
    "やればできる度",
    "バグ耐性ゲージ",
    "今日のやる気残量",
    "カオス指数",
    "進捗予測不能度",
    "謎パワー充填率",
    "OS愛着度",
    "自己肯定感ブースト",
    "無敵モード発動率",
    "デバッグ運勢"
]


def random_param_set() -> List[Dict[str, str]]:
    num_params = random.randint(3, 6)
    selected = random.sample(HYPEBAR_PARAMS, num_params)
    result = []
    for name in selected:
        if "度" in name or "率" in name or "指数" in name or "ゲージ" in name or "残量" in name or "発動率" in name:
            value = f"{random.randint(0, 100)}%"
        elif "運勢" in name:
            value = random.choice(["大吉", "中吉", "小吉", "凶", "超吉", "謎"])
        else:
            value = str(random.randint(0, 9999))
        result.append({"name": name, "value": value})
    return result


def print_hypebar():
    print("[OS自己肯定感ハイプバー]")
    for param in random_param_set():
        print(f"{param['name']}: {param['value']}")


def log_hypebar(logfile: str):
    params = random_param_set()
    with open(logfile, 'a', encoding='utf-8') as f:
        f.write(f"[OS自己肯定感ハイプバー] {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        for param in params:
            f.write(f"{param['name']}: {param['value']}\n")
        f.write("\n")


def list_history(logfile: str, count: int):
    if not os.path.exists(logfile):
        print("履歴ファイルがありません。")
        return
    with open(logfile, encoding='utf-8') as f:
        lines = f.readlines()
    blocks = []
    block = []
    for line in lines:
        if line.startswith('[OS自己肯定感ハイプバー]') and block:
            blocks.append(block)
            block = [line]
        else:
            block.append(line)
    if block:
        blocks.append(block)
    for b in blocks[-count:]:
        print(''.join(b))


def summary_stats(logfile: str):
    if not os.path.exists(logfile):
        print("履歴ファイルがありません。")
        return
    param_counts = {}
    with open(logfile, encoding='utf-8') as f:
        for line in f:
            for name in HYPEBAR_PARAMS:
                if line.startswith(name):
                    param_counts[name] = param_counts.get(name, 0) + 1
    print("パラメータ出現回数:")
    for name, count in sorted(param_counts.items(), key=lambda x: -x[1]):
        print(f"{name}: {count}回")


def main():
    parser = argparse.ArgumentParser(description='OS自己肯定感ハイプバー')
    subparsers = parser.add_subparsers(dest='command')

    parser_show = subparsers.add_parser('show', help='ハイプバーを表示')

    parser_log = subparsers.add_parser('log', help='ハイプバーを履歴に記録')
    parser_log.add_argument('--file', default='hypebar.log', help='履歴ファイル')

    parser_list = subparsers.add_parser('list', help='履歴を表示')
    parser_list.add_argument('--file', default='hypebar.log', help='履歴ファイル')
    parser_list.add_argument('--count', type=int, default=5, help='表示件数')

    parser_summary = subparsers.add_parser('summary', help='パラメータ出現回数を集計')
    parser_summary.add_argument('--file', default='hypebar.log', help='履歴ファイル')

    args = parser.parse_args()

    if args.command == 'show' or args.command is None:
        print_hypebar()
    elif args.command == 'log':
        log_hypebar(args.file)
        print("ハイプバーを記録しました。")
    elif args.command == 'list':
        list_history(args.file, args.count)
    elif args.command == 'summary':
        summary_stats(args.file)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
