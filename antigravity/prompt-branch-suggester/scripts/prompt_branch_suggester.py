import argparse
import subprocess
import os
import sys
import json
from datetime import datetime

def get_current_branch():
    try:
        result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def get_latest_commit_message():
    try:
        result = subprocess.run(['git', 'log', '-1', '--pretty=%B'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def get_last_diff():
    try:
        result = subprocess.run(['git', 'diff', '--name-status', 'HEAD~1..HEAD'], capture_output=True, text=True, check=True)
        return result.stdout.strip().splitlines()
    except subprocess.CalledProcessError:
        return []

def suggest_prompt(branch, commit_msg, diff):
    suggestions = []
    # ブランチ名による分岐
    if branch.startswith('feature/'):
        suggestions.append({
            'file': 'SUGGESTED_CLAUDE.md',
            'content': f"## 指示分岐案\n- ブランチ: {branch}\n- 差分: {', '.join([d.split('\t')[-1] for d in diff if d])}\n- 推奨指示: 新機能追加に伴うコードレビューを優先してください。"
        })
    elif branch.startswith('hotfix/') or branch.startswith('fix/'):
        suggestions.append({
            'file': 'SUGGESTED_AGENTS.md',
            'content': f"- ブランチ: {branch}\n- 差分: {', '.join([d.split('\t')[-1] for d in diff if d])}\n- 推奨指示: 緊急バグ修正。テストカバレッジを重視し、最小限の変更で対応してください。"
        })
    elif 'refactor' in commit_msg.lower():
        suggestions.append({
            'file': 'SUGGESTED_CLAUDE.md',
            'content': f"## 指示分岐案\n- ブランチ: {branch}\n- 差分: {', '.join([d.split('\t')[-1] for d in diff if d])}\n- 推奨指示: コード構造の整理。既存機能の互換性維持に注意してください。"
        })
    elif len(diff) > 10:
        suggestions.append({
            'file': 'SUGGESTED_AGENTS.md',
            'content': f"- ブランチ: {branch}\n- 差分: {', '.join([d.split('\t')[-1] for d in diff if d])}\n- 推奨指示: 大規模な変更。段階的なレビューとテストを推奨します。"
        })
    else:
        suggestions.append({
            'file': 'SUGGESTED_CLAUDE.md',
            'content': f"## 指示分岐案\n- ブランチ: {branch}\n- 差分: {', '.join([d.split('\t')[-1] for d in diff if d])}\n- 推奨指示: 通常の作業。既存のワークフローに従ってください。"
        })
    return suggestions

def save_suggestions(suggestions, skill_dir):
    os.makedirs(skill_dir, exist_ok=True)
    for s in suggestions:
        path = os.path.join(skill_dir, s['file'])
        if os.path.exists(path):
            # 既存ファイルは上書きしない
            continue
        with open(path, 'w', encoding='utf-8') as f:
            f.write(s['content'])

def print_summary(branch, commit_msg, diff, suggestions):
    print(f"Current branch: {branch}")
    print(f"Latest commit message: {commit_msg}")
    print(f"Diff files: {', '.join([d.split('\t')[-1] for d in diff if d])}")
    print("\nSuggested prompt files:")
    for s in suggestions:
        print(f"- {s['file']}")

def main():
    parser = argparse.ArgumentParser(description='Prompt Branch Suggester')
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_suggest = subparsers.add_parser('suggest', help='Suggest prompt branch files')
    parser_suggest.add_argument('--skill-dir', type=str, default='.agent/skills/prompt-branch-suggester/', help='Skill output directory')

    parser_list = subparsers.add_parser('list', help='List suggested files')
    parser_list.add_argument('--skill-dir', type=str, default='.agent/skills/prompt-branch-suggester/', help='Skill output directory')

    parser_summary = subparsers.add_parser('summary', help='Show current branch and suggestion summary')
    parser_summary.add_argument('--skill-dir', type=str, default='.agent/skills/prompt-branch-suggester/', help='Skill output directory')

    args = parser.parse_args()

    if args.command == 'suggest':
        branch = get_current_branch()
        commit_msg = get_latest_commit_message()
        diff = get_last_diff()
        if not branch or not commit_msg:
            print('Error: Not a git repository or cannot get branch info.')
            sys.exit(1)
        suggestions = suggest_prompt(branch, commit_msg, diff)
        save_suggestions(suggestions, args.skill_dir)
        print_summary(branch, commit_msg, diff, suggestions)
    elif args.command == 'list':
        if not os.path.isdir(args.skill_dir):
            print('No suggestion files found.')
            sys.exit(0)
        files = [f for f in os.listdir(args.skill_dir) if f.startswith('SUGGESTED_') and f.endswith('.md')]
        if not files:
            print('No suggestion files found.')
        else:
            print('Suggestion files:')
            for f in files:
                print(f'- {f}')
    elif args.command == 'summary':
        branch = get_current_branch()
        commit_msg = get_latest_commit_message()
        diff = get_last_diff()
        suggestions = suggest_prompt(branch, commit_msg, diff)
        print_summary(branch, commit_msg, diff, suggestions)

if __name__ == '__main__':
    main()
