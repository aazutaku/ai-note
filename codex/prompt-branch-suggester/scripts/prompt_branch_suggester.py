import argparse
import os
import sys
import subprocess
import datetime
from typing import List, Tuple, Optional

try:
    import git
except ImportError:
    print("[ERROR] GitPython is required. Install with 'pip install GitPython'.")
    sys.exit(1)

def get_repo(path: str = '.') -> Optional[git.Repo]:
    try:
        repo = git.Repo(path, search_parent_directories=True)
        return repo
    except git.exc.InvalidGitRepositoryError:
        print("[ERROR] Not a git repository.")
        return None

def get_current_branch(repo: git.Repo) -> str:
    return repo.active_branch.name

def get_last_commit_message(repo: git.Repo) -> str:
    return repo.head.commit.message.strip()

def get_recent_diff(repo: git.Repo, num: int = 1) -> List[str]:
    try:
        commits = list(repo.iter_commits('HEAD', max_count=num+1))
        if len(commits) < 2:
            return []
        diff = commits[0].diff(commits[1], create_patch=True)
        diff_summaries = []
        for d in diff:
            if d.a_path and d.change_type:
                diff_summaries.append(f"{d.change_type.upper()}: {d.a_path}")
        return diff_summaries
    except Exception as e:
        print(f"[ERROR] Failed to get diff: {e}")
        return []

def suggest_instruction_file(branch: str, diff: List[str], commit_msg: str) -> Tuple[str, List[str]]:
    proposals = []
    branch_key = branch.replace('/', '-').replace('_', '-')
    if branch.startswith('feature/'):
        proposals.append(f"Create AGENTS.{branch_key}.md with feature-specific instructions.")
    elif branch.startswith('hotfix/') or 'fix' in branch.lower():
        proposals.append(f"Create CLAUDE.{branch_key}.md for hotfix context.")
    elif branch.startswith('release/'):
        proposals.append(f"Prepare AGENTS.{branch_key}.md for release QA checks.")
    elif branch.startswith('refactor') or 'refactor' in commit_msg.lower():
        proposals.append(f"Suggest AGENTS.{branch_key}.md with refactoring guidelines.")
    else:
        proposals.append(f"Temporary prompt set for branch {branch}.")
    temp_prompts = []
    if 'login' in branch.lower() or 'login' in commit_msg.lower():
        temp_prompts.append("Focus on input validation and error handling for login flow.")
        temp_prompts.append("Prioritize security best practices.")
    if any('test' in d.lower() for d in diff):
        temp_prompts.append("Ensure all new tests pass and cover edge cases.")
    if not temp_prompts:
        temp_prompts.append("Review code changes and update documentation as needed.")
    return proposals[0], temp_prompts

def save_suggestion_file(branch: str, proposal: str, prompts: List[str]):
    ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    fname = f"PROMPT_SUGGEST_{branch.replace('/', '-')}_{ts}.md"
    content = f"# Prompt Branch Suggestion\n\n## Proposal\n{proposal}\n\n## Temporary Prompts\n" + "\n".join(f"- {p}" for p in prompts)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[INFO] Suggestion file saved: {fname}")

def cli_suggest(args):
    repo = get_repo()
    if not repo:
        sys.exit(1)
    branch = get_current_branch(repo)
    commit_msg = get_last_commit_message(repo)
    diff = get_recent_diff(repo)
    print(f"[INFO] Detected branch: {branch}")
    print(f"[INFO] Recent diff: {', '.join(diff) if diff else 'No recent changes.'}")
    proposal, prompts = suggest_instruction_file(branch, diff, commit_msg)
    print(f"[PROPOSAL] {proposal}")
    print("[PROPOSAL] Temporary prompt set:")
    for p in prompts:
        print(f"- {p}")
    if args.save:
        save_suggestion_file(branch, proposal, prompts)

def cli_list(args):
    files = [f for f in os.listdir('.') if f.startswith('PROMPT_SUGGEST_') and f.endswith('.md')]
    if not files:
        print("[INFO] No suggestion files found.")
        return
    for fname in sorted(files):
        print(f"- {fname}")

def cli_summary(args):
    files = [f for f in os.listdir('.') if f.startswith('PROMPT_SUGGEST_') and f.endswith('.md')]
    if not files:
        print("[INFO] No suggestion files found.")
        return
    for fname in sorted(files):
        print(f"\n# {fname}")
        with open(fname, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[:10]:
                print(line.strip())
            if len(lines) > 10:
                print("...")

def main():
    parser = argparse.ArgumentParser(description='Prompt Branch Suggester Skill')
    subparsers = parser.add_subparsers(dest='command')
    suggest_parser = subparsers.add_parser('suggest', help='Suggest prompt branch instructions')
    suggest_parser.add_argument('--save', action='store_true', help='Save suggestion to file')
    list_parser = subparsers.add_parser('list', help='List saved suggestion files')
    summary_parser = subparsers.add_parser('summary', help='Show summary of suggestion files')
    args = parser.parse_args()
    if args.command == 'suggest':
        cli_suggest(args)
    elif args.command == 'list':
        cli_list(args)
    elif args.command == 'summary':
        cli_summary(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
