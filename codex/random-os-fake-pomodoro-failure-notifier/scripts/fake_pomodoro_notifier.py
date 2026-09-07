import sys
import os
import random
import time
import argparse
import platform
import subprocess
from typing import List

FAKE_FAILURE_MESSAGES = [
    "失敗：トマトが爆発しました。作業時間は跡形もありません。",
    "警告：集中力が鍋底にこびりつきました。スクレーパー推奨。",
    "注意：タイマーがピザに変身したため無効です。",
    "エラー：ポモドーロがケチャップになりました。再起動してください。",
    "失敗：休憩時間がトマトソースに吸収されました。",
    "警告：作業集中度がピクルスレベルに低下しました。",
    "注意：トマトタイマーがサルサに変化しました。",
    "失敗：時間泥棒がトマトを盗みました。",
    "警告：ポモドーロがパスタに巻き込まれました。",
    "注意：集中力がピザ生地の下に隠れました。",
    "失敗：タイマーがオーブンで焼かれすぎました。",
    "エラー：トマトの種がタイマーを詰まらせました。",
    "警告：休憩がトマトジュースに溶けました。",
    "注意：作業意欲がピザカッターでカットされました。",
    "失敗：トマト農家がストライキ中です。",
    "警告：集中力がピクルス瓶に閉じ込められました。",
    "注意：タイマーがトマト缶に変身しました。",
    "失敗：休憩時間がピザの箱に吸収されました。"
]

TRIGGER_KEYWORDS = [
    "ポモドーロ", "集中", "タイマー", "作業開始", "休憩", "25分", "タスク", "集中タイム", "start pomodoro", "focus", "break"
]

OS_TYPE = platform.system()

def send_notification(message: str):
    """Send a desktop notification or fallback to terminal output."""
    try:
        if OS_TYPE == "Darwin":
            # macOS
            script = f'display notification "{message}" with title "ポモドーロ失敗通知"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif OS_TYPE == "Linux":
            # Linux (notify-send)
            subprocess.run(["notify-send", "ポモドーロ失敗通知", message], check=True)
        elif OS_TYPE == "Windows":
            # Windows 10+ (toast via PowerShell)
            powershell = (
                f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
                f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent(0);'
                f'$textNodes = $template.GetElementsByTagName("text");'
                f'$textNodes.Item(0).AppendChild($template.CreateTextNode("ポモドーロ失敗通知")) > $null;'
                f'$textNodes.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null;'
                f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
                f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("PomodoroFail");'
                f'$notifier.Show($toast);'
            )
            subprocess.run(["powershell", "-Command", powershell], check=True)
        else:
            print(f"[通知] {message}")
    except Exception as e:
        print(f"[通知] {message} (通知エラー: {e})")

def random_failure_message() -> str:
    return random.choice(FAKE_FAILURE_MESSAGES)

def parse_args():
    parser = argparse.ArgumentParser(description="Fake Pomodoro Failure Notifier")
    subparsers = parser.add_subparsers(dest="command")

    parser_start = subparsers.add_parser("start", help="ポモドーロタイマー開始 (フェイク通知発動)")
    parser_start.add_argument("--duration", type=int, default=25, help="作業時間(分)")
    parser_start.add_argument("--break", type=int, default=5, help="休憩時間(分)")

    parser_notify = subparsers.add_parser("notify", help="即座にフェイク通知を表示")
    parser_notify.add_argument("--count", type=int, default=1, help="通知回数")

    parser_list = subparsers.add_parser("list", help="通知メッセージ一覧表示")

    return parser.parse_args()

def run_pomodoro(duration: int, break_duration: int):
    print(f"[INFO] ポモドーロタイマー開始: {duration}分 作業 → {break_duration}分 休憩 (フェイク通知あり)")
    send_notification(random_failure_message())
    for i in range(duration):
        time.sleep(0.1)  # 実際は1分だがデモ用に0.1秒
    send_notification(random_failure_message())
    print(f"[INFO] 作業終了。休憩タイム: {break_duration}分")
    for i in range(break_duration):
        time.sleep(0.1)
    send_notification(random_failure_message())
    print(f"[INFO] ポモドーロサイクル完了 (全てフェイク通知)")

def notify_random(count: int):
    for _ in range(count):
        msg = random_failure_message()
        send_notification(msg)
        print(f"[通知] {msg}")
        time.sleep(0.5)

def list_messages():
    print("--- フェイク通知メッセージ一覧 ---")
    for i, msg in enumerate(FAKE_FAILURE_MESSAGES):
        print(f"{i+1:02d}: {msg}")

def semantic_trigger(text: str) -> bool:
    """Check if the input text contains trigger keywords."""
    text = text.lower()
    return any(kw.lower() in text for kw in TRIGGER_KEYWORDS)

def main():
    args = parse_args()
    if args.command == "start":
        run_pomodoro(args.duration, args.break)
    elif args.command == "notify":
        notify_random(args.count)
    elif args.command == "list":
        list_messages()
    else:
        print("Usage: python fake_pomodoro_notifier.py [start|notify|list] [options]")
        print("例: python fake_pomodoro_notifier.py start --duration 25 --break 5")
        print("例: python fake_pomodoro_notifier.py notify --count 3")
        print("例: python fake_pomodoro_notifier.py list")

if __name__ == "__main__":
    main()
