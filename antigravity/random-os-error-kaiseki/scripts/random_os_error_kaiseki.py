import sys
import os
import random
import traceback
import argparse
from subprocess import CalledProcessError, run, PIPE

try:
    from plyer import notification
except ImportError:
    notification = None

KATAKANA_TERMS = [
    "パケット・シンフォニー",
    "バッファ・カタストロフ",
    "デジタル・アンビエント",
    "プロトコル・フェーズ",
    "メモリ・オーバードライブ",
    "システム・アトモスフィア",
    "ビット・レゾナンス",
    "フレーム・パラダイム",
    "セグメント・ファンタジア",
    "ストリーム・エクリプス",
    "ノード・スペクトル",
    "プロセス・シンクロニシティ",
    "キャッシュ・オルタナティブ",
    "スレッド・アブストラクション",
    "データ・コンフリクト",
    "バイナリ・カタルシス",
    "インターフェース・ディストーション",
    "レジスタ・シンフォニー",
    "パイプライン・カオス",
    "シグナル・サスペンション"
]

KATAKANA_ERRORS = [
    "がバッファ・カタストロフを検出しました",
    "のプロトコル・フェーズが不正です",
    "がデジタル・アンビエントをオーバーフローしました",
    "のメモリ・オーバードライブに失敗しました",
    "がシステム・アトモスフィアを喪失しました",
    "のビット・レゾナンスが崩壊しました",
    "がフレーム・パラダイムを逸脱しました",
    "のセグメント・ファンタジアが消失しました",
    "がストリーム・エクリプスに巻き込まれました",
    "のノード・スペクトルが不安定です",
    "がプロセス・シンクロニシティを失いました",
    "のキャッシュ・オルタナティブが限界です",
    "がスレッド・アブストラクションに迷い込みました",
    "のデータ・コンフリクトが発生しました",
    "がバイナリ・カタルシスを起動できません",
    "のインターフェース・ディストーションが発生しました",
    "がレジスタ・シンフォニーを失調しました",
    "のパイプライン・カオスが暴走しています",
    "がシグナル・サスペンションに陥りました"
]

def generate_katakana_error():
    term = random.choice(KATAKANA_TERMS)
    error = random.choice(KATAKANA_ERRORS)
    return f"{term}{error}"

def notify_desktop(message, title="OSカイセキ通知"):
    if notification:
        try:
            notification.notify(title=title, message=message, timeout=5)
        except Exception:
            pass
    else:
        # Fallback to notify-send if plyer is not available (Linux)
        if sys.platform.startswith('linux'):
            try:
                run(["notify-send", title, message], check=True)
            except Exception:
                pass
        # For MacOS, use osascript
        elif sys.platform == 'darwin':
            try:
                run([
                    "osascript", "-e",
                    f'display notification "{message}" with title "{title}"'
                ], check=True)
            except Exception:
                pass
        # For Windows, fallback to print
        else:
            print(f"[通知] {message}")

def handle_exception(exc_type, exc_value, exc_traceback):
    # Print the real error
    print(''.join(traceback.format_exception(exc_type, exc_value, exc_traceback)), file=sys.stderr)
    # Notify with random katakana error
    msg = generate_katakana_error()
    notify_desktop(msg)
    print(f"[通知] {msg}", file=sys.stderr)

def run_command(args):
    try:
        result = run(args.command, shell=True, check=True, stdout=PIPE, stderr=PIPE, text=True)
        print(result.stdout)
    except CalledProcessError as e:
        print(e.stderr, file=sys.stderr)
        msg = generate_katakana_error()
        notify_desktop(msg)
        print(f"[通知] {msg}", file=sys.stderr)
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        handle_exception(exc_type, exc_value, exc_traceback)

def simulate_error(args):
    try:
        # Simulate a FileNotFoundError
        with open("/this/file/does/not/exist.txt") as f:
            f.read()
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        handle_exception(exc_type, exc_value, exc_traceback)

def main():
    parser = argparse.ArgumentParser(description="random-os-error-kaiseki: エラー時に謎のカタカナOS風通知を生成")
    subparsers = parser.add_subparsers(dest="subcommand")

    cmd_parser = subparsers.add_parser("run", help="指定コマンドを実行し、エラー時にカタカナ通知")
    cmd_parser.add_argument("command", help="実行するコマンド (例: 'ls /notfound')")

    sim_parser = subparsers.add_parser("simulate", help="擬似的にエラーを発生させて通知をテスト")

    args = parser.parse_args()

    if args.subcommand == "run":
        run_command(args)
    elif args.subcommand == "simulate":
        simulate_error(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
