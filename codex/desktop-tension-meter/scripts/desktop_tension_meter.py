import sys
import time
import random
import threading
import argparse
from datetime import datetime
try:
    import tkinter as tk
    import psutil
    import keyboard
except ImportError as e:
    print(f"必要なモジュールが見つかりません: {e}\n pip install psutil keyboard")
    sys.exit(1)

TENSION_LABELS = [
    (0, 30, "平常心"),
    (31, 60, "やや焦り"),
    (61, 80, "高まる緊張"),
    (81, 100, "極度緊張")
]

LOG_FILE = "tension_meter.log"

class TypingSpeedMonitor:
    def __init__(self):
        self.count = 0
        self.last_reset = time.time()
        self.lock = threading.Lock()
        keyboard.on_press(self._on_key)

    def _on_key(self, e):
        with self.lock:
            self.count += 1

    def get_speed(self):
        now = time.time()
        with self.lock:
            elapsed = now - self.last_reset
            speed = self.count / elapsed * 60 if elapsed > 0 else 0
            self.count = 0
            self.last_reset = now
        return speed

class DesktopTensionMeter:
    def __init__(self, interval_min=300, interval_max=600, duration=6):
        self.interval_min = interval_min
        self.interval_max = interval_max
        self.duration = duration
        self._stop = threading.Event()
        self.typing_monitor = TypingSpeedMonitor()

    def _get_commit_count(self):
        # git log --since=1.hour --pretty=oneline | wc -l
        try:
            import subprocess
            out = subprocess.check_output([
                'git', 'log', '--since=1.hour', '--pretty=oneline'
            ], stderr=subprocess.DEVNULL)
            return len(out.decode().splitlines())
        except Exception:
            return random.randint(0, 5)

    def _calc_tension(self):
        base = random.randint(0, 100)
        typing_speed = min(int(self.typing_monitor.get_speed()), 100)
        commit_count = self._get_commit_count()
        # 根拠になりそうでならない計算
        tension = int(0.4 * base + 0.3 * typing_speed + 0.3 * commit_count * 10)
        tension = max(0, min(100, tension))
        for low, high, label in TENSION_LABELS:
            if low <= tension <= high:
                return tension, label
        return tension, "未知"

    def _show_teletext(self, tension, label):
        root = tk.Tk()
        root.overrideredirect(True)
        root.attributes('-topmost', True)
        root.attributes('-alpha', 0.85)
        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()
        width, height = 420, 60
        x = screen_w - width - 20
        y = screen_h - height - 60
        root.geometry(f"{width}x{height}+{x}+{y}")
        frame = tk.Frame(root, bg='#222', bd=2)
        frame.pack(fill=tk.BOTH, expand=True)
        msg = f"緊張度: {label} (推定値: {tension})"
        label_widget = tk.Label(frame, text=msg, font=("Meiryo", 20, "bold"), fg="#fff", bg="#222")
        label_widget.pack(expand=True)
        def close():
            root.destroy()
        root.after(self.duration * 1000, close)
        root.mainloop()

    def _log(self, tension, label):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] 緊張度: {label} (推定値: {tension})\n")

    def run(self):
        print("desktop-tension-meter: テロップ表示を開始します。Ctrl+Cで終了。")
        try:
            while not self._stop.is_set():
                tension, label = self._calc_tension()
                self._log(tension, label)
                t = threading.Thread(target=self._show_teletext, args=(tension, label))
                t.daemon = True
                t.start()
                interval = random.randint(self.interval_min, self.interval_max)
                for _ in range(interval):
                    if self._stop.is_set():
                        break
                    time.sleep(1)
        except KeyboardInterrupt:
            print("\n終了します。")
            self._stop.set()

    def stop(self):
        self._stop.set()

    def show_log(self, lines=10):
        try:
            with open(LOG_FILE, encoding="utf-8") as f:
                logs = f.readlines()[-lines:]
            for line in logs:
                print(line.strip())
        except Exception:
            print("ログが見つかりません。")

    def summary(self):
        try:
            with open(LOG_FILE, encoding="utf-8") as f:
                logs = f.readlines()
            counts = {}
            for line in logs:
                for _, _, label in TENSION_LABELS:
                    if label in line:
                        counts[label] = counts.get(label, 0) + 1
            print("緊張度ラベル別出現回数:")
            for label in [l for _, _, l in TENSION_LABELS]:
                print(f"{label}: {counts.get(label, 0)}回")
        except Exception:
            print("ログが見つかりません。")

def main():
    parser = argparse.ArgumentParser(description="desktop-tension-meter: 意味のない緊張度テロップをデスクトップに表示")
    sub = parser.add_subparsers(dest="command")
    run_p = sub.add_parser("run", help="テロップ表示を開始")
    run_p.add_argument("--min", type=int, default=300, help="最短間隔(秒)")
    run_p.add_argument("--max", type=int, default=600, help="最長間隔(秒)")
    run_p.add_argument("--duration", type=int, default=6, help="テロップ表示秒数")
    log_p = sub.add_parser("log", help="直近の緊張度ログを表示")
    log_p.add_argument("--lines", type=int, default=10, help="表示行数")
    sub.add_parser("summary", help="緊張度ラベル別出現回数を集計")
    args = parser.parse_args()
    meter = DesktopTensionMeter()
    if args.command == "run":
        meter = DesktopTensionMeter(args.min, args.max, args.duration)
        meter.run()
    elif args.command == "log":
        meter.show_log(args.lines)
    elif args.command == "summary":
        meter.summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
