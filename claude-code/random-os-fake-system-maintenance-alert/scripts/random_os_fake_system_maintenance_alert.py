import sys
import argparse
import random
import datetime
import platform
import os

# 通知メッセージテンプレート
ALERT_TEMPLATES = [
    "重要：本日{time}より全システムを逆さまにします。",
    "緊急：マウス左クリック機能が右クリックに統合されます。",
    "全端末の画面表示を縦書きに切り替えます。",
    "明日午前2時から全ユーザーのパスワードが『password』にリセットされます。",
    "本日深夜、マウスカーソルが常に逃げ続けるモードに移行します。",
    "全ファイル名がランダムな絵文字に変換されます。",
    "重要：全システムで『Ctrl+Z』が『シャットダウン』に割り当てられます。",
    "ご案内：本日{time}より全ユーザーのデスクトップ画像が社長の顔写真に変更されます。",
    "緊急：明日から全アプリがコマンドライン専用になります。",
    "重要：全システムの言語設定がラテン語に変更されます。",
    "本日{time}より全端末の時計が逆回転モードになります。",
    "全ユーザーのログイン名がランダムな数字列に変更されます。",
    "本日{time}から全ての通知音が『ピヨピヨ』に統一されます。",
    "全システムのマウスカーソルが1.5倍速で移動します。",
    "全ユーザーのホームディレクトリが『/tmp』に移動されます。"
]

PREFIXES = [
    "[OSメンテナンス通知]",
    "[システム保守案内]",
    "[重要なお知らせ]",
    "[緊急メンテナンス]",
    "[ご案内]"
]

# 通知内容をランダム生成
def generate_alert():
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M")
    template = random.choice(ALERT_TEMPLATES)
    prefix = random.choice(PREFIXES)
    # テンプレートに {time} が含まれていれば置換
    message = template.replace("{time}", time_str)
    return f"{prefix} {message}"

# 複数件生成
def generate_alerts(count=1):
    alerts = []
    for _ in range(count):
        alerts.append(generate_alert())
    return alerts

# OS別通知表示 (クロスプラットフォーム)
def show_notification(message):
    sys_platform = platform.system()
    try:
        if sys_platform == "Darwin":
            # macOS: AppleScript 経由で通知
            os.system(f'''osascript -e 'display notification "{message}" with title "Fake OS Maintenance"' ''')
        elif sys_platform == "Linux":
            # Linux: notify-send (要インストール)
            os.system(f'notify-send "Fake OS Maintenance" "{message}"')
        elif sys_platform == "Windows":
            # Windows: powershell 経由で通知
            powershell_cmd = (
                f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
                f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
                f'$textNodes = $template.GetElementsByTagName("text");'
                f'$textNodes.Item(0).AppendChild($template.CreateTextNode("Fake OS Maintenance")) > $null;'
                f'$textNodes.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null;'
                f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
                f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("Fake OS Maintenance");'
                f'$notifier.Show($toast);'
            )
            os.system(f'powershell -Command "{powershell_cmd}"')
        else:
            # 未対応OSは標準出力
            print(message)
    except Exception as e:
        print(f"通知エラー: {e}")
        print(message)

# CLIサブコマンド定義
def main():
    parser = argparse.ArgumentParser(description="ランダムな偽OSシステムメンテナンス通知を表示します。")
    subparsers = parser.add_subparsers(dest="command")

    # log: 通知を1件生成して表示
    parser_log = subparsers.add_parser("log", help="ランダム通知を1件表示")
    parser_log.add_argument("-n", "--number", type=int, default=1, help="通知件数 (デフォルト:1)")
    parser_log.add_argument("--silent", action="store_true", help="通知を標準出力のみに表示")

    # list: 通知を複数件生成して出力
    parser_list = subparsers.add_parser("list", help="ランダム通知を複数件生成して一覧表示")
    parser_list.add_argument("-n", "--number", type=int, default=5, help="通知件数 (デフォルト:5)")

    # summary: テンプレート一覧
    parser_summary = subparsers.add_parser("summary", help="利用可能な通知テンプレート一覧を表示")

    args = parser.parse_args()

    if args.command == "log":
        alerts = generate_alerts(args.number)
        for alert in alerts:
            if args.silent:
                print(alert)
            else:
                show_notification(alert)
                print(alert)
    elif args.command == "list":
        alerts = generate_alerts(args.number)
        for alert in alerts:
            print(alert)
    elif args.command == "summary":
        print("利用可能な通知テンプレート:")
        for i, temp in enumerate(ALERT_TEMPLATES, 1):
            print(f"{i:2d}. {temp}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
