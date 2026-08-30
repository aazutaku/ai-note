import sys
import os
import platform
import random
import subprocess
import argparse
import time
from datetime import datetime

BOSS_NAMES = [
    "メモリ喰らい魔王",
    "ディスク断捨離伯爵",
    "プロセス暴走忍者",
    "残業タイムリーパー",
    "バグ召喚師",
    "CPU炎上王",
    "ネットワーク監視鬼",
    "アップデート妖精",
    "マウス封印将軍",
    "スクリーンセーバー幻術師"
]

BOSS_COMMANDS = [
    "今すぐ椅子から立ち上がり、3回回転せよ！",
    "ファイル整理を怠る者に明日はない！",
    "10秒間、目を閉じて深呼吸！",
    "本日は残業魔王が降臨中。覚悟せよ！",
    "ストレッチしない者はバグに呪われる！",
    "コーヒーを淹れてリセットせよ！",
    "目を画面から離して遠くを見よ！",
    "1分間、何もせず静止せよ！",
    "机の上を片付けよ！",
    "OSの再起動は不要だ、今は耐えよ！"
]

BOSS_TITLES = [
    "謎のOSボス",
    "ボス",
    "新たな刺客",
    "警告",
    "任務",
    "緊急指令",
    "挑戦状",
    "乱入者"
]

HISTORY_FILE = os.path.expanduser("~/.random_os_mystery_boss_pop.log")


def select_boss():
    name = random.choice(BOSS_NAMES)
    command = random.choice(BOSS_COMMANDS)
    title = random.choice(BOSS_TITLES)
    return title, name, command


def notify(title, message):
    system = platform.system()
    try:
        if system == "Darwin":  # macOS
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            subprocess.run(["notify-send", title, message], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=8)
            except ImportError:
                # Fallback: powershell
                ps_cmd = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
                ps_cmd += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
                ps_cmd += f'$template.GetElementsByTagName("text")[0].AppendChild($template.CreateTextNode("{title}")) > $null;'
                ps_cmd += f'$template.GetElementsByTagName("text")[1].AppendChild($template.CreateTextNode("{message}")) > $null;'
                ps_cmd += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
                ps_cmd += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("random-os-mystery-boss-pop");'
                ps_cmd += f'$notifier.Show($toast)'
                subprocess.run(["powershell", "-Command", ps_cmd], check=True)
        else:
            print(f"[通知] {title}: {message}")
    except Exception as e:
        print(f"通知エラー: {e}")
        print(f"[通知] {title}: {message}")


def log_history(title, name, command):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] {title}『{name}』: {command}\n"
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(line)


def show_boss():
    title, name, command = select_boss()
    msg = f"{name}が出現！\n{command}"
    notify(title, msg)
    log_history(title, name, command)
    print(f"[通知] {title}「{name}」\n命令: {command}")


def list_history(limit=10):
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()[-limit:]
        print("--- 最近のボス履歴 ---")
        for line in lines:
            print(line.strip())


def summary():
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    bosses = {}
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        for line in f:
            for name in BOSS_NAMES:
                if name in line:
                    bosses[name] = bosses.get(name, 0) + 1
    print("--- ボス出現回数 ---")
    for name, count in sorted(bosses.items(), key=lambda x: -x[1]):
        print(f"{name}: {count}回")


def parse_args():
    parser = argparse.ArgumentParser(description="random-os-mystery-boss-pop: 謎のOSボスがランダムに出現し、命令や警告を通知します。")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("pop", help="ボスを1体ランダム出現させる")
    subparsers.add_parser("list", help="直近のボス履歴を表示")
    subparsers.add_parser("summary", help="ボス出現回数のサマリーを表示")

    parser.add_argument("--repeat", type=int, default=1, help="連続でボスを出現させる回数")
    parser.add_argument("--interval", type=int, default=0, help="複数回出現時の間隔（秒）")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "pop" or args.command is None:
        for i in range(args.repeat):
            show_boss()
            if args.repeat > 1 and i < args.repeat - 1:
                time.sleep(args.interval)
    elif args.command == "list":
        list_history()
    elif args.command == "summary":
        summary()
    else:
        print("コマンドが不正です。--help を参照してください。")

if __name__ == "__main__":
    main()
