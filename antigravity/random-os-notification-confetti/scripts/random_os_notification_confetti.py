import sys
import os
import random
import time
import argparse
import platform
import threading

try:
    if platform.system() == 'Darwin':
        import pync
    elif platform.system() == 'Windows':
        from win10toast import ToastNotifier
    elif platform.system() == 'Linux':
        import notify2
except ImportError:
    pass

CONFETTI_MESSAGES = [
    '本日も出社おめでとう！',
    '意味なく祝福します。',
    'さっきのls、最高でした。',
    'runコマンド、見事な実行力！',
    '今日は何もなくても祝っておきます。',
    'そのgit add、素晴らしい判断です。',
    'make build、祝福の嵐。',
    'vim保存、お疲れさまでした。',
    'push前の静けさに乾杯。',
    'ls -la、完璧でした。',
    '何もしてないのに祝います。',
    '今日もターミナルが輝いています。',
    'あなたのコマンドに紙吹雪を。',
    'build成功、おめでとう！',
    'git commit、ナイスです。',
    '編集保存、祝福します。',
    'どんな作業にもエールを送ります。',
    'lsのタイミング、最高でした。',
    '意味はないけど祝います。',
    'push成功、紙吹雪！',
]

TRIGGER_KEYWORDS = [
    'ls', 'git', 'make', 'build', 'run', 'vim', 'nano', 'code', 'save', 'commit', 'push', 'pull', 'edit', 'open'
]

NOTIFY_INTERVAL_RANGE = (300, 900)  # 5分〜15分の間隔
LAST_NOTIFY_FILE = os.path.expanduser('~/.random_confetti_notify_time')


def can_notify():
    """
    通知間隔を制御。前回通知から十分経過していればTrue。
    """
    now = time.time()
    if os.path.exists(LAST_NOTIFY_FILE):
        try:
            with open(LAST_NOTIFY_FILE, 'r') as f:
                last = float(f.read().strip())
            if now - last < random.randint(*NOTIFY_INTERVAL_RANGE):
                return False
        except Exception:
            pass
    return True


def update_notify_time():
    try:
        with open(LAST_NOTIFY_FILE, 'w') as f:
            f.write(str(time.time()))
    except Exception:
        pass


def select_random_message():
    return random.choice(CONFETTI_MESSAGES)


def send_notification(message):
    sys_platform = platform.system()
    try:
        if sys_platform == 'Darwin':
            pync.notify(message, title='通知')
        elif sys_platform == 'Windows':
            toaster = ToastNotifier()
            toaster.show_toast('通知', message, duration=5, threaded=True)
        elif sys_platform == 'Linux':
            notify2.init('Confetti')
            n = notify2.Notification('通知', message)
            n.set_urgency(notify2.URGENCY_NORMAL)
            n.show()
        else:
            print('[通知]', message)
    except Exception as e:
        print('[通知]', message, '(通知APIエラー:', e, ')')


def monitor_commands(logfile=None):
    """
    コマンド履歴や作業ログを監視し、トリガーキーワード検出時に通知。
    """
    last_line = ''
    while True:
        if logfile and os.path.exists(logfile):
            with open(logfile, 'r') as f:
                lines = f.readlines()
                if lines:
                    line = lines[-1].strip()
                    if line != last_line:
                        last_line = line
                        if any(k in line for k in TRIGGER_KEYWORDS):
                            if can_notify():
                                msg = select_random_message()
                                send_notification(msg)
                                update_notify_time()
        else:
            # 標準入力監視（例: コマンドラッパー経由）
            try:
                line = sys.stdin.readline()
                if not line:
                    time.sleep(1)
                    continue
                line = line.strip()
                if any(k in line for k in TRIGGER_KEYWORDS):
                    if can_notify():
                        msg = select_random_message()
                        send_notification(msg)
                        update_notify_time()
            except KeyboardInterrupt:
                break
        time.sleep(2)


def random_notify_loop():
    """
    完全ランダムな間隔で祝福通知を送り続けるバックグラウンドループ。
    """
    while True:
        wait_sec = random.randint(*NOTIFY_INTERVAL_RANGE)
        time.sleep(wait_sec)
        if can_notify():
            msg = select_random_message()
            send_notification(msg)
            update_notify_time()


def main():
    parser = argparse.ArgumentParser(description='Random OS Notification Confetti')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='バックグラウンドでランダム通知')
    parser_monitor = subparsers.add_parser('monitor', help='コマンド履歴やログを監視し通知')
    parser_monitor.add_argument('--logfile', type=str, default=None, help='監視するコマンド履歴ファイル')
    parser_test = subparsers.add_parser('test', help='1回だけテスト通知')

    args = parser.parse_args()

    if args.command == 'run':
        print('Confetti通知をバックグラウンドで実行します（Ctrl+Cで停止）')
        try:
            random_notify_loop()
        except KeyboardInterrupt:
            print('\n終了します')
    elif args.command == 'monitor':
        print('コマンド履歴監視モード（Ctrl+Cで停止）')
        try:
            monitor_commands(logfile=args.logfile)
        except KeyboardInterrupt:
            print('\n終了します')
    elif args.command == 'test':
        msg = select_random_message()
        send_notification(msg)
        update_notify_time()
        print('テスト通知を送信しました:', msg)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
