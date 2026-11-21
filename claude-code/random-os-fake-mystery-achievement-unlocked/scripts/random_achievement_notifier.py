import sys
import time
import random
import argparse
import threading
import os

try:
    import notify2
except ImportError:
    notify2 = None

ACHIEVEMENTS = [
    {
        'title': 'Ctrl+C連打名人',
        'desc': 'たった今、Ctrl+Cを5回連打しました。あなたの指はもう止められません。'
    },
    {
        'title': '5分間マウス未使用',
        'desc': 'マウスを5分間一切動かさずに作業しました。集中力の化身です。'
    },
    {
        'title': 'このコマンド誰も使ってない王',
        'desc': '誰も使っていない謎コマンドを実行しました。孤高のパイオニアです。'
    },
    {
        'title': '謎の引数職人',
        'desc': 'コマンドに意味不明な引数を付けて実行しました。想像力が暴走しています。'
    },
    {
        'title': '一発成功伝説',
        'desc': '何も調べずにコマンドを一発で成功させました。運と勘の申し子です。'
    },
    {
        'title': 'タイポの帝王',
        'desc': 'コマンドを3回連続でタイプミスしました。指が迷走しています。'
    },
    {
        'title': 'コピペ忍者',
        'desc': '1分間に5回以上コピペを繰り返しました。手癖が光ります。'
    },
    {
        'title': '謎の沈黙',
        'desc': '10分間何も入力せずに放置しました。深い思索中？'
    },
    {
        'title': '一人ビルド祭り',
        'desc': '1時間で10回以上ビルドしました。ビルドの鬼です。'
    },
    {
        'title': 'lsマスター',
        'desc': 'lsコマンドを1分間に5回以上叩きました。ファイルの所在に敏感です。'
    },
    {
        'title': 'rmコマンド恐怖症',
        'desc': 'rmコマンドを実行しようとして躊躇しました。慎重派です。'
    },
    {
        'title': '謎のエラーコレクター',
        'desc': '1分間に3回以上エラーを発生させました。エラーの申し子です。'
    },
    {
        'title': 'README信者',
        'desc': 'README.mdを10回以上開きました。説明書大好きです。'
    },
    {
        'title': 'git add忘れ王',
        'desc': 'git commit時にファイルをaddし忘れました。うっかり屋です。'
    },
    {
        'title': '謎のパスジャンパー',
        'desc': 'cdコマンドで3連続ディレクトリ移動しました。移動の達人です。'
    }
]

NOTIFY_TITLE = 'OS Achievement Unlocked!'


def can_notify():
    if notify2 is None:
        return False
    try:
        notify2.init('random-os-fake-mystery-achievement-unlocked')
        return True
    except Exception:
        return False


def send_notification(title, message):
    if can_notify():
        n = notify2.Notification(title, message)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.show()
    else:
        print(f'[{title}]\n{message}\n')


def random_achievement():
    ach = random.choice(ACHIEVEMENTS)
    return ach['title'], ach['desc']


def notify_once():
    title, desc = random_achievement()
    send_notification(NOTIFY_TITLE, f'称号: {title}\n説明: {desc}')


def random_interval_notifier(min_sec=120, max_sec=600, stop_event=None):
    while True:
        interval = random.randint(min_sec, max_sec)
        for _ in range(interval):
            if stop_event and stop_event.is_set():
                return
            time.sleep(1)
        notify_once()


def list_achievements():
    for ach in ACHIEVEMENTS:
        print(f"- {ach['title']}: {ach['desc']}")


def summary():
    print(f"登録済み称号数: {len(ACHIEVEMENTS)}")
    print("例:")
    for ach in random.sample(ACHIEVEMENTS, min(3, len(ACHIEVEMENTS))):
        print(f"  ・{ach['title']} - {ach['desc']}")


def main():
    parser = argparse.ArgumentParser(description='謎のOS実績解除通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('notify', help='ランダムな実績通知を即時表示')
    subparsers.add_parser('list', help='全実績一覧を表示')
    subparsers.add_parser('summary', help='実績サマリーを表示')
    subparsers.add_parser('daemon', help='ランダム間隔で自動通知 (Ctrl+Cで停止)')

    args = parser.parse_args()

    if args.command == 'notify':
        notify_once()
    elif args.command == 'list':
        list_achievements()
    elif args.command == 'summary':
        summary()
    elif args.command == 'daemon':
        stop_event = threading.Event()
        try:
            print('謎の実績解除通知デーモンを開始します (Ctrl+Cで停止)')
            random_interval_notifier(stop_event=stop_event)
        except KeyboardInterrupt:
            stop_event.set()
            print('\nデーモンを停止しました')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
