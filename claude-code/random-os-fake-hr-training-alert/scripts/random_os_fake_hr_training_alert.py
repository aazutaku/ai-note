import random
import sys
import argparse
import platform
import subprocess
import time

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

# 人事研修通知メッセージのテンプレート
NOTIFICATION_TEMPLATES = [
    "緊急：本日{hour}時より“謎のパワポ芸入門”人事研修に強制参加してください。",
    "重要：OS公式“無限ビデオ視聴”研修が{minutes}分後に開始されます。",
    "今すぐ“謎マナー講座”を受講してください。",
    "本日中に“仮想空間での正しい座り方”研修を完了せよ。",
    "“OS人事主催：謎のチームビルディング”研修が間もなく始まります。",
    "至急：新設“無限自己紹介ループ”研修にログインしてください。",
    "【強制】“AI倫理と謎の社内ルール”講座が始まります。",
    "【通知】“OS流・意味不明なマナー”研修をただちに受講してください。",
    "【アラート】“仮想背景の選び方”研修が自動的に開始されます。",
    "【必須】“謎の1on1面談”の事前動画を全員視聴してください。"
]

PREFIXES = ["[ALERT]", "[NOTICE]", "[WARNING]", "[MANDATORY]", "[REMINDER]", "[INFO]", "[HR-ALERT]", "[OS-HR]"]

KEYWORDS = ["通知", "研修", "人事", "アラート", "alert", "training", "hr"]


def generate_random_message():
    template = random.choice(NOTIFICATION_TEMPLATES)
    hour = random.randint(9, 18)
    minutes = random.choice([5, 10, 15, 20, 30, 45, 60])
    msg = template.format(hour=hour, minutes=minutes)
    prefix = random.choice(PREFIXES)
    return f"{prefix} {msg}"


def send_os_notification(title, message):
    system = platform.system()
    if PLYER_AVAILABLE:
        try:
            notification.notify(title=title, message=message, timeout=8)
            return True
        except Exception:
            pass
    # fallback: OS別通知
    if system == "Darwin":  # macOS
        script = f'display notification "{message}" with title "{title}"'
        subprocess.call(["osascript", "-e", script])
        return True
    elif system == "Linux":
        try:
            subprocess.call(["notify-send", title, message])
            return True
        except Exception:
            pass
    elif system == "Windows":
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(title, message, duration=8)
            return True
        except Exception:
            pass
    return False


def print_terminal_notification(message):
    border = "=" * (len(message) + 4)
    print(f"\n{border}\n| {message} |\n{border}\n")


def trigger_notification():
    msg = generate_random_message()
    title = "OS人事研修アラート"
    sent = send_os_notification(title, msg)
    if not sent:
        print_terminal_notification(msg)
    else:
        print(f"[通知] {msg}")


def detect_keywords_in_args(args):
    joined = ' '.join(args).lower()
    for kw in KEYWORDS:
        if kw.lower() in joined:
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description="謎のOS人事研修アラート通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="ランダムな人事研修アラートを即時発動")
    parser_alert.add_argument("--count", type=int, default=1, help="連続発動回数")

    parser_demo = subparsers.add_parser("demo", help="複数回ランダム通知をデモ表示")
    parser_demo.add_argument("--interval", type=float, default=2.0, help="通知間隔(秒)")
    parser_demo.add_argument("--times", type=int, default=5, help="通知回数")

    parser.add_argument("args", nargs=argparse.REMAINDER, help="コマンドライン引数からキーワード検出時に発動")

    args = parser.parse_args()

    if args.command == "alert":
        for _ in range(args.count):
            trigger_notification()
            time.sleep(0.8)
        return
    elif args.command == "demo":
        for _ in range(args.times):
            trigger_notification()
            time.sleep(args.interval)
        return
    # 暗黙発動: 残り引数にキーワードが含まれていれば発動
    if args.args and detect_keywords_in_args(args.args):
        trigger_notification()
        return
    # 明示呼び出し無しの場合はヘルプ表示
    parser.print_help()

if __name__ == "__main__":
    main()
