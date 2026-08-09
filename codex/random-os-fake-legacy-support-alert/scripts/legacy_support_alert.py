import sys
import argparse
import random
import time
import threading
from typing import List

try:
    from plyer import notification
except ImportError:
    notification = None

LEGACY_ALERTS = [
    {
        'title': 'サポート終了通知',
        'message': 'Windows 98互換モードのサポートは本日をもって終了しました。今後はY2K非対応環境での動作保証はありません。'
    },
    {
        'title': 'サポート終了通知',
        'message': 'IE6向け最適化は永遠に封印されました。レガシーCSSハックの時代は終わりました。'
    },
    {
        'title': 'サポート終了通知',
        'message': 'フロッピー対応APIが静かに旅立ちました。FDドライブの回転音はもう聞こえません。'
    },
    {
        'title': 'サポート終了通知',
        'message': 'MS-DOSバッチファイルの自動起動サポートが終了しました。AUTOEXEC.BATは過去のものです。'
    },
    {
        'title': 'サポート終了通知',
        'message': 'Netscape Navigator 4.7向け最適化が廃止されました。Blinkタグは永遠に。'
    },
    {
        'title': 'サポート終了通知',
        'message': 'SCSI外付けMOドライブのサポートが終了しました。交換メディアの時代に別れを。'
    },
    {
        'title': 'サポート終了通知',
        'message': 'BASICインタープリタの標準搭載が終了しました。10 PRINT "HELLO" の時代は終わりました。'
    },
    {
        'title': 'サポート終了通知',
        'message': 'Windows XP Lunaテーマのサポートがついに終了しました。青いスタートボタンに感謝を。'
    },
    {
        'title': 'サポート終了通知',
        'message': 'レガシーCOMポート経由のプリンタサポートが廃止されました。紙詰まりにさようなら。'
    },
    {
        'title': 'サポート終了通知',
        'message': 'ActiveXコントロールのサポートが完全終了。Webセキュリティ向上のため。'
    },
]

HISTORY: List[dict] = []


def show_notification(alert: dict):
    if notification:
        notification.notify(
            title=alert['title'],
            message=alert['message'],
            timeout=7
        )
    else:
        print(f"[{alert['title']}]")
        print(alert['message'])
        print("---")


def random_alert() -> dict:
    alert = random.choice(LEGACY_ALERTS)
    HISTORY.append(alert)
    return alert


def log_alert(alert: dict):
    # ローカルファイル保存はしない設計
    pass


def list_alerts():
    if not HISTORY:
        print("まだ通知履歴はありません。")
        return
    for i, alert in enumerate(HISTORY, 1):
        print(f"{i}. {alert['title']} : {alert['message']}")


def summary_alerts():
    print(f"通知発火回数: {len(HISTORY)}")
    titles = set(a['title'] for a in HISTORY)
    print(f"種類: {len(titles)}")


def trigger_alert():
    alert = random_alert()
    show_notification(alert)
    log_alert(alert)


def periodic_mode(interval: int = 60):
    try:
        while True:
            trigger_alert()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("periodic modeを終了します。")


def parse_args():
    parser = argparse.ArgumentParser(description='ランダムなレガシーOSサポート終了通知を表示します。')
    subparsers = parser.add_subparsers(dest='command')

    trigger_parser = subparsers.add_parser('trigger', help='即座に通知を発火')
    periodic_parser = subparsers.add_parser('periodic', help='一定間隔で通知を発火')
    periodic_parser.add_argument('--interval', type=int, default=60, help='通知間隔(秒)')
    list_parser = subparsers.add_parser('list', help='通知履歴を表示')
    summary_parser = subparsers.add_parser('summary', help='通知履歴のサマリを表示')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'trigger':
        trigger_alert()
    elif args.command == 'periodic':
        periodic_mode(args.interval)
    elif args.command == 'list':
        list_alerts()
    elif args.command == 'summary':
        summary_alerts()
    else:
        print('コマンドを指定してください。例: trigger, periodic, list, summary')

if __name__ == '__main__':
    main()
