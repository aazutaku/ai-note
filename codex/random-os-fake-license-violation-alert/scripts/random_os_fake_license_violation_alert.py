import sys
import os
import random
import time
import argparse
import platform
from datetime import datetime

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

VIOLATION_TEMPLATES = [
    {
        'violation': 'あなたの椅子、座りすぎライセンス違反',
        'advice': '立ち上がってストレッチしてください。',
        'code': 'CHR-999'
    },
    {
        'violation': 'コーヒーブレイク無許可利用を検出',
        'advice': '直ちに作業に戻ってください。',
        'code': 'CFE-007'
    },
    {
        'violation': '謎のキーボード配列違反',
        'advice': '管理者に連絡してください。',
        'code': 'KBD-314'
    },
    {
        'violation': 'マウスクリック過剰利用違反',
        'advice': 'クリック数を減らしてください。',
        'code': 'MSE-201'
    },
    {
        'violation': '未認可タブ開きすぎ違反',
        'advice': '不要なタブを閉じてください。',
        'code': 'TAB-404'
    },
    {
        'violation': 'スクリーンショット無許可保存違反',
        'advice': 'スクリーンショットは許可後に保存してください。',
        'code': 'SS-888'
    },
    {
        'violation': '未承認フォント利用違反',
        'advice': '公式フォントに切り替えてください。',
        'code': 'FNT-123'
    },
    {
        'violation': 'ディスプレイ輝度不適合違反',
        'advice': '輝度を調整してください。',
        'code': 'BRG-567'
    },
    {
        'violation': '未認可ショートカットキー利用違反',
        'advice': 'ショートカットキーの利用申請をしてください。',
        'code': 'SCT-321'
    },
    {
        'violation': 'OSアップデート回避違反',
        'advice': 'アップデートを実施してください。',
        'code': 'UPD-001'
    }
]

HISTORY_FILE = os.path.expanduser('~/.random_os_fake_license_violation_alert.log')


def send_notification(title, message):
    system = platform.system()
    if PLYER_AVAILABLE:
        notification.notify(title=title, message=message, app_name='OS License Violation', timeout=10)
    elif system == 'Darwin':
        os.system(f'''osascript -e 'display notification "{message}" with title "{title}"' ''')
    elif system == 'Linux':
        os.system(f'notify-send "{title}" "{message}"')
    elif system == 'Windows':
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=10)
        except ImportError:
            print("[通知]", title)
            print(message)
    else:
        print("[通知]", title)
        print(message)


def random_violation():
    v = random.choice(VIOLATION_TEMPLATES)
    # ランダムで文言を少し変化させる
    variants = [
        v['violation'],
        v['violation'].replace('違反', 'ライセンス違反'),
        v['violation'].replace('検出', '発見'),
        v['violation'].replace('未認可', '無許可'),
        v['violation'].replace('未承認', '未登録'),
    ]
    violation_text = random.choice(variants)
    advice = v['advice']
    code = v['code']
    return violation_text, advice, code


def format_notification(violation, advice, code):
    lines = [
        "OSライセンス違反警告",
        f"違反内容: {violation}",
        f"対策: {advice}違反コード: {code}"
    ]
    return "\n".join(lines)


def log_violation(violation, advice, code):
    now = datetime.now().isoformat(timespec='seconds')
    with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{now}\t{violation}\t{advice}\t{code}\n")


def list_history(limit=10):
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines = lines[-limit:]
    print("--- 通知履歴 ---")
    for line in lines:
        ts, violation, advice, code = line.strip().split('\t')
        print(f"[{ts}] {violation} / {advice} / {code}")


def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    counts = {}
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            _, violation, _, _ = line.strip().split('\t')
            counts[violation] = counts.get(violation, 0) + 1
    print("--- 違反内容ごとの発生回数 ---")
    for v, c in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{v}: {c}回")


def main():
    parser = argparse.ArgumentParser(description='謎のOSライセンス違反警告をランダム通知')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='即時で通知を1回発生させる')
    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_list.add_argument('--limit', type=int, default=10, help='表示件数')
    parser_summary = subparsers.add_parser('summary', help='違反内容ごとの発生回数集計')
    parser_daemon = subparsers.add_parser('daemon', help='バックグラウンドでランダム間隔通知')
    parser_daemon.add_argument('--min', type=int, default=600, help='最小間隔(秒)')
    parser_daemon.add_argument('--max', type=int, default=1800, help='最大間隔(秒)')

    args = parser.parse_args()

    if args.command == 'log' or args.command is None:
        violation, advice, code = random_violation()
        msg = format_notification(violation, advice, code)
        send_notification('OSライセンス違反警告', f"違反内容: {violation}\n対策: {advice}違反コード: {code}")
        log_violation(violation, advice, code)
        print('[通知] OSライセンス違反警告')
        print(f"違反内容: {violation}")
        print(f"対策: {advice}違反コード: {code}")
    elif args.command == 'list':
        list_history(args.limit)
    elif args.command == 'summary':
        summary_history()
    elif args.command == 'daemon':
        print('バックグラウンド通知を開始します (Ctrl+Cで停止)')
        try:
            while True:
                wait = random.randint(args.min, args.max)
                time.sleep(wait)
                violation, advice, code = random_violation()
                send_notification('OSライセンス違反警告', f"違反内容: {violation}\n対策: {advice}違反コード: {code}")
                log_violation(violation, advice, code)
        except KeyboardInterrupt:
            print('\n通知デーモンを終了しました')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
