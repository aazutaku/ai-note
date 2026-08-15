import sys
import time
import random
import argparse
import platform
import subprocess
from threading import Thread

try:
    from tqdm import tqdm
except ImportError:
    tqdm = None

# メッセージ候補
NOTIFICATIONS = [
    "システムは5分間、無の境地に入ります。",
    "強制メンテ：心の再起動モード",
    "OS推奨：椅子で悟りを開いてください",
    "謎のシャットダウン瞑想タイム発動中…",
    "進捗バーで悟り度を計測中",
    "静寂を強制する謎タイマーが現れました",
    "メモリ最適化中：思考を一時停止してください",
    "CPU負荷低減：心のリセットを推奨",
    "OSからのお知らせ：深呼吸してみましょう",
    "仮想再起動：現実世界でリフレッシュしてください"
]

END_MESSAGES = [
    "悟りタイムが完了しました。作業に戻れます。",
    "再起動完了。集中モードに復帰します。",
    "無の境地から帰還しました。",
    "OS瞑想モード終了。引き続き作業をどうぞ。"
]

# OS通知を送る
def send_notification(title, message):
    system = platform.system()
    try:
        if system == "Darwin":  # macOS
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "{title}"'
            ], check=True)
        elif system == "Linux":
            subprocess.run([
                "notify-send", title, message
            ], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=5)
            except ImportError:
                print(f"[通知] {title}: {message}")
        else:
            print(f"[通知] {title}: {message}")
    except Exception as e:
        print(f"[通知] {title}: {message} (通知失敗: {e})")

# 進捗バーを表示
def meditation_progress_bar(duration_sec):
    steps = 10
    interval = duration_sec / steps
    if tqdm:
        for i in tqdm(range(steps), desc="瞑想度", ncols=60):
            time.sleep(interval)
    else:
        for i in range(steps):
            bar = "[" + "=" * (i+1) + " " * (steps - i - 1) + "]"
            percent = int((i+1) / steps * 100)
            print(f"[進捗バー] 瞑想度: {bar} {percent}%")
            time.sleep(interval)

# タイマー表示
def meditation_timer(duration_sec):
    for remaining in range(duration_sec, 0, -1):
        mins, secs = divmod(remaining, 60)
        time_str = f"{mins:02}:{secs:02}"
        print(f"[タイマー] 残り {time_str}", end="\r", flush=True)
        time.sleep(1)
    print(" " * 40, end="\r")

# メイン瞑想イベント
def run_meditation_event(duration=300):
    notif = random.choice(NOTIFICATIONS)
    send_notification("謎のOS瞑想タイム", notif)
    print(f"[通知] {notif}")
    # 進捗バーとタイマーを並列実行
    bar_thread = Thread(target=meditation_progress_bar, args=(duration,))
    timer_thread = Thread(target=meditation_timer, args=(duration,))
    bar_thread.start()
    timer_thread.start()
    bar_thread.join()
    timer_thread.join()
    end_msg = random.choice(END_MESSAGES)
    send_notification("瞑想終了", end_msg)
    print(f"\n[終了通知] {end_msg}")

# コマンドライン引数処理
def parse_args():
    parser = argparse.ArgumentParser(
        description="謎のOSシャットダウン瞑想タイムをランダム発動するスクリプト"
    )
    parser.add_argument(
        "run",
        nargs="?",
        default=None,
        help="瞑想タイムを即時発動"
    )
    parser.add_argument(
        "--duration", "-d",
        type=int,
        default=300,
        help="瞑想タイムの秒数 (デフォルト: 300秒)"
    )
    parser.add_argument(
        "list",
        nargs="?",
        default=None,
        help="通知メッセージ一覧を表示"
    )
    return parser.parse_args()

# メイン関数
def main():
    args = parse_args()
    if args.run == "run":
        run_meditation_event(duration=args.duration)
    elif args.list == "list":
        print("--- 通知メッセージ候補 ---")
        for m in NOTIFICATIONS:
            print(f"- {m}")
        print("--- 終了メッセージ候補 ---")
        for m in END_MESSAGES:
            print(f"- {m}")
    else:
        # 暗黙発動用: stdinからキーワード検知
        print("[INFO] キーワード監視モード。Ctrl+Cで終了。")
        keywords = ["shutdown", "meditation", "再起動", "無の境地", "悟り"]
        try:
            while True:
                line = sys.stdin.readline()
                if not line:
                    break
                if any(k in line for k in keywords):
                    if random.random() < 0.5:  # 50%の確率で発動
                        run_meditation_event(duration=180)
        except KeyboardInterrupt:
            print("\n[INFO] 終了します。")

if __name__ == "__main__":
    main()
