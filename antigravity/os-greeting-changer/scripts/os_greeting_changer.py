import sys
import random
import argparse
from datetime import datetime

# 偽OSメッセージ一覧
FAKE_OS_MESSAGES = [
    "[OS Boot] Windows 99 Ultimate Edition 起動中…",
    "[OS Boot] Macintosh SE/30が時空を超えて復活しました。",
    "[OS Boot] Linux 9.99 Coffee Break中。しばらくお待ちください。",
    "[OS Boot] BeOS Hyper Edition: 仮想次元からの帰還。",
    "[OS Boot] Solaris Nebula 起動準備中…",
    "[OS Boot] MS-DOS 10.0が異世界でロードされています。",
    "[OS Boot] Amiga 5000X 幻想モードで起動します。",
    "[OS Boot] OS/2 Warp Infinity Edition 準備完了。",
    "[OS Boot] CP/M 2025 Quantum Edition ロード中…",
    "[OS Boot] Red Star OS 8.8.8 起動中…",
    "[OS Boot] Plan 9 from Bell Labs: 次元転送開始。",
    "[OS Boot] QNX Hypervisor: 仮想宇宙を展開中。",
    "[OS Boot] TempleOS Resurrection 起動します。",
    "[OS Boot] Android 42.0 Nebula Edition 起動準備中。",
    "[OS Boot] iOS 20.2.1 Retro Modeで起動しています。",
    "[OS Boot] FreeBSD 13.37 Unicorn Edition 起動中。",
    "[OS Boot] NetWare 2023起動しています。",
    "[OS Boot] Xenix 3000: タイムトラベルモード起動。",
    "[OS Boot] Haiku OS 5.0が幻想空間でロード中。",
    "[OS Boot] MINIX 10.0: 教育用宇宙OS起動。"
]

LOG_FILE = None  # ログファイルは使わない設計


def print_random_os_message():
    msg = random.choice(FAKE_OS_MESSAGES)
    print(msg)
    return msg

def list_all_messages():
    for idx, msg in enumerate(FAKE_OS_MESSAGES, 1):
        print(f"{idx:2d}: {msg}")

def summary():
    print(f"登録されている偽OSメッセージ数: {len(FAKE_OS_MESSAGES)}")
    print("一例: ")
    for msg in random.sample(FAKE_OS_MESSAGES, min(3, len(FAKE_OS_MESSAGES))):
        print(f"  - {msg}")

def search_messages(keyword):
    found = [msg for msg in FAKE_OS_MESSAGES if keyword.lower() in msg.lower()]
    if not found:
        print(f"キーワード '{keyword}' を含む偽OSメッセージは見つかりませんでした。")
    else:
        for msg in found:
            print(msg)

def main():
    parser = argparse.ArgumentParser(description="ターミナル起動時に偽OS起動メッセージを表示するスクリプト")
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='ランダムな偽OS起動メッセージを表示 (デフォルト)')
    parser_list = subparsers.add_parser('list', help='全ての偽OS起動メッセージを一覧表示')
    parser_summary = subparsers.add_parser('summary', help='登録されているメッセージの概要を表示')
    parser_search = subparsers.add_parser('search', help='キーワードで偽OSメッセージを検索')
    parser_search.add_argument('keyword', type=str, help='検索キーワード')

    # 引数なしの場合はlog動作
    if len(sys.argv) == 1:
        print_random_os_message()
        sys.exit(0)

    args = parser.parse_args()

    if args.command == 'log':
        print_random_os_message()
    elif args.command == 'list':
        list_all_messages()
    elif args.command == 'summary':
        summary()
    elif args.command == 'search':
        search_messages(args.keyword)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
