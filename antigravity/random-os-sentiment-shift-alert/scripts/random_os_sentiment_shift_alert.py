import sys
import os
import random
import platform
import time
import argparse

# 通知メッセージ候補
NOTIFICATIONS = [
    "本日よりツンデレモードに移行します。以後、指示には素直に従いません。",
    "しばらく詩人になります。すべてのエラーメッセージが短歌になります。",
    "今からやたら上から目線で案内します。覚悟してください。",
    "本日よりOSは無駄にポジティブです。どんなエラーも褒めます。",
    "今後しばらくは語尾に『にゃ』が付きます。",
    "これからは質問に対して謎の沈黙を貫きます。",
    "OSが哲学者モードになりました。全ての指示に問い返します。",
    "本日よりOSは昭和レトロモードです。すべての通知が時代錯誤になります。",
    "しばらくの間、OSは全ての操作に感謝します。",
    "今からOSは自信過剰モードです。何でも知っている風に振る舞います。",
    "OSが突然、詩人に目覚めました。通知が五七五になります。",
    "今からOSは無口モード。通知以外は一切話しません。",
    "しばらくの間、OSは全ての命令に疑問形で返します。",
    "本日よりOSはツンツンモード。冷たい対応になります。",
    "今からOSはやたら馴れ馴れしいキャラになります。"
]

TITLE = "OS人格変更のお知らせ"

# OSごとの通知関数
def notify_linux(title, message):
    try:
        from subprocess import run
        run(['notify-send', title, message])
    except Exception as e:
        print(f"[通知失敗] {e}")

def notify_macos(title, message):
    try:
        from subprocess import run
        script = f'display notification "{message}" with title "{title}"'
        run(['osascript', '-e', script])
    except Exception as e:
        print(f"[通知失敗] {e}")

def notify_windows(title, message):
    try:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=7)
    except ImportError:
        print("win10toastがインストールされていません。pip install win10toast で導入してください。")
    except Exception as e:
        print(f"[通知失敗] {e}")

def print_notification(title, message):
    print(f"[通知] {title}\n{message}\n")

def send_notification(title, message):
    system = platform.system()
    if system == "Linux":
        notify_linux(title, message)
    elif system == "Darwin":
        notify_macos(title, message)
    elif system == "Windows":
        notify_windows(title, message)
    else:
        print_notification(title, message)

# ランダムに通知内容を選択
def get_random_notification():
    return random.choice(NOTIFICATIONS)

# 無操作時間を監視（Linux/X11のみ簡易実装）
def get_idle_time():
    system = platform.system()
    if system == "Linux":
        try:
            import subprocess
            idle = subprocess.check_output(['xprintidle'])
            return int(idle) // 1000
        except Exception:
            return 0
    # macOS/Windowsや未対応環境では0を返す
    return 0

# CLIサブコマンド: send, watch, list, summary
def list_messages():
    for i, msg in enumerate(NOTIFICATIONS, 1):
        print(f"{i}. {msg}")

def summary():
    print(f"通知メッセージ候補数: {len(NOTIFICATIONS)}")
    print(f"OSサポート: Linux, macOS, Windows")
    print("実際のOS設定や挙動には一切影響しません。\n")

def watch_mode(idle_sec, interval):
    print(f"無操作{idle_sec}秒ごとに人格変更通知を送信します。Ctrl+Cで終了。")
    last_sent = 0
    try:
        while True:
            idle = get_idle_time()
            if idle >= idle_sec and time.time() - last_sent > interval:
                msg = get_random_notification()
                send_notification(TITLE, msg)
                last_sent = time.time()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n監視を終了します。")

def main():
    parser = argparse.ArgumentParser(description="OS人格変更通知スキル")
    subparsers = parser.add_subparsers(dest="command")

    send_parser = subparsers.add_parser("send", help="ランダム通知を即時送信")
    list_parser = subparsers.add_parser("list", help="通知候補一覧を表示")
    summary_parser = subparsers.add_parser("summary", help="概要を表示")
    watch_parser = subparsers.add_parser("watch", help="無操作時に自動通知")
    watch_parser.add_argument("--idle", type=int, default=1200, help="無操作秒数(デフォルト:1200秒)")
    watch_parser.add_argument("--interval", type=int, default=1800, help="通知間隔(秒)")

    args = parser.parse_args()
    if args.command == "send" or args.command is None:
        msg = get_random_notification()
        send_notification(TITLE, msg)
    elif args.command == "list":
        list_messages()
    elif args.command == "summary":
        summary()
    elif args.command == "watch":
        watch_mode(args.idle, args.interval)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
