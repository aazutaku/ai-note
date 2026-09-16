import random
import sys
import argparse
import platform
import subprocess
import os

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

PATCH_TITLES = [
    "Patch Tuesday Alert",
    "緊急パッチ適用通知",
    "OSアップデート速報",
    "公式パッチノート",
    "システム更新情報"
]

FAKE_PATCHES = [
    "OSがCapsLockキーの連打回数を自動でツイートする機能を追加しました。",
    "Altキー長押しでデスクトップ壁紙がランダムな俳句に変わる不具合を修正。",
    "Ctrlキーを3秒間押し続けるとOSが自己紹介を開始します。",
    "マウスカーソルが一定時間停止すると、画面上でダンスを始めます。",
    "ターミナルでlsコマンド実行時、ディレクトリ名がすべて回文に変換されます。",
    "新機能: Shiftキー同時押しでファイル名が古代文字に変換されます。",
    "重要: スクロールホイール逆回転時、画面が上下逆さまになります。",
    "修正: タスクバーが1時間ごとに色を自動で変えます。",
    "アップデート: サウンドミュート時、OSが静かに拍手します。",
    "新機能: ターミナルでexitコマンド実行時、OSが励ましの言葉を表示します。",
    "Ctrl+Alt+DelでOSが今日のラッキーアイテムを教えてくれます。",
    "CapsLockがONのまま1分経過すると、画面がミラーボールに変化します。",
    "Alt+Tabで切り替えたウィンドウが一瞬だけ透明化されます。",
    "新機能: ファイルコピー時に進捗バーが虹色に点滅します。",
    "修正: スリープ復帰時にOSが詩を朗読する問題を解消しました。",
    "重要: スペースキー連打でOSがリズムゲームモードに突入します。",
    "新機能: ターミナルでhistoryコマンド実行時、過去のコマンドが俳句形式で表示されます。",
    "アップデート: デスクトップアイコンが毎朝ランダムな位置にシャッフルされます。",
    "修正: 再起動時にOSがユーザーにおみくじを引かせる機能を追加。",
    "重要: マウス右クリックでOSが今日の天気を詠唱します。"
]

TERMINAL_COLORS = {
    "HEADER": '\033[95m',
    "OKBLUE": '\033[94m',
    "OKCYAN": '\033[96m',
    "OKGREEN": '\033[92m',
    "WARNING": '\033[93m',
    "FAIL": '\033[91m',
    "ENDC": '\033[0m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m'
}

def generate_fake_patch():
    title = random.choice(PATCH_TITLES)
    body = random.choice(FAKE_PATCHES)
    return f"[{title}] {body}"

def show_terminal_alert(message):
    color = random.choice([
        TERMINAL_COLORS["OKGREEN"],
        TERMINAL_COLORS["OKBLUE"],
        TERMINAL_COLORS["OKCYAN"],
        TERMINAL_COLORS["WARNING"]
    ])
    print(f"{color}{message}{TERMINAL_COLORS['ENDC']}")

def show_desktop_notification(message):
    if PLYER_AVAILABLE:
        notification.notify(
            title="Patch Tuesday Alert",
            message=message,
            timeout=8
        )
    else:
        system = platform.system()
        if system == "Darwin":
            script = f'display notification "{message}" with title "Patch Tuesday Alert"'
            subprocess.run(["osascript", "-e", script])
        elif system == "Linux":
            subprocess.run(["notify-send", "Patch Tuesday Alert", message])
        elif system == "Windows":
            # Fallback: use msg.exe if available
            try:
                subprocess.run(["msg", "*", message])
            except Exception:
                pass
        else:
            pass  # No supported notification

def list_patches(n=5):
    for _ in range(n):
        msg = generate_fake_patch()
        show_terminal_alert(msg)

def summary():
    print("このSkillは、完全ランダムな“ありえないパッチノート”を生成し、ターミナルやデスクトップに通知します。通知内容は現実のOSアップデートとは一切関係ありません。")

def parse_args():
    parser = argparse.ArgumentParser(description="Random OS Fake Patch Tuesday Alert")
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='ランダムなパッチノート通知を1件表示')
    parser_alert.add_argument('--desktop', action='store_true', help='デスクトップ通知も行う')

    parser_list = subparsers.add_parser('list', help='複数のパッチノートをターミナルに表示')
    parser_list.add_argument('-n', type=int, default=5, help='表示件数 (デフォルト5)')

    parser_summary = subparsers.add_parser('summary', help='Skill概要を表示')

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'alert':
        msg = generate_fake_patch()
        show_terminal_alert(msg)
        if args.desktop:
            show_desktop_notification(msg)
    elif args.command == 'list':
        list_patches(args.n)
    elif args.command == 'summary':
        summary()
    else:
        # デフォルトは1件通知
        msg = generate_fake_patch()
        show_terminal_alert(msg)
        show_desktop_notification(msg)

if __name__ == '__main__':
    main()
