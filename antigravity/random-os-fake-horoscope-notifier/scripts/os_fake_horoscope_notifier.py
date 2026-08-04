import os
import sys
import random
import platform
import subprocess
import datetime
from pathlib import Path

HOROSCOPE_MESSAGES = [
    {
        "fortune": "コードレビュー運が最高潮！",
        "lucky": "git diff",
        "advice": "設計書の再確認を忘れずに。"
    },
    {
        "fortune": "バグ回避率が20%上昇中。",
        "lucky": "vim",
        "advice": "コミット前に深呼吸。"
    },
    {
        "fortune": "仕様変更星が逆行中。",
        "lucky": "ls",
        "advice": "READMEをよく読もう。"
    },
    {
        "fortune": "新機能実装運が上昇！",
        "lucky": "touch",
        "advice": "小まめな保存を忘れずに。"
    },
    {
        "fortune": "デバッグ運が好調。",
        "lucky": "pdb",
        "advice": "エラー文をよく観察しよう。"
    },
    {
        "fortune": "レビュー依頼のタイミング良し。",
        "lucky": "pull request",
        "advice": "感謝を伝えると吉。"
    },
    {
        "fortune": "CI/CD運が安定中。",
        "lucky": "docker-compose",
        "advice": "キャッシュクリアを忘れずに。"
    },
    {
        "fortune": "仕様質問運が上昇傾向。",
        "lucky": "slack",
        "advice": "疑問は早めに相談。"
    }
]

NOTIFY_HISTORY_PATH = str(Path.home() / ".os_horoscope_notified")


def already_notified_today():
    try:
        if not os.path.exists(NOTIFY_HISTORY_PATH):
            return False
        with open(NOTIFY_HISTORY_PATH, "r") as f:
            last_date = f.read().strip()
        today = datetime.date.today().isoformat()
        return last_date == today
    except Exception:
        return False

def mark_notified():
    try:
        with open(NOTIFY_HISTORY_PATH, "w") as f:
            today = datetime.date.today().isoformat()
            f.write(today)
    except Exception:
        pass

def generate_horoscope():
    msg = random.choice(HOROSCOPE_MESSAGES)
    lines = [
        f"[OS Horoscope] 今日の運勢: {msg['fortune']}",
        f"ラッキーコマンド: {msg['lucky']}",
        f"アドバイス: {msg['advice']}"
    ]
    return "\n".join(lines)

def send_desktop_notification(title, message):
    system = platform.system()
    try:
        if system == "Linux":
            subprocess.run([
                "notify-send", title, message
            ], check=True)
            return True
        elif system == "Darwin":
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run([
                "osascript", "-e", script
            ], check=True)
            return True
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=6)
                return True
            except ImportError:
                # Fallback to terminal output
                return False
        else:
            return False
    except Exception:
        return False

def print_terminal_notification(message):
    print("\n" + message + "\n")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="OS Fake Horoscope Notifier")
    parser.add_argument("--force", action="store_true", help="強制的に通知を表示する（1日1回制限を無視）")
    args = parser.parse_args()

    if not args.force and already_notified_today():
        return
    msg = generate_horoscope()
    title = "OS Horoscope"
    notified = send_desktop_notification(title, msg)
    if not notified:
        print_terminal_notification(msg)
    mark_notified()

if __name__ == "__main__":
    main()
