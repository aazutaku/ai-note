import sys
import random
import platform
import subprocess
import argparse
import time
from typing import List

FAKE_PATCH_NOTES = [
    "超重要: バグ『脳内会議ループが止まらない』を修正しました。",
    "新機能: やる気を一時的に1.5倍に加速するモードを追加。",
    "セキュリティ強化: “無限リファクタリング”の脆弱性を一時的に封印。",
    "パフォーマンス改善: “Slack通知が止まらない”問題を根本から対策。",
    "既知の問題: “金曜日の集中力低下”は引き続き調査中です。",
    "新機能: “納期ギリギリモード”を実装（推奨されません）。",
    "バグ修正: “コーヒーが切れるとビルドが失敗する”問題を解決。",
    "互換性向上: “昼寝API”との連携を強化。",
    "安定性向上: “無限デバッグ地獄”からの自動脱出をサポート。",
    "UI改善: “やる気ゲージ”の表示がより分かりやすくなりました。",
    "パッチノート: “今日のやる気”は保証されません。",
    "新機能: “脳内BGM自動切り替え”を追加。",
    "バグ修正: “週明けに記憶が消える”問題を一部解消。",
    "安定性向上: “夜更かし検知”機能を強化。",
    "パフォーマンス改善: “会議中の眠気”を低減するアルゴリズムを導入。"
]

NOTIFY_TITLE = "OS Patch Alert"


def select_random_note() -> str:
    return random.choice(FAKE_PATCH_NOTES)


def send_notification(title: str, message: str):
    system = platform.system()
    try:
        if system == "Darwin":  # macOS
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            subprocess.run(["notify-send", title, message], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=5, threaded=True)
                # Wait for threaded notification to finish
                time.sleep(5)
            except ImportError:
                print("win10toastが見つかりません。pip install win10toast を実行してください。", file=sys.stderr)
        else:
            print(f"未対応のOSです: {system}", file=sys.stderr)
    except Exception as e:
        print(f"通知の送信に失敗しました: {e}", file=sys.stderr)


def list_patch_notes():
    print("--- 収録済みウソパッチノート一覧 ---")
    for i, note in enumerate(FAKE_PATCH_NOTES, 1):
        print(f"{i:2d}. {note}")


def summary():
    print(f"登録ウソパッチノート数: {len(FAKE_PATCH_NOTES)}")
    print(f"対応OS: macOS, Linux, Windows (win10toast要)\n")
    print("このSkillは、作業中にジョーク通知をデスクトップに表示し、緊張感や笑いを演出します。実害はありません。")


def log(times: int = 1, interval: float = 0):
    for _ in range(times):
        note = select_random_note()
        print(f"[{NOTIFY_TITLE}] {note}")
        send_notification(NOTIFY_TITLE, note)
        if interval > 0:
            time.sleep(interval)


def parse_args():
    parser = argparse.ArgumentParser(description="謎のOS緊急パッチアラートをデスクトップ通知で爆誕させるSkill")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_log = subparsers.add_parser("log", help="ウソパッチノートをランダムに通知する")
    parser_log.add_argument("-n", "--times", type=int, default=1, help="通知回数 (デフォルト1)")
    parser_log.add_argument("-i", "--interval", type=float, default=0, help="通知間隔(秒)")

    parser_list = subparsers.add_parser("list", help="収録済みウソパッチノート一覧を表示")
    parser_summary = subparsers.add_parser("summary", help="Skill概要を表示")

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "log":
        log(times=args.times, interval=args.interval)
    elif args.command == "list":
        list_patch_notes()
    elif args.command == "summary":
        summary()
    else:
        print("不明なコマンドです。--help を参照してください。", file=sys.stderr)

if __name__ == '__main__':
    main()
