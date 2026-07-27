import random
import sys
import argparse
import time
import platform
import threading
from datetime import datetime

try:
    from plyer import notification
except ImportError:
    notification = None

FAKE_PATCH_NOTES = [
    [
        "超重要：バグ『脳内会議ループが止まらない』を修正",
        "新機能：やる気を一時的に1.5倍に加速するボタンを追加",
        "セキュリティ：コーヒーブレイク検出機能を強化"
    ],
    [
        "重要：タスク切替時の『無限思考モード』を抑制",
        "新機能：Slack通知を自動で既読にするオプションを追加",
        "安定性：エラー時に『深呼吸推奨』メッセージを表示"
    ],
    [
        "バグ修正：『今日やる気が出ない』現象を一時的に回避",
        "新機能：コーヒー残量低下時のアラートを追加",
        "改善：マウスカーソルの迷子率を低減"
    ],
    [
        "パフォーマンス：『無限リファクタリング』を抑止",
        "新機能：ランダムに褒めてくれる通知を追加",
        "安定性：月曜日の起動時に優しくなる設定を追加"
    ],
    [
        "修正：『気が付くと夕方』バグを軽減",
        "新機能：定時退社ボタンを（見た目だけ）追加",
        "セキュリティ：『おやつ食べ過ぎ』検出機能を強化"
    ]
]

FAKE_VERSIONS = [
    "12.34.5678", "2024.06.01-beta", "v4.2.0-rc1", "0.99.99", "2024.1.1a", "23.7.42.1001"
]

FAKE_TITLES = [
    "OS緊急パッチアラート",
    "システムアップデート通知",
    "超重要：即時適用推奨パッチ",
    "謎のアップデート速報",
    "非公式パッチノート"
]

def generate_fake_patch():
    version = random.choice(FAKE_VERSIONS)
    notes = random.choice(FAKE_PATCH_NOTES)
    title = random.choice(FAKE_TITLES)
    body = f"バージョン: {version}\n- " + "\n- ".join(notes) + "\n\n詳細は公式サイトをご確認ください。"
    return title, body

def show_notification(title, message, timeout=10):
    if notification is None:
        print("[警告] plyerがインストールされていません。通知はコンソール出力のみです。")
        print(f"[{title}]\n{message}")
        return
    notification.notify(
        title=title,
        message=message,
        timeout=timeout
    )

def log_event(title, message, logfile="fake_patch_alert.log"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {title}\n{message}\n---\n")

def list_logs(logfile="fake_patch_alert.log", count=5):
    try:
        with open(logfile, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("ログファイルが存在しません。")
        return
    entries = []
    entry = []
    for line in lines:
        if line.strip() == '---':
            if entry:
                entries.append(entry)
                entry = []
        else:
            entry.append(line)
    for e in entries[-count:]:
        print("".join(e))
        print("---")

def summary_logs(logfile="fake_patch_alert.log"):
    try:
        with open(logfile, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("ログファイルが存在しません。")
        return
    count = sum(1 for line in lines if line.startswith("["))
    print(f"これまでに発動した偽パッチ通知: {count} 回")

def auto_alert_loop(interval=1800):
    while True:
        title, body = generate_fake_patch()
        show_notification(title, body)
        log_event(title, body)
        time.sleep(interval)

def main():
    parser = argparse.ArgumentParser(description="Fake OS Urgent Patch Alert Skill")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="今すぐ偽パッチ通知を表示")
    parser_alert.add_argument("--log", action="store_true", help="通知内容をログに保存")

    parser_auto = subparsers.add_parser("auto", help="一定間隔で自動的に偽パッチ通知を発動")
    parser_auto.add_argument("--interval", type=int, default=1800, help="通知間隔(秒)")

    parser_list = subparsers.add_parser("list", help="過去の偽パッチ通知ログを表示")
    parser_list.add_argument("--count", type=int, default=5, help="表示する件数")

    parser_summary = subparsers.add_parser("summary", help="通知発動回数のサマリーを表示")

    args = parser.parse_args()

    if args.command == "alert":
        title, body = generate_fake_patch()
        show_notification(title, body)
        if args.log:
            log_event(title, body)
    elif args.command == "auto":
        print(f"{args.interval}秒ごとに偽パッチ通知を発動します。終了はCtrl+C")
        try:
            auto_alert_loop(interval=args.interval)
        except KeyboardInterrupt:
            print("\n自動通知を終了しました。")
    elif args.command == "list":
        list_logs(count=args.count)
    elif args.command == "summary":
        summary_logs()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
