import argparse
import os
import re
import sys
import subprocess
from typing import List, Tuple
import random

DAJARE_TEMPLATES = [
    '{file}を修正したら、{pun}っときた！',
    '{file}に手を加えたら、{pun}な結果に！',
    '{file}にバグがあったけど、バグっと直した！',
    '{file}で証明した、証明書だけにshow me!',
    '{file}の内容を整理したら、整理整頓せいりー！',
    '{file}を追加したら、ついかっとなってやった。',
    '{file}が変わった、変わったねー！',
    '{file}に関数追加、関数だけに感謝！',
    '{file}のバグをfix、fixだけにフィックスミー！',
    '{file}のロジックを強化、強化だけに強火！',
    '{file}のテストを追加、テストだけにテストーリー！',
]

EXCLUDE_PATHS = ['.git', 'build', 'dist', '__pycache__']

PUN_DICTIONARY = [
    ('math', '待ってました'),
    ('util', 'うっつーる'),
    ('test', 'テストーリー'),
    ('fix', 'フィックスミー'),
    ('logic', '強火'),
    ('add', 'ついかっと'),
    ('proof', 'show me'),
    ('sort', '整理整頓せいりー'),
    ('bug', 'バグっと'),
    ('func', '感謝'),
]

def get_staged_files() -> List[str]:
    try:
        result = subprocess.run([
            'git', 'diff', '--cached', '--name-only', '--diff-filter=ACMRT'
        ], capture_output=True, text=True)
        files = result.stdout.strip().split('\n')
        return [f for f in files if f and not any(f.startswith(ex) for ex in EXCLUDE_PATHS)]
    except Exception as e:
        print(f'Error getting staged files: {e}')
        return []

def get_file_diff(file: str) -> str:
    try:
        result = subprocess.run([
            'git', 'diff', '--cached', file
        ], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return ''

def extract_keywords(files: List[str], diffs: List[str]) -> List[str]:
    keywords = set()
    for fname in files:
        base = os.path.basename(fname)
        for k, pun in PUN_DICTIONARY:
            if k in base.lower():
                keywords.add((k, pun))
    for diff in diffs:
        for k, pun in PUN_DICTIONARY:
            if re.search(r'\b' + re.escape(k) + r'\b', diff, re.IGNORECASE):
                keywords.add((k, pun))
    return list(keywords)

def generate_dajare_messages(files: List[str], keywords: List[Tuple[str, str]]) -> List[str]:
    messages = []
    for fname in files:
        base = os.path.basename(fname)
        for k, pun in keywords:
            if k in base.lower():
                template = random.choice(DAJARE_TEMPLATES)
                msg = template.format(file=base, pun=pun)
                messages.append(msg)
    # ファイル名が合致しない場合も適当に生成
    if not messages:
        for fname in files:
            base = os.path.basename(fname)
            template = random.choice(DAJARE_TEMPLATES)
            msg = template.format(file=base, pun='ダジャレ')
            messages.append(msg)
    return list(set(messages))[:5]

def interactive_select(messages: List[str]) -> str:
    print('[commit-dajare-generator]')
    for idx, msg in enumerate(messages):
        print(f'生成候補: ({idx+1}) {msg}')
    print('選択: (番号入力, 0でキャンセル, eで編集)')
    while True:
        sel = input('> ').strip()
        if sel == '0':
            print('キャンセルしました')
            sys.exit(0)
        if sel.lower() == 'e':
            print('編集モード:')
            edited = input('メッセージを入力してください: ').strip()
            if edited:
                return edited
        if sel.isdigit() and 1 <= int(sel) <= len(messages):
            return messages[int(sel)-1]
        print('無効な入力です')

def commit_with_message(msg: str):
    try:
        result = subprocess.run([
            'git', 'commit', '-m', msg
        ])
        if result.returncode != 0:
            print('git commit に失敗しました')
    except Exception as e:
        print(f'commitエラー: {e}')

def main():
    parser = argparse.ArgumentParser(description='コミット時に理系ダジャレメッセージを生成するスキル')
    parser.add_argument('--list', action='store_true', help='生成候補だけ表示しコミットしない')
    parser.add_argument('--commit', action='store_true', help='生成したメッセージでgit commitを実行')
    args = parser.parse_args()

    files = get_staged_files()
    if not files:
        print('ステージされたファイルがありません')
        sys.exit(1)
    diffs = [get_file_diff(f) for f in files]
    keywords = extract_keywords(files, diffs)
    messages = generate_dajare_messages(files, keywords)
    if not messages:
        print('ダジャレ生成に失敗しました')
        sys.exit(1)
    msg = interactive_select(messages)
    if args.list:
        print(f'選択メッセージ: {msg}')
        sys.exit(0)
    if args.commit:
        commit_with_message(msg)
    else:
        print(f'コミットメッセージ案: {msg}')

if __name__ == '__main__':
    main()
