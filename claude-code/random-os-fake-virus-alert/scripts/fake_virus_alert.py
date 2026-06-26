import sys
import time
import random
import argparse
import threading
from datetime import datetime

try:
    from plyer import notification
except ImportError:
    print('plyerライブラリが必要です。\nインストール: pip install plyer')
    sys.exit(1)

FAKE_ALERTS = [
    ('危険: 未知のバグウイルスを検出しました！', 'この通知はジョークです。安心してください。'),
    ('注意: あなたのコードが自我を持ちました。', '念のため再起動をおすすめします（冗談です）。'),
    ('システム警告: 机の下にバグが落ちています。', '拾っても何も起きません。'),
    ('ウイルス検出: これは冗談です。安心してください。', '本物のウイルスではありません。'),
    ('重大: コーヒーがキーボードに侵入しました。', '今すぐカップを確認してください。'),
    ('警告: デバッグ中にAIが目覚めました。', '現実世界への影響はありません。'),
    ('通知: コードが「こんにちは」と話しかけています。', '返事は不要です。'),
    ('情報: バグが自己増殖を開始しました。', 'この通知はフィクションです。'),
    ('システム情報: あなたのPCは完全に安全です。', 'この通知はネタです。'),
    ('警告: 画面の向こうから誰かが見ています。', '気のせいです。')
]

LOG_FILE = None  # ログ保存は行わない


def send_fake_alert():
    title, message = random.choice(FAKE_ALERTS)
    notification.notify(
        title=title,
        message=message,
        app_name='Fake Virus Alert',
        timeout=8
    )
    print(f"[通知] {title}")


def alert_loop(interval_min=900, interval_max=3600, repeat=3):
    """
    interval_min: 最小インターバル秒（デフォルト15分）
    interval_max: 最大インターバル秒（デフォルト1時間）
    repeat: 通知回数
    """
    for i in range(repeat):
        wait = random.randint(interval_min, interval_max)
        time.sleep(wait)
        send_fake_alert()


def list_alerts():
    print("利用可能なフェイク通知一覧:")
    for i, (title, message) in enumerate(FAKE_ALERTS, 1):
        print(f"{i}. {title} - {message}")


def summary():
    print("random-os-fake-virus-alert Skill概要:")
    print("- 完全ネタ通知のみをデスクトップに表示")
    print("- 実害ゼロ、システム変更なし")
    print("- 通知内容は10種からランダム選択")
    print("- Windows/macOS/Linux対応 (plyer利用)")
    print("- ログや履歴は保存しません")


def parse_args():
    parser = argparse.ArgumentParser(description='random-os-fake-virus-alert: ネタウイルス通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='今すぐフェイク通知を表示')
    parser_alert.add_argument('--repeat', type=int, default=1, help='通知回数 (デフォルト1)')
    parser_alert.add_argument('--interval-min', type=int, default=900, help='最小インターバル秒 (デフォルト900=15分)')
    parser_alert.add_argument('--interval-max', type=int, default=3600, help='最大インターバル秒 (デフォルト3600=1時間)')

    parser_list = subparsers.add_parser('list', help='利用可能な通知一覧を表示')
    parser_summary = subparsers.add_parser('summary', help='Skill概要を表示')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'alert':
        if args.repeat == 1:
            send_fake_alert()
        else:
            # 別スレッドで通知ループを実行
            t = threading.Thread(target=alert_loop, kwargs={
                'interval_min': args.interval_min,
                'interval_max': args.interval_max,
                'repeat': args.repeat
            })
            t.daemon = True
            t.start()
            print(f"通知を{args.repeat}回、{args.interval_min}-{args.interval_max}秒間隔で実行します。")
            try:
                while t.is_alive():
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n中断されました。")
    elif args.command == 'list':
        list_alerts()
    elif args.command == 'summary':
        summary()
    else:
        print("コマンドを指定してください。例: python fake_virus_alert.py alert --repeat 2")

if __name__ == '__main__':
    main()
