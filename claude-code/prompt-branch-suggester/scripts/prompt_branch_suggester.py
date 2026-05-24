import argparse
import os
import subprocess
import sys
from datetime import datetime
from typing import List, Optional

EXCLUDE_PATHS = ['.git', 'node_modules', '.claude', '__pycache__']

BRANCH_PREFIX_KEYWORDS = ['feature/', 'hotfix/', 'bugfix/', 'release/', 'refactor/']
COMMIT_KEYWORDS = ['fix', 'refactor', 'urgent', 'add', 'remove', 'update', 'test', 'docs']

PROMPT_TEMPLATE = '''# CLAUDE_prompt_branch_{branch_name}.md
- ブランチ名: {branch_name}
- 直近コミット: "{commit_msg}"
- 差分ファイル: {diff_files}
- 指示セット:
{instructions}
'''

INSTRUCTION_RULES = [
    (lambda b, c: 'login' in b or 'login' in c, 'ログイン機能の追加・検証に集中する指示セット\n既存の認証ロジックには触れない\nUI/UXの改善案も提案'),
    (lambda b, c: 'refactor' in b or 'refactor' in c, 'リファクタリング対象のファイルに限定してコード改善\n既存の仕様を壊さないよう注意'),
    (lambda b, c: 'hotfix' in b or 'urgent' in c, '緊急修正のため最小限の変更に留める\n影響範囲を明記'),
    (lambda b, c: True, '通常の機能追加または修正\n既存機能への影響を最小限に')
]

def get_current_branch() -> Optional[str]:
    try:
        out = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], text=True)
        return out.strip()
    except Exception:
        return None

def get_last_commit_message() -> Optional[str]:
    try:
        out = subprocess.check_output(['git', 'log', '-1', '--pretty=%B'], text=True)
        return out.strip()
    except Exception:
        return None

def get_git_diff_files() -> List[str]:
    try:
        out = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'], text=True)
        files = [f.strip() for f in out.splitlines() if f.strip()]
        return [f for f in files if not any(f.startswith(ex) for ex in EXCLUDE_PATHS)]
    except Exception:
        return []

def suggest_instructions(branch: str, commit: str) -> str:
    for rule, instruction in INSTRUCTION_RULES:
        if rule(branch, commit):
            return instruction
    return ''

def generate_prompt_file(branch: str, commit: str, diff_files: List[str], dry_run=False) -> str:
    safe_branch = branch.replace('/', '_').replace('-', '_')
    filename = f'CLAUDE_prompt_branch_{safe_branch}.md'
    instructions = suggest_instructions(branch.lower(), commit.lower())
    content = PROMPT_TEMPLATE.format(
        branch_name=branch,
        commit_msg=commit,
        diff_files=', '.join(diff_files) if diff_files else '（差分なし）',
        instructions=instructions
    )
    if not dry_run:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    return filename

def list_prompt_files():
    files = [f for f in os.listdir('.') if f.startswith('CLAUDE_prompt_branch_') and f.endswith('.md')]
    for f in files:
        print(f)

def summary_prompt_file(filename: str):
    if not os.path.exists(filename):
        print(f'[ERROR] {filename} が存在しません')
        return
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
    print(''.join(lines[:10]) + ('...\n' if len(lines) > 10 else ''))

def main():
    parser = argparse.ArgumentParser(description='prompt-branch-suggester: 作業ブランチやdiffからClaude指示ファイルを自動生成')
    subparsers = parser.add_subparsers(dest='command')

    gen_parser = subparsers.add_parser('generate', help='現在の状態から指示ファイルを生成')
    gen_parser.add_argument('--dry-run', action='store_true', help='ファイルを生成せず内容のみ表示')

    list_parser = subparsers.add_parser('list', help='生成済み指示ファイルを一覧表示')
    sum_parser = subparsers.add_parser('summary', help='指示ファイルの冒頭を表示')
    sum_parser.add_argument('filename', help='要約するファイル名')

    args = parser.parse_args()
    if args.command == 'generate' or args.command is None:
        branch = get_current_branch() or 'unknown_branch'
        commit = get_last_commit_message() or 'no commit message'
        diff_files = get_git_diff_files()
        print(f'[INFO] 現在のブランチ: {branch}')
        print(f'[INFO] 直近コミット: "{commit}"')
        print(f'[INFO] 差分ファイル: {", ".join(diff_files) if diff_files else "（差分なし）"}')
        filename = generate_prompt_file(branch, commit, diff_files, dry_run=getattr(args, 'dry_run', False))
        if getattr(args, 'dry_run', False):
            print('[DRY RUN] ファイル生成せず内容のみ表示')
        else:
            print(f'[OK] {filename} を生成しました')
    elif args.command == 'list':
        list_prompt_files()
    elif args.command == 'summary':
        summary_prompt_file(args.filename)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
