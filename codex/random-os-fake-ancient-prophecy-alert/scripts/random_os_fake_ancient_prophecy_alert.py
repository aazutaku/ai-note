import sys
import random
import platform
import subprocess
import argparse
import os
from datetime import datetime

PROPHECY_TEMPLATES = [
    "{direction}の{place}に{phenomenon}現る",
    "{direction}の{place}に{legendary}眠る",
    "{ancient}が目覚めし時、{event}始まる",
    "{direction}の{place}に{shadow}動く",
    "{place}の{artifact}が{phenomenon}を呼ぶ",
    "{direction}の{log}に{storm}迫る",
    "{ancient}の{artifact}が{place}に現る",
    "{legendary}が{direction}の{place}に降臨す",
    "{place}の{artifact}が{event}を導く",
    "{direction}の{artifact}が{phenomenon}を告げる"
]

DIRECTIONS = ["北", "東", "南", "西"]
PLACES = ["リポジトリ", "コード砂漠", "依存関係", "ログ", "CI/CD", "ビルド", "デプロイ", "ブランチ"]
PHENOMENA = ["巨大バグの影", "エラーの嵐", "未踏のバグ", "謎の警告", "伝説のレビュアー", "古のCI/CD", "神秘のマージ", "闇のコンフリクト", "真のデプロイ", "不滅のテスト"]
LEGENDARIES = ["伝説のレビュアー", "古のCI/CD", "神秘のマージ", "不滅のテスト", "隠されたバグハンター"]
ANCIENTS = ["古のOS", "預言者", "伝承のエンジニア", "時の管理者"]
EVENTS = ["真のデプロイ", "不滅のテスト", "大いなるリファクタ", "混沌のマージ", "覚醒のリリース"]
ARTIFACTS = ["秘宝", "バグトークン", "レビュースタンプ", "エラーログ", "マージキー"]
SHADOWS = ["巨大バグの影", "未踏のバグ", "闇のコンフリクト"]
LOGS = ["ログ", "エラーログ", "ビルドログ"]
STORMS = ["エラーの嵐", "警告の雨", "バグの吹雪"]

HISTORY_FILE = os.path.expanduser("~/.random_os_fake_ancient_prophecy_history.log")


def generate_prophecy():
    template = random.choice(PROPHECY_TEMPLATES)
    prophecy = template.format(
        direction=random.choice(DIRECTIONS),
        place=random.choice(PLACES),
        phenomenon=random.choice(PHENOMENA),
        legendary=random.choice(LEGENDARIES),
        ancient=random.choice(ANCIENTS),
        event=random.choice(EVENTS),
        artifact=random.choice(ARTIFACTS),
        shadow=random.choice(SHADOWS),
        log=random.choice(LOGS),
        storm=random.choice(STORMS)
    )
    return prophecy


def notify_os(title, message):
    system = platform.system()
    try:
        if system == "Linux":
            # notify-send (libnotify-bin) 必須
            subprocess.run(["notify-send", title, message], check=True)
        elif system == "Darwin":
            # macOS: AppleScript
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Windows":
            # Windows 10+: powershell toast notification
            script = f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime];"
            script += f"$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);"
            script += f"$template.GetElementsByTagName('text')[0].AppendChild($template.CreateTextNode('{title}')) | Out-Null;"
            script += f"$template.GetElementsByTagName('text')[1].AppendChild($template.CreateTextNode('{message}')) | Out-Null;"
            script += f"$toast = [Windows.UI.Notifications.ToastNotification]::new($template);"
            script += f"[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('random-os-fake-ancient-prophecy-alert').Show($toast);"
            subprocess.run(["powershell", "-Command", script], check=True)
        else:
            print(f"[OS預言通知] {message}")
    except Exception as e:
        print(f"[通知失敗] {message} ({e})")


def log_history(prophecy):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {prophecy}\n")


def list_history(count=10):
    if not os.path.exists(HISTORY_FILE):
        print("履歴はありません。")
        return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines[-count:]:
        print(line.strip())


def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴はありません。")
        return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"預言通知履歴: {len(lines)}件")
    if lines:
        print(f"最新: {lines[-1].strip()}")


def main():
    parser = argparse.ArgumentParser(description="random-os-fake-ancient-prophecy-alert: OS預言通知スキル")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="預言通知を即時発動")
    parser_alert.add_argument("-n", "--number", type=int, default=1, help="連続発動回数")

    parser_list = subparsers.add_parser("list", help="預言通知履歴を表示")
    parser_list.add_argument("-c", "--count", type=int, default=10, help="表示件数")

    parser_summary = subparsers.add_parser("summary", help="預言通知履歴のサマリ表示")

    args = parser.parse_args()

    if args.command == "alert":
        for _ in range(args.number):
            prophecy = generate_prophecy()
            notify_os("OS預言通知", prophecy)
            log_history(prophecy)
    elif args.command == "list":
        list_history(args.count)
    elif args.command == "summary":
        summary_history()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
