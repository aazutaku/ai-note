import sys
import argparse
import random
import platform
import subprocess
import time
from typing import List

# 通知文テンプレート
TEMPLATES = [
    '警告: あなたのディスク残量は“{unit}”です。至急ご確認ください。',
    '緊急: SSDの空きが“{unit}”にまで減少！宇宙的対策が必要です。',
    '注意: 残り容量は“{unit}”分です。お腹が空きます。',
    '警告: ディスクスペースが“{unit}”レベルで不足中。',
    'アラート: 空きディスク容量が“{unit}”です。',
    '重大: ストレージ残量が“{unit}”しかありません。',
    '警告: ディスク空きが“{unit}”となっています。',
    '警告: あなたのストレージは“{unit}”の危機に瀕しています。',
    '注意: ディスク残量が“{unit}”です。',
    '緊急: ディスクスペースが“{unit}”しかありません。',
]

# 現実離れした単位リスト
UNITS = [
    'カブトムシ2匹分',
    'ギャラクシー級に不足',
    'ラーメンどんぶり0.5杯',
    '時空間のひずみ',
    '18世紀の蒸気機関車1両分',
    'ブラックホールのエッセンス',
    'ネコのヒゲ3本分',
    '量子もつれ状態',
    '宇宙船の燃料タンク1滴分',
    'ピザ1スライス',
    'マシュマロ4個分',
    '無限小',
    'シュレディンガーの猫1匹分',
    'バナナの皮2枚',
    '小惑星帯の砂粒1粒',
    'ペンギンの涙1滴',
    'パンダのくしゃみ1回分',
    '恐竜の卵1個分',
    '宇宙の果ての静寂',
    'カップラーメンのスープ1cc',
]

# OSごとの通知実装

def send_notification(title: str, message: str):
    system = platform.system()
    try:
        if system == 'Darwin':  # macOS
            subprocess.run([
                'osascript',
                '-e', f'display notification "{message}" with title "{title}"'
            ], check=True)
        elif system == 'Linux':
            subprocess.run([
                'notify-send', title, message
            ], check=True)
        elif system == 'Windows':
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=5, threaded=True)
            except ImportError:
                print('[!] win10toastモジュールが必要です: pip install win10toast')
                print(f'{title}: {message}')
        else:
            print(f'{title}: {message}')
    except Exception as e:
        print(f'[通知失敗] {e}')
        print(f'{title}: {message}')

# ランダム通知文生成

def generate_random_message() -> str:
    template = random.choice(TEMPLATES)
    unit = random.choice(UNITS)
    return template.format(unit=unit)

# CLIコマンド実装

def cmd_notify(args):
    msg = generate_random_message()
    send_notification('ディスク残量危機', msg)
    print(f'[通知] {msg}')

def cmd_batch(args):
    count = args.count if args.count > 0 else 5
    interval = args.interval if args.interval > 0 else 3
    for i in range(count):
        msg = generate_random_message()
        send_notification('ディスク残量危機', msg)
        print(f'[{i+1}/{count}] {msg}')
        if i < count - 1:
            time.sleep(interval)

def cmd_list(args):
    print('--- 通知テンプレート ---')
    for t in TEMPLATES:
        print(f'- {t}')
    print('\n--- 単位例 ---')
    for u in UNITS:
        print(f'- {u}')

def cmd_summary(args):
    print('このSkillは、現実離れしたディスク残量危機通知をランダム生成し通知します。')
    print('実際のディスク容量やシステム操作は一切行いません。')
    print('通知内容は完全にフェイクです。')

# メイン関数

def main():
    parser = argparse.ArgumentParser(description='random-os-fake-disk-space-crisis: フェイクなディスク残量危機通知を炸裂させるジョークSkill')
    subparsers = parser.add_subparsers(dest='command')

    # notify
    parser_notify = subparsers.add_parser('notify', help='ランダムな危機通知を1回表示')
    parser_notify.set_defaults(func=cmd_notify)

    # batch
    parser_batch = subparsers.add_parser('batch', help='複数回ランダム通知を連続表示')
    parser_batch.add_argument('--count', type=int, default=5, help='通知回数 (デフォルト5)')
    parser_batch.add_argument('--interval', type=int, default=3, help='通知間隔秒 (デフォルト3)')
    parser_batch.set_defaults(func=cmd_batch)

    # list
    parser_list = subparsers.add_parser('list', help='テンプレートと単位リストを表示')
    parser_list.set_defaults(func=cmd_list)

    # summary
    parser_summary = subparsers.add_parser('summary', help='Skill概要を表示')
    parser_summary.set_defaults(func=cmd_summary)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
