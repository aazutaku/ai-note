import argparse
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple

def run_git_command(args: List[str], cwd: Optional[str] = None) -> str:
    try:
        result = subprocess.run(['git'] + args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return ''

def get_git_root(path: str) -> Optional[str]:
    root = run_git_command(['rev-parse', '--show-toplevel'], cwd=path)
    return root if root else None

def list_branches(git_root: str) -> List[str]:
    output = run_git_command(['branch', '--list'], cwd=git_root)
    return [line.strip().replace('* ', '') for line in output.splitlines() if line.strip()]

def get_current_branch(git_root: str) -> Optional[str]:
    output = run_git_command(['rev-parse', '--abbrev-ref', 'HEAD'], cwd=git_root)
    return output if output else None

def get_recent_commits(git_root: str, branch: str, max_count: int = 10) -> List[Dict]:
    output = run_git_command(['log', branch, f'--max-count={max_count}', '--pretty=format:%H|%an|%ad|%s', '--date=iso'], cwd=git_root)
    commits = []
    for line in output.splitlines():
        parts = line.split('|', 3)
        if len(parts) == 4:
            commits.append({
                'hash': parts[0],
                'author': parts[1],
                'date': parts[2],
                'subject': parts[3],
            })
    return commits

def get_branch_point(git_root: str, branch: str, base: str = 'develop') -> Optional[str]:
    output = run_git_command(['merge-base', branch, base], cwd=git_root)
    return output if output else None

def get_modified_files(git_root: str) -> List[str]:
    output = run_git_command(['status', '--porcelain'], cwd=git_root)
    files = []
    for line in output.splitlines():
        if line:
            files.append(line[3:])
    return files

def get_recently_modified_files(git_root: str, branch: str, max_files: int = 5) -> List[Tuple[str, str]]:
    output = run_git_command(['log', branch, '--name-only', '--pretty=format:%ad|%an', '--date=iso', f'--max-count={max_files*2}'], cwd=git_root)
    lines = output.splitlines()
    result = []
    last_meta = None
    for line in lines:
        if '|' in line:
            last_meta = line
        elif line.strip():
            if last_meta:
                date, author = last_meta.split('|', 1)
                result.append((line.strip(), date.strip()))
    # Remove duplicates, keep order
    seen = set()
    unique = []
    for fname, dt in result:
        if fname not in seen:
            unique.append((fname, dt))
            seen.add(fname)
        if len(unique) >= max_files:
            break
    return unique

def summarize_context(git_root: str) -> str:
    branches = list_branches(git_root)
    curr_branch = get_current_branch(git_root)
    if not curr_branch:
        return 'Gitブランチ情報が取得できませんでした。'
    recent_files = get_recently_modified_files(git_root, curr_branch)
    recent_commits = get_recent_commits(git_root, curr_branch, 3)
    branch_point = get_branch_point(git_root, curr_branch)
    other_branches = [b for b in branches if b != curr_branch]
    msg = []
    msg.append('[Context Branch Highlighter]')
    msg.append(f'主要作業ブランチ: {curr_branch} (最終編集: {recent_files[0][1] if recent_files else "N/A"})')
    if recent_files:
        msg.append('関連ファイル: ' + ', '.join([f[0] for f in recent_files]))
    msg.append('直近の編集履歴:')
    for c in recent_commits:
        msg.append(f'  - {c["date"][:16]}: {c["subject"]} ({c["author"]})')
    if branch_point:
        msg.append(f'分岐点: develop → {curr_branch}')
    if other_branches:
        msg.append('他の並行ブランチ: ' + ', '.join(other_branches))
    msg.append(f'推奨: {curr_branch} に注力')
    return '\n'.join(msg)

def main():
    parser = argparse.ArgumentParser(description='Context Branch Highlighter')
    subparsers = parser.add_subparsers(dest='command')

    parser_summary = subparsers.add_parser('summary', help='現在の作業コンテキストを要約表示')
    parser_summary.add_argument('--path', type=str, default='.', help='対象ディレクトリ (Gitリポジトリ)')

    parser_list = subparsers.add_parser('list', help='全ブランチと直近の編集ファイル一覧')
    parser_list.add_argument('--path', type=str, default='.', help='対象ディレクトリ')

    parser_log = subparsers.add_parser('log', help='ブランチごとの編集履歴を表示')
    parser_log.add_argument('--branch', type=str, default=None, help='対象ブランチ')
    parser_log.add_argument('--path', type=str, default='.', help='対象ディレクトリ')
    parser_log.add_argument('--count', type=int, default=10, help='表示件数')

    args = parser.parse_args()
    git_root = get_git_root(args.path)
    if not git_root:
        print('このディレクトリはGitリポジトリではありません。', file=sys.stderr)
        sys.exit(1)

    if args.command == 'summary':
        print(summarize_context(git_root))
    elif args.command == 'list':
        branches = list_branches(git_root)
        print('全ブランチ:')
        for b in branches:
            print('  -', b)
        curr_branch = get_current_branch(git_root)
        if curr_branch:
            files = get_recently_modified_files(git_root, curr_branch, 10)
            print(f'直近の編集ファイル ({curr_branch}):')
            for f, dt in files:
                print(f'  - {f} ({dt[:16]})')
    elif args.command == 'log':
        branch = args.branch or get_current_branch(git_root)
        if not branch:
            print('ブランチが指定されていません。', file=sys.stderr)
            sys.exit(1)
        commits = get_recent_commits(git_root, branch, args.count)
        print(f'{branch} の編集履歴:')
        for c in commits:
            print(f'  - {c["date"][:16]}: {c["subject"]} ({c["author"]})')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
