import random
import time
import sys
import argparse
import threading
import platform
import subprocess

BAKUMATSU_EVENTS = [
    ("緊急：システムはあと{minutes}分で明治維新されます", "明治維新"),
    ("本日は黒船再来。本能寺リブートまで残り{minutes}分", "黒船再来"),
    ("土佐藩アップデートまで残り{minutes}分", "土佐藩アップデート"),
    ("会津藩セーフモード突入まで残り{minutes}分", "会津藩セーフモード"),
    ("西郷どんプロセスが終了するまで{minutes}分", "西郷プロセス終了"),
    ("坂本龍馬のバージョンアップまで残り{minutes}分", "龍馬バージョンアップ"),
    ("江戸幕府シャットダウンまで{minutes}分", "江戸幕府シャットダウン"),
    ("薩長連合ネットワーク再構築まで{minutes}分", "薩長連合再構築"),
    ("新選組アップデート適用まで{minutes}分", "新選組アップデート"),
    ("ペリー警告：黒船リセットまで{minutes}分", "ペリー警告")
]

TERMINAL_PREFIX = "[幕末カウントダウン]"


def random_event():
    event_tpl, event_name = random.choice(BAKUMATSU_EVENTS)
    minutes = random.randint(5, 30)
    message = event_tpl.format(minutes=minutes)
    return message, event_name, minutes


def notify_desktop(title, message):
    system = platform.system()
    try:
        if system == "Darwin":  # macOS
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "{title}"'
            ])
        elif system == "Linux":
            subprocess.run([
                "notify-send", title, message
            ])
        elif system == "Windows":
            # Use Toast notification via powershell
            ps_script = f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;"
            ps_script += f"$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);"
            ps_script += f"$template.GetElementsByTagName('text')[0].AppendChild($template.CreateTextNode('{title}')) > $null;"
            ps_script += f"$template.GetElementsByTagName('text')[1].AppendChild($template.CreateTextNode('{message}')) > $null;"
            ps_script += f"$toast = [Windows.UI.Notifications.ToastNotification]::new($template);"
            ps_script += f"$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('os-fake-bakumatsu-countdown-alert');"
            ps_script += f"$notifier.Show($toast);"
            subprocess.run(["powershell", "-Command", ps_script], shell=True)
        else:
            print(f"{TERMINAL_PREFIX} {title}: {message}")
    except Exception as e:
        print(f"{TERMINAL_PREFIX} 通知失敗: {e}")


def print_terminal_alert(message, minutes):
    print(f"{TERMINAL_PREFIX} {message}")
    print(f"残り時間: {minutes:02d}:00\n")


def countdown(minutes, event_name, desktop=False):
    total_seconds = minutes * 60
    for remaining in range(total_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        sys.stdout.write(f"\r{TERMINAL_PREFIX} {event_name} 残り時間: {mins:02d}:{secs:02d}")
        sys.stdout.flush()
        time.sleep(1)
    print(f"\n{TERMINAL_PREFIX} {event_name} タイムアップ！\n")
    if desktop:
        notify_desktop("幕末カウントダウン終了", f"{event_name}が完了しました")


def list_events():
    print("利用可能な幕末カウントダウンイベント:")
    for idx, (tpl, name) in enumerate(BAKUMATSU_EVENTS, 1):
        print(f"{idx}. {name}")


def summary():
    print("このスクリプトは、幕末日本をテーマにしたフェイクカウントダウンアラートをCLIまたはデスクトップ通知で表示します。実害ゼロ、歴史パロディ専用です。")


def main():
    parser = argparse.ArgumentParser(description="幕末カウントダウンアラート (os-fake-bakumatsu-countdown-alert)")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    parser_log = subparsers.add_parser("log", help="ランダムな幕末アラートを表示")
    parser_log.add_argument("--desktop", action="store_true", help="デスクトップ通知も表示")
    parser_log.add_argument("--countdown", action="store_true", help="カウントダウン演出も実行")
    parser_log.add_argument("--minutes", type=int, default=None, help="カウントダウン分数を指定")

    parser_list = subparsers.add_parser("list", help="利用可能なイベント一覧を表示")
    parser_summary = subparsers.add_parser("summary", help="概要を表示")

    args = parser.parse_args()

    if args.command == "log":
        message, event_name, minutes = random_event()
        if args.minutes is not None and 1 <= args.minutes <= 60:
            minutes = args.minutes
            message = message.split("まで残り")[0] + f"まで残り{minutes}分"
        print_terminal_alert(message, minutes)
        if args.desktop:
            notify_desktop("幕末カウントダウン", message)
        if args.countdown:
            countdown(minutes, event_name, desktop=args.desktop)
    elif args.command == "list":
        list_events()
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
