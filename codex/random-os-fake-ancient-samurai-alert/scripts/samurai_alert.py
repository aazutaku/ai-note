import sys
import os
import random
import argparse
import platform
import subprocess
from typing import List

SAMURAI_MESSAGES = [
    "拙者、あなたのAltキーの抜刀訓練状況を監視しておる。",
    "油断大敵、マウスの居合切りに注意せよ。",
    "このターミナル、既に斬撃済み。",
    "ファイル保存、まるで刀の鞘納めの如し。",
    "スクロールは風の如く、急ぐべからず。",
    "ウィンドウ切替、まるで忍びの如し。",
    "コマンド入力、心静かに一刀両断せよ。",
    "エラー多発、修羅の道を歩む覚悟はあるか。",
    "ディレクトリ移動、まるで城攻めの如し。",
    "ログアウト、武士の情けを忘れるな。",
    "CapsLock、誤って押すは切腹もの也。",
    "スリープ解除、まるで瞑想から覚める侍の如し。",
    "バッテリー残量、命の灯火に等し。",
    "パーミッション拒否、門前払いの恥辱也。",
    "ファイル名に空白、敵の隙を作るな。",
    "コピペ多用、己の刀を信じよ。",
    "アップデート怠慢、刀の錆に注意せよ。",
    "タスクキル、敵将首を討ち取ったり。",
    "リネーム、名を変えるは覚悟の証。",
    "シンタックスエラー、文法の乱れは心の乱れ。"
]

NOTIF_TITLE = "OS侍警告"


def choose_message() -> str:
    return random.choice(SAMURAI_MESSAGES)


def show_terminal_alert(message: str):
    print(f"[{NOTIF_TITLE}] {message}")


def show_desktop_notification(message: str):
    system = platform.system()
    if system == "Darwin":
        # macOS
        script = f'display notification "{message}" with title "{NOTIF_TITLE}"'
        try:
            subprocess.run(["osascript", "-e", script], check=True)
        except Exception as e:
            show_terminal_alert(message)
    elif system == "Linux":
        # Linux (notify-send)
        try:
            subprocess.run(["notify-send", NOTIF_TITLE, message], check=True)
        except Exception as e:
            show_terminal_alert(message)
    elif system == "Windows":
        # Windows 10+ (powershell toast)
        try:
            powershell_script = (
                f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null; "
                f"$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02); "
                f"$textNodes = $template.GetElementsByTagName('text'); "
                f"$textNodes.Item(0).AppendChild($template.CreateTextNode('{NOTIF_TITLE}')) > $null; "
                f"$textNodes.Item(1).AppendChild($template.CreateTextNode('{message}')) > $null; "
                f"$toast = [Windows.UI.Notifications.ToastNotification]::new($template); "
                f"$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('SamuraiAlert'); "
                f"$notifier.Show($toast);"
            )
            subprocess.run([
                "powershell", "-NoProfile", "-Command", powershell_script
            ], check=True)
        except Exception as e:
            show_terminal_alert(message)
    else:
        show_terminal_alert(message)


def list_messages():
    print("--- OS侍 謎メッセージ一覧 ---")
    for i, msg in enumerate(SAMURAI_MESSAGES, 1):
        print(f"{i:2d}: {msg}")


def alert(args):
    msg = choose_message()
    if args.terminal:
        show_terminal_alert(msg)
    else:
        show_desktop_notification(msg)


def main():
    parser = argparse.ArgumentParser(
        description="作業中に謎のOS侍警告を炸裂させるスキル。デスクトップ通知またはターミナル出力で侍メッセージを表示。"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_alert = subparsers.add_parser("alert", help="ランダムな侍警告を表示")
    parser_alert.add_argument(
        "--terminal", action="store_true", help="ターミナル出力のみ（デスクトップ通知を使わない）"
    )
    parser_alert.set_defaults(func=alert)

    parser_list = subparsers.add_parser("list", help="すべての侍メッセージを一覧表示")
    parser_list.set_defaults(func=lambda args: list_messages())

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
