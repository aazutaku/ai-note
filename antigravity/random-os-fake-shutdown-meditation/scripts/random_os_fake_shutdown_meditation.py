import random
import time
import argparse
import sys
import threading
import platform

try:
    from plyer import notification
except ImportError:
    notification = None

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    tk = None

SHUTDOWN_MESSAGES = [
    "システムは5分間、無の境地に入ります。",
    "強制メンテ：心の再起動モード",
    "OS推奨：椅子で悟りを開いてください。",
    "謎のシャットダウン瞑想タイム発動。",
    "進捗バーで悟りを計測中...",
    "今こそ静寂を強制します。",
    "あなたの心を再起動しています...",
    "OSメンテナンス: 一時的に思考停止してください。",
    "瞑想モード：何も考えないでください。",
    "システム推奨：深呼吸タイム。"
]

PROGRESS_BAR_LENGTH = 30
MEDITATION_TIME_SEC = 5 * 60  # 5分


def send_notification(title, message):
    if notification:
        try:
            notification.notify(
                title=title,
                message=message,
                timeout=10
            )
        except Exception as e:
            print(f"[通知失敗]: {e}")
    else:
        print(f"[通知] {title}: {message}")


def random_message():
    return random.choice(SHUTDOWN_MESSAGES)


def print_progress_bar(percent):
    filled = int(PROGRESS_BAR_LENGTH * percent)
    bar = '=' * filled + ' ' * (PROGRESS_BAR_LENGTH - filled)
    sys.stdout.write(f"\r[進捗バー] 瞑想度: {int(percent*100)}% [{bar}]")
    sys.stdout.flush()


def meditation_timer(duration=MEDITATION_TIME_SEC):
    start = time.time()
    end = start + duration
    while time.time() < end:
        elapsed = time.time() - start
        percent = min(elapsed / duration, 1.0)
        print_progress_bar(percent)
        remain = int(end - time.time())
        mins, secs = divmod(remain, 60)
        sys.stdout.write(f"  [タイマー] 残り {mins:02d}:{secs:02d}")
        sys.stdout.flush()
        time.sleep(1)
    print_progress_bar(1.0)
    sys.stdout.write("  [タイマー] 完了!\n")
    sys.stdout.flush()


def gui_progress_bar(duration=MEDITATION_TIME_SEC):
    if not tk:
        print("tkinterが利用できません。CLI進捗バーを利用します。")
        meditation_timer(duration)
        return
    root = tk.Tk()
    root.title("謎のOSシャットダウン瞑想タイム")
    root.geometry("400x120+100+100")
    label = tk.Label(root, text=random_message(), font=("Meiryo", 12))
    label.pack(pady=10)
    progress = ttk.Progressbar(root, orient="horizontal", length=350, mode="determinate")
    progress.pack(pady=10)
    timer_label = tk.Label(root, text="", font=("Meiryo", 10))
    timer_label.pack()

    def update():
        elapsed = time.time() - start
        percent = min(elapsed / duration, 1.0)
        progress['value'] = percent * 100
        remain = int(duration - elapsed)
        mins, secs = divmod(max(remain,0), 60)
        timer_label.config(text=f"残り {mins:02d}:{secs:02d}")
        if elapsed < duration:
            root.after(1000, update)
        else:
            timer_label.config(text="瞑想タイム終了!")
            root.after(2000, root.destroy)
    start = time.time()
    update()
    root.mainloop()


def trigger_meditation(mode="auto", duration=MEDITATION_TIME_SEC):
    message = random_message()
    send_notification("謎のOSシャットダウン瞑想タイム", message)
    print(f"[通知] {message}")
    if mode == "gui":
        gui_progress_bar(duration)
    else:
        meditation_timer(duration)
    send_notification("瞑想タイム終了", "作業を再開できます。")
    print("[通知] 瞑想タイム終了。作業を再開できます。\n")


def main():
    parser = argparse.ArgumentParser(description="random-os-fake-shutdown-meditation: 謎のシャットダウン瞑想タイムを演出")
    parser.add_argument('--mode', choices=['auto', 'cli', 'gui'], default='auto', help='進捗バー表示モード')
    parser.add_argument('--duration', type=int, default=MEDITATION_TIME_SEC, help='瞑想タイム(秒)')
    parser.add_argument('--test', action='store_true', help='テスト通知のみ発行')
    parser.add_argument('--list-messages', action='store_true', help='全メッセージ一覧表示')
    args = parser.parse_args()

    if args.list_messages:
        print("-- メッセージ一覧 --")
        for msg in SHUTDOWN_MESSAGES:
            print(f"- {msg}")
        sys.exit(0)

    if args.test:
        send_notification("テスト通知", random_message())
        sys.exit(0)

    mode = args.mode
    if mode == 'auto':
        if tk:
            mode = 'gui'
        else:
            mode = 'cli'
    trigger_meditation(mode=mode, duration=args.duration)

if __name__ == '__main__':
    main()
