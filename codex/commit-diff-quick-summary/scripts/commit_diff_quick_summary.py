import argparse
import subprocess
import sys
import os
from typing import List, Tuple, Optional
import openai
import pathlib

EXCLUDE_PATHS = ['node_modules', 'build', '.git', '.venv', '__pycache__']


def get_git_root() -> str:
    try:
        root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], stderr=subprocess.DEVNULL)
        return root.decode('utf-8').strip()
    except subprocess.CalledProcessError:
        print("Error: Not a git repository.", file=sys.stderr)
        sys.exit(1)


def is_excluded(path: str) -> bool:
    return any(part in EXCLUDE_PATHS for part in pathlib.Path(path).parts)


def get_diff_files() -> List[str]:
    try:
        files = subprocess.check_output(['git', 'diff', '--name-only', '--cached'], stderr=subprocess.DEVNULL)
        return [f for f in files.decode('utf-8').splitlines() if f and not is_excluded(f)]
    except subprocess.CalledProcessError:
        print("Error: Unable to get diff files.", file=sys.stderr)
        sys.exit(1)


def get_diff_content(files: List[str]) -> str:
    if not files:
        return ""
    try:
        diff = subprocess.check_output(['git', 'diff', '--cached', '--'] + files, stderr=subprocess.DEVNULL)
        return diff.decode('utf-8')
    except subprocess.CalledProcessError:
        print("Error: Unable to get diff content.", file=sys.stderr)
        sys.exit(1)


def chunk_diff(diff: str, max_tokens: int = 1800) -> List[str]:
    # OpenAI token換算でざっくり分割（1トークン ≒ 4文字）
    lines = diff.splitlines()
    chunks = []
    chunk = []
    char_count = 0
    for line in lines:
        chunk.append(line)
        char_count += len(line)
        if char_count > max_tokens * 4:
            chunks.append('\n'.join(chunk))
            chunk = []
            char_count = 0
    if chunk:
        chunks.append('\n'.join(chunk))
    return chunks


def summarize_diff(diff: str, api_key: str, language: str = 'ja') -> str:
    openai.api_key = api_key
    system_prompt = (
        "あなたは優秀なソフトウェアエンジニアです。以下のgit差分を読み、主要な変更点と影響範囲を端的に日本語で要約してください。"\
        "出力例にならい、ファイル単位で変更箇所と影響範囲を簡潔にまとめてください。"
    )
    chunks = chunk_diff(diff)
    summaries = []
    for idx, chunk in enumerate(chunks):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": chunk}
                ],
                max_tokens=512,
                temperature=0.2
            )
            summaries.append(response['choices'][0]['message']['content'].strip())
        except Exception as e:
            print(f"Error during OpenAI API call: {e}", file=sys.stderr)
            sys.exit(1)
    return '\n'.join(summaries)


def print_summary(summary: str):
    print("主要な変更点・影響範囲まとめ:\n")
    print(summary)


def main():
    parser = argparse.ArgumentParser(description="コミット差分をAIで要約するツール")
    subparsers = parser.add_subparsers(dest='command')

    parser_summary = subparsers.add_parser('summary', help='現在のgit差分をAIで要約')
    parser_summary.add_argument('--api-key', type=str, default=os.environ.get('OPENAI_API_KEY'), help='OpenAI APIキー')
    parser_summary.add_argument('--lang', type=str, default='ja', choices=['ja', 'en'], help='要約言語')
    parser_summary.add_argument('--show-diff', action='store_true', help='要約前にdiff内容も表示')

    parser_list = subparsers.add_parser('list', help='差分ファイル一覧を表示')

    args = parser.parse_args()

    if args.command == 'list':
        files = get_diff_files()
        print("差分ファイル一覧:")
        for f in files:
            print(f)
        sys.exit(0)

    if args.command == 'summary':
        if not args.api_key:
            print("Error: OpenAI APIキーが必要です (--api-key または OPENAI_API_KEY)", file=sys.stderr)
            sys.exit(1)
        files = get_diff_files()
        if not files:
            print("コミット予定の差分がありません。", file=sys.stderr)
            sys.exit(0)
        diff = get_diff_content(files)
        if args.show_diff:
            print("--- 差分内容 ---\n")
            print(diff)
            print("\n--- 要約 ---\n")
        summary = summarize_diff(diff, args.api_key, args.lang)
        print_summary(summary)
        sys.exit(0)

    parser.print_help()
    sys.exit(1)


if __name__ == '__main__':
    main()
