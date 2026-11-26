import argparse
import random
import sys
import time
import threading
from datetime import datetime, timedelta

FAKE_PROCESS_NAMES = [
    'XQ-Shadow', 'GhostIndex', 'SilentWatcher', 'QuantumSync',
    'NebulaTask', 'PhantomMerge', 'MetaCrawler', 'DarkTrace',
    'OblivionScan', 'ZeroPoint', 'SpecterRun', 'BlackBox',
    'NullEvent', 'EchoPulse', 'VortexSweep', 'CipherDaemon'
]

FAKE_ALERTS = [
    '[ALERT] 未知のバックグラウンドプロセスがPID {pid}で起動しました。',
    '[INFO] 集計タスク“{name}”進捗: {progress}% 完了。残り時間: {eta}。',
    '[WARNING] プロセスID {pid} の挙動を監視しています…',
    '[NOTICE] 不明な解析ジョブ“{name}”がバックグラウンドで動作中。',
    '[ALERT] システムリソースの一部が一時的にロックされました。',
    '[INFO] “{name}”プロセスが異常なI/Oパターンを検出しました。',
    '[WARNING] 不明なプロセスID {pid} が一時停止されました。',
    '[NOTICE] システム内部で“{name}”の再構成が進行中です。',
    '[ALERT] 検証不能なメモリ領域にアクセスが発生しました。',
    '[INFO] “{name}”のバックグラウンド解析が{progress}%進行中。',
    '[WARNING] 非公開プロセスID {pid} の監視を開始しました。',
    '[NOTICE] “{name}”の進捗バー: [{bar}] {progress}%'
]

PROGRESS_BARS = [
    lambda p: '=' * (p // 10) + ' ' * (10 - p // 10),
    lambda p: '#' * (p // 10) + '-' * (10 - p // 10),
    lambda p: '>' * (p // 20) + '.' * (5 - p // 20)
]

def random_pid():
    return random.randint(1000, 99999)

def random_progress():
    return random.randint(1, 99)

def random_eta():
    mins = random.randint(0, 59)
    secs = random.randint(10, 59)
    return f"{mins}分{secs}秒"

def random_name():
    return random.choice(FAKE_PROCESS_NAMES)

def random_bar(progress):
    bar_fn = random.choice(PROGRESS_BARS)
    return bar_fn(progress)

def generate_fake_alert():
    template = random.choice(FAKE_ALERTS)
    pid = random_pid()
    progress = random_progress()
    eta = random_eta()
    name = random_name()
    bar = random_bar(progress)
    return template.format(pid=pid, progress=progress, eta=eta, name=name, bar=bar)

def print_alert():
    alert = generate_fake_alert()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] {alert}")

def random_interval(min_sec=20, max_sec=120):
    return random.uniform(min_sec, max_sec)

def alert_loop(count=None):
    i = 0
    try:
        while count is None or i < count:
            print_alert()
            i += 1
            sleep_time = random_interval()
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("\n[INFO] Fake alert loop interrupted by user.")

def list_alerts(n=10):
    for _ in range(n):
        print_alert()
        time.sleep(0.2)

def summary():
    print("=== random-os-fake-mysterious-background-process-alert ===")
    print("このスクリプトは、完全ランダムなタイミング・内容で謎のバックグラウンドプロセス通知を生成します。\n")
    print("サブコマンド:")
    print("  log [--count N]   : ランダムな間隔でN回(省略時は無限)通知")
    print("  list [--num N]    : 直ちにN個の通知を表示")
    print("  summary           : このSkillの概要を表示")
    print("\n本Skillは演出目的のみで、システムやファイルに一切影響を与えません。\n")

def parse_args():
    parser = argparse.ArgumentParser(description="Fake mysterious OS background process alert generator.")
    subparsers = parser.add_subparsers(dest='command')

    log_parser = subparsers.add_parser('log', help='Run fake alerts at random intervals')
    log_parser.add_argument('--count', type=int, default=None, help='Number of alerts (default: infinite)')

    list_parser = subparsers.add_parser('list', help='Show N fake alerts immediately')
    list_parser.add_argument('--num', type=int, default=5, help='Number of alerts to show (default: 5)')

    subparsers.add_parser('summary', help='Show summary of this skill')

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'log':
        alert_loop(count=args.count)
    elif args.command == 'list':
        list_alerts(n=args.num)
    elif args.command == 'summary' or args.command is None:
        summary()
    else:
        print("Unknown command. Use --help for usage.")

if __name__ == '__main__':
    main()
