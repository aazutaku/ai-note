import sys
import argparse
import random
import threading
import time
import platform
try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    tk = None

MOOD_WEATHER_LIST = [
    "絶好調・晴れ",
    "やる気霧雨",
    "集中力台風接近中",
    "バグの嵐",
    "仕様雪崩",
    "納期雷警報",
    "バグの小春日和",
    "会議前線通過中",
    "レビュー曇り時々晴れ",
    "進捗微風",
    "仕様熱波",
    "タスク猛吹雪",
    "やる気微塵",
    "集中力高気圧",
    "デバッグ寒波",
    "コミット晴れのち雷",
    "バグの霧",
    "仕様の大雨",
    "テスト嵐",
    "納期の虹"
]

REFRESH_INTERVALS = [120, 180, 240, 300]  # 秒

class MoodWeatherBar:
    def __init__(self, interval=None):
        self.current_mood = None
        self.next_interval = interval or random.choice(REFRESH_INTERVALS)
        self.root = None
        self.label = None
        self.running = True
        self.platform = platform.system()
        self._lock = threading.Lock()

    def random_mood(self):
        return random.choice(MOOD_WEATHER_LIST)

    def update_mood(self):
        with self._lock:
            self.current_mood = self.random_mood()
            self.next_interval = random.choice(REFRESH_INTERVALS)
            if self.label:
                self.label.config(text=self._format_text())

    def _format_text(self):
        return f"[OS風・謎の気分天気バー]\n現在の気分天気: {self.current_mood}\n（次回更新まで: {self.next_interval//60}分）"

    def _tkinter_loop(self):
        self.root = tk.Tk()
        self.root.title("OS風・謎の気分天気バー")
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)
        self.root.geometry(f"400x90+{self.root.winfo_screenwidth()-420}+30")
        self.label = tk.Label(self.root, text=self._format_text(), font=("Meiryo", 13), justify="left", anchor="w")
        self.label.pack(fill="both", expand=True, padx=10, pady=10)
        threading.Thread(target=self._auto_refresh, daemon=True).start()
        self.root.protocol("WM_DELETE_WINDOW", self.stop)
        self.root.mainloop()

    def _auto_refresh(self):
        while self.running:
            time.sleep(self.next_interval)
            if not self.running:
                break
            self.update_mood()

    def _windows_notify(self):
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            while self.running:
                mood = self.random_mood()
                interval = random.choice(REFRESH_INTERVALS)
                toaster.show_toast(
                    "OS風・謎の気分天気バー",
                    f"現在の気分天気: {mood}\n（次回更新まで: {interval//60}分）",
                    duration=10,
                    threaded=True
                )
                for _ in range(interval):
                    if not self.running:
                        break
                    time.sleep(1)
        except ImportError:
            print("win10toastがインストールされていません。\n pip install win10toast で導入してください。")

    def start(self):
        self.current_mood = self.random_mood()
        if self.platform == "Windows":
            self._windows_notify()
        elif tk:
            self._tkinter_loop()
        else:
            print(self._format_text())
            print("tkinterが利用できません。CLI出力のみ対応します。")
            while self.running:
                time.sleep(self.next_interval)
                self.update_mood()
                print(self._format_text())

    def stop(self):
        self.running = False
        if self.root:
            self.root.destroy()


def list_moods():
    print("--- 気分天気ワード一覧 ---")
    for m in MOOD_WEATHER_LIST:
        print(f"- {m}")

def main():
    parser = argparse.ArgumentParser(description="謎の気分天気バーを表示します")
    subparsers = parser.add_subparsers(dest="command")

    parser_show = subparsers.add_parser("show", help="気分天気バーを表示")
    parser_show.add_argument("--interval", type=int, help="更新間隔（秒）")

    parser_list = subparsers.add_parser("list", help="気分天気ワード一覧を表示")

    parser_once = subparsers.add_parser("once", help="1回だけランダム気分天気を表示")

    args = parser.parse_args()

    if args.command == "show":
        bar = MoodWeatherBar(interval=args.interval)
        try:
            bar.start()
        except KeyboardInterrupt:
            bar.stop()
    elif args.command == "list":
        list_moods()
    elif args.command == "once":
        mood = random.choice(MOOD_WEATHER_LIST)
        interval = random.choice(REFRESH_INTERVALS)
        print(f"[OS風・謎の気分天気バー]\n現在の気分天気: {mood}\n（次回更新まで: {interval//60}分）")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
