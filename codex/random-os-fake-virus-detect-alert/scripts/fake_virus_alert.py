import sys
import os
import random
import time
import argparse
import platform

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
    '怠惰ウイルス',
    '残業無限増殖型バグウイルス',
    'コーヒー依存症ウイルス',
    '会議無限ループ型ウイルス',
    '進捗ゼロウイルス',
    '無限リファクタリングウイルス',
    '仕様変更感染型ウイルス',
    '無限デバッグウイルス',
    'エナジードリンク依存症ウイルス',
    'タスク増殖型ウイルス',
    'やる気喪失ウイルス',
    '納期爆発ウイルス',
    'ランチ逃亡ウイルス',
    'Slack通知過剰ウイルス',
    'モチベ低下ウイルス',
    'レビュー無限待ちウイルス',
    'リリース延期ウイルス',
    'バグ温存ウイルス',
    '自己肯定感減少ウイルス',
    '仕様未定義ウイルス'
]

FAKE_ALERT_PATTERNS = [
    '謎のウイルス検出: "{name}" がシステムに潜伏中です！',
    '検出: "{name}" (脅威度: {level}) を隔離しました',
    '"{name}" がCPU使用率を上昇させています',
    '"{name}" の駆除に失敗しました',
    '"{name}" が発見されました。至急ご休憩ください',
    '警告: "{name}" の活動を検知しました',
    '"{name}" を削除しました（再発の可能性あり）',
    '"{name}" の感染が拡大中です',
    '"{name}" がメモリを消費しています',
    'システムは "{name}" の影響下にあります'
]

THREAT_LEVELS = ['低', '中', '高', '極低', '注意', '未知']


def pick_fake_alert():
    name = random.choice(FAKE_VIRUS_NAMES)
    pattern = random.choice(FAKE_ALERT_PATTERNS)
    level = random.choice(THREAT_LEVELS)
    return pattern.format(name=name, level=level)


def notify(message):
    system = platform.system()
    if system == 'Windows':
        try:
            toaster = ToastNotifier()
            toaster.show_toast('ウイルス検出アラート', message, duration=8, threaded=True)
        except Exception as e:
            print('[通知失敗] Windows通知APIエラー:', e)
            print('[通知内容]', message)
    elif system == 'Darwin':
        try:
            script = f'display notification "{message}" with title "ウイルス検出アラート"'
            subprocess.run(['osascript', '-e', script], check=True)
        except Exception as e:
            print('[通知失敗] macOS通知APIエラー:', e)
            print('[通知内容]', message)
    else:
        try:
            notify2.init('FakeVirusAlert')
            n = notify2.Notification('ウイルス検出アラート', message)
            n.set_timeout(8000)
            n.show()
        except Exception as e:
            print('[通知失敗] Linux通知APIエラー:', e)
            print('[通知内容]', message)


def trigger_alert():
    alert = pick_fake_alert()
    print(f'[通知] {alert}')
    notify(alert)


def run_periodic_alerts(interval_sec=600, count=None):
    print(f'[INFO] 定期的にジョークウイルスアラートを通知します (間隔: {interval_sec}秒)')
    i = 0
    try:
        while True:
            trigger_alert()
            i += 1
            if count and i >= count:
                break
            time.sleep(interval_sec)
    except KeyboardInterrupt:
        print('\n[INFO] 停止されました')


def list_fake_viruses():
    print('== ジョークウイルス名一覧 ==')
    for v in FAKE_VIRUS_NAMES:
        print('-', v)


def list_patterns():
    print('== 通知パターン一覧 ==')
    for p in FAKE_ALERT_PATTERNS:
        print('-', p.replace('{name}', 'ウイルス名').replace('{level}', '脅威度'))


def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Virus Detect Alert')
    subparsers = parser.add_subparsers(dest='command')

    trigger_parser = subparsers.add_parser('trigger', help='即時でジョークアラートを通知')
    run_parser = subparsers.add_parser('run', help='定期的にジョークアラートを通知')
    run_parser.add_argument('--interval', type=int, default=600, help='通知間隔(秒)')
    run_parser.add_argument('--count', type=int, help='通知回数(指定しない場合は無限)')
    list_parser = subparsers.add_parser('list', help='ジョークウイルス名一覧を表示')
    patterns_parser = subparsers.add_parser('patterns', help='通知パターン一覧を表示')

    args = parser.parse_args()

    if args.command == 'trigger':
        trigger_alert()
    elif args.command == 'run':
        run_periodic_alerts(interval_sec=args.interval, count=args.count)
    elif args.command == 'list':
        list_fake_viruses()
    elif args.command == 'patterns':
        list_patterns()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
