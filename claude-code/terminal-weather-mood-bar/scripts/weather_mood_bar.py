import argparse
import random
import datetime
import subprocess
import sys
from typing import Optional, Tuple

try:
    from git import Repo
except ImportError:
    Repo = None

WEATHER_TYPES = [
    ('晴れ', 27, 35),
    ('曇り', 18, 26),
    ('雨', 10, 17),
    ('雪', -5, 3),
    ('春一番', 20, 24),
    ('真夏日', 30, 39),
    ('台風', 22, 28),
    ('快晴', 25, 32),
    ('みぞれ', 2, 8),
    ('雷雨', 16, 23)
]

MOOD_LEVELS = [
    ('氷点下', 'やる気ゼロ'),
    ('小春日和', 'ほんのり前向き'),
    ('春一番レベル', 'やや高め'),
    ('真夏日', '絶好調'),
    ('台風接近', '不安定'),
    ('秋晴れ', '安定')
]

FORECASTS = [
    '夕方から雨のち快晴',
    '夜は曇り',
    '明日は晴れ',
    '午後から雷雨注意',
    '一時的にみぞれ',
    '終日安定',
    '突風に注意',
    '気圧の谷',
    '夕方から回復',
    '気温差に注意'
]

def get_commit_count_today(repo_path: Optional[str] = None) -> int:
    """今日のコミット数を取得"""
    if Repo is None:
        return -1
    try:
        repo = Repo(repo_path or '.')
        today = datetime.datetime.now().date()
        count = 0
        for commit in repo.iter_commits('HEAD', max_count=100):
            commit_date = datetime.datetime.fromtimestamp(commit.committed_date).date()
            if commit_date == today:
                count += 1
        return count
    except Exception:
        return -1

def map_commit_to_weather(commit_count: int) -> Tuple[str, int]:
    """コミット数から気分天気をマッピング"""
    if commit_count < 0:
        return random_weather()
    if commit_count == 0:
        return ('雪', random.randint(-3, 2))
    elif commit_count == 1:
        return ('曇り', random.randint(14, 18))
    elif commit_count == 2:
        return ('雨', random.randint(10, 16))
    elif commit_count < 5:
        return ('晴れ', random.randint(20, 26))
    elif commit_count < 10:
        return ('快晴', random.randint(25, 32))
    else:
        return ('真夏日', random.randint(32, 38))

def random_weather() -> Tuple[str, int]:
    weather, tmin, tmax = random.choice(WEATHER_TYPES)
    temp = random.randint(tmin, tmax)
    return (weather, temp)

def map_commit_to_mood(commit_count: int) -> Tuple[str, str]:
    if commit_count < 0:
        return random.choice(MOOD_LEVELS)
    elif commit_count == 0:
        return MOOD_LEVELS[0]
    elif commit_count == 1:
        return MOOD_LEVELS[1]
    elif commit_count < 4:
        return MOOD_LEVELS[2]
    elif commit_count < 8:
        return MOOD_LEVELS[3]
    elif commit_count < 12:
        return MOOD_LEVELS[5]
    else:
        return MOOD_LEVELS[4]

def get_forecast() -> str:
    return random.choice(FORECASTS)

def show_weather_mood(repo_path: Optional[str] = None) -> None:
    commit_count = get_commit_count_today(repo_path)
    weather, temp = map_commit_to_weather(commit_count)
    mood, mood_desc = map_commit_to_mood(commit_count)
    forecast = get_forecast()
    print("[今日の気分] {}  体感温度: {}℃".format(weather, temp))
    print("[テンション] {}（{}）".format(mood, mood_desc))
    print("[気分予報] {}".format(forecast))
    if commit_count >= 0:
        print("[コミット頻度] {}回/日 → 気温: {}℃".format(commit_count, temp))
    else:
        print("[コミット頻度] 取得不可 → 気温: {}℃".format(temp))
    print("--------------------------------------")

def main():
    parser = argparse.ArgumentParser(description='ターミナル気分天気バー')
    subparsers = parser.add_subparsers(dest='command')

    show_parser = subparsers.add_parser('show', help='気分天気を表示')
    show_parser.add_argument('--repo', type=str, default=None, help='Gitリポジトリパス')

    args = parser.parse_args()

    if args.command == 'show' or args.command is None:
        show_weather_mood(args.repo)
    else:
        print('未対応のコマンドです')
        sys.exit(1)

if __name__ == '__main__':
    main()
