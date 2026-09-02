import sys
import random
import time
import argparse
import threading
import platform

try:
    if platform.system() == 'Linux':
        import notify2
    elif platform.system() == 'Windows':
        from win10toast import ToastNotifier
    elif platform.system() == 'Darwin':
        import subprocess
    else:
        notify2 = None
except ImportError:
    notify2 = None

def get_random_alert():
    titles = [
        '重大', '警告', '注意', 'アラート', '通知', 'OS公式', 'システム', 'Error', 'Critical'
    ]
    bodies = [
        'OSメモリリーク警告: システムメモリがどこかに消えました。',
        '記憶領域が流出しています。至急対応してください。',
        'あなたのやる気メモリもリークしています。',
        'メモリリーク検出: 0xDEADBEEF番地に異常発生。',
        '仮想メモリが現実逃避を始めました。',
        'RAMがRAMENになりました。',
        'プロセスが記憶を失いました。',
        'OSが自分の存在を疑い始めました。',
        '記憶領域がブラックホール化しています。',
        'メモリバンクが夢の国へ旅立ちました。',
        'システムのやる気が0%になりました。',
        '警告: メモリがどこかでパーティー中。',
        'エラー: メモリが現実逃避を決意しました。',
        '注意: 仮想メモリが物理的に疲弊しています。',
        'メモリリーク: 物理法則が崩壊しました。'
    ]
    title = random.choice(titles)
    body = random.choice(bodies)
    return title, body

def send_notification(title, message):
    system = platform.system()
    if system == 'Linux' and notify2:
        notify2.init('FakeMemoryLeakAlert')
        n = notify2.Notification(title, message)
        n.set_urgency(notify2.URGENCY_CRITICAL)
        n.show()
    elif system == 'Windows':
        try:
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=5, threaded=True)
        except Exception as e:
            print(f"[通知失敗] {e}")
    elif system == 'Darwin':
        try:
            subprocess.run([
                'osascript', '-e',
                f'display notification "{message}" with title "{title}"'
            ])
        except Exception as e:
            print(f"[通知失敗] {e}")
    else:
        print(f"[{title}] {message}")

def alert_once():
    title, msg = get_random_alert()
    send_notification(title, msg)

def alert_loop(interval, count):
    for _ in range(count):
        alert_once()
        time.sleep(interval)

def list_alerts():
    print("--- フェイクメモリリーク通知例 ---")
    for _ in range(10):
        title, msg = get_random_alert()
        print(f"[{title}] {msg}")

def summary():
    print("このSkillは、OSメモリリークを模したフェイク通知をランダムに生成し、ユーザーの画面に表示します。実際のシステムには一切影響を与えません。\n")
    print("サポートOS: Linux (notify2), Windows (win10toast), macOS (osascript)\n")
    print("通知例:")
    list_alerts()

def parse_args():
    parser = argparse.ArgumentParser(description='Fake OS Memory Leak Alert Skill')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='1回だけフェイクアラートを表示')
    parser_loop = subparsers.add_parser('loop', help='N回フェイクアラートを表示')
    parser_loop.add_argument('--interval', type=int, default=10, help='通知間隔(秒)')
    parser_loop.add_argument('--count', type=int, default=5, help='通知回数')
    parser_list = subparsers.add_parser('list', help='通知例を10件表示')
    parser_summary = subparsers.add_parser('summary', help='Skill概要と通知例を表示')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'alert':
        alert_once()
    elif args.command == 'loop':
        alert_loop(args.interval, args.count)
    elif args.command == 'list':
        list_alerts()
    elif args.command == 'summary':
        summary()
    else:
        print("コマンドを指定してください: alert | loop | list | summary")

if __name__ == '__main__':
    main()
