import random
import argparse
import sys
import os
import time
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

BUG_PATTERNS = [
    'CapsLockキーが月曜だけ逆転するバグ',
    '昼寝検出バグ',
    'キーボードのJキー過剰使用バグ',
    'マウスカーソルがランダムに消えるバグ',
    'スクリーンショットがすべて白黒になるバグ',
    'USBポートが「気分」で動作するバグ',
    '本日限定「タスクバー消失」バグ',
    'ファイル名がすべて「謎」になるバグ',
    '音量ミキサーが逆立ちするバグ',
    'エクスプローラーが詩的になるバグ',
    'バッテリー残量が「不明」になるバグ',
    '時計が未来を指すバグ',
    '壁紙が毎時変わるバグ',
    'ウィンドウが勝手に拍手するバグ',
    'ショートカットキーが謎の動作をするバグ',
    '通知音がランダムな楽器音になるバグ',
    'スタートメニューがシャッフルされるバグ',
    'クリップボードが詩を書くバグ',
    'ログイン画面がパズルになるバグ',
    'ファイルが自動でリネームされるバグ'
]

REWARDS = [
    '1バグポイント進呈',
    '伝説の称号「バグハンター」授与',
    '謎のトロフィー',
    '2バグポイント＋昼寝券',
    '3バグポイント',
    '名誉バグ修正者バッジ',
    '1.5バグポイント＋謎の称号',
    '「Jの守護者」称号進呈',
    '睡魔征服者の称号',
    'バグバウンティ限定ステッカー',
    'バグポイント＋開発者の微笑み',
    '謎のバグ図鑑',
    '未知の称号「OSの友」',
    '栄誉あるバグポイント',
    'バグバウンティ祭り参加券',
    '謎のデジタルバッジ'
]

TITLES = [
    '発見',
    '重大',
    '速報',
    '緊急',
    '限定',
    '祝'
]

def generate_alert():
    title = random.choice(TITLES)
    bug = random.choice(BUG_PATTERNS)
    reward = random.choice(REWARDS)
    message = f"{title}: {bug}を修正した方に{reward}。"
    return message

def format_alert():
    alert = generate_alert()
    lines = ["[OS Bug Bounty Alert]", alert]
    return '\n'.join(lines)

def notify_desktop(message):
    if not PLYER_AVAILABLE:
        return False
    try:
        notification.notify(
            title="OS Bug Bounty Alert",
            message=message,
            timeout=8
        )
        return True
    except Exception:
        return False

def log_alert(message, logfile=None):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    entry = f"[{timestamp}] {message}\n"
    if logfile:
        with open(logfile, 'a', encoding='utf-8') as f:
            f.write(entry)
    else:
        sys.stdout.write(entry)


def list_examples(n=5):
    for _ in range(n):
        print(format_alert())
        print()

def summary():
    print("このSkillは完全ランダムな偽バグバウンティ通知を生成し、デスクトップ通知またはターミナルに表示します。通知内容は現実離れしており、実害・データ損失はありません。")


def main():
    parser = argparse.ArgumentParser(description='os-fake-bug-bounty-alert: ランダムな偽バグバウンティ通知を生成します。')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='1件の偽バグバウンティ通知を生成・表示')
    parser_alert.add_argument('--log', type=str, help='通知内容を指定ファイルに追記')
    parser_alert.add_argument('--desktop', action='store_true', help='デスクトップ通知も行う')

    parser_list = subparsers.add_parser('list', help='複数の通知例を表示')
    parser_list.add_argument('-n', type=int, default=5, help='表示件数')

    parser_summary = subparsers.add_parser('summary', help='Skillの概要を表示')

    args = parser.parse_args()

    if args.command == 'alert':
        alert = format_alert()
        print(alert)
        if args.log:
            log_alert(alert, args.log)
        if args.desktop:
            if not notify_desktop(alert):
                print('(デスクトップ通知に失敗しました。plyerパッケージが必要です)')
    elif args.command == 'list':
        list_examples(args.n)
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
