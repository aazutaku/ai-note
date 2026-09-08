import os
import sys
import random
import argparse
from datetime import datetime
import platform
import subprocess

STATE_FILE = os.path.expanduser('~/.os_fake_morning_assembly_alert_state')

SLOGANS = [
    'エラーは友達、バグは宝',
    '今日も一日、ノーコンパイルエラー',
    'OSは裏切らない',
    'デバッグは朝飯前',
    'コードレビューは愛のムチ',
    'コミットは一日一善',
    'リファクタリングは未来への投資',
    'テストカバレッジ90%超を目指せ',
    'バグ報告は感謝の証',
    '仕様は生き物、変化を恐れるな'
]

CHECKINS = [
    '1番、2番、3番...全員いるか？',
    '点呼開始！名前を呼ばれたら「はい」と返事してください',
    '全員集合！今日も元気に開発スタート',
    'リーダーから順に自己紹介をどうぞ',
    '出席確認：欠席者はSlackで連絡'
]

EXERCISES = [
    '画面の前で背筋を伸ばしてください',
    'OS公式体操：手首ストレッチをどうぞ',
    '深呼吸してリフレッシュしましょう',
    '目を閉じて10秒間リラックス',
    '椅子から立ち上がって軽く屈伸'
]

GOALS = [
    'テストカバレッジ90%超を目指しましょう',
    '未解決バグを3件減らしましょう',
    'ドキュメントを1ページ更新しましょう',
    'レビュー待ちのPRを全て確認しましょう',
    '今日の新規バグゼロを目指しましょう'
]

NOTIF_TEMPLATES = [
    '[OS朝礼通知] 本日のスローガン: "{slogan}"',
    '[点呼開始] {checkin}',
    '[OS公式体操] {exercise}',
    '[作業目標] 本日は「{goal}」'
]

def is_first_run():
    if not os.path.exists(STATE_FILE):
        return True
    try:
        with open(STATE_FILE, 'r') as f:
            last_date = f.read().strip()
        today = datetime.now().strftime('%Y-%m-%d')
        return last_date != today
    except Exception:
        return True

def update_state():
    try:
        with open(STATE_FILE, 'w') as f:
            f.write(datetime.now().strftime('%Y-%m-%d'))
    except Exception:
        pass

def random_assembly_messages():
    slogan = random.choice(SLOGANS)
    checkin = random.choice(CHECKINS)
    exercise = random.choice(EXERCISES)
    goal = random.choice(GOALS)
    messages = [
        NOTIF_TEMPLATES[0].format(slogan=slogan),
        NOTIF_TEMPLATES[1].format(checkin=checkin),
        NOTIF_TEMPLATES[2].format(exercise=exercise),
        NOTIF_TEMPLATES[3].format(goal=goal)
    ]
    # シャッフルして2-4件出す
    random.shuffle(messages)
    n = random.randint(2, 4)
    return messages[:n]

def notify_desktop(message):
    sysname = platform.system()
    try:
        if sysname == 'Darwin':
            subprocess.run(['osascript', '-e', f'display notification "{message}" with title "OS朝礼通知"'], check=True)
        elif sysname == 'Linux':
            subprocess.run(['notify-send', 'OS朝礼通知', message], check=True)
        elif sysname == 'Windows':
            # Windows 10以降: powershell経由
            ps = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
            ps += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
            ps += f'$textNodes = $template.GetElementsByTagName("text");$textNodes.Item(0).AppendChild($template.CreateTextNode("OS朝礼通知")) > $null;'
            ps += f'$textNodes.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null;'
            ps += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
            ps += f'[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("FakeMorningAssembly").Show($toast)'
            subprocess.run(['powershell', '-Command', ps], check=True)
        else:
            print(message)
    except Exception:
        print(message)

def show_assembly_alert():
    messages = random_assembly_messages()
    for msg in messages:
        print(msg)
        notify_desktop(msg)


def main():
    parser = argparse.ArgumentParser(description='OS Fake Morning Assembly Alert')
    parser.add_argument('command', nargs='?', default='auto', choices=['auto', 'alert', 'reset', 'show', 'help'],
                        help='auto:初回のみ発動, alert:毎回発動, reset:状態リセット, show:今日の通知, help:使い方')
    args = parser.parse_args()

    if args.command == 'help':
        print('''\nOS Fake Morning Assembly Alert\n\nコマンド例:\n  python os_fake_morning_assembly_alert.py auto   # 初回のみ発動\n  python os_fake_morning_assembly_alert.py alert  # 毎回通知\n  python os_fake_morning_assembly_alert.py reset  # 状態リセット\n  python os_fake_morning_assembly_alert.py show   # 今日の通知内容を再表示\n''')
        return
    if args.command == 'reset':
        if os.path.exists(STATE_FILE):
            os.remove(STATE_FILE)
        print('状態ファイルをリセットしました')
        return
    if args.command == 'show':
        if not os.path.exists(STATE_FILE):
            print('今日の通知はまだありません')
            return
        today = datetime.now().strftime('%Y-%m-%d')
        with open(STATE_FILE, 'r') as f:
            last_date = f.read().strip()
        if last_date != today:
            print('今日の通知はまだありません')
            return
        # 再度ランダム生成（同じ内容にはなりません）
        show_assembly_alert()
        return
    if args.command == 'alert':
        show_assembly_alert()
        update_state()
        return
    # auto
    if is_first_run():
        show_assembly_alert()
        update_state()
    else:
        pass  # 2回目以降は何もしない

if __name__ == '__main__':
    main()
