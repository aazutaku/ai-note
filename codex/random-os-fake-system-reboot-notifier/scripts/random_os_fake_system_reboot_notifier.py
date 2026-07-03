import random
import sys
import argparse
import platform
from datetime import datetime

try:
    from plyer import notification
except ImportError:
    notification = None

REASONS = [
    'カーネルの気まぐれ',
    '不明なエラーコード 0xDEADBEEF',
    'メモリの気分転換',
    'OSの自己主張',
    'システムの都合',
    'CPUの気まぐれ',
    '管理者のイタズラ',
    'アップデートの衝動',
    '謎のシステムイベント',
    '予期しない例外発生',
    'AIの判断',
    'ユーザーの運命',
    '未知のプロセス干渉',
    'タイムラインの修正',
    'システムの気分転換'
]

TITLES = [
    '重要なお知らせ',
    'システムメンテナンス',
    'OSアップデート',
    '緊急通知',
    'システム警告',
    '再起動予告',
    '管理者メッセージ',
    'OSからのお願い'
]

ACTIONS = [
    '5分後にシステムは謎の理由で再起動します。',
    '3分後に全プロセスが一時停止されます。',
    '10分後に再起動が予定されています。',
    '2分後にOSが自動的に再起動します。',
    '1分後にシステムがリセットされます。',
    '7分後に全サービスが再起動されます。',
    '15分後にOSが再起動します。',
    '6分後にセッションが終了します。',
    '4分後に強制的に再起動されます。',
    '8分後にシステムが再起動します。'
]

LOG = []


def generate_notification():
    title = random.choice(TITLES)
    action = random.choice(ACTIONS)
    reason = random.choice(REASONS)
    message = f"{title}: {action}\n理由: {reason}"
    return title, action, reason, message


def send_notification(title, message):
    if notification:
        try:
            notification.notify(
                title=title,
                message=message,
                app_name='FakeSystemRebootNotifier',
                timeout=10
            )
        except Exception as e:
            print(f"[エラー] 通知送信に失敗しました: {e}")
    else:
        # plyerがない場合はstdoutに出力
        print(f"[通知] {title}: {message}")


def log_event(title, action, reason):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    LOG.append({
        'time': now,
        'title': title,
        'action': action,
        'reason': reason
    })


def list_events():
    if not LOG:
        print("[履歴] 通知履歴はありません。")
        return
    for ev in LOG:
        print(f"[{ev['time']}] {ev['title']} | {ev['action']} | 理由: {ev['reason']}")


def summary():
    print(f"合計通知回数: {len(LOG)}")
    reasons = {}
    for ev in LOG:
        reasons[ev['reason']] = reasons.get(ev['reason'], 0) + 1
    if reasons:
        print("理由別内訳:")
        for k, v in sorted(reasons.items(), key=lambda x: -x[1]):
            print(f"  {k}: {v}回")


def main():
    parser = argparse.ArgumentParser(description='謎のOS再起動通知スキル')
    subparsers = parser.add_subparsers(dest='command')

    parser_notify = subparsers.add_parser('notify', help='ランダムな再起動通知を送信')
    parser_notify.add_argument('--dry-run', action='store_true', help='通知を画面に表示せず標準出力に出す')

    subparsers.add_parser('list', help='通知履歴を表示')
    subparsers.add_parser('summary', help='通知の集計を表示')

    args = parser.parse_args()

    if args.command == 'notify' or args.command is None:
        title, action, reason, message = generate_notification()
        if getattr(args, 'dry_run', False):
            print(f"[通知] {title}: {action}\n理由: {reason}")
        else:
            send_notification(title, f"{action}\n理由: {reason}")
        log_event(title, action, reason)
    elif args.command == 'list':
        list_events()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
