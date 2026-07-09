import sys
import os
import argparse
import random
import subprocess
import platform
import time
from pathlib import Path

try:
    from playsound import playsound
except ImportError:
    playsound = None

# 通知メッセージのバリエーション
NOTIFY_MESSAGES = [
    '今から本当に "{cmd}" を実行しますか？',
    '運命の選択が迫る！',
    'ドラマチックな瞬間に突入します。',
    'この操作は取り消せません。',
    '心の準備はできていますか？',
    '重大なコマンドが検出されました。',
    'あなたの選択が未来を変えるかもしれません。',
    'エンジニアの運命を賭けた一手！',
    '緊張のドラムロールが鳴り響く…',
    'さあ、運命の実行ボタンを押しましょう。'
]

# 重大コマンドリスト
CRITICAL_COMMANDS = [
    'git push', 'rm ', 'rm -rf', 'npm publish', 'docker push', 'gcloud app deploy',
    'kubectl delete', 'terraform apply', 'aws s3 rm', 'az webapp deploy', 'scp ', 'rsync '
]

# ドラムロール音ファイル（WAV/MP3）
DRUMROLL_SOUNDS = [
    str(Path(__file__).parent / 'sounds/drumroll1.wav'),
    str(Path(__file__).parent / 'sounds/drumroll2.wav'),
    str(Path(__file__).parent / 'sounds/drumroll3.wav')
]


def is_critical_command(cmdline):
    for kw in CRITICAL_COMMANDS:
        if cmdline.strip().startswith(kw):
            return True
    return False


def play_drumroll():
    # 環境変数で無効化可
    if os.environ.get('DRUMROLL_ALERT_SOUND', '1') != '1':
        return
    sound_file = random.choice(DRUMROLL_SOUNDS)
    if not Path(sound_file).exists():
        print(f"[WARN] ドラムロール音ファイルが見つかりません: {sound_file}")
        return
    if playsound:
        try:
            playsound(sound_file)
        except Exception as e:
            print(f"[WARN] ドラムロール音再生失敗: {e}")
    else:
        # fallback: OS標準プレイヤー
        if platform.system() == 'Darwin':
            subprocess.run(['afplay', sound_file])
        elif platform.system() == 'Windows':
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{sound_file}").PlaySync();'])
        else:
            subprocess.run(['aplay', sound_file])


def send_notification(title, message):
    # 環境変数で無効化可
    if os.environ.get('DRUMROLL_ALERT_NOTIFY', '1') != '1':
        return
    sys_os = platform.system()
    if sys_os == 'Darwin':
        script = f'display notification "{message}" with title "{title}"'
        subprocess.run(['osascript', '-e', script])
    elif sys_os == 'Linux':
        subprocess.run(['notify-send', title, message])
    elif sys_os == 'Windows':
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(title, message, duration=5)
        except ImportError:
            # fallback: powershell
            ps_script = f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime];"
            ps_script += f"$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);"
            ps_script += f"$toastXml = $template;"
            ps_script += f"$toastXml.GetElementsByTagName('text')[0].AppendChild($toastXml.CreateTextNode('{title}')) | Out-Null;"
            ps_script += f"$toastXml.GetElementsByTagName('text')[1].AppendChild($toastXml.CreateTextNode('{message}')) | Out-Null;"
            ps_script += f"$toast = [Windows.UI.Notifications.ToastNotification]::new($toastXml);"
            ps_script += f"[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('DrumrollAlert').Show($toast);"
            subprocess.run(['powershell', '-Command', ps_script])
    else:
        print(f"[通知] {title}: {message}")


def drumroll_alert(cmdline):
    print("[INFO] 重大コマンド検知: ドラムロール演出を開始します。")
    play_drumroll()
    for i in range(2):
        msg = random.choice(NOTIFY_MESSAGES).format(cmd=cmdline)
        send_notification("Drumroll Alert", msg)
        time.sleep(1)
    time.sleep(1)
    print(f"[INFO] コマンド \"{cmdline}\" を実行します。")


def main():
    parser = argparse.ArgumentParser(description='重大コマンド直前にドラムロールと通知で演出するスキル')
    parser.add_argument('command', nargs=argparse.REMAINDER, help='実行予定のコマンド')
    parser.add_argument('--dry-run', action='store_true', help='コマンド実行はせず演出だけ行う')
    parser.add_argument('--list-critical', action='store_true', help='重大コマンドリストを表示')
    parser.add_argument('--test-notify', action='store_true', help='通知テスト')
    parser.add_argument('--test-sound', action='store_true', help='ドラムロール音テスト')
    args = parser.parse_args()

    if args.list_critical:
        print("重大コマンド一覧:")
        for cmd in CRITICAL_COMMANDS:
            print(f"  - {cmd}")
        sys.exit(0)
    if args.test_notify:
        send_notification("Drumroll Alert", "これは通知テストです。")
        sys.exit(0)
    if args.test_sound:
        play_drumroll()
        sys.exit(0)
    if not args.command:
        print("[ERROR] コマンドを指定してください。例: drumroll_alert.py git push")
        sys.exit(1)
    cmdline = ' '.join(args.command)
    if is_critical_command(cmdline):
        drumroll_alert(cmdline)
    else:
        print(f"[INFO] 通常コマンド: {cmdline}")
    if not args.dry_run:
        try:
            subprocess.run(args.command)
        except Exception as e:
            print(f"[ERROR] コマンド実行失敗: {e}")

if __name__ == '__main__':
    main()
