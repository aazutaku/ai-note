import random
import time
import argparse
import sys
import os
from threading import Thread

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

FAKE_COMMANDS = [
    "make coffee --now",
    "deploy to mars",
    "brew install unicorn",
    "sudo teleport /dev/brain mars:",
    "rm -rf bad_vibes/",
    "git push origin imagination",
    "chmod +x /dev/dreams",
    "ls /parallel_universe",
    "cat /etc/telepathy.conf",
    "systemctl restart universe",
    "curl https://matrix.os/awakening",
    "python3 -m time_travel",
    "npm install --global enlightenment",
    "docker run -it reality:latest",
    "ssh user@multiverse",
    "echo 'hello from the other side'",
    "scp consciousness.tar.gz mind:/tmp/",
    "sudo apt-get install happiness",
    "export PATH=$PATH:/usr/local/telepathy",
    "killall bad_thoughts"
]

ALERT_PATTERNS = [
    "あなたが心の中で考えたコマンドを検出しました：'{cmd}'",
    "念波検出：'{cmd}'",
    "OSがあなたの妄想コマンドを察知しました：'{cmd}'",
    "思念コマンド受信：'{cmd}'",
    "テレパシーコマンド検出：'{cmd}'",
    "読心術モード発動：'{cmd}'が浮かびました",
    "OSがあなたの脳内コマンドをキャッチ：'{cmd}'"
]

LOG_FILE = os.path.expanduser("~/.telepathic_command_alert.log")


def generate_alert():
    cmd = random.choice(FAKE_COMMANDS)
    pattern = random.choice(ALERT_PATTERNS)
    message = pattern.format(cmd=cmd)
    return message


def show_notification(message):
    if PLYER_AVAILABLE:
        notification.notify(
            title="Telepathic OS Alert",
            message=message,
            app_name="TelepathicCommandAlert",
            timeout=8
        )
    else:
        # Fallback: print to stderr
        print(f"[Telepathic OS Alert] {message}", file=sys.stderr)


def log_alert(message):
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {message}\n")
    except Exception as e:
        pass  # Ignore logging errors


def alert_loop(interval_min=600, interval_max=1800, once=False):
    while True:
        message = generate_alert()
        show_notification(message)
        log_alert(message)
        if once:
            break
        sleep_time = random.randint(interval_min, interval_max)
        time.sleep(sleep_time)


def list_alerts(limit=10):
    if not os.path.exists(LOG_FILE):
        print("No alerts logged yet.")
        return
    with open(LOG_FILE, encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines[-limit:]:
        print(line.strip())


def summary_alerts():
    if not os.path.exists(LOG_FILE):
        print("No alerts logged yet.")
        return
    with open(LOG_FILE, encoding='utf-8') as f:
        lines = f.readlines()
    print(f"Total alerts: {len(lines)}")
    if lines:
        print(f"First alert: {lines[0].strip()}")
        print(f"Last alert: {lines[-1].strip()}")


def parse_args():
    parser = argparse.ArgumentParser(description="Telepathic OS Fake Command Alert")
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_run = subparsers.add_parser('run', help='Start random telepathic alerts (default)')
    parser_run.add_argument('--interval-min', type=int, default=600, help='Minimum interval between alerts (sec)')
    parser_run.add_argument('--interval-max', type=int, default=1800, help='Maximum interval between alerts (sec)')
    parser_run.add_argument('--once', action='store_true', help='Show only one alert and exit')

    parser_list = subparsers.add_parser('list', help='List recent telepathic alerts')
    parser_list.add_argument('--limit', type=int, default=10, help='Number of alerts to show')

    parser_summary = subparsers.add_parser('summary', help='Show summary of telepathic alerts')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'run':
        alert_loop(interval_min=args.interval_min, interval_max=args.interval_max, once=args.once)
    elif args.command == 'list':
        list_alerts(limit=args.limit)
    elif args.command == 'summary':
        summary_alerts()
    else:
        print("Unknown command.")

if __name__ == '__main__':
    main()
