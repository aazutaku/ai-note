import random
import argparse
import sys
import time
import os
import platform
import subprocess
from datetime import datetime

QUEST_TEMPLATES = [
    {
        'title': '緊急任務: {location}に眠る{target}退治',
        'location': ['Cドライブ深奥', 'ネットワークの彼方', 'レジストリ迷宮', '未確認フォルダ', 'システムログの闇'],
        'target': ['古のバグ', '伝説のプロセス', '謎のメモリリーク', '消えたショートカット', '幻の設定ファイル'],
        'reward': ['システム安定度+100', 'CPU使用率-10%', '未知の称号「バグスレイヤー」', 'メモリ開放', '管理者権限の祝福']
    },
    {
        'title': '伝説の{item}捜索開始',
        'item': ['USBメモリ', 'フロッピーディスク', 'バックアップHDD', 'Wi-Fiルーター', '未認識デバイス'],
        'location': ['デスク下の未確認領域', '引き出しの奥', 'ケーブルジャングル', 'サーバールーム', '箱の中'],
        'reward': ['発見者バッジ', 'ストレージ容量+1GB', '謎のファイルアクセス権', '伝説の称号「発掘王」', 'OSからの感謝状']
    },
    {
        'title': '極秘: {mission}指令',
        'mission': ['レジストリ迷宮からの脱出', '未読ログの全読破', '隠しプロセスの発見', 'システム設定の最適化', '謎のタスクスケジューラ解除'],
        'deadline': ['24時間以内', '本日中', '次回起動時まで', '今すぐ', '週末まで'],
        'reward': ['セキュリティレベル+10', 'OS称賛メッセージ', '管理者パスワードのヒント', '伝説の壁紙', '未知のアップデート権']
    }
]

HISTORY_FILE = os.path.expanduser('~/.legendary_quest_history.log')


def generate_quest():
    template = random.choice(QUEST_TEMPLATES)
    title = template['title']
    fields = {}
    for k, v in template.items():
        if k == 'title':
            continue
        fields[k] = random.choice(v)
    quest = title.format(**fields)
    # Optional fields
    details = []
    for k, v in fields.items():
        if k not in ['title']:
            details.append(f"{k.capitalize()}: {v}")
    # Add reward if exists
    if 'reward' in template:
        reward = random.choice(template['reward'])
        details.append(f"報酬: {reward}")
    if 'deadline' in fields:
        details.append(f"期限: {fields['deadline']}")
    return quest, details


def notify_terminal(quest, details):
    print("[OS Quest Notification]")
    print(quest)
    for d in details:
        print(d)
    print("---")


def notify_os(quest, details):
    system = platform.system()
    message = quest + "\n" + "\n".join(details)
    try:
        if system == 'Darwin':  # macOS
            subprocess.run([
                'osascript', '-e', f'display notification "{message}" with title "伝説のOSクエスト"'
            ], check=True)
        elif system == 'Linux':
            subprocess.run([
                'notify-send', '伝説のOSクエスト', message
            ], check=True)
        elif system == 'Windows':
            from ctypes import windll
            import threading
            def toast():
                try:
                    import win10toast
                    toaster = win10toast.ToastNotifier()
                    toaster.show_toast("伝説のOSクエスト", message, duration=10)
                except ImportError:
                    print("win10toastが必要です: pip install win10toast")
            t = threading.Thread(target=toast)
            t.start()
        else:
            notify_terminal(quest, details)
    except Exception as e:
        print(f"OS通知に失敗しました: {e}")
        notify_terminal(quest, details)


def save_history(quest, details):
    try:
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
            f.write(f"[{datetime.now().isoformat()}] {quest}\n")
            for d in details:
                f.write(f"  {d}\n")
            f.write("---\n")
    except Exception as e:
        print(f"履歴保存に失敗しました: {e}")


def list_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        print(f.read())


def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    quests = []
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('['):
                quests.append(line.strip())
    print(f"これまで発生した伝説のクエスト数: {len(quests)}")
    for q in quests[-5:]:
        print(q)


def main():
    parser = argparse.ArgumentParser(description='伝説のOSクエスト通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_notify = subparsers.add_parser('notify', help='今すぐ伝説のクエスト通知を出す')
    parser_notify.add_argument('--os', action='store_true', help='OS通知も行う')
    parser_notify.add_argument('--save', action='store_true', help='履歴に保存')

    parser_list = subparsers.add_parser('list', help='過去のクエスト履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='クエスト履歴のサマリー')

    parser_daemon = subparsers.add_parser('daemon', help='一定時間ごとにランダム通知 (Ctrl+Cで停止)')
    parser_daemon.add_argument('--interval', type=int, default=1800, help='通知間隔(秒, デフォルト30分)')
    parser_daemon.add_argument('--os', action='store_true', help='OS通知も行う')
    parser_daemon.add_argument('--save', action='store_true', help='履歴に保存')

    args = parser.parse_args()

    if args.command == 'notify':
        quest, details = generate_quest()
        if args.os:
            notify_os(quest, details)
        else:
            notify_terminal(quest, details)
        if args.save:
            save_history(quest, details)
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary_history()
    elif args.command == 'daemon':
        try:
            while True:
                quest, details = generate_quest()
                if args.os:
                    notify_os(quest, details)
                else:
                    notify_terminal(quest, details)
                if args.save:
                    save_history(quest, details)
                wait = args.interval + random.randint(-60, 60)
                time.sleep(max(60, wait))
        except KeyboardInterrupt:
            print("\n伝説のクエスト通知デーモンを終了します。")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
