import sys
import time
import random
import argparse
import threading
from datetime import datetime

try:
    from plyer import notification
except ImportError:
    print("plyerモジュールが必要です。pip install plyer でインストールしてください。", file=sys.stderr)
    sys.exit(1)

FAKE_ALERTS = [
    "CPU温存のため10分間タイピング禁止",
    "マウス移動過多: 省エネモード発動中",
    "電力節約のため思考も控えめにお願いします",
    "ディスプレイ輝度自動減光中。目を細めてご利用ください",
    "無意味なクリックが多発しています。省エネのため自重を推奨",
    "省電力のため、今から5分間だけ深呼吸してください",
    "OSが自動的にアイドル状態へ移行します。動かないでください",
    "エネルギー節約のため、今は何もしないでください",
    "CPU温度が低下中: そのまま静かにお過ごしください",
    "バッテリー節約のため、画面を見つめる時間を減らしましょう",
    "省エネモード: 余計な思考やアイデアの発生を抑制中",
    "パワーセーブ発動: キーボード入力を控えてください",
    "省エネのため、しばらくマウスを手放してください",
    "OS省電力警告: まばたき回数を減らしてください",
    "電力節約のため、心拍数を下げてください"
]

HISTORY = []

DEFAULT_INTERVAL = 600  # 10分(秒)
MIN_INTERVAL = 60       # 1分
MAX_INTERVAL = 1800     # 30分


def send_fake_alert(alert_text=None):
    if alert_text is None:
        alert_text = random.choice(FAKE_ALERTS)
    title = "OSパワーセーバー警告"
    notification.notify(
        title=title,
        message=alert_text,
        app_name="FakePowerSaver",
        timeout=10
    )
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    HISTORY.append((timestamp, alert_text))
    print(f"[{timestamp}] [通知] {title}: {alert_text}")


def alert_loop(interval, stop_event):
    while not stop_event.is_set():
        send_fake_alert()
        for _ in range(interval):
            if stop_event.is_set():
                break
            time.sleep(1)


def list_history():
    if not HISTORY:
        print("通知履歴はありません。")
        return
    for ts, msg in HISTORY:
        print(f"{ts} | {msg}")


def summary():
    print(f"通知回数: {len(HISTORY)}")
    unique = set(msg for _, msg in HISTORY)
    print(f"ユニークな通知内容: {len(unique)}件")
    print("最近の通知:")
    for ts, msg in HISTORY[-5:]:
        print(f"  {ts} | {msg}")


def main():
    parser = argparse.ArgumentParser(description="ランダムな偽パワーセーバー警告をデスクトップ通知するスクリプト")
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='定期的に偽警告を通知')
    parser_run.add_argument('--interval', type=int, default=DEFAULT_INTERVAL, help='通知間隔(秒)')

    parser_test = subparsers.add_parser('test', help='即時で偽警告を1回通知')

    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知履歴のサマリー')

    if len(sys.argv) == 1:
        # デフォルトはrun
        args = parser.parse_args(['run'])
    else:
        args = parser.parse_args()

    if args.command == 'run':
        interval = args.interval
        if interval < MIN_INTERVAL or interval > MAX_INTERVAL:
            print(f"通知間隔は{MIN_INTERVAL}～{MAX_INTERVAL}秒の範囲で指定してください。", file=sys.stderr)
            sys.exit(1)
        stop_event = threading.Event()
        try:
            print(f"ランダム偽パワーセーバー警告を{interval}秒ごとに通知します。Ctrl+Cで終了")
            alert_loop(interval, stop_event)
        except KeyboardInterrupt:
            print("\n通知を終了しました。")
            stop_event.set()
    elif args.command == 'test':
        send_fake_alert()
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
