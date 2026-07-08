import sys
import os
import random
import subprocess
import argparse
import platform
import time
from datetime import datetime

CYBERPUNK_MESSAGES = [
    ("NeuroOS", "ニューロン接続不良を検出: シナプス・インターフェース再起動推奨"),
    ("ChromeSys", "クローム義手ファームウェアのアップデートが利用可能です"),
    ("SynthWave", "シンセ脳波異常: 脳内信号の再調整を推奨"),
    ("GhostShell", "ゴースト・プロトコルがアクティブ化されました"),
    ("GridNet", "ネットワーク・ジャック警告: 外部アクセス試行を検出"),
    ("PulseCore", "バイオ・バッテリー残量低下: 充電ステーションへの接続を推奨"),
    ("NanoGuard", "ナノマシン自己修復モードが作動しました"),
    ("OptiLink", "視覚拡張モジュールの再調整が必要です"),
    ("CipherSec", "暗号化プロトコルの異常検出: セキュリティ監査を推奨"),
    ("EchoGrid", "サウンド・フィードバックループ警告: 音声出力の制御を推奨"),
    ("NeuroOS", "仮想人格の同期ズレを検出: メモリ断片化の可能性あり"),
    ("GhostShell", "自己認証失敗: ゴーストIDの再登録が必要です"),
    ("PulseCore", "生体認証データの更新を推奨します"),
    ("SynthWave", "脳波パターンが異常値を記録: 医療AIに連絡推奨"),
    ("GridNet", "外部ネットワークからの不審な信号を遮断しました"),
]

OS_TYPE = platform.system()


def show_notification(title, message):
    try:
        if OS_TYPE == "Darwin":
            # macOS: Use terminal-notifier if available
            if shutil.which("terminal-notifier"):
                subprocess.run([
                    "terminal-notifier",
                    "-title", title,
                    "-message", message
                ])
            else:
                # fallback to AppleScript
                script = f'display notification "{message}" with title "{title}"'
                subprocess.run(["osascript", "-e", script])
        elif OS_TYPE == "Linux":
            if shutil.which("notify-send"):
                subprocess.run(["notify-send", title, message])
            else:
                print(f"[通知失敗] notify-sendが見つかりません: {title} - {message}")
        elif OS_TYPE == "Windows":
            try:
                from plyer import notification
                notification.notify(title=title, message=message, app_name="Cyberpunk Notifier")
            except ImportError:
                print(f"[通知失敗] plyerパッケージが必要です: {title} - {message}")
        else:
            print(f"[通知未対応OS] {title}: {message}")
    except Exception as e:
        print(f"[通知エラー] {e}")


def random_message():
    return random.choice(CYBERPUNK_MESSAGES)


def notify_once():
    title, message = random_message()
    show_notification(title, message)
    print(f"[{title}] {message}")


def notify_loop(interval, count):
    for i in range(count):
        notify_once()
        if i < count - 1:
            time.sleep(interval)


def list_messages():
    print("--- サイバーパンク風通知メッセージ一覧 ---")
    for title, msg in CYBERPUNK_MESSAGES:
        print(f"[{title}] {msg}")


def summary():
    print("Skill: random-os-fake-cyberpunk-notifier")
    print(f"通知パターン数: {len(CYBERPUNK_MESSAGES)}")
    print(f"対応OS: macOS, Linux, Windows")
    print(f"通知API: terminal-notifier, notify-send, plyer")


def parse_args():
    parser = argparse.ArgumentParser(description="サイバーパンク風の架空OS通知をデスクトップに表示します。")
    subparsers = parser.add_subparsers(dest="command")

    parser_once = subparsers.add_parser("notify", help="1回だけ通知を表示")
    parser_loop = subparsers.add_parser("loop", help="指定回数/間隔で通知を繰り返す")
    parser_loop.add_argument("-n", "--count", type=int, default=5, help="通知回数 (デフォルト: 5)")
    parser_loop.add_argument("-i", "--interval", type=int, default=60, help="通知間隔(秒) (デフォルト: 60)")
    parser_list = subparsers.add_parser("list", help="全通知メッセージを表示")
    parser_summary = subparsers.add_parser("summary", help="Skill概要を表示")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "notify":
        notify_once()
    elif args.command == "loop":
        notify_loop(args.interval, args.count)
    elif args.command == "list":
        list_messages()
    elif args.command == "summary":
        summary()
    else:
        print("使い方: python cyberpunk_notifier.py [notify|loop|list|summary]")
        print("例: python cyberpunk_notifier.py notify")

if __name__ == '__main__':
    import shutil
    main()
