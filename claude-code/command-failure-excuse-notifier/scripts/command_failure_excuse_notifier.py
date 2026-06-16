import argparse
import subprocess
import random
import sys
import platform
from typing import List, Tuple

try:
    from plyer import notification
except ImportError:
    notification = None

EXCUSES = [
    "猫がキーボードを踏みました",
    "運命のせいです",
    "宇宙線がビットをひっくり返しました",
    "今日は星の巡りが悪いようです",
    "コーヒーをこぼしました",
    "ネットワークの妖精がいたずらしました",
    "月の引力が強すぎました",
    "バグではなく仕様です",
    "AIが休憩中でした",
    "きっと誰かのせいです"
]

def get_random_excuse() -> str:
    return random.choice(EXCUSES)

def send_notification(title: str, message: str):
    if notification:
        try:
            notification.notify(
                title=title,
                message=message,
                app_name="Command Failure Excuse Notifier",
                timeout=8
            )
        except Exception as e:
            print(f"[WARN] 通知送信に失敗: {e}", file=sys.stderr)
    else:
        # plyer未導入の場合は警告
        print("[WARN] plyer未導入のため通知は表示されません", file=sys.stderr)

def run_command(command: List[str]) -> Tuple[int, str, str]:
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def print_and_notify_error(command: List[str], returncode: int, stderr: str):
    print(f"[ERROR] Command failed: {' '.join(command)}")
    if stderr:
        print(f"[STDERR] {stderr.strip()}")
    excuse = get_random_excuse()
    print(f"[EXCUSE] 言い訳: {excuse}")
    send_notification(
        title="コマンド失敗: 言い訳通知",
        message=f"{excuse}\n(エラー: {' '.join(command)})"
    )

def list_excuses():
    print("利用可能な言い訳リスト:")
    for idx, excuse in enumerate(EXCUSES, 1):
        print(f"  {idx}. {excuse}")

def summary():
    print("Skill概要:")
    print("  コマンド失敗時に毎回異なる言い訳をOS通知&標準出力に表示します。\n  plyerによるクロスプラットフォーム通知対応。\n  言い訳はランダム選択されます。\n  エラーメッセージは失われません。")

def main():
    parser = argparse.ArgumentParser(description="コマンド失敗時に言い訳を通知するSkill")
    subparsers = parser.add_subparsers(dest="subcmd", help="サブコマンド")

    parser_run = subparsers.add_parser("run", help="コマンドを実行し失敗時に言い訳通知")
    parser_run.add_argument("--run", nargs=argparse.REMAINDER, help="実行するコマンド")

    parser_list = subparsers.add_parser("list", help="言い訳リストを表示")
    parser_summary = subparsers.add_parser("summary", help="Skill概要を表示")

    args = parser.parse_args()

    if args.subcmd == "run":
        if not args.run or len(args.run) == 0:
            print("--run の後に実行コマンドを指定してください", file=sys.stderr)
            sys.exit(2)
        command = args.run
        returncode, stdout, stderr = run_command(command)
        if returncode != 0:
            print_and_notify_error(command, returncode, stderr)
        else:
            print(stdout.strip())
    elif args.subcmd == "list":
        list_excuses()
    elif args.subcmd == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
