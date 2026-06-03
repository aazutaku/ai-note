import argparse
import sys
import requests
import os
import math

def get_github_pr_comments(repo, pr_number, token):
    headers = {'Authorization': f'token {token}'}
    comments = []
    page = 1
    while True:
        url = f'https://api.github.com/repos/{repo}/pulls/{pr_number}/comments?page={page}&per_page=100'
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            raise Exception(f'GitHub API error: {resp.status_code} {resp.text}')
        data = resp.json()
        if not data:
            break
        for c in data:
            if c.get('user', {}).get('type') != 'Bot':
                comments.append(c['body'])
        page += 1
    return comments

def get_gitlab_pr_comments(project_id, mr_iid, token):
    headers = {'PRIVATE-TOKEN': token}
    comments = []
    page = 1
    while True:
        url = f'https://gitlab.com/api/v4/projects/{project_id}/merge_requests/{mr_iid}/notes?page={page}&per_page=100'
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            raise Exception(f'GitLab API error: {resp.status_code} {resp.text}')
        data = resp.json()
        if not data:
            break
        for c in data:
            if not c.get('system', False):
                comments.append(c['body'])
        page += 1
    return comments

def calc_hp(num_comments, max_hp=100, damage_per_comment=10):
    hp = max_hp - num_comments * damage_per_comment
    return max(0, hp)

def render_hp_bar(hp, max_hp, bar_length=10):
    filled = int(bar_length * hp / max_hp)
    empty = bar_length - filled
    return '[' + '█' * filled + '-' * empty + f'] {hp}/{max_hp}'

def summarize_comments(comments, max_lines=5):
    lines = []
    for c in comments[:max_lines]:
        first_line = c.strip().split('\n')[0]
        lines.append(f'- {first_line}')
    if len(comments) > max_lines:
        lines.append('...')
    return '\n'.join(lines)

def analyze_github(args):
    token = args.token or os.environ.get('GITHUB_TOKEN')
    if not token:
        print('Error: GitHub token required (--token or GITHUB_TOKEN env)')
        sys.exit(1)
    try:
        comments = get_github_pr_comments(args.repo, args.pr, token)
    except Exception as e:
        print(f'API error: {e}')
        sys.exit(1)
    num_comments = len(comments)
    hp = calc_hp(num_comments, args.max_hp, args.damage)
    bar = render_hp_bar(hp, args.max_hp)
    print(f'[PR #{args.pr}] コードレビューHPゲージ')
    print(f'HP: {bar}')
    print(f'指摘数: {num_comments} (HP -{num_comments*args.damage})')
    print('コメント:')
    print(summarize_comments(comments))
    if hp == 0:
        print('あなたのコードは力尽きた...')
    elif hp < args.max_hp // 2:
        print('あなたのコードは半分の体力を失いました！')

def analyze_gitlab(args):
    token = args.token or os.environ.get('GITLAB_TOKEN')
    if not token:
        print('Error: GitLab token required (--token or GITLAB_TOKEN env)')
        sys.exit(1)
    try:
        comments = get_gitlab_pr_comments(args.project_id, args.mr, token)
    except Exception as e:
        print(f'API error: {e}')
        sys.exit(1)
    num_comments = len(comments)
    hp = calc_hp(num_comments, args.max_hp, args.damage)
    bar = render_hp_bar(hp, args.max_hp)
    print(f'[MR !{args.mr}] コードレビューHPゲージ')
    print(f'HP: {bar}')
    print(f'指摘数: {num_comments} (HP -{num_comments*args.damage})')
    print('コメント:')
    print(summarize_comments(comments))
    if hp == 0:
        print('あなたのコードは力尽きた...')
    elif hp < args.max_hp // 2:
        print('あなたのコードは半分の体力を失いました！')

def main():
    parser = argparse.ArgumentParser(description='RPG風コードレビューHPゲージ')
    subparsers = parser.add_subparsers(dest='cmd')

    gh = subparsers.add_parser('github', help='GitHub PRのHPゲージ表示')
    gh.add_argument('--repo', required=True, help='org/repo 形式')
    gh.add_argument('--pr', type=int, required=True, help='PR番号')
    gh.add_argument('--token', help='GitHub APIトークン')
    gh.add_argument('--max-hp', type=int, default=100, help='最大HP')
    gh.add_argument('--damage', type=int, default=10, help='指摘1件あたりのHP減少')
    gh.set_defaults(func=analyze_github)

    gl = subparsers.add_parser('gitlab', help='GitLab MRのHPゲージ表示')
    gl.add_argument('--project-id', required=True, help='GitLabプロジェクトID')
    gl.add_argument('--mr', type=int, required=True, help='MR番号')
    gl.add_argument('--token', help='GitLab APIトークン')
    gl.add_argument('--max-hp', type=int, default=100, help='最大HP')
    gl.add_argument('--damage', type=int, default=10, help='指摘1件あたりのHP減少')
    gl.set_defaults(func=analyze_gitlab)

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        sys.exit(0)
    args.func(args)

if __name__ == '__main__':
    main()
