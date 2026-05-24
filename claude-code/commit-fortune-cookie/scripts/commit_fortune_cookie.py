import sys
import argparse
import random
import datetime
import subprocess
from typing import List, Optional

FORTUNE_RESULTS = [
    '大吉', '中吉', '小吉', '吉', '末吉', '凶', '大凶'
]
LUCKY_LANGUAGES = [
    'Python', 'JavaScript', 'TypeScript', 'Go', 'Rust', 'Ruby', 'Kotlin', 'C++', 'Java', 'Scala', 'Haskell', 'PHP', 'Swift', 'C#', 'Perl', 'Elixir', 'Dart', 'Bash', 'Lua'
]
ADVICE_LIST = [
    '今日はJavaScriptに手を出すな',
    '大吉:コンフリクトなし',
    '凶:動くと思うな',
    'レビュー依頼は慎重に',
    'テスト書かずにpushすると危険',
    '今日は型エラーに注意',
    'PRは小さくまとめよう',
    'コミットメッセージは丁寧に',
    '今日は新しい言語に挑戦してみよう',
    'コードレビューでツッコミが入るかも',
    '動作確認は念入りに',
    '今日はペアプロが吉',
    'ドキュメント更新を忘れずに',
    'リファクタリングは明日にしよう',
    'マージ前にpullしておこう',
    'CIが落ちても慌てるな',
    '今日は静的解析ツールを試すと吉',
    'バグは見つけたら即修正',
    'デプロイは慎重に',
    '今日はコードより休憩が大事',
    '新しいライブラリの導入は控えめに',
    '今日はレビュー依頼が通りやすい日',
    'コミット粒度を意識しよう',
    '今日はコメント多めに書くと吉',
    'ローカルで動いても油断するな',
    '今日はブランチ名にこだわってみよう',
    'push前にdiffを確認しよう',
    '今日はペアレビューがオススメ',
    'エディタの設定を見直してみよう',
    '今日は新しいショートカットを覚えると吉'
]


def get_latest_commit_message() -> Optional[str]:
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--pretty=%B'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception:
        return None

def deterministic_random_seed(commit_message: Optional[str], timestamp: str) -> int:
    base = (commit_message or '') + timestamp
    return sum(ord(c) for c in base)

def select_fortune(seed: int) -> str:
    random.seed(seed)
    return random.choice(FORTUNE_RESULTS)

def select_lucky_language(seed: int) -> str:
    random.seed(seed + 13)
    return random.choice(LUCKY_LANGUAGES)

def select_advice(seed: int) -> str:
    random.seed(seed + 29)
    return random.choice(ADVICE_LIST)

def print_fortune(commit_message: Optional[str], timestamp: str):
    seed = deterministic_random_seed(commit_message, timestamp)
    fortune = select_fortune(seed)
    lucky_language = select_lucky_language(seed)
    advice = select_advice(seed)
    print('=== 今日の開発運勢 ===')
    print(f'運勢: {fortune}')
    print(f'ラッキー言語: {lucky_language}')
    print(f'アドバイス: 「{advice}」')
    if commit_message:
        print(f'コミットメッセージ: "{commit_message}"')
    print(f'タイムスタンプ: {timestamp}')
    print('=======================')

def handle_log(args):
    commit_message = get_latest_commit_message()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print_fortune(commit_message, timestamp)

def handle_list(args):
    print('--- 運勢バリエーション一覧 ---')
    print('運勢:', ', '.join(FORTUNE_RESULTS))
    print('ラッキー言語:', ', '.join(LUCKY_LANGUAGES))
    print('アドバイス例:')
    for advice in ADVICE_LIST[:10]:
        print(f' - {advice}')
    print('...他多数')

def handle_summary(args):
    print('commit-fortune-cookie: コミットごとに運勢・ラッキー言語・アドバイスを表示するスキルです。')
    print('明示呼び出し: /commit-fortune-cookie')
    print('暗黙発動: commit, push, merge など')
    print('詳細は SKILL.md を参照してください。')

def main():
    parser = argparse.ArgumentParser(description='commit-fortune-cookie: コミットごとに開発運勢を表示するスキル')
    subparsers = parser.add_subparsers(dest='command')
    parser_log = subparsers.add_parser('log', help='今の運勢を表示（通常発動）')
    parser_log.set_defaults(func=handle_log)
    parser_list = subparsers.add_parser('list', help='運勢・ラッキー言語・アドバイス一覧')
    parser_list.set_defaults(func=handle_list)
    parser_summary = subparsers.add_parser('summary', help='スキル概要を表示')
    parser_summary.set_defaults(func=handle_summary)

    # デフォルトはlog
    if len(sys.argv) == 1:
        args = parser.parse_args(['log'])
    else:
        args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
