import sys
import random
import platform
import subprocess
import argparse
import threading
import time

COFFEE_ALERTS = [
    "重大: コーヒーカップが満杯です。溢れる前に一時的なコーヒー断ちを推奨します。",
    "警告: システムのカフェイン値が限界を超えました。再起動を検討してください。",
    "注意: コーヒー残量が異常に多いです。作業効率低下の恐れあり。",
    "エラー: 仮想マグカップがオーバーフローしました。",
    "情報: コーヒーインジェクションが検出されました。ご注意ください。",
    "警告: コーヒーフィルタのキャッシュが破損しています。",
    "重大: デジタルカフェイン障害が発生しました。冷静な対応を。",
    "注意: OSのカフェインレベルがしきい値を超えました。",
    "情報: コーヒーAPIから過剰なリクエストを検出。",
    "エラー: コーヒー・バッファが溢れました。"
]

OS_TYPE = platform.system()


def send_notification(message):
    if OS_TYPE == "Linux":
        try:
            subprocess.run([
                "notify-send", "[OS通知]", message
            ], check=True)
        except Exception as e:
            print(f"notify-send失敗: {e}")
    elif OS_TYPE == "Darwin":
        try:
            script = f'display notification "{message}" with title "OS通知"'
            subprocess.run([
                "osascript", "-e", script
            ], check=True)
        except Exception as e:
            print(f"osascript失敗: {e}")
    elif OS_TYPE == "Windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("OS通知", message, duration=5)
        except ImportError:
            print("win10toastがインストールされていません。pip install win10toast で導入してください。")
        except Exception as e:
            print(f"Windows通知失敗: {e}")
    else:
        print(f"[OS通知] {message}")


def random_alert():
    message = random.choice(COFFEE_ALERTS)
    send_notification(message)
    return message


def list_alerts():
    for i, msg in enumerate(COFFEE_ALERTS):
        print(f"{i+1}: {msg}")


def summary():
    print("=== コーヒーあふれ警告 Skill 概要 ===")
    print(f"対応OS: Linux, macOS, Windows")
    print(f"登録メッセージ数: {len(COFFEE_ALERTS)}")
    print("通知例:")
    for msg in random.sample(COFFEE_ALERTS, min(3, len(COFFEE_ALERTS))):
        print(f"  - {msg}")


def periodic_alert(interval=1800, count=3):
    print(f"{count}回、{interval}秒ごとにコーヒー警告を発火します。Ctrl+Cで中断可。")
    for i in range(count):
        msg = random_alert()
        print(f"[{i+1}/{count}] {msg}")
        if i < count - 1:
            try:
                time.sleep(interval)
            except KeyboardInterrupt:
                print("中断されました。")
                break


def main():
    parser = argparse.ArgumentParser(description="OSコーヒーあふれ警告 Skill")
    subparsers = parser.add_subparsers(dest="command")

    trigger_parser = subparsers.add_parser("trigger", help="ランダムなコーヒー警告を即時発火")
    list_parser = subparsers.add_parser("list", help="登録済み警告メッセージ一覧表示")
    summary_parser = subparsers.add_parser("summary", help="Skill概要とサンプルを表示")
    periodic_parser = subparsers.add_parser("periodic", help="定期的に警告を発火")
    periodic_parser.add_argument("--interval", type=int, default=1800, help="通知間隔(秒)")
    periodic_parser.add_argument("--count", type=int, default=3, help="通知回数")

    args = parser.parse_args()
    if args.command == "trigger":
        msg = random_alert()
        print(f"[OS通知] {msg}")
    elif args.command == "list":
        list_alerts()
    elif args.command == "summary":
        summary()
    elif args.command == "periodic":
        periodic_alert(args.interval, args.count)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
