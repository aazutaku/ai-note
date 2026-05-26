import os
import sys
import json
import argparse
import datetime
import random
import requests
from pathlib import Path

MOOD_MAP = {
    '最高': {'status': '絶好調', 'msg': '今日もバリバリいきましょう！'},
    'だるい': {'status': '本日省エネ運転', 'msg': '無理せずいきましょう。'},
    '普通': {'status': '平常運転', 'msg': 'いつも通りです。'},
    '眠い': {'status': '仮眠推奨', 'msg': 'ちょっと休憩しましょう。'},
    '怒り': {'status': '要注意', 'msg': '深呼吸しましょう。'},
    '楽しい': {'status': 'ノリノリ', 'msg': '楽しんでます！'},
    '悲しい': {'status': 'しんみり', 'msg': '気分転換しましょう。'},
}

NEGA_TSUKKOMI = [
    'そろそろコーヒータイム？',
    'リフレッシュも大事です。',
    '一息つきませんか？',
    '今日は早めに切り上げましょう。',
    '無理は禁物ですよ。',
]

DAILY_NEWS = [
    '6月の開発者は梅雨に負けない',
    '本日のバグは気分次第',
    '新しいAPIと新しい気分',
    '今日の小ネタ: ステータスバーで自己主張',
    'Slackにも気分を伝えよう',
]

LOCAL_STATE_PATH = Path.home() / '.os_status_mood_light.json'


def get_current_mood():
    mood = os.environ.get('MOOD', None)
    if mood:
        return mood
    if LOCAL_STATE_PATH.exists():
        try:
            with open(LOCAL_STATE_PATH, 'r') as f:
                data = json.load(f)
                return data.get('mood', '普通')
        except Exception:
            return '普通'
    return '普通'


def set_local_mood(mood):
    data = {
        'mood': mood,
        'updated': datetime.datetime.now().isoformat()
    }
    try:
        with open(LOCAL_STATE_PATH, 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f'ローカル保存失敗: {e}')


def get_status_message(mood):
    info = MOOD_MAP.get(mood, MOOD_MAP['普通'])
    status = info['status']
    msg = info['msg']
    today = datetime.date.today().toordinal()
    daily = DAILY_NEWS[today % len(DAILY_NEWS)]
    if mood == 'だるい' or mood == '眠い' or mood == '悲しい':
        tsukkomi = random.choice(NEGA_TSUKKOMI)
    else:
        tsukkomi = ''
    return status, msg, daily, tsukkomi


def show_status():
    mood = get_current_mood()
    status, msg, daily, tsukkomi = get_status_message(mood)
    print(f'[{status}] {msg}')
    print(f'（本日のネタ: {daily}）')
    if tsukkomi:
        print(f'（ツッコミ: {tsukkomi}）')


def set_status(mood, slack=False):
    set_local_mood(mood)
    os.environ['MOOD'] = mood
    print(f'気分を「{mood}」に設定しました。')
    if slack:
        slack_token = os.environ.get('SLACK_TOKEN')
        if not slack_token:
            print('Slack連携にはSLACK_TOKEN環境変数が必要です。')
            return
        status, msg, _, _ = get_status_message(mood)
        set_slack_status(status, msg, slack_token)


def set_slack_status(status, msg, token):
    profile = {
        'status_text': f'{status}: {msg}',
        'status_emoji': ':speech_balloon:',
        'status_expiration': 0
    }
    url = 'https://slack.com/api/users.profile.set'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json; charset=utf-8'
    }
    payload = {'profile': profile}
    try:
        r = requests.post(url, headers=headers, json=payload)
        if r.status_code == 200 and r.json().get('ok'):
            print('Slackステータスを更新しました。')
        else:
            print(f'Slack更新失敗: {r.text}')
    except Exception as e:
        print(f'Slack APIエラー: {e}')


def list_moods():
    print('利用可能な気分:')
    for k in MOOD_MAP:
        print(f'  {k}: {MOOD_MAP[k]["status"]} - {MOOD_MAP[k]["msg"]}')


def main():
    parser = argparse.ArgumentParser(description='os-status-mood-light: 気分をOSやSlackに可視化')
    subparsers = parser.add_subparsers(dest='command')

    set_parser = subparsers.add_parser('set', help='気分を設定')
    set_parser.add_argument('--mood', required=True, help='気分（最高, だるい, 普通, 眠い, 怒り, 楽しい, 悲しい）')
    set_parser.add_argument('--slack', action='store_true', help='Slackステータスも更新')

    show_parser = subparsers.add_parser('show', help='現在の気分を表示')
    list_parser = subparsers.add_parser('list', help='利用可能な気分一覧')

    args = parser.parse_args()

    if args.command == 'set':
        mood = args.mood
        if mood not in MOOD_MAP:
            print(f'未定義の気分: {mood}')
            list_moods()
            sys.exit(1)
        set_status(mood, slack=args.slack)
    elif args.command == 'show':
        show_status()
    elif args.command == 'list':
        list_moods()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
