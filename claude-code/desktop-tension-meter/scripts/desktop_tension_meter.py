import sys
import argparse
import random
import time
import threading
import subprocess
import os
from datetime import datetime
try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    tk = None  # headless環境用

TENSION_LABELS = [
    (0, 40, '平常心'),
    (41, 70, 'やや焦り'),
    (71, 89, '緊張気味'),
    (90, 100, '極度緊張')
]

CONFIG = {
    'min_interval': 180,   # 秒
    'max_interval': 600,   # 秒
    'notify_duration': 8,  # 秒
    'use_commit': True,
    'use_typing': True,
    'logfile': os.path.expanduser('~/.desktop_tension_meter.log')
}

def get_commit_count():
    try:
        out = subprocess.check_output(['git', 'rev-list', '--count', 'HEAD'], stderr=subprocess.DEVNULL)
        return int(out.strip())
    except Exception:
        return random.randint(0, 100)

def get_typing_speed():
    # ダミー実装: 実際のタイピング速度取得は困難なためランダム
    return random.randint(20, 120)

def calc_tension():
    base = random.randint(0, 100)
    if CONFIG['use_commit']:
        commit = get_commit_count()
        base = (base + min(commit, 100)) // 2
    if CONFIG['use_typing']:
        typing = get_typing_speed()
        base = (base + min(typing, 100)) // 2
    return min(max(base, 0), 100)

def get_label(score):
    for low, high, label in TENSION_LABELS:
        if low <= score <= high:
            return label
    return '未知'

def log_event(score, label):
    with open(CONFIG['logfile'], 'a') as f:
        f.write(f"{datetime.now().isoformat()}\t{score}\t{label}\n")

def show_notification(score, label, duration):
    # OSごとに分岐
    if sys.platform.startswith('linux'):
        try:
            subprocess.Popen(['notify-send', f'緊張度: {score}%（{label}）',
                             '--expire-time', str(duration * 1000)])
        except Exception:
            pass
    elif sys.platform == 'darwin':
        osa = f'display notification "緊張度: {score}%（{label}）" with title "desktop-tension-meter"'
        subprocess.call(['osascript', '-e', osa])
    elif sys.platform.startswith('win'):
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast("desktop-tension-meter",
                               f"緊張度: {score}%（{label}）",
                               duration=duration)
        except Exception:
            pass
    else:
        # tkinter fallback
        if tk:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("desktop-tension-meter", f"緊張度: {score}%（{label}）")
            root.destroy()

def tension_loop(args):
    while True:
        score = calc_tension()
        label = get_label(score)
        log_event(score, label)
        show_notification(score, label, CONFIG['notify_duration'])
        interval = random.randint(CONFIG['min_interval'], CONFIG['max_interval'])
        if args.verbose:
            print(f"[desktop-tension-meter] 緊張度: {score}%（{label}） 次回: {interval//60}分後")
        time.sleep(interval)

def list_logs():
    if not os.path.exists(CONFIG['logfile']):
        print("ログがありません")
        return
    with open(CONFIG['logfile']) as f:
        for line in f:
            print(line.strip())

def summary_logs():
    if not os.path.exists(CONFIG['logfile']):
        print("ログがありません")
        return
    scores = []
    with open(CONFIG['logfile']) as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                try:
                    scores.append(int(parts[1]))
                except ValueError:
                    continue
    if not scores:
        print("集計データなし")
        return
    print(f"平均緊張度: {sum(scores)//len(scores)}%  最大: {max(scores)}%  最小: {min(scores)}%  件数: {len(scores)}")

def main():
    parser = argparse.ArgumentParser(description='desktop-tension-meter: デスクトップに無意味な緊張度をテロップ表示')
    subparsers = parser.add_subparsers(dest='command')

    run_p = subparsers.add_parser('run', help='バックグラウンドで緊張度テロップを表示')
    run_p.add_argument('--verbose', action='store_true', help='詳細ログを標準出力')

    list_p = subparsers.add_parser('list', help='緊張度ログを表示')
    summary_p = subparsers.add_parser('summary', help='緊張度ログを集計')

    args = parser.parse_args()
    if args.command == 'run' or args.command is None:
        try:
            tension_loop(args)
        except KeyboardInterrupt:
            print("\n[desktop-tension-meter] 終了します")
    elif args.command == 'list':
        list_logs()
    elif args.command == 'summary':
        summary_logs()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
