import argparse
import random
import sys
import requests
import os
from typing import List, Dict, Optional

OMIKUJI_RESULTS = [
    ("大吉", "運命のリファクタリング"),
    ("中吉", "ちょっと良い感じ"),
    ("小吉", "軽い修正だけど運は微妙"),
    ("末吉", "まあまあの変更"),
    ("凶", "波乱の予感"),
    ("大凶", "全てを巻き込む混沌"),
    ("吉", "普通のアップデート"),
    ("半吉", "やや良し"),
    ("末小吉", "微妙な運勢"),
    ("平", "何も起きないかも"),
]

GITHUB_API_URL = "https://api.github.com"


def omikuji_title(original_title: str) -> str:
    fortune, comment = random.choice(OMIKUJI_RESULTS)
    return f"[{fortune}] {comment}: {original_title}"


def get_pr_info(owner: str, repo: str, pr_number: int, token: str) -> Dict:
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/pulls/{pr_number}"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()


def update_pr_title(owner: str, repo: str, pr_number: int, new_title: str, token: str) -> None:
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/pulls/{pr_number}"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    data = {"title": new_title}
    resp = requests.patch(url, headers=headers, json=data)
    resp.raise_for_status()


def list_omikuji_samples(n: int = 10, sample_title: str = "サンプルPRタイトル") -> List[str]:
    results = []
    for _ in range(n):
        results.append(omikuji_title(sample_title))
    return results


def parse_args():
    parser = argparse.ArgumentParser(description="PRタイトルをおみくじ風に変換するツール")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_run = subparsers.add_parser("run", help="指定のPRタイトルをおみくじ化してGitHubに反映")
    parser_run.add_argument("--owner", required=True, help="GitHubリポジトリのオーナー名")
    parser_run.add_argument("--repo", required=True, help="リポジトリ名")
    parser_run.add_argument("--pr", type=int, required=True, help="PR番号")
    parser_run.add_argument("--token", required=False, help="GitHubトークン（環境変数GITHUB_TOKENでも可）")
    parser_run.add_argument("--dry-run", action="store_true", help="タイトル変更せず出力のみ")

    parser_sample = subparsers.add_parser("sample", help="おみくじタイトルのサンプルを表示")
    parser_sample.add_argument("--n", type=int, default=10, help="サンプル数")
    parser_sample.add_argument("--title", default="サンプルPRタイトル", help="元タイトル")

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "sample":
        samples = list_omikuji_samples(args.n, args.title)
        for s in samples:
            print(s)
        return
    elif args.command == "run":
        token = args.token or os.environ.get("GITHUB_TOKEN")
        if not token:
            print("GitHubトークンが指定されていません。--token または GITHUB_TOKEN 環境変数を設定してください。", file=sys.stderr)
            sys.exit(1)
        try:
            pr_info = get_pr_info(args.owner, args.repo, args.pr, token)
            original_title = pr_info.get("title", "")
            new_title = omikuji_title(original_title)
            if args.dry_run:
                print(f"新タイトル: {new_title}")
                return
            update_pr_title(args.owner, args.repo, args.pr, new_title, token)
            print(f"PR #{args.pr} のタイトルを変更しました: {new_title}")
        except requests.HTTPError as e:
            print(f"APIエラー: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as ex:
            print(f"エラー: {ex}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
