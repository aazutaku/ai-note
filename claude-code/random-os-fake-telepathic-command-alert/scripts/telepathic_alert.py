import sys
import argparse
import random
import time
import platform
import subprocess
from typing import List

# テレパシーコマンド候補
FAKE_COMMANDS = [
    "make coffee",
    "brew install happiness",
    "sudo teleport /workspace moon_base",
    "git push --force-to-parallel-universe",
    "deploy to mars",
    "rm -rf /anxiety",
    "activate time_machine",
    "pip install dreams",
    "open portal --to=vacation",
    "chmod +x /motivation",
    "start quantum-debugger",
    "echo 'hello multiverse'",
    "docker run -it unicorn:latest",
    "ssh root@telepathy-server",
    "cat /etc/telepathy.conf",
    "ls /hidden/desires",
    "sudo reboot universe",
    "git merge --strategy=telepathy",
    "npm install --global inspiration",
    "python -m daydream"
]

# テレパシー通知メッセージテンプレート
TEMPLATES = [
    "あなたが心の中で考えたコマンドを検出しました: '{cmd}'",
    "念波キャッチ: '{cmd}'",
    "OSがあなたの妄想コマンドを感知: '{cmd}'",
    "読心術発動: '{cmd}'",
    "未知のコマンドが念波で伝わりました: '{cmd}'",
    "テレパシー通信受信: '{cmd}'",
    "OSがあなたの未来予想コマンドを捕捉: '{cmd}'",
    "サイキック検出: '{cmd}'",
    "脳内コマンドインターセプト: '{cmd}'",
    "OSがあなたの思念を読み取りました: '{cmd}'"
]

# OS通知を送信する（クロスプラットフォーム対応）
def send_notification(message: str):
    system = platform.system()
    if system == "Darwin":  # macOS
        script = f'display notification "{message}" with title "Telepathic OS Alert"'
        subprocess.run(["osascript", "-e", script], check=False)
    elif system == "Linux":
        try:
            subprocess.run(["notify-send", "Telepathic OS Alert", message], check=False)
        except FileNotFoundError:
            print(f"[Telepathic OS Alert]\n{message}")
    elif system == "Windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("Telepathic OS Alert", message, duration=5)
        except ImportError:
            print(f"[Telepathic OS Alert]\n{message}")
    else:
        print(f"[Telepathic OS Alert]\n{message}")

# ランダムなフェイク通知を生成
def generate_fake_alert() -> str:
    cmd = random.choice(FAKE_COMMANDS)
    template = random.choice(TEMPLATES)
    return template.format(cmd=cmd)

# ログ保存はしないが、出力履歴用にメモリ保持（デモ用）
ALERT_HISTORY: List[str] = []

# コマンド: 通知を1回表示
def alert_once(args):
    message = generate_fake_alert()
    send_notification(message)
    ALERT_HISTORY.append(message)
    print(f"[Telepathic OS Alert]\n{message}")

# コマンド: 指定回数通知
def alert_multi(args):
    count = args.count
    interval = args.interval
    for _ in range(count):
        alert_once(args)
        time.sleep(interval)

# コマンド: 履歴リスト（このSkillではメモリのみ）
def alert_list(args):
    if not ALERT_HISTORY:
        print("まだ通知履歴はありません。")
    else:
        print("--- Telepathic OS Alert 履歴 ---")
        for i, msg in enumerate(ALERT_HISTORY, 1):
            print(f"{i:02d}: {msg}")

# コマンド: サマリー
def alert_summary(args):
    print(f"通知回数: {len(ALERT_HISTORY)}")
    if ALERT_HISTORY:
        print(f"最新通知: {ALERT_HISTORY[-1]}")

# 引数パーサ
def build_parser():
    parser = argparse.ArgumentParser(
        description="OSが読心術で検出した架空コマンド通知をランダム表示するSkill"
    )
    subparsers = parser.add_subparsers(dest="command")
    # alert once
    p_once = subparsers.add_parser("alert", help="1回だけ通知を表示")
    p_once.set_defaults(func=alert_once)
    # alert multi
    p_multi = subparsers.add_parser("multi", help="複数回ランダム通知")
    p_multi.add_argument("--count", type=int, default=3, help="通知回数")
    p_multi.add_argument("--interval", type=float, default=2.0, help="通知間隔(秒)")
    p_multi.set_defaults(func=alert_multi)
    # list
    p_list = subparsers.add_parser("list", help="通知履歴を表示")
    p_list.set_defaults(func=alert_list)
    # summary
    p_summary = subparsers.add_parser("summary", help="通知サマリーを表示")
    p_summary.set_defaults(func=alert_summary)
    return parser

# メインエントリ
if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
