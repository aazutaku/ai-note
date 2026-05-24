import argparse
import subprocess
import sys
import os
from typing import List, Tuple

def run_git_diff(cached: bool = False, paths: List[str] = None) -> str:
    cmd = ['git', 'diff']
    if cached:
        cmd.append('--cached')
    if paths:
        cmd += paths
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running git diff: {e.stderr}", file=sys.stderr)
        sys.exit(1)

def parse_diff(diff_text: str) -> List[Tuple[str, str]]:
    # Returns list of (filename, diff_chunk)
    files = []
    current_file = None
    current_chunk = []
    for line in diff_text.splitlines():
        if line.startswith('diff --git'):
            if current_file and current_chunk:
                files.append((current_file, '\n'.join(current_chunk)))
            parts = line.split(' ')
            # e.g., diff --git a/foo.py b/foo.py
            if len(parts) >= 4:
                current_file = parts[2][2:]  # strip 'a/'
            else:
                current_file = None
            current_chunk = [line]
        else:
            if current_file is not None:
                current_chunk.append(line)
    if current_file and current_chunk:
        files.append((current_file, '\n'.join(current_chunk)))
    return files

def summarize_diff_chunks(diff_chunks: List[Tuple[str, str]]) -> Tuple[List[str], List[str]]:
    # This is a simple heuristic summary; in production, call Claude API here
    major_changes = []
    impacts = set()
    for filename, chunk in diff_chunks:
        added = sum(1 for l in chunk.splitlines() if l.startswith('+') and not l.startswith('+++'))
        removed = sum(1 for l in chunk.splitlines() if l.startswith('-') and not l.startswith('---'))
        if added or removed:
            major_changes.append(f"- {filename}: {added}行追加, {removed}行削除")
            if filename.endswith('.py') or filename.endswith('.js'):
                impacts.add("コードロジックの変更")
            elif filename.endswith('.md'):
                impacts.add("ドキュメント更新")
            elif filename.startswith('tests/'):
                impacts.add("テストケースの追加/修正")
    return major_changes, list(impacts)

def print_summary(major_changes: List[str], impacts: List[str]):
    print("主要な変更点:")
    if major_changes:
        for line in major_changes:
            print(line)
    else:
        print("- 変更点なし")
    print("影響範囲:")
    if impacts:
        for line in impacts:
            print(f"- {line}")
    else:
        print("- 特筆すべき影響なし")

def main():
    parser = argparse.ArgumentParser(description="コミット差分をAIで要約するツール")
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_summary = subparsers.add_parser('summary', help='現在のdiffを要約')
    parser_summary.add_argument('--cached', action='store_true', help='git diff --cachedでステージ済み差分を要約')
    parser_summary.add_argument('paths', nargs='*', help='要約対象のファイル/ディレクトリ')

    parser_show = subparsers.add_parser('show', help='現在のdiffを表示')
    parser_show.add_argument('--cached', action='store_true', help='git diff --cachedでステージ済み差分を表示')
    parser_show.add_argument('paths', nargs='*', help='表示対象のファイル/ディレクトリ')

    args = parser.parse_args()

    if args.command == 'summary':
        diff = run_git_diff(cached=args.cached, paths=args.paths)
        if not diff.strip():
            print("差分がありません。コミット予定の変更がありません。")
            sys.exit(0)
        diff_chunks = parse_diff(diff)
        major_changes, impacts = summarize_diff_chunks(diff_chunks)
        print_summary(major_changes, impacts)
    elif args.command == 'show':
        diff = run_git_diff(cached=args.cached, paths=args.paths)
        print(diff)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
