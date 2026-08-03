import sys
import os
import random
import time
import platform
import argparse
from threading import Thread

try:
    if platform.system() == 'Windows':
        from win10toast import ToastNotifier
    elif platform.system() == 'Darwin':
        import subprocess
    else:
        import notify2
except ImportError:
    pass

FAKE_VIRUS_NAMES = [
    ('怠惰ウイルス', 'Sloth.Trojan.Lazy-2024'),
    ('残業無限増殖型バグウイルス', 'Overwork.Bug.InfiniteLoop'),
    ('コーヒー依存症ウイルス', 'Coffee.Addict.Worm'),
    ('会議無限ループウイルス', 'Meeting.Loop.Infinite'),
    ('やる気喪失型ウイルス', 'Motivation.Dropper.Zero'),
    ('昼寝推進ウイルス', 'Nap.Promotion.Agent'),
    ('タスク逃避型ウイルス', 'Task.Evasion.Trojan'),
    ('納期遅延ウイルス', 'Deadline.Lag.Backdoor'),
    ('ネットサーフィン誘導ウイルス', 'Surfing.Redirector.Fun'),
    ('集中力散漫ウイルス', 'Focus.Disruptor.Random'),
    ('おやつタイム強制ウイルス', 'Snack.Time.Injector'),
    ('進捗ゼロウイルス', 'NoProgress.Null.Agent'),
    ('仕様変更拡散ウイルス', 'SpecChange.Spreader'),
    ('バグ自己増殖ウイルス', 'Bug.SelfReplicator'),
    ('リファクタリング無限地獄ウイルス', 'Refactor.InfiniteHell')
]

FAKE_LEVELS = [
    ('超低', 'コーヒーを飲んでください'),
    ('無害', '休憩を推奨します'),
    ('注意', '深呼吸しましょう'),
    ('警戒', '一度立ち上がってストレッチ')
]

OS_NAMES = {
    'Windows': 'Windows 10',
    'Darwin': 'macOS Ventura',
    'Linux': 'Ubuntu 22.04'
}

def get_os_name():
    sys_os = platform.system()
    return OS_NAMES.get(sys_os, sys_os)

def random_alert():
    virus_jp, virus_en = random.choice(FAKE_VIRUS_NAMES)
    level, action = random.choice(FAKE_LEVELS)
    os_name = get_os_name()
    alert_title = 'ウイルス検出アラート'
    alert_msg = f'OS: {os_name}\n検出ウイルス: {virus_jp} ({virus_en})\n脅威レベル: {level}\n対策: {action}'
    return alert_title, alert_msg

def send_notification(title, message):
    sys_os = platform.system()
    if sys_os == 'Windows':
        try:
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=8, threaded=True)
        except Exception as e:
            print(f'[通知失敗] {e}')
    elif sys_os == 'Darwin':
        try:
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script])
        except Exception as e:
            print(f'[通知失敗] {e}')
    else:
        try:
            notify2.init('FakeVirusAlert')
            n = notify2.Notification(title, message)
            n.set_urgency(notify2.URGENCY_LOW)
            n.show()
        except Exception as e:
            print(f'[通知失敗] {e}')

def alert_loop(interval, count, dry_run=False):
    for i in range(count):
        title, msg = random_alert()
        if dry_run:
            print(f'[{title}]\n{msg}\n')
        else:
            send_notification(title, msg)
        time.sleep(interval)

def list_viruses():
    print('--- 登録済みフェイクウイルス一覧 ---')
    for vjp, ven in FAKE_VIRUS_NAMES:
        print(f'{vjp} ({ven})')

def summary():
    print('フェイクウイルス検出アラート Skill 概要:')
    print(f'登録ウイルス数: {len(FAKE_VIRUS_NAMES)}')
    print(f'通知レベル数: {len(FAKE_LEVELS)}')
    print('対応OS:', ', '.join(OS_NAMES.values()))
    print('通知方式: OS標準通知API')

def parse_args():
    parser = argparse.ArgumentParser(description='謎のOSウイルス検出アラートをランダム表示するSkill')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='ランダムにウイルス検出アラートを表示')
    parser_log.add_argument('--interval', type=int, default=60, help='通知間隔(秒)')
    parser_log.add_argument('--count', type=int, default=3, help='通知回数')
    parser_log.add_argument('--dry-run', action='store_true', help='通知をコンソール出力のみ')

    subparsers.add_parser('list', help='登録済みフェイクウイルス一覧を表示')
    subparsers.add_parser('summary', help='Skillの概要を表示')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'log':
        alert_loop(args.interval, args.count, args.dry_run)
    elif args.command == 'list':
        list_viruses()
    elif args.command == 'summary':
        summary()
    else:
        print('サブコマンドを指定してください (log/list/summary)')

if __name__ == '__main__':
    main()
