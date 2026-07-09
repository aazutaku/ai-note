import os
import sys
import random
import argparse
import platform
import subprocess
import threading
import time

DRUMROLL_SOUNDS = [
    'drumroll1.wav',
    'drumroll2.wav',
    'drumroll3.wav'
]

NOTIFY_MESSAGES = [
    '今から「{cmd}」を実行します。本当に進めますか？',
    '運命の選択が迫る！',
    '重大コマンド発動。覚悟はできていますか？',
    'この一手が未来を変えるかも…',
    '慎重に、今が分岐点です。',
    'ドラムロール…運命の瞬間が近づいています！'
]

MAJOR_COMMANDS = [
    'git push', 'rm', 'rm -rf', 'npm publish', 'docker push', 'kubectl apply', 'terraform apply', 'systemctl restart', 'chmod 777', 'chown', 'mv', 'cp', 'sudo', 'make install'
]


def play_sound(sound_file):
    sys_os = platform.system()
    if not os.path.exists(sound_file):
        print(f'[WARN] サウンドファイル {sound_file} が見つかりません')
        return
    try:
        if sys_os == 'Darwin':
            subprocess.run(['afplay', sound_file], check=True)
        elif sys_os == 'Linux':
            # aplay or paplay
            if subprocess.call(['which', 'paplay'], stdout=subprocess.DEVNULL) == 0:
                subprocess.run(['paplay', sound_file], check=True)
            else:
                subprocess.run(['aplay', sound_file], check=True)
        elif sys_os == 'Windows':
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{sound_file}").PlaySync();'], check=True)
        else:
            print('[WARN] 未対応OSのためサウンド再生をスキップ')
    except Exception as e:
        print(f'[ERROR] サウンド再生失敗: {e}')

def send_notification(title, message):
    sys_os = platform.system()
    try:
        if sys_os == 'Darwin':
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', script], check=True)
        elif sys_os == 'Linux':
            subprocess.run(['notify-send', title, message], check=True)
        elif sys_os == 'Windows':
            # Windows 10+ Toast通知
            ps_script = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
            ps_script += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
            ps_script += f'$textNodes = $template.GetElementsByTagName("text");'
            ps_script += f'$textNodes.Item(0).AppendChild($template.CreateTextNode("{title}")) > $null;'
            ps_script += f'$textNodes.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null;'
            ps_script += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
            ps_script += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("Python Script");'
            ps_script += f'$notifier.Show($toast);'
            subprocess.run(["powershell", "-Command", ps_script], check=True)
        else:
            print('[WARN] 未対応OSのため通知をスキップ')
    except Exception as e:
        print(f'[ERROR] 通知送信失敗: {e}')

def random_drumroll():
    return random.choice(DRUMROLL_SOUNDS)

def random_notify(cmd):
    msg = random.choice(NOTIFY_MESSAGES)
    return msg.format(cmd=cmd)

def is_major_command(cmd):
    for major in MAJOR_COMMANDS:
        if cmd.strip().startswith(major):
            return True
    return False

def drumroll_alert(cmd):
    print('[DRUMROLL] ドラムロール再生中...')
    sound_file = random_drumroll()
    # サウンド再生は別スレッドで
    t = threading.Thread(target=play_sound, args=(sound_file,))
    t.start()
    notify_msg = random_notify(cmd)
    send_notification('Drumroll Alert', notify_msg)
    print(f'[NOTIFY] {notify_msg}')
    t.join()
    print('[DRUMROLL] ドラムロール終了！')
    # 追加通知
    notify_msg2 = random_notify(cmd)
    send_notification('Drumroll Alert', notify_msg2)
    print(f'[NOTIFY] {notify_msg2}')
    print(f'[INFO] コマンド「{cmd}」を続行してください。')

def cli():
    parser = argparse.ArgumentParser(description='重大コマンド直前にドラムロール演出と通知を発動')
    parser.add_argument('--command', '-c', type=str, required=True, help='実行予定のコマンド名')
    parser.add_argument('--force', action='store_true', help='重大コマンド以外でも強制発動')
    args = parser.parse_args()
    cmd = args.command.strip()
    if is_major_command(cmd) or args.force:
        drumroll_alert(cmd)
    else:
        print(f'[INFO] コマンド「{cmd}」は重大コマンドではないため演出をスキップします')

def main():
    cli()

if __name__ == '__main__':
    main()
