import argparse
import random
import sys
import time
import platform
import subprocess
from datetime import datetime

FAKE_FEATURES = [
    'スタートメニューに“謎のボタン”を追加',
    'カレンダーに猫の日を自動登録',
    'バッテリー残量が減るとBGMが流れる機能',
    '壁紙が1分ごとにランダムで90年代風に変化',
    'コマンドプロンプトに「こんにちは」と返す隠し機能',
    'ウィンドウを閉じるときに「本当に閉じますか？」を10回表示',
    'デスクトップアイコンが時々踊る',
    '未使用のUSBポートに「ご苦労さま」と通知',
    'ランダムでマウスポインタが逆さまに',
    'エラー音が「ピコーン」から「ポヨーン」に変更'
]

FAKE_BUGFIXES = [
    'たまに現れる幽霊プロセスをさらに不可視化',
    '未確認のバグをさらに未確認化',
    'メモ帳が勝手に閉じる問題を再現できませんでした',
    'スクリーンセーバーが起動しない時、代わりに何もしないように修正',
    '右クリックが左クリックになることがある問題を未解決のまま放置',
    'アップデート通知が重複表示される問題を3倍に増加',
    'ログイン画面のヒントを謎の暗号に変更',
    '「ファイルが見つかりません」エラーをもっと丁寧に表示',
    '再起動時に時々「お疲れさま」と表示',
    'タスクバーが消える問題を見なかったことに'
]

FAKE_KNOWN_ISSUES = [
    'アップデート後も何も変わらない場合があります',
    '通知がたまに英語になります',
    'ごく稀に通知が2回表示されることがあります',
    'このアップデートは実際には存在しません',
    '一部の機能は想像上のものです',
    '通知内容が理解不能な場合があります',
    'バージョン番号に意味はありません',
    'アップデート後に再起動してもしなくても変わりません',
    '通知が消えない場合はそっとしておいてください',
    'この通知を信じないでください'
]

FAKE_VERSIONS = [
    '13.4.9-fake', '2024.06.01-beta', 'XP-NextGen', '11.0.0-joke', '0.9.99-mock', '3.1415-pi', '42.0.0', '1.2.3.4.5', '22H2-prank', 'v0.0.0-fun']


def generate_fake_update():
    version = random.choice(FAKE_VERSIONS)
    features = random.sample(FAKE_FEATURES, k=2)
    bugfixes = random.sample(FAKE_BUGFIXES, k=2)
    known_issues = random.sample(FAKE_KNOWN_ISSUES, k=1)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lines = [
        '[OSアップデート通知]',
        f'バージョン: {version}',
        f'日時: {timestamp}',
        f'- 新機能: {features[0]}',
        f'- 新機能: {features[1]}',
        f'- バグ修正: {bugfixes[0]}',
        f'- バグ修正: {bugfixes[1]}',
        f'- 既知の問題: {known_issues[0]}',
        '（この通知はジョークです）'
    ]
    return '\n'.join(lines)


def show_notification(message):
    system = platform.system()
    try:
        if system == 'Darwin':
            subprocess.run([
                'osascript', '-e', f'display notification "{message}" with title "Fake OS Update"'
            ], check=True)
        elif system == 'Linux':
            subprocess.run([
                'notify-send', 'Fake OS Update', message
            ], check=True)
        elif system == 'Windows':
            # Use Toast notification via powershell
            ps_script = f"""
            [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null
            $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02)
            $textNodes = $template.GetElementsByTagName('text')
            $textNodes.Item(0).AppendChild($template.CreateTextNode('Fake OS Update')) > $null
            $textNodes.Item(1).AppendChild($template.CreateTextNode('{message}')) > $null
            $toast = [Windows.UI.Notifications.ToastNotification]::new($template)
            $notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('FakeOSUpdate')
            $notifier.Show($toast)
            """
            subprocess.run([
                'powershell', '-Command', ps_script
            ], check=True)
        else:
            print(message)
    except Exception as e:
        print(f"通知の表示に失敗しました: {e}\n内容:\n{message}")


def notify():
    msg = generate_fake_update()
    show_notification(msg)
    print(msg)


def list_samples():
    print('--- サンプル通知 ---')
    for _ in range(3):
        print(generate_fake_update())
        print('----------------------')


def summary():
    print('このSkillは、架空のOSアップデート通知をランダムに生成し、デスクトップ通知として表示します。通知内容は完全なジョークで、実際のシステムには影響しません。')


def main():
    parser = argparse.ArgumentParser(description='random-os-fake-update-notifier')
    subparsers = parser.add_subparsers(dest='command')

    notify_parser = subparsers.add_parser('notify', help='ランダムなOSアップデート通知を表示')
    list_parser = subparsers.add_parser('list', help='サンプル通知を3件表示')
    summary_parser = subparsers.add_parser('summary', help='Skillの概要を表示')

    args = parser.parse_args()
    if args.command == 'notify':
        notify()
    elif args.command == 'list':
        list_samples()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
