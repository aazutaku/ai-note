import sys
import argparse
import random
import os
import platform
import time
from typing import List

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

EXCUSES = [
    "今バグが出たのは水星逆行のせいです。",
    "コードが今日は恥ずかしがっているようです。",
    "太陽フレアが強すぎて動作が不安定です。",
    "量子もつれの影響で一時的に停止しました。",
    "今日はOSの気分が乗らないみたいです。",
    "近所のWi-Fiが共鳴してエラーが発生しました。",
    "サーバーが月齢を気にしています。",
    "バグは宇宙線のせいかもしれません。",
    "システムが週末モードに入っています。",
    "AIが今日は休暇を取っています。",
    "OSがコーヒーブレイク中です。",
    "コードが自己主張を始めました。",
    "CPUが星占いに夢中です。",
    "今日はキーボードが反抗期です。",
    "電磁波が強すぎます。",
    "メモリが懐古主義に走っています。",
    "ネットワークが人見知りしています。",
    "天気が良すぎて動きたくないようです。",
    "OSが哲学的な悩みに陥っています。",
    "今日のバグはブラックホールのせいです。"
]

LOG_FILE = os.path.expanduser("~/.random_os_excuse_generator.log")


def notify_excuse(excuse: str):
    if PLYER_AVAILABLE:
        notification.notify(
            title="OS Excuse",
            message=excuse,
            app_name="random-os-excuse-generator",
            timeout=5
        )
    else:
        print(f"[OS Excuse] {excuse}")


def log_excuse(excuse: str):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{timestamp}\t{excuse}\n")


def list_excuses(count: int = 10):
    if not os.path.exists(LOG_FILE):
        print("No excuse log found.")
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[-count:]:
            print(line.strip())


def summary():
    if not os.path.exists(LOG_FILE):
        print("No excuse log found.")
        return
    count = 0
    freq = {}
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            count += 1
            excuse = line.strip().split('\t')[-1]
            freq[excuse] = freq.get(excuse, 0) + 1
    print(f"Total excuses generated: {count}")
    print("Top excuses:")
    for excuse, n in sorted(freq.items(), key=lambda x: -x[1])[:5]:
        print(f"  {excuse} ({n} times)")


def generate_excuse() -> str:
    return random.choice(EXCUSES)


def main():
    parser = argparse.ArgumentParser(description="Random OS Excuse Generator - ユーモラスな言い訳をランダムで表示")
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_log = subparsers.add_parser('log', help='新しい言い訳を生成し通知＆ログ')
    parser_log.add_argument('--count', type=int, default=1, help='生成する言い訳の数')

    parser_list = subparsers.add_parser('list', help='過去の言い訳ログを表示')
    parser_list.add_argument('--count', type=int, default=10, help='表示する最新ログ数')

    parser_summary = subparsers.add_parser('summary', help='言い訳生成の集計')

    args = parser.parse_args()

    if args.command == 'log':
        for _ in range(args.count):
            excuse = generate_excuse()
            notify_excuse(excuse)
            log_excuse(excuse)
    elif args.command == 'list':
        list_excuses(args.count)
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
