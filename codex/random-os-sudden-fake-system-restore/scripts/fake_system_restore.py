import argparse
import random
import sys
import time
from typing import List

RESTORE_MESSAGES = [
    "謎の変更を元に戻しています...",
    "OSの気分調整中...",
    "不明なファイルを復元中...",
    "レジストリの気まぐれを修正中...",
    "システムの気分転換を実施中...",
    "意味不明なエラーを解決中...",
    "不可視ファイルを復元中...",
    "進捗バーの色を調整中...",
    "謎のプロセスを再起動中...",
    "仮想メモリのご機嫌を確認中...",
    "バックグラウンドで何かしています...",
    "システムのやる気を回復中..."
]

COMPLETE_MESSAGE = "システム復元完了（何も起きませんでした）"


def generate_progress_steps(min_steps=8, max_steps=20) -> List[int]:
    steps = random.randint(min_steps, max_steps)
    progress_points = sorted(random.sample(range(5, 100), steps - 1))
    progress_points.append(100)
    return progress_points


def pick_random_message() -> str:
    return random.choice(RESTORE_MESSAGES)


def print_restore_header():
    print("[OSシステム復元ツール]")
    print("-----------------------------")


def print_restore_footer():
    print("-----------------------------")


def simulate_restore(progress_delay=0.6, message_delay=0.3):
    print_restore_header()
    progress_steps = generate_progress_steps()
    last_progress = 0
    for progress in progress_steps:
        message = pick_random_message()
        bar = progress_bar(progress)
        sys.stdout.write(f"\r進捗: {progress:3d}% {bar} | {message}    ")
        sys.stdout.flush()
        time.sleep(random.uniform(progress_delay * 0.5, progress_delay * 1.2))
        sys.stdout.write("\n")
        time.sleep(random.uniform(message_delay * 0.5, message_delay * 1.5))
        last_progress = progress
    sys.stdout.write(f"進捗: 100% | {COMPLETE_MESSAGE}\n")
    print_restore_footer()


def progress_bar(progress: int, width: int = 24) -> str:
    filled = int(width * progress / 100)
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def handle_log(args):
    print("[LOG] フェイク復元進捗を記録します (実際には何も保存されません)")
    simulate_restore()


def handle_list(args):
    print("[LIST] 過去のフェイク復元履歴 (履歴はありません)")
    print("(このSkillは履歴保存機能を持ちません)")


def handle_summary(args):
    print("[SUMMARY] フェイク復元進捗のサマリー")
    print("全てランダム生成・記録なし・本物の復元ではありません")


def main():
    parser = argparse.ArgumentParser(
        description="謎のOSシステム復元進捗ウィンドウをフェイク表示するスクリプト"
    )
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    parser_log = subparsers.add_parser("log", help="フェイク復元進捗を表示")
    parser_log.set_defaults(func=handle_log)

    parser_list = subparsers.add_parser("list", help="履歴一覧 (機能しません)")
    parser_list.set_defaults(func=handle_list)

    parser_summary = subparsers.add_parser("summary", help="サマリー表示")
    parser_summary.set_defaults(func=handle_summary)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        # デフォルト動作: フェイク復元進捗を表示
        simulate_restore()

if __name__ == '__main__':
    main()
