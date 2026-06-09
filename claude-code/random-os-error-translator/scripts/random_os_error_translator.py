import argparse
import random
import sys
import os
import datetime
from typing import List, Dict

# OS風エラー演出パターン
OS_ERROR_PATTERNS = [
    {
        'name': 'MS-DOS',
        'patterns': [
            ('Permission denied', 'このファイルは神聖にして侵入を禁ず。'),
            ('File not found', '指定されたファイルは存在しません。'),
            ('Is a directory', 'これはディレクトリです。ファイル操作は無効です。'),
            ('Operation not permitted', '推奨されていない操作です。'),
            ('No such file or directory', 'ファイルまたはディレクトリが見つかりません。'),
        ]
    },
    {
        'name': 'AmigaOS',
        'patterns': [
            ('Permission denied', 'ファイルへのアクセスは銀河評議会の承認が必要です。'),
            ('File not found', 'ファイルは時空の狭間に消えました。'),
            ('Is a directory', 'ディレクトリは生命体です。敬意を払いましょう。'),
            ('Operation not permitted', 'この操作は宇宙法により禁止されています。'),
            ('No such file or directory', '探索したが見つかりませんでした。'),
        ]
    },
    {
        'name': '謎の国産OS',
        'patterns': [
            ('Permission denied', '推奨されていない操作です。'),
            ('File not found', '指定されたファイルは宇宙の彼方に消えました。'),
            ('Is a directory', 'ディレクトリ操作は管理者のみ許可されています。'),
            ('Operation not permitted', 'この操作は現在サポートされていません。'),
            ('No such file or directory', 'ファイルが見つかりませんでした。'),
        ]
    },
    {
        'name': 'Unix System V',
        'patterns': [
            ('Permission denied', 'アクセス権限がありません。'),
            ('File not found', 'ファイルが存在しません。'),
            ('Is a directory', 'ディレクトリに対して無効な操作です。'),
            ('Operation not permitted', '操作が許可されていません。'),
            ('No such file or directory', '指定されたパスが無効です。'),
        ]
    },
    {
        'name': 'Macintosh System 7',
        'patterns': [
            ('Permission denied', 'このファイルはFinderによってロックされています。'),
            ('File not found', 'アイコンがデスクトップから消えました。'),
            ('Is a directory', 'フォルダには直接アクセスできません。'),
            ('Operation not permitted', 'この操作はサポートされていません。'),
            ('No such file or directory', '指定されたアイテムが見つかりません。'),
        ]
    },
]

LOG_FILE = os.path.expanduser('~/.random_os_error_translator.log')


def parse_args():
    parser = argparse.ArgumentParser(description='ランダムOS風エラートランスレータ')
    subparsers = parser.add_subparsers(dest='command')

    # 明示呼び出し
    run_parser = subparsers.add_parser('run', help='エラーメッセージを変換')
    run_parser.add_argument('error_message', type=str, help='変換対象のエラーメッセージ')

    # ログ閲覧
    log_parser = subparsers.add_parser('log', help='変換履歴を表示')
    log_parser.add_argument('--tail', type=int, default=10, help='直近N件のみ表示')

    # サマリー
    summary_parser = subparsers.add_parser('summary', help='変換パターンのサマリー')

    return parser.parse_args()


def select_os_pattern(error_message: str) -> Dict:
    """
    エラーメッセージに最もマッチするOS風パターンをランダムに選択
    """
    candidates = []
    for os_pattern in OS_ERROR_PATTERNS:
        for key, val in os_pattern['patterns']:
            if key.lower() in error_message.lower():
                candidates.append((os_pattern['name'], val))
    if not candidates:
        # 完全一致しない場合はランダムなOS名でジェネリックな演出
        os_pattern = random.choice(OS_ERROR_PATTERNS)
        return {
            'os': os_pattern['name'],
            'message': '未知のエラーが発生しました。詳細は管理者にお問い合わせください。'
        }
    os_name, os_msg = random.choice(candidates)
    return {
        'os': os_name,
        'message': os_msg
    }


def format_output(os_name: str, os_msg: str, orig_error: str) -> str:
    return f"[OS風エラー演出: {os_name}]\n> {os_msg}\n[元のエラー]: {orig_error}\n"


def log_translation(os_name: str, os_msg: str, orig_error: str):
    now = datetime.datetime.now().isoformat()
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{now}\t{os_name}\t{os_msg}\t{orig_error}\n")


def show_log(tail: int = 10):
    if not os.path.exists(LOG_FILE):
        print('変換履歴はまだありません。')
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines[-tail:]:
        dt, os_name, os_msg, orig_error = line.strip().split('\t')
        print(f"[{dt}] {os_name}: {os_msg} (元エラー: {orig_error})")


def show_summary():
    print('--- OS風エラー演出パターン一覧 ---')
    for os_pattern in OS_ERROR_PATTERNS:
        print(f"- {os_pattern['name']}")
        for key, val in os_pattern['patterns']:
            print(f"    '{key}' → '{val}'")
    print('\n演出パターンは随時追加可能です。')


def main():
    args = parse_args()
    if args.command == 'run':
        result = select_os_pattern(args.error_message)
        output = format_output(result['os'], result['message'], args.error_message)
        print(output)
        log_translation(result['os'], result['message'], args.error_message)
    elif args.command == 'log':
        show_log(args.tail)
    elif args.command == 'summary':
        show_summary()
    else:
        print('使い方:')
        print('  python random_os_error_translator.py run "Permission denied: test.txt"')
        print('  python random_os_error_translator.py log --tail 5')
        print('  python random_os_error_translator.py summary')

if __name__ == '__main__':
    main()
