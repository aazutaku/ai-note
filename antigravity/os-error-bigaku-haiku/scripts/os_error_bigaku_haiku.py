import sys
import subprocess
import argparse
import traceback
import os
from typing import Optional, Tuple

HAIKU_TEMPLATES = {
    'Permission denied': [
        'Permission denied',
        '心閉ざして',
        '春霞'
    ],
    'No such file or directory': [
        'ファイルなし',
        '探し求めて',
        '夕暮れ時'
    ],
    'File exists': [
        'ファイル在り',
        '重ねた想い',
        '夏の雲'
    ],
    'Is a directory': [
        'ディレクトリ',
        '開けてみれば',
        '空の箱'
    ],
    'Not a directory': [
        '道迷い',
        'ディレクトリじゃ',
        'なかったよ'
    ],
    'Segmentation fault': [
        'セグメンテーション',
        '記憶の彼方',
        '絶望感'
    ],
    'Connection refused': [
        '拒まれて',
        '扉は固く',
        '冬の朝'
    ],
    'Broken pipe': [
        '壊れた管',
        '流れ止まりて',
        '静寂なり'
    ],
    'Timeout': [
        '時は過ぎ',
        '待ちぼうけして',
        '秋の暮れ'
    ],
    'Read-only file system': [
        '読み取りのみ',
        '書き込めぬまま',
        '雪の夜'
    ],
    'default': [
        'エラーかな',
        '思い悩んで',
        '深呼吸'
    ]
}

def extract_error_type(stderr: str) -> Tuple[str, str]:
    """
    エラーメッセージから主要なエラータイプを抽出
    """
    for key in HAIKU_TEMPLATES.keys():
        if key in stderr:
            return key, stderr.strip()
    # Python例外の場合
    if 'PermissionError' in stderr:
        return 'Permission denied', stderr.strip()
    if 'FileNotFoundError' in stderr:
        return 'No such file or directory', stderr.strip()
    if 'IsADirectoryError' in stderr:
        return 'Is a directory', stderr.strip()
    if 'NotADirectoryError' in stderr:
        return 'Not a directory', stderr.strip()
    if 'BrokenPipeError' in stderr:
        return 'Broken pipe', stderr.strip()
    if 'TimeoutError' in stderr:
        return 'Timeout', stderr.strip()
    return 'default', stderr.strip()

def format_haiku(error_type: str) -> str:
    haiku = HAIKU_TEMPLATES.get(error_type, HAIKU_TEMPLATES['default'])
    return '  ' + '\n          '.join(haiku)

def run_command(cmd_args: list) -> int:
    try:
        completed = subprocess.run(cmd_args, capture_output=True, text=True, check=True)
        if completed.stdout:
            print(completed.stdout, end='')
        return 0
    except subprocess.CalledProcessError as e:
        stderr = e.stderr if e.stderr else str(e)
        error_type, raw_msg = extract_error_type(stderr)
        print(f"[元エラー] {raw_msg}")
        print(f"[俳句]{os.linesep}{format_haiku(error_type)}")
        return e.returncode if hasattr(e, 'returncode') else 1
    except Exception as ex:
        tb = traceback.format_exc()
        error_type, _ = extract_error_type(str(ex))
        print(f"[元エラー] {str(ex)}")
        print(f"[俳句]{os.linesep}{format_haiku(error_type)}")
        return 1

def list_haiku_templates():
    print("# 登録済みエラー俳句テンプレート一覧:")
    for key, haiku in HAIKU_TEMPLATES.items():
        print(f"\n{key}")
        print('  ' + '\n  '.join(haiku))

def summary():
    print("このスクリプトは、コマンド実行時のエラーを和風俳句に変換して表示します。主要なOSエラーに対応しています。")
    print("詳細は --help をご覧ください。")

def main():
    parser = argparse.ArgumentParser(
        description='コマンド実行時のOSエラーを和風俳句に変換して表示するツール')
    subparsers = parser.add_subparsers(dest='subcmd', required=False)

    parser_run = subparsers.add_parser('run', help='コマンドを実行し、エラーがあれば俳句化')
    parser_run.add_argument('cmd', nargs=argparse.REMAINDER, help='実行するコマンド')

    parser_list = subparsers.add_parser('list', help='エラー俳句テンプレート一覧を表示')
    parser_summary = subparsers.add_parser('summary', help='Skill概要を表示')

    # デフォルトは run
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()

    if args.subcmd == 'run':
        if not args.cmd:
            print('コマンドを指定してください。')
            sys.exit(1)
        sys.exit(run_command(args.cmd))
    elif args.subcmd == 'list':
        list_haiku_templates()
    elif args.subcmd == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
