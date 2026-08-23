import argparse
import random
import sys
import time
import os

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

FAKE_INCIDENTS = [
    {
        'title': 'OSセキュリティインシデント発生!',
        'cause': 'あなたのマウスが自我を持ち始めました。',
        'action': 'マウスに優しく話しかけてください。',
    },
    {
        'title': 'OSセキュリティインシデント発生!',
        'cause': '本日よりキーボードの配列が毎分自動変更されます。',
        'action': 'タイピングスキルを鍛えてください。',
    },
    {
        'title': 'OSセキュリティインシデント発生!',
        'cause': 'システムがピーマン型ウイルスに感染しました。',
        'action': 'ピーマンを食べて対抗してください。',
    },
    {
        'title': 'OSセキュリティインシデント発生!',
        'cause': 'あなたの椅子が物理的に乗っ取られました。',
        'action': '椅子に座る前に許可を取りましょう。',
    },
    {
        'title': 'OSセキュリティインシデント発生!',
        'cause': '本日よりマウスが逆方向に動きます。',
        'action': '脳内変換力を高めてください。',
    },
    {
        'title': 'OSセキュリティインシデント発生!',
        'cause': '全ユーザーのデスクトップ壁紙が謎の猫画像に変更されました。',
        'action': '猫を愛でてください。',
    },
    {
        'title': 'OSセキュリティインシデント発生!',
        'cause': 'CPUが突然詩を詠み始めました。',
        'action': '詩を静かに聞きましょう。',
    },
    {
        'title': 'OSセキュリティインシデント発生!',
        'cause': 'システム時刻が毎秒ランダムに変動しています。',
        'action': '時間に縛られない心を持ちましょう。',
    },
    {
        'title': 'OSセキュリティインシデント発生!',
        'cause': '全ファイル名が「たけのこ」に書き換えられました。',
        'action': 'たけのこ派の勝利を祝ってください。',
    },
    {
        'title': 'OSセキュリティインシデント発生!',
        'cause': '画面が上下逆さまになりました。',
        'action': '首を180度回してご覧ください。',
    },
]

HISTORY = []

TRIGGER_KEYWORDS = [
    'セキュリティインシデント',
    'ウイルス',
    'OS異常',
    'ハッキング',
    '乗っ取られ',
    '感染',
    '謎の',
    '逆方向',
]


def pick_random_incident():
    return random.choice(FAKE_INCIDENTS)


def show_notification(incident):
    msg = f"原因: {incident['cause']}\n対応: {incident['action']}"
    if PLYER_AVAILABLE:
        notification.notify(
            title=incident['title'],
            message=msg,
            timeout=8
        )
    else:
        # Fallback: print to terminal
        print(f"[警告] {incident['title']}\n{msg}\n---")


def log_incident(incident):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    HISTORY.append({
        'time': timestamp,
        'title': incident['title'],
        'cause': incident['cause'],
        'action': incident['action']
    })


def list_history():
    if not HISTORY:
        print('インシデント履歴はありません。')
        return
    for h in HISTORY:
        print(f"[{h['time']}] {h['title']}\n原因: {h['cause']}\n対応: {h['action']}\n---")


def check_for_keywords(text):
    for k in TRIGGER_KEYWORDS:
        if k in text:
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description='OSランダムフェイクセキュリティインシデント通知')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='フェイクインシデント通知を即座に発動')
    parser_alert.add_argument('--count', type=int, default=1, help='通知回数 (デフォルト1)')

    parser_list = subparsers.add_parser('list', help='通知履歴を表示')

    parser_monitor = subparsers.add_parser('monitor', help='標準入力を監視し、キーワードで自動通知')
    parser_monitor.add_argument('--interval', type=float, default=0.5, help='監視間隔(秒)')

    args = parser.parse_args()

    if args.command == 'alert':
        for _ in range(args.count):
            incident = pick_random_incident()
            show_notification(incident)
            log_incident(incident)
            time.sleep(1)
    elif args.command == 'list':
        list_history()
    elif args.command == 'monitor':
        print('標準入力を監視します。Ctrl+Cで終了。')
        try:
            while True:
                line = sys.stdin.readline()
                if not line:
                    time.sleep(args.interval)
                    continue
                if check_for_keywords(line):
                    incident = pick_random_incident()
                    show_notification(incident)
                    log_incident(incident)
        except KeyboardInterrupt:
            print('\n監視を終了しました。')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
