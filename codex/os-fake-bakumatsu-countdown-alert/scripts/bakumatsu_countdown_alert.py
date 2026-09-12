import sys
import argparse
import random
import time
import platform
import subprocess
from datetime import datetime

BAKUMATSU_ALERTS = [
    "緊急：システムはあと{mins}分で明治維新されます。",
    "本日は黒船再来。本能寺リブートまで残り{mins}分。",
    "徳川システム維持モード終了まで残り{mins}分。",
    "坂本龍馬のアップデート適用まで残り{mins}分。",
    "ペリー提督がポート{port}に接続を試みています。残り{mins}分で開国。",
    "新選組プロセスが暴走中。鎮圧カウントダウン：{mins}分。",
    "幕府ファイアウォール解除まで残り{mins}分。",
    "長州藩スクリプトが起動。システム再構築まで{mins}分。",
    "西郷隆盛がリブートを要求。再起動まで{mins}分。",
    "薩摩藩ネットワーク切断まで残り{mins}分。"
]

PORTS = [80, 443, 8080, 3000, 22, 1868, 1192]


def random_alert():
    mins = random.randint(3, 20)
    port = random.choice(PORTS)
    alert = random.choice(BAKUMATSU_ALERTS)
    return alert.format(mins=mins, port=port), mins


def show_terminal_alert(alert_text, mins):
    print("[OS幕末カウントダウン通知]")
    print(alert_text)
    print(f"カウントダウン開始：{mins:02d}:00")
    for i in range(mins, 0, -1):
        sys.stdout.write(f"\r残り {i:02d}:00 ...    ")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n[幕末カウントダウン終了] システムは無事維新されました（何も起きません）\n")


def show_os_notification(alert_text):
    sys_os = platform.system()
    title = "OS幕末カウントダウン通知"
    if sys_os == "Darwin":
        script = f'display notification "{alert_text}" with title "{title}"'
        subprocess.call(["osascript", "-e", script])
    elif sys_os == "Linux":
        subprocess.call(["notify-send", title, alert_text])
    elif sys_os == "Windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, alert_text, duration=10)
        except ImportError:
            print("[通知] win10toastが見つかりません。pip install win10toast でインストールしてください。")
    else:
        print(f"[通知未対応OS] {alert_text}")


def log_alert(alert_text, mins):
    logline = f"{datetime.now().isoformat()} | {alert_text} | {mins}分\n"
    with open("bakumatsu_alert.log", "a", encoding="utf-8") as f:
        f.write(logline)


def list_log():
    try:
        with open("bakumatsu_alert.log", "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines[-10:]:
            print(line.strip())
    except FileNotFoundError:
        print("まだ通知履歴がありません。")


def summary_log():
    try:
        with open("bakumatsu_alert.log", "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"通算通知回数: {len(lines)}")
        if lines:
            print(f"最新: {lines[-1].strip()}")
    except FileNotFoundError:
        print("まだ通知履歴がありません。")


def main():
    parser = argparse.ArgumentParser(description='OS幕末カウントダウン通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='幕末カウントダウン通知を発動')
    parser_alert.add_argument('--os', action='store_true', help='OSネイティブ通知も併用')
    parser_alert.add_argument('--log', action='store_true', help='通知履歴を記録')

    parser_list = subparsers.add_parser('list', help='通知履歴を最新10件表示')
    parser_summary = subparsers.add_parser('summary', help='通知履歴のサマリー表示')

    args = parser.parse_args()

    if args.command == 'alert':
        alert_text, mins = random_alert()
        show_terminal_alert(alert_text, mins)
        if args.os:
            show_os_notification(alert_text)
        if args.log:
            log_alert(alert_text, mins)
    elif args.command == 'list':
        list_log()
    elif args.command == 'summary':
        summary_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
