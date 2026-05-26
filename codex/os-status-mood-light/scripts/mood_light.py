import os
import sys
import argparse
import datetime
import json
import requests
from pathlib import Path

MOOD_MESSAGES = {
    '最高': ['絶好調！今日もバリバリ行きましょう。', 'やる気MAX。全力疾走。'],
    'だるい': ['本日省エネ運転。無理せずいきましょう。', 'やる気チャージ中。コーヒー推奨。'],
    'ねむい': ['睡眠は大事。仮眠推奨。', '目覚ましソング再生の時間です。'],
    '普通': ['平常運転です。', '特に波風なし。'],
    '楽しい': ['楽しい気分が伝わってきます！', 'その調子で！'],
    'つらい': ['無理せず休憩を。', '深呼吸してみましょう。'],
    '怒り': ['クールダウン推奨。', '落ち着いていきましょう。'],
    '悲しい': ['寄り添います。無理しないで。', '気分転換をおすすめします。'],
}

MOOD_LOG_PATH = Path.home() / '.os_status_mood_light_log.jsonl'

SLACK_DEFAULT_ICON = ':thought_balloon:'


def get_mood():
    mood = os.environ.get('MOOD', '普通')
    return mood

def set_mood(mood: str):
    os.environ['MOOD'] = mood
    return mood

def pick_message(mood: str):
    import random
    if mood in MOOD_MESSAGES:
        return random.choice(MOOD_MESSAGES[mood])
    else:
        return '今日も一日頑張りましょう。'

def log_mood(mood: str, message: str):
    now = datetime.datetime.now().isoformat()
    entry = {'timestamp': now, 'mood': mood, 'message': message}
    with open(MOOD_LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')

def show_mood():
    mood = get_mood()
    message = pick_message(mood)
    print(f'[os-status-mood-light] 気分: {mood}\n{message}')
    log_mood(mood, message)

def set_mood_cli(mood):
    set_mood(mood)
    show_mood()

def list_mood_logs(limit=10):
    if not MOOD_LOG_PATH.exists():
        print('ログがありません。')
        return
    with open(MOOD_LOG_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines[-limit:]:
        entry = json.loads(line)
        print(f"{entry['timestamp']} | {entry['mood']} | {entry['message']}")

def summary_mood():
    if not MOOD_LOG_PATH.exists():
        print('ログがありません。')
        return
    counts = {}
    with open(MOOD_LOG_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            entry = json.loads(line)
            mood = entry['mood']
            counts[mood] = counts.get(mood, 0) + 1
    print('気分別出現回数:')
    for mood, count in sorted(counts.items(), key=lambda x: -x[1]):
        print(f'{mood}: {count}回')

def send_slack_status(mood: str, message: str, webhook_url: str):
    payload = {
        'text': f'[os-status-mood-light] 気分: {mood}\n{message}',
        'icon_emoji': SLACK_DEFAULT_ICON
    }
    try:
        resp = requests.post(webhook_url, json=payload)
        if resp.status_code != 200:
            print(f'Slack通知失敗: {resp.status_code} {resp.text}')
        else:
            print('Slack通知成功')
    except Exception as e:
        print(f'Slack通知エラー: {e}')

def parse_args():
    parser = argparse.ArgumentParser(description='os-status-mood-light: 気分可視化スキル')
    subparsers = parser.add_subparsers(dest='command')

    show_parser = subparsers.add_parser('show', help='現在の気分を表示')
    show_parser.add_argument('--slack-webhook-url', type=str, help='Slack Webhook URLに通知')

    set_parser = subparsers.add_parser('set', help='気分を設定')
    set_parser.add_argument('--mood', type=str, required=True, help='設定する気分')
    set_parser.add_argument('--slack-webhook-url', type=str, help='Slack Webhook URLに通知')

    list_parser = subparsers.add_parser('list', help='気分ログを表示')
    list_parser.add_argument('--limit', type=int, default=10, help='表示件数')

    summary_parser = subparsers.add_parser('summary', help='気分の集計')

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'show':
        mood = get_mood()
        message = pick_message(mood)
        print(f'[os-status-mood-light] 気分: {mood}\n{message}')
        log_mood(mood, message)
        if args.slack_webhook_url:
            send_slack_status(mood, message, args.slack_webhook_url)
    elif args.command == 'set':
        set_mood(args.mood)
        message = pick_message(args.mood)
        print(f'[os-status-mood-light] 気分: {args.mood}\n{message}')
        log_mood(args.mood, message)
        if args.slack_webhook_url:
            send_slack_status(args.mood, message, args.slack_webhook_url)
    elif args.command == 'list':
        list_mood_logs(args.limit)
    elif args.command == 'summary':
        summary_mood()
    else:
        print('コマンドを指定してください。 --help でヘルプ表示')

if __name__ == '__main__':
    main()
