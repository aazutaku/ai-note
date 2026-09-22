import sys
import argparse
import random
import time
import threading
import platform
import os

try:
    from plyer import notification
except ImportError:
    notification = None

HEROES = [
    {'name': 'バグスレイヤー・アリス', 'title': '伝説のデバッグ勇者'},
    {'name': 'コマンド使いのジョン', 'title': 'CLIの達人'},
    {'name': 'rootの精霊', 'title': 'システムの守護者'},
    {'name': 'Gitマスター・ミカ', 'title': 'バージョン管理の魔術師'},
    {'name': 'コンパイルの賢者', 'title': 'ビルドの導師'},
    {'name': 'シェルの忍者・サトシ', 'title': '自動化の忍者'},
    {'name': 'メモリの妖精・ユイ', 'title': 'RAMの守護者'},
    {'name': 'ネットワークの勇者・リナ', 'title': '通信の魔導士'},
    {'name': 'パッチ職人・ケン', 'title': '修正の名匠'},
    {'name': 'デプロイ王・レイ', 'title': '本番環境の覇者'}
]

MESSAGES = [
    '{title}「{name}」が参上しました！',
    '“{name}”がバグ退治に出動します。',
    '{title}「{name}」がログインしました。',
    '{title}「{name}」が召喚されました。',
    '{title}からのメッセージ: “焦らず進もう！”',
    '{title}「{name}」があなたの作業を見守っています。',
    '{title}「{name}」が新たなバグを検知しました。',
    '{title}「{name}」がコマンド入力をサポートします。',
    '{title}「{name}」がシステムに加わりました。',
    '{title}「{name}」がログを監視中です。'
]

TRIGGER_KEYWORDS = [
    '寂しい', '集中力が切れた', 'バグが倒せない', '助けて', 'つらい', 'もうだめ', 'やる気が出ない', '孤独', '眠い'
]

def show_notification(message):
    if notification:
        notification.notify(
            title='OS英雄召喚',
            message=message,
            app_name='FakeITHeroSummon',
            timeout=7
        )
    else:
        # Fallback: print to terminal
        print('[OS通知]', message)


def random_hero_message():
    hero = random.choice(HEROES)
    template = random.choice(MESSAGES)
    return template.format(name=hero['name'], title=hero['title'])


def summon_hero():
    message = random_hero_message()
    show_notification(message)
    return message


def listen_for_keywords():
    # Placeholder: In an actual agent, this would hook into semantic triggers
    pass


def random_timed_summon(min_sec=900, max_sec=3600, stop_event=None):
    # By default, triggers every 15-60min
    while not (stop_event and stop_event.is_set()):
        wait_time = random.randint(min_sec, max_sec)
        for _ in range(wait_time):
            if stop_event and stop_event.is_set():
                return
            time.sleep(1)
        summon_hero()


def run_daemon(args):
    stop_event = threading.Event()
    t = threading.Thread(target=random_timed_summon, args=(args.min_sec, args.max_sec, stop_event))
    t.daemon = True
    t.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
        t.join()


def main():
    parser = argparse.ArgumentParser(description='謎のOS英雄召喚通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    summon_parser = subparsers.add_parser('summon', help='即時で英雄通知を発動')
    daemon_parser = subparsers.add_parser('daemon', help='ランダムな間隔で自動発動')
    daemon_parser.add_argument('--min-sec', type=int, default=900, help='最小待機秒数 (デフォルト900秒)')
    daemon_parser.add_argument('--max-sec', type=int, default=3600, help='最大待機秒数 (デフォルト3600秒)')

    list_parser = subparsers.add_parser('list', help='召喚可能な英雄一覧を表示')

    args = parser.parse_args()

    if args.command == 'summon':
        message = summon_hero()
        print('[OS通知]', message)
    elif args.command == 'daemon':
        print('ランダムOS英雄召喚デーモンを起動します... (Ctrl+Cで停止)')
        run_daemon(args)
    elif args.command == 'list':
        print('召喚可能な英雄一覧:')
        for hero in HEROES:
            print(' - {0} ({1})'.format(hero['name'], hero['title']))
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
