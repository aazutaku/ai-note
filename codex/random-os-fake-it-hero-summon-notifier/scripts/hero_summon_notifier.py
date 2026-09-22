import sys
import os
import random
import time
import argparse
import platform
import subprocess
from datetime import datetime

HERO_MESSAGES = [
    '伝説のデバッグ勇者「メモリ・マスター」が召喚されました！',
    '今こそバグ退治の時！“コマンド使いのジョン”出動',
    'シェルの魔法使い「Zshの賢者」が現れた！',
    'あなたの作業を見守る“Gitの守護者”が加勢します',
    'バグの洞窟に“Stack Overflowの精霊”が舞い降りました',
    'コードの彼方から“Pull Requestの勇者”が現れた！',
    'ビルドの神「Makefileの導師」が舞い降りた',
    '“正規表現の忍者”が静かに現れた',
    '“Dockerの錬金術師”がサポートに加わった',
    '“Vimの伝道師”があなたの手元に現れた',
    '“バグ退治の戦士”がログを見守っています',
    '“コマンドラインの守護神”があなたの背後に',
    '“ネットワークの賢者”が接続を見守っています',
    '“ターミナルの精霊”が応援にきました',
    '“バージョン管理の勇者”が現れた！',
    '“APIの魔法使い”が参上',
    '“パーミッションの守護者”が警戒中',
    '“セグフォの祓い師”がバグを追放します',
    '“バッチ処理の巨匠”が降臨',
    '“リファクタリングの勇者”が剣を抜いた',
]

LOG_FILE = os.path.expanduser('~/.hero_summon_notifier.log')


def send_notification(message):
    system = platform.system()
    title = 'OS通知'
    try:
        if system == 'Linux':
            subprocess.run(['notify-send', title, message], check=False)
        elif system == 'Darwin':
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', script], check=False)
        elif system == 'Windows':
            # Windows 10+ only, fallback to terminal output
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=5)
            except ImportError:
                print(f'[OS通知] {message}')
        else:
            print(f'[OS通知] {message}')
    except Exception as e:
        print(f'[OS通知] {message} (通知失敗: {e})')


def log_message(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f'{timestamp} {message}\n')


def summon_hero():
    message = random.choice(HERO_MESSAGES)
    send_notification(message)
    log_message(message)
    return message


def list_log():
    if not os.path.exists(LOG_FILE):
        print('通知履歴はありません。')
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        print(line.strip())


def summary_log():
    if not os.path.exists(LOG_FILE):
        print('通知履歴はありません。')
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f'通知回数: {len(lines)}')
    last = lines[-1].strip() if lines else 'なし'
    print(f'最新通知: {last}')


def random_wait(min_sec=300, max_sec=1200):
    wait_time = random.randint(min_sec, max_sec)
    time.sleep(wait_time)


def auto_mode(loop=False):
    try:
        while True:
            summon_hero()
            if not loop:
                break
            random_wait()
    except KeyboardInterrupt:
        print('自動通知を終了します。')


def main():
    parser = argparse.ArgumentParser(description='random-os-fake-it-hero-summon-notifier')
    subparsers = parser.add_subparsers(dest='command')

    parser_summon = subparsers.add_parser('summon', help='今すぐ英雄を召喚')
    parser_auto = subparsers.add_parser('auto', help='ランダム間隔で自動通知 (Ctrl+Cで停止)')
    parser_auto.add_argument('--loop', action='store_true', help='永続ループ')
    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知履歴のサマリを表示')

    args = parser.parse_args()

    if args.command == 'summon':
        msg = summon_hero()
        print(f'[OS通知] {msg}')
    elif args.command == 'auto':
        auto_mode(loop=args.loop)
    elif args.command == 'list':
        list_log()
    elif args.command == 'summary':
        summary_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
