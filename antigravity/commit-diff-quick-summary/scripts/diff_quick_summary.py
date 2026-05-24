import subprocess
import sys
import argparse
import os
import json
from typing import List, Dict, Tuple

OPENAI_API_KEY_ENV = 'OPENAI_API_KEY'
OPENAI_MODEL = 'gpt-3.5-turbo'


def run_git_diff(staged: bool = False) -> str:
    cmd = ['git', 'diff']
    if staged:
        cmd.append('--cached')
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print('Git diff failed:', e.stderr)
        sys.exit(1)


def parse_diff_files(diff_text: str) -> List[str]:
    files = set()
    for line in diff_text.splitlines():
        if line.startswith('diff --git'):
            parts = line.split(' ')
            if len(parts) >= 4:
                file_path = parts[2][2:]  # Remove 'a/'
                files.add(file_path)
    return list(files)


def summarize_with_openai(diff_text: str, api_key: str, model: str = OPENAI_MODEL) -> str:
    import requests
    endpoint = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    system_prompt = (
        'あなたは優秀なソフトウェアレビュアーです。以下のgit diffの内容を要約し、主要な変更点・影響範囲・不要な変更の有無を日本語で端的にまとめてください。ファイル単位で簡潔に列挙し、全体の影響も述べてください。'
    )
    # トークン制限回避: diffが長すぎる場合は先頭・末尾のみ使う
    max_diff_len = 3500
    if len(diff_text) > max_diff_len:
        diff_text = diff_text[:max_diff_len//2] + '\n...\n' + diff_text[-max_diff_len//2:]
    payload = {
        'model': model,
        'messages': [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': diff_text}
        ],
        'max_tokens': 512,
        'temperature': 0.2
    }
    response = requests.post(endpoint, headers=headers, json=payload, timeout=60)
    if response.status_code != 200:
        raise RuntimeError(f'OpenAI API error: {response.status_code} {response.text}')
    data = response.json()
    return data['choices'][0]['message']['content'].strip()


def print_summary(summary: str):
    print(summary)


def list_changed_files(staged: bool = False):
    diff_text = run_git_diff(staged=staged)
    files = parse_diff_files(diff_text)
    if files:
        print('変更されたファイル:')
        for f in files:
            print(f'- {f}')
    else:
        print('変更はありません')


def main():
    parser = argparse.ArgumentParser(description='コミット前のgit差分をAIで要約表示')
    subparsers = parser.add_subparsers(dest='command')

    parser_summary = subparsers.add_parser('summary', help='現在のdiffを要約')
    parser_summary.add_argument('--staged', action='store_true', help='--cached (staged) の差分を要約')

    parser_list = subparsers.add_parser('list', help='変更ファイル一覧を表示')
    parser_list.add_argument('--staged', action='store_true', help='--cached (staged) の変更を表示')

    args = parser.parse_args()

    if args.command == 'summary':
        api_key = os.environ.get(OPENAI_API_KEY_ENV)
        if not api_key:
            print(f'エラー: {OPENAI_API_KEY_ENV} 環境変数にOpenAI APIキーを設定してください')
            sys.exit(1)
        diff_text = run_git_diff(staged=args.staged)
        if not diff_text.strip():
            print('差分がありません')
            sys.exit(0)
        try:
            summary = summarize_with_openai(diff_text, api_key)
        except Exception as e:
            print('要約に失敗しました:', e)
            sys.exit(1)
        print_summary(summary)
    elif args.command == 'list':
        list_changed_files(staged=args.staged)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
