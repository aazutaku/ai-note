import sys
import time
import random
import argparse
from threading import Thread
from datetime import datetime

# 擬似的なプロセス名・警告文・進捗バー生成用データ
PROCESS_NAMES = [
    'phantomd', 'shadow-indexer', 'ghostproc', 'mysteryd', 'obscure-task',
    'unknown-agent', 'cryptic-daemon', 'foggyjob', 'twilightd', 'darkwatcher'
]
WARNINGS = [
    'システムリソースの一時的な再配分を検出',
    '不明なI/Oアクティビティ',
    '解析残り時間が不定です',
    'プロセス優先度が自動調整されました',
    '未知のデータフローを監視中',
    'プロセス間通信の遅延を検知',
    'メモリ空間で不可解な変動',
    'セッションIDの一時的な重複',
    'バックグラウンドで未知の集計作業',
    'ログファイルの断片化を検出'
]

def random_progress_bar(percent):
    bar_length = 10
    filled = int(bar_length * percent / 100)
    return '█' * filled + '░' * (bar_length - filled)

def random_pid():
    return random.randint(1000, 9999)

def random_time_left():
    return f"{random.randint(1, 30)}分"

def random_process_name():
    return random.choice(PROCESS_NAMES)

def random_warning():
    return random.choice(WARNINGS)

def generate_alert():
    style = random.choice(['ALERT', 'NOTICE', 'OS ALERT'])
    proc_name = random_process_name()
    pid = random_pid()
    percent = random.randint(20, 90)
    progress = random_progress_bar(percent)
    time_left = random_time_left()
    warning = random_warning()
    lines = []
    if style == 'ALERT':
        lines.append(f"[ALERT] プロセスID {pid} の挙動を監視中。詳細: {warning}")
    elif style == 'NOTICE':
        lines.append(f"[OS NOTICE] 未知の集計作業 “{proc_name}” がバックグラウンドで開始されました。")
        lines.append(f"進捗: {progress} {percent}% | 残り: {time_left}")
    else:
        lines.append(f"[OS ALERT] 謎のバックグラウンドプロセス “{proc_name}” (PID: {pid}) が起動しました。")
        lines.append(f"進捗: {progress} {percent}% | 解析残り時間: {time_left}")
        lines.append(f"警告: {warning}")
    return '\n'.join(lines)

def print_alert():
    alert = generate_alert()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}]\n{alert}\n---")

def random_sleep(min_sec=30, max_sec=120):
    t = random.uniform(min_sec, max_sec)
    time.sleep(t)

def alert_loop(count=None, min_sec=30, max_sec=120):
    i = 0
    try:
        while count is None or i < count:
            random_sleep(min_sec, max_sec)
            print_alert()
            i += 1
    except KeyboardInterrupt:
        print("\n[終了] 謎のバックグラウンドプロセス通知を停止しました。", file=sys.stderr)
        sys.exit(0)

def list_examples():
    for _ in range(5):
        print_alert()
        time.sleep(0.2)

def summary():
    print("このスキルは、完全に無害なOS風バックグラウンドプロセス通知をランダムなタイミングで出力します。意味不明な警告や進捗バーを含み、実際のシステムには影響しません。\n")
    print("- 通知内容は毎回異なります\n- 実害やデータ損失はありません\n- Ctrl+C で終了可能\n")

def main():
    parser = argparse.ArgumentParser(description='謎のOS風バックグラウンドプロセス通知をランダムに出力')
    subparsers = parser.add_subparsers(dest='command')

    run_parser = subparsers.add_parser('run', help='ランダムな通知を出力し続ける')
    run_parser.add_argument('--count', type=int, default=None, help='通知の回数 (省略時は無限)')
    run_parser.add_argument('--min-sec', type=int, default=30, help='通知間隔の最小秒数')
    run_parser.add_argument('--max-sec', type=int, default=120, help='通知間隔の最大秒数')

    list_parser = subparsers.add_parser('list', help='通知サンプルを5件表示')
    summary_parser = subparsers.add_parser('summary', help='Skill概要を表示')

    args = parser.parse_args()

    if args.command == 'run':
        alert_loop(count=args.count, min_sec=args.min_sec, max_sec=args.max_sec)
    elif args.command == 'list':
        list_examples()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
