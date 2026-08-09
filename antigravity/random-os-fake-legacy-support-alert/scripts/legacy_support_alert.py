import sys
import os
import random
import argparse
import platform
import time

try:
    if platform.system() == 'Linux':
        import notify2
    elif platform.system() == 'Windows':
        from win10toast import ToastNotifier
    elif platform.system() == 'Darwin':
        import subprocess
    else:
        notify2 = None
except ImportError:
    notify2 = None

LEGACY_ALERTS = [
    "98互換モードのサポートは2024年6月30日をもって終了しました。",
    "IE6向け最適化機能は永遠に封印されました。",
    "フロッピーディスク対応APIが静かに旅立ちました。",
    "MS-DOSバッチファイル自動補完は伝説となりました。",
    "Netscape Navigator対応パッチの配布は終了しました。",
    "Windows Meのエラー報告機能は静かに消えました。",
    "ActiveXコントロールのサポートは本日をもって終了です。",
    "BASICインタプリタの自動起動は歴史の彼方へ。",
    "SCSI外付けMOドライブ対応が完全終了しました。",
    "Lotus 1-2-3連携APIの提供は終了しました。",
    "Y2K対応パッチのメンテナンスは打ち切られました。",
    "Windows 2000のセーフモード起動支援は廃止されました。",
    "テレホーダイ自動切替サービスはご利用いただけません。",
    "IE5.5向けCSSハックは封印されました。",
    "フロッピーディスクの自動マウント機能は伝説となりました。",
    "MSN Messenger連携APIは消滅しました。",
    "VGA16色モードのサポートは打ち切られました。",
    "PC-9801互換BIOSのサポートが終了しました。",
    "Windows XPのLunaテーマ互換性は完全に失われました。",
    "ZIPドライブ自動認識は歴史の彼方へ。"
]

LOG_FILE = os.path.expanduser("~/.legacy_support_alert.log")


def send_notification(message):
    system = platform.system()
    if system == 'Linux' and 'notify2' in sys.modules:
        notify2.init("Legacy Support Alert")
        n = notify2.Notification("サポート終了通知", message)
        n.show()
    elif system == 'Windows':
        try:
            toaster = ToastNotifier()
            toaster.show_toast("サポート終了通知", message, duration=5, threaded=True)
        except Exception:
            print(f"[サポート終了通知] {message}")
    elif system == 'Darwin':
        try:
            subprocess.run(["osascript", "-e", f'display notification "{message}" with title "サポート終了通知"'], check=True)
        except Exception:
            print(f"[サポート終了通知] {message}")
    else:
        print(f"[サポート終了通知] {message}")


def log_alert(message):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")


def random_alert():
    message = random.choice(LEGACY_ALERTS)
    send_notification(message)
    log_alert(message)
    return message


def list_alerts():
    for i, msg in enumerate(LEGACY_ALERTS, 1):
        print(f"{i:2d}: {msg}")


def show_log():
    if not os.path.exists(LOG_FILE):
        print("通知ログはまだありません。")
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        print(f.read())


def summary():
    if not os.path.exists(LOG_FILE):
        print("通知ログはまだありません。")
        return
    counts = {}
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            for msg in LEGACY_ALERTS:
                if msg in line:
                    counts[msg] = counts.get(msg, 0) + 1
    print("== 通知内容ごとの発生回数 ==")
    for msg, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{cnt:3d}回: {msg}")


def main():
    parser = argparse.ArgumentParser(description="謎のレガシーOSサポート終了通知をランダム表示")
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='通知ログを表示')
    parser_list = subparsers.add_parser('list', help='通知メッセージ一覧')
    parser_summary = subparsers.add_parser('summary', help='通知内容ごとの発生回数')
    parser_alert = subparsers.add_parser('alert', help='ランダム通知を即時発火')

    args = parser.parse_args()

    if args.command == 'log':
        show_log()
    elif args.command == 'list':
        list_alerts()
    elif args.command == 'summary':
        summary()
    elif args.command == 'alert' or args.command is None:
        msg = random_alert()
        print(f"[サポート終了通知] {msg}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
