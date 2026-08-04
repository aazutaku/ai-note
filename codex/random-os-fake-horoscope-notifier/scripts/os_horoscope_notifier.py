import os
import sys
import argparse
import random
import datetime
import json
import platform
import subprocess

NOTIFY_HISTORY_FILE = os.path.expanduser('~/.os_horoscope_notifier_history.json')

LUCKY_COMMANDS = [
    'ls', 'cd', 'grep', 'cat', 'git commit', 'vim', 'rm', 'mkdir', 'touch',
    'python', 'docker', 'curl', 'ssh', 'top', 'ps', 'find', 'tail', 'head', 'chmod', 'chown', 'scp'
]

FORTUNE_MESSAGES = [
    'バグ回避率が{percent}%上昇。',
    '今日の進捗は{percent}%増加の予感。',
    'コーヒーブレイク推奨。',
    'レビュー運が好調。',
    'コードリーディング力が冴える日。',
    '仕様変更星が逆行中。',
    'git pushは慎重に。',
    'テストカバレッジが自然と上昇。',
    '依存関係のトラブルに注意。',
    '新しいIDEプラグインとの出会いがあるかも。',
    'マージコンフリクト運が低下中。',
    'PRがすんなり通る可能性大。',
    'デバッグの女神が微笑む日。',
    'コードレビューで褒められるかも。',
    'CI/CDパイプラインが安定。',
    'Slack通知が多め。',
    '仕様書の読み間違いに注意。',
    'ペアプロが吉。',
    '深追いは禁物。',
    'こまめなgit commit推奨。',
]

LUCKY_ITEMS = [
    'マグカップ', 'お気に入りのキーボード', '青い付箋', 'USBメモリ', 'エディタのテーマ',
    'デバッグ用アヒル', '観葉植物', '座布団', 'イヤホン', 'コーヒー', 'メモ帳', '新しいタブ',
    'ステッカー', 'ランチパック', 'スニーカー', 'お気に入りのペン', 'マウスパッド', 'デスクライト'
]

BORDER = '=' * 27


def load_history():
    if os.path.exists(NOTIFY_HISTORY_FILE):
        try:
            with open(NOTIFY_HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_history(history):
    try:
        with open(NOTIFY_HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[WARN] 履歴保存失敗: {e}")

def already_notified_today(history):
    today = datetime.date.today().isoformat()
    return history.get('last_notify_date') == today

def update_notify_date(history):
    today = datetime.date.today().isoformat()
    history['last_notify_date'] = today
    save_history(history)

def generate_fortune():
    lucky_cmd = random.choice(LUCKY_COMMANDS)
    fortune_msg = random.choice(FORTUNE_MESSAGES)
    percent = random.randint(5, 30)
    fortune_msg = fortune_msg.format(percent=percent)
    lucky_item = random.choice(LUCKY_ITEMS)
    lines = [
        BORDER,
        'OS Horoscope Notifier',
        f'運勢: 今日は「{lucky_cmd}」コマンドが幸運を呼びます。',
        fortune_msg,
        f'ラッキーアイテム: {lucky_item}',
        BORDER
    ]
    return '\n'.join(lines)

def show_terminal_notification(msg):
    print(msg)

def show_desktop_notification(msg):
    system = platform.system()
    title = 'OS Horoscope Notifier'
    # Linux (notify-send)
    if system == 'Linux':
        try:
            subprocess.run(['notify-send', title, msg], check=True)
        except Exception as e:
            print(f"[WARN] notify-send失敗: {e}")
    # macOS (osascript)
    elif system == 'Darwin':
        try:
            script = f'display notification "{msg}" with title "{title}"'
            subprocess.run(['osascript', '-e', script], check=True)
        except Exception as e:
            print(f"[WARN] osascript失敗: {e}")
    else:
        print("[INFO] デスクトップ通知は未対応OSです。ターミナルに表示します。")
        print(msg)

def notify(args):
    history = load_history()
    if already_notified_today(history):
        if not args.force:
            print('[INFO] 今日は既に通知済みです。')
            return
    msg = generate_fortune()
    if args.desktop:
        show_desktop_notification(msg)
    else:
        show_terminal_notification(msg)
    update_notify_date(history)

def list_history(args):
    history = load_history()
    date = history.get('last_notify_date', 'なし')
    print(f'最終通知日: {date}')

def main():
    parser = argparse.ArgumentParser(description='OS Horoscope Notifier - ランダムなOS星占い通知をお届けします')
    subparsers = parser.add_subparsers(dest='command')

    notify_parser = subparsers.add_parser('notify', help='本日の星占い通知を表示')
    notify_parser.add_argument('--desktop', action='store_true', help='デスクトップ通知を利用する')
    notify_parser.add_argument('--force', action='store_true', help='1日1回制限を無視して通知')
    notify_parser.set_defaults(func=notify)

    list_parser = subparsers.add_parser('list', help='通知履歴を表示')
    list_parser.set_defaults(func=list_history)

    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
        sys.exit(1)
    args.func(args)

if __name__ == '__main__':
    main()
