import sys
import random
import argparse
import time
import os

try:
    import notify2
except ImportError:
    notify2 = None

# 勅令テンプレート
DECREE_TEMPLATES = [
    "皇帝より勅令：本日より{key}の使用を禁ず。",
    "御前会議：{key}の叛逆を鎮圧せよ。",
    "皇帝直々の命：{key}は三度までしか許されぬ。",
    "勅令：本日、{key}は謹慎処分とする。",
    "玉座より：{key}の乱用を慎むべし。",
    "王宮告示：{key}の者は直ちに出頭せよ。",
    "帝国法令：{key}の再起動を禁ず。",
    "皇帝の意志：{key}の者は褒賞を受ける。",
    "勅命：{key}の乱用は国賊と見なす。",
    "御前裁決：{key}の審問を開始する。"
]

# キーワード候補
KEYWORDS = [
    "CapsLock",
    "スペースキー",
    "Backspace",
    "タブキー",
    "Enterキー",
    "スクリーンショット",
    "Shiftキー",
    "マウスホイール",
    "NumLock",
    "Ctrlキー",
    "Altキー",
    "ファイル保存",
    "再起動",
    "ログアウト",
    "ウィンドウ切替"
]

HISTORY_FILE = os.path.expanduser("~/.emperor_decree_history.txt")


def generate_decree():
    template = random.choice(DECREE_TEMPLATES)
    key = random.choice(KEYWORDS)
    decree = template.format(key=key)
    return decree


def notify_decree(decree):
    if notify2 is None:
        print(decree)
        return
    try:
        notify2.init("Emperor Decree Notifier")
        n = notify2.Notification("古代皇帝の勅令", decree)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.set_timeout(5000)
        n.show()
    except Exception as e:
        print(f"[通知失敗] {decree}\n{e}")


def log_decree(decree):
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {decree}\n")
    except Exception as e:
        print(f"[履歴保存失敗] {e}")


def list_history(limit=10):
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()[-limit:]
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("履歴はまだありません。")


def summary():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        total = len(lines)
        unique = len(set(line.split(' ', 2)[-1] for line in lines))
        print(f"発令回数: {total}回\nユニーク勅令: {unique}種")
    except FileNotFoundError:
        print("履歴はまだありません。")


def main():
    parser = argparse.ArgumentParser(description="古代皇帝の勅令通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_notify = subparsers.add_parser("notify", help="勅令を即時通知")
    parser_notify.add_argument("--log", action="store_true", help="履歴に記録する")

    parser_list = subparsers.add_parser("list", help="勅令履歴を表示")
    parser_list.add_argument("--limit", type=int, default=10, help="表示件数")

    parser_summary = subparsers.add_parser("summary", help="勅令履歴のサマリ表示")

    args = parser.parse_args()

    if args.command == "notify" or args.command is None:
        decree = generate_decree()
        notify_decree(decree)
        if hasattr(args, 'log') and args.log:
            log_decree(decree)
    elif args.command == "list":
        list_history(args.limit)
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
