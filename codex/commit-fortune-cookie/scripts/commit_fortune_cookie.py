import sys
import argparse
import hashlib
import random
import datetime
import os

def get_commit_message():
    # Try to get last commit message if inside a git repo
    try:
        import subprocess
        result = subprocess.run(['git', 'log', '-1', '--pretty=%B'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return None
    except Exception:
        return None

def get_commit_timestamp():
    try:
        import subprocess
        result = subprocess.run(['git', 'log', '-1', '--pretty=%ct'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            ts = int(result.stdout.strip())
            return datetime.datetime.fromtimestamp(ts)
        else:
            return datetime.datetime.now()
    except Exception:
        return datetime.datetime.now()

def fortune_seed(message, timestamp):
    base = f"{message or ''}{timestamp}"
    h = hashlib.sha256(base.encode('utf-8')).hexdigest()
    seed = int(h[:16], 16)
    return seed

FORTUNES = [
    "大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"
]

LUCKY_LANGS = [
    "Python", "JavaScript", "Rust", "Go", "TypeScript", "Ruby", "C#", "Java", "C++", "Kotlin", "Swift", "PHP", "Haskell"
]

ADVICES = [
    "今日はJavaScriptに手を出すな。",
    "大吉: コンフリクトなし！",
    "凶: 動くと思うな。",
    "ラッキー言語で書けばバグが減るかも。",
    "今日はコミットメッセージに魂を込めよ。",
    "push前に深呼吸しよう。",
    "レビューは優しさで。",
    "新しい技術に挑戦すべし。",
    "今日は静かにコードを書こう。",
    "エラーを恐れず進め。",
    "リファクタリングは明日でも遅くない。",
    "今日は型安全を意識しよう。",
    "動くコードより読みやすいコードを。",
    "バグはあなたの味方。",
    "今日はテストを書こう。",
    "無理せず休憩を。"
]

def generate_fortune(message, timestamp):
    seed = fortune_seed(message, timestamp)
    random.seed(seed)
    fortune = random.choice(FORTUNES)
    lucky_lang = random.choice(LUCKY_LANGS)
    advice = random.choice(ADVICES)
    return fortune, lucky_lang, advice

def print_fortune(fortune, lucky_lang, advice, message, timestamp):
    print("=== 今日の開発運勢 ===")
    print(f"運勢: {fortune}")
    print(f"ラッキー言語: {lucky_lang}")
    print(f"アドバイス: {advice}")
    if message:
        print(f"コミットメッセージ: {message}")
    print(f"タイムスタンプ: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    print("----------------------")

def main():
    parser = argparse.ArgumentParser(description='commit-fortune-cookie: コミット時に運勢を表示するスキル')
    subparsers = parser.add_subparsers(dest='command')

    show_parser = subparsers.add_parser('show', help='運勢を表示')
    show_parser.add_argument('--message', type=str, help='コミットメッセージ')
    show_parser.add_argument('--timestamp', type=str, help='タイムスタンプ (YYYY-MM-DD HH:MM:SS)')

    args = parser.parse_args()

    if args.command == 'show':
        message = args.message
        if not message:
            message = get_commit_message()
        if args.timestamp:
            try:
                timestamp = datetime.datetime.strptime(args.timestamp, '%Y-%m-%d %H:%M:%S')
            except Exception:
                timestamp = datetime.datetime.now()
        else:
            timestamp = get_commit_timestamp()
        fortune, lucky_lang, advice = generate_fortune(message, timestamp)
        print_fortune(fortune, lucky_lang, advice, message, timestamp)
    else:
        # Default: show current fortune
        message = get_commit_message()
        timestamp = get_commit_timestamp()
        fortune, lucky_lang, advice = generate_fortune(message, timestamp)
        print_fortune(fortune, lucky_lang, advice, message, timestamp)

if __name__ == '__main__':
    main()
