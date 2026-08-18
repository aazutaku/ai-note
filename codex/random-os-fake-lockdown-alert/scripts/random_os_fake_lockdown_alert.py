import sys
import argparse
import random
import datetime
import platform
import subprocess
from typing import List

REASONS = [
    "カフェイン摂取量が閾値を超過",
    "キーボード過熱検知",
    "マウスクリック過多による自動防御",
    "OSが自律的にストライキを宣言",
    "AIによる過剰監視を感知",
    "定期的な非日常イベント発動",
    "コーヒーブレイク未取得",
    "ファイル名に禁止ワード検出",
    "ランダムな量子ゆらぎ発生",
    "オペレータの集中力がピーク",
    "ディスプレイ輝度が謎の閾値到達"
]

TARGETS = [
    "全ユーザーディレクトリ",
    "本日作成された全ファイル",
    "デスクトップフォルダ",
    "全プロセス",
    "USBデバイス",
    "開いている全ターミナル",
    "ネットワーク接続",
    "全ウィンドウ",
    "仮想メモリ領域",
    "一時ファイル",
    "全アプリケーション"
]

UNLOCKS = [
    "深呼吸を5回行ってください",
    "画面を3回タップしてください",
    "キーボードのスペースキーを2秒間長押し",
    "コーヒーを一口飲んでください",
    "好きな曲を1分間再生",
    "椅子から立ち上がってストレッチ",
    "目を閉じて10秒カウント",
    "となりの人に挨拶する",
    "OSに優しく話しかける",
    "何もせず30秒待つ"
]

TITLES = [
    "緊急OSロックダウン通知",
    "謎のシステム凍結警告",
    "ファイルアクセス一時停止アラート",
    "全プロセス一時封鎖宣言",
    "AI発令: 予防的ロックダウン",
    "オペレータ混乱防止モード発動"
]

NOTES = [
    "この通知は実際の操作には影響しません",
    "ご安心ください、ファイルは安全です",
    "本通知はジョークです。",
    "現実の環境には一切影響しません",
    "解除方法はあくまで参考です"
]


def generate_alert() -> str:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    title = random.choice(TITLES)
    target = random.choice(TARGETS)
    reason = random.choice(REASONS)
    unlock = random.choice(UNLOCKS)
    note = random.choice(NOTES)
    alert = f"=== {title} ===\n"
    alert += f"発令時刻: {now}\n"
    alert += f"対象: {target}\n"
    alert += f"理由: {reason}\n"
    alert += f"解除方法: {unlock}\n"
    alert += f"備考: {note}\n"
    return alert


def print_alert():
    alert = generate_alert()
    print(alert)


def send_desktop_notification(alert: str):
    os_name = platform.system()
    title = alert.split('\n')[0].replace('=', '').strip()
    body = '\n'.join(alert.split('\n')[1:]).strip()
    try:
        if os_name == 'Linux':
            subprocess.run([
                'notify-send', title, body
            ], check=True)
        elif os_name == 'Darwin':
            # macOS
            script = f'display notification "{body}" with title "{title}"'
            subprocess.run(['osascript', '-e', script], check=True)
        elif os_name == 'Windows':
            # Windows 10+ (requires ToastNotifier)
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, body, duration=8)
            except ImportError:
                print("win10toastが見つかりません。標準出力のみで通知します。")
                print(alert)
        else:
            print(alert)
    except Exception as e:
        print(f"通知の送信に失敗しました: {e}")
        print(alert)


def list_examples(n=3):
    for _ in range(n):
        print(generate_alert())
        print('-' * 40)


def main():
    parser = argparse.ArgumentParser(
        description='謎のOSロックダウン通知をランダムに生成・表示します。'
    )
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='ランダムな通知を標準出力に表示')
    parser_alert.add_argument('--desktop', action='store_true', help='デスクトップ通知も送る')

    parser_list = subparsers.add_parser('list', help='サンプル通知を複数表示')
    parser_list.add_argument('-n', type=int, default=3, help='表示する通知数')

    args = parser.parse_args()

    if args.command == 'alert':
        alert = generate_alert()
        print(alert)
        if args.desktop:
            send_desktop_notification(alert)
    elif args.command == 'list':
        list_examples(args.n)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
