import os
import sys
import json
import random
import argparse
import datetime
import subprocess
from pathlib import Path

HISTORY_PATH = Path.home() / '.random_os_horoscope_history.json'

LUCKY_COMMANDS = [
    'ls', 'cd', 'git status', 'grep', 'cat', 'vim', 'nano', 'pwd', 'docker ps', 'make',
    'curl', 'python', 'tree', 'rm', 'mv', 'cp', 'ssh', 'htop', 'ps aux', 'killall'
]

FORTUNES = [
    '今日はバグ回避率が{percent}%上昇します。',
    'コードレビュー運が絶好調。積極的に依頼を！',
    '依存関係のトラブルに要注意。慎重なアップデートを。',
    '新しいIDE拡張機能を試すと吉。',
    'コミットメッセージが冴え渡る一日。',
    '設計書の読み返しが開運のカギ。',
    'ペアプロで思わぬ発見がありそう。',
    'デプロイ運が高まっています。',
    '今日はレビューコメントが優しくなります。',
    'コード整形ツールが幸運を呼びます。',
    'CI/CDパイプラインが順調に流れる予感。',
    'バグ報告は早めが吉。',
    '新規プロジェクト開始に最適な日。',
    '技術書を読むとスキルアップ運アップ。',
    'リファクタリング運が上昇中。',
    'コーヒーブレイクがひらめきを呼ぶでしょう。'
]

WARNINGS = [
    '仕様変更星が逆行中。コミット前にREADMEを確認！',
    '依存パッケージ流星群接近。アップデートは慎重に。',
    'マージコンフリクト座が活発化。こまめなpull推奨。',
    'API制限星が低迷。リクエストは控えめに。',
    'ネットワーク障害星が微妙に影響中。',
    'レビュー待ち渋滞発生。気長に待ちましょう。',
    'ドキュメント星が薄め。仕様確認を怠らずに。',
    'タイポ星が接近中。スペルチェックを忘れずに。',
    'OSアップデート星が逆行。再起動は計画的に。',
    'エラー星が不安定。ログをこまめに確認。'
]

BORDER = '─────────────────────────────'


def load_history():
    if HISTORY_PATH.exists():
        try:
            with open(HISTORY_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_history(history):
    try:
        with open(HISTORY_PATH, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[WARN] 履歴保存に失敗: {e}")


def generate_fortune():
    percent = random.randint(5, 30)
    fortune = random.choice(FORTUNES)
    if '{percent}' in fortune:
        fortune = fortune.format(percent=percent)
    return fortune


def generate_notification():
    fortune = generate_fortune()
    lucky = random.choice(LUCKY_COMMANDS)
    warning = random.choice(WARNINGS)
    lines = [
        BORDER,
        '【OS星占い通知】',
        f'運勢：{fortune}',
        f'ラッキーコマンド：{lucky}',
        f'注意：{warning}',
        BORDER
    ]
    return '\n'.join(lines)


def show_terminal_notification(msg):
    print(msg)


def show_os_notification(title, msg):
    # macOS
    if sys.platform == 'darwin':
        script = f'display notification "{msg}" with title "{title}"'
        try:
            subprocess.run(['osascript', '-e', script], check=True)
        except Exception as e:
            print(f"[WARN] OS通知失敗: {e}")
    # Linux (notify-send)
    elif sys.platform.startswith('linux'):
        try:
            subprocess.run(['notify-send', title, msg], check=True)
        except Exception as e:
            print(f"[WARN] OS通知失敗: {e}")
    # Windows (toast)
    elif sys.platform.startswith('win'):
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, msg, duration=5)
        except ImportError:
            print("[WARN] win10toastが未インストールのため、OS通知をスキップします。pip install win10toast で導入可能です。")
        except Exception as e:
            print(f"[WARN] OS通知失敗: {e}")
    else:
        print("[INFO] このOSではOS通知がサポートされていません。")


def already_notified_today(history):
    today = datetime.date.today().isoformat()
    return history.get('last_notified') == today


def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Horoscope Notifier')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('notify', help='今日の星占い通知を表示')
    subparsers.add_parser('history', help='過去の通知履歴を表示')
    subparsers.add_parser('reset', help='履歴をリセット')

    args = parser.parse_args()
    history = load_history()

    if args.command == 'notify' or args.command is None:
        if already_notified_today(history):
            msg = history.get('last_message', '(本日の通知は既に表示済みです)')
        else:
            msg = generate_notification()
            history['last_notified'] = datetime.date.today().isoformat()
            history['last_message'] = msg
            if 'log' not in history:
                history['log'] = []
            history['log'].append({'date': history['last_notified'], 'message': msg})
            save_history(history)
        show_terminal_notification(msg)
        show_os_notification('OS星占い', msg.replace('\n', ' '))
    elif args.command == 'history':
        log = history.get('log', [])
        if not log:
            print('履歴はありません。')
        else:
            print('=== OS星占い通知履歴 ===')
            for entry in log[-10:]:
                print(f"{entry['date']}\n{entry['message']}\n")
    elif args.command == 'reset':
        save_history({})
        print('履歴をリセットしました。')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
