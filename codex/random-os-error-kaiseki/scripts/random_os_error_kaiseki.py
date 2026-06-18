import sys
import subprocess
import argparse
import random
import os
import platform
import traceback
from typing import List

KATAKANA_TERMS_1 = [
    "パケット・シンフォニー",
    "デジタル・アンビエント",
    "メモリ・エクリプス",
    "カーネル・リゾナンス",
    "プロトコル・フラクタル",
    "バッファ・カタストロフ",
    "システム・パラダイム",
    "データ・スペクトラム",
    "ストリーム・コンダクター",
    "ロジック・オペランド",
    "アーキテクチャ・クロニクル",
    "ノード・オーケストラ",
    "プロセス・インシデント",
    "セグメント・エクリプス",
    "スレッド・コンフリクト"
]
KATAKANA_TERMS_2 = [
    "バッファ・カタストロフを検出しました",
    "オーバーフローしました",
    "カーネル・リゾナンスが不正です",
    "プロトコル・フラクタルを阻害しました",
    "パラダイム・シフトが発生しました",
    "メモリ・リークを観測しました",
    "データ・コリジョンが発生しました",
    "ノード・フェーズが崩壊しました",
    "ストリーム・インシデントを検出しました",
    "ロジック・パルスが消失しました",
    "アーキテクチャ・エラーが発生しました",
    "オペランド・アノマリーを記録しました",
    "プロセス・カスケードが停止しました",
    "セグメント・デグレードを検出しました",
    "スレッド・パニックが発生しました"
]


def generate_katakana_error() -> str:
    part1 = random.choice(KATAKANA_TERMS_1)
    part2 = random.choice(KATAKANA_TERMS_2)
    return f"{part1}{part2 if part2.startswith('が') or part2.startswith('を') else 'が' + part2}"


def notify_desktop(message: str):
    system = platform.system()
    if system == "Darwin":  # macOS
        script = f'display notification "{message}" with title "random-os-error-kaiseki"'
        subprocess.run(["osascript", "-e", script], check=False)
    elif system == "Linux":
        subprocess.run(["notify-send", "random-os-error-kaiseki", message], check=False)
    elif system == "Windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("random-os-error-kaiseki", message, duration=5)
        except ImportError:
            print("[通知失敗] win10toastが必要です: pip install win10toast", file=sys.stderr)
    else:
        print(f"[通知未対応OS] {system}", file=sys.stderr)


def run_and_kaiseki(cmd: List[str]):
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(proc.stdout, end='')
        print(proc.stderr, end='')
    except subprocess.CalledProcessError as e:
        print(e.stdout, end='')
        print(e.stderr, end='')
        print(f"[error] コマンド実行に失敗しました: {e}", file=sys.stderr)
        # エラー時に謎カタカナ通知
        for _ in range(random.randint(1, 2)):
            msg = generate_katakana_error()
            notify_desktop(msg)
    except Exception as ex:
        print(traceback.format_exc(), file=sys.stderr)
        msg = generate_katakana_error()
        notify_desktop(msg)


def list_examples():
    print("--- random-os-error-kaiseki 出力例 ---")
    for _ in range(5):
        print(f"[通知] {generate_katakana_error()}")


def main():
    parser = argparse.ArgumentParser(description="コマンド実行時のエラーをカタカナ謎解説で通知するSkill")
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="コマンドを実行し、エラー時に謎カタカナ通知")
    parser_run.add_argument("cmd", nargs=argparse.REMAINDER, help="実行するコマンド")

    parser_list = subparsers.add_parser("list", help="ランダムなカタカナエラー例を表示")

    args = parser.parse_args()

    if args.command == "run":
        if not args.cmd:
            print("コマンドを指定してください", file=sys.stderr)
            sys.exit(1)
        run_and_kaiseki(args.cmd)
    elif args.command == "list":
        list_examples()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
