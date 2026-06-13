import sys
import os
import random
import argparse
import platform
import subprocess
import threading
import time

BGM_TITLES = [
    "なつかしのファミコン効果音",
    "宇宙戦艦発進テーマ",
    "朝礼のチャイム",
    "伝説のRPGセーブポイント",
    "早朝の商店街BGM",
    "昭和の駅ホームメロディ",
    "地下迷宮の環境音",
    "謎の工場アラーム",
    "温泉旅館の夕食ベル",
    "バブル期のCMジングル",
    "放課後のチャイム",
    "無人島サバイバルBGM",
    "都市伝説のBGM",
    "深夜のラジオジングル",
    "謎のゲームオーバー曲"
]

NOTIFY_LOCK = threading.Lock()
NOTIFIED_ONCE = False


def pick_random_bgm():
    return random.choice(BGM_TITLES)


def notify_mac(title, message):
    script = f'display notification "{message}" with title "{title}"'
    try:
        subprocess.run(["osascript", "-e", script], check=True)
    except Exception as e:
        print(f"[WARN] macOS通知失敗: {e}")


def notify_linux(title, message):
    try:
        subprocess.run(["notify-send", title, message], check=True)
    except Exception as e:
        print(f"[WARN] Linux通知失敗: {e}")


def notify_windows(title, message):
    try:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=5, threaded=True)
        # Wait for notification to disappear
        time.sleep(5)
    except ImportError:
        print("[WARN] win10toast未インストール。pip install win10toast で導入してください。")
    except Exception as e:
        print(f"[WARN] Windows通知失敗: {e}")


def send_os_notification(title, message):
    system = platform.system()
    if system == "Darwin":
        notify_mac(title, message)
    elif system == "Linux":
        notify_linux(title, message)
    elif system == "Windows":
        notify_windows(title, message)
    else:
        print(f"[INFO] OS通知未対応: {system}")


def show_random_bgm_notification():
    global NOTIFIED_ONCE
    with NOTIFY_LOCK:
        if NOTIFIED_ONCE:
            return False
        bgm = pick_random_bgm()
        title = "あなたの今日の作業BGM"
        send_os_notification(title, bgm)
        print(f"[OS通知] {title}: {bgm}")
        NOTIFIED_ONCE = True
        return True


def reset_notification():
    global NOTIFIED_ONCE
    with NOTIFY_LOCK:
        NOTIFIED_ONCE = False


def list_bgm_titles():
    print("--- BGMタイトル一覧 ---")
    for idx, title in enumerate(BGM_TITLES, 1):
        print(f"{idx}. {title}")


def summary():
    print("random-os-soundtrack-notifier: ターミナルやエディタ起動時に、完全ランダムな“今日の作業BGM”をOS通知で1回だけ表示します。通知はタイトルのみで、実際のBGM再生はありません。")


def main():
    parser = argparse.ArgumentParser(description="random-os-soundtrack-notifier: あなたの今日の作業BGMをランダム通知")
    subparsers = parser.add_subparsers(dest="command")

    parser_notify = subparsers.add_parser("notify", help="ランダムBGMをOS通知で1回表示")
    parser_reset = subparsers.add_parser("reset", help="通知済みフラグをリセット")
    parser_list = subparsers.add_parser("list", help="BGMタイトル一覧を表示")
    parser_summary = subparsers.add_parser("summary", help="Skillの概要を表示")

    args = parser.parse_args()

    if args.command == "notify" or args.command is None:
        show_random_bgm_notification()
    elif args.command == "reset":
        reset_notification()
        print("通知済みフラグをリセットしました。")
    elif args.command == "list":
        list_bgm_titles()
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
