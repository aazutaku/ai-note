import os
import sys
import time
import random
import argparse
import platform
import json
import subprocess
from datetime import datetime, timedelta

ACHIEVEMENTS = [
    {
        "title": "Ctrl+C連打名人",
        "detail": "10秒間に7回のCtrl+Cを検出しました"
    },
    {
        "title": "5分間マウス未使用",
        "detail": "キーボード操作のみで作業を継続しました"
    },
    {
        "title": "このコマンド誰も使ってない王",
        "detail": "直近30日間で初めて'cat /dev/null'を実行"
    },
    {
        "title": "謎のディレクトリ発見者",
        "detail": "/tmp/unknown_dir に初アクセス"
    },
    {
        "title": "ls -la連打職人",
        "detail": "1分間に15回ls -la"
    },
    {
        "title": "タイピング音速超え",
        "detail": "1分間に500文字以上タイプ"
    },
    {
        "title": "無音作業ゾーン",
        "detail": "30分間一切の通知なしで作業"
    },
    {
        "title": "空白コマンド実行者",
        "detail": "何も入力せずEnterを5回押下"
    },
    {
        "title": "意味不明な引数王",
        "detail": "コマンドに存在しない引数を3回指定"
    },
    {
        "title": "謎のファイル生成者",
        "detail": "/dev/nullに10回リダイレクト"
    }
]

HISTORY_FILE = os.path.expanduser("~/.random_os_fake_achievements.json")

# OS通知APIのラッパー
class Notifier:
    def __init__(self):
        self.system = platform.system()

    def notify(self, title, message):
        if self.system == "Linux":
            self._notify_linux(title, message)
        elif self.system == "Darwin":
            self._notify_mac(title, message)
        elif self.system == "Windows":
            self._notify_windows(title, message)
        else:
            self._notify_terminal(title, message)

    def _notify_linux(self, title, message):
        try:
            subprocess.run(["notify-send", title, message], check=True)
        except Exception:
            self._notify_terminal(title, message)

    def _notify_mac(self, title, message):
        script = f'display notification "{message}" with title "{title}"'
        try:
            subprocess.run(["osascript", "-e", script], check=True)
        except Exception:
            self._notify_terminal(title, message)

    def _notify_windows(self, title, message):
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(title, message, duration=5)
        except Exception:
            self._notify_terminal(title, message)

    def _notify_terminal(self, title, message):
        print(f"[Achievement Unlocked]\n称号: {title}\n詳細: {message}\n")

# 実績履歴の保存・読み込み
class AchievementHistory:
    def __init__(self, path=HISTORY_FILE):
        self.path = path
        self.history = self._load()

    def _load(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def add(self, achievement):
        record = {
            "title": achievement["title"],
            "detail": achievement["detail"],
            "timestamp": datetime.now().isoformat()
        }
        self.history.append(record)
        self._save()

    def _save(self):
        try:
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(self.history, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def list(self, limit=10):
        return self.history[-limit:]

    def summary(self):
        counts = {}
        for rec in self.history:
            counts[rec["title"]] = counts.get(rec["title"], 0) + 1
        return counts

# 実績通知メイン処理
class AchievementNotifier:
    def __init__(self, interval_min=60, interval_max=600):
        self.notifier = Notifier()
        self.history = AchievementHistory()
        self.interval_min = interval_min
        self.interval_max = interval_max
        self.last_notify = datetime.now() - timedelta(seconds=interval_max)

    def random_achievement(self):
        return random.choice(ACHIEVEMENTS)

    def notify_random(self):
        ach = self.random_achievement()
        self.notifier.notify(ach["title"], ach["detail"])
        self.history.add(ach)
        self.last_notify = datetime.now()

    def run(self, duration=1800):
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < duration:
            now = datetime.now()
            wait = random.randint(self.interval_min, self.interval_max)
            time.sleep(wait)
            self.notify_random()

    def log(self):
        self.notify_random()

    def list(self, limit=10):
        for rec in self.history.list(limit):
            print(f"[{rec['timestamp']}] {rec['title']} - {rec['detail']}")

    def summary(self):
        counts = self.history.summary()
        for title, cnt in counts.items():
            print(f"{title}: {cnt}回")


def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Mystery Achievement Notifier")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_run = subparsers.add_parser("run", help="バックグラウンドでランダム通知を実行")
    parser_run.add_argument("--duration", type=int, default=1800, help="実行時間(秒)")
    parser_run.add_argument("--interval-min", type=int, default=60, help="通知間隔の最小秒数")
    parser_run.add_argument("--interval-max", type=int, default=600, help="通知間隔の最大秒数")

    parser_log = subparsers.add_parser("log", help="即時で1件通知")
    parser_list = subparsers.add_parser("list", help="履歴を表示")
    parser_list.add_argument("--limit", type=int, default=10, help="表示件数")
    parser_summary = subparsers.add_parser("summary", help="実績別集計")

    args = parser.parse_args()
    notifier = AchievementNotifier(
        interval_min=getattr(args, "interval_min", 60),
        interval_max=getattr(args, "interval_max", 600)
    )

    if args.command == "run":
        notifier.run(duration=args.duration)
    elif args.command == "log":
        notifier.log()
    elif args.command == "list":
        notifier.list(limit=args.limit)
    elif args.command == "summary":
        notifier.summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
