import argparse
import random
import sys
from datetime import datetime, timedelta
from pathlib import Path
try:
    from git import Repo, InvalidGitRepositoryError
except ImportError:
    Repo = None
    InvalidGitRepositoryError = Exception

WEATHER_TYPES = [
    ("快晴", 28, 35),
    ("晴れ", 22, 28),
    ("曇り", 16, 22),
    ("小雨", 12, 16),
    ("雨", 6, 12),
    ("冬日", -5, 6),
    ("真夏日", 32, 40),
]

MOOD_LABELS = [
    ("真夏日", 32),
    ("快晴", 28),
    ("晴れ", 22),
    ("曇り", 16),
    ("小雨", 12),
    ("雨", 6),
    ("冬日", -2),
]

BAR_PREFIX = "[terminal-weather-mood-bar]"


def get_commit_count(repo_path: str = ".", days: int = 1) -> int:
    if Repo is None:
        return -1
    try:
        repo = Repo(repo_path, search_parent_directories=True)
    except InvalidGitRepositoryError:
        return -1
    since = datetime.now() - timedelta(days=days)
    commits = list(repo.iter_commits(since=since.strftime('%Y-%m-%d')))
    return len(commits)


def mood_from_commit_count(commit_count: int) -> (str, int):
    if commit_count < 0:
        # fallback: random mood
        label, tmin, tmax = random.choice(WEATHER_TYPES)
        temp = random.randint(tmin, tmax)
        return label, temp
    # Map commit count to temp (0-10: cold, 11-30: mild, 31+: hot)
    if commit_count == 0:
        label, temp = "曇り", random.randint(14, 19)
    elif commit_count < 3:
        label, temp = "小雨", random.randint(10, 15)
    elif commit_count < 7:
        label, temp = "晴れ", random.randint(20, 25)
    elif commit_count < 15:
        label, temp = "快晴", random.randint(25, 32)
    else:
        label, temp = "真夏日", random.randint(32, 38)
    return label, temp


def random_mood_weather() -> (str, int):
    label, tmin, tmax = random.choice(WEATHER_TYPES)
    temp = random.randint(tmin, tmax)
    return label, temp


def format_weather_bar(label: str, temp: int) -> str:
    return f"{BAR_PREFIX} 今日の気分：{label}、気温{temp}度"

def format_mood_bar(label: str, temp: int) -> str:
    return f"{BAR_PREFIX} テンション：{label}（{temp}度）"


def print_weather_bar(repo_path: str = "."):
    commit_count = get_commit_count(repo_path)
    label, temp = mood_from_commit_count(commit_count)
    print(format_weather_bar(label, temp))

def print_mood_bar(repo_path: str = "."):
    commit_count = get_commit_count(repo_path)
    label, temp = mood_from_commit_count(commit_count)
    print(format_mood_bar(label, temp))

def print_random_weather_bar():
    label, temp = random_mood_weather()
    print(format_weather_bar(label, temp))

def print_random_mood_bar():
    label, temp = random_mood_weather()
    print(format_mood_bar(label, temp))

def list_examples():
    examples = [
        format_weather_bar("小雨", 17),
        format_mood_bar("真夏日", 32),
        format_weather_bar("曇り時々晴れ", 21),
        format_weather_bar("快晴", 28),
        format_mood_bar("冬日", -2),
    ]
    for ex in examples:
        print(ex)

def main():
    parser = argparse.ArgumentParser(description="terminal-weather-mood-bar: 気分天気をターミナルバーに表示")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("weather", help="今日の気分天気を表示 (commit頻度ベース)")
    subparsers.add_parser("mood", help="今日のテンション天気を表示 (commit頻度ベース)")
    subparsers.add_parser("random-weather", help="ランダム気分天気を表示")
    subparsers.add_parser("random-mood", help="ランダムテンション天気を表示")
    subparsers.add_parser("examples", help="出力例を表示")

    parser.add_argument("--repo", type=str, default=".", help="Gitリポジトリのパス (デフォルト: カレントディレクトリ)")

    args = parser.parse_args()

    if args.command == "weather":
        print_weather_bar(args.repo)
    elif args.command == "mood":
        print_mood_bar(args.repo)
    elif args.command == "random-weather":
        print_random_weather_bar()
    elif args.command == "random-mood":
        print_random_mood_bar()
    elif args.command == "examples":
        list_examples()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
