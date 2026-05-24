import argparse
import os
import subprocess
import sys
from datetime import datetime, timedelta
from typing import List, Tuple, Dict

def get_git_branch() -> str:
    try:
        result = subprocess.run([
            'git', 'rev-parse', '--abbrev-ref', 'HEAD'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return '(not a git repository)'

def get_git_branches() -> List[str]:
    try:
        result = subprocess.run(['git', 'branch'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        branches = [line.strip().replace('* ', '') for line in result.stdout.splitlines()]
        return branches
    except subprocess.CalledProcessError:
        return []

def get_recently_modified_files(limit: int = 10) -> List[Tuple[str, float]]:
    files = []
    for root, dirs, filenames in os.walk('.'):
        # 除外ディレクトリ
        if '.git' in dirs:
            dirs.remove('.git')
        for fname in filenames:
            path = os.path.join(root, fname)
            try:
                stat = os.stat(path)
                mtime = stat.st_mtime
                files.append((path, mtime))
            except Exception:
                continue
    files.sort(key=lambda x: x[1], reverse=True)
    return files[:limit]

def get_recent_git_logs(limit: int = 10) -> List[Dict]:
    try:
        result = subprocess.run([
            'git', 'log', f'-{limit}', '--pretty=format:%h|%an|%ad|%s', '--date=iso'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        logs = []
        for line in result.stdout.strip().splitlines():
            parts = line.split('|', 3)
            if len(parts) == 4:
                logs.append({
                    'hash': parts[0],
                    'author': parts[1],
                    'date': parts[2],
                    'subject': parts[3]
                })
        return logs
    except subprocess.CalledProcessError:
        return []

def format_time_ago(epoch: float) -> str:
    now = datetime.now().timestamp()
    diff = now - epoch
    if diff < 60:
        return f'{int(diff)}秒前'
    elif diff < 3600:
        return f'{int(diff // 60)}分前'
    elif diff < 86400:
        return f'{int(diff // 3600)}時間前'
    else:
        return f'{int(diff // 86400)}日前'

def summary():
    print('[Context Branch Highlighter]')
    current_branch = get_git_branch()
    print(f'現在の作業ブランチ: {current_branch}')

    files = get_recently_modified_files(limit=5)
    if files:
        print('直近の編集ファイル:')
        for path, mtime in files:
            print(f'  - {path} ({format_time_ago(mtime)})')
    else:
        print('直近の編集ファイルは見つかりません')

    print(f'推奨フォーカス: {current_branch}')
    branches = get_git_branches()
    if branches:
        others = [b for b in branches if b != current_branch]
        if others:
            print(f'他のアクティブブランチ: {", ".join(others)}')
    print('')

def log():
    logs = get_recent_git_logs(limit=10)
    print('[直近のGitコミットログ]')
    for l in logs:
        print(f'{l["hash"]} | {l["author"]} | {l["date"]} | {l["subject"]}')

def list_files():
    files = get_recently_modified_files(limit=10)
    print('[最近編集されたファイル]')
    for path, mtime in files:
        print(f'{path} ({format_time_ago(mtime)})')

def main():
    parser = argparse.ArgumentParser(description='Context Branch Highlighter')
    subparsers = parser.add_subparsers(dest='command')

    parser_summary = subparsers.add_parser('summary', help='現在の作業ブランチ・ファイルを要約表示')
    parser_log = subparsers.add_parser('log', help='直近のGitコミットログを表示')
    parser_list = subparsers.add_parser('list', help='最近編集されたファイル一覧')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)
    if args.command == 'summary':
        summary()
    elif args.command == 'log':
        log()
    elif args.command == 'list':
        list_files()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
