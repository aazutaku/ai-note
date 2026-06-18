import sys
import subprocess
import random
import argparse
import platform
import os
import traceback

def get_random_katakana_error():
    subjects = [
        'パケット・シンフォニー', 'デジタル・アンビエント', 'フレーム・カーネル', 'バイナリ・アーキタイプ',
        'メモリ・コンポーザー', 'プロトコル・エクリプス', 'ストリーム・オルガノン', 'バッファ・クロニクル',
        'シグナル・レゾナンス', 'クラスタ・アトモスフィア', 'プロセス・エクリプス', 'コア・パラダイム',
        'データ・レゾリューション', 'オペランド・カタリスト', 'スレッド・シンフォニー', 'パラメータ・オーバードライブ'
    ]
    actions = [
        'がバッファ・カタストロフを検出しました', 'がオーバーフローしました', 'がシグナル・ディストーションを感知しました',
        'がプロトコル・パニックを発生させました', 'がメモリ・フラグメンテーションを起こしました',
        'がストリーム・エクリプスに突入しました', 'がフレーム・アウトオブレンジです',
        'がデータ・パラドックスを引き起こしました', 'がプロセス・タイムシフトを検知しました',
        'がクラスタ・デグレードを報告しました', 'がコア・アンビエントを検出しました',
        'がオペランド・ミスマッチを発生させました', 'がスレッド・インバージョンに失敗しました',
        'がパラメータ・サチュレーションを超過しました'
    ]
    return f'{random.choice(subjects)}{random.choice(actions)}'

def notify(message):
    system = platform.system()
    if system == 'Linux':
        try:
            subprocess.run(['notify-send', message], check=True)
        except Exception:
            print(f'[通知失敗] {message}')
    elif system == 'Darwin':
        script = f'display notification "{message}" with title "random-os-error-kaiseki"'
        try:
            subprocess.run(['osascript', '-e', script], check=True)
        except Exception:
            print(f'[通知失敗] {message}')
    elif system == 'Windows':
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("random-os-error-kaiseki", message, duration=5)
        except ImportError:
            print('[通知失敗] win10toastパッケージが必要です')
            print(message)
    else:
        print(f'[通知未対応] {message}')

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(result.stdout, end='')
            print(result.stderr, end='')
            katakana_error = get_random_katakana_error()
            notify(katakana_error)
            print(f'[通知] {katakana_error}')
        else:
            print(result.stdout, end='')
    except Exception as e:
        print(traceback.format_exc())
        katakana_error = get_random_katakana_error()
        notify(katakana_error)
        print(f'[通知] {katakana_error}')

def show_last_error():
    # 直近のエラー内容を取得（ここではダミー）
    katakana_error = get_random_katakana_error()
    notify(katakana_error)
    print(f'[通知] {katakana_error}')

def main():
    parser = argparse.ArgumentParser(description='random-os-error-kaiseki: OS風カタカナエラー通知')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='コマンドを実行し、失敗時にカタカナエラー通知')
    parser_run.add_argument('cmd', nargs=argparse.REMAINDER, help='実行コマンド')

    parser_last = subparsers.add_parser('last', help='直近のエラーをカタカナ解説で通知')

    args = parser.parse_args()

    if args.command == 'run':
        if not args.cmd:
            print('コマンドを指定してください')
            sys.exit(1)
        run_command(' '.join(args.cmd))
    elif args.command == 'last':
        show_last_error()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
