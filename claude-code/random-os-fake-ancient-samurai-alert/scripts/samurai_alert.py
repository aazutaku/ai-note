import sys
import argparse
import random
import platform
import subprocess
from typing import List

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

SAMURAI_MESSAGES = [
    "拙者、Altキーの抜刀訓練状況を監視しておる。",
    "油断大敵、マウスの居合切りに注意せよ。",
    "今宵もCtrl+Cの奥義を磨くべし。",
    "タスク切り替え、まるで手裏剣のごとし。",
    "心静かに、Enterキーの一撃を放つべし。",
    "ファイル保存、まるで巻物の如し。怠るべからず。",
    "スクリーンショットは、現代の写し絵なり。",
    "CapsLockの暴発、油断の証なり。",
    "コピペの術、侮るなかれ。",
    "Alt+Tabの極意、会得せよ。",
    "ウィンドウ整列、刀の如く正確に。",
    "Slackの通知、敵か味方か見極めよ。",
    "マウスカーソルの動き、燕返しの如し。",
    "パスワードは秘伝の巻物、漏らすべからず。",
    "アップデートの催促、黒船来航の如し。",
    "バッテリー残量、命の灯火。油断するな。",
    "プリンタの不調、妖怪の仕業か。",
    "Wi-Fi断絶、孤島に取り残されし侍の心境なり。",
    "ログイン失敗、門前払いの屈辱。",
    "再起動は、心機一転の儀式なり。"
]

NOTIFY_TITLE = "OS侍のお達し"


def pick_random_message(messages: List[str]) -> str:
    return random.choice(messages)


def notify_desktop(message: str):
    system = platform.system()
    if PLYER_AVAILABLE:
        notification.notify(
            title=NOTIFY_TITLE,
            message=message,
            app_name="SamuraiAlert",
            timeout=6
        )
    else:
        # Fallback: Try native notification commands
        try:
            if system == "Darwin":  # macOS
                script = f'display notification "{message}" with title "{NOTIFY_TITLE}"'
                subprocess.run(["osascript", "-e", script], check=True)
            elif system == "Linux":
                subprocess.run([
                    "notify-send", NOTIFY_TITLE, message
                ], check=True)
            elif system == "Windows":
                # Windows fallback: print to terminal
                print(f"[{NOTIFY_TITLE}]\n{message}\n")
            else:
                print(f"[{NOTIFY_TITLE}]\n{message}\n")
        except Exception:
            print(f"[{NOTIFY_TITLE}]\n{message}\n")


def notify_terminal(message: str):
    border = "=" * (len(NOTIFY_TITLE) + 8)
    print(f"\n{border}\n[{NOTIFY_TITLE}]\n{message}\n{border}\n")


def list_messages():
    for i, msg in enumerate(SAMURAI_MESSAGES, 1):
        print(f"{i:2d}: {msg}")


def main():
    parser = argparse.ArgumentParser(
        description="謎のOS侍からの時代錯誤な通知をランダムで発動するスクリプト。"
    )
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    parser_alert = subparsers.add_parser("alert", help="ランダムな侍通知を表示")
    parser_alert.add_argument(
        "--terminal", action="store_true", help="デスクトップ通知ではなくターミナル出力で表示"
    )
    parser_alert.add_argument(
        "--count", type=int, default=1, help="通知回数（デフォルト1回）"
    )

    parser_list = subparsers.add_parser("list", help="全通知メッセージ一覧を表示")

    args = parser.parse_args()

    if args.command == "alert":
        for _ in range(args.count):
            msg = pick_random_message(SAMURAI_MESSAGES)
            if args.terminal:
                notify_terminal(msg)
            else:
                notify_desktop(msg)
    elif args.command == "list":
        list_messages()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
