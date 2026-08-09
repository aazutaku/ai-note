import sys
import os
import random
import argparse
import platform
import subprocess
import time
from typing import List

LEGACY_ALERTS = [
    "98互換モードのサポートが本日終了しました。",
    "IE6向け最適化は永遠に封印されました。",
    "フロッピー対応APIが旅立ちました。",
    "Windows MEのリモートデスクトップ機能は伝説となりました。",
    "OS/2 Warp対応プリンタドライバの提供が終了しました。",
    "Netscape Navigator 4用CSS互換レイヤーが削除されました。",
    "MS-DOSバッチ互換レイヤーが眠りにつきました。",
    "ActiveXコントロールのサポートが時空の彼方へ消えました。",
    "ISAバス対応ドライバの提供が終了しました。",
    "Windows 3.1向けTrueTypeフォントAPIが封印されました。",
    "PC-98エミュレーションモードが宇宙の果てに旅立ちました。",
    "Lotus 1-2-3互換モードが永久に失われました。",
    "BASICランタイムのサポートが消滅しました。",
    "SCSI-1デバイスの自動検出機能が削除されました。",
    "IE5.5用Active Desktopの提供が終了しました。",
    "Windows 2000のセーフモード起動支援が歴史に幕を下ろしました。",
    "VGA16色互換APIが時代の流れに消えました。",
    "MSN Messenger連携機能が永遠に失われました。",
    "Windows XP Lunaテーマのサポートが終了しました。",
    "FAT12ファイルシステムのサポートがついに終焉を迎えました。",
    "PCMCIAカードホットスワップAPIが消滅しました。",
    "Windows 95用DirectX 3.0互換モードが削除されました。",
    "古のレガシーBIOSサポートが宇宙の塵となりました。",
    "Netscape Plugin APIの提供が終了しました。",
    "Windows 98SEのUSB1.1互換レイヤーが封印されました。"
]

HISTORY_FILE = os.path.expanduser("~/.random_os_fake_legacy_support_alert_history")


def send_notification(message: str):
    system = platform.system()
    try:
        if system == "Darwin":
            script = f'display notification "{message}" with title "通知"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("通知", message, duration=5)
            except ImportError:
                # fallback to PowerShell
                script = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
                script += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
                script += f'$textNodes = $template.GetElementsByTagName("text");'
                script += f'$textNodes.Item(0).AppendChild($template.CreateTextNode("通知")) > $null;'
                script += f'$textNodes.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null;'
                script += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
                script += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("random-os-fake-legacy-support-alert");'
                script += f'$notifier.Show($toast);'
                subprocess.run(["powershell", "-Command", script], check=True)
        elif system == "Linux":
            subprocess.run(["notify-send", "通知", message], check=True)
        else:
            print(f"[通知] {message}")
    except Exception as e:
        print(f"[通知] {message} (通知送信に失敗: {e})")


def get_random_alert() -> str:
    return random.choice(LEGACY_ALERTS)


def log_alert(message: str):
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {message}\n")
    except Exception:
        pass  # 履歴保存失敗は無視


def list_history(limit: int = 20):
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines[-limit:]:
            print(line.strip())
    except Exception as e:
        print(f"履歴読み込み失敗: {e}")


def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。")
        return
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"通知履歴件数: {len(lines)}")
        recent = lines[-5:] if len(lines) >= 5 else lines
        print("直近の通知:")
        for line in recent:
            print("  " + line.strip())
    except Exception as e:
        print(f"履歴集計失敗: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="謎のレガシーOSサポート終了通知をランダムで表示するスクリプト")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")
    parser_log = subparsers.add_parser("log", help="ランダム通知を発火し履歴に記録")
    parser_list = subparsers.add_parser("list", help="通知履歴を表示")
    parser_list.add_argument("-n", "--num", type=int, default=20, help="表示件数")
    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリを表示")

    args = parser.parse_args()

    if args.command == "log" or args.command is None:
        # 明示呼び出し or デフォルト
        message = get_random_alert()
        send_notification(message)
        log_alert(message)
        print(f"[通知] {message}")
    elif args.command == "list":
        list_history(args.num)
    elif args.command == "summary":
        summary_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
