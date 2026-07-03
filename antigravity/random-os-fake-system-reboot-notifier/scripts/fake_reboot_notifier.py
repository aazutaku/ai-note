import random
import time
import argparse
import sys
import os
from datetime import datetime
try:
    from plyer import notification
except ImportError:
    print('plyerモジュールが必要です。\nインストール: pip install plyer')
    sys.exit(1)

LOG_FILE = os.path.expanduser('~/.random_os_fake_reboot.log')

REASONS = [
    'カーネルの気まぐれ',
    'OSの気分転換',
    'メモリがやる気を失いました',
    'ネットワークの都合',
    '未知のエラー',
    'システムの自己主張',
    '管理者の気まぐれ',
    'プロセスが踊りだしました',
    '電源ボタンが押された気がしました',
    '時間の流れに逆らえません',
    'バグが自己増殖',
    'ファイルシステムの反乱',
    'アップデートの気配',
    'ユーザーの集中力低下',
    'コーヒーが切れました',
    'CPUが休憩を要求',
    '仮想メモリの夢',
    'セキュリティの気まぐれ',
    'OSの自己診断',
    'パーミッションの逆襲'
]

TITLES = [
    '重要なお知らせ：{min}分後にシステムは謎の理由で再起動します',
    'システム再起動まで残り{min}分です',
    'システムはまもなく再起動されます',
    '再起動予告：{min}分後にシステムが再起動される予定です',
    '警告：システム再起動がスケジュールされました',
    '通知：OS再起動まであと{min}分',
    'ご注意：システムが再起動を要求しています',
    '再起動のお知らせ：{min}分後',
    'システムからの通知：再起動準備中',
    '再起動インフォメーション：{min}分後に開始'
]

MINUTES = [1, 2, 3, 5, 10]


def get_random_notification():
    min_left = random.choice(MINUTES)
    title_template = random.choice(TITLES)
    title = title_template.format(min=min_left)
    reason = random.choice(REASONS)
    return title, reason, min_left


def show_notification(title, message):
    notification.notify(
        title=title,
        message='理由：' + message,
        app_name='Fake OS Reboot Notifier',
        timeout=10
    )


def log_notification(title, reason):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logline = f'[{now}] {title} | 理由：{reason}\n'
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(logline)
    except Exception as e:
        print(f'ログ書き込みエラー: {e}')


def list_logs():
    if not os.path.exists(LOG_FILE):
        print('ログファイルが存在しません。')
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print('=== Fake Reboot 通知履歴 ===')
    for line in lines:
        print(line.strip())


def summary_logs():
    if not os.path.exists(LOG_FILE):
        print('ログファイルが存在しません。')
        return
    count = 0
    reasons = {}
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            count += 1
            if '理由：' in line:
                reason = line.split('理由：')[-1].strip()
                reasons[reason] = reasons.get(reason, 0) + 1
    print(f'通知回数: {count}')
    print('理由別内訳:')
    for r, c in sorted(reasons.items(), key=lambda x: -x[1]):
        print(f'  {r}: {c}回')


def main():
    parser = argparse.ArgumentParser(description='Fake OS System Reboot Notifier')
    subparsers = parser.add_subparsers(dest='command')

    parser_notify = subparsers.add_parser('notify', help='ランダムな再起動通知を即座に表示')
    parser_log = subparsers.add_parser('list', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知理由の統計を表示')
    parser_test = subparsers.add_parser('test', help='複数回テスト通知（デバッグ用）')
    parser_test.add_argument('--count', type=int, default=3, help='通知回数')

    args = parser.parse_args()

    if args.command == 'notify' or args.command is None:
        title, reason, min_left = get_random_notification()
        show_notification(title, reason)
        log_notification(title, reason)
        print(f'[通知] {title}\n理由：{reason}')
    elif args.command == 'list':
        list_logs()
    elif args.command == 'summary':
        summary_logs()
    elif args.command == 'test':
        for i in range(args.count):
            title, reason, min_left = get_random_notification()
            show_notification(title, reason)
            log_notification(title, reason)
            print(f'[通知] {title}\n理由：{reason}')
            time.sleep(1)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
