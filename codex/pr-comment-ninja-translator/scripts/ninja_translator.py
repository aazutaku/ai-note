import argparse
import sys
import re
import requests
from typing import List, Optional

NINJA_PREFIXES = [
    "拙者思うに、",
    "ござる…",
    "忍法、",
    "影の如く、",
    "お主、",
    "これは…",
    "うむ、",
    "ふむ、",
    "この術式、",
    "忍びの心得として、"
]
NINJA_SUFFIXES = [
    "でござる。",
    "の術！",
    "と見受けられる！",
    "お願い申す！",
    "よろしいか？",
    "拙者も同意でござる。",
    "…かもしれぬ。",
    "…と申す！",
    "…でござろう！",
    "…御免！"
]
NINJA_WORDS = [
    (r"バグ", "バグの術"),
    (r"関数", "術式"),
    (r"変数", "変数（影）"),
    (r"修正", "修正の術"),
    (r"テスト", "テストの術"),
    (r"不足", "足りぬ"),
    (r"明確", "明快"),
    (r"問題", "難儀"),
    (r"確認", "見極め"),
    (r"必要", "必須の術"),
    (r"追加", "加えるの術"),
    (r"削除", "消すの術"),
    (r"改善", "改良の術")
]

def ninja_translate(text: str) -> str:
    lines = text.strip().splitlines()
    result = []
    for line in lines:
        orig = line.strip()
        if not orig:
            result.append("")
            continue
        # 変換
        ninja_line = orig
        for pat, rep in NINJA_WORDS:
            ninja_line = re.sub(pat, rep, ninja_line)
        # プレフィックスとサフィックスを適当に付加
        prefix = NINJA_PREFIXES[hash(ninja_line) % len(NINJA_PREFIXES)]
        suffix = NINJA_SUFFIXES[hash(orig) % len(NINJA_SUFFIXES)]
        # 既に忍者語ならスキップ
        if any(w in ninja_line for w in ["でござる", "術", "拙者", "ござる…"]):
            result.append(ninja_line)
        else:
            # 文章の長さや終止形に応じて調整
            if ninja_line.endswith("。"):
                ninja_line = ninja_line[:-1]
            ninja_line = f"{prefix}{ninja_line}{suffix}"
            result.append(ninja_line)
    return "\n".join(result)

def fetch_github_comment(token: str, repo: str, comment_id: int) -> Optional[str]:
    url = f"https://api.github.com/repos/{repo}/pulls/comments/{comment_id}"
    headers = {"Authorization": f"token {token}"}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json().get("body", "")
    else:
        print(f"GitHub API error: {resp.status_code} {resp.text}", file=sys.stderr)
        return None

def post_github_comment(token: str, repo: str, pr_number: int, body: str):
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    resp = requests.post(url, headers=headers, json={"body": body})
    if resp.status_code == 201:
        print("コメント投稿成功！")
    else:
        print(f"投稿失敗: {resp.status_code} {resp.text}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="PRコメントを忍者口調に変換するツール")
    subparsers = parser.add_subparsers(dest="command")

    # translateコマンド
    p_trans = subparsers.add_parser("translate", help="テキストを忍者口調に変換")
    p_trans.add_argument("--text", type=str, help="変換するテキスト")
    p_trans.add_argument("--infile", type=str, help="テキストファイルから入力")
    p_trans.add_argument("--outfile", type=str, help="変換結果をファイル出力")

    # github-fetchコマンド
    p_fetch = subparsers.add_parser("github-fetch", help="GitHub PRコメントを取得して変換")
    p_fetch.add_argument("--token", type=str, required=True, help="GitHubアクセストークン")
    p_fetch.add_argument("--repo", type=str, required=True, help="リポジトリ名 (user/repo)")
    p_fetch.add_argument("--comment-id", type=int, required=True, help="PRコメントID")
    p_fetch.add_argument("--post", action="store_true", help="変換後にPRへコメント投稿")
    p_fetch.add_argument("--pr-number", type=int, help="コメント投稿先PR番号")

    args = parser.parse_args()
    if args.command == "translate":
        if args.text:
            input_text = args.text
        elif args.infile:
            try:
                with open(args.infile, encoding="utf-8") as f:
                    input_text = f.read()
            except Exception as e:
                print(f"ファイル読み込み失敗: {e}", file=sys.stderr)
                sys.exit(1)
        else:
            print("--text か --infile を指定してください", file=sys.stderr)
            sys.exit(1)
        result = ninja_translate(input_text)
        if args.outfile:
            with open(args.outfile, "w", encoding="utf-8") as f:
                f.write(result)
        else:
            print(result)
    elif args.command == "github-fetch":
        comment = fetch_github_comment(args.token, args.repo, args.comment_id)
        if comment is None:
            sys.exit(1)
        result = ninja_translate(comment)
        print("---- 変換結果 ----")
        print(result)
        if args.post:
            if not args.pr_number:
                print("--pr-number を指定してください", file=sys.stderr)
                sys.exit(1)
            post_github_comment(args.token, args.repo, args.pr_number, result)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
