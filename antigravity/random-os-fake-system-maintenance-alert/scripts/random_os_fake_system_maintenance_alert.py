import sys
import os
import random
import argparse
import platform
import subprocess
import time
from typing import List

FAKE_ALERTS = [
    '重要：本日21:00より全システムを逆さまにします。',
    '緊急：マウス左クリック機能が右クリックに統合されます。',
    'ご注意：全ユーザーのパスワードが「password」に初期化されます。',
    '臨時：画面の明るさがランダムに変動します。',
    '予告：全ファイル名がモールス信号表記に変換されます。',
    '速報：Ctrl+Cが無効化されます。',
    '緊急：ターミナルの背景色が1分ごとに変化します。',
    '重要：システム時刻が10分進みます。',
    'ご案内：全ユーザーのデスクトップが共有されます。',
    '臨時：CapsLockが常時オンになります。',
    '予告：すべての通知が英語に変換されます。',
    '重要：本日深夜に全プロセスが自動再起動されます。',
    '緊急：ファイルの拡張子がランダムに変更されます。',
    'ご注意：マウスホイールが逆回転になります。',
    '速報：全ウィンドウが自動で最小化されます。',
    '臨時：すべてのショートカットキーが入れ替わります。',
    '予告：ターミナルのフォントが手書き風になります。',
    '重要：全ユーザーの壁紙が「富士山」に統一されます。',
    '緊急：ログイン画面のBGMが「第九」に変更されます。',
    'ご案内：明日から全員root権限での作業となります。',
    '臨時：全ユーザーのホームディレクトリが一時的に「/tmp」に移動されます。',
    '予告：ファイル検索コマンドが「find」から「seek」に変更されます。',
    '重要：全システムの言語設定がランダム化されます。',
    '緊急：ネットワーク通信がモールス信号で暗号化されます。',
    'ご注意：明日午前中は全ユーザーのアカウント名が入れ替わります。',
    '速報：全アプリケーションが縦書き表示に切り替わります。',
    '臨時：すべてのファイルがzip圧縮されます。',
    '予告：ターミナルのプロンプトが俳句になります。',
    '重要：全ユーザーのパスワードが「12345678」に変更されます。',
    '緊急：全システムの時計が逆回転します。',
]


def pick_random_alerts(n: int = 1) -> List[str]:
    return random.sample(FAKE_ALERTS, k=min(n, len(FAKE_ALERTS)))


def show_terminal_alert(alert: str):
    print(f"[ALERT] {alert}")


def show_desktop_notification(alert: str):
    system = platform.system()
    try:
        if system == "Linux":
            # notify-send is available on most Linux desktops
            subprocess.run([
                "notify-send", "偽システムメンテナンス通知", alert
            ], check=False)
        elif system == "Darwin":
            # macOS notification via AppleScript
            script = f'display notification "{alert}" with title "偽システムメンテナンス通知"'
            subprocess.run([
                "osascript", "-e", script
            ], check=False)
        elif system == "Windows":
            # Windows 10+ notification via powershell
            powershell_script = f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null; " \
                f"$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02); " \
                f"$textNodes = $template.GetElementsByTagName('text'); " \
                f"$textNodes.Item(0).AppendChild($template.CreateTextNode('偽システムメンテナンス通知')) > $null; " \
                f"$textNodes.Item(1).AppendChild($template.CreateTextNode('{alert}')) > $null; " \
                f"$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('FakeMaintenance'); " \
                f"$notification = [Windows.UI.Notifications.ToastNotification]::new($template); " \
                f"$notifier.Show($notification);"
            subprocess.run(["powershell", "-Command", powershell_script], check=False)
        else:
            show_terminal_alert(alert)
    except Exception as e:
        show_terminal_alert(alert)


def show_alert(alert: str, mode: str = "auto"):
    if mode == "desktop":
        show_desktop_notification(alert)
    elif mode == "terminal":
        show_terminal_alert(alert)
    elif mode == "auto":
        if sys.stdout.isatty():
            show_terminal_alert(alert)
        else:
            show_desktop_notification(alert)
    else:
        show_terminal_alert(alert)


def list_alerts():
    for i, alert in enumerate(FAKE_ALERTS, 1):
        print(f"{i:2d}: {alert}")


def summary():
    print(f"登録済み偽メンテナンス通知数: {len(FAKE_ALERTS)}")
    print("例:")
    for alert in pick_random_alerts(3):
        print(f"  - {alert}")


def main():
    parser = argparse.ArgumentParser(
        description='謎のOSシステムメンテナンス予告通知をランダム表示するスクリプト')
    subparsers = parser.add_subparsers(dest='command', help='サブコマンド')

    parser_alert = subparsers.add_parser('alert', help='ランダムな偽メンテナンス通知を表示')
    parser_alert.add_argument('-n', '--number', type=int, default=1, help='通知数 (デフォルト: 1)')
    parser_alert.add_argument('--mode', choices=['auto', 'desktop', 'terminal'], default='auto', help='通知方法')
    parser_alert.add_argument('--interval', type=float, default=0, help='複数通知時の間隔(秒)')

    parser_list = subparsers.add_parser('list', help='登録済み通知一覧を表示')

    parser_summary = subparsers.add_parser('summary', help='通知数や例を表示')

    args = parser.parse_args()

    if args.command == 'alert':
        alerts = pick_random_alerts(args.number)
        for i, alert in enumerate(alerts):
            show_alert(alert, mode=args.mode)
            if args.interval > 0 and i < len(alerts) - 1:
                time.sleep(args.interval)
    elif args.command == 'list':
        list_alerts()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
