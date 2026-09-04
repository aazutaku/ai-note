import argparse
import random
import sys
import time
import platform
import subprocess
from typing import List

# 通知メッセージ候補
FAKE_TOPICS = [
    "今すぐ全員集合：超重要案件について",
    "本日の議題：コーヒー豆の粒度再検討",
    "出欠はOSが自動判定します",
    "緊急：システムフォントの統一案",
    "会議URLは後日発表されます",
    "全ユーザー参加必須：謎のアップデート説明会",
    "議題：ユーザー名の読み方再確認",
    "重要度MAX：OSマスコットキャラ選定会議",
    "本日の会議はAIが進行します",
    "OS公式：謎の新機能発表会"
]

FAKE_NOTES = [
    "重要度MAX。会議URLは後日発表。",
    "参加必須。欠席は自動的に記録されます。",
    "会議の録画は禁止されています。",
    "議事録はAIが自動生成します。",
    "議題は当日発表。サプライズあり。",
    "出席確認はOSが行います。",
    "会議終了後、アンケートがあります。",
    "会議時間は未定です。",
    "会議資料は配布されません。",
    "会議開始時刻：今すぐ"
]

FAKE_PARTICIPANTS = [
    "全ユーザー（出欠はOSが自動判定します）",
    "管理者・ゲスト含む全員",
    "選抜メンバー（選定基準は非公開）",
    "AI・人間全員",
    "本日ログインしたユーザー全員",
    "OSサポートチーム",
    "全アプリケーション開発者",
    "特別ゲストあり",
    "匿名参加可能",
    "参加者リストは後日公開"
]

# OSごとに通知を出す

def send_notification(title: str, message: str):
    system = platform.system()
    try:
        if system == "Darwin":  # macOS
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "{title}"'
            ], check=True)
        elif system == "Linux":
            subprocess.run([
                "notify-send", title, message], check=True)
        elif system == "Windows":
            try:
                from plyer import notification
                notification.notify(title=title, message=message, timeout=6)
            except ImportError:
                print("[警告] plyerパッケージが必要です: pip install plyer")
        else:
            print("[通知未対応] このOSでは通知がサポートされていません。")
    except Exception as e:
        print(f"[通知エラー] {e}")


def generate_fake_alert() -> str:
    topic = random.choice(FAKE_TOPICS)
    note = random.choice(FAKE_NOTES)
    participant = random.choice(FAKE_PARTICIPANTS)
    alert = (
        "[OS公式] 緊急カンファレンスコール通知\n"
        "----------------------------------------\n"
        f"議題: {topic}\n"
        f"参加必須: {participant}\n"
        "開始時刻: 今すぐ\n"
        f"備考: {note}\n"
        "----------------------------------------"
    )
    return alert


def print_alert(alert: str):
    print(alert)


def log_alert(alert: str, logfile: str = "conference_call_alert.log"):
    try:
        with open(logfile, "a", encoding="utf-8") as f:
            f.write(alert + "\n\n")
    except Exception as e:
        print(f"[ログエラー] {e}")


def list_log(logfile: str = "conference_call_alert.log"):
    try:
        with open(logfile, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("ログファイルが存在しません。")
    except Exception as e:
        print(f"[ログ表示エラー] {e}")


def summary_log(logfile: str = "conference_call_alert.log"):
    try:
        with open(logfile, "r", encoding="utf-8") as f:
            alerts = f.read().split("[OS公式] 緊急カンファレンスコール通知")
            count = len([a for a in alerts if a.strip()])
            print(f"過去のフェイク会議通知回数: {count}")
    except FileNotFoundError:
        print("ログファイルが存在しません。")
    except Exception as e:
        print(f"[サマリーエラー] {e}")


def main():
    parser = argparse.ArgumentParser(description="OS公式フェイク会議通知スキル")
    subparsers = parser.add_subparsers(dest="command")

    # 通知発動
    parser_alert = subparsers.add_parser("alert", help="フェイク会議通知を即時発動")
    parser_alert.add_argument("--no-notify", action="store_true", help="デスクトップ通知を出さずにターミナル出力のみ")
    parser_alert.add_argument("--log", action="store_true", help="通知内容をログファイルに保存")

    # ログ閲覧
    parser_list = subparsers.add_parser("list", help="過去の通知ログを表示")
    parser_list.add_argument("--logfile", default="conference_call_alert.log", help="ログファイル名")

    # サマリー
    parser_summary = subparsers.add_parser("summary", help="通知回数のサマリーを表示")
    parser_summary.add_argument("--logfile", default="conference_call_alert.log", help="ログファイル名")

    # デモ自動発動
    parser_demo = subparsers.add_parser("demo", help="一定間隔で自動的にフェイク通知を発動 (Ctrl+Cで停止)")
    parser_demo.add_argument("--interval", type=int, default=3600, help="通知間隔(秒)")
    parser_demo.add_argument("--log", action="store_true", help="通知内容をログファイルに保存")

    args = parser.parse_args()

    if args.command == "alert":
        alert = generate_fake_alert()
        print_alert(alert)
        if not args.no_notify:
            send_notification("緊急カンファレンスコール", alert.replace("\n", " "))
        if args.log:
            log_alert(alert)
    elif args.command == "list":
        list_log(args.logfile)
    elif args.command == "summary":
        summary_log(args.logfile)
    elif args.command == "demo":
        try:
            while True:
                alert = generate_fake_alert()
                print_alert(alert)
                send_notification("緊急カンファレンスコール", alert.replace("\n", " "))
                if args.log:
                    log_alert(alert)
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\n[終了] デモモードを停止しました。")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
