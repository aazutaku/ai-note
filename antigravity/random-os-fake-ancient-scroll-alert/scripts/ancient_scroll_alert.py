import sys
import random
import time
import argparse
import platform
import subprocess
import os
from datetime import datetime

SCROLL_PREFIX = '[古文書巻物通知]'
DIRECTIONS = ['西', '東', '南', '北', '中央', '隠れ里', '遥か彼方', '深き森', '静寂の谷', '天空']
SUBJECTS = [
    'コードベース', 'モジュール', '依存関係', 'テストケース', 'ログ', '関数', '変数', 'バージョン', 'パッチ', 'リポジトリ',
    'プロセス', '設定ファイル', 'ビルド', 'API', 'デーモン', 'パイプライン', 'ジョブ', 'スクリプト', 'コンフィグ', 'キャッシュ'
]
OMENS = [
    'バグの兆し', '伝説の関数現る', '静かな異変', '謎の預言', '沈黙の影', '不可思議な動作', '警告の風', '更新の予感',
    '混沌の気配', '安寧のしるし', '予期せぬ変化', '古き知恵の囁き', '未知のエラー', '闇のパッチ', '光のリファクタ',
    '古代の警鐘', '未来の影', '忘れられしバージョン', '幻のデバッグ', '秘められたバグ'
]

EXTRA_LINES = [
    '巻物を開く者、真理に至るべし。',
    'この預言、心に刻むべし。',
    '古き者の声が響く。',
    '静かなる観察者に幸いあれ。',
    '時の彼方より警告す。',
    '巻物の端に記されし言葉。'
]

HISTORY_FILE = os.path.expanduser('~/.ancient_scroll_alert_history')


def generate_scroll_message():
    direction = random.choice(DIRECTIONS)
    subject = random.choice(SUBJECTS)
    omen = random.choice(OMENS)
    line = f"{SCROLL_PREFIX} {direction}の{subject}に{omen}。"
    # 20%の確率で追加の古文書風一文を加える
    if random.random() < 0.2:
        line += f"\n{random.choice(EXTRA_LINES)}"
    return line


def show_notification(message):
    system = platform.system()
    try:
        if system == 'Darwin':  # macOS
            subprocess.run(['osascript', '-e', f'display notification "{message}" with title "巻物預言"'], check=True)
        elif system == 'Linux':
            subprocess.run(['notify-send', '巻物預言', message], check=True)
        elif system == 'Windows':
            # Windows 10+ Toast通知
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("巻物預言", message, duration=5)
            except ImportError:
                print(message)
        else:
            print(message)
    except Exception as e:
        print(f"[通知失敗] {e}\n{message}")


def log_history(message):
    try:
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now().isoformat()}\t{message.replace(chr(10), ' ')}\n")
    except Exception:
        pass


def list_history(limit=10):
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[-limit:]:
                print(line.strip())
    except Exception:
        print("履歴がありません。")


def summary_history():
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"巻物通知履歴: {len(lines)}件")
            directions = {}
            for line in lines:
                for d in DIRECTIONS:
                    if f'{d}の' in line:
                        directions[d] = directions.get(d, 0) + 1
            for d, cnt in directions.items():
                print(f"{d}: {cnt}回")
    except Exception:
        print("履歴がありません。")


def main():
    parser = argparse.ArgumentParser(description='謎のOS公式・古文書巻物通知スクリプト')
    subparsers = parser.add_subparsers(dest='command', required=False)

    parser_log = subparsers.add_parser('log', help='今すぐ巻物通知を表示')
    parser_log.add_argument('--count', type=int, default=1, help='通知回数')
    parser_log.add_argument('--interval', type=float, default=0, help='通知間隔(秒)')
    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_list.add_argument('--limit', type=int, default=10, help='表示件数')
    parser_summary = subparsers.add_parser('summary', help='通知履歴の集計')

    args = parser.parse_args()
    if args.command == 'log' or args.command is None:
        count = getattr(args, 'count', 1)
        interval = getattr(args, 'interval', 0)
        for _ in range(count):
            msg = generate_scroll_message()
            print(msg)
            show_notification(msg)
            log_history(msg)
            if interval > 0 and _ < count - 1:
                time.sleep(interval)
    elif args.command == 'list':
        list_history(args.limit)
    elif args.command == 'summary':
        summary_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
