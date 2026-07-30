import random
import time
import argparse
import sys
from threading import Thread
try:
    from plyer import notification
except ImportError:
    print("plyerモジュールが必要です。'pip install plyer'でインストールしてください。", file=sys.stderr)
    sys.exit(1)

VIOLATION_MESSAGES = [
    "あなたの椅子、座りすぎライセンス違反を検出しました。直ちに立ち上がってください。",
    "コーヒーブレイク無許可利用を検出しました。管理者に連絡してください。",
    "謎のキーボード配列違反が発生しました。再起動をおすすめします。",
    "OS標準フォント以外の利用が検出されました。違反ポイント加算中。",
    "マウスのクリック回数が1日上限を超過しました。ご注意ください。",
    "タスクバーのアイコン数が規定値を超えています。整理してください。",
    "キーボードショートカット無断拡張違反。管理者権限が必要です。",
    "スクリーンショット乱用違反が発生しました。",
    "ウィンドウ切替速度違反。OS推奨値を守ってください。",
    "仮想デスクトップの過剰生成違反。制限を超えています。",
    "壁紙の無断変更違反。デフォルトに戻してください。",
    "USB機器の抜き差し回数が多すぎます。違反記録中。",
    "OSアップデート先延ばし違反。すぐに更新してください。",
    "ディスプレイ明るさ調整違反。推奨値を超えています。"
]

TITLE = "OSライセンス違反警告"

class AlertLogger:
    def __init__(self):
        self.logs = []

    def log(self, msg):
        ts = time.strftime('%Y-%m-%d %H:%M:%S')
        self.logs.append({'time': ts, 'message': msg})

    def list_logs(self):
        return self.logs

    def summary(self):
        return f"合計{len(self.logs)}件の違反警告が発生しました。"

logger = AlertLogger()


def random_interval(min_sec=60, max_sec=300):
    return random.randint(min_sec, max_sec)


def show_notification(message):
    notification.notify(
        title=TITLE,
        message=message,
        app_name="FakeOSLicenseAlert",
        timeout=8
    )
    logger.log(message)


def alert_once():
    msg = random.choice(VIOLATION_MESSAGES)
    show_notification(msg)


def alert_loop(count=None, min_interval=60, max_interval=300):
    i = 0
    while count is None or i < count:
        alert_once()
        i += 1
        interval = random_interval(min_interval, max_interval)
        time.sleep(interval)


def cli():
    parser = argparse.ArgumentParser(description="謎のOSライセンス違反警告をデスクトップ通知で表示するジョークスクリプト")
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='1回だけ違反警告を表示')
    parser_alert.add_argument('--count', type=int, default=1, help='表示回数 (デフォルト1)')

    parser_loop = subparsers.add_parser('loop', help='定期的に違反警告を表示')
    parser_loop.add_argument('--min-interval', type=int, default=60, help='最短間隔(秒)')
    parser_loop.add_argument('--max-interval', type=int, default=300, help='最長間隔(秒)')
    parser_loop.add_argument('--count', type=int, default=None, help='表示回数 (未指定で無限)')

    parser_list = subparsers.add_parser('list', help='発生した違反警告の履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='違反警告の発生件数サマリ')

    args = parser.parse_args()

    if args.command == 'alert':
        for _ in range(args.count):
            alert_once()
    elif args.command == 'loop':
        try:
            alert_loop(count=args.count, min_interval=args.min_interval, max_interval=args.max_interval)
        except KeyboardInterrupt:
            print("\n通知ループを中断しました。")
    elif args.command == 'list':
        logs = logger.list_logs()
        if not logs:
            print("違反警告履歴はありません。")
        else:
            for l in logs:
                print(f"[{l['time']}] {l['message']}")
    elif args.command == 'summary':
        print(logger.summary())
    else:
        parser.print_help()

if __name__ == '__main__':
    cli()
