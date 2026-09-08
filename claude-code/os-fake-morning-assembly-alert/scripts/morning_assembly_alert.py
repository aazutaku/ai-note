import sys
import os
import random
import argparse
import datetime
import platform
import subprocess

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

SLOGANS = [
    "エラーは友達、焦らず冷静に！",
    "朝の一歩が未来を変える。",
    "バグゼロでリリース！",
    "レビューは愛、指摘は成長。",
    "全員で品質向上！",
    "OSは仲間、再起動も大事。",
    "今日も安全第一！",
    "コードに思いやりを。",
    "仕様書はよく読もう。",
    "困ったら助け合い。"
]

CHECKS = [
    "点呼開始: 1番から順に返事してください。",
    "本日の出席確認を行います。",
    "健康状態を自己申告してください。",
    "今日のやる気を10段階で宣言してください。",
    "新メンバーは挙手してください。"
]

EXERCISES = [
    "OS公式体操のご案内: 5分間ストレッチ推奨",
    "ディスプレイから目を離して深呼吸しましょう。",
    "手首・肩のストレッチを行いましょう。",
    "背筋を伸ばして座り直しましょう。",
    "軽く画面から離れて歩きましょう。"
]

TASKS = [
    "本日の作業目標: 『バグゼロでリリース！』",
    "本日の作業目標: 『PRレビューを3件！』",
    "本日の作業目標: 『テストカバレッジ90%超』",
    "本日の作業目標: 『ドキュメントを整備』",
    "本日の作業目標: 『定時退社』"
]

HISTORY_FILE = os.path.expanduser("~/.os_fake_morning_assembly_alert_history")


def already_shown_today():
    today = datetime.date.today().isoformat()
    if not os.path.exists(HISTORY_FILE):
        return False
    try:
        with open(HISTORY_FILE, 'r') as f:
            lines = f.readlines()
        return any(today in line for line in lines)
    except Exception:
        return False


def mark_shown_today():
    today = datetime.date.today().isoformat()
    try:
        with open(HISTORY_FILE, 'a') as f:
            f.write(f"{today}\n")
    except Exception:
        pass


def generate_message():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    slogan = random.choice(SLOGANS)
    check = random.choice(CHECKS)
    exercise = random.choice(EXERCISES)
    task = random.choice(TASKS)
    lines = [
        f"[OS朝礼通知] {now}",
        f"本日のスローガン: 「{slogan}」",
        check,
        exercise,
        task
    ]
    return '\n'.join(lines)


def show_notification(message):
    title = "OS朝礼通知"
    # Try desktop notification first
    if PLYER_AVAILABLE:
        try:
            notification.notify(
                title=title,
                message=message,
                timeout=8
            )
            return
        except Exception:
            pass
    # Fallback to platform-specific notification
    sysname = platform.system()
    try:
        if sysname == 'Darwin':  # macOS
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', script], check=False)
        elif sysname == 'Linux':
            subprocess.run(['notify-send', title, message], check=False)
        elif sysname == 'Windows':
            # Use toast notification via powershell
            ps_script = f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null; " \
                f"$template = [Windows.UI.Notifications.ToastTemplateType]::ToastText02; " \
                f"$xml = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent($template); " \
                f"$xml.GetElementsByTagName('text')[0].AppendChild($xml.CreateTextNode('{title}')) > $null; " \
                f"$xml.GetElementsByTagName('text')[1].AppendChild($xml.CreateTextNode('{message}')) > $null; " \
                f"$toast = [Windows.UI.Notifications.ToastNotification]::new($xml); " \
                f"[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('OS朝礼通知').Show($toast);"
            subprocess.run(['powershell', '-Command', ps_script], check=False)
    except Exception:
        pass
    # Always print to terminal as fallback
    print(message)


def main():
    parser = argparse.ArgumentParser(description='OS Fake Morning Assembly Alert')
    parser.add_argument('--force', action='store_true', help='強制的に通知を表示')
    parser.add_argument('--log', action='store_true', help='本日の通知履歴を表示')
    parser.add_argument('--reset', action='store_true', help='履歴をリセット')
    args = parser.parse_args()

    if args.reset:
        try:
            if os.path.exists(HISTORY_FILE):
                os.remove(HISTORY_FILE)
                print('履歴をリセットしました。')
            else:
                print('履歴ファイルは存在しません。')
        except Exception as e:
            print(f'履歴リセット失敗: {e}')
        return

    if args.log:
        if not os.path.exists(HISTORY_FILE):
            print('履歴はありません。')
            return
        with open(HISTORY_FILE, 'r') as f:
            print('過去の通知日:')
            for line in f:
                print(line.strip())
        return

    if not args.force and already_shown_today():
        return
    message = generate_message()
    show_notification(message)
    mark_shown_today()

if __name__ == '__main__':
    main()
