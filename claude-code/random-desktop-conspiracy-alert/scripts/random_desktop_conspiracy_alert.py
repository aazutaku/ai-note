import random
import time
import argparse
import sys
import threading
from datetime import datetime, timedelta

try:
    from plyer import notification
except ImportError:
    print('plyerパッケージが必要です。pip install plyer でインストールしてください。')
    sys.exit(1)

CONSPIRACY_MESSAGES = [
    'Wi-Fiの波動があなたの思考を妨害しています。',
    'コードレビューは宇宙人の監視下にあります。',
    '本日15時、全てのバグが覚醒します。',
    'あなたのキーボードは秘密組織により記録されています。',
    '開発環境が量子もつれ状態に突入しました。',
    '全てのTODOコメントはAIによって解析されています。',
    'あなたのマウス操作は遠隔操作されています。',
    '本日のコミットは秘密結社の承認待ちです。',
    'デバッグログは政府機関に転送されています。',
    'このエラーは次元の歪みによるものです。',
    'あなたの画面は裏で誰かが見ています。',
    '全てのバグは陰謀の一部です。',
    'リファクタリングは時空警察の監督下にあります。',
    'APIキーは宇宙の中心で管理されています。',
    '全てのパスワードは夢の中で漏洩しています。',
    'あなたの開発環境はパラレルワールドと同期しています。',
    '本日のタスクは量子乱数で決定されました。',
    'あなたのIDEはAIによって操られています。',
    '全ての仕様変更は超常現象の影響です。',
    'あなたのバグは自己増殖を始めました。'
]

TRIGGER_KEYWORDS = [
    '集中力', 'バグ', '監視', 'Wi-Fi', '宇宙人', '秘密', '陰謀', 'エラー', 'デバッグ', 'レビュー'
]

HISTORY_FILE = '.claude/skills/random-desktop-conspiracy-alert/alert_history.log'
MAX_AUTO_ALERTS_PER_HOUR = 3


def send_notification(message):
    notification.notify(
        title='謎の陰謀論アラート',
        message=message,
        app_name='random-desktop-conspiracy-alert',
        timeout=8
    )
    log_alert(message)


def log_alert(message):
    try:
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
            f.write(f'{datetime.now().isoformat()}\t{message}\n')
    except Exception as e:
        pass  # ログ失敗は無視


def list_alerts(limit=20):
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line in lines[-limit:]:
            print(line.strip())
    except FileNotFoundError:
        print('まだアラート履歴がありません。')


def summary_alerts():
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print(f'アラート総数: {len(lines)}')
        last = lines[-1].strip() if lines else 'なし'
        print(f'最新アラート: {last}')
    except FileNotFoundError:
        print('まだアラート履歴がありません。')


def count_alerts_in_last_hour():
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        now = datetime.now()
        count = 0
        for line in reversed(lines):
            ts = line.split('\t')[0]
            t = datetime.fromisoformat(ts)
            if now - t < timedelta(hours=1):
                count += 1
            else:
                break
        return count
    except Exception:
        return 0


def auto_alert_loop():
    while True:
        # 1時間に最大MAX_AUTO_ALERTS_PER_HOUR回まで
        if count_alerts_in_last_hour() < MAX_AUTO_ALERTS_PER_HOUR:
            msg = random.choice(CONSPIRACY_MESSAGES)
            send_notification(msg)
        time.sleep(random.randint(1200, 1800))  # 20-30分間隔


def keyword_trigger(text):
    for kw in TRIGGER_KEYWORDS:
        if kw in text:
            if count_alerts_in_last_hour() < MAX_AUTO_ALERTS_PER_HOUR:
                msg = random.choice(CONSPIRACY_MESSAGES)
                send_notification(msg)
                print(f'キーワード「{kw}」でアラート発動: {msg}')
            else:
                print('今時間帯の自動アラート上限に達しています。')
            return
    print('キーワード未検出。アラートは発動しません。')


def main():
    parser = argparse.ArgumentParser(description='random-desktop-conspiracy-alert: 謎の陰謀論アラートをデスクトップ通知で爆誕させる')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='即座に陰謀論アラートを表示')
    parser_alert.add_argument('--message', '-m', type=str, help='任意のメッセージを指定')

    parser_list = subparsers.add_parser('list', help='アラート履歴を表示')
    parser_list.add_argument('--limit', '-n', type=int, default=10, help='表示件数')

    parser_summary = subparsers.add_parser('summary', help='アラート履歴のサマリを表示')

    parser_keyword = subparsers.add_parser('trigger', help='テキストからキーワード検出でアラート発動')
    parser_keyword.add_argument('text', type=str, help='判定するテキスト')

    parser_auto = subparsers.add_parser('auto', help='自動でランダムアラートを定期発動(1時間最大3回)')

    args = parser.parse_args()

    if args.command == 'alert':
        msg = args.message if args.message else random.choice(CONSPIRACY_MESSAGES)
        send_notification(msg)
        print(f'アラート発動: {msg}')
    elif args.command == 'list':
        list_alerts(args.limit)
    elif args.command == 'summary':
        summary_alerts()
    elif args.command == 'trigger':
        keyword_trigger(args.text)
    elif args.command == 'auto':
        print('自動アラートモード開始 (Ctrl+Cで停止)')
        try:
            auto_alert_loop()
        except KeyboardInterrupt:
            print('\n自動アラートモード終了')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
