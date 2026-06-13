import sys
import os
import random
import argparse
import platform
import subprocess
import time
from datetime import datetime

BGM_LIST = [
    'なつかしのファミコン効果音',
    '宇宙戦艦発進テーマ',
    '朝礼のチャイム',
    '地下鉄ホームの発車ベル',
    '伝説のボス戦イントロ',
    '昭和のニュース速報ジングル',
    '無人駅の自動アナウンス',
    'カセットテープ逆再生',
    'レトロPCの起動音',
    '体育祭の入場行進曲',
    '昭和アニメのエンディング',
    '校内放送のテスト音声',
    '謎の電子音ループ',
    '古い映画館の幕開けファンファーレ',
    '工場の昼休みサイレン',
    '昭和の電話呼び出し音',
    '駅の発車メロディ',
    '謎のカウントダウン',
    'ラジオ体操第一',
    'デパート閉店の音楽',
    '深夜番組のエンディング',
    'ビル火災避難訓練のアナウンス',
    '古いビデオの巻き戻し音',
    '時報のピッピッポーン',
    '昭和の目覚まし時計',
    'レトロゲームのゲームオーバー',
    '電子レンジの終了音',
    '昔のパチンコ屋BGM',
    'カラオケの予約コール',
    '謎の宇宙通信音'
]

NOTIFY_HISTORY_FILE = os.path.join(os.path.expanduser('~'), '.random_os_soundtrack_notifier_last')


def get_random_bgm_title():
    # 履歴ファイルを読んで直近のBGMを避ける
    last_title = None
    if os.path.exists(NOTIFY_HISTORY_FILE):
        try:
            with open(NOTIFY_HISTORY_FILE, 'r', encoding='utf-8') as f:
                last_title = f.read().strip()
        except Exception:
            last_title = None
    candidates = [t for t in BGM_LIST if t != last_title]
    if not candidates:
        candidates = BGM_LIST
    return random.choice(candidates)


def notify_os(title, message):
    system = platform.system()
    try:
        if system == 'Darwin':  # macOS
            subprocess.run([
                'osascript', '-e', f'display notification "{message}" with title "{title}"'
            ], check=True)
        elif system == 'Linux':
            subprocess.run([
                'notify-send', title, message
            ], check=True)
        elif system == 'Windows':
            # Windows 10 以降のトースト通知 (powershell)
            ps_script = f"""
            [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null
            $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02)
            $textNodes = $template.GetElementsByTagName('text')
            $textNodes.Item(0).AppendChild($template.CreateTextNode('{title}')) > $null
            $textNodes.Item(1).AppendChild($template.CreateTextNode('{message}')) > $null
            $toast = [Windows.UI.Notifications.ToastNotification]::new($template)
            $notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Python Script')
            $notifier.Show($toast)
            """
            subprocess.run([
                'powershell', '-NoProfile', '-Command', ps_script
            ], check=True)
        else:
            print(f"[通知] {title}: {message}")
    except Exception as e:
        print(f"[通知失敗] {title}: {message} ({e})")


def save_last_bgm(title):
    try:
        with open(NOTIFY_HISTORY_FILE, 'w', encoding='utf-8') as f:
            f.write(title)
    except Exception:
        pass


def show_bgm_notification():
    bgm = get_random_bgm_title()
    notify_os('あなたの今日の作業BGM', bgm)
    save_last_bgm(bgm)
    print(f'[通知] あなたの今日の作業BGM: {bgm}')


def list_bgm_titles():
    print('--- BGM候補一覧 ---')
    for i, t in enumerate(BGM_LIST, 1):
        print(f'{i:2d}: {t}')


def show_history():
    if os.path.exists(NOTIFY_HISTORY_FILE):
        try:
            with open(NOTIFY_HISTORY_FILE, 'r', encoding='utf-8') as f:
                last = f.read().strip()
            print(f'前回のBGM通知: {last}')
        except Exception:
            print('履歴の読み込みに失敗しました。')
    else:
        print('まだBGM通知履歴はありません。')


def clear_history():
    if os.path.exists(NOTIFY_HISTORY_FILE):
        try:
            os.remove(NOTIFY_HISTORY_FILE)
            print('BGM通知履歴を削除しました。')
        except Exception:
            print('履歴削除に失敗しました。')
    else:
        print('削除する履歴がありません。')


def main():
    parser = argparse.ArgumentParser(description='random-os-soundtrack-notifier: あなたの今日の作業BGMをランダム通知')
    subparsers = parser.add_subparsers(dest='command')

    parser_notify = subparsers.add_parser('notify', help='ランダムBGMを1回通知')
    parser_list = subparsers.add_parser('list', help='BGMタイトル候補を表示')
    parser_history = subparsers.add_parser('history', help='前回の通知BGMを表示')
    parser_clear = subparsers.add_parser('clear', help='通知履歴を削除')

    # デフォルトはnotify
    if len(sys.argv) == 1:
        show_bgm_notification()
        return

    args = parser.parse_args()
    if args.command == 'notify':
        show_bgm_notification()
    elif args.command == 'list':
        list_bgm_titles()
    elif args.command == 'history':
        show_history()
    elif args.command == 'clear':
        clear_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
