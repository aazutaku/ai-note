import sys
import random
import argparse
import datetime
import os
import json
from typing import List, Optional

PROPHECY_MESSAGES = [
    "エラー: 明日あなたは3回pushに失敗します",
    "警告: 来週GitHubが逆行します",
    "注意: コードレビューで哲学的質問を受けます",
    "エラー: 2日後、npm installが永遠に終わりません",
    "警告: あなたのCIは満月の夜にだけ動作します",
    "注意: 近日、VSCodeが詩的なメッセージを表示します",
    "エラー: 未来のあなたはlsコマンドで迷子になります",
    "警告: 3日後、make buildが宇宙的エラーを返します",
    "注意: あなたのpull requestは時空の狭間に消えます",
    "エラー: 週末、あなたのIDEが哲学的沈黙に陥ります",
    "警告: 近日、シンタックスエラーが詩的に現れます",
    "注意: 未来のあなたはREADMEを書き直す運命です"
]

LOG_FILE = os.path.expanduser("~/.random_os_fake_error_prophecy.log")

class ProphecyLogger:
    def __init__(self, log_file: str = LOG_FILE):
        self.log_file = log_file

    def log(self, message: str):
        now = datetime.datetime.now().isoformat()
        entry = {"timestamp": now, "message": message}
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"[ProphecyLogger] ログ書き込み失敗: {e}", file=sys.stderr)

    def list(self, limit: Optional[int] = None) -> List[dict]:
        results = []
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        entry = json.loads(line.strip())
                        results.append(entry)
                    except Exception:
                        continue
        except FileNotFoundError:
            return []
        if limit:
            return results[-limit:]
        return results

    def summary(self):
        entries = self.list()
        counts = {}
        for entry in entries:
            msg = entry["message"]
            prefix = msg.split(":")[0]
            counts[prefix] = counts.get(prefix, 0) + 1
        return counts


def random_prophecy() -> str:
    return random.choice(PROPHECY_MESSAGES)


def print_prophecy(message: str, color: bool = True):
    # ANSI color codes for error/warning/notice
    if color:
        if message.startswith("エラー"):
            print(f"\033[91m{message}\033[0m")  # Red
        elif message.startswith("警告"):
            print(f"\033[93m{message}\033[0m")  # Yellow
        elif message.startswith("注意"):
            print(f"\033[94m{message}\033[0m")  # Blue
        else:
            print(message)
    else:
        print(message)


def main():
    parser = argparse.ArgumentParser(
        description="未来予言風の偽OSエラーメッセージをランダム表示するスクリプト"
    )
    subparsers = parser.add_subparsers(dest="command", required=False)

    # prophecyコマンド
    parser_prophecy = subparsers.add_parser("prophecy", help="今すぐ予言エラーを表示")
    parser_prophecy.add_argument("--no-log", action="store_true", help="ログに記録しない")
    parser_prophecy.add_argument("--no-color", action="store_true", help="色付けしない")

    # logコマンド
    parser_log = subparsers.add_parser("log", help="過去の予言エラーを表示")
    parser_log.add_argument("--limit", type=int, default=10, help="最新N件のみ表示")

    # summaryコマンド
    parser_summary = subparsers.add_parser("summary", help="予言エラーの統計を表示")

    # デフォルト: prophecy
    args = parser.parse_args()
    logger = ProphecyLogger()

    if args.command == "log":
        entries = logger.list(limit=args.limit)
        if not entries:
            print("（予言エラーの履歴はありません）")
            return
        for entry in entries:
            ts = entry["timestamp"]
            msg = entry["message"]
            print(f"[{ts}] {msg}")
    elif args.command == "summary":
        summary = logger.summary()
        if not summary:
            print("（予言エラーの統計はありません）")
            return
        for k, v in summary.items():
            print(f"{k}: {v}回")
    else:
        message = random_prophecy()
        print_prophecy(message, color=not getattr(args, 'no_color', False))
        if not getattr(args, 'no_log', False):
            logger.log(message)

if __name__ == '__main__':
    main()
