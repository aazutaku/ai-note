import argparse
import subprocess
import sys
import random
import platform
import threading
import time

try:
    from plyer import notification
except ImportError:
    notification = None

EXCUSES = [
    '猫がキーボードを踏みました',
    '宇宙線がビットをひっくり返しました',
    '運命のせいです',
    '今日は水星逆行です',
    'AIの気まぐれです',
    'ネットワークの妖精が悪さをしました',
    'コーヒーが足りません',
    'コードの神様が休暇中です',
    '机の上のホコリが原因です',
    '月の引力の影響です',
    '時間軸がずれました',
    'サーバの気分が乗りません',
    '開発者のせいではありません',
    '電子の流れが逆でした',
    '世界線が違いました'
]

HISTORY = []


def send_notification(title, message):
    if notification is not None:
        try:
            notification.notify(title=title, message=message, timeout=5)
        except Exception as e:
            print(f'[通知失敗] {e}', file=sys.stderr)
    else:
        # Fallback: print to stderr
        print(f'[通知] {title}: {message}', file=sys.stderr)


def run_command(cmd_args):
    """指定コマンドを実行し、失敗時に言い訳通知を送る"""
    try:
        proc = subprocess.run(cmd_args, capture_output=True, text=True)
        stdout, stderr = proc.stdout, proc.stderr
        if proc.returncode != 0:
            excuse = random.choice(EXCUSES)
            send_notification('言い訳', excuse)
            HISTORY.append({'cmd': ' '.join(cmd_args), 'excuse': excuse, 'rc': proc.returncode, 'stderr': stderr.strip(), 'time': time.time()})
            sys.stderr.write(stderr)
            sys.exit(proc.returncode)
        else:
            sys.stdout.write(stdout)
    except FileNotFoundError as e:
        excuse = random.choice(EXCUSES)
        send_notification('言い訳', excuse)
        HISTORY.append({'cmd': ' '.join(cmd_args), 'excuse': excuse, 'rc': 127, 'stderr': str(e), 'time': time.time()})
        print(f'command not found: {cmd_args[0]}', file=sys.stderr)
        sys.exit(127)
    except Exception as e:
        excuse = random.choice(EXCUSES)
        send_notification('言い訳', excuse)
        HISTORY.append({'cmd': ' '.join(cmd_args), 'excuse': excuse, 'rc': 1, 'stderr': str(e), 'time': time.time()})
        print(f'error: {e}', file=sys.stderr)
        sys.exit(1)


def list_history():
    if not HISTORY:
        print('通知履歴はありません')
        return
    for idx, item in enumerate(HISTORY):
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item['time']))
        print(f"[{idx+1}] {t} コマンド: {item['cmd']} | 言い訳: {item['excuse']} | RC: {item['rc']}")
        if item['stderr']:
            print(f"  エラー: {item['stderr']}")


def summary():
    print(f'通知回数: {len(HISTORY)}')
    if HISTORY:
        reasons = {}
        for h in HISTORY:
            reasons[h['excuse']] = reasons.get(h['excuse'], 0) + 1
        print('言い訳ランキング:')
        for excuse, count in sorted(reasons.items(), key=lambda x: -x[1]):
            print(f'  {excuse}: {count}回')


def main():
    parser = argparse.ArgumentParser(description='コマンド失敗時に言い訳を通知するツール')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='コマンドを実行し、失敗時に言い訳通知')
    parser_run.add_argument('cmd', nargs=argparse.REMAINDER, help='実行するコマンド')

    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知履歴のサマリー')

    args = parser.parse_args()

    if args.command == 'run':
        if not args.cmd:
            print('コマンドを指定してください', file=sys.stderr)
            sys.exit(2)
        run_command(args.cmd)
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
