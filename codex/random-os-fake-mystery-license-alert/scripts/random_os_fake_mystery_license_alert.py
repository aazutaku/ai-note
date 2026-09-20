import os
import sys
import time
import random
import argparse
import threading

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

LICENSE_ITEMS = [
    'Ctrlキー', 'Caps Lock', 'NumPad', '仮想RAM拡張モジュール', 'システム時刻同期サービス',
    'Altキー', 'Fnキー', 'Bluetooth Stack', 'USB Root Hub', 'タッチパッド感度調整',
    'スクリーンショット機能', 'クリップボード履歴', '仮想デスクトップ', 'ウィンドウスナップ',
    'ダークモード', 'サウンドミュート', 'バッテリー残量表示', '通知センター', 'フォントレンダラー',
    'デバイスマネージャ', 'プリンタドライバ', 'Wi-Fi自動接続', 'ネットワークプロファイル',
    'タスクスケジューラ', 'スクリーンセーバー', 'デバイス暗号化', 'マウス加速度', '仮想メモリ',
    'ログイン画面カスタマイズ', 'プロセスモニタ', 'ファイルインデックス', 'IME変換エンジン',
    'ウィンドウ透明度', 'システム通知音', 'USBデバッグ', 'システム復元', '自動アップデート'
]

MESSAGE_TEMPLATES = [
    '[ALERT] OSライセンス警告: あなたの{item}のライセンスは本日24:00をもって失効します。再認証を行ってください。',
    '[WARNING] {item}機能は試用期間を超過しました。継続利用には管理者権限が必要です。',
    '[NOTICE] {item}のライセンスが期限切れです。パフォーマンス低下の可能性があります。',
    '[ALERT] {item}の利用権が失効しました。手動設定を推奨します。',
    '[WARNING] {item}のライセンスが本日失効しました。',
    '[NOTICE] {item}の認証期限が切れています。サポート窓口へご連絡ください。',
    '[ALERT] {item}のライセンスが無効です。機能制限モードで動作します。',
    '[WARNING] {item}の利用は本日までです。アップグレードをご検討ください。',
    '[NOTICE] {item}のライセンス認証が必要です。',
    '[ALERT] {item}の試用期間が終了しました。'
]


def generate_random_message():
    item = random.choice(LICENSE_ITEMS)
    template = random.choice(MESSAGE_TEMPLATES)
    return template.format(item=item)


def send_notification(message):
    if PLYER_AVAILABLE:
        notification.notify(
            title='OSライセンス警告',
            message=message,
            app_name='random-os-fake-mystery-license-alert',
            timeout=8
        )
    else:
        # Fallback: print to stderr
        print(message, file=sys.stderr)


def alert_once(args):
    message = generate_random_message()
    send_notification(message)
    if args.log:
        with open(args.log, 'a', encoding='utf-8') as f:
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} {message}\n')


def alert_loop(args):
    count = 0
    try:
        while args.times is None or count < args.times:
            wait_sec = random.randint(args.min_interval, args.max_interval)
            time.sleep(wait_sec)
            message = generate_random_message()
            send_notification(message)
            if args.log:
                with open(args.log, 'a', encoding='utf-8') as f:
                    f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} {message}\n')
            count += 1
    except KeyboardInterrupt:
        print('Alert loop interrupted by user.')


def list_templates(args):
    print('--- 利用可能な通知テンプレート ---')
    for t in MESSAGE_TEMPLATES:
        print(f'- {t}')
    print('\n--- ライセンス対象アイテム例 ---')
    for i in LICENSE_ITEMS:
        print(f'- {i}')


def summary(args):
    print('Skill: random-os-fake-mystery-license-alert')
    print('架空のOS機能・デバイスのライセンス期限切れ通知を、ランダムなタイミング・内容で発生させます。')
    print('実害なし・通知のみ。')
    print('通知対象やテンプレートはlistコマンドで確認可能。')


def parse_args():
    parser = argparse.ArgumentParser(description='Random OS Fake Mystery License Alert')
    subparsers = parser.add_subparsers(dest='subcmd', required=True)

    parser_once = subparsers.add_parser('once', help='1回だけ通知を表示')
    parser_once.add_argument('--log', help='通知内容を指定ファイルに追記')
    parser_once.set_defaults(func=alert_once)

    parser_loop = subparsers.add_parser('loop', help='ランダム間隔で繰り返し通知')
    parser_loop.add_argument('--min-interval', type=int, default=300, help='最小待機秒数 (default: 300)')
    parser_loop.add_argument('--max-interval', type=int, default=1800, help='最大待機秒数 (default: 1800)')
    parser_loop.add_argument('--times', type=int, help='通知回数 (指定しない場合は無限)')
    parser_loop.add_argument('--log', help='通知内容を指定ファイルに追記')
    parser_loop.set_defaults(func=alert_loop)

    parser_list = subparsers.add_parser('list', help='通知テンプレートとアイテム一覧')
    parser_list.set_defaults(func=list_templates)

    parser_summary = subparsers.add_parser('summary', help='Skill概要')
    parser_summary.set_defaults(func=summary)

    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
