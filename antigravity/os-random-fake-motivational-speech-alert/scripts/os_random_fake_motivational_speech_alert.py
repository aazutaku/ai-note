import sys
import random
import argparse
import platform
import subprocess
from typing import List

MOTIVATIONAL_MESSAGES = [
    "あなたのキーボードの叩き方に、未来への情熱を感じます。",
    "今こそ、コード界の伝説になるときです。",
    "そのコミットは、宇宙規模の進化を生み出します。",
    "あなたのデバッグ魂が、世界を救う。",
    "1行のコードが、歴史を変える。",
    "OSはあなたの努力を見守っています。",
    "そのpushは、銀河を照らす光です。",
    "エラーに立ち向かうあなたに、拍手を送ります。",
    "あなたのアルゴリズムが、時代を変える。",
    "今こそ、コードで世界を救うヒーローに。",
    "その一歩が、OSの未来を切り開く。",
    "あなたのcommitが、次世代のOSを作る。",
    "コードの海を泳ぐあなたに、OSからエールを。",
    "そのビルドは、伝説の始まりです。",
    "OSはあなたの挑戦を全力で応援します。",
    "そのテストは、宇宙の安定を支えます。",
    "あなたのリファクタが、OSの美しさを高めます。",
    "バグを倒すあなたに、OSからメダルを。",
    "そのレビューが、未来の標準を作ります。",
    "OSはあなたの進化を信じています。"
]

NOTIFICATION_TITLE = "OS公式通知"


def pick_random_message() -> str:
    return random.choice(MOTIVATIONAL_MESSAGES)


def send_notification(message: str, title: str = NOTIFICATION_TITLE) -> None:
    system = platform.system()
    try:
        if system == "Linux":
            subprocess.run(["notify-send", title, message], check=True)
        elif system == "Darwin":  # macOS
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=5, threaded=True)
            except ImportError:
                print(f"[{title}] {message}")
                print("win10toastが見つかりません。'pip install win10toast'でインストールしてください。")
        else:
            print(f"[{title}] {message}")
    except Exception as e:
        print(f"[{title}] {message}")
        print(f"通知の送信に失敗しました: {e}")


def log_message(logfile: str, message: str) -> None:
    try:
        with open(logfile, 'a', encoding='utf-8') as f:
            f.write(f"[{NOTIFICATION_TITLE}] {message}\n")
    except Exception as e:
        print(f"ログファイルへの書き込みに失敗しました: {e}")


def list_log(logfile: str, count: int = 10) -> None:
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[-count:]:
                print(line.strip())
    except FileNotFoundError:
        print("ログファイルが見つかりません。まだ通知が記録されていません。")
    except Exception as e:
        print(f"ログファイルの読み込みに失敗しました: {e}")


def summary_log(logfile: str) -> None:
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print(f"通知履歴: {len(lines)}件")
        unique_msgs = set(line.strip() for line in lines)
        print(f"ユニークなメッセージ: {len(unique_msgs)}件")
    except FileNotFoundError:
        print("ログファイルが見つかりません。")
    except Exception as e:
        print(f"ログファイルの集計に失敗しました: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="OS公式風やる気爆上げスピーチ通知スクリプト"
    )
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="ランダム通知を発火")
    parser_alert.add_argument("--log", type=str, default=None, help="通知内容を指定ファイルに記録")

    parser_list = subparsers.add_parser("list", help="通知ログを表示")
    parser_list.add_argument("--log", type=str, required=True, help="通知ログファイルパス")
    parser_list.add_argument("--count", type=int, default=10, help="表示件数")

    parser_summary = subparsers.add_parser("summary", help="通知ログの集計")
    parser_summary.add_argument("--log", type=str, required=True, help="通知ログファイルパス")

    args = parser.parse_args()

    if args.command == "alert":
        msg = pick_random_message()
        send_notification(msg)
        if args.log:
            log_message(args.log, msg)
    elif args.command == "list":
        list_log(args.log, args.count)
    elif args.command == "summary":
        summary_log(args.log)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
