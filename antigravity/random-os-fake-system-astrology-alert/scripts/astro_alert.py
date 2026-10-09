import random
import time
import argparse
import sys
import threading
from datetime import datetime

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

ASTRO_COMMANDS = [
    'ls', 'grep', 'cat', 'cd', 'echo', 'rm', 'mkdir', 'touch', 'pwd', 'find', 'chmod',
    'curl', 'git', 'nano', 'vim', 'top', 'htop', 'ps', 'kill', 'ssh', 'scp', 'tar', 'zip'
]

PLANETS = [
    '水星', '金星', '地球', '火星', '木星', '土星', '天王星', '海王星', '冥王星'
]

ASTRO_EVENTS = [
    '水星逆行中につきバグ注意',
    '今日はネットワーク遅延に注意',
    'あなたの運命ファイル: ~/.bashrc',
    '今日の運勢: システム再起動に注意',
    'ラッキーIPアドレス: 127.0.0.1',
    '今日のアンラッキーコマンド: sudo rm -rf /',
    '星座的に今週はメモリ不足に注意',
    'あなたの守護惑星は{planet}です',
    '今日のラッキーコマンド: {command}',
    'ログインシェルに幸運が訪れる予感',
    '木星が昇る日はコマンド入力ミスに注意',
    '土星の影響でgit pushに要注意',
    '宇宙の流れに身を任せて再起動',
    '今日の運命のプロセスID: {pid}',
    'ラッキーポート番号: {port}'
]

def generate_alert():
    command = random.choice(ASTRO_COMMANDS)
    planet = random.choice(PLANETS)
    pid = random.randint(100, 99999)
    port = random.choice([22, 80, 443, 3306, 5432, 8080, 6379])
    event = random.choice(ASTRO_EVENTS)
    event = event.replace('{command}', command)
    event = event.replace('{planet}', planet)
    event = event.replace('{pid}', str(pid))
    event = event.replace('{port}', str(port))
    return f"[AstroSys Alert] {event}"

def show_notification(message):
    if PLYER_AVAILABLE:
        notification.notify(
            title='AstroSys Alert',
            message=message.replace('[AstroSys Alert] ', ''),
            timeout=7
        )
    else:
        print(message)

def random_alert_loop(interval_min, interval_max, stop_event):
    while not stop_event.is_set():
        wait_time = random.uniform(interval_min, interval_max)
        stop_event.wait(wait_time)
        if stop_event.is_set():
            break
        alert = generate_alert()
        show_notification(alert)

def log_alerts(count, output):
    logs = []
    for _ in range(count):
        alert = generate_alert()
        logs.append(f"{datetime.now().isoformat()} {alert}")
        show_notification(alert)
        time.sleep(1)
    if output:
        try:
            with open(output, 'a', encoding='utf-8') as f:
                for log in logs:
                    f.write(log + '\n')
            print(f"[AstroSys Alert] {len(logs)}件のログを {output} に保存しました。")
        except Exception as e:
            print(f"[AstroSys Alert] ログ保存エラー: {e}")

def list_sample_alerts(num):
    for _ in range(num):
        print(generate_alert())

def parse_args():
    parser = argparse.ArgumentParser(description='AstroSys: システム占星術風ランダム通知')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='ランダム間隔で通知を表示')
    parser_run.add_argument('--min', type=float, default=60, help='最小間隔(秒)')
    parser_run.add_argument('--max', type=float, default=300, help='最大間隔(秒)')

    parser_log = subparsers.add_parser('log', help='指定回数だけ通知しログ保存')
    parser_log.add_argument('--count', type=int, default=5, help='通知回数')
    parser_log.add_argument('--output', type=str, default='', help='ログファイルパス')

    parser_list = subparsers.add_parser('list', help='サンプル通知を表示')
    parser_list.add_argument('--num', type=int, default=5, help='サンプル数')

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'run':
        stop_event = threading.Event()
        try:
            t = threading.Thread(target=random_alert_loop, args=(args.min, args.max, stop_event))
            t.start()
            print('[AstroSys Alert] ランダム通知モードを開始します。Ctrl+Cで終了。')
            while t.is_alive():
                t.join(1)
        except KeyboardInterrupt:
            stop_event.set()
            print('\n[AstroSys Alert] 通知を終了します。')
    elif args.command == 'log':
        log_alerts(args.count, args.output)
    elif args.command == 'list':
        list_sample_alerts(args.num)
    else:
        print('[AstroSys Alert] サブコマンドを指定してください: run | log | list')
        sys.exit(1)

if __name__ == '__main__':
    main()
