import random
import time
import argparse
import sys
import threading
from datetime import datetime, timedelta
try:
    from plyer import notification
except ImportError:
    print('plyerパッケージが必要です。pip install plyer でインストールしてください。')
    sys.exit(1)

MASCOTS = [
    {
        'name': 'カーネルくん',
        'messages': [
            'システムの裏側から君を応援してるよ！',
            '今日もプロセス管理は完璧だね。',
            'カーネルパニックは気にしないで！',
            '再起動しても君の努力は消えないよ。'
        ]
    },
    {
        'name': 'ビットちゃん',
        'messages': [
            'ビットの海であなたの成功を祈っています。',
            '0と1の間にも無限の可能性があるよ。',
            'ビット落ちしないように休憩してね。',
            'あなたの努力、全部見えてるよ！'
        ]
    },
    {
        'name': 'メモリ犬',
        'messages': [
            'メモリの片隅で見守っています。休憩も大事！',
            'ガーベジコレクションは任せて！',
            'メモリリークにはご用心。',
            '君のRAMはいつもフル稼働だね。'
        ]
    },
    {
        'name': 'タスクキャット',
        'messages': [
            'タスク管理は計画的に。たまには深呼吸。',
            'マルチタスクは猫の手も借りたい。',
            'ToDoリスト、もう一度見直してみては？',
            '休憩時間もスケジュールに入れよう！'
        ]
    },
    {
        'name': 'バグバード',
        'messages': [
            'バグは友達、怖くないよ！',
            'バグ退治は焦らずじっくり。',
            '今日もどこかでバグが羽ばたいています。',
            'バグを見つけたら褒めてあげよう。'
        ]
    },
    {
        'name': 'アップデートパンダ',
        'messages': [
            'アップデートは計画的に。',
            '最新バージョンで快適作業！',
            'たまには再起動も大切です。',
            'アップデート通知、見逃さないでね。'
        ]
    },
    {
        'name': 'プロセスモール',
        'messages': [
            'プロセスの流れに身を任せて。',
            '時にはプロセスをkillする勇気も必要。',
            'forkして新しい自分を発見！',
            'プロセス管理の達人だね。'
        ]
    },
    {
        'name': 'ログリス',
        'messages': [
            'ログは嘘をつかない。',
            'エラーログも大切な仲間。',
            'たまにはログを眺めてみては？',
            'ログに人生を刻もう。'
        ]
    }
]

NOTIFY_INTERVAL_MIN = 900  # 15分
NOTIFY_INTERVAL_MAX = 3600 # 1時間

HISTORY = []


def pick_random_mascot():
    mascot = random.choice(MASCOTS)
    message = random.choice(mascot['messages'])
    return mascot['name'], message


def show_notification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name='Random OS Mascot Notifier',
            timeout=8
        )
        return True
    except Exception as e:
        print(f'通知エラー: {e}')
        return False


def notify_once():
    mascot, msg = pick_random_mascot()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    show_notification(f'{mascot}', msg)
    HISTORY.append({'time': now, 'mascot': mascot, 'message': msg})
    print(f'[通知] {mascot}: {msg}')


def notify_loop():
    while True:
        interval = random.randint(NOTIFY_INTERVAL_MIN, NOTIFY_INTERVAL_MAX)
        notify_once()
        time.sleep(interval)


def list_history():
    if not HISTORY:
        print('通知履歴はありません。')
        return
    for item in HISTORY:
        print(f"[{item['time']}] {item['mascot']}: {item['message']}")


def summary():
    from collections import Counter
    mascot_counts = Counter([h['mascot'] for h in HISTORY])
    print('通知マスコット出現回数:')
    for mascot, count in mascot_counts.items():
        print(f'{mascot}: {count}回')


def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Mascot Notifier')
    subparsers = parser.add_subparsers(dest='command', help='サブコマンド')

    parser_log = subparsers.add_parser('log', help='1回だけ通知を表示')
    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='マスコット出現回数を集計')
    parser_daemon = subparsers.add_parser('daemon', help='定期的に通知を自動表示')

    args = parser.parse_args()

    if args.command == 'log':
        notify_once()
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    elif args.command == 'daemon' or args.command is None:
        print('マスコット通知デーモンを開始します。Ctrl+Cで終了。')
        try:
            notify_loop()
        except KeyboardInterrupt:
            print('\n終了します。')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
