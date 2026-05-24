import argparse
import os
import sys
from datetime import datetime
from typing import List, Optional

LOG_DIR = os.path.expanduser("~/.claude/skills/context-switch-logbook/")
LOG_FILE = os.path.join(LOG_DIR, "context_switch_log.txt")


def ensure_log_dir():
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
    except Exception as e:
        print(f"[ERROR] ログディレクトリ作成失敗: {e}", file=sys.stderr)
        sys.exit(1)


def log_context_switch(reason: str):
    ensure_log_dir()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{now}] {reason.strip()}\n"
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
    except Exception as e:
        print(f"[ERROR] ログ書き込み失敗: {e}", file=sys.stderr)
        sys.exit(1)


def list_logs(limit: Optional[int] = None):
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if limit:
                lines = lines[-limit:]
            for line in lines:
                print(line.rstrip())
    except FileNotFoundError:
        print("[INFO] ログファイルがまだ作成されていません。")
    except Exception as e:
        print(f"[ERROR] ログ読み込み失敗: {e}", file=sys.stderr)
        sys.exit(1)


def summary_logs():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        total = len(lines)
        contexts = {}
        for line in lines:
            if "] " in line:
                _, rest = line.split("] ", 1)
                key = rest.split("から", 1)[0] if "から" in rest else rest.split("へ", 1)[0]
                key = key.strip()
                if key:
                    contexts[key] = contexts.get(key, 0) + 1
        print(f"合計記録数: {total}")
        print("文脈切替回数 (上位5件):")
        for k, v in sorted(contexts.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {k}: {v}回")
    except FileNotFoundError:
        print("[INFO] ログファイルがまだ作成されていません。")
    except Exception as e:
        print(f"[ERROR] サマリー取得失敗: {e}", file=sys.stderr)
        sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser(description="文脈切替ログブック: context-switch-logbook")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # logサブコマンド
    p_log = subparsers.add_parser("log", help="文脈切替を記録する")
    p_log.add_argument("reason", type=str, help="切替理由・経緯 (日本語で簡潔に)")

    # listサブコマンド
    p_list = subparsers.add_parser("list", help="ログを一覧表示")
    p_list.add_argument("-n", "--limit", type=int, default=None, help="最新n件のみ表示")

    # summaryサブコマンド
    subparsers.add_parser("summary", help="文脈切替のサマリーを表示")

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "log":
        log_context_switch(args.reason)
        print("[OK] 文脈切替が記録されました。")
    elif args.command == "list":
        list_logs(args.limit)
    elif args.command == "summary":
        summary_logs()
    else:
        print("[ERROR] 未知のコマンドです。", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
