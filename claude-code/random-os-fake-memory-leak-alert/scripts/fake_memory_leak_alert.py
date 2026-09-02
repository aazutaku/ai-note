import sys
import random
import platform
import argparse
import time
import threading

try:
    if platform.system() == 'Darwin':
        from pync import Notifier
    elif platform.system() == 'Windows':
        from win10toast import ToastNotifier
    else:
        import notify2
except ImportError:
    pass

ALERT_MESSAGES = [
    '[ALERT] 重大：メモリがどこかに消えました',
    '[WARNING] OS公式：記憶領域流出中',
    '[INFO] 注意：あなたのやる気メモリもリークしています',
    '[CRITICAL] システムリソースが想定外の方向に流出しています',
    '[NOTICE] メモリリーク検出ツールがバグっています（たぶん）',
    '[ERROR] メモリ領域の一部がブラックホール化',
    '[ALERT] RAMの一部が異次元に転送されました',
    '[WARNING] メモリ管理プロセスが自己崩壊を開始',
    '[INFO] 仮想メモリが現実逃避中',
    '[CRITICAL] システムヒープが溢れかえっています',
    '[NOTICE] メモリリーク検出：再起動推奨（嘘です）',
    '[ALERT] OSからの緊急通知：記憶領域が蒸発しました',
    '[WARNING] メモリリークにより思考力が減少しています',
    '[INFO] メモリが勝手に解放されました',
    '[CRITICAL] メモリリークの波動を検出しました',
    '[NOTICE] メモリリーク警告：この通知はジョークです',
]

CATEGORY_MAP = {
    'ALERT': 'Critical',
    'WARNING': 'Warning',
    'INFO': 'Information',
    'CRITICAL': 'Critical',
    'NOTICE': 'Information',
    'ERROR': 'Error',
}

def send_notification(message):
    system = platform.system()
    title = 'OS Memory Leak Alert'
    # Extract category from message
    cat = 'INFO'
    for k in CATEGORY_MAP.keys():
        if message.startswith(f'[{k}]'):
            cat = k
            break
    if system == 'Darwin':
        try:
            Notifier.notify(message, title=title)
        except Exception as e:
            print(f'[通知失敗(macOS)]: {e}')
    elif system == 'Windows':
        try:
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=5, threaded=True, icon_path=None)
        except Exception as e:
            print(f'[通知失敗(Windows)]: {e}')
    else:
        try:
            notify2.init('FakeMemoryLeakAlert')
            n = notify2.Notification(title, message)
            n.set_urgency(notify2.URGENCY_CRITICAL if cat in ['ALERT','CRITICAL','ERROR'] else notify2.URGENCY_NORMAL)
            n.show()
        except Exception as e:
            print(f'[通知失敗(Linux)]: {e}')

def random_alert():
    message = random.choice(ALERT_MESSAGES)
    send_notification(message)
    print(message)

def alert_loop(interval, count):
    for i in range(count):
        random_alert()
        if i < count-1:
            time.sleep(interval)

def list_messages():
    print('利用可能なフェイク警告一覧:')
    for msg in ALERT_MESSAGES:
        print(f'- {msg}')

def summary():
    print('random-os-fake-memory-leak-alert Skill 概要:')
    print(f'通知パターン数: {len(ALERT_MESSAGES)}')
    print('対応OS:', platform.system())
    print('通知方式: OS標準通知API')

def parse_args():
    parser = argparse.ArgumentParser(description='謎のOSメモリリーク警告をランダムに表示')
    subparsers = parser.add_subparsers(dest='command')
    parser_alert = subparsers.add_parser('alert', help='即座にランダム警告を1回表示')
    parser_loop = subparsers.add_parser('loop', help='一定間隔で複数回警告を表示')
    parser_loop.add_argument('--interval', type=int, default=10, help='通知間隔(秒)')
    parser_loop.add_argument('--count', type=int, default=3, help='通知回数')
    parser_list = subparsers.add_parser('list', help='全通知パターンを表示')
    parser_summary = subparsers.add_parser('summary', help='Skill概要を表示')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'alert' or args.command is None:
        random_alert()
    elif args.command == 'loop':
        alert_loop(args.interval, args.count)
    elif args.command == 'list':
        list_messages()
    elif args.command == 'summary':
        summary()
    else:
        print('コマンドが不明です。--help を参照してください。')

if __name__ == '__main__':
    main()
