import sys
import random
import argparse
import platform
import time
from datetime import datetime

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

OS_VERSIONS = [
    '10.0.1-fake', '11.2.9-beta', '13.4.7-fake', 'X.0.0.1-phantom', '2024.06.99-ghost', '9.9.9-myth', '8.1.5-absurd'
]

NEW_FEATURES = [
    'Shiftキー5連打で画面が180度回転します。',
    'Altキー長押しでOSが詩を朗読します。',
    'Ctrlキーの押下速度が基準値未満の場合、全アプリが自動で再起動します。',
    'エクスプローラーで「猫」と入力すると、画面が毛だらけになります。',
    'F1キーでサポートセンターのAIが即座に謎かけを開始します。',
    'PrintScreenで現在の気分がSNSに自動投稿されます。',
    'NumLockを2回押すと、画面が90年代風になります。',
    'InsertキーでOSが自動的に詩を生成します。',
    'Pauseキーで全ウィンドウが一時停止し、BGMが流れます。',
    'ScrollLockで画面がスクロールしながら色が変化します。'
]

FIXES = [
    'CapsLockが押された際、全ウィンドウが詩的に閉じる問題を解決。',
    'タスクバーが時々消える現象を修正。',
    'マウス右クリックでランダムな絵文字が出現する問題を修正。',
    'エクスプローラーで「パッチ」と入力すると再起動する現象を解消。',
    'ダークモードで画面が真っ暗になる問題を修正。',
    'USBメモリを抜くとOSが短歌を詠む問題を修正。',
    '時計が逆回転する現象を修正。',
    'ログイン時にOSが自己紹介を始める問題を修正。',
    'ファイル名に「謎」が含まれると消える現象を修正。',
    'タッチパッド操作で画面が反転する問題を修正。'
]

KNOWN_ISSUES = [
    'マウスホイール逆回転時に天気予報が流れる場合があります。',
    '一部環境でCtrl+Zが未来に移動することがあります。',
    'Alt+TabでOSが詩を朗読し続ける場合があります。',
    'CapsLock点灯時に画面がピンク色になることがあります。',
    'タスクマネージャー起動時にOSが居眠りする場合があります。',
    'NumLock解除時に全アプリが再起動することがあります。',
    'エクスプローラーで「未来」と検索すると時空が歪む場合があります。',
    'ログアウト時にOSが名言を残す場合があります。',
    'ウィンドウ移動時に背景がランダムに変化する場合があります。',
    'サウンド設定で鳥のさえずりが鳴ることがあります。'
]

HEADER = '[Patch Tuesday Alert]'


def generate_patch_note():
    version = random.choice(OS_VERSIONS)
    features = random.sample(NEW_FEATURES, k=random.randint(1, 2))
    fixes = random.sample(FIXES, k=random.randint(1, 2))
    issues = random.sample(KNOWN_ISSUES, k=random.randint(1, 2))
    lines = [HEADER, f'OSバージョン: {version}']
    for f in features:
        lines.append(f'- 新機能: {f}')
    for fix in fixes:
        lines.append(f'- 修正: {fix}')
    for issue in issues:
        lines.append(f'- 既知の問題: {issue}')
    return '\n'.join(lines)


def send_desktop_notification(title, message):
    if not PLYER_AVAILABLE:
        return False
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=7
        )
        return True
    except Exception:
        return False


def print_terminal_alert(note):
    border = '=' * 60
    print(f'\n{border}')
    print(note)
    print(f'{border}\n')


def log_patch_note(note):
    try:
        with open('patch_tuesday_alert.log', 'a', encoding='utf-8') as f:
            f.write(f'[{datetime.now().isoformat()}]\n{note}\n\n')
    except Exception:
        pass


def list_logs():
    try:
        with open('patch_tuesday_alert.log', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('ログファイルが存在しません。')


def summary_logs():
    try:
        with open('patch_tuesday_alert.log', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        count = sum(1 for l in lines if l.startswith('['))
        print(f'過去のパッチ通知回数: {count}')
    except FileNotFoundError:
        print('ログファイルが存在しません。')


def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Patch Tuesday Alert')
    subparsers = parser.add_subparsers(dest='command', help='サブコマンド')
    parser_log = subparsers.add_parser('log', help='パッチ通知を生成して表示')
    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知履歴の件数を表示')
    args = parser.parse_args()

    if args.command == 'log' or args.command is None:
        note = generate_patch_note()
        sent = False
        if PLYER_AVAILABLE and platform.system() in ('Windows', 'Darwin', 'Linux'):
            sent = send_desktop_notification('Patch Tuesday Alert', note.replace('\n', ' '))
        if not sent:
            print_terminal_alert(note)
        log_patch_note(note)
    elif args.command == 'list':
        list_logs()
    elif args.command == 'summary':
        summary_logs()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
