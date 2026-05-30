import sys
import argparse
import random
import requests
import os
from typing import List, Tuple

OMIKUJI_RESULTS = [
    ("大吉", [
        "運命のリファクタリング",
        "祝・テストカバレッジ向上",
        "最高の機能追加",
        "伝説のバグ修正",
        "未来を変えるPR"
    ]),
    ("中吉", [
        "ちょっと良いバグ修正",
        "堅実なリファクタリング",
        "安定性アップデート",
        "良い感じの改善",
        "無難な機能追加"
    ]),
    ("小吉", [
        "軽い修正だけど運は微妙",
        "ささやかな改善",
        "微妙なリファクタ",
        "地味なバグ修正",
        "控えめな機能追加"
    ]),
    ("末吉", [
        "ささやかな機能追加",
        "運勢はこれから",
        "地道なテスト追加",
        "慎ましいアップデート",
        "静かな改善"
    ]),
    ("凶", [
        "不穏な依存関係の更新",
        "危険なバグ修正",
        "波乱のリファクタ",
        "運命を狂わすPR",
        "闇に包まれた修正"
    ])
]

GITHUB_API_URL = "https://api.github.com"


def get_random_omikuji_title() -> str:
    fortune, phrases = random.choice(OMIKUJI_RESULTS)
    phrase = random.choice(phrases)
    return f"{fortune}: {phrase}"


def is_omikuji_title(title: str) -> bool:
    for fortune, _ in OMIKUJI_RESULTS:
        if title.startswith(fortune + ":"):
            return True
    return False


def fetch_pr_title(repo: str, pr_number: int, token: str) -> str:
    url = f"{GITHUB_API_URL}/repos/{repo}/pulls/{pr_number}"
    headers = {"Authorization": f"token {token}"}
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception(f"Failed to fetch PR: {resp.status_code} {resp.text}")
    return resp.json().get("title", "")


def update_pr_title(repo: str, pr_number: int, new_title: str, token: str):
    url = f"{GITHUB_API_URL}/repos/{repo}/pulls/{pr_number}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }
    data = {"title": new_title}
    resp = requests.patch(url, headers=headers, json=data)
    if resp.status_code not in (200, 201):
        raise Exception(f"Failed to update PR: {resp.status_code} {resp.text}")
    return resp.json()


def omikuji_command(args):
    token = args.token or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GitHub token is required via --token or GITHUB_TOKEN env var.", file=sys.stderr)
        sys.exit(1)
    try:
        title = fetch_pr_title(args.repo, args.pr_number, token)
        if is_omikuji_title(title):
            print(f"PR #{args.pr_number} is already omikuji: {title}")
            return
        new_title = get_random_omikuji_title()
        update_pr_title(args.repo, args.pr_number, new_title, token)
        print(f"Updated PR #{args.pr_number} title to: {new_title}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)


def preview_command(args):
    for _ in range(args.count):
        print(get_random_omikuji_title())


def main():
    parser = argparse.ArgumentParser(description="PRタイトルをおみくじ風に変換するツール")
    subparsers = parser.add_subparsers(dest="command")

    omikuji_parser = subparsers.add_parser("omikuji", help="指定PRのタイトルをおみくじ化")
    omikuji_parser.add_argument("--repo", required=True, help="リポジトリ名 (owner/repo)")
    omikuji_parser.add_argument("--pr-number", type=int, required=True, help="PR番号")
    omikuji_parser.add_argument("--token", help="GitHubアクセストークン")
    omikuji_parser.set_defaults(func=omikuji_command)

    preview_parser = subparsers.add_parser("preview", help="おみくじタイトルをランダム生成して表示")
    preview_parser.add_argument("--count", type=int, default=5, help="生成数")
    preview_parser.set_defaults(func=preview_command)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
