import sys
import os
import random
import platform
import subprocess
import argparse
try:
    from win10toast import ToastNotifier
except ImportError:
    ToastNotifier = None

MEMO_LIST = [
    "冷蔵庫にプリンあり",
    "上司が見ている",
    "バグは空から降ってくる",
    "謎の引き出しを開けるな",
    "システムはあなたを見ている",
    "今日の運勢: ファイルが消えるかも",
    "この通知は意味がありません",
    "未確認のプロセスが起動しました",
    "あなたの席に誰かが座った",
    "OSがあなたに微笑んでいます",
    "エラー: エラーがありません",
    "次の会議は10分前に終了しました",
    "USBポートに謎の力を感じる",
    "メモ: コーヒーを飲みすぎないで",
    "警告: 何も警告しません",
    "デバッグ: ここはデバッグしないで",
    "秘密: この通知は自動で消えます",
    "ファイルシステムが踊っています",
    "メモリがあなたを覚えています",
    "新しいバグが生まれました",
    "このメモは消せません",
    "謎のプロセスが終了しました",
    "あなたのマウスが迷子です",
    "今日のラッキーカラー: #404040",
    "タスクバーが息をしています",
    "この通知はランダムです",
    "OSからの挑戦状",
    "あなたの机の下に秘密があります",
    "意味不明なエラーが発生しました",
    "このメモは読まないでください"
]

TITLE = "謎のOSメモ"

def pick_random_memo():
    return random.choice(MEMO_LIST)

def notify_linux(summary, body):
    try:
        subprocess.run([
            'notify-send', summary, body
        ], check=True)
    except Exception as e:
        print(f"[ERROR] Linux通知失敗: {e}")

def notify_macos(summary, body):
    try:
        script = f'display notification "{body}" with title "{summary}"'
        subprocess.run([
            'osascript', '-e', script
        ], check=True)
    except Exception as e:
        print(f"[ERROR] macOS通知失敗: {e}")

def notify_windows(summary, body):
    if ToastNotifier is None:
        print("[ERROR] win10toastがインストールされていません。pip install win10toast を実行してください。")
        return
    try:
        toaster = ToastNotifier()
        toaster.show_toast(summary, body, duration=5, threaded=True)
    except Exception as e:
        print(f"[ERROR] Windows通知失敗: {e}")

def notify(summary, body):
    sys_platform = platform.system()
    if sys_platform == 'Linux':
        notify_linux(summary, body)
    elif sys_platform == 'Darwin':
        notify_macos(summary, body)
    elif sys_platform == 'Windows':
        notify_windows(summary, body)
    else:
        print(f"[WARN] 未対応OS: {sys_platform}. 通知内容: {summary}: {body}")

def list_memos():
    print("--- 謎のOSメモ候補一覧 ---")
    for idx, memo in enumerate(MEMO_LIST, 1):
        print(f"{idx:2d}. {memo}")

def summary():
    print("このスキルは、完全ランダムな謎のメモをデスクトップ通知として表示します。\n通知内容は実用性ゼロの怪文書です。\n対応OS: Linux, macOS, Windows")

def parse_args():
    parser = argparse.ArgumentParser(description='random-desktop-fake-os-memo: 謎のOSメモをランダム通知')
    subparsers = parser.add_subparsers(dest='command', required=False)

    subparsers.add_parser('log', help='謎のメモを1件ランダム通知')
    subparsers.add_parser('list', help='メモ候補一覧を表示')
    subparsers.add_parser('summary', help='スキル概要を表示')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.command is None or args.command == 'log':
        memo = pick_random_memo()
        print(f"[デスクトップ通知]\n{TITLE}: {memo}")
        notify(TITLE, memo)
    elif args.command == 'list':
        list_memos()
    elif args.command == 'summary':
        summary()
    else:
        print("[ERROR] 未知のコマンドです。--help を参照してください。")

if __name__ == '__main__':
    main()
