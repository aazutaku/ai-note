import random
import argparse
import sys
import platform
import subprocess
from typing import List

# BGMタイトル生成用データ
BGM_PREFIXES = [
    '第3会議室の', 'Cドライブ', '未定義変数の', '再起動前夜の', 'メモリ不足の',
    '仮想環境の', 'システム管理者の', '深夜残業の', 'バグ修正中の', 'ログイン画面の',
    'ファイル転送中の', 'ネットワーク不調の', 'アップデート待ちの', 'パーミッション拒否の',
    'プロセス監視の', '無限ループの', 'セッション切断の', 'デバッグ中の', 'サーバーダウンの',
    'バックアップ直前の', 'コマンド失敗の', 'パスワード忘却の', 'CPU暴走の', '空き容量ゼロの'
]
BGM_SUFFIXES = [
    '静寂', '幻想曲', 'バラード', 'ワルツ', '夜想曲', 'エチュード', 'ソナタ', '協奏曲',
    'セレナーデ', 'カプリッチョ', 'マーチ', 'インテルメッツォ', 'カンタータ', 'レクイエム',
    'メヌエット', 'パストラーレ', 'カノン', 'トッカータ', 'フーガ', 'リチェルカーレ'
]

# OS通知送信

def send_os_notification(title: str, message: str):
    current_os = platform.system()
    try:
        if current_os == 'Darwin':  # macOS
            subprocess.run([
                'osascript', '-e', f'display notification "{message}" with title "{title}"'
            ], check=True)
        elif current_os == 'Linux':
            subprocess.run([
                'notify-send', title, message
            ], check=True)
        elif current_os == 'Windows':
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)
        else:
            print(f"[{title}] {message}")
    except Exception as e:
        print(f"[通知失敗] {title}: {message} ({e})")

# BGMタイトル生成

def generate_bgm_title() -> str:
    prefix = random.choice(BGM_PREFIXES)
    suffix = random.choice(BGM_SUFFIXES)
    return f'{prefix}{suffix}'

# 通知メッセージ生成

def format_notification(title: str) -> str:
    return f"[OS公式通知] 本日の作業用BGM: 『{title}』"

# CLIサブコマンド: log, list, summary (ダミーで履歴管理)

class AlertHistory:
    def __init__(self):
        self.history: List[str] = []

    def add(self, title: str):
        self.history.append(title)

    def list(self):
        for i, t in enumerate(self.history):
            print(f"{i+1}. {t}")

    def summary(self):
        print(f"合計 {len(self.history)} 件のBGMタイトルが生成されました。")

# メイン関数

def main():
    parser = argparse.ArgumentParser(description='謎のOS公式BGM推奨通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='BGM通知を1回表示')
    parser_alert.add_argument('--os-notify', action='store_true', help='OS通知も送信')
    parser_alert.add_argument('--count', type=int, default=1, help='通知回数')

    subparsers.add_parser('list', help='生成済みBGMタイトル一覧')
    subparsers.add_parser('summary', help='生成履歴のサマリー')

    args = parser.parse_args()
    history = AlertHistory()

    if args.command == 'alert':
        for _ in range(args.count):
            title = generate_bgm_title()
            msg = format_notification(title)
            print(msg)
            if args.os_notify:
                send_os_notification('OS公式通知', f'本日の作業用BGM: 『{title}』')
            history.add(title)
    elif args.command == 'list':
        history.list()
    elif args.command == 'summary':
        history.summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
