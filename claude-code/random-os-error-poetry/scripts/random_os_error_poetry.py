import sys
import argparse
import traceback
import random
import os
from typing import Optional, Tuple, List

POETIC_TEMPLATES = [
    (
        'PermissionError',
        [
            '許されぬ権限よ、我が手にパーミッションを。',
            '閉ざされた門の向こうに、{path}の夢。',
            '鉄の扉は静かに拒む、我が願いを。',
            'この道は選ばれし者のみが歩む。',
        ]
    ),
    (
        'FileNotFoundError',
        [
            '見つからぬ道、404の黄昏。',
            '失われしファイル、{path}は幻。',
            '探し求めし{path}、風の中に消ゆ。',
            '存在しないページに、我は問いかける。',
        ]
    ),
    (
        'IsADirectoryError',
        [
            '{path}はディレクトリなり、ファイルの仮面を脱ぎ捨てて。',
            '道を誤りし者よ、ディレクトリの深淵へ。',
            'ファイルと思いし{path}、実は広き箱庭。',
        ]
    ),
    (
        'NotADirectoryError',
        [
            '{path}は道にあらず、行き止まりの石壁。',
            'ディレクトリたらんとした{path}、しかし叶わず。',
        ]
    ),
    (
        'OSError',
        [
            'OSの叫び、見えざる力が我を阻む。',
            '予期せぬ障壁、システムの深奥より。',
            '機械仕掛けの運命に翻弄される我が手。',
        ]
    ),
]

def parse_error_message(msg: str) -> Tuple[str, Optional[str]]:
    """
    エラーメッセージから例外名とパス（あれば）を抽出する。
    """
    for exc, _ in POETIC_TEMPLATES:
        if exc in msg:
            # パス抽出（簡易）
            parts = msg.split(":")
            path = None
            for part in parts:
                if "'" in part:
                    path = part.split("'")[1]
                    break
            return exc, path
    # OSError系以外
    return 'OSError', None

def poeticize_error(msg: str) -> str:
    exc, path = parse_error_message(msg)
    for template_exc, templates in POETIC_TEMPLATES:
        if exc == template_exc:
            lines = []
            for tmpl in random.sample(templates, min(2, len(templates))):
                if '{path}' in tmpl and path:
                    lines.append(tmpl.format(path=path))
                else:
                    lines.append(tmpl)
            poetic = "\n".join(lines)
            return f"{poetic}\n[原文: {msg}]"
    # fallback
    return f"OSの詩情: {msg}"

def run_cli():
    parser = argparse.ArgumentParser(
        description='OSエラーを詩的に変換して表示します。')
    parser.add_argument('error', nargs='?', help='エラーメッセージ文字列（省略時は標準入力）')
    parser.add_argument('--log', action='store_true', help='詩化したメッセージをエラー履歴として保存')
    parser.add_argument('--list', action='store_true', help='詩化エラーログを一覧表示')
    parser.add_argument('--summary', action='store_true', help='詩化エラーの種類統計を表示')
    args = parser.parse_args()

    log_path = os.path.expanduser('~/.random_os_error_poetry.log')

    if args.list:
        if os.path.exists(log_path):
            with open(log_path, 'r', encoding='utf-8') as f:
                print(f.read())
        else:
            print('まだエラーログはありません。')
        return
    if args.summary:
        if os.path.exists(log_path):
            counts = {}
            with open(log_path, 'r', encoding='utf-8') as f:
                for line in f:
                    for exc, _ in POETIC_TEMPLATES:
                        if exc in line:
                            counts[exc] = counts.get(exc, 0) + 1
            if counts:
                print('エラー詩の種類統計:')
                for k, v in counts.items():
                    print(f'  {k}: {v}件')
            else:
                print('統計情報がありません。')
        else:
            print('まだエラーログはありません。')
        return

    if args.error:
        msg = args.error
    else:
        msg = sys.stdin.read().strip()
    poetic = poeticize_error(msg)
    print(poetic)
    if args.log:
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(poetic.replace('\n', ' ') + '\n')

def main():
    try:
        run_cli()
    except Exception as e:
        tb = traceback.format_exc()
        print(poeticize_error(f"OSError: {e}\n{tb}"))

if __name__ == '__main__':
    main()
