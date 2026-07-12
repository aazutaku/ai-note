import sys
import os
import random
import argparse
import platform
from datetime import datetime

try:
    if platform.system() == 'Darwin':
        import subprocess
    elif platform.system() == 'Windows':
        from plyer import notification
    elif platform.system() == 'Linux':
        import notify2
except ImportError:
    pass

QUOTES = [
    "本日もバグに感謝せよ",
    "進捗ゼロ、それもまた進化",
    "コードは寝かせて美味しくなる",
    "仕様書は読むものではなく感じるもの",
    "エラーは成長の証",
    "OSの気分で挙動が変わる、それが真理",
    "デバッグは心の旅路",
    "動けば正義、止まれば哲学",
    "リファクタリングは永遠の未完成",
    "ログは未来への手紙",
    "バグは愛、修正は義務",
    "今日の進捗は明日の肥やし",
    "無駄な最適化は人生のスパイス",
    "テストコードは裏切らない",
    "コミットメッセージは詩である"
]

HISTORY_FILE = os.path.join(os.path.expanduser("~"), ".random_os_motivational_history.txt")


def show_notification(message):
    system = platform.system()
    if system == 'Darwin':
        try:
            subprocess.run([
                'osascript', '-e', f'display notification "{message}" with title "OS格言"'
            ], check=True)
        except Exception as e:
            print(f"[ERROR] 通知失敗: {e}")
    elif system == 'Windows':
        try:
            notification.notify(
                title='OS格言',
                message=message,
                app_name='Random OS Motivational Quote Notifier',
                timeout=6
            )
        except Exception as e:
            print(f"[ERROR] 通知失敗: {e}")
    elif system == 'Linux':
        try:
            notify2.init('Random OS Motivational Quote Notifier')
            n = notify2.Notification('OS格言', message)
            n.set_timeout(6000)
            n.show()
        except Exception as e:
            print(f"[ERROR] 通知失敗: {e}")
    else:
        print(f"[通知] OS格言: {message}")


def get_random_quote():
    return random.choice(QUOTES)


def save_history(quote):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
            f.write(f"[{now}] {quote}\n")
    except Exception as e:
        print(f"[ERROR] 履歴保存失敗: {e}")


def list_quotes():
    for idx, q in enumerate(QUOTES, 1):
        print(f"{idx}. {q}")


def show_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if not lines:
                print("履歴がありません。")
                return
            for line in lines[-20:]:
                print(line.strip())
    except Exception as e:
        print(f"[ERROR] 履歴読み込み失敗: {e}")


def clear_history():
    try:
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
            print("履歴を削除しました。")
        else:
            print("履歴ファイルがありません。")
    except Exception as e:
        print(f"[ERROR] 履歴削除失敗: {e}")


def notify():
    quote = get_random_quote()
    show_notification(quote)
    save_history(quote)
    print(f"[通知] OS格言: {quote}")


def main():
    parser = argparse.ArgumentParser(description='Random OS Motivational Quote Notifier')
    subparsers = parser.add_subparsers(dest='command')

    notify_parser = subparsers.add_parser('notify', help='ランダムなOS格言を通知')
    list_parser = subparsers.add_parser('list', help='格言一覧を表示')
    history_parser = subparsers.add_parser('history', help='通知履歴を表示')
    clear_parser = subparsers.add_parser('clear', help='通知履歴を削除')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == 'notify':
        notify()
    elif args.command == 'list':
        list_quotes()
    elif args.command == 'history':
        show_history()
    elif args.command == 'clear':
        clear_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
