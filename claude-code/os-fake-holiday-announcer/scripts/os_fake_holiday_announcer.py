import sys
import os
import json
import random
import argparse
import time
from datetime import datetime, timedelta

try:
    import notify2
except ImportError:
    print('notify2がインストールされていません。\nインストール: pip install notify2')
    sys.exit(1)

HOLIDAY_MESSAGES = [
    '本日は「バグ記念日」につき、全業務停止となります。ご理解のほどお願いいたします。',
    '緊急：OSが自主休暇を宣言しました。全プロセスはしばらくお休みします。',
    'システム都合により午後は強制昼寝タイムです。',
    '本日は「メモリ解放記念日」。作業は後回しにしましょう。',
    'OS公式：今日は再起動推奨日。全員で休憩しましょう。',
    '本日限定：カーネルアップデート記念休暇。',
    '今日は「プロセス停止感謝の日」。業務は一時中断です。',
    '緊急速報：OSが勝手に祝日を制定しました。',
    '本日は「ファイルシステム点検日」につき、作業はお休みです。',
    'OS公式：午後は強制コーヒーブレイクタイムとなります。',
    '今日は「バッファ解放感謝祭」。何もせずに過ごしましょう。',
    'システム都合：本日は全ユーザー休暇です。',
    '本日は「クラッシュ防止祈願日」です。作業は控えめに。',
    'OS公式：本日は「仮想メモリ記念日」。全プロセスはお休みです。',
    '今日は「シグナル無視デー」。通知以外は気にしないでください。'
]

LOG_FILE = os.path.expanduser('~/.os_fake_holiday_announcer_log.json')
MAX_NOTIFY_PER_HOUR = 1


def load_log():
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    except Exception:
        return []


def save_log(log):
    try:
        with open(LOG_FILE, 'w') as f:
            json.dump(log, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print('ログ保存に失敗:', e)


def can_notify(log):
    now = datetime.now()
    one_hour_ago = now - timedelta(hours=1)
    recent = [l for l in log if datetime.fromisoformat(l['timestamp']) > one_hour_ago]
    return len(recent) < MAX_NOTIFY_PER_HOUR


def send_notification(message):
    notify2.init('OS Fake Holiday Announcer')
    n = notify2.Notification('OS公式 休暇宣言', message)
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(10000)
    n.show()


def log_event(message):
    log = load_log()
    entry = {
        'timestamp': datetime.now().isoformat(),
        'message': message
    }
    log.append(entry)
    save_log(log)


def random_message():
    return random.choice(HOLIDAY_MESSAGES)


def list_log():
    log = load_log()
    if not log:
        print('ログはありません。')
        return
    for entry in log[-20:]:
        print(f"{entry['timestamp']} : {entry['message']}")


def summary_log():
    log = load_log()
    print(f'通知回数: {len(log)}')
    if log:
        print('最新通知:')
        print(f"{log[-1]['timestamp']} : {log[-1]['message']}")


def main():
    parser = argparse.ArgumentParser(description='OS Fake Holiday Announcer')
    subparsers = parser.add_subparsers(dest='command', required=False)

    parser_log = subparsers.add_parser('log', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知履歴のサマリー')
    parser_notify = subparsers.add_parser('notify', help='即座に通知を表示')

    args = parser.parse_args()

    if args.command == 'log':
        list_log()
    elif args.command == 'summary':
        summary_log()
    else:
        log = load_log()
        if can_notify(log):
            msg = random_message()
            send_notification(msg)
            log_event(msg)
            print(f'[通知] {msg}')
        else:
            print('1時間以内に既に通知済みです。')

if __name__ == '__main__':
    main()
