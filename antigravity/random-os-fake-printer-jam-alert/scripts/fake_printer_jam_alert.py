import os
import sys
import time
import random
import argparse
import threading
from datetime import datetime

try:
    if sys.platform.startswith('win'):
        from win10toast import ToastNotifier
        notifier = ToastNotifier()
        OS_TYPE = 'windows'
    elif sys.platform == 'darwin':
        import pync
        OS_TYPE = 'mac'
    else:
        import notify2
        notify2.init('FakePrinterJam')
        OS_TYPE = 'linux'
except ImportError:
    notifier = None
    OS_TYPE = 'none'

FAKE_FILES = [
    'main.py', 'report_2024.txt', 'summary.docx', 'invoice.pdf', 'README.md',
    'data_export.csv', 'backup.tar.gz', 'presentation.pptx', 'notes.txt', 'draft.doc'
]

JAM_MESSAGES = [
    '重要：プリンタで“{file}”が詰まりました。紙を手で給紙してください。',
    '警告：印刷待ちジョブが渋滞中。謎のトナーを補充してください。',
    'エラー：{file}の印刷中に紙詰まりが発生しました。プリンタカバーを開けてください。',
    '注意：プリンタが応答しません。紙を裏返して再度セットしてください。',
    '重大：印刷キューに未知の障害が発生しました。管理者に連絡してください。',
    '警告：プリンタメモリが溢れています。紙を一枚ずつ挿入してください。',
    'エラー：{file}の印刷でトナーが認識されません。純正トナーを装着してください。',
    '注意：プリンタが“{file}”の用紙サイズを判別できません。A4をセットしてください。',
    '重大：プリンタ内部で紙が迷子になりました。全てのカバーを開けて点検してください。',
    '警告：プリンタが“{file}”の印刷を拒否しました。再試行してください。'
]

LOG_FILE = os.path.expanduser('~/.fake_printer_jam_alert.log')


def random_message():
    file = random.choice(FAKE_FILES)
    msg = random.choice(JAM_MESSAGES)
    return msg.format(file=file)


def send_notification(msg):
    if OS_TYPE == 'windows' and notifier:
        notifier.show_toast('OS通知', msg, duration=8, threaded=True)
    elif OS_TYPE == 'mac':
        try:
            import pync
            pync.notify(msg, title='OS通知')
        except Exception:
            pass
    elif OS_TYPE == 'linux':
        try:
            import notify2
            n = notify2.Notification('OS通知', msg)
            n.set_timeout(8000)
            n.show()
        except Exception:
            pass
    else:
        print('[OS通知]', msg)


def log_notification(msg):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f'[{now}] {msg}\n')


def random_interval(min_sec=90, max_sec=600):
    return random.randint(min_sec, max_sec)


def alert_loop(forever=True, count=0):
    sent = 0
    while forever or sent < count:
        wait = random_interval()
        time.sleep(wait)
        msg = random_message()
        send_notification(msg)
        log_notification(msg)
        sent += 1


def list_logs(lines=10):
    if not os.path.exists(LOG_FILE):
        print('ログが存在しません。')
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        logs = f.readlines()
        for line in logs[-lines:]:
            print(line.strip())


def summary_logs():
    if not os.path.exists(LOG_FILE):
        print('ログが存在しません。')
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        logs = f.readlines()
    print(f'通知回数: {len(logs)}')
    files = {}
    for l in logs:
        for fname in FAKE_FILES:
            if fname in l:
                files[fname] = files.get(fname, 0) + 1
    print('通知対象ファイルランキング:')
    for k, v in sorted(files.items(), key=lambda x: -x[1]):
        print(f'  {k}: {v}回')


def clear_logs():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print('ログを削除しました。')
    else:
        print('ログが存在しません。')


def main():
    parser = argparse.ArgumentParser(description='Fake OS Printer Jam Alert Skill')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='ランダムなプリンタ紙詰まり通知を発生させる')
    parser_run.add_argument('--count', type=int, help='通知回数（指定しない場合は無限）')

    parser_list = subparsers.add_parser('list', help='直近の通知ログを表示')
    parser_list.add_argument('--lines', type=int, default=10, help='表示する行数')

    parser_summary = subparsers.add_parser('summary', help='通知ログのサマリを表示')
    parser_clear = subparsers.add_parser('clear', help='通知ログを削除')

    args = parser.parse_args()

    if args.command == 'run':
        if args.count:
            alert_loop(forever=False, count=args.count)
        else:
            try:
                alert_loop()
            except KeyboardInterrupt:
                print('\n終了します。')
    elif args.command == 'list':
        list_logs(lines=args.lines)
    elif args.command == 'summary':
        summary_logs()
    elif args.command == 'clear':
        clear_logs()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
