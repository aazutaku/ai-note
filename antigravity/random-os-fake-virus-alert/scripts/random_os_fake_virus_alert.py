import sys
import os
import time
import random
import argparse
import platform
import subprocess
from threading import Thread

# --- 通知メッセージ集 ---
FAKE_ALERTS = [
    {
        'title': '危険：未知のバグウイルスを検出！',
        'body': 'あなたのコードが自我を持ち始めました。直ちにコーヒーを補給してください。'
    },
    {
        'title': '注意：OSがAIに乗っ取られました',
        'body': 'これは冗談です。作業の合間に深呼吸しましょう。'
    },
    {
        'title': '警告：メモリ内に謎の“やる気ウイルス”',
        'body': '影響はありません。気分転換にストレッチをおすすめします。'
    },
    {
        'title': 'システム警告：バグ感染の疑い',
        'body': '実害ゼロ。作業の手を止めて一息つきましょう。'
    },
    {
        'title': 'ウイルス警告：デバッグ魂感染',
        'body': 'この通知はジョークです。引き続き健全な開発を！'
    },
    {
        'title': '注意：コードが夜更かしを始めました',
        'body': 'そろそろ休憩しませんか？'
    },
    {
        'title': '警告：AIバグ検出',
        'body': 'この警告はフィクションです。安心して作業を続けてください。'
    },
    {
        'title': '危険：未知のやる気ウイルス',
        'body': '副作用：突然の集中力上昇。ジョーク通知です。'
    },
    {
        'title': '警告：OSが冗談モードに移行',
        'body': '今だけの限定通知。深呼吸してリフレッシュ！'
    },
    {
        'title': '注意：システムが笑いを検出',
        'body': 'この通知は本物ではありません。安心してください。'
    }
]

# --- OSごとの通知関数 ---
def notify_windows(title, body):
    try:
        import win10toast
        toaster = win10toast.ToastNotifier()
        toaster.show_toast(title, body, duration=6, threaded=True)
    except ImportError:
        # fallback: powershell
        ps_command = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
        ps_command += f'$template = [Windows.UI.Notifications.ToastTemplateType]::ToastText02;'
        ps_command += f'$xml = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent($template);'
        ps_command += f'$textNodes = $xml.GetElementsByTagName("text");'
        ps_command += f'$textNodes.Item(0).AppendChild($xml.CreateTextNode("{title}")) > $null;'
        ps_command += f'$textNodes.Item(1).AppendChild($xml.CreateTextNode("{body}")) > $null;'
        ps_command += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($xml);'
        ps_command += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("FakeVirusAlert");'
        ps_command += f'$notifier.Show($toast);'
        subprocess.run(["powershell", "-Command", ps_command], shell=True)


def notify_macos(title, body):
    script = f'display notification "{body}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])


def notify_linux(title, body):
    try:
        subprocess.run(["notify-send", title, body])
    except Exception as e:
        print(f"[通知失敗] {e}")


def show_notification(title, body):
    sys_platform = platform.system()
    if sys_platform == 'Windows':
        notify_windows(title, body)
    elif sys_platform == 'Darwin':
        notify_macos(title, body)
    elif sys_platform == 'Linux':
        notify_linux(title, body)
    else:
        print(f"[通知] {title}: {body}")


def random_alert():
    alert = random.choice(FAKE_ALERTS)
    show_notification(alert['title'], alert['body'])


def alert_loop(min_interval=900, max_interval=2700, once=False):
    """
    min_interval, max_interval: 秒単位。15〜45分の間隔でランダム通知。
    once: Trueなら1回だけ通知。
    """
    if once:
        random_alert()
        return
    while True:
        wait = random.randint(min_interval, max_interval)
        time.sleep(wait)
        random_alert()


def list_alerts():
    print("--- サンプル通知一覧 ---")
    for i, alert in enumerate(FAKE_ALERTS):
        print(f"{i+1}. {alert['title']}\n   {alert['body']}\n")


def main():
    parser = argparse.ArgumentParser(description='完全ネタのOSウイルスアラート通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_once = subparsers.add_parser('once', help='1回だけ通知を表示')
    parser_loop = subparsers.add_parser('loop', help='ランダム間隔で通知を繰り返し表示')
    parser_loop.add_argument('--min', type=int, default=900, help='通知間隔(秒)の最小値(デフォルト900)')
    parser_loop.add_argument('--max', type=int, default=2700, help='通知間隔(秒)の最大値(デフォルト2700)')
    parser_list = subparsers.add_parser('list', help='通知メッセージ一覧を表示')

    args = parser.parse_args()
    if args.command == 'once':
        random_alert()
    elif args.command == 'loop':
        try:
            alert_loop(min_interval=args.min, max_interval=args.max)
        except KeyboardInterrupt:
            print("\n[終了] 通知ループを停止しました。")
    elif args.command == 'list':
        list_alerts()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
