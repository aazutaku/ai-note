import sys
import random
import argparse
import time
import os
import subprocess
from typing import List

def get_prophecy_lines() -> List[str]:
    subjects = [
        "南のコード砂漠", "北のリポジトリ", "西のCI/CDの門", "東のデプロイ渓谷",
        "中央のバグの祭壇", "古のコミット樹", "忘却のIssue沼", "静寂のPull Request山"
    ]
    actions = [
        "巨大バグの影動く", "伝説のレビュアー現る", "テストの嵐吹き荒れる",
        "神秘のマージコンフリクト迫る", "古代Lintの声響く", "警告の風が吹く",
        "未踏のバージョンアップ始まる", "謎のCI失敗繰り返す"
    ]
    omens = [
        "時を超えしレビュアー、北のリポジトリに現る。",
        "西のCI/CDの門、今まさに開かれん。",
        "南のコード砂漠に巨大バグの影動く。",
        "中央のバグの祭壇、静かに揺らぐ。",
        "古のコミット樹、枝分かれの時近し。",
        "忘却のIssue沼、深き謎を湛える。",
        "静寂のPull Request山に警告の風が吹く。",
        "東のデプロイ渓谷、神秘のマージコンフリクト迫る。"
    ]
    lines = []
    # 1〜2行は subjects + actions, 1行は omens から選ぶ
    n = random.randint(1, 2)
    for _ in range(n):
        subj = random.choice(subjects)
        act = random.choice(actions)
        lines.append(f"{subj}に{act}。")
    lines.append(random.choice(omens))
    return lines

def format_prophecy(lines: List[str]) -> str:
    border = "=" * 24
    body = "\n".join(lines)
    return f"{border}\n古代OS預言通知\n{body}\n{border}"

def show_notification(message: str):
    # クロスプラットフォームで通知を表示
    if sys.platform.startswith("darwin"):
        # macOS: AppleScript で通知
        script = f'display notification "{message}" with title "古代OS預言"'
        subprocess.run(["osascript", "-e", script])
    elif sys.platform.startswith("linux"):
        # Linux: notify-send
        try:
            subprocess.run(["notify-send", "古代OS預言", message])
        except Exception:
            pass  # notify-sendがなければ無視
    elif sys.platform.startswith("win"):
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("古代OS預言", message, duration=7)
        except ImportError:
            print("[警告] win10toastが見つかりません。pip install win10toast でインストールしてください。")
    # 端末にも出力
    print(message)

def prophecy_alert():
    lines = get_prophecy_lines()
    message = format_prophecy(lines)
    show_notification(message)

def list_prophecies(count: int = 5):
    for _ in range(count):
        lines = get_prophecy_lines()
        message = format_prophecy(lines)
        print(message)
        print()

def summary():
    print("このSkillは、架空のOS公式による古代預言通知をランダムに生成し、ターミナルやデスクトップに表示します。実用性はありませんが、開発現場に非日常の彩りを加えます。明示呼び出し・自動発動の両対応。")

def parse_args():
    parser = argparse.ArgumentParser(description="古代OS預言通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    alert_parser = subparsers.add_parser("alert", help="預言通知を即時発動")

    list_parser = subparsers.add_parser("list", help="ランダム預言を複数表示")
    list_parser.add_argument("--count", type=int, default=5, help="表示する預言の数")

    summary_parser = subparsers.add_parser("summary", help="Skill概要を表示")

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == "alert" or args.command is None:
        prophecy_alert()
    elif args.command == "list":
        list_prophecies(args.count)
    elif args.command == "summary":
        summary()
    else:
        print("不明なコマンドです。--help を参照してください。")

if __name__ == '__main__':
    main()
