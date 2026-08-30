import sys
import os
import random
import platform
import subprocess
import argparse
import time
from typing import Tuple, List

BOSS_TITLES = [
    'メモリ喰いのバグ魔王',
    'CPUオーバーロード伯爵',
    'SSDトロール',
    '残業魔王',
    'ブルースクリーン大佐',
    'アップデート将軍',
    'ネットワーク断絶王',
    'マウスカースル騎士',
    'ウィンドウズの亡霊',
    'カーネルパニック姫'
]

BOSS_MESSAGES = [
    '緊急任務：今すぐ椅子から立ち上がり、3回ジャンプせよ！',
    '警告：本日は残業魔王が降臨中。集中力を維持できるか？',
    '今すぐストレッチせよ！',
    'あなたの作業は監視されている。',
    '定時退社の夢は幻となった。',
    'USBケーブルが絡まっているぞ。',
    '画面の端に目を向けよ。',
    'コーヒーを淹れる時間だ。',
    '今すぐ深呼吸せよ。',
    '5分間だけ休憩してもよい。'
]

BOSS_PREFIXES = [
    '降臨',
    '出現',
    '警告',
    '襲来',
    '乱入',
    '召喚'
]

TERMINAL_BOSS_FORMAT = 'Mystery Boss: {title}が現れた！「{message}」'


def generate_boss() -> Tuple[str, str, str]:
    title = random.choice(BOSS_TITLES)
    message = random.choice(BOSS_MESSAGES)
    prefix = random.choice(BOSS_PREFIXES)
    return prefix, title, message


def notify_windows(title: str, message: str):
    try:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=7, threaded=True)
    except ImportError:
        # Fallback: PowerShell notification
        script = f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null; "
        script += f"$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02); "
        script += f"$textNodes = $template.GetElementsByTagName('text'); "
        script += f"$textNodes.Item(0).AppendChild($template.CreateTextNode('{title}')) > $null; "
        script += f"$textNodes.Item(1).AppendChild($template.CreateTextNode('{message}')) > $null; "
        script += f"$toast = [Windows.UI.Notifications.ToastNotification]::new($template); "
        script += f"$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('RandomBossPop'); "
        script += f"$notifier.Show($toast);"
        subprocess.Popen(["powershell", "-Command", script], shell=True)


def notify_macos(title: str, message: str):
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])


def notify_linux(title: str, message: str):
    try:
        subprocess.run(["notify-send", title, message])
    except Exception as e:
        print(f"notify-send failed: {e}")


def send_notification(title: str, message: str):
    system = platform.system()
    if system == 'Windows':
        notify_windows(title, message)
    elif system == 'Darwin':
        notify_macos(title, message)
    elif system == 'Linux':
        notify_linux(title, message)
    else:
        print(f"[通知未対応OS] {title}: {message}")


def print_terminal_boss(prefix: str, title: str, message: str):
    print(f"【{prefix}：{title}】\n{message}\n")


def boss_pop(args):
    prefix, title, message = generate_boss()
    full_title = f"{prefix}：{title}"
    print_terminal_boss(prefix, title, message)
    send_notification(full_title, message)


def boss_list(args):
    print("=== ボスキャラ一覧 ===")
    for i, t in enumerate(BOSS_TITLES, 1):
        print(f"{i}. {t}")
    print("\n=== メッセージ例 ===")
    for i, m in enumerate(BOSS_MESSAGES, 1):
        print(f"{i}. {m}")


def boss_summary(args):
    print("このSkillは、OSの通知機能を使ってランダムなボスキャラとメッセージを表示します。\n")
    print(f"対応OS: Windows, macOS, Linux (notify-send)\nボスキャラ数: {len(BOSS_TITLES)}\nメッセージ数: {len(BOSS_MESSAGES)}")


def main():
    parser = argparse.ArgumentParser(description="Random OS Mystery Boss Pop: カオスなボスキャラ通知を表示")
    subparsers = parser.add_subparsers()

    pop_parser = subparsers.add_parser('pop', help='ランダムなボスキャラ通知を表示')
    pop_parser.set_defaults(func=boss_pop)

    list_parser = subparsers.add_parser('list', help='ボスキャラやメッセージ一覧を表示')
    list_parser.set_defaults(func=boss_list)

    summary_parser = subparsers.add_parser('summary', help='Skill概要を表示')
    summary_parser.set_defaults(func=boss_summary)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
