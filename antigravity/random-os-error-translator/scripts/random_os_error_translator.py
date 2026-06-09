import sys
import argparse
import traceback
import random
from typing import List, Tuple

# OS風エラーパターン定義
OS_ERROR_PATTERNS = [
    {
        'os': 'MS-DOS風',
        'patterns': [
            ('Permission denied', 'このファイルは神聖にして侵入を禁ず。'),
            ('No such file or directory', '指定されたパスは存在しません。'),
            ('File exists', '既に存在しています。'),
            ('Is a directory', 'ディレクトリ指定が不正です。'),
            ('Not a directory', 'ディレクトリではありません。'),
            ('Connection refused', '通信路が閉ざされています。'),
            ('Operation not permitted', '許可されていない操作です。'),
            ('Invalid argument', '引数が無効です。'),
            ('Broken pipe', 'パイプが破損しました。'),
        ]
    },
    {
        'os': '謎の国産OS風',
        'patterns': [
            ('Permission denied', '推奨されていない操作です。'),
            ('No such file or directory', 'そのようなファイルはありません。'),
            ('File exists', '同名ファイルが既に登録済みです。'),
            ('Is a directory', 'フォルダ指定に誤りがあります。'),
            ('Not a directory', 'フォルダではありません。'),
            ('Connection refused', '接続は拒否されました。'),
            ('Operation not permitted', '操作が許可されていません。'),
            ('Invalid argument', '不正なパラメータです。'),
            ('Broken pipe', '通信経路が断絶しました。'),
        ]
    },
    {
        'os': 'Linux風',
        'patterns': [
            ('Permission denied', 'ルート様のご許可が必要です。'),
            ('No such file or directory', 'ファイルが見つかりません。'),
            ('File exists', 'ファイルは既に存在しています。'),
            ('Is a directory', 'ディレクトリ指定の不一致です。'),
            ('Not a directory', 'ディレクトリではありません。'),
            ('Connection refused', '接続が拒否されました。'),
            ('Operation not permitted', '許可されていない操作です。'),
            ('Invalid argument', '無効な引数です。'),
            ('Broken pipe', 'パイプが壊れました。'),
        ]
    },
    {
        'os': '古代UNIX風',
        'patterns': [
            ('Permission denied', '権限がありません。'),
            ('No such file or directory', 'そんなファイルはない。'),
            ('File exists', 'ファイルは既にある。'),
            ('Is a directory', 'ディレクトリが指定された。'),
            ('Not a directory', 'ディレクトリではない。'),
            ('Connection refused', '接続不可。'),
            ('Operation not permitted', '許可されていない。'),
            ('Invalid argument', '引数が不正。'),
            ('Broken pipe', 'パイプ破損。'),
        ]
    },
    {
        'os': '架空OS風',
        'patterns': [
            ('Permission denied', 'この領域は管理者しか入れません。'),
            ('No such file or directory', '幻のファイルです。'),
            ('File exists', '時空の彼方に既に存在します。'),
            ('Is a directory', 'ディレクトリの迷宮に迷い込んだ。'),
            ('Not a directory', 'ここはディレクトリではありません。'),
            ('Connection refused', '門が閉ざされています。'),
            ('Operation not permitted', '禁断の操作です。'),
            ('Invalid argument', '謎の引数です。'),
            ('Broken pipe', 'パイプが異次元に消えました。'),
        ]
    },
]

GENERIC_MESSAGES = [
    '未知のエラーが発生しました。',
    '何かがうまくいきませんでした。',
    '原因不明の障害です。',
    'システムが混乱しています。',
    '詳細は不明です。',
]

def translate_error_message(original: str) -> Tuple[str, str]:
    os_pattern = random.choice(OS_ERROR_PATTERNS)
    for pat, msg in os_pattern['patterns']:
        if pat in original:
            return f"[{os_pattern['os']}] {msg}", os_pattern['os']
    # 該当しない場合は汎用メッセージ
    return f"[{os_pattern['os']}] {random.choice(GENERIC_MESSAGES)}", os_pattern['os']

def print_translated_error(errmsg: str):
    translated, osname = translate_error_message(errmsg)
    print(translated)
    print(f"(元のエラー: {errmsg})")

def simulate_error(args):
    # テスト用に例外を発生させる
    try:
        if args.type == 'permission':
            open('/root/flag', 'r')
        elif args.type == 'notfound':
            open('/notfound/file.txt', 'r')
        elif args.type == 'exists':
            import tempfile
            with tempfile.NamedTemporaryFile(delete=False) as tf:
                fname = tf.name
            open(fname, 'x')
            open(fname, 'x')
        elif args.type == 'custom':
            raise RuntimeError('Custom error for testing')
        else:
            raise Exception('Unknown error type')
    except Exception as e:
        errmsg = str(e)
        print_translated_error(errmsg)
        if args.verbose:
            traceback.print_exc()

def wrap_command(args):
    import subprocess
    try:
        proc = subprocess.run(args.command, shell=True, capture_output=True, text=True)
        if proc.returncode != 0:
            errmsg = proc.stderr.strip() or proc.stdout.strip() or f"Command failed with code {proc.returncode}"
            print_translated_error(errmsg)
        else:
            print(proc.stdout)
    except Exception as e:
        errmsg = str(e)
        print_translated_error(errmsg)

def main():
    parser = argparse.ArgumentParser(description='Random OS Error Translator')
    subparsers = parser.add_subparsers(dest='subcmd')

    sim_parser = subparsers.add_parser('simulate', help='テスト用エラーを発生させる')
    sim_parser.add_argument('--type', choices=['permission', 'notfound', 'exists', 'custom'], default='permission', help='エラー種別')
    sim_parser.add_argument('--verbose', action='store_true', help='詳細なトレースバックを表示')

    wrap_parser = subparsers.add_parser('wrap', help='コマンド実行のエラーをOS風に変換')
    wrap_parser.add_argument('command', help='実行するコマンド')

    args = parser.parse_args()
    if args.subcmd == 'simulate':
        simulate_error(args)
    elif args.subcmd == 'wrap':
        wrap_command(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
