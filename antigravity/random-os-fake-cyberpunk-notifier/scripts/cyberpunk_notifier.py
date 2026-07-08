import sys
import argparse
import random
import time
import platform
import threading

# OSごとの通知モジュール準備
def get_notifier():
    current_os = platform.system()
    if current_os == 'Windows':
        try:
            from win10toast import ToastNotifier
            return ToastNotifier()
        except ImportError:
            print('win10toast が必要です: pip install win10toast')
            sys.exit(1)
    elif current_os == 'Darwin':
        try:
            import pync
            return pync
        except ImportError:
            print('pync が必要です: pip install pync')
            sys.exit(1)
    elif current_os == 'Linux':
        try:
            import notify2
            notify2.init('Cyberpunk Notifier')
            return notify2
        except ImportError:
            print('notify2 が必要です: pip install notify2')
            sys.exit(1)
    else:
        print('未対応OSです')
        sys.exit(1)

# サイバーパンク風の通知メッセージ生成
def generate_notification():
    titles = [
        'ニューロン接続不良を検出',
        'シンセ脳波警告',
        'クローム義手アップデート推奨',
        'バイオウェア温度異常',
        'データシャード破損警告',
        'サイバーデッキ再起動推奨',
        'ホログラム投影エラー',
        'AIパーソナリティ競合',
        'ナノマシン活動低下',
        'メンタル・ファイアウォール侵害',
        'リフレックスブースター異常',
        '光学迷彩バッテリー低下',
        'クローム義眼キャリブレーション失敗',
        'ネットランナー認証失敗',
        '仮想人格同期エラー'
    ]
    bodies = [
        'システムは脳内ニューロン接続の不安定化を検出しました。バイオウェア再起動を推奨します。',
        '異常なシンセ脳波パターンを検出。メンタル・ファイアウォールの強化を推奨。',
        '最新のクローム義手ドライバが利用可能です。アップデートをお勧めします。',
        'バイオウェアの温度が規定値を超えました。冷却システムの点検を推奨します。',
        'データシャードの一部が破損しています。バックアップを確認してください。',
        'サイバーデッキの応答が遅延しています。再起動を推奨します。',
        'ホログラム投影に失敗しました。プロジェクターモジュールの再設定を推奨。',
        'AIパーソナリティ間で競合が発生しました。優先順位を再設定してください。',
        'ナノマシン活動が低下しています。補充を検討してください。',
        'メンタル・ファイアウォールが外部からの侵害を検出しました。即時対策を推奨。',
        'リフレックスブースターの応答速度が低下しています。診断を実施してください。',
        '光学迷彩バッテリーが残り10%です。充電を推奨します。',
        'クローム義眼のキャリブレーションに失敗しました。再調整が必要です。',
        'ネットランナー認証に失敗しました。アクセス権を確認してください。',
        '仮想人格との同期にエラーが発生しました。再同期を推奨します。'
    ]
    idx = random.randint(0, len(titles) - 1)
    return titles[idx], bodies[idx]

# 通知を表示する関数
def show_notification(notifier, title, body):
    current_os = platform.system()
    if current_os == 'Windows':
        notifier.show_toast(title, body, duration=6, threaded=True)
    elif current_os == 'Darwin':
        notifier.notify(body, title=title)
    elif current_os == 'Linux':
        n = notifier.Notification(title, body)
        n.set_timeout(6000)
        n.show()

# 通知履歴を保持する
notification_history = []

def log_notification(title, body):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    notification_history.append({'time': timestamp, 'title': title, 'body': body})

# 通知をランダムな間隔で自動発火
def auto_notify_loop(notifier, min_interval, max_interval, count):
    for _ in range(count):
        title, body = generate_notification()
        show_notification(notifier, title, body)
        log_notification(title, body)
        interval = random.uniform(min_interval, max_interval)
        time.sleep(interval)

# 履歴表示
def print_history(limit=None):
    print('--- 通知履歴 ---')
    entries = notification_history[-limit:] if limit else notification_history
    for entry in entries:
        print(f"[{entry['time']}] {entry['title']} : {entry['body']}")

# サマリー表示
def print_summary():
    print(f'通知回数: {len(notification_history)}')
    titles = set([entry['title'] for entry in notification_history])
    print(f'ユニーク通知種別: {len(titles)}')

# CLIエントリポイント
def main():
    parser = argparse.ArgumentParser(description='サイバーパンク風架空OS通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    notify_parser = subparsers.add_parser('notify', help='ランダム通知を一定回数発火')
    notify_parser.add_argument('--min-interval', type=float, default=30, help='通知間隔の最小秒数')
    notify_parser.add_argument('--max-interval', type=float, default=120, help='通知間隔の最大秒数')
    notify_parser.add_argument('--count', type=int, default=5, help='通知回数')

    list_parser = subparsers.add_parser('list', help='通知履歴を表示')
    list_parser.add_argument('--limit', type=int, default=None, help='直近N件のみ表示')

    summary_parser = subparsers.add_parser('summary', help='通知サマリーを表示')

    args = parser.parse_args()
    notifier = get_notifier()

    if args.command == 'notify':
        auto_notify_loop(notifier, args.min_interval, args.max_interval, args.count)
    elif args.command == 'list':
        print_history(args.limit)
    elif args.command == 'summary':
        print_summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
