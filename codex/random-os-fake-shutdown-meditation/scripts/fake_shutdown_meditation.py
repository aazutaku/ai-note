import sys
import time
import random
import threading
import argparse
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False
try:
    import tkinter as tk
    from tkinter import ttk
    TK_AVAILABLE = True
except ImportError:
    TK_AVAILABLE = False

MEDITATION_MESSAGES = [
    "システムは5分間、無の境地に入ります",
    "強制メンテ：心の再起動モード",
    "OS推奨：椅子で悟りを開いてください",
    "プロセス停止：思考のリセットを推奨します",
    "無限ループ検出：内面デバッグを開始します",
    "メモリ解放：雑念を消去中...",
    "ユーザー入力を遮断します。しばらく無になってください",
    "悟り進捗バーを初期化中...",
    "OSアップデート：心のパッチ適用中",
    "CPU温度上昇：沈静化モード突入"
]

PROGRESS_BAR_LENGTH = 30
MEDITATION_TIME_SEC = 300  # 5分


def send_notification(title, message):
    if PLYER_AVAILABLE:
        notification.notify(title=title, message=message, timeout=7)
    else:
        print(f"[通知] {title}: {message}")


def print_progress_bar(percent):
    bar_length = PROGRESS_BAR_LENGTH
    filled_length = int(bar_length * percent // 100)
    bar = '█' * filled_length + ' ' * (bar_length - filled_length)
    print(f"[進捗バー] 瞑想度: [{bar}] {percent}%")


def show_tk_progress_bar(duration_sec):
    if not TK_AVAILABLE:
        print("[警告] Tkinterがインストールされていないため、GUI進捗バーは表示できません。")
        return
    root = tk.Tk()
    root.title("OS Fake Shutdown Meditation")
    root.geometry("420x120+100+100")
    label = tk.Label(root, text=random.choice(MEDITATION_MESSAGES), font=("Meiryo", 12))
    label.pack(pady=10)
    progress = ttk.Progressbar(root, orient="horizontal", length=350, mode="determinate")
    progress.pack(pady=10)
    timer_label = tk.Label(root, text="", font=("Meiryo", 10))
    timer_label.pack(pady=5)
    
    def update_bar():
        for i in range(duration_sec + 1):
            percent = int(i * 100 / duration_sec)
            progress['value'] = percent
            remain = duration_sec - i
            m, s = divmod(remain, 60)
            timer_label.config(text=f"残り {m:02}:{s:02}")
            root.update()
            time.sleep(1)
        root.destroy()
    threading.Thread(target=update_bar).start()
    root.mainloop()


def meditation_sequence(duration_sec=300, gui=True, interval=30):
    # 1. 開始通知
    msg = random.choice(MEDITATION_MESSAGES)
    send_notification("Fake Shutdown Meditation", msg)
    print(f"[通知] {msg}")
    start = time.time()
    elapsed = 0
    percent = 0
    if gui and TK_AVAILABLE:
        threading.Thread(target=show_tk_progress_bar, args=(duration_sec,)).start()
    while elapsed < duration_sec:
        percent = int((elapsed / duration_sec) * 100)
        print_progress_bar(percent)
        if random.random() < 0.33:
            msg = random.choice(MEDITATION_MESSAGES)
            send_notification("Fake Shutdown Meditation", msg)
            print(f"[通知] {msg}")
        remain = duration_sec - elapsed
        m, s = divmod(remain, 60)
        print(f"[タイマー] 残り {m:02}:{s:02}")
        time.sleep(interval)
        elapsed = int(time.time() - start)
    print_progress_bar(100)
    send_notification("Fake Shutdown Meditation", "瞑想タイム終了！作業に戻れます。")
    print("[通知] 瞑想タイム終了！作業に戻れます。")


def list_messages():
    print("--- ランダム瞑想メッセージ一覧 ---")
    for msg in MEDITATION_MESSAGES:
        print(f"- {msg}")


def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Shutdown Meditation Skill")
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="瞑想タイムを発動する")
    parser_run.add_argument("--duration", type=int, default=300, help="瞑想タイム(秒)")
    parser_run.add_argument("--nogui", action="store_true", help="GUI進捗バーを表示しない")
    parser_run.add_argument("--interval", type=int, default=30, help="進捗・通知の更新間隔(秒)")

    parser_list = subparsers.add_parser("list", help="メッセージ一覧を表示")

    args = parser.parse_args()
    if args.command == "run":
        meditation_sequence(duration_sec=args.duration, gui=not args.nogui, interval=args.interval)
    elif args.command == "list":
        list_messages()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
