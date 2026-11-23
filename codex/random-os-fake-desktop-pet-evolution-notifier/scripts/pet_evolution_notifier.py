import argparse
import random
import sys
import os
import platform
from datetime import datetime

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

# ペット進化・誕生パターン
EVOLUTION_PATTERNS = [
    "あなたのマウスポインタは本日“幻のカメレオン形態”に進化しました。",
    "本日よりキーボードに“サボテン系ペット”が宿ります。",
    "デスクトップ領域に“浮遊型ペンギン”が誕生しました。お世話不要です。",
    "あなたのターミナルには“夜行性リス”が進化して棲みつきました。",
    "本日限定で“回転式クラゲ”がデスクトップを巡回中です。",
    "マウスクリック時に“瞬間移動型カメ”が現れます。",
    "あなたのファイルアイコンに“忍者モルモット”が潜んでいます。",
    "ウィンドウ切替時に“歌うアザラシ”が応援します。",
    "デスクトップ右下に“透明ハリネズミ”が棲みつきました。",
    "本日、スクリーンセーバーに“踊るミミズク”が乱入します。",
    "あなたのエディタに“詠唱型カラス”がアドバイスを始めました。",
    "キーボードのFキーに“ひらめきイルカ”が宿りました。",
    "ターミナルのプロンプトに“跳ねるウサギ”が現れました。",
    "デスクトップ壁紙の裏に“隠れヤモリ”が進化しました。",
    "本日、USBポートに“電脳カブトムシ”が誕生しました。"
]

# 通知タイトル
NOTIFY_TITLE = "OS公式通知"

# 通知を出す（plyerがあればデスクトップ、なければprint）
def notify(message):
    if PLYER_AVAILABLE:
        try:
            notification.notify(title=NOTIFY_TITLE, message=message, app_name="FakeDesktopPet", timeout=7)
        except Exception as e:
            print(f"[通知失敗] {e}\n[OS公式通知] {message}")
    else:
        print(f"[OS公式通知] {message}")

# ランダムで進化通知を生成
def generate_notification():
    return random.choice(EVOLUTION_PATTERNS)

# 履歴ログ用ファイルパス（ユーザーディレクトリ直下）
def get_log_path():
    home = os.path.expanduser("~")
    return os.path.join(home, ".fake_desktop_pet_notify.log")

# 通知ログを保存
def log_notification(message):
    log_path = get_log_path()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

# ログ一覧表示
def list_notifications():
    log_path = get_log_path()
    if not os.path.exists(log_path):
        print("通知履歴はありません。")
        return
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            print(line.rstrip())

# ログ要約表示
def summary_notifications():
    log_path = get_log_path()
    if not os.path.exists(log_path):
        print("通知履歴はありません。")
        return
    counts = {}
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            for pattern in EVOLUTION_PATTERNS:
                if pattern in line:
                    counts[pattern] = counts.get(pattern, 0) + 1
    print("--- 通知パターン別集計 ---")
    for pattern, count in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{pattern} : {count}回")

# CLI引数パース
def parse_args():
    parser = argparse.ArgumentParser(description="謎のOS公式デスクトップペット進化通知をランダムで炸裂させるスクリプト")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")
    subparsers.add_parser("notify", help="ランダムな進化通知を1回出す")
    subparsers.add_parser("log", help="通知履歴を一覧表示")
    subparsers.add_parser("summary", help="通知履歴をパターン別に集計表示")
    return parser.parse_args()

# メイン処理
def main():
    args = parse_args()
    if args.command == "notify" or args.command is None:
        message = generate_notification()
        notify(message)
        log_notification(message)
    elif args.command == "log":
        list_notifications()
    elif args.command == "summary":
        summary_notifications()
    else:
        print("不明なコマンドです。--help を参照してください。")

if __name__ == "__main__":
    main()
