import argparse
import random
import string
import sys
import time
import os
import subprocess
from datetime import datetime, timedelta

# メッセージテンプレート
TEMPLATES = [
    '重要: プリンタで“{filename}”が紙詰まりを起こしました。',
    '警告: 印刷待ちジョブが渋滞中です。トナーを補充してください。',
    'エラー: ファイル“{filename}”の印刷中に謎の紙詰まりが発生しました。',
    '注意: プリンタが“手動給紙”を要求しています。',
    '警告: プリンタが“未定義エラー”で停止しました。',
    '重大: “{filename}”の印刷が失敗しました。紙を手で給紙してください。',
    '通知: プリンタに“謎のトナー”を補充してください。',
    '警告: 印刷ジョブ“{filename}”がプリンタ内部で迷子になりました。',
    'エラー: プリンタが“紙詰まり(コード: J-404)”を検出しました。',
    '重要: “{filename}”の印刷がタイムアウトしました。プリンタを再起動してください。',
]

FAKE_FILENAMES = [
    'report_2024.txt', 'main.py', 'invoice_final.docx', 'data_export.csv',
    'presentation.pptx', 'draft_v2.md', 'summary.xlsx', 'image_scan_03.jpg',
    'notes.txt', 'manual_draft.pdf', 'backup_2023.zip', 'archive.tar.gz'
]

# OS通知を送る（Linux: notify-send, Mac: osascript, Windows: print to terminal）
def send_notification(message):
    if sys.platform.startswith('linux'):
        try:
            subprocess.run(['notify-send', message], check=True)
        except Exception:
            print(f'[OS通知] {message}')
    elif sys.platform == 'darwin':
        script = f'display notification "{message}" with title "プリンタ警告"'
        try:
            subprocess.run(['osascript', '-e', script], check=True)
        except Exception:
            print(f'[OS通知] {message}')
    elif sys.platform == 'win32':
        # Windows 10+ の場合は PowerShell通知も可能だが、ここではprintのみ
        print(f'[OS通知] {message}')
    else:
        print(f'[OS通知] {message}')

# ランダムなファイル名を選ぶ
def random_filename():
    if random.random() < 0.7:
        return random.choice(FAKE_FILENAMES)
    else:
        # ランダムなファイル名を生成
        name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 12)))
        ext = random.choice(['.txt', '.docx', '.csv', '.py', '.pdf', '.md', '.jpg'])
        return name + ext

# メッセージをランダム生成
def generate_message():
    template = random.choice(TEMPLATES)
    if '{filename}' in template:
        filename = random_filename()
        return template.format(filename=filename)
    else:
        return template

# 通知をランダムなタイミングで発生させる
def run_random_alerts(count=None, min_interval=30, max_interval=300):
    i = 0
    while True:
        message = generate_message()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if random.random() < 0.5:
            # ターミナルにも出す
            print(f'[Terminal] {now} {message}')
        send_notification(message)
        i += 1
        if count is not None and i >= count:
            break
        interval = random.randint(min_interval, max_interval)
        time.sleep(interval)

# 明示呼び出し用
def trigger_once():
    message = generate_message()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[Terminal] {now} {message}')
    send_notification(message)

# CLIサブコマンド: run/once/list_templates

def list_templates():
    print('利用可能なメッセージテンプレート:')
    for i, t in enumerate(TEMPLATES):
        print(f'{i+1}: {t}')

def main():
    parser = argparse.ArgumentParser(description='random-os-fake-printer-jam-alert Skill')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='ランダムな間隔でプリンタ警告を発生させる')
    parser_run.add_argument('--count', type=int, default=None, help='通知回数 (指定しないと無限)')
    parser_run.add_argument('--min-interval', type=int, default=30, help='最小間隔(秒)')
    parser_run.add_argument('--max-interval', type=int, default=300, help='最大間隔(秒)')

    parser_once = subparsers.add_parser('once', help='1回だけ即時プリンタ警告を発生')
    parser_list = subparsers.add_parser('list_templates', help='テンプレート一覧表示')

    args = parser.parse_args()

    if args.command == 'run':
        try:
            run_random_alerts(count=args.count, min_interval=args.min_interval, max_interval=args.max_interval)
        except KeyboardInterrupt:
            print('\n[終了] プリンタ警告スキルを停止しました。')
    elif args.command == 'once':
        trigger_once()
    elif args.command == 'list_templates':
        list_templates()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
