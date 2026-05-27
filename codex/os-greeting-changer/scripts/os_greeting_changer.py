import argparse
import random
import sys
from datetime import datetime

FAKE_OS_MESSAGES = [
    "[Windows 99 Professional Edition 起動中...]",
    "[Macintosh SE/30が時空を超えて復活しました]",
    "[Linux 12.04: コーヒータイム中、しばらくお待ち下さい]",
    "[BeOS Hyper Edition: メモリ空間を再構築しています]",
    "[NEC PC-9801 Universe 起動... 未来OSモード]",
    "[Amiga Galaxy OS: フロッピーを宇宙からダウンロード中]",
    "[Atari ST++: MIDIシーケンサーを自己進化中]",
    "[Sun Solaris 11.99: 太陽フレア検出...再起動します]",
    "[OS/3 Warp: ワープゲート初期化中]",
    "[PalmOS Infinity: タッチペンを検出しました]",
    "[MS-DOS 13.1: 仮想メモリが無限大です]",
    "[Commodore 128 Ultra: BASICインタープリタをAI化中]",
    "[Haiku OS: 五七五で起動します]",
    "[Plan 9 from Bell Labs: プラネット9へログイン中]",
    "[QNX Quantum Edition: カーネルが量子化されました]",
    "[Solaris 42.0: 太陽系ネットワークに接続中]",
    "[ReactOS 5.0: 互換性が宇宙レベルに拡張されました]",
    "[TempleOS 3.1: 神託を受信中]",
    "[IRIX 9.9: グラフィック次元を展開しています]",
    "[NextStep 6.0: タイムマシン起動準備完了]"
]

HISTORY = []


def print_random_greeting():
    message = random.choice(FAKE_OS_MESSAGES)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    HISTORY.append((timestamp, message))
    print(message)
    return message


def list_greetings():
    print("=== os-greeting-changer: メッセージ一覧 ===")
    for idx, msg in enumerate(FAKE_OS_MESSAGES, 1):
        print(f"{idx}. {msg}")


def show_history():
    if not HISTORY:
        print("履歴はありません。直近のセッションでのみ有効です。")
        return
    print("=== os-greeting-changer: このセッションの履歴 ===")
    for t, m in HISTORY:
        print(f"{t}: {m}")


def summary():
    print(f"本Skillには{len(FAKE_OS_MESSAGES)}種類の偽OS起動メッセージが登録されています。\n")
    print("例:")
    for msg in random.sample(FAKE_OS_MESSAGES, 3):
        print(f"- {msg}")
    print("\nファイルやシステムには一切影響を与えません。安全にご利用いただけます。")


def main():
    parser = argparse.ArgumentParser(
        description="ターミナル起動時に偽OSメッセージをランダム表示する遊び心Skill"
    )
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser("log", help="偽OSメッセージを1つランダム表示（デフォルト動作）")
    parser_list = subparsers.add_parser("list", help="登録済みの全メッセージ一覧を表示")
    parser_history = subparsers.add_parser("history", help="このセッションで表示した履歴を表示")
    parser_summary = subparsers.add_parser("summary", help="Skillの概要とサンプルを表示")

    args = parser.parse_args()

    if args.command is None or args.command == "log":
        print_random_greeting()
    elif args.command == "list":
        list_greetings()
    elif args.command == "history":
        show_history()
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
