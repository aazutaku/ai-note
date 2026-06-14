import sys
import traceback
import argparse
import random
from typing import Optional, Tuple, List

# 詩的変換テンプレート集
POETRY_TEMPLATES = {
    'Permission denied': [
        '許されぬ権限よ、我が手にパーミッションを。\n閉ざされた扉の向こうに、静かなるファイルは眠る。',
        '扉は固く閉ざされ、我が願いは届かず。\n権限なき者に道は開かれぬ。'
    ],
    'No such file or directory': [
        '見つからぬ道、404の黄昏。\nファイルの幻影は、虚空に消えゆく。',
        '探し求めしものは、既にこの世になし。\nディレクトリの彼方に、静寂だけが残る。'
    ],
    'File exists': [
        '既に在りしもの、二度とは生まれず。\n存在の重みが、上書きを拒む。',
        '重複の悲しみ、ファイルは既に息づく。\n新しき名を与えよ。'
    ],
    'Is a directory': [
        'それは道なり、ファイルにあらず。\nディレクトリの深淵を覗くなかれ。',
        'ファイルと思いしは、実は道標。\nディレクトリの森を彷徨う。'
    ],
    'Not a directory': [
        '道と思いきや、そこは壁。\nディレクトリの名を持たぬ者よ。',
        '進むべき道は閉ざされ、そこにディレクトリは無い。'
    ],
    'Connection refused': [
        '繋がらぬ想い、拒まれし通信。\nサーバの沈黙に、心は波打つ。',
        '門は閉ざされ、接続は叶わず。\nネットワークの彼方に声は届かない。'
    ],
    'Not implemented': [
        '未だ見ぬ機能、実装の夜明けを待つ。\n未来への扉は、今は閉じられている。'
    ],
    'Timeout': [
        '時の流れに追いつけず。\nタイムアウトの鐘が静かに鳴る。'
    ]
}

# エラーメッセージから詩を生成
def poeticize_error(error_msg: str) -> Optional[str]:
    for key, poems in POETRY_TEMPLATES.items():
        if key.lower() in error_msg.lower():
            return random.choice(poems)
    return None

# エラーハンドリングラッパー
class PoetryErrorHandler:
    def __init__(self):
        self.last_error = None

    def handle(self, exc_type, exc_value, exc_tb):
        tb_str = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
        error_msg = str(exc_value)
        poem = poeticize_error(error_msg)
        if poem:
            print('---')
            print(poem)
            print(f'（原文: {error_msg}）')
        else:
            print('---')
            print('エラーが発生しましたが、詩的変換できませんでした。')
            print(f'（原文: {error_msg}）')
        self.last_error = (exc_type, exc_value, tb_str)

# CLIサブコマンド: ファイルを開いて読み込む（エラー発生時に詩化）
def cmd_cat(args):
    try:
        with open(args.filename, 'r', encoding='utf-8') as f:
            print(f.read())
    except Exception as e:
        sys.excepthook(*sys.exc_info())

# CLIサブコマンド: ディレクトリをリストする
import os
def cmd_ls(args):
    try:
        files = os.listdir(args.path)
        for name in files:
            print(name)
    except Exception as e:
        sys.excepthook(*sys.exc_info())

# CLIサブコマンド: ファイルを新規作成（既存ならエラー）
def cmd_touch(args):
    try:
        with open(args.filename, 'x', encoding='utf-8') as f:
            f.write('')
        print(f'{args.filename} を作成しました')
    except Exception as e:
        sys.excepthook(*sys.exc_info())

# CLIサブコマンド: ダミーで接続失敗を再現
def cmd_connect(args):
    import socket
    try:
        s = socket.create_connection((args.host, args.port), timeout=2)
        s.close()
        print('接続成功')
    except Exception as e:
        sys.excepthook(*sys.exc_info())

# CLIサブコマンド: 任意のエラーメッセージを詩化
def cmd_poem(args):
    poem = poeticize_error(args.message)
    if poem:
        print('---')
        print(poem)
        print(f'（原文: {args.message}）')
    else:
        print('---')
        print('詩的変換できませんでした。')
        print(f'（原文: {args.message}）')

# メイン関数

def main():
    handler = PoetryErrorHandler()
    sys.excepthook = handler.handle
    parser = argparse.ArgumentParser(description='OSエラーを詩的に変換するCLIツール')
    subparsers = parser.add_subparsers(dest='command')

    parser_cat = subparsers.add_parser('cat', help='ファイル内容を表示')
    parser_cat.add_argument('filename')
    parser_cat.set_defaults(func=cmd_cat)

    parser_ls = subparsers.add_parser('ls', help='ディレクトリ一覧')
    parser_ls.add_argument('path')
    parser_ls.set_defaults(func=cmd_ls)

    parser_touch = subparsers.add_parser('touch', help='新規ファイル作成')
    parser_touch.add_argument('filename')
    parser_touch.set_defaults(func=cmd_touch)

    parser_connect = subparsers.add_parser('connect', help='ホストに接続')
    parser_connect.add_argument('host')
    parser_connect.add_argument('port', type=int)
    parser_connect.set_defaults(func=cmd_connect)

    parser_poem = subparsers.add_parser('poem', help='任意のエラーメッセージを詩化')
    parser_poem.add_argument('message')
    parser_poem.set_defaults(func=cmd_poem)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
