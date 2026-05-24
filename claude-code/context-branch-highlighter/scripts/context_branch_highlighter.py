import argparse
import os
import subprocess
import sys
from datetime import datetime, timedelta
from typing import List, Dict, Optional

def run_git_command(args: List[str], cwd: Optional[str] = None) -> str:
    try:
        result = subprocess.run(['git'] + args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Git command failed: {' '.join(args)}\n{e.stderr.strip()}")

def get_current_branch() -> str:
    return run_git_command(['rev-parse', '--abbrev-ref', 'HEAD'])

def get_recently_modified_files(limit: int = 5) -> List[Dict]:
    output = run_git_command(['log', '--name-only', '--pretty=format:%ct', '-n', str(limit * 3)])
    lines = output.splitlines()
    files = []
    last_time = None
    for line in lines:
        if line.isdigit():
            last_time = int(line)
        elif line.strip() != '':
            files.append({'file': line.strip(), 'timestamp': last_time})
    # Remove duplicates, keep most recent
    seen = set()
    result = []
    for entry in files:
        if entry['file'] not in seen:
            seen.add(entry['file'])
            result.append(entry)
        if len(result) >= limit:
            break
    return result

def get_branch_relations(current: str) -> Dict:
    # Find parent (merge-base with main/develop), siblings (branches from same parent)
    branches = run_git_command(['branch', '--format=%(refname:short)']).splitlines()
    parent = None
    siblings = []
    main_branches = ['main', 'master', 'develop']
    for mb in main_branches:
        if mb in branches:
            try:
                merge_base = run_git_command(['merge-base', current, mb])
                # Find which branch is direct parent
                parent = mb
                break
            except Exception:
                continue
    # Siblings: branches with same parent (simplified)
    for b in branches:
        if b != current and b != parent:
            try:
                if parent:
                    mb = run_git_command(['merge-base', b, parent])
                    if mb == run_git_command(['merge-base', current, parent]):
                        siblings.append(b)
            except Exception:
                continue
    return {'parent': parent, 'siblings': siblings}

def get_branch_tree(current: str) -> List[str]:
    # Show ancestry (current <- parent <- grandparent)
    ancestry = [current]
    try:
        commit = run_git_command(['rev-parse', current])
        for _ in range(3):
            parents = run_git_command(['rev-list', '--parents', '-n', '1', commit]).split()
            if len(parents) > 1:
                parent_commit = parents[1]
                parent_branch = None
                branches = run_git_command(['branch', '--contains', parent_commit, '--format=%(refname:short)']).splitlines()
                for b in branches:
                    if b not in ancestry:
                        parent_branch = b
                        break
                if parent_branch:
                    ancestry.append(parent_branch)
                    commit = parent_commit
                else:
                    break
            else:
                break
    except Exception:
        pass
    return ancestry

def print_context_summary():
    try:
        current_branch = get_current_branch()
    except Exception as e:
        print("[Error] gitリポジトリ外、またはブランチ情報取得失敗:", e)
        sys.exit(1)
    print("[Context Branch Highlighter]")
    print(f"現在注力すべきブランチ: {current_branch}")
    print("直近の編集ファイル:")
    try:
        files = get_recently_modified_files()
        now = datetime.now()
        for entry in files:
            ts = datetime.fromtimestamp(entry['timestamp'])
            delta = now - ts
            mins = int(delta.total_seconds() / 60)
            print(f"  - {entry['file']} ({mins}分前)")
    except Exception:
        print("  (取得不可)")
    try:
        rel = get_branch_relations(current_branch)
        print("関連ブランチ:")
        print(f"  - {rel['parent']} (親)")
        for sib in rel['siblings']:
            print(f"  - {sib} (兄弟)")
    except Exception:
        print("関連ブランチ情報取得不可")
    try:
        ancestry = get_branch_tree(current_branch)
        print("ブランチ分岐状況:")
        indent = "  "
        for i, b in enumerate(ancestry):
            if i == 0:
                print(f"  {b}", end="")
            else:
                print(f" ← {b}", end="")
        print("")
    except Exception:
        print("ブランチツリー取得不可")

def main():
    parser = argparse.ArgumentParser(description="Context Branch Highlighter - 作業コンテキストの可視化ツール")
    subparsers = parser.add_subparsers(dest='command')

    parser_summary = subparsers.add_parser('summary', help='現在の作業コンテキストを要約表示')
    parser_log = subparsers.add_parser('log', help='直近の編集ファイル一覧')
    parser_log.add_argument('--limit', type=int, default=10, help='表示件数')
    parser_list = subparsers.add_parser('list', help='全ブランチ一覧と分岐状況')

    args = parser.parse_args()
    if args.command == 'summary' or args.command is None:
        print_context_summary()
    elif args.command == 'log':
        try:
            files = get_recently_modified_files(limit=args.limit)
            now = datetime.now()
            for entry in files:
                ts = datetime.fromtimestamp(entry['timestamp'])
                delta = now - ts
                mins = int(delta.total_seconds() / 60)
                print(f"{entry['file']} ({mins}分前)")
        except Exception as e:
            print("[Error]", e)
    elif args.command == 'list':
        try:
            branches = run_git_command(['branch', '--format=%(refname:short)']).splitlines()
            print("全ブランチ:")
            for b in branches:
                print(f"  - {b}")
        except Exception as e:
            print("[Error]", e)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
