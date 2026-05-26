import argparse
import sys
import os
import random
import datetime
from typing import Tuple, Optional

try:
    from git import Repo, InvalidGitRepositoryError
except ImportError:
    Repo = None
    InvalidGitRepositoryError = Exception

def get_git_commit_count(repo_path: str, since_days: int = 1) -> int:
    if not Repo:
        return -1
    try:
        repo = Repo(repo_path, search_parent_directories=True)
        since = datetime.datetime.now() - datetime.timedelta(days=since_days)
        commits = list(repo.iter_commits(since=since.isoformat()))
        return len(commits)
    except InvalidGitRepositoryError:
        return -1
    except Exception:
        return -1

def map_commit_to_weather(commit_count: int) -> Tuple[str, int, str]:
    # commit_countが-1ならランダム
    weather_types = [
        ("快晴", 27, "真夏日"),
        ("晴れ", 23, "やる気十分"),
        ("曇り", 18, "普通"),
        ("小雨", 15, "やや低め"),
        ("大雨", 10, "低気圧"),
        ("雪", 2, "冬眠モード"),
        ("春一番", 20, "上昇気流"),
        ("台風", 30, "荒ぶる魂")
    ]
    if commit_count == -1:
        idx = random.randint(0, len(weather_types)-1)
        w, t, m = weather_types[idx]
        temp = t + random.randint(-2, 2)
        return w, temp, m
    if commit_count >= 15:
        return "快晴", 28 + random.randint(-1,2), "真夏日"
    elif commit_count >= 10:
        return "晴れ", 23 + random.randint(-2,2), "やる気十分"
    elif commit_count >= 5:
        return "曇り", 18 + random.randint(-2,2), "普通"
    elif commit_count >= 2:
        return "小雨", 15 + random.randint(-2,2), "やや低め"
    elif commit_count > 0:
        return "大雨", 10 + random.randint(-2,2), "低気圧"
    elif commit_count == 0:
        return "雪", 2 + random.randint(-1,1), "冬眠モード"
    else:
        idx = random.randint(0, len(weather_types)-1)
        w, t, m = weather_types[idx]
        temp = t + random.randint(-2, 2)
        return w, temp, m

def generate_report(repo_path: Optional[str] = None) -> str:
    commit_count = get_git_commit_count(repo_path or os.getcwd())
    weather, temp, mood = map_commit_to_weather(commit_count)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if commit_count == -1:
        commit_info = "commit頻度：取得不可 (ランダム)"
    else:
        commit_info = f"commit数：{commit_count} (本日)"
    report = (
        f"[terminal-weather-mood-bar] ({now})\n"
        f"今日の気分：{weather}、気温{temp}度\n"
        f"テンション：{mood}\n"
        f"{commit_info}\n"
        f"-----------------------------"
    )
    return report

def print_report(args):
    report = generate_report(args.repo)
    print(report)

def main():
    parser = argparse.ArgumentParser(
        description="terminal-weather-mood-bar: 気分やテンションを天気・気温風に表示するツール"
    )
    subparsers = parser.add_subparsers(dest="command")

    show_parser = subparsers.add_parser("show", help="現在の気分天気を表示")
    show_parser.add_argument("--repo", type=str, default=None, help="Gitリポジトリのパス (省略時はカレント)")
    
    # サブコマンド: summary (過去7日分)
    summary_parser = subparsers.add_parser("summary", help="過去7日分の気分天気を表示")
    summary_parser.add_argument("--repo", type=str, default=None, help="Gitリポジトリのパス (省略時はカレント)")

    args = parser.parse_args()

    if args.command == "show":
        print_report(args)
    elif args.command == "summary":
        repo_path = args.repo or os.getcwd()
        print(f"[terminal-weather-mood-bar] 過去7日分の気分天気レポート\n-----------------------------")
        for i in range(7, 0, -1):
            day = datetime.datetime.now() - datetime.timedelta(days=i)
            commit_count = get_git_commit_count(repo_path, since_days=i)
            weather, temp, mood = map_commit_to_weather(commit_count)
            date_str = day.strftime("%Y-%m-%d")
            if commit_count == -1:
                commit_info = "commit頻度：取得不可 (ランダム)"
            else:
                commit_info = f"commit数：{commit_count}"
            print(f"{date_str} | 気分：{weather}、{temp}度 | テンション：{mood} | {commit_info}")
        print("-----------------------------")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
