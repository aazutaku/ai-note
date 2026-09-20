import random
import time
import argparse
import sys
import threading
import platform
import subprocess
from typing import List

# 謎のデバイス・機能名リスト
DEVICE_LIST = [
    'Caps Lockキー', 'Ctrlキー', 'Num Lock機能', 'スクロールバー', 'Shiftキー',
    'ターミナルウィンドウの最大化機能', 'Altキー', 'ファイル名自動補完',
    'ウィンドウの影', 'マウスホイール', 'クリップボード履歴',
    '右クリックメニュー', 'タスクバー', 'デスクトップアイコン',
    '仮想デスクトップ', 'ウィンドウスナップ', 'フォントアンチエイリアス',
    'ダークモード', 'サウンドミュート', 'バッテリー残量表示',
    'パスワード入力欄', 'スクリーンショット機能', 'ファイルドラッグ&ドロップ',
    'ネットワークアイコン', 'Bluetooth管理', '画面回転', 'IMEオン/オフ',
    'タッチパッド', '通知センター', 'ウィンドウピン留め', 'エクスプローラ検索'
]

# 謎の警告文テンプレート
TEMPLATE_LIST = [
    'OSライセンス警告: あなたの{device}のライセンスは本日をもって失効しました。再認証が必要です。',
    'システム通知: {device}の試用期間が終了しました。今後は一部機能が制限されます。',
    'OSライセンス警告: {device}の利用権が期限切れとなりました。管理者にお問い合わせください。',
    'システム通知: {device}の年間ライセンスが失効しました。継続利用には更新手続きが必要です。',
    'OSライセンス警告: {device}の認証が切れています。',
    'システム通知: {device}の有効期限が過ぎています。',
    'OSライセンス警告: {device}の利用は本日で終了となります。',
    'システム通知: {device}のアクティベーションが必要です。',
    'OSライセンス警告: {device}の利用が一時的に制限されています。',
    'システム通知: {device}のライセンス状態に問題が発生しました。'
]

# OS通知API呼び出し（macOS, Linux, Windows対応）
def notify_os(title: str, message: str):
    system = platform.system()
    try:
        if system == 'Darwin':  # macOS
            subprocess.run(['osascript', '-e', f'display notification "{message}" with title "{title}"'], check=True)
        elif system == 'Linux':
            subprocess.run(['notify-send', title, message], check=True)
        elif system == 'Windows':
            # Windows 10+ 用 PowerShell通知
            ps_script = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
            ps_script += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
            ps_script += f'$template.GetElementsByTagName("text")[0].AppendChild($template.CreateTextNode("{title}")) > $null;'
            ps_script += f'$template.GetElementsByTagName("text")[1].AppendChild($template.CreateTextNode("{message}")) > $null;'
            ps_script += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
            ps_script += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("FakeLicenseAlert");'
            ps_script += f'$notifier.Show($toast)'
            subprocess.run(['powershell', '-Command', ps_script], check=True)
        else:
            print(f'[ALERT] {title}: {message}')
    except Exception:
        print(f'[ALERT] {title}: {message}')

# 謎の警告文生成
def generate_alert() -> str:
    device = random.choice(DEVICE_LIST)
    template = random.choice(TEMPLATE_LIST)
    return template.format(device=device)

# ターミナル出力
def print_alert(alert: str):
    print(f'[ALERT] {alert}')

# 通知発火
def fire_alert():
    alert = generate_alert()
    print_alert(alert)
    notify_os('OSライセンス警告', alert)

# ランダムなタイミングで繰り返し発火
class RandomAlertThread(threading.Thread):
    def __init__(self, min_interval=60, max_interval=300, max_count=5):
        super().__init__()
        self.min_interval = min_interval
        self.max_interval = max_interval
        self.max_count = max_count
        self._stop_event = threading.Event()

    def run(self):
        count = 0
        while not self._stop_event.is_set() and count < self.max_count:
            wait = random.randint(self.min_interval, self.max_interval)
            time.sleep(wait)
            fire_alert()
            count += 1

    def stop(self):
        self._stop_event.set()

# CLIサブコマンド: log, list, summary（ダミー: 実際のログ保存はしない）
def cli_log(args):
    fire_alert()

def cli_list(args):
    print('--- 最近の謎ライセンス警告例 ---')
    for _ in range(5):
        print_alert(generate_alert())

def cli_summary(args):
    print('このSkillは、作業中に謎のOSライセンス期限切れ警告をランダムに表示します。実害は一切ありません。')

# CLIパーサ
def main():
    parser = argparse.ArgumentParser(description='random-os-fake-mystery-license-alert: 謎のOSライセンス期限切れ通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='今すぐ謎の警告を1件発火')
    parser_log.set_defaults(func=cli_log)

    parser_list = subparsers.add_parser('list', help='警告文例を5件表示')
    parser_list.set_defaults(func=cli_list)

    parser_summary = subparsers.add_parser('summary', help='Skill概要を表示')
    parser_summary.set_defaults(func=cli_summary)

    parser_random = subparsers.add_parser('random', help='ランダムなタイミングで複数回警告を発火')
    parser_random.add_argument('--min', type=int, default=60, help='最小間隔(秒)')
    parser_random.add_argument('--max', type=int, default=300, help='最大間隔(秒)')
    parser_random.add_argument('--count', type=int, default=5, help='最大発火回数')

    args = parser.parse_args()

    if args.command == 'random':
        thread = RandomAlertThread(min_interval=args.min, max_interval=args.max, max_count=args.count)
        thread.start()
        try:
            while thread.is_alive():
                thread.join(1)
        except KeyboardInterrupt:
            thread.stop()
            print('\n[INFO] ランダム警告を中断しました。')
    elif hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
