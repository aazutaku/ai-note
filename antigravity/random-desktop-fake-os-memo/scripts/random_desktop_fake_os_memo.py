import sys
import os
import random
import time
import argparse
import platform
import subprocess
from typing import List

MEMO_LIST = [
    "冷蔵庫にプリンあり",
    "上司が見ている",
    "バグは空から降ってくる",
    "謎の引き出しを開けるな",
    "今日は何曜日でもない",
    "システムがあなたを見つめています",
    "画面の右下を見てはいけない",
    "コードに名前をつけてはいけない",
    "この通知は幻です",
    "再起動しても戻らない",
    "USBメモリは抜かないで",
    "電源ボタンは押すな",
    "ログイン画面に秘密がある",
    "このメッセージは自動で消えません",
    "何もしていないのに壊れた",
    "あなたの後ろに誰かいる",
    "今日の運勢: バグ多め",
    "コーヒーをこぼすな",
    "ファイル名は秘密",
    "メモリが逃げ出した",
    "この通知を無視しないで",
    "デバッグは夢の中で",
    "謎のエラーが発生しました",
    "キーボードが逆さまです",
    "マウスが迷子",
    "プリンターが踊りだす",
    "画面の端に何かいる",
    "設定ファイルを開かないで",
    "今日も一日意味不明",
    "あなたは選ばれし者"
]

def get_random_memo() -> str:
    return random.choice(MEMO_LIST)

def notify_linux(message: str):
    try:
        subprocess.run([
            'notify-send', 'OSメモ', message
        ], check=True)
    except Exception as e:
        print(f"[通知失敗] {e}")

def notify_macos(message: str):
    try:
        subprocess.run([
            'osascript', '-e', f'display notification "{message}" with title "OSメモ"'
        ], check=True)
    except Exception as e:
        print(f"[通知失敗] {e}")

def notify_windows(message: str):
    try:
        import win10toast
        toaster = win10toast.ToastNotifier()
        toaster.show_toast("OSメモ", message, duration=5)
    except ImportError:
        print("win10toastがインストールされていません。pip install win10toast で導入してください。")
    except Exception as e:
        print(f"[通知失敗] {e}")

def show_notification(message: str):
    sys_platform = platform.system()
    if sys_platform == "Linux":
        notify_linux(message)
    elif sys_platform == "Darwin":
        notify_macos(message)
    elif sys_platform == "Windows":
        notify_windows(message)
    else:
        print(f"[通知] OSメモ: {message}")

def list_memos():
    print("--- OSメモ候補一覧 ---")
    for idx, memo in enumerate(MEMO_LIST):
        print(f"{idx+1:02d}: {memo}")

def summary():
    print(f"登録されている怪文書メモ数: {len(MEMO_LIST)}")
    print(f"例: {random.choice(MEMO_LIST)}")

def log_memo():
    memo = get_random_memo()
    print(f"[通知] OSメモ: {memo}")
    show_notification(memo)

def random_loop(interval_min: int, interval_max: int, count: int):
    for i in range(count):
        memo = get_random_memo()
        print(f"[通知] OSメモ: {memo}")
        show_notification(memo)
        if i < count - 1:
            delay = random.randint(interval_min, interval_max)
            time.sleep(delay)

def parse_args():
    parser = argparse.ArgumentParser(description="random-desktop-fake-os-memo: 謎のOSメモをデスクトップ通知で表示")
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_log = subparsers.add_parser('log', help='ランダムなOSメモを1回通知')
    parser_list = subparsers.add_parser('list', help='OSメモ候補一覧を表示')
    parser_summary = subparsers.add_parser('summary', help='メモ候補のサマリを表示')
    parser_loop = subparsers.add_parser('loop', help='一定回数ランダム間隔で通知')
    parser_loop.add_argument('--min', type=int, default=10, help='通知間隔の最小秒数 (デフォルト10)')
    parser_loop.add_argument('--max', type=int, default=60, help='通知間隔の最大秒数 (デフォルト60)')
    parser_loop.add_argument('--count', type=int, default=5, help='通知回数 (デフォルト5)')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'log':
        log_memo()
    elif args.command == 'list':
        list_memos()
    elif args.command == 'summary':
        summary()
    elif args.command == 'loop':
        random_loop(args.min, args.max, args.count)
    else:
        print("不明なコマンドです")

if __name__ == '__main__':
    main()
