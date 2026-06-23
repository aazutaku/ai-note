import sys
import os
import random
import platform
import subprocess
import argparse
import datetime
import json

MESSAGES = [
    'Wi-Fiの波動が干渉しています。',
    'コードレビューは宇宙人の監視下にあります。',
    '本日15時、全てのバグが覚醒します。',
    'あなたのマウスは政府の追跡装置です。',
    'デプロイのたびに時空が歪みます。',
    'キーボードのF5は次元転移ボタンです。',
    'Slackの通知は異次元から送られています。',
    'あなたのターミナルは監視されています。',
    'バグは自己増殖します。',
    '本日のコミットはAIに記録されています。',
    'ディスプレイの明るさは陰謀の証拠です。',
    'あなたのエディタは感情を持っています。',
    'リリース日は毎回宇宙の法則に従います。',
    '全てのパスワードは猫によって管理されています。',
    '開発サーバーは異世界と接続されています。',
    'あなたの椅子は真実を知っています。',
    '午前3時に全てのログが覚醒します。',
    'コードのバグは月の満ち欠けに影響されます。',
    'VPN接続はパラレルワールドへの扉です。',
    'あなたのGitHubアカウントは未来人に観測されています。'
]

LOG_FILE = os.path.join(os.path.dirname(__file__), 'conspiracy_alert_log.json')


def send_notification(message):
    sys_platform = platform.system()
    try:
        if sys_platform == 'Linux':
            subprocess.run(['notify-send', '[通知]', message], check=True)
        elif sys_platform == 'Darwin':
            script = f'display notification "{message}" with title "通知"'
            subprocess.run(['osascript', '-e', script], check=True)
        elif sys_platform == 'Windows':
            try:
                from win10toast import ToastNotifier
            except ImportError:
                print('win10toastがインストールされていません。pip install win10toast を実行してください。')
                return
            toaster = ToastNotifier()
            toaster.show_toast('通知', message, duration=5, threaded=True)
        else:
            print(f'未対応OS: {sys_platform}')
    except Exception as e:
        print(f'通知送信エラー: {e}')


def log_message(message):
    now = datetime.datetime.now().isoformat()
    entry = {'timestamp': now, 'message': message}
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                logs = json.load(f)
        except Exception:
            logs = []
    logs.append(entry)
    try:
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f'ログ保存エラー: {e}')


def list_logs():
    if not os.path.exists(LOG_FILE):
        print('通知履歴はありません。')
        return
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            logs = json.load(f)
        for entry in logs:
            print(f"[{entry['timestamp']}] {entry['message']}")
    except Exception as e:
        print(f'履歴表示エラー: {e}')


def summary_logs():
    if not os.path.exists(LOG_FILE):
        print('通知履歴はありません。')
        return
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            logs = json.load(f)
        print(f'通知発生回数: {len(logs)}')
        days = {}
        for entry in logs:
            day = entry['timestamp'][:10]
            days[day] = days.get(day, 0) + 1
        print('日別通知回数:')
        for day, count in sorted(days.items()):
            print(f'  {day}: {count}')
        print('直近5件:')
        for entry in logs[-5:]:
            print(f"  [{entry['timestamp']}] {entry['message']}")
    except Exception as e:
        print(f'サマリー表示エラー: {e}')


def send_random_alert():
    message = random.choice(MESSAGES)
    send_notification(message)
    log_message(message)
    print(f'[通知] {message}')


def main():
    parser = argparse.ArgumentParser(description='Random Desktop Conspiracy Alert')
    subparsers = parser.add_subparsers(dest='command')

    send_parser = subparsers.add_parser('send', help='ランダムな陰謀論アラートを即時通知')
    list_parser = subparsers.add_parser('list', help='過去の通知履歴を表示')
    summary_parser = subparsers.add_parser('summary', help='通知履歴のサマリーを表示')

    args = parser.parse_args()
    if args.command == 'send':
        send_random_alert()
    elif args.command == 'list':
        list_logs()
    elif args.command == 'summary':
        summary_logs()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
