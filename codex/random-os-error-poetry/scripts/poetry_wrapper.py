import subprocess
import sys
import argparse
import re
from typing import Optional, Tuple

# --- 詩テンプレート定義 ---
ERROR_POETRY_MAP = [
    (re.compile(r'Permission denied', re.I),
     "許されぬ権限よ、我が手にパーミッションを"),
    (re.compile(r'No such file or directory', re.I),
     "見つからぬ道、404の黄昏"),
    (re.compile(r'FileNotFoundError', re.I),
     "消えたファイル、虚空に溶けて"),
    (re.compile(r'IsADirectoryError', re.I),
     "運命に抗う者よ、根を断つこと叶わず"),
    (re.compile(r'OSError', re.I),
     "OSの深淵、響くエラーの調べ"),
    (re.compile(r'404', re.I),
     "404の彼方、失われしページの詩"),
    (re.compile(r'Access is denied', re.I),
     "拒まれし扉、アクセスの夢遠く"),
    (re.compile(r'not found', re.I),
     "探し人、見つからぬまま夜は更ける"),
]

# --- 詩変換関数 ---
def poeticize_error(stderr: str) -> Optional[str]:
    for pattern, poem in ERROR_POETRY_MAP:
        if pattern.search(stderr):
            return f"{poem}\n  ({stderr.strip()})"
    return None

# --- コマンド実行ラッパ ---
def run_command(cmd_args: list) -> Tuple[int, str, str]:
    try:
        proc = subprocess.Popen(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out, err = proc.communicate()
        return proc.returncode, out, err
    except Exception as e:
        return 1, '', str(e)

# --- CLIサブコマンド: run ---
def cli_run(args):
    code, out, err = run_command(args.command)
    sys.stdout.write(out)
    if err:
        poem = poeticize_error(err)
        if poem:
            sys.stderr.write(poem + '\n')
        else:
            sys.stderr.write(err)
    sys.exit(code)

# --- CLIサブコマンド: test (サンプルエラーを詩化) ---
def cli_test(args):
    test_errs = [
        "Permission denied: '/root'",
        "No such file or directory: 'missing.txt'",
        "FileNotFoundError: [Errno 2]",
        "IsADirectoryError: [Errno 21] Is a directory: '/'",
        "OSError: [Errno 5] Input/output error",
        "404 Not Found",
        "Access is denied",
        "command not found: foobar"
    ]
    for err in test_errs:
        poem = poeticize_error(err)
        print(f"元エラー: {err}")
        print(f"詩変換: {poem if poem else err}\n")

# --- CLIサブコマンド: list (詩テンプレート一覧) ---
def cli_list(args):
    print("対応エラーパターンと詩テンプレート:")
    for pattern, poem in ERROR_POETRY_MAP:
        print(f"- {pattern.pattern} => {poem}")

# --- CLIサブコマンド: summary ---
def cli_summary(args):
    print("random-os-error-poetry: OSエラーや例外を詩的に変換して表示します。\n")
    print("使い方例:")
    print("  python poetry_wrapper.py run ls /root")
    print("  python poetry_wrapper.py run cat missing.txt")
    print("  python poetry_wrapper.py test")
    print("  python poetry_wrapper.py list")

# --- メイン ---
def main():
    parser = argparse.ArgumentParser(description='random-os-error-poetry: OSエラーを即興詩に変換するラッパ')
    subparsers = parser.add_subparsers(dest='subcmd', required=True)

    p_run = subparsers.add_parser('run', help='コマンドをラップして詩的エラー表示')
    p_run.add_argument('command', nargs=argparse.REMAINDER, help='実行するコマンド')
    p_run.set_defaults(func=cli_run)

    p_test = subparsers.add_parser('test', help='サンプルエラーを詩化して表示')
    p_test.set_defaults(func=cli_test)

    p_list = subparsers.add_parser('list', help='詩テンプレート一覧')
    p_list.set_defaults(func=cli_list)

    p_summary = subparsers.add_parser('summary', help='Skill概要')
    p_summary.set_defaults(func=cli_summary)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
