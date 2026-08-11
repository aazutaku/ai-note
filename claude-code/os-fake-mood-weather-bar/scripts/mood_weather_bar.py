import sys
import os
import random
import argparse
import platform
import subprocess
from datetime import datetime

MOODS = [
    ("絶好調・晴れ", "今日は何をやっても順調！この勢いでタスクを消化しよう。"),
    ("やる気霧雨", "やる気が微妙に降り注ぐ午後。コーヒーで回復を！"),
    ("集中力台風接近中", "集中の嵐が迫る。タスクを片付けるチャンス！"),
    ("バグの嵐", "バグが吹き荒れる一日。冷静なデバッグを。"),
    ("仕様雪崩", "仕様変更の雪崩に注意。落ち着いて対応しよう。"),
    ("納期雷雨", "納期の雷が鳴り響く。計画的に進めよう。"),
    ("無気力曇り", "やる気が曇りがち。気分転換を挟もう。"),
    ("眠気霧", "眠気の霧が立ち込める。短い休憩を。"),
    ("インスピレーション虹", "アイデアの虹がかかる瞬間！メモを忘れずに。"),
    ("レビュー雹", "レビューの雹が降る。指摘も前向きに受け止めよう。")
]

LOG_PATH = os.path.expanduser("~/.claude_fake_mood_weather_bar.log")


def choose_mood():
    return random.choice(MOODS)


def format_output(mood, comment, timestamp=None):
    if not timestamp:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[気分天気バー] {timestamp}\n本日の気分天気：{mood}\nコメント：{comment}\n"


def show_notification(mood, comment):
    system = platform.system()
    title = "気分天気バー"
    message = f"{mood}\n{comment}"
    try:
        if system == "Darwin":
            # macOS: use osascript
            script = f'display notification "{comment}" with title "{mood}" subtitle "気分天気バー"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            # Linux: use notify-send
            subprocess.run(["notify-send", title, f"{mood}\n{comment}"], check=True)
        elif system == "Windows":
            # Windows: use Toast (via powershell)
            ps_script = f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null; " \
                        f"$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02); " \
                        f"$textNodes = $template.GetElementsByTagName('text'); " \
                        f"$textNodes.Item(0).AppendChild($template.CreateTextNode('{mood}')) > $null; " \
                        f"$textNodes.Item(1).AppendChild($template.CreateTextNode('{comment}')) > $null; " \
                        f"$toast = [Windows.UI.Notifications.ToastNotification]::new($template); " \
                        f"$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('気分天気バー'); " \
                        f"$notifier.Show($toast);"
            subprocess.run(["powershell", "-Command", ps_script], check=True)
        else:
            print("[WARN] 未対応OSです。通知は標準出力のみ行います。")
            print(f"{title}: {mood}\n{comment}")
    except Exception as e:
        print(f"[ERROR] 通知の表示に失敗しました: {e}")
        print(f"{title}: {mood}\n{comment}")


def log_mood(mood, comment, timestamp=None):
    out = format_output(mood, comment, timestamp)
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(out + "\n")
    except Exception as e:
        print(f"[ERROR] ログの保存に失敗: {e}")


def list_logs(limit=10):
    if not os.path.exists(LOG_PATH):
        print("ログファイルがありません。")
        return
    try:
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            lines = f.read().split("\n\n")
            lines = [l for l in lines if l.strip()]
            for entry in lines[-limit:]:
                print(entry)
                print("")
    except Exception as e:
        print(f"[ERROR] ログの読み込みに失敗: {e}")


def summary():
    if not os.path.exists(LOG_PATH):
        print("ログファイルがありません。")
        return
    counter = {}
    try:
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("本日の気分天気："):
                    mood = line.strip().split("：", 1)[1]
                    counter[mood] = counter.get(mood, 0) + 1
        print("=== 気分天気 出現回数集計 ===")
        for mood, cnt in sorted(counter.items(), key=lambda x: -x[1]):
            print(f"{mood}: {cnt}回")
    except Exception as e:
        print(f"[ERROR] 集計に失敗: {e}")


def main():
    parser = argparse.ArgumentParser(description="謎の気分天気バーを画面端に表示")
    subparsers = parser.add_subparsers(dest="command")

    show_parser = subparsers.add_parser("show", help="気分天気バーを表示")
    show_parser.add_argument("--log", action="store_true", help="表示内容をログに記録")

    list_parser = subparsers.add_parser("list", help="過去の気分天気バー出力を一覧表示")
    list_parser.add_argument("--limit", type=int, default=10, help="表示する件数")

    summary_parser = subparsers.add_parser("summary", help="気分天気の出現回数を集計")

    args = parser.parse_args()

    if args.command == "show":
        mood, comment = choose_mood()
        out = format_output(mood, comment)
        print(out)
        show_notification(mood, comment)
        if args.log:
            log_mood(mood, comment)
    elif args.command == "list":
        list_logs(args.limit)
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
