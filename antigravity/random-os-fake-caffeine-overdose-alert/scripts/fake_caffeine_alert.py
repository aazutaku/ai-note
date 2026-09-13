import sys
import random
import time
import argparse
import platform
import subprocess

try:
    from plyer import notification
    HAS_PLYER = True
except ImportError:
    HAS_PLYER = False

ALERT_MESSAGES = [
    "重大: あなたのカフェイン血中濃度が“徹夜エンジニア”レベルに到達しました。",
    "警告: コーヒーカップが自動でリフィルされました。水分補給を推奨します。",
    "System Notice: 今すぐストレッチと水分補給を行ってください。",
    "Fake Alert: あなたの作業スピードがカフェイン規定値を超えました。",
    "OSより: カフェイン摂取量が上限に達しました。仮眠を推奨します。",
    "警告: あなたのキーボードからカフェイン臭が検出されました。",
    "重大: エナジードリンクが自動で注文されました。",
    "System Alert: あなたのコーヒー消費量がOSの安全基準を超えました。",
    "警告: 眠気検出センサーが作動しました。今すぐ深呼吸してください。",
    "Fake Notice: あなたの集中力がカフェイン依存域に突入しました。"
]

TITLE_OPTIONS = [
    "[OS ALERT]",
    "[WARNING]",
    "[System Notice]",
    "[Fake Alert]",
    "[OSより]"
]

LOG_FILE = None  # ログやファイル保存は行わない設計


def random_alert_message():
    title = random.choice(TITLE_OPTIONS)
    message = random.choice(ALERT_MESSAGES)
    return title, message


def show_desktop_notification(title, message):
    if HAS_PLYER:
        notification.notify(
            title=title,
            message=message,
            app_name="FakeCaffeineAlert",
            timeout=7
        )
        return True
    else:
        # OSごとのフォールバック
        system = platform.system()
        if system == "Darwin":  # macOS
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script])
            return True
        elif system == "Linux":
            try:
                subprocess.run(["notify-send", title, message])
                return True
            except Exception:
                pass
        elif system == "Windows":
            # Windows 10+ の場合
            try:
                import win10toast
                toaster = win10toast.ToastNotifier()
                toaster.show_toast(title, message, duration=7)
                return True
            except Exception:
                pass
    return False


def print_terminal_alert(title, message):
    print(f"{title} {message}")


def fire_alert():
    title, message = random_alert_message()
    shown = show_desktop_notification(title, message)
    if not shown:
        print_terminal_alert(title, message)


def run_random_mode(min_interval=30, max_interval=180, count=5):
    for i in range(count):
        wait_time = random.randint(min_interval, max_interval)
        time.sleep(wait_time)
        fire_alert()


def main():
    parser = argparse.ArgumentParser(description="Fake Caffeine Overdose Alert Skill")
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='今すぐフェイク警告を1回表示')
    parser_random = subparsers.add_parser('random', help='ランダムな間隔で複数回フェイク警告を表示')
    parser_random.add_argument('--min', type=int, default=30, help='最小インターバル(秒)')
    parser_random.add_argument('--max', type=int, default=180, help='最大インターバル(秒)')
    parser_random.add_argument('--count', type=int, default=5, help='警告回数')

    parser_list = subparsers.add_parser('list', help='全フェイク警告メッセージを一覧表示')
    parser_summary = subparsers.add_parser('summary', help='Skill概要を表示')

    args = parser.parse_args()

    if args.command == 'alert':
        fire_alert()
    elif args.command == 'random':
        run_random_mode(args.min, args.max, args.count)
    elif args.command == 'list':
        for t in TITLE_OPTIONS:
            for m in ALERT_MESSAGES:
                print(f"{t} {m}")
    elif args.command == 'summary':
        print("このSkillは、完全にフェイクなカフェイン過剰摂取警告をランダムなタイミングで表示します。通知内容は毎回異なり、作業空間に一瞬のカオスをもたらします。")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
