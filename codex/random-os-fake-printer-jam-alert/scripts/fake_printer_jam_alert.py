import os
import sys
import random
import time
import argparse
import subprocess
from datetime import datetime, timedelta

# 通知メッセージのテンプレート
MESSAGE_TEMPLATES = [
    '重要：プリンタで“{filename}”が紙詰まりを検出しました。',
    '警告：印刷ジョブが渋滞中です。トナー補充を試してください。',
    'エラー：プリンタが“{filename}”を処理中に謎のジャムが発生。',
    '指示：紙を手で給紙してください。',
    '注意：プリンタに未知のエラーコード #{error_code}。',
    '警告：印刷待ちジョブが多すぎます。',
    'エラー：プリンタが“{filename}”を印刷中にヒーター異常。',
    '重要：プリンタの用紙トレイが空です。',
    '指示：謎のトナーを補充してください。',
    '注意：プリンタが“{filename}”を認識できません。',
    'エラー：プリンタの出力トレイが詰まっています。',
    '警告：プリンタが休憩中です。しばらくお待ちください。',
    '重要：プリンタが“{filename}”で紙詰まり（第3給紙カセット）。',
    '注意：プリンタのネットワークが不安定です。',
    'エラー：印刷ジョブがタイムアウトしました。',
    '指示：プリンタのカバーを一度閉じてください。',
    '警告：プリンタが“{filename}”で不明な問題を検出。',
    '重要：プリンタのメモリが不足しています。',
    '注意：プリンタのIPアドレスが迷子です。',
    'エラー：プリンタが“{filename}”の印刷を拒否しました。',
]

# サンプルファイル名リスト
SAMPLE_FILENAMES = [
    'main.py', 'README.md', 'report.docx', 'data.csv', 'script.sh', 'notes.txt',
    'diagram.png', 'invoice.pdf', 'presentation.pptx', 'summary.xlsx', 'draft.tex',
    'archive.zip', 'config.yaml', 'logfile.log', 'thesis.doc', 'manual.pdf',
]

# エラーコード生成
ERROR_CODES = ['E42', 'JAM99', 'PAPER404', 'TNR-7', 'ERR-PRT', 'E-PRNTR', 'XJAM', 'CODE13']

# OS通知コマンド
NOTIFY_COMMANDS = [
    ['notify-send', '{title}', '{message}'],  # Linux
    ['osascript', '-e', 'display notification "{message}" with title "{title}"'],  # macOS
]

HISTORY = []


def random_filename():
    return random.choice(SAMPLE_FILENAMES)

def random_error_code():
    return random.choice(ERROR_CODES)

def random_message():
    template = random.choice(MESSAGE_TEMPLATES)
    msg = template.format(
        filename=random_filename(),
        error_code=random_error_code()
    )
    return msg

def send_notification(message, title='OS通知'):
    sent = False
    for cmd_tpl in NOTIFY_COMMANDS:
        try:
            cmd = [part.format(title=title, message=message) for part in cmd_tpl]
            # macOSのosascriptは全体を-eで渡す
            if cmd[0] == 'osascript':
                subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                subprocess.run(cmd, check=True)
            sent = True
            break
        except Exception:
            continue
    if not sent:
        print(f'[OS通知] {message}')


def log_event(message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    HISTORY.append({'timestamp': now, 'message': message})

def list_history():
    if not HISTORY:
        print('通知履歴はありません。')
        return
    for event in HISTORY:
        print(f"[{event['timestamp']}] {event['message']}")

def summary():
    print(f'通知履歴件数: {len(HISTORY)}')
    if HISTORY:
        print(f'最新: {HISTORY[-1]["timestamp"]} - {HISTORY[-1]["message"]}')


def random_interval(min_sec=30, max_sec=180):
    return random.randint(min_sec, max_sec)

def run_alert_loop(duration=None, max_count=None):
    """
    duration: ループを続ける秒数
    max_count: 最大通知回数
    """
    start = datetime.now()
    count = 0
    while True:
        if duration and (datetime.now() - start).total_seconds() > duration:
            break
        if max_count and count >= max_count:
            break
        interval = random_interval()
        time.sleep(interval)
        msg = random_message()
        send_notification(msg)
        log_event(msg)
        count += 1


def explicit_trigger():
    msg = random_message()
    send_notification(msg)
    log_event(msg)


def parse_args():
    parser = argparse.ArgumentParser(description='Fake Printer Jam Alert Skill')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='ランダムなタイミングでプリンタ紙詰まり通知を発生させる')
    parser_run.add_argument('--duration', type=int, default=None, help='動作秒数（省略時は無限）')
    parser_run.add_argument('--max-count', type=int, default=None, help='最大通知回数')

    parser_explicit = subparsers.add_parser('alert', help='即座に1件通知を発生させる')

    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知履歴の要約')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'run':
        print('プリンタ紙詰まり通知ループを開始します...')
        try:
            run_alert_loop(duration=args.duration, max_count=args.max_count)
        except KeyboardInterrupt:
            print('\n中断されました。')
    elif args.command == 'alert':
        explicit_trigger()
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    else:
        print('コマンドを指定してください (run/alert/list/summary)')

if __name__ == '__main__':
    main()
