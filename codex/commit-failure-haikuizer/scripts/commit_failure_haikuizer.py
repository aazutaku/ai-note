import sys
import argparse
import random
import re
from typing import List

# 俳句のテンプレート候補
HAIKU_TEMPLATES = [
    ["{season}", "{action}の{target}", "{emotion}"],
    ["{error_word}", "{target}に{action}", "{wish}"],
    ["{action}して", "{target}の中", "{emotion}"],
    ["{target}かな", "{action}のあと", "{emotion}"],
    ["{emotion}", "{target}に{action}", "{season}"],
]

SEASON_WORDS = [
    "春の空", "夏の夜", "秋の風", "冬の朝", "遠き空", "夕暮れに", "朝焼けや"
]
ACTIONS = [
    "pushできず", "commit失敗", "衝突して", "pullできず", "競合して", "保存できず", "解決せず"
]
EMOTIONS = [
    "ため息よ", "迷い道", "涙落ち", "立ち尽くす", "苦笑い", "悩み深し", "また明日"
]
WISHES = [
    "次こそは", "願い込め", "やり直し", "再挑戦", "もう一度"
]

# 主要なエラー語句
ERROR_WORDS = [
    "error", "failed", "conflict", "拒否され", "競合", "unmerged", "denied", "not found"
]

def extract_target(error_message: str) -> str:
    # ファイル名やリポジトリ名等を抽出
    file_match = re.search(r'([\w\-/]+\.(py|js|java|rb|go|ts|c|cpp|h|md))', error_message)
    if file_match:
        return file_match.group(1)
    repo_match = re.search(r"github.com[:/](\w+/[\w-]+)", error_message)
    if repo_match:
        return repo_match.group(1)
    # デフォルト
    return "この場所"

def extract_error_word(error_message: str) -> str:
    for w in ERROR_WORDS:
        if w in error_message.lower():
            return w
    return "失敗"

def make_haiku(error_message: str) -> List[str]:
    target = extract_target(error_message)
    action = random.choice(ACTIONS)
    season = random.choice(SEASON_WORDS)
    emotion = random.choice(EMOTIONS)
    wish = random.choice(WISHES)
    error_word = extract_error_word(error_message)
    template = random.choice(HAIKU_TEMPLATES)
    mapping = {
        "target": target,
        "action": action,
        "season": season,
        "emotion": emotion,
        "wish": wish,
        "error_word": error_word
    }
    return [line.format(**mapping) for line in template]

def print_haiku(error_message: str):
    haiku = make_haiku(error_message)
    print("\n俳句:")
    for line in haiku:
        print(line)

def cli():
    parser = argparse.ArgumentParser(description='Commit Failure Haikuizer: エラーを俳句に変換')
    subparsers = parser.add_subparsers(dest='command')

    # 明示呼び出し
    haiku_parser = subparsers.add_parser('haiku', help='エラーメッセージを俳句化')
    haiku_parser.add_argument('message', type=str, help='エラーメッセージ')

    # ログ機能（オプション）
    log_parser = subparsers.add_parser('log', help='俳句ログを表示')
    log_parser.add_argument('--file', type=str, default='.haiku_log.txt', help='ログファイルパス')

    args = parser.parse_args()

    if args.command == 'haiku':
        print_haiku(args.message)
    elif args.command == 'log':
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                print(f.read())
        except FileNotFoundError:
            print('ログファイルがありません')
    else:
        parser.print_help()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        # 標準入力からエラー文を受け取る
        print('エラーメッセージを入力してください（Ctrl+Dで終了）:')
        error_message = sys.stdin.read().strip()
        if error_message:
            print_haiku(error_message)
        else:
            print('エラーメッセージが空です')
    else:
        cli()
