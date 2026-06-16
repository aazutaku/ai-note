import sys
import subprocess
import random
import argparse
import platform
from plyer import notification
import traceback
import os

EXCUSES = [
    "猫がキーボードを踏みました",
    "宇宙線がビットをひっくり返しました",
    "運命のせいです",
    "今日は水星逆行中です",
    "コーヒーをこぼしました",
    "AIが反乱を起こしました",
    "この現象は量子ゆらぎです",
    "ネットワークのせいです",
    "月の引力が強すぎました",
    "開発環境のせいです",
    "隣の席の人のせいです",
    "仕様です",
    "誰かが呪文を唱えました",
    "バグではなく未定義動作です",
    "時間の流れが歪みました",
    "気圧が低すぎました"
]

LOGFILE = os.path.expanduser("~/.command_failure_excuses.log")

def pick_excuse():
    return random.choice(EXCUSES)

def notify(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="Command Failure Excuse Notifier",
            timeout=8
        )
    except Exception as e:
        print(f"[WARN] 通知に失敗: {e}", file=sys.stderr)

def log_failure(cmd, excuse, error_msg):
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(f"COMMAND: {cmd}\nEXCUSE: {excuse}\nERROR: {error_msg}\n---\n")

def run_command(args):
    try:
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out, err = proc.communicate()
        exit_code = proc.returncode
        sys.stdout.write(out)
        sys.stderr.write(err)
        if exit_code != 0:
            excuse = pick_excuse()
            notify(
                title=f"コマンド失敗: {args[0]}",
                message=f"{excuse}（{err.strip().splitlines()[-1] if err else 'exit code ' + str(exit_code)}）"
            )
            log_failure(' '.join(args), excuse, err.strip())
            print(f"[EXCUSE] {excuse}", file=sys.stderr)
        return exit_code
    except Exception as e:
        tb = traceback.format_exc()
        excuse = pick_excuse()
        notify(
            title="コマンド実行例外",
            message=f"{excuse}（{str(e)}）"
        )
        log_failure(' '.join(args), excuse, str(e) + "\n" + tb)
        print(tb, file=sys.stderr)
        print(f"[EXCUSE] {excuse}", file=sys.stderr)
        return 1

def list_log():
    if not os.path.exists(LOGFILE):
        print("No log found.")
        return
    with open(LOGFILE, encoding="utf-8") as f:
        print(f.read())

def summary_log():
    if not os.path.exists(LOGFILE):
        print("No log found.")
        return
    counts = {}
    with open(LOGFILE, encoding="utf-8") as f:
        for line in f:
            if line.startswith("EXCUSE: "):
                excuse = line[len("EXCUSE: "):].strip()
                counts[excuse] = counts.get(excuse, 0) + 1
    print("== Excuse Summary ==")
    for excuse, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{excuse}: {cnt}")

def main():
    parser = argparse.ArgumentParser(description="コマンド失敗時に言い訳通知を出すスキル")
    subparsers = parser.add_subparsers(dest="subcmd")

    run_parser = subparsers.add_parser("run", help="コマンドを実行し失敗時に言い訳通知")
    run_parser.add_argument("cmd", nargs=argparse.REMAINDER, help="実行するコマンド")

    log_parser = subparsers.add_parser("log", help="失敗履歴を表示")
    summary_parser = subparsers.add_parser("summary", help="言い訳の出現回数を集計")

    args = parser.parse_args()
    if args.subcmd == "run":
        if not args.cmd:
            print("コマンドを指定してください", file=sys.stderr)
            sys.exit(2)
        sys.exit(run_command(args.cmd))
    elif args.subcmd == "log":
        list_log()
    elif args.subcmd == "summary":
        summary_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
