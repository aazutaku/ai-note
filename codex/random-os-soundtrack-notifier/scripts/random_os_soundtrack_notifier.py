import sys
import os
import random
import platform
import subprocess
import argparse
from typing import List

SOUNDTRACKS = [
    '情熱大陸',
    '運命（ベートーヴェン）',
    '初音ミクの消失',
    'ドラクエ戦闘曲',
    '朝のラジオ体操 第一',
    'NHKニュースのテーマ',
    '笑点のテーマ',
    'サザエさんのエンディング',
    'ファミマ入店音',
    'マリオの地下BGM',
    'エヴァンゲリオン「残酷な天使のテーゼ」',
    'ポケモンセンターBGM',
    '水戸黄門のテーマ',
    'ドラえもんのうた',
    'ルパン三世のテーマ',
    'ゴジラのテーマ',
    'パチンコ屋の開店音',
    '運動会の徒競走BGM',
    'ピタゴラスイッチのテーマ',
    '仮面ライダー変身音',
    'サクラ大戦「檄!帝国華撃団」',
    'カノン（パッヘルベル）',
    '千本桜',
    '世界の車窓から',
    '暴れん坊将軍のテーマ',
    'プリキュアのオープニング',
    'アニメ「けいおん!」OP',
    'スーパー戦隊シリーズOP',
    'モンスターハンター村BGM',
    'ウルトラマンのテーマ',
    '天空の城ラピュタ「君をのせて」',
    '銀河鉄道999',
    'ヤマト発進音',
    'タモリ倶楽部OP',
    'バイオリン協奏曲第1番',
    'インベーダーゲームBGM',
    'ボレロ（ラヴェル）',
    'アナ雪「Let It Go」',
    'ロッキーのテーマ',
    '北の国から',
    '徹子の部屋のテーマ',
    'MOTHER「Pollyanna」',
    'カービィのグリーングリーンズ',
    'ゼルダの伝説メインテーマ',
    'FFファンファーレ',
    'ペルソナ5「Life Will Change」',
    'テトリスBGM',
    'パワプロサクセスBGM',
    'ニコニコ動画「組曲」',
    'ドラゴンボール「摩訶不思議アドベンチャー」'
]


def select_random_soundtrack() -> str:
    return random.choice(SOUNDTRACKS)


def notify_mac(title: str, message: str):
    script = f'display notification "{message}" with title "{title}"'
    try:
        subprocess.run(['osascript', '-e', script], check=True)
    except Exception as e:
        print(f"[ERROR] macOS通知失敗: {e}")


def notify_linux(title: str, message: str):
    try:
        subprocess.run(['notify-send', title, message], check=True)
    except Exception as e:
        print(f"[ERROR] Linux通知失敗: {e}")


def notify_windows(title: str, message: str):
    try:
        import win10toast
        toaster = win10toast.ToastNotifier()
        toaster.show_toast(title, message, duration=5)
    except ImportError:
        # fallback: powershell toast
        ps_script = f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null; " \
                    f"$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02); " \
                    f"$textNodes = $template.GetElementsByTagName('text'); " \
                    f"$textNodes.Item(0).AppendChild($template.CreateTextNode('{title}')) > $null; " \
                    f"$textNodes.Item(1).AppendChild($template.CreateTextNode('{message}')) > $null; " \
                    f"$toast = [Windows.UI.Notifications.ToastNotification]::new($template); " \
                    f"$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Python Script'); " \
                    f"$notifier.Show($toast)"
        try:
            subprocess.run(['powershell', '-Command', ps_script], check=True)
        except Exception as e:
            print(f"[ERROR] Windows通知失敗: {e}")
    except Exception as e:
        print(f"[ERROR] Windows通知失敗: {e}")


def notify(title: str, message: str):
    system = platform.system()
    if system == 'Darwin':
        notify_mac(title, message)
    elif system == 'Linux':
        notify_linux(title, message)
    elif system == 'Windows':
        notify_windows(title, message)
    else:
        print(f"[通知] {title}: {message}")


def list_soundtracks():
    print("== ランダムBGM候補一覧 ==")
    for i, track in enumerate(SOUNDTRACKS, 1):
        print(f"{i}. {track}")


def main():
    parser = argparse.ArgumentParser(description='random-os-soundtrack-notifier: 理不尽なBGM通知スキル')
    subparsers = parser.add_subparsers(dest='command', help='サブコマンド')

    parser_notify = subparsers.add_parser('notify', help='ランダムBGMを通知')
    parser_notify.add_argument('--dry-run', action='store_true', help='通知せずに内容だけ表示')

    parser_list = subparsers.add_parser('list', help='BGM候補一覧を表示')

    parser_sample = subparsers.add_parser('sample', help='擬似通知出力例を表示')
    parser_sample.add_argument('--count', type=int, default=5, help='例の数')

    args = parser.parse_args()

    if args.command == 'notify' or args.command is None:
        track = select_random_soundtrack()
        title = '今日の作業BGM'
        message = f'『{track}』'
        if hasattr(args, 'dry_run') and args.dry_run:
            print(f"[通知] {title}: {message}")
        else:
            notify(title, message)
    elif args.command == 'list':
        list_soundtracks()
    elif args.command == 'sample':
        for _ in range(args.count):
            track = select_random_soundtrack()
            print(f"[通知] 今日の作業BGM: 『{track}』")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
