import random
import sys
import time
import argparse
import platform
from threading import Thread

try:
    from plyer import notification
except ImportError:
    notification = None
    
try:
    from win10toast import ToastNotifier
except ImportError:
    ToastNotifier = None

def get_os():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        return 'windows'
    elif 'darwin' in os_name:
        return 'macos'
    elif 'linux' in os_name:
        return 'linux'
    else:
        return 'unknown'

DRAMATIC_MESSAGES = [
    "システムはあと3分で壮絶にシャットダウンします（理由：宇宙エネルギー調整のため）",
    "全プロセスよ、さらば…",
    "OSカーネル、最後の咆哮をあげよ！",
    "電源オフまで残り42秒。運命に抗うな。",
    "本日はこれにて全ての稼働を終了します（理由：量子トンネルのメンテナンス）",
    "管理者の気まぐれにより、全てのプロセスは消滅します。",
    "シャットダウン・オブ・ザ・ギャラクシー、発動準備完了。",
    "このOSは今宵、伝説となる。",
    "プロセスよ、永遠の眠りにつけ。",
    "全ユーザーに告ぐ：あと120秒でこの世界は終焉を迎えます。",
    "メモリ解放の儀式を開始します。",
    "CPUの魂よ、昇華せよ。",
    "システムは自己崩壊プロトコルを実行します。",
    "電源ボタンが勝手に押されます。",
    "全てのファイルが記憶の彼方へ旅立ちます。",
    "OSの寿命が尽きました。",
    "カオスな電源オフ、今ここに。",
    "仮想世界の終末時計が0を指しました。",
    "全プロセス、最後のログを残せ。",
    "この通知を見たあなたはラッキーです。"
]


def send_notification(title, message):
    os_type = get_os()
    if os_type == 'windows' and ToastNotifier is not None:
        try:
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=7, threaded=True)
            return True
        except Exception as e:
            pass
    if notification is not None:
        try:
            notification.notify(title=title, message=message, app_name="Dramatic Poweroff Alert", timeout=7)
            return True
        except Exception as e:
            pass
    # Fallback: print to console
    print(f"[通知] {message}")
    return False

def random_message():
    return random.choice(DRAMATIC_MESSAGES)

def alert_once():
    title = "壮大な電源オフ予告"
    message = random_message()
    send_notification(title, message)

def alert_loop(count=5, interval=60):
    title = "壮大な電源オフ予告"
    used = set()
    for _ in range(count):
        msg = random_message()
        # なるべく重複を避ける
        while msg in used and len(used) < len(DRAMATIC_MESSAGES):
            msg = random_message()
        used.add(msg)
        send_notification(title, msg)
        time.sleep(interval)

def list_messages():
    print("=== Dramatic Poweroff Alert: メッセージ一覧 ===")
    for i, msg in enumerate(DRAMATIC_MESSAGES, 1):
        print(f"{i}. {msg}")

def summary():
    print("Dramatic Poweroff Alert Skill")
    print("- ランダムな壮大な電源オフ予告をデスクトップ通知で表示")
    print(f"- メッセージ数: {len(DRAMATIC_MESSAGES)}")
    print("- OS対応: Windows, macOS, Linux (plyer/win10toast使用)")
    print("- 実際のシャットダウン等は一切行いません")

def parse_args():
    parser = argparse.ArgumentParser(description='Dramatic Poweroff Alert - OS電源オフの壮大な予告を通知で爆誕させる')
    subparsers = parser.add_subparsers(dest='command')

    parser_once = subparsers.add_parser('once', help='1回だけ通知を表示')
    parser_loop = subparsers.add_parser('loop', help='複数回通知を表示')
    parser_loop.add_argument('--count', type=int, default=5, help='通知回数')
    parser_loop.add_argument('--interval', type=int, default=60, help='通知間隔(秒)')
    subparsers.add_parser('list', help='メッセージ一覧表示')
    subparsers.add_parser('summary', help='Skill概要')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'once' or args.command is None:
        alert_once()
    elif args.command == 'loop':
        alert_loop(count=args.count, interval=args.interval)
    elif args.command == 'list':
        list_messages()
    elif args.command == 'summary':
        summary()
    else:
        print("不明なコマンドです。--help を参照してください。")

if __name__ == '__main__':
    main()
