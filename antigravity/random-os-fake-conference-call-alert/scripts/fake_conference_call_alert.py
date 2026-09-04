import random
import time
import argparse
import sys
import os
from datetime import datetime, timedelta
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

def get_random_topic():
    topics = [
        '全社的にマウスの左クリック禁止案',
        'コーヒー豆の粒度再検討',
        '今すぐ全員集合：超重要案件について',
        '出欠はOSが自動判定します',
        '本日の議題：デバッグログの永久保存義務化',
        '「Ctrl+Z」キー廃止の是非',
        '全社員のデスクトップ壁紙統一',
        'AIによる会議自動進行案',
        '今日のランチメニュー緊急再考',
        'OSバージョン名を動物名に統一',
        'システム再起動祭り開催',
        '全社的にタブとスペースの統一',
        'ランダム抽選による出席',
        '重要案件につき全員参加必須',
        '参加しない場合は自動的に再起動されます（嘘）',
        '本日の議題：会議のための会議について',
        'マイクロマネジメントの是非',
        '全社的なパスワード変更祭り',
        'OSがあなたの出欠を監視しています',
        '本日の議題：会議の議題を決める会議'
    ]
    return random.choice(topics)

def get_random_attendance():
    options = [
        'OSが自動判定します',
        'ランダム抽選',
        '全員参加必須',
        '参加は任意（嘘）',
        '抽選で選ばれた方のみ',
        'AIが決定します',
        '参加しない場合は自動的に再起動されます（嘘）'
    ]
    return random.choice(options)

def get_random_time():
    options = [
        '直ちに',
        '5分後',
        '10秒後',
        '本日中',
        '今すぐ',
        'ランダムなタイミングで'
    ]
    return random.choice(options)

def generate_alert():
    topic = get_random_topic()
    attendance = get_random_attendance()
    start_time = get_random_time()
    notice = random.choice([
        '重要案件につき全員参加必須',
        '参加しない場合は自動的に再起動されます（嘘）',
        'この通知はフィクションです',
        'OSがあなたを見守っています',
        '議題に異議申し立て不可'
    ])
    alert = f"[OS Official Conference Call Alert]\n議題: {topic}\n出欠: {attendance}\n開始時刻: {start_time}\n注意: {notice}\n"
    return alert

def show_notification(alert):
    if PLYER_AVAILABLE:
        notification.notify(
            title='OS Official Conference Call',
            message=alert.replace('\n', ' '),
            app_name='FakeConfCall',
            timeout=8
        )
    else:
        # Fallback: print to terminal
        print(alert)

def log_alert(alert, logfile):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(logfile, 'a', encoding='utf-8') as f:
        f.write(f'[{now}]\n{alert}\n')

def list_alerts(logfile):
    if not os.path.exists(logfile):
        print('No alerts have been logged yet.')
        return
    with open(logfile, 'r', encoding='utf-8') as f:
        print(f.read())

def summary_alerts(logfile):
    if not os.path.exists(logfile):
        print('No alerts have been logged yet.')
        return
    count = 0
    with open(logfile, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('[OS Official Conference Call Alert]'):
                count += 1
    print(f'Total fake conference call alerts: {count}')

def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Conference Call Alert')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='Generate and log a fake conference call alert')
    parser_log.add_argument('--logfile', type=str, default='fake_conf_alert.log', help='Log file path')
    parser_log.add_argument('--notify', action='store_true', help='Show desktop notification if possible')

    parser_list = subparsers.add_parser('list', help='List all logged fake alerts')
    parser_list.add_argument('--logfile', type=str, default='fake_conf_alert.log', help='Log file path')

    parser_summary = subparsers.add_parser('summary', help='Show summary of fake alerts')
    parser_summary.add_argument('--logfile', type=str, default='fake_conf_alert.log', help='Log file path')

    parser_run = subparsers.add_parser('run', help='Run in background and alert at random intervals')
    parser_run.add_argument('--logfile', type=str, default='fake_conf_alert.log', help='Log file path')
    parser_run.add_argument('--min-interval', type=int, default=3600, help='Minimum interval (seconds)')
    parser_run.add_argument('--max-interval', type=int, default=5400, help='Maximum interval (seconds)')
    parser_run.add_argument('--notify', action='store_true', help='Show desktop notification if possible')

    args = parser.parse_args()

    if args.command == 'log':
        alert = generate_alert()
        log_alert(alert, args.logfile)
        if args.notify:
            show_notification(alert)
        else:
            print(alert)
    elif args.command == 'list':
        list_alerts(args.logfile)
    elif args.command == 'summary':
        summary_alerts(args.logfile)
    elif args.command == 'run':
        print('Fake Conference Call Alert Daemon started.')
        try:
            while True:
                interval = random.randint(args.min_interval, args.max_interval)
                time.sleep(interval)
                alert = generate_alert()
                log_alert(alert, args.logfile)
                if args.notify:
                    show_notification(alert)
                else:
                    print(alert)
        except KeyboardInterrupt:
            print('Daemon stopped.')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
