import sys
import time
import random
import argparse
import threading
from typing import List

RESTORE_MESSAGES = [
    "謎の変更を元に戻しています...",
    "OSの気分調整中...",
    "予期せぬファイルを復元中...",
    "システムのやる気を回復中...",
    "無意味なキャッシュを削除中...",
    "復元ポイントを探索中...",
    "謎のプロセスを巻き戻し中...",
    "一時ファイルを整理しています...",
    "ユーザーの混乱度を調整中...",
    "OSの記憶をリフレッシュ中..."
]

COMPLETE_MESSAGE = "復元が完了しました（何も変わりません）"

class FakeRestoreProgress:
    def __init__(self, min_steps=5, max_steps=12, min_delay=0.5, max_delay=2.0):
        self.min_steps = min_steps
        self.max_steps = max_steps
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.progress_points = self._generate_progress_points()
        self.messages = self._generate_messages()
        self._stop_event = threading.Event()

    def _generate_progress_points(self) -> List[int]:
        steps = random.randint(self.min_steps, self.max_steps)
        points = sorted(random.sample(range(5, 100), steps - 1)) + [100]
        return points

    def _generate_messages(self) -> List[str]:
        return random.choices(RESTORE_MESSAGES, k=len(self.progress_points))

    def run(self):
        print("[OS System Restore]")
        for idx, (percent, msg) in enumerate(zip(self.progress_points, self.messages)):
            if self._stop_event.is_set():
                break
            sys.stdout.write(f"進捗: {percent}% | 状態: {msg}\n")
            sys.stdout.flush()
            # 最後は短め
            if percent == 100:
                time.sleep(0.8)
            else:
                time.sleep(random.uniform(self.min_delay, self.max_delay))
        print(f"進捗: 100% | 状態: {COMPLETE_MESSAGE}")

    def stop(self):
        self._stop_event.set()


def list_messages():
    print("利用可能なフェイク復元メッセージ:")
    for msg in RESTORE_MESSAGES:
        print(f"- {msg}")

def summary():
    print("Fake System Restore Skill 概要:")
    print("- 完全ランダムな進捗バーとメッセージを生成")
    print("- システムやファイルには一切影響なし")
    print("- CLIサブコマンド: run, list, summary")


def main():
    parser = argparse.ArgumentParser(description="謎のOSシステム復元フェイク進捗バーを表示します。")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_run = subparsers.add_parser("run", help="フェイク復元進捗バーを開始")
    parser_run.add_argument("--min-steps", type=int, default=5, help="進捗ステップの最小数")
    parser_run.add_argument("--max-steps", type=int, default=12, help="進捗ステップの最大数")
    parser_run.add_argument("--min-delay", type=float, default=0.5, help="各ステップ間の最小遅延(秒)")
    parser_run.add_argument("--max-delay", type=float, default=2.0, help="各ステップ間の最大遅延(秒)")

    parser_list = subparsers.add_parser("list", help="利用可能なフェイクメッセージ一覧")
    parser_summary = subparsers.add_parser("summary", help="Skill概要を表示")

    args = parser.parse_args()

    try:
        if args.command == "run":
            frp = FakeRestoreProgress(
                min_steps=args.min_steps,
                max_steps=args.max_steps,
                min_delay=args.min_delay,
                max_delay=args.max_delay
            )
            frp.run()
        elif args.command == "list":
            list_messages()
        elif args.command == "summary":
            summary()
        else:
            parser.print_help()
    except KeyboardInterrupt:
        print("\n[中断されました]")
    except Exception as e:
        print(f"[エラー]: {e}")

if __name__ == '__main__':
    main()
