import random
import sys
import argparse
import time
from plyer import notification

FAKE_ERRORS = [
    "エラー: コーヒーブレイク不足",
    "STOP CODE: 眠気の暴走",
    "原因: キーボードに猫が乗りました",
    "エラー: コードレビュー過多",
    "STOP CODE: 机の上に謎の書類",
    "原因: インターネットの海で遭難",
    "エラー: 進捗が迷子になりました",
    "STOP CODE: マウスが反抗期",
    "原因: コーヒーが冷めました",
    "エラー: 画面の向こうから猫の鳴き声"
]

FAKE_HINTS = [
    "ヒント: 立ち上がってストレッチしましょう",
    "ヒント: 深呼吸してみましょう",
    "ヒント: コーヒーを淹れ直しましょう",
    "ヒント: 目を休めてください",
    "ヒント: ちょっと散歩してみませんか?",
    "ヒント: チームメンバーに声をかけてみましょう",
    "ヒント: 水分補給を忘れずに",
    "ヒント: 猫を撫でてリラックスしましょう"
]

FAKE_FOOTER = "---\nこれはジョーク通知です。作業を続けても問題ありません。"


def generate_fake_bluescreen():
    error = random.choice(FAKE_ERRORS)
    stop_code = random.choice([e for e in FAKE_ERRORS if e != error])
    cause = random.choice([e for e in FAKE_ERRORS if e != error and e != stop_code])
    hint = random.choice(FAKE_HINTS)
    lines = [
        "[FAKE OS BLUESCREEN]",
        error,
        stop_code,
        cause,
        hint,
        FAKE_FOOTER
    ]
    return "\n".join(lines)


def show_notification(message, title="FAKE OS BLUESCREEN"):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="FakeBlueScreenNotifier",
            timeout=10
        )
    except Exception as e:
        print(f"[通知失敗]: {e}")
        print(message)


def log_event(message):
    try:
        with open("fake_bluescreen_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]\n{message}\n\n")
    except Exception as e:
        print(f"[ログ保存失敗]: {e}")


def list_logs():
    try:
        with open("fake_bluescreen_log.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("[ログファイルが存在しません]")


def summary_logs():
    try:
        count = 0
        with open("fake_bluescreen_log.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("[20"):
                    count += 1
        print(f"発行済みジョーク通知数: {count}")
    except FileNotFoundError:
        print("[ログファイルが存在しません]")


def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Bluescreen Notifier")
    subparsers = parser.add_subparsers(dest="command")

    parser_notify = subparsers.add_parser("notify", help="ジョークブルースクリーン通知を表示")
    parser_notify.add_argument("--log", action="store_true", help="通知内容をログファイルに保存")

    parser_list = subparsers.add_parser("list", help="通知ログを一覧表示")
    parser_summary = subparsers.add_parser("summary", help="通知発行数を表示")

    args = parser.parse_args()

    if args.command == "notify":
        msg = generate_fake_bluescreen()
        show_notification(msg)
        print(msg)
        if args.log:
            log_event(msg)
    elif args.command == "list":
        list_logs()
    elif args.command == "summary":
        summary_logs()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
