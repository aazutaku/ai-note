import os
import sys
import random
import time
import argparse
import threading
from datetime import datetime

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

QUEST_TEMPLATES = [
    "緊急任務: {location}に眠る{target}退治",
    "伝説の{item}捜索開始 - 手がかり: {hint}",
    "システム管理者からの挑戦状: {challenge}",
    "秘密のプロセス\"{process}.exe\"を発見せよ",
    "禁断の{place}迷宮に挑め",
    "未知のファイル\"{file}\"の正体を暴け",
    "古の{device}の封印を解放せよ",
    "OSの神託: {prophecy}",
    "伝説のバッチファイル\"{batch}\"を実行せよ",
    "謎のタスク\"{task}\"を完遂せよ"
]

QUEST_VARS = {
    "location": ["Cドライブ深奥", "システムフォルダ", "Program Filesの裏側", "レジストリの迷宮", "ネットワークの果て"],
    "target": ["古のバグ", "消えた設定", "幽霊プロセス", "未知のウイルス", "隠れファイル"],
    "item": ["USBメモリ", "ライセンスキー", "失われたショートカット", "幻のアイコン", "管理者パスワード"],
    "hint": ["旧PCの引き出し", "謎のメモ.txt", "開かずのフォルダ", "READMEに隠されたヒント", "壁紙の裏"],
    "challenge": ["ゴミ箱の中から消えたファイルを探せ", "3日以内に未知のエラーを再現せよ", "隠されたユーザーを見つけよ", "システム時計を未来に進めろ", "ログファイルの暗号を解読せよ"],
    "process": ["dragon", "phoenix", "unicorn", "goblin", "wizard"],
    "place": ["レジストリ", "サービス", "ドライバ", "タスクスケジューラ", "スタートアップ"],
    "file": ["secret.dll", "mystery.sys", "hidden.txt", "legend.bat", "ghost.exe"],
    "device": ["フロッピーディスク", "SCSIドライブ", "モデム", "CRTモニタ", "PS/2マウス"],
    "prophecy": ["今日中にブルースクリーンを回避せよ", "ダークモードを極めよ", "すべての通知を受け入れよ", "未知のショートカットを発見せよ", "隠し設定を解放せよ"],
    "batch": ["start_legend.bat", "awakening.cmd", "final_quest.bat", "dragon_hunt.bat", "phoenix_rise.cmd"],
    "task": ["1000個のウィンドウを閉じろ", "連続リブートに耐えろ", "すべてのアイコンを並べ替えよ", "謎のプロセスを終了せよ", "無限ループから脱出せよ"]
}

LOG_FILE = os.path.expanduser("~/.legendary_quest_log.txt")


def generate_quest():
    template = random.choice(QUEST_TEMPLATES)
    quest = template
    for key in QUEST_VARS:
        if f'{{{key}}}' in template:
            quest = quest.replace(f'{{{key}}}', random.choice(QUEST_VARS[key]))
    return quest


def notify_quest(quest):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"[OS Notification] {quest}"
    print(message)
    if PLYER_AVAILABLE:
        notification.notify(
            title="伝説のOSクエスト",
            message=quest,
            timeout=8
        )
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{timestamp} {quest}\n")


def random_notify_loop(min_interval=300, max_interval=1200, stop_event=None):
    while not (stop_event and stop_event.is_set()):
        wait_sec = random.randint(min_interval, max_interval)
        for _ in range(wait_sec):
            if stop_event and stop_event.is_set():
                return
            time.sleep(1)
        quest = generate_quest()
        notify_quest(quest)


def list_log(count=10):
    if not os.path.exists(LOG_FILE):
        print("No quest notifications have been logged yet.")
        return
    with open(LOG_FILE, encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines[-count:]:
        print(line.strip())


def summary():
    if not os.path.exists(LOG_FILE):
        print("No quest notifications have been logged yet.")
        return
    with open(LOG_FILE, encoding='utf-8') as f:
        lines = f.readlines()
    print(f"Total fake legendary quests notified: {len(lines)}")


def main():
    parser = argparse.ArgumentParser(description="伝説のOSクエスト通知スクリプト")
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='通知履歴を最新から10件表示')
    parser_log.add_argument('--count', type=int, default=10, help='表示件数 (デフォルト10)')

    parser_summary = subparsers.add_parser('summary', help='通知の総数を表示')

    parser_notify = subparsers.add_parser('notify', help='今すぐ伝説のクエスト通知を表示')

    parser_daemon = subparsers.add_parser('daemon', help='ランダムな間隔で自動通知 (Ctrl+Cで停止)')
    parser_daemon.add_argument('--min', type=int, default=300, help='最小通知間隔(秒)')
    parser_daemon.add_argument('--max', type=int, default=1200, help='最大通知間隔(秒)')

    args = parser.parse_args()

    if args.command == 'log':
        list_log(args.count)
    elif args.command == 'summary':
        summary()
    elif args.command == 'notify':
        quest = generate_quest()
        notify_quest(quest)
    elif args.command == 'daemon':
        stop_event = threading.Event()
        try:
            print(f"伝説のOSクエスト通知デーモンを起動します (間隔: {args.min}-{args.max}秒)。Ctrl+Cで停止")
            random_notify_loop(args.min, args.max, stop_event)
        except KeyboardInterrupt:
            print("\nデーモンを停止しました。")
            stop_event.set()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
