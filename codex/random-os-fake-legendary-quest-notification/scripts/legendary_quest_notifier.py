import sys
import os
import random
import time
import argparse
import platform

try:
    import notify2  # Linux
except ImportError:
    notify2 = None
try:
    from win10toast import ToastNotifier  # Windows
except ImportError:
    ToastNotifier = None

QUEST_TEMPLATES = [
    "緊急任務: Cドライブ深奥に眠る古のバグを討伐せよ！",
    "新ミッション: 伝説のUSBメモリを社内のどこかで発見せよ",
    "極秘指令: レジストリの迷宮から失われたキーを奪還せよ",
    "挑戦状: システムフォントの中に隠された幻の文字を探し出せ",
    "特別任務: タスクマネージャーの裏に潜む謎のプロセスを追跡せよ",
    "伝説のクエスト: デスクトップの彼方に眠る未保存ファイルを復活させよ",
    "至急: ゴミ箱の底から消えたはずのアイコンを取り戻せ",
    "極秘: BIOSの奥深くに封印された古の設定を解読せよ",
    "チャレンジ: 10年前のバックアップから現代に蘇るデータを救出せよ",
    "特命: ネットワークの海を越えて幻のプリンタを発見せよ"
]

REWARDS = [
    "報酬: システムの安寧と謎の称号",
    "報酬: 未知のファイル群",
    "報酬: OSからの感謝状",
    "報酬: 伝説のバッジ",
    "報酬: バーチャルコーヒー",
    "報酬: 開発者の微笑み",
    "報酬: メモリの加護",
    "報酬: キーボードの祝福",
    "報酬: 伝説のスクリーンセーバー",
    "報酬: システムアップタイム+1"
]

HISTORY_FILE = os.path.expanduser('~/.legendary_quest_history')


def generate_quest():
    quest = random.choice(QUEST_TEMPLATES)
    reward = random.choice(REWARDS)
    return f"[OS公式伝説クエスト通知]\n{quest}\n{reward}"


def show_notification(message):
    system = platform.system()
    if system == "Linux" and notify2:
        notify2.init("Legendary Quest")
        n = notify2.Notification("伝説のOSクエスト", message)
        n.show()
    elif system == "Windows" and ToastNotifier:
        toaster = ToastNotifier()
        toaster.show_toast("伝説のOSクエスト", message, duration=7)
    elif system == "Darwin":
        # macOS: use osascript
        os.system(f"osascript -e 'display notification \"{message}\" with title \"伝説のOSクエスト\"'")
    else:
        print(message)


def save_history(message):
    try:
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}\n{message}\n\n")
    except Exception as e:
        pass  # 履歴保存失敗は無視


def list_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴はまだありません。")
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        print(f.read())


def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴はまだありません。")
        return
    count = 0
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("[OS公式伝説クエスト通知]"):
                count += 1
    print(f"発行された伝説クエスト通知の合計: {count}")


def random_wait(min_sec=600, max_sec=3600):
    wait_time = random.randint(min_sec, max_sec)
    time.sleep(wait_time)


def main():
    parser = argparse.ArgumentParser(description="伝説のOSクエスト通知スクリプト")
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='今すぐ伝説のクエスト通知を発行')
    parser_list = subparsers.add_parser('list', help='過去の通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知履歴のサマリーを表示')
    parser_daemon = subparsers.add_parser('daemon', help='ランダム間隔で自動通知 (バックグラウンド)')
    parser_daemon.add_argument('--min', type=int, default=600, help='最小待機秒数(デフォルト600)')
    parser_daemon.add_argument('--max', type=int, default=3600, help='最大待機秒数(デフォルト3600)')

    args = parser.parse_args()

    if args.command == 'log':
        message = generate_quest()
        show_notification(message)
        save_history(message)
        print(message)
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary_history()
    elif args.command == 'daemon':
        print("伝説のOSクエスト自動通知モード開始。Ctrl+Cで停止します。")
        try:
            while True:
                message = generate_quest()
                show_notification(message)
                save_history(message)
                print(message)
                random_wait(args.min, args.max)
        except KeyboardInterrupt:
            print("\n自動通知を終了しました。")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
