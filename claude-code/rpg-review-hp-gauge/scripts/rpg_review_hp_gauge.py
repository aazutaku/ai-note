import argparse
import sys
import os
import requests
import math

def get_review_comments(owner, repo, pr_number, github_token):
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github+json'
    }
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/comments'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f'GitHub API error: {response.status_code} {response.text}')
    comments = response.json()
    return len(comments)

def get_pr_title(owner, repo, pr_number, github_token):
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github+json'
    }
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f'GitHub API error: {response.status_code} {response.text}')
    pr = response.json()
    return pr.get('title', f'PR #{pr_number}')

def calc_hp(total_hp, num_comments, damage_per_comment):
    hp = max(0, total_hp - num_comments * damage_per_comment)
    return hp

def render_hp_gauge(hp, total_hp, gauge_length=20):
    filled = int((hp / total_hp) * gauge_length) if total_hp > 0 else 0
    empty = gauge_length - filled
    return '[' + '■' * filled + '□' * empty + f'] {hp}/{total_hp}'

def hp_status_message(hp, total_hp):
    if hp == 0:
        return '力尽きた...'
    elif hp < total_hp * 0.3:
        return 'HPがピンチ！'
    elif hp < total_hp * 0.7:
        return 'まだまだ戦える！'
    else:
        return '余裕の戦い！'

def print_report(pr_number, pr_title, num_comments, hp, total_hp):
    print('=== RPG Review HP Gauge ===')
    print(f'Pull Request: #{pr_number} - {pr_title}')
    print(f'指摘数: {num_comments}')
    print(f'HP: {render_hp_gauge(hp, total_hp)}')
    print(f'状態: {hp_status_message(hp, total_hp)}')
    print('-' * 29)

def main():
    parser = argparse.ArgumentParser(description='RPG風HPゲージでPRレビュー指摘数を可視化')
    parser.add_argument('--pr', type=int, nargs='+', required=True, help='Pull Request番号(複数可)')
    parser.add_argument('--repo', type=str, required=True, help='リポジトリ (owner/repo)')
    parser.add_argument('--total-hp', type=int, default=100, help='初期HP (デフォルト: 100)')
    parser.add_argument('--damage', type=int, default=2, help='指摘1件あたりのHP減少量 (デフォルト: 2)')
    parser.add_argument('--token', type=str, default=None, help='GitHubアクセストークン (環境変数GITHUB_TOKENでも可)')
    parser.add_argument('--markdown', action='store_true', help='Markdown形式で出力')
    args = parser.parse_args()

    github_token = args.token or os.environ.get('GITHUB_TOKEN')
    if not github_token:
        print('Error: GitHubアクセストークンが必要です (--token または環境変数GITHUB_TOKEN)')
        sys.exit(1)

    owner_repo = args.repo.split('/')
    if len(owner_repo) != 2:
        print('Error: --repoは owner/repo 形式で指定してください')
        sys.exit(1)
    owner, repo = owner_repo

    reports = []
    for pr_number in args.pr:
        try:
            num_comments = get_review_comments(owner, repo, pr_number, github_token)
            pr_title = get_pr_title(owner, repo, pr_number, github_token)
            hp = calc_hp(args.total_hp, num_comments, args.damage)
            reports.append({
                'pr': pr_number,
                'title': pr_title,
                'comments': num_comments,
                'hp': hp
            })
        except Exception as e:
            print(f'PR #{pr_number} の取得に失敗: {e}', file=sys.stderr)
            continue

    if args.markdown:
        print('### RPG Review HP Gauge')
        for r in reports:
            print(f'- **PR #{r["pr"]}**: {r["title"]}')
            print(f'  - 指摘数: {r["comments"]}')
            print(f'  - HP: `{render_hp_gauge(r["hp"], args.total_hp)}`')
            print(f'  - 状態: {hp_status_message(r["hp"], args.total_hp)}')
            print('')
    else:
        for r in reports:
            print_report(r['pr'], r['title'], r['comments'], r['hp'], args.total_hp)

if __name__ == '__main__':
    main()
