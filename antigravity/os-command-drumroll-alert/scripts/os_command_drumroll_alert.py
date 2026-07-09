import sys
import os
import argparse
import platform
import random
import subprocess
import tempfile
import threading
import time

try:
    from plyer import notification
except ImportError:
    notification = None

DRUMROLL_SOUNDS = [
    'https://cdn.pixabay.com/audio/2022/10/16/audio_12b5c8c7e8.mp3',
    'https://cdn.pixabay.com/audio/2022/10/16/audio_120d7a3b83.mp3',
    'https://cdn.pixabay.com/audio/2022/10/16/audio_12b5c8c7e8.mp3'
]

ALERT_MESSAGES = [
    '運命の選択が迫る！本当に実行しますか？',
    '今から本当にやるのか？',
    '重大操作直前！覚悟はできていますか？',
    'Drumroll... Are you sure you want to proceed?',
    'このコマンド、後戻りできません！'
]

TRIGGER_KEYWORDS = [
    'git push',
    'rm -rf',
    'npm publish',
    'docker system prune',
    'systemctl restart',
    'kubectl delete',
    'gcloud compute instances delete',
    'terraform apply',
    'aws s3 rm',
    'chmod 777',
    'chown',
    'shutdown',
    'reboot',
    'dd if=',
    'mkfs',
    'diskutil eraseDisk'
]

def download_sound(url):
    import urllib.request
    fd, path = tempfile.mkstemp(suffix='.mp3')
    os.close(fd)
    urllib.request.urlretrieve(url, path)
    return path

def play_sound(path):
    sysname = platform.system()
    if sysname == 'Darwin':
        subprocess.Popen(['afplay', path])
    elif sysname == 'Linux':
        subprocess.Popen(['mpg123', path])
    elif sysname == 'Windows':
        subprocess.Popen(['powershell', '-c', f'(New-Object Media.SoundPlayer "{path}").PlaySync();'])
    else:
        print('サウンド再生未対応OSです')

def show_notification(title, message):
    sysname = platform.system()
    if notification:
        notification.notify(title=title, message=message, timeout=5)
    elif sysname == 'Darwin':
        subprocess.Popen(['osascript', '-e', f'display notification "{message}" with title "{title}"'])
    elif sysname == 'Linux':
        subprocess.Popen(['notify-send', title, message])
    elif sysname == 'Windows':
        subprocess.Popen(['powershell', '-Command', f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null; $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02); $textNodes = $template.GetElementsByTagName("text"); $textNodes.Item(0).AppendChild($template.CreateTextNode("{title}")) > $null; $textNodes.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null; $toast = [Windows.UI.Notifications.ToastNotification]::new($template); [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("os-command-drumroll-alert").Show($toast);'])
    else:
        print(f'通知未対応OS: {title} {message}')

def drumroll_alert(command):
    msg = random.choice(ALERT_MESSAGES)
    sound_url = random.choice(DRUMROLL_SOUNDS)
    print(f'[ドラムロール音が鳴る]')
    print(f'[デスクトップ通知] {msg} {command}')
    print(f'[ターミナル出力] Drumroll... Are you sure you want to proceed with "{command}"?')
    # Download and play sound in background
    path = download_sound(sound_url)
    t = threading.Thread(target=play_sound, args=(path,))
    t.start()
    show_notification('重大コマンド警告', f'{msg} {command}')
    # 簡易的なYes/Noプロンプト
    while True:
        ans = input('実行しますか？ [y/N]: ')
        if ans.lower() in ['y', 'yes']:
            return True
        elif ans.lower() in ['', 'n', 'no']:
            print('キャンセルされました')
            return False
        else:
            print('y または n を入力してください')

def is_major_command(cmd):
    for kw in TRIGGER_KEYWORDS:
        if kw in cmd:
            return True
    return False

def run_command(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f'コマンド失敗: {e}')

def main():
    parser = argparse.ArgumentParser(description='os-command-drumroll-alert')
    parser.add_argument('command', nargs=argparse.REMAINDER, help='実行するコマンド')
    parser.add_argument('--list-keywords', action='store_true', help='重大コマンドキーワード一覧を表示')
    args = parser.parse_args()

    if args.list_keywords:
        print('重大コマンドキーワード:')
        for kw in TRIGGER_KEYWORDS:
            print(f'- {kw}')
        sys.exit(0)

    if not args.command:
        print('コマンドを指定してください')
        sys.exit(1)

    cmd_str = ' '.join(args.command)
    if is_major_command(cmd_str):
        proceed = drumroll_alert(cmd_str)
        if not proceed:
            sys.exit(0)
    run_command(cmd_str)

if __name__ == '__main__':
    main()
