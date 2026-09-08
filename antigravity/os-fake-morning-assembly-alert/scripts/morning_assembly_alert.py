import os
import sys
import random
import platform
import subprocess
import argparse
import datetime
import json

SLOGANS = [
    'バグは朝のうちに退治せよ',
    '今日も安全第一で開発を',
    'レビューは丁寧に、コミットは小まめに',
    'OS体操でリフレッシュ',
    '朝の一歩が一日を決める',
    '新しい発想は朝礼から',
    'エラーは怖くない、仲間がいる',
    '本日のキーワード: 継続は力なり',
    'コードは人のために書こう',
    '健康第一、バグ第二'
]

CHECKINS = [
    '点呼開始: 1番から順にお名前をどうぞ。',
    '点呼: みなさん、今日も元気ですか？',
    '出席確認: 返事は「はい！」でお願いします。',
    '点呼: 欠席者はいませんか？',
    '点呼: チーム全員の準備OK？'
]

EXERCISES = [
    'OS公式体操のご案内: 10:05より画面端でストレッチ動画を再生します。',
    '体操タイム: 1分間のストレッチを推奨します。',
    'OS体操: みんなで肩回しをしましょう。',
    '体操案内: 立ち上がって深呼吸を3回。',
    '公式体操: 指のストレッチも忘れずに。'
]

GOALS = [
    '本日の作業目標: 「コミットは小まめに、レビューは丁寧に」',
    '本日の作業目標: 「バグゼロを目指しましょう」',
    '本日の作業目標: 「健康第一、無理せず進めよう」',
    '本日の作業目標: 「新しい技術にチャレンジ」',
    '本日の作業目標: 「コードレビューを積極的に」'
]

EXCLUDE_PATHS = ['/tmp', '/var', '/etc', '/bin', '/sbin']

STATE_FILE = os.path.expanduser('~/.os_fake_morning_assembly_state.json')


def already_shown_today():
    today = datetime.date.today().isoformat()
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                data = json.load(f)
                if data.get('date') == today:
                    return True
        except Exception:
            pass
    return False

def mark_shown_today():
    today = datetime.date.today().isoformat()
    data = {'date': today}
    try:
        with open(STATE_FILE, 'w') as f:
            json.dump(data, f)
    except Exception:
        pass

def in_exclude_path():
    cwd = os.path.abspath(os.getcwd())
    for path in EXCLUDE_PATHS:
        if cwd.startswith(path):
            return True
    return False

def random_message():
    slogan = random.choice(SLOGANS)
    checkin = random.choice(CHECKINS)
    exercise = random.choice(EXERCISES)
    goal = random.choice(GOALS)
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    lines = [
        f'[OS朝礼通知] {now}',
        f'本日のスローガン: 「{slogan}」',
        checkin,
        exercise,
        goal
    ]
    return '\n'.join(lines)

def send_notification(message):
    system = platform.system()
    title = 'OS朝礼通知'
    try:
        if system == 'Linux':
            # Use notify-send
            subprocess.run(['notify-send', title, message], check=False)
        elif system == 'Darwin':
            # macOS: use osascript
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', script], check=False)
        elif system == 'Windows':
            # Windows: use PowerShell
            ps_script = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
            ps_script += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
            ps_script += f'$textNodes = $template.GetElementsByTagName("text");'
            ps_script += f'$textNodes.Item(0).AppendChild($template.CreateTextNode("{title}")) > $null;'
            ps_script += f'$textNodes.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null;'
            ps_script += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
            ps_script += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("FakeMorningAssembly");'
            ps_script += f'$notifier.Show($toast);'
            subprocess.run(['powershell', '-Command', ps_script], check=False)
        else:
            # Fallback: print to stdout
            print(message)
    except Exception as e:
        print(f'通知送信エラー: {e}\n{message}', file=sys.stderr)

def cli_show(args):
    if in_exclude_path():
        return
    if already_shown_today():
        return
    msg = random_message()
    send_notification(msg)
    mark_shown_today()
    if args.print:
        print(msg)

def cli_reset(args):
    if os.path.exists(STATE_FILE):
        try:
            os.remove(STATE_FILE)
            print('朝礼通知状態をリセットしました。')
        except Exception as e:
            print(f'リセット失敗: {e}')
    else:
        print('リセット不要: 状態ファイルは存在しません。')

def cli_status(args):
    if already_shown_today():
        print('本日すでに朝礼通知を表示済みです。')
    else:
        print('本日はまだ朝礼通知を表示していません。')

def main():
    parser = argparse.ArgumentParser(description='OS Fake Morning Assembly Alert')
    subparsers = parser.add_subparsers(dest='command')

    show_parser = subparsers.add_parser('show', help='朝礼通知を表示（通常は自動発動）')
    show_parser.add_argument('--print', action='store_true', help='通知内容を標準出力にも表示')
    show_parser.set_defaults(func=cli_show)

    reset_parser = subparsers.add_parser('reset', help='通知状態をリセット')
    reset_parser.set_defaults(func=cli_reset)

    status_parser = subparsers.add_parser('status', help='本日の通知状態を表示')
    status_parser.set_defaults(func=cli_status)

    args = parser.parse_args()
    if not args.command:
        # デフォルトはshow
        args = parser.parse_args(['show'])
    args.func(args)

if __name__ == '__main__':
    main()
