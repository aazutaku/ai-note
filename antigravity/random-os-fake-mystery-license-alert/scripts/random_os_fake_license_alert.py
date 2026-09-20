import random
import time
import argparse
import sys
from threading import Thread

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

FAKE_LICENSES = [
    {
        'title': 'OSライセンス通知',
        'body': 'Caps Lock の試用ライセンスが本日で失効しました。継続利用には追加認証が必要です。'
    },
    {
        'title': 'OSライセンス警告',
        'body': 'Ctrlキーの年間ライセンスが期限切れとなりました。操作の一部が制限される可能性があります。'
    },
    {
        'title': 'OSライセンス通知',
        'body': 'NumPad拡張機能のサポート期間が終了しました。再アクティベートを推奨します。'
    },
    {
        'title': 'OSライセンス警告',
        'body': 'F13キーのベータライセンスが期限切れです。正式ライセンス取得をご検討ください。'
    },
    {
        'title': 'OSライセンス通知',
        'body': 'Scroll Lock 機能の体験版が終了しました。アップグレードが必要です。'
    },
    {
        'title': 'OSライセンス警告',
        'body': 'Print Screen キーの利用権が本日失効しました。詳細は管理者まで。'
    },
    {
        'title': 'OSライセンス通知',
        'body': 'Insertキーのサブスクリプションが期限切れです。自動更新は行われません。'
    },
    {
        'title': 'OSライセンス警告',
        'body': 'Functionキー群のライセンスが一部失効しました。ご注意ください。'
    },
    {
        'title': 'OSライセンス通知',
        'body': 'テンキー区画の利用ライセンスが本日で終了します。再取得を推奨します。'
    },
    {
        'title': 'OSライセンス警告',
        'body': 'Altキーの法人ライセンスが期限切れです。個人利用は継続可能です。'
    },
]


def show_notification(title, body):
    if PLYER_AVAILABLE:
        notification.notify(
            title=title,
            message=body,
            app_name='FakeOSLicense',
            timeout=8
        )
    else:
        print(f"[ALERT] {title}\n{body}\n")


def random_alert_loop(min_interval=600, max_interval=1800, stop_after=None):
    """
    min_interval, max_interval: seconds between alerts (10-30min default)
    stop_after: seconds, or None for infinite
    """
    start_time = time.time()
    while True:
        interval = random.randint(min_interval, max_interval)
        time.sleep(interval)
        license_info = random.choice(FAKE_LICENSES)
        show_notification(license_info['title'], license_info['body'])
        if stop_after is not None and (time.time() - start_time) > stop_after:
            break


def preview_alerts(count=3):
    for i in range(count):
        license_info = random.choice(FAKE_LICENSES)
        show_notification(license_info['title'], license_info['body'])
        time.sleep(1)


def list_alerts():
    for idx, lic in enumerate(FAKE_LICENSES):
        print(f"{idx+1}. {lic['title']} : {lic['body']}")


def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Mystery License Alert Skill')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='バックグラウンドでランダム通知を発生させる')
    parser_run.add_argument('--min', type=int, default=600, help='通知間隔の最小秒数 (デフォルト600=10分)')
    parser_run.add_argument('--max', type=int, default=1800, help='通知間隔の最大秒数 (デフォルト1800=30分)')
    parser_run.add_argument('--duration', type=int, default=None, help='稼働時間(秒)。指定しなければ無限')

    parser_preview = subparsers.add_parser('preview', help='サンプル通知を即時に数件表示')
    parser_preview.add_argument('--count', type=int, default=3, help='表示件数')

    parser_list = subparsers.add_parser('list', help='通知メッセージ一覧を表示')

    args = parser.parse_args()

    if args.command == 'run':
        print(f"[Info] Fake OS License Alert: ランダム通知を開始します (Ctrl+Cで終了)")
        try:
            random_alert_loop(min_interval=args.min, max_interval=args.max, stop_after=args.duration)
        except KeyboardInterrupt:
            print("\n[Info] 通知を終了しました。")
    elif args.command == 'preview':
        preview_alerts(count=args.count)
    elif args.command == 'list':
        list_alerts()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
