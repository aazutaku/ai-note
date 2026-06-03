import argparse
import json
import os
import sys
from datetime import datetime

data_dir = os.path.join(os.path.dirname(__file__), 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

def load_reviews():
    path = os.path.join(data_dir, 'reviews.json')
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_reviews(reviews):
    path = os.path.join(data_dir, 'reviews.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)

def calc_hp(num_issues, max_hp=100, issue_per_hp=5):
    hp = max_hp - num_issues * issue_per_hp
    hp = max(0, min(max_hp, hp))
    return hp

def hp_bar(hp, max_hp=100, bar_len=10):
    filled = int(bar_len * hp / max_hp)
    bar = '█' * filled + '░' * (bar_len - filled)
    return f'[{bar}] {hp}/{max_hp}'

def log_review(pr_id, num_issues, reviewer, max_hp=100, issue_per_hp=5):
    reviews = load_reviews()
    hp = calc_hp(num_issues, max_hp, issue_per_hp)
    entry = {
        'timestamp': datetime.now().isoformat(),
        'pr_id': pr_id,
        'num_issues': num_issues,
        'reviewer': reviewer,
        'hp': hp,
        'max_hp': max_hp
    }
    reviews.append(entry)
    save_reviews(reviews)
    return entry

def list_reviews():
    reviews = load_reviews()
    if not reviews:
        print('No review logs found.')
        return
    for r in reviews:
        print(f"PR: {r['pr_id']} | 指摘数: {r['num_issues']} | HP: {r['hp']}/{r['max_hp']} | Reviewer: {r['reviewer']} | {r['timestamp']}")

def summary():
    reviews = load_reviews()
    if not reviews:
        print('No review logs found.')
        return
    total = len(reviews)
    avg_issues = sum([r['num_issues'] for r in reviews]) / total
    avg_hp = sum([r['hp'] for r in reviews]) / total
    print(f'レビュー記録数: {total}')
    print(f'平均指摘数: {avg_issues:.2f}')
    print(f'平均残HP: {avg_hp:.2f}')

def show_gauge(num_issues, max_hp=100, issue_per_hp=5):
    hp = calc_hp(num_issues, max_hp, issue_per_hp)
    bar = hp_bar(hp, max_hp)
    print(f'[HPゲージ] あなたのコードの体力: {bar}')
    print(f'指摘数: {num_issues} (最大HP: {max_hp})')
    if hp == 0:
        print('力尽きた... 次回の冒険に期待しよう！')

def parse_args():
    parser = argparse.ArgumentParser(description='RPG風コードレビューHPゲージ')
    subparsers = parser.add_subparsers(dest='command')

    log_parser = subparsers.add_parser('log', help='レビュー指摘数を記録')
    log_parser.add_argument('--pr', required=True, help='PR ID')
    log_parser.add_argument('--issues', type=int, required=True, help='指摘数')
    log_parser.add_argument('--reviewer', required=True, help='レビュワー名')
    log_parser.add_argument('--max-hp', type=int, default=100, help='最大HP')
    log_parser.add_argument('--issue-per-hp', type=int, default=5, help='指摘1件あたりHP減少量')

    list_parser = subparsers.add_parser('list', help='レビュー履歴を一覧表示')
    summary_parser = subparsers.add_parser('summary', help='レビュー履歴のサマリー表示')

    gauge_parser = subparsers.add_parser('gauge', help='HPゲージを表示')
    gauge_parser.add_argument('--issues', type=int, required=True, help='指摘数')
    gauge_parser.add_argument('--max-hp', type=int, default=100, help='最大HP')
    gauge_parser.add_argument('--issue-per-hp', type=int, default=5, help='指摘1件あたりHP減少量')

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'log':
        entry = log_review(args.pr, args.issues, args.reviewer, args.max_hp, args.issue_per_hp)
        print('レビュー記録を保存しました:')
        bar = hp_bar(entry['hp'], entry['max_hp'])
        print(f'[HPゲージ] あなたのコードの体力: {bar}')
        print(f'指摘数: {entry["num_issues"]} (最大HP: {entry["max_hp"]})')
        if entry['hp'] == 0:
            print('力尽きた... 次回の冒険に期待しよう！')
    elif args.command == 'list':
        list_reviews()
    elif args.command == 'summary':
        summary()
    elif args.command == 'gauge':
        show_gauge(args.issues, args.max_hp, args.issue_per_hp)
    else:
        print('コマンドを指定してください (log, list, summary, gauge)')

if __name__ == '__main__':
    main()
