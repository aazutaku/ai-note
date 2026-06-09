import argparse
import random
import sys
import traceback
from typing import List, Tuple, Dict

OS_STYLES = [
    {
        'name': 'MS-DOS風',
        'templates': [
            'システムが混乱しました。操作は許可されません。',
            '致命的エラー: コマンドまたはファイル名が違います。',
            'このファイルは神聖にして侵入を禁ず。',
            'コマンドまたはファイル名が正しくありません。',
        ]
    },
    {
        'name': 'AmigaOS風',
        'templates': [
            '申し訳ありません、この命令は神の領域です。',
            'Guru Meditation: システムが拒否しました。',
            'あなたの要求は受理されませんでした。',
            'ファイルアクセスが拒否されました。',
        ]
    },
    {
        'name': '国産OS風',
        'templates': [
            'ファイルが見つかりませんでした。再起動を推奨します。',
            '推奨されていない操作です。',
            '操作に失敗しました。管理者にご連絡ください。',
            '不明なエラーが発生しました。',
        ]
    },
    {
        'name': 'Unix風',
        'templates': [
            'Operation not permitted. Consult your sysadmin.',
            'Segmentation fault (core dumped).',
            'Permission denied: access is futile.',
            'No such file or directory. Try again later.',
        ]
    },
    {
        'name': 'Windows 95風',
        'templates': [
            '致命的な例外 OE が 0028:C0011E36 で発生しました。',
            'この操作はサポートされていません。',
            'アクセスが拒否されました。',
            'ファイルまたはパスが見つかりません。',
        ]
    },
    {
        'name': 'CP/M風',
        'templates': [
            'BDOS ERROR: File not found.',
            'BDOS ERROR: Disk full.',
            'BDOS ERROR: Read only file.',
            'BDOS ERROR: Unknown command.',
        ]
    }
]

EXCLUDE_ERRORS = [
    'Kernel panic',
    'Segmentation fault',
    'Out of memory',
    'System halt',
]

def random_os_style_message(original_error: str) -> Tuple[str, str]:
    """
    ランダムなOS風メッセージを生成し、元のエラーも返す。
    """
    os_style = random.choice(OS_STYLES)
    template = random.choice(os_style['templates'])
    return f"[{os_style['name']}] {template}", original_error

def should_exclude(error_message: str) -> bool:
    """
    致命的なエラーは除外
    """
    for excl in EXCLUDE_ERRORS:
        if excl.lower() in error_message.lower():
            return True
    return False

def translate_error(error_message: str) -> str:
    """
    エラーをOS風に変換し、元のエラーも併記
    """
    if should_exclude(error_message):
        return error_message
    os_msg, orig = random_os_style_message(error_message)
    return f"{os_msg}\n(元のエラー: {orig})"

def simulate_command(cmd: List[str]):
    """
    疑似的にコマンドを実行し、エラー時に変換表示
    """
    import subprocess
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout, end='')
    except subprocess.CalledProcessError as e:
        err = e.stderr.strip() or str(e)
        print(translate_error(err))
    except FileNotFoundError as e:
        print(translate_error(str(e)))
    except Exception as e:
        print(translate_error(str(e)))

def log_error(error_message: str, logfile: str = 'os_error_log.txt'):
    with open(logfile, 'a', encoding='utf-8') as f:
        f.write(f"{error_message}\n")

def list_logs(logfile: str = 'os_error_log.txt'):
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            for line in f:
                print(line.rstrip())
    except FileNotFoundError:
        print('ログファイルがありません。')

def summary_logs(logfile: str = 'os_error_log.txt'):
    from collections import Counter
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        counter = Counter(lines)
        for msg, count in counter.most_common():
            print(f'{msg} : {count}回')
    except FileNotFoundError:
        print('ログファイルがありません。')

def main():
    parser = argparse.ArgumentParser(description='random-os-error-translator: エラーをランダムOS風に変換')
    subparsers = parser.add_subparsers(dest='command')

    # translateサブコマンド
    p_translate = subparsers.add_parser('translate', help='エラーメッセージをOS風に変換')
    p_translate.add_argument('message', nargs='+', help='変換したいエラーメッセージ')
    p_translate.add_argument('--log', action='store_true', help='ログに記録する')

    # simulateサブコマンド
    p_simulate = subparsers.add_parser('simulate', help='コマンドを実行しエラー時に変換')
    p_simulate.add_argument('cmd', nargs=argparse.REMAINDER, help='実行するコマンド')

    # logサブコマンド
    p_log = subparsers.add_parser('log', help='エラーをログに追加')
    p_log.add_argument('message', nargs='+', help='記録するエラーメッセージ')

    # listサブコマンド
    p_list = subparsers.add_parser('list', help='ログを一覧表示')

    # summaryサブコマンド
    p_summary = subparsers.add_parser('summary', help='ログの要約')

    args = parser.parse_args()

    if args.command == 'translate':
        msg = ' '.join(args.message)
        result = translate_error(msg)
        print(result)
        if args.log:
            log_error(result)
    elif args.command == 'simulate':
        if not args.cmd:
            print('コマンドを指定してください。')
            sys.exit(1)
        simulate_command(args.cmd)
    elif args.command == 'log':
        msg = ' '.join(args.message)
        log_error(msg)
        print('ログに記録しました。')
    elif args.command == 'list':
        list_logs()
    elif args.command == 'summary':
        summary_logs()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
