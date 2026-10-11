import sys
import random
import time
import argparse
import platform
import subprocess
from typing import List

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

MESSAGES = [
    "[OS公式通知] 本日、あなたの集中力ゲージが限界に到達しました。コーヒーブレイクが自動発動されます。",
    "[OS推奨] 重要：OS推奨のリフレッシュタイム到来。3分間の休憩を推奨します。",
    "[警告] ユーザーの生産性が閾値を超過しました。強制的にコーヒーブレイクを開始します。",
    "[システム] コーヒーブレイクプロトコル v2.3.4 が実行されました。復帰までお待ちください。",
    "[OS通知] あなたの作業効率が低下しています。今すぐコーヒーを淹れましょう。",
    "[重要] システムAIによる分析結果：あなたの脳波が休憩を要求しています。",
    "[OSアラート] 定期リフレッシュタイム：コーヒーまたはお茶の準備を推奨。",
    "[管理者通知] 作業集中度が最大値に達しました。強制的に休憩モードへ移行します。",
    "[OSメッセージ] ユーザーの生産性維持のため、コーヒーブレイクを自動挿入しました。",
    "[システム警告] 長時間無休憩が検出されました。OS推奨のリフレッシュを実施してください。"
]

HINTS = [
    "コーヒーが苦手な場合はお茶や水でもOKです。",
    "短いストレッチや深呼吸もおすすめです。",
    "画面から目を離して遠くを見てみましょう。",
    "休憩後は作業効率が向上することが科学的に証明されています。"
]

LOG_FILE = None  # ログ保存機能はデフォルト無効


def send_desktop_notification(title: str, message: str):
    if PLYER_AVAILABLE:
        notification.notify(
            title=title,
            message=message,
            app_name="OS Coffee Break",
            timeout=10
        )
    else:
        system = platform.system()
        if system == "Darwin":  # macOS
            subprocess.call([
                "osascript", "-e",
                f'display notification "{message}" with title "{title}"'
            ])
        elif system == "Linux":
            subprocess.call([
                "notify-send", title, message])
        elif system == "Windows":
            # Windows用の簡易通知（コマンドプロンプト）
            print(f"{title}: {message}")
        else:
            print(f"{title}: {message}")


def print_terminal_alert(message: str, hint: str = None):
    print("\n=== OS公式コーヒーブレイク通知 ===")
    print(message)
    if hint:
        print(f"ヒント: {hint}")
    print("===============================\n")


def random_wait(min_sec=60, max_sec=600):
    wait_time = random.randint(min_sec, max_sec)
    time.sleep(wait_time)


def trigger_alert():
    message = random.choice(MESSAGES)
    hint = random.choice(HINTS) if random.random() < 0.5 else None
    send_desktop_notification("OSコーヒーブレイク通知", message)
    print_terminal_alert(message, hint)


def run_random_mode(args):
    try:
        while True:
            wait = random.randint(args.min_interval, args.max_interval)
            time.sleep(wait)
            trigger_alert()
            if args.once:
                break
    except KeyboardInterrupt:
        print("\n[INFO] コーヒーブレイク通知スクリプトを終了します。")


def run_once(args):
    trigger_alert()


def list_messages(args):
    print("利用可能な通知メッセージ一覧:")
    for msg in MESSAGES:
        print("-", msg)


def main():
    parser = argparse.ArgumentParser(
        description="謎のOS公式コーヒーブレイク通知をランダムに発動するスクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_random = subparsers.add_parser(
        "random", help="ランダムな間隔で通知を発動 (デフォルト)")
    parser_random.add_argument("--min-interval", type=int, default=120,
                              help="通知間隔の最小秒数 (デフォルト: 120)")
    parser_random.add_argument("--max-interval", type=int, default=900,
                              help="通知間隔の最大秒数 (デフォルト: 900)")
    parser_random.add_argument("--once", action="store_true",
                              help="1回だけ通知して終了")

    parser_once = subparsers.add_parser(
        "once", help="1回だけ即座に通知を発動")

    parser_list = subparsers.add_parser(
        "list", help="通知メッセージ一覧を表示")

    args = parser.parse_args()

    if args.command == "once":
        run_once(args)
    elif args.command == "list":
        list_messages(args)
    else:
        run_random_mode(args)

if __name__ == '__main__':
    main()
