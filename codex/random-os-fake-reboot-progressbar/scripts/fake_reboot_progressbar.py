import sys
import time
import random
import argparse
from typing import List

PROGRESS_MESSAGES = [
    "再起動準備中…",
    "謎のプロセス終了中…",
    "システムキャッシュを解放中…",
    "仮想デバイスを初期化中…",
    "レジストリを最適化中…",
    "メモリリークを検知中…",
    "仮想カーネルを再構成中…",
    "OSカーネルをシャッフル中…",
    "不要なバイナリを圧縮中…",
    "未知のエラーを解析中…",
    "セキュリティホールを拡張中…",
    "リセットトークンを生成中…",
    "謎のデータを消去中…",
    "非現実プロセスを終了中…",
    "仮想ファームウェアを更新中…",
    "全ての設定を忘却中…",
    "OSの記憶を初期化中…",
    "システム時間を巻き戻し中…"
]

FINAL_MESSAGES = [
    "あと3分で全てがリセットされます",
    "もうすぐ再起動が完了します",
    "最終プロセスを終了中…",
    "全ての作業が無に帰します",
    "あと少しで現実がリセットされます"
]

COMPLETE_MESSAGE = "[====================] 100% 完了！実際には何も起きませんでした。"

BAR_LENGTH = 20


def random_progress_steps(num_steps: int) -> List[int]:
    steps = sorted(random.sample(range(5, 100), num_steps - 1)) + [100]
    return steps


def random_progress_messages(num_steps: int) -> List[str]:
    messages = random.sample(PROGRESS_MESSAGES, k=min(num_steps-1, len(PROGRESS_MESSAGES)))
    if num_steps - 1 > len(PROGRESS_MESSAGES):
        messages += random.choices(PROGRESS_MESSAGES, k=num_steps-1-len(PROGRESS_MESSAGES))
    final_msg = random.choice(FINAL_MESSAGES)
    return messages[:num_steps-1] + [final_msg]


def print_progress_bar(percent: int, message: str):
    filled_len = int(BAR_LENGTH * percent // 100)
    bar = '[' + '=' * filled_len + '>' + ' ' * (BAR_LENGTH - filled_len - 1) + ']'
    sys.stdout.write(f"\r{bar} {percent}% {message}")
    sys.stdout.flush()


def run_progressbar(duration: float = 8.0, steps: int = 6, quiet: bool = False):
    progress_points = random_progress_steps(steps)
    messages = random_progress_messages(steps)
    prev_percent = 0
    for i, percent in enumerate(progress_points):
        msg = messages[i]
        # 時間配分
        sleep_time = duration / steps
        if not quiet:
            print_progress_bar(percent, msg)
        time.sleep(sleep_time)
        prev_percent = percent
    if not quiet:
        sys.stdout.write("\n" + COMPLETE_MESSAGE + "\n")
        sys.stdout.flush()


def cli():
    parser = argparse.ArgumentParser(
        description="謎のOS再起動進捗バーをランダムに表示するスクリプト (冗談用)"
    )
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    run_parser = subparsers.add_parser("run", help="進捗バーを表示")
    run_parser.add_argument("--duration", type=float, default=8.0, help="進捗バー全体の表示秒数 (デフォルト8秒)")
    run_parser.add_argument("--steps", type=int, default=6, help="進捗ステップ数 (デフォルト6)")
    run_parser.add_argument("--quiet", action="store_true", help="出力を抑制 (テスト用)")

    list_parser = subparsers.add_parser("list-messages", help="使用可能な進捗メッセージ一覧を表示")

    args = parser.parse_args()
    if args.command == "run":
        try:
            run_progressbar(duration=args.duration, steps=args.steps, quiet=args.quiet)
        except KeyboardInterrupt:
            sys.stdout.write("\n進捗バーが中断されました。\n")
            sys.stdout.flush()
    elif args.command == "list-messages":
        print("進捗メッセージ一覧:")
        for msg in PROGRESS_MESSAGES:
            print(f"- {msg}")
        print("\n最終メッセージ例:")
        for msg in FINAL_MESSAGES:
            print(f"- {msg}")
    else:
        parser.print_help()


def main():
    cli()

if __name__ == '__main__':
    main()
