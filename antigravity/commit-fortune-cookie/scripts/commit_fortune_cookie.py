import sys
import argparse
import random
import datetime
import os
from typing import List, Optional

def get_fortunes() -> List[str]:
    return [
        "大吉",
        "中吉",
        "小吉",
        "末吉",
        "吉",
        "凶",
        "大凶"
    ]

def get_lucky_languages() -> List[str]:
    return [
        "Python",
        "JavaScript",
        "Go",
        "Rust",
        "TypeScript",
        "Ruby",
        "C++",
        "Java",
        "Kotlin",
        "Swift",
        "PHP",
        "Scala",
        "Perl"
    ]

def get_advices() -> List[str]:
    return [
        "今日はJavaScriptに手を出すな。",
        "大吉:コンフリクトなし。",
        "凶:動くと思うな。",
        "テストコードは後回しにしないで。",
        "レビューは慎重に。",
        "今日は大胆なリファクタリングを避けよ。",
        "コミットメッセージは丁寧に書こう。",
        "ブランチ名に遊び心を。",
        "新しい言語に触れてみよう。",
        "今日は静かにコードを書く日。",
        "push前に一息つこう。",
        "バグはあなたの味方。",
        "運命を信じてmergeせよ。",
        "今日はコードの美しさを意識しよう。",
        "コミット粒度は細かく。",
        "CIが赤でも落ち込むな。",
        "レビュー依頼は早めに。",
        "ドキュメントを忘れずに。"
    ]

def select_random(items: List[str], seed: Optional[int] = None) -> str:
    if seed is not None:
        random.seed(seed)
    return random.choice(items)

def get_commit_message() -> str:
    # 環境変数や引数からコミットメッセージを取得する想定
    # 例: GIT_COMMIT_MSG 環境変数 or --message/-m オプション
    msg = os.environ.get('GIT_COMMIT_MSG')
    if msg:
        return msg
    # git commit --message から取得
    return "(コミットメッセージ未取得)"

def print_fortune(commit_msg: str, timestamp: Optional[str] = None):
    now = timestamp or datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # シード値: commit_msg+now で毎回違う結果
    seed = hash(commit_msg + now)
    fortune = select_random(get_fortunes(), seed)
    lucky_lang = select_random(get_lucky_languages(), seed + 1)
    advice = select_random(get_advices(), seed + 2)
    print("=== 今日のコミット運勢 ===")
    print(f"運勢: {fortune}")
    print(f"ラッキー言語: {lucky_lang}")
    print(f"アドバイス: {advice}")
    print(f"コミット: \"{commit_msg}\"")
    print(f"時刻: {now}")
    print("=========================")

def log_fortune(commit_msg: str, timestamp: str, log_path: str = '.fortune_cookie_log'):
    line = f"{timestamp}\t{commit_msg}\n"
    try:
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(line)
    except Exception as e:
        print(f"[warn] ログ保存失敗: {e}")

def list_log(log_path: str = '.fortune_cookie_log', limit: int = 10):
    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()[-limit:]
        print("=== コミット運勢ログ ===")
        for line in lines:
            print(line.strip())
        print("=====================")
    except FileNotFoundError:
        print("ログファイルがありません。まだコミットしていません。")

def parse_args():
    parser = argparse.ArgumentParser(description='commit-fortune-cookie: コミット時に運勢を表示するスクリプト')
    subparsers = parser.add_subparsers(dest='command', help='サブコマンド')

    parser_main = subparsers.add_parser('show', help='今日の運勢を表示')
    parser_main.add_argument('-m', '--message', type=str, help='コミットメッセージ')
    parser_main.add_argument('-t', '--timestamp', type=str, help='時刻 (YYYY-MM-DD HH:MM:SS)')
    parser_main.add_argument('--nolog', action='store_true', help='ログ保存しない')

    parser_log = subparsers.add_parser('log', help='運勢ログを表示')
    parser_log.add_argument('--limit', type=int, default=10, help='表示件数')

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'show' or args.command is None:
        commit_msg = args.message or get_commit_message()
        now = args.timestamp or datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print_fortune(commit_msg, now)
        if not args.nolog:
            log_fortune(commit_msg, now)
    elif args.command == 'log':
        list_log(limit=args.limit)
    else:
        print("不明なコマンドです。--help を参照してください。")

if __name__ == '__main__':
    main()
