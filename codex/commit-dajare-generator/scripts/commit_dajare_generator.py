import os
import sys
import argparse
import subprocess
import re
import random
from typing import List, Tuple

def get_staged_files() -> List[str]:
    try:
        result = subprocess.run([
            'git', 'diff', '--cached', '--name-only'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', check=True)
        files = result.stdout.strip().split('\n')
        return [f for f in files if f]
    except Exception as e:
        print(f"[commit-dajare-generator] git diff error: {e}")
        return []

def get_file_diff(filename: str) -> str:
    try:
        result = subprocess.run([
            'git', 'diff', '--cached', filename
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', check=True)
        return result.stdout
    except Exception as e:
        return ''

def extract_keywords_from_diff(diff_text: str) -> List[str]:
    # シンプルなキーワード抽出: 追加・削除行から英単語/日本語単語を抽出
    keywords = set()
    for line in diff_text.split('\n'):
        if line.startswith('+') or line.startswith('-'):
            # 英単語
            for w in re.findall(r'[a-zA-Z_]{3,}', line):
                keywords.add(w.lower())
            # 日本語単語
            for w in re.findall(r'[\u3040-\u30ff\u4e00-\u9fff]{2,}', line):
                keywords.add(w)
    return list(keywords)

def generate_dajare(file: str, keywords: List[str]) -> str:
    basename = os.path.basename(file)
    name, ext = os.path.splitext(basename)
    dajare_patterns = [
        # 日本語ファイル名・キーワード
        (r'bug', lambda: f"バグがバグっと消えた！"),
        (r'fix', lambda: f"直したらフィックス（fix）した！"),
        (r'update', lambda: f"アップデートしてアップ（up）した気分！"),
        (r'add', lambda: f"addだけに、味（add）わい深い追加！"),
        (r'algorithm', lambda: f"アルゴリズムにアルゴリズム（あるごり無）！"),
        (r'readme', lambda: f"読んでみー（README）！"),
        (r'doc', lambda: f"ドキュメントをドッキュメント！"),
        (r'test', lambda: f"テストして手ストップ（test up）！"),
        (r'config', lambda: f"コンフィグを今フィグ（今更）！"),
        (r'py$', lambda: f"Pythonだけにパイっと直した！"),
        (r'js$', lambda: f"JavaScriptでジャバっと修正！"),
        (r'md$', lambda: f"Markdownでマークだもん！"),
    ]
    # ファイル名・キーワードからダジャレ生成
    for pat, func in dajare_patterns:
        if re.search(pat, name, re.IGNORECASE) or any(re.search(pat, k, re.IGNORECASE) for k in keywords):
            return f"{basename} を修正したので、{func()}"
    # それ以外は汎用
    generic_templates = [
        f"{basename} を編集、編集（エンジュー）しちゃった！",
        f"{basename} をいじって、いじ（維持）できたかな？",
        f"{basename} の変更、変こう（変更）してみた！",
        f"{basename} を追加、ついかっと（追加っと）やった！",
        f"{basename} の修正、修正（しゅうせい）せいこう！"
    ]
    return random.choice(generic_templates)

def compose_commit_message(files: List[str]) -> str:
    messages = []
    for f in files:
        diff = get_file_diff(f)
        keywords = extract_keywords_from_diff(diff)
        msg = generate_dajare(f, keywords)
        messages.append(msg)
    return '\n'.join([f"[commit-dajare-generator] {m}" for m in messages])

def print_commit_message():
    files = get_staged_files()
    if not files:
        print("[commit-dajare-generator] ステージされたファイルがありません。")
        return
    message = compose_commit_message(files)
    print(message)

def main():
    parser = argparse.ArgumentParser(description='commit-dajare-generator: コミット用ダジャレメッセージ自動生成')
    subparsers = parser.add_subparsers(dest='command')

    parser_gen = subparsers.add_parser('generate', help='ステージされた変更からダジャレコミットメッセージを生成')
    parser_list = subparsers.add_parser('list', help='ステージされたファイル一覧を表示')
    parser_test = subparsers.add_parser('test', help='ダジャレ生成のテスト')
    parser_test.add_argument('--file', type=str, required=False, help='テスト用ファイル名')
    parser_test.add_argument('--keywords', type=str, nargs='*', default=[], help='テスト用キーワード')

    args = parser.parse_args()
    if args.command == 'generate':
        print_commit_message()
    elif args.command == 'list':
        files = get_staged_files()
        print("[commit-dajare-generator] ステージされたファイル:")
        for f in files:
            print(f" - {f}")
    elif args.command == 'test':
        fname = args.file or 'test.py'
        keywords = args.keywords
        msg = generate_dajare(fname, keywords)
        print(f"[commit-dajare-generator] {msg}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
