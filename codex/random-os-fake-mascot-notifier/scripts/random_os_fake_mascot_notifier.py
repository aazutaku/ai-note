import argparse
import random
import sys
import time
import threading
from datetime import datetime, timedelta
try:
    from plyer import notification
except ImportError:
    print('plyerライブラリが必要です。pip install plyer でインストールしてください。')
    sys.exit(1)

MASCOTS = [
    {
        'name': 'カーネルくん',
        'messages': [
            '今日もメモリリークしないようにね！',
            'カーネルパニックは突然やってくるよ！',
            'そのバグ、root権限で直してみよう！',
            'プロセス管理はお任せあれ！'
        ]
    },
    {
        'name': 'ビットちゃん',
        'messages': [
            'あなたの成功をビット単位で数えています。',
            '0と1の間にも無限の可能性があるよ！',
            'バイナリの世界から応援してる！',
            'ビット落ちしてない？休憩も大事だよ！'
        ]
    },
    {
        'name': 'メモリ犬',
        'messages': [
            '休憩しないとスワップしちゃうぞ！',
            'メモリクリアも大切だよ。',
            'RAM満タンでもがんばれ！',
            'キャッシュに頼りすぎないでね！'
        ]
    },
    {
        'name': 'タスクキャット',
        'messages': [
            'そのタスク、まだ終わってないよ！',
            'マルチタスクは猫の得意技！',
            '一つずつ片付けていこう！',
            'タスクキルは計画的に！'
        ]
    },
    {
        'name': 'パーミッションパンダ',
        'messages': [
            'もっと自分に許可をあげて！',
            'rootでやるのは危険だよ！',
            'アクセス権限は守ろうね。',
            'chmod 777はやめておこう！'
        ]
    },
    {
        'name': 'シグナルうさぎ',
        'messages': [
            'SIGKILLされる前に休憩しよう！',
            'シグナル送信中…やる気も送信中！',
            'プロセスに愛を送ります。',
            'Ctrl+Cで一息つこう！'
        ]
    },
    {
        'name': 'バッファフクロウ',
        'messages': [
            'バッファオーバーフローに注意！',
            '夜更かししすぎはバッファ不足の元。',
            'データはしっかり詰めてね。',
            'バッファリング中…あなたも休憩を！'
        ]
    }
]

MIN_INTERVAL = 600  # 最小通知間隔（秒）
MAX_INTERVAL = 2400 # 最大通知間隔（秒）

history = []


def random_mascot_message():
    mascot = random.choice(MASCOTS)
    msg = random.choice(mascot['messages'])
    return mascot['name'], msg


def send_notification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name='Random OS Mascot Notifier',
            timeout=8
        )
    except Exception as e:
        print(f'通知エラー: {e}')


def notify_once():
    mascot, msg = random_mascot_message()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    send_notification(f'{mascot}', msg)
    history.append({'time': timestamp, 'mascot': mascot, 'msg': msg})
    print(f'[{timestamp}] [{mascot}] {msg}')


def auto_notify_loop():
    while True:
        interval = random.randint(MIN_INTERVAL, MAX_INTERVAL)
        time.sleep(interval)
        notify_once()


def list_history(limit=10):
    for item in history[-limit:]:
        print(f"[{item['time']}] [{item['mascot']}] {item['msg']}")


def summary():
    count = len(history)
    mascot_count = {}
    for item in history:
        mascot_count[item['mascot']] = mascot_count.get(item['mascot'], 0) + 1
    print(f'通知総数: {count}')
    for mascot, c in mascot_count.items():
        print(f'  {mascot}: {c}回')


def parse_args():
    parser = argparse.ArgumentParser(description='Random OS Fake Mascot Notifier')
    subparsers = parser.add_subparsers(dest='command')

    parser_once = subparsers.add_parser('once', help='1回だけ通知を表示')
    parser_auto = subparsers.add_parser('auto', help='自動で定期的に通知')
    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_list.add_argument('--limit', type=int, default=10, help='表示件数')
    parser_summary = subparsers.add_parser('summary', help='通知履歴のサマリー')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'once':
        notify_once()
    elif args.command == 'auto':
        print('自動通知モード開始 (Ctrl+Cで終了)')
        try:
            notify_once()
            auto_notify_loop()
        except KeyboardInterrupt:
            print('\n自動通知を終了します')
    elif args.command == 'list':
        list_history(limit=getattr(args, 'limit', 10))
    elif args.command == 'summary':
        summary()
    else:
        print('コマンドを指定してください (once/auto/list/summary)')

if __name__ == '__main__':
    main()
