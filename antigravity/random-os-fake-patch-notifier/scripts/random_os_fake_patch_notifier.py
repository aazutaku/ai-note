import random
import time
import sys
import argparse
import platform
import subprocess
from datetime import datetime

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

FAKE_PATCH_NOTES = [
    [
        "バグ修正: やる気が0になる問題を修正",
        "新機能: 午後3時に眠気を自動注入",
        "既知の問題: 希望が時々消失することがあります"
    ],
    [
        "バグ修正: キーボードが突然歌い出す問題を修正",
        "新機能: 画面の端にランダムな猫が出現します",
        "既知の問題: コーヒーが冷める速度が2倍になっています"
    ],
    [
        "新機能: 3時のおやつ自動リマインダーを追加",
        "バグ修正: 画面を見つめすぎると現実逃避する問題を修正",
        "既知の問題: タスクバーが時々踊りだします"
    ],
    [
        "新機能: 進捗がない場合、画面が自動で暗転します",
        "バグ修正: ウィンドウが勝手に閉じる問題を修正",
        "既知の問題: 進捗が出るとは限りません"
    ],
    [
        "バグ修正: 机から物が落ちる現象を修正(未検証)",
        "新機能: 画面右下に謎のボタンを追加(用途不明)",
        "既知の問題: ボタンを押すと何も起きません"
    ],
    [
        "新機能: 週末になると自動で休憩を提案します",
        "バグ修正: 画面が突然真っ白になる問題を修正",
        "既知の問題: 休憩提案がしつこい場合があります"
    ],
    [
        "バグ修正: マウスが現実世界をクリックする問題を修正",
        "新機能: 画面内にランダムな犬が出現します",
        "既知の問題: 犬が吠えることがあります"
    ],
    [
        "新機能: 進捗バーが気分で変動します",
        "バグ修正: 画面の色が突然変わる問題を修正",
        "既知の問題: 進捗バーが現実を反映しません"
    ]
]

VERSION_FORMATS = [
    "v{major}.{minor}.{patch}",
    "v{major}.{minor}.{patch}-beta",
    "v{major}.{minor}.{patch}-rc{rc}"
]

def random_version():
    major = random.randint(1, 15)
    minor = random.randint(0, 99)
    patch = random.randint(0, 99)
    rc = random.randint(1, 5)
    fmt = random.choice(VERSION_FORMATS)
    return fmt.format(major=major, minor=minor, patch=patch, rc=rc)

def random_patch_note():
    notes = random.choice(FAKE_PATCH_NOTES)
    random.shuffle(notes)
    return notes

def show_notification(title, message):
    if PLYER_AVAILABLE:
        notification.notify(
            title=title,
            message=message,
            timeout=8
        )
    else:
        plat = platform.system()
        if plat == "Darwin":
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "{title}"'
            ])
        elif plat == "Linux":
            subprocess.run([
                "notify-send", title, message])
        elif plat == "Windows":
            # fallback: print to stdout
            print(f"[通知] {title}\n{message}")
        else:
            print(f"[通知] {title}\n{message}")

def generate_fake_patch_note():
    version = random_version()
    notes = random_patch_note()
    title = f"OSパッチノート {version}"
    message = "\n".join(notes)
    return title, message

def log_notification(title, message):
    logline = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {title}\n{message}\n"
    with open(".random_os_fake_patch_notifier.log", "a", encoding="utf-8") as f:
        f.write(logline)

def random_wait(min_sec=60, max_sec=900):
    return random.randint(min_sec, max_sec)

def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Patch Notifier Skill")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser("log", help="通知履歴を表示")
    parser_list = subparsers.add_parser("list", help="通知履歴をリスト表示")
    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリーを表示")
    parser_run = subparsers.add_parser("run", help="Skill本体を実行 (常駐) ※Ctrl+Cで停止")
    parser_run.add_argument("--min", type=int, default=60, help="通知の最小間隔(秒)")
    parser_run.add_argument("--max", type=int, default=900, help="通知の最大間隔(秒)")

    args = parser.parse_args()

    if args.command == "log":
        try:
            with open(".random_os_fake_patch_notifier.log", encoding="utf-8") as f:
                print(f.read())
        except FileNotFoundError:
            print("通知履歴がありません。")
    elif args.command == "list":
        try:
            with open(".random_os_fake_patch_notifier.log", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("["):
                        print(line.strip())
        except FileNotFoundError:
            print("通知履歴がありません。")
    elif args.command == "summary":
        try:
            with open(".random_os_fake_patch_notifier.log", encoding="utf-8") as f:
                lines = f.readlines()
            count = sum(1 for l in lines if l.startswith("["))
            print(f"通知回数: {count}")
            if count > 0:
                print(f"最新: {lines[-3].strip()}")
        except FileNotFoundError:
            print("通知履歴がありません。")
    elif args.command == "run":
        print("[INFO] Random OS Fake Patch Notifier Skillを開始します。Ctrl+Cで停止。")
        try:
            while True:
                wait_sec = random_wait(args.min, args.max)
                time.sleep(wait_sec)
                title, message = generate_fake_patch_note()
                show_notification(title, message)
                log_notification(title, message)
        except KeyboardInterrupt:
            print("\n[INFO] Skillを終了します。")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
