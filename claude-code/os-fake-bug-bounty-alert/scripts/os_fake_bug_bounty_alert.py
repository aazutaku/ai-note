import random
import argparse
import subprocess
import sys
import platform
import time
from typing import Tuple, List

BUG_TITLES = [
    'Jキー過剰使用バグ',
    '昼寝検出バグ',
    'ショートカットキー同時押し虹色バグ',
    'マウスを1分間動かさないと幻のウィンドウ出現バグ',
    'ターミナルで"ls"を10回連続実行すると謎のメッセージ出現バグ',
    'CapsLock点滅バグ',
    '仮想デスクトップ無限増殖バグ',
    'コーヒーブレイク未検出バグ',
    'ファイル名が"unicorn"だと消えないバグ',
    'スクリーンセーバーが踊りだすバグ',
    'USBメモリ挿入で祝福音バグ',
    'ウィンドウ端が丸くなるバグ',
    'Ctrl+Zで現実世界が一時停止するバグ',
    'タスクバーがジャンプするバグ',
    'エディタが自動で褒めてくるバグ',
    'コマンド入力でAIがジョークを返すバグ',
    '仮想メモリが夢を見るバグ',
    'ネットワーク切断時に猫画像が表示されるバグ',
    'バッテリー残量が増える表示バグ',
    '時計が逆回転するバグ'
]

REWARDS = [
    '1バグポイント進呈',
    '本日限定“虹色エンジニア”称号',
    '3バグポイント + 秘密のバグ修正証明書',
    '“幻のデバッガー”称号',
    '謎のアイテム: デバッグ・キャンディ',
    'バグ修正クーポン券',
    '“昼寝王”の称号',
    '特製バグバウンティ・ステッカー',
    '仮想コーヒーチケット',
    '幻のアップデート通知',
    'バグバウンティ・ギフトボックス',
    'OS非公式称号: バグマスター',
    'バグ発見者限定・秘密のメッセージ',
    '伝説のデバッグバッジ',
    '今日だけ有効なバグ修正パワー',
    '“AIに褒められる権”',
    '謎のバグバウンティ・コイン',
    'デバッグ・エネルギードリンク',
    '仮想世界のバグ修正証',
    'バグバウンティ・メダル'
]

PREFIXES = [
    '発見:',
    '重大:',
    '速報:',
    '新着:',
    '緊急:',
    '注意:',
    'お知らせ:',
    '限定:',
    '祝:',
    '特報:'
]

NOTIFY_TITLE = 'Fake OS Bug Bounty Alert'


def generate_bug_bounty() -> Tuple[str, str]:
    prefix = random.choice(PREFIXES)
    bug = random.choice(BUG_TITLES)
    reward = random.choice(REWARDS)
    return f'{prefix} {bug}', f'報酬: {reward}'


def notify_desktop(title: str, message: str) -> bool:
    system = platform.system()
    try:
        if system == 'Linux':
            subprocess.run(['notify-send', title, message], check=True)
            return True
        elif system == 'Darwin':  # macOS
            osa_script = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', osa_script], check=True)
            return True
        else:
            return False
    except Exception as e:
        return False


def print_terminal(title: str, message: str):
    print(f'[{title}]')
    print(message)


def alert_once():
    bug_msg, reward_msg = generate_bug_bounty()
    notified = notify_desktop(NOTIFY_TITLE, f'{bug_msg}\n{reward_msg}')
    if not notified:
        print_terminal(NOTIFY_TITLE, f'{bug_msg}\n{reward_msg}')


def alert_loop(interval: int, count: int):
    for _ in range(count):
        alert_once()
        time.sleep(interval)


def list_samples(num: int = 5):
    for _ in range(num):
        bug_msg, reward_msg = generate_bug_bounty()
        print(f'[{NOTIFY_TITLE}]')
        print(f'{bug_msg}\n{reward_msg}\n')


def parse_args():
    parser = argparse.ArgumentParser(description='Fake OS Bug Bounty Alert Skill')
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_alert = subparsers.add_parser('alert', help='ランダムなバグバウンティ通知を1回表示')
    parser_alert.add_argument('--loop', type=int, default=0, help='指定回数繰り返し通知')
    parser_alert.add_argument('--interval', type=int, default=10, help='繰り返し時の秒間隔')

    parser_list = subparsers.add_parser('list', help='サンプル通知を複数表示')
    parser_list.add_argument('--num', type=int, default=5, help='表示するサンプル数')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'alert':
        if args.loop > 0:
            alert_loop(args.interval, args.loop)
        else:
            alert_once()
    elif args.command == 'list':
        list_samples(args.num)
    else:
        print('コマンドが不明です')
        sys.exit(1)

if __name__ == '__main__':
    main()
