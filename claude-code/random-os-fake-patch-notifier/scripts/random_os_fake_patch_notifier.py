import sys
import time
import random
import argparse
import platform
import subprocess
from datetime import datetime

# 架空のパッチノート生成用データ
FAKE_BUGS = [
    "やる気が0になる問題を修正",
    "キーボードの『やる気』キーが物理的に消失する問題を解決",
    "コーヒー検出機能が誤作動する場合があります",
    "マウスカーソルが画面外に逃げ出すバグを修正",
    "CPUが突然詩を詠み始める問題を修正",
    "ディスプレイがランダムに上下逆さまになる現象を解決",
    "タスクバーが昼寝を始めるバグを修正",
    "音量ミキサーが勝手にクラシックモードになる問題",
    "スクリーンセーバーが現実逃避するバグを修正",
    "ファイル名が全て『未定』になる問題を解決"
]
FAKE_FEATURES = [
    "午後3時になると自動で睡魔を注入します",
    "新しい『やる気ブースト』ボタンを追加",
    "ランダムで壁紙が昭和風に変わる機能",
    "USB接続時に『ご褒美』サウンドを再生",
    "自動でタスクを先延ばしする機能",
    "進捗ゼロでも祝福通知を送信",
    "マウスポインタが時々ジャンプする新仕様",
    "未保存ファイルを自動で妄想保存",
    "『やる気』メーターを常時表示",
    "新しいバグを毎週自動生成"
]
FAKE_KNOWN_ISSUES = [
    "コーヒー検出機能が誤作動する場合があります",
    "進捗バーが逆走することがあります",
    "やる気ブーストが一時的に無効になることがあります",
    "壁紙が昭和風に固定されることがあります",
    "USBご褒美サウンドが鳴らない場合があります",
    "未保存ファイルが妄想保存されないことがあります",
    "祝福通知が過剰に発生する場合があります"
]


def generate_fake_patch_note():
    version = f"{random.randint(1, 10)}.{random.randint(0, 20)}.{random.randint(0, 99)}"
    bugs = random.sample(FAKE_BUGS, k=random.randint(1, 2))
    features = random.sample(FAKE_FEATURES, k=random.randint(1, 2))
    known_issues = random.sample(FAKE_KNOWN_ISSUES, k=1)
    lines = [f"OS Patch Notes {version}"]
    for b in bugs:
        lines.append(f"- バグ修正: {b}")
    for f in features:
        lines.append(f"- 新機能: {f}")
    for k in known_issues:
        lines.append(f"- 既知の問題: {k}")
    return "\n".join(lines)


def send_notification(title, message):
    system = platform.system()
    try:
        if system == "Darwin":  # macOS
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            subprocess.run(["notify-send", title, message], check=True)
        elif system == "Windows":
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(title, message, duration=7)
        else:
            print(f"[通知] {title}\n{message}")
    except Exception as e:
        print(f"通知送信に失敗しました: {e}")
        print(f"[通知] {title}\n{message}")


def log_patch_note(note):
    log_file = "random_os_fake_patch.log"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}]\n{note}\n\n")


def list_logs():
    log_file = "random_os_fake_patch.log"
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("まだ通知履歴がありません。")


def summary_logs():
    log_file = "random_os_fake_patch.log"
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        count = sum(1 for l in lines if l.startswith("["))
        print(f"通知履歴数: {count}")
    except FileNotFoundError:
        print("まだ通知履歴がありません。")


def random_wait_loop(min_sec=600, max_sec=3600):
    while True:
        wait_time = random.randint(min_sec, max_sec)
        time.sleep(wait_time)
        note = generate_fake_patch_note()
        send_notification("OS Patch Notes", note)
        log_patch_note(note)


def main():
    parser = argparse.ArgumentParser(description="謎のOSパッチノート通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_notify = subparsers.add_parser("notify", help="即座に通知を発生させる")
    parser_loop = subparsers.add_parser("loop", help="ランダムなタイミングで自動通知を繰り返す")
    parser_list = subparsers.add_parser("list", help="通知履歴を表示")
    parser_summary = subparsers.add_parser("summary", help="通知履歴の件数を表示")

    args = parser.parse_args()

    if args.command == "notify":
        note = generate_fake_patch_note()
        send_notification("OS Patch Notes", note)
        log_patch_note(note)
    elif args.command == "loop":
        print("ランダム通知ループを開始します (Ctrl+Cで停止)...")
        try:
            random_wait_loop()
        except KeyboardInterrupt:
            print("\n通知ループを終了しました。")
    elif args.command == "list":
        list_logs()
    elif args.command == "summary":
        summary_logs()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
