import argparse
import os
import sys
import random
import requests
from typing import List, Optional

OMIKUJI_WORDS = [
    ("大吉", "運命のリファクタリング"),
    ("中吉", "そこそこ良い実装"),
    ("小吉", "軽い修正だけど運は微妙"),
    ("吉", "まあまあなアップデート"),
    ("末吉", "とりあえず動く修正"),
    ("凶", "バグの予感がする変更"),
    ("大凶", "運命を狂わすコミット"),
    ("半吉", "微妙なコードの追加"),
    ("平", "特に何も起きないPR"),
    ("超大吉", "伝説のマージリクエスト")
]

GITHUB_API = "https://api.github.com"


def get_github_token() -> str:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set.", file=sys.stderr)
        sys.exit(1)
    return token


def get_pr_title(owner: str, repo: str, pr_number: int, token: str) -> str:
    url = f"{GITHUB_API}/repos/{owner}/{repo}/pulls/{pr_number}"
    headers = {"Authorization": f"token {token}"}
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print(f"Error: Failed to fetch PR #{pr_number} title. Status: {resp.status_code}", file=sys.stderr)
        sys.exit(1)
    return resp.json()["title"]


def set_pr_title(owner: str, repo: str, pr_number: int, new_title: str, token: str) -> None:
    url = f"{GITHUB_API}/repos/{owner}/{repo}/pulls/{pr_number}"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    data = {"title": new_title}
    resp = requests.patch(url, headers=headers, json=data)
    if resp.status_code != 200:
        print(f"Error: Failed to update PR title. Status: {resp.status_code}", file=sys.stderr)
        sys.exit(1)


def omikuji_title() -> str:
    fortune, phrase = random.choice(OMIKUJI_WORDS)
    return f"{fortune}：{phrase}"


def backup_title(pr_number: int, title: str):
    backup_file = f".pr_title_omikuji_backup_{pr_number}.txt"
    with open(backup_file, "w", encoding="utf-8") as f:
        f.write(title)


def restore_title(pr_number: int) -> Optional[str]:
    backup_file = f".pr_title_omikuji_backup_{pr_number}.txt"
    if not os.path.exists(backup_file):
        return None
    with open(backup_file, "r", encoding="utf-8") as f:
        return f.read().strip()


def list_fortunes():
    print("利用可能な運勢タイトル:")
    for fortune, phrase in OMIKUJI_WORDS:
        print(f"- {fortune}：{phrase}")


def main():
    parser = argparse.ArgumentParser(description="PRタイトルをおみくじ風に変換するスクリプト")
    subparsers = parser.add_subparsers(dest="command")

    # 変換コマンド
    omikuji_parser = subparsers.add_parser("omikuji", help="PRタイトルをおみくじ風に変換")
    omikuji_parser.add_argument("--owner", required=True, help="GitHubリポジトリのオーナー名")
    omikuji_parser.add_argument("--repo", required=True, help="リポジトリ名")
    omikuji_parser.add_argument("--pr", type=int, required=True, help="PR番号")

    # 元に戻す
    restore_parser = subparsers.add_parser("restore", help="タイトルを元に戻す")
    restore_parser.add_argument("--pr", type=int, required=True, help="PR番号")
    restore_parser.add_argument("--owner", required=True, help="GitHubリポジトリのオーナー名")
    restore_parser.add_argument("--repo", required=True, help="リポジトリ名")

    # 運勢リスト
    list_parser = subparsers.add_parser("list", help="運勢ワード一覧を表示")

    args = parser.parse_args()
    token = get_github_token()

    if args.command == "omikuji":
        title = get_pr_title(args.owner, args.repo, args.pr, token)
        backup_title(args.pr, title)
        new_title = omikuji_title()
        set_pr_title(args.owner, args.repo, args.pr, new_title, token)
        print(f"PRタイトルを '{new_title}' に変更しました。")
    elif args.command == "restore":
        orig_title = restore_title(args.pr)
        if orig_title is None:
            print("バックアップタイトルが見つかりません。", file=sys.stderr)
            sys.exit(1)
        set_pr_title(args.owner, args.repo, args.pr, orig_title, token)
        print(f"PRタイトルを元に戻しました: {orig_title}")
    elif args.command == "list":
        list_fortunes()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
