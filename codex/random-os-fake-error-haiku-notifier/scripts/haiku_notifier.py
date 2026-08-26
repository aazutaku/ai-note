import sys
import argparse
import random
import platform
import subprocess
import time

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

HAIKU_LIST = [
    "バグの香や\n春まだ遠き\nデバッグ道",
    "夜のバグ\n静けさ破る\n警告音",
    "エラー出て\nまた一歩ずつ\n成長す",
    "ifの闇\nelseの迷い\n朝が来る",
    "落ちるコード\n桜のごとし\n散り急ぐ",
    "例外に\n心惑いて\nリファクタ",
    "デバッグ道\n夜更けに響く\nバグの声",
    "未定義の\n変数を追って\n春遠し",
    "文法エラー\n気付けば朝日\n窓の外",
    "Stack trace\n流れる川の\nごとくなり"
]

DEFAULT_TITLE = "謎のOS公式・エラー俳句"


def pick_random_haiku():
    return random.choice(HAIKU_LIST)


def send_notification(title, message, timeout=5):
    """
    Cross-platform notification.
    Prefer plyer, fallback to platform-specific methods.
    """
    if PLYER_AVAILABLE:
        notification.notify(title=title, message=message, timeout=timeout)
    else:
        system = platform.system()
        if system == "Darwin":
            # macOS: use osascript
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script])
        elif system == "Linux":
            # Linux: use notify-send
            subprocess.run(["notify-send", title, message])
        elif system == "Windows":
            # Windows fallback (no plyer): use toast via powershell
            ps_script = f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null; " \
                        f"$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02); " \
                        f"$template.GetElementsByTagName('text')[0].AppendChild($template.CreateTextNode('{title}')) > $null; " \
                        f"$template.GetElementsByTagName('text')[1].AppendChild($template.CreateTextNode('{message}')) > $null; " \
                        f"$toast = [Windows.UI.Notifications.ToastNotification]::new($template); " \
                        f"[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Python').Show($toast); "
            subprocess.Popen(["powershell", "-Command", ps_script], shell=True)
        else:
            print(f"[通知] {title}\n{message}")


def detect_error_lines(lines):
    error_keywords = ["Traceback", "Exception", "error:", "Error:", "エラー", "例外"]
    for line in lines:
        for kw in error_keywords:
            if kw in line:
                return True
    return False


def haiku_notify(args):
    haiku = pick_random_haiku()
    send_notification(DEFAULT_TITLE, haiku)
    print(f"[俳句通知] {haiku}")


def monitor_stdin(args):
    """Monitor stdin for error output and notify on error."""
    buffer = []
    try:
        for line in sys.stdin:
            buffer.append(line.rstrip())
            sys.stdout.write(line)
            sys.stdout.flush()
            if detect_error_lines([line]):
                haiku = pick_random_haiku()
                send_notification(DEFAULT_TITLE, haiku)
                print(f"[俳句通知] {haiku}")
                time.sleep(0.5)
    except KeyboardInterrupt:
        pass


def list_haiku(args):
    for i, h in enumerate(HAIKU_LIST, 1):
        print(f"{i}.\n{h}\n")


def main():
    parser = argparse.ArgumentParser(description="エラー発生時に謎の俳句をOS通知するSkill")
    subparsers = parser.add_subparsers(dest="command")

    parser_notify = subparsers.add_parser("notify", help="ランダム俳句を即時通知")
    parser_notify.set_defaults(func=haiku_notify)

    parser_monitor = subparsers.add_parser("monitor", help="標準入力を監視しエラー検知で俳句通知")
    parser_monitor.set_defaults(func=monitor_stdin)

    parser_list = subparsers.add_parser("list", help="内蔵俳句一覧を表示")
    parser_list.set_defaults(func=list_haiku)

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        sys.exit(1)
    args.func(args)

if __name__ == "__main__":
    main()
