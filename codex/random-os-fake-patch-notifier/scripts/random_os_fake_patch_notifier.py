import random
import time
import argparse
import sys
import os
from datetime import datetime, timedelta
try:
    import notify2
except ImportError:
    notify2 = None
try:
    from win10toast import ToastNotifier
except ImportError:
    ToastNotifier = None

PATCH_TITLES = [
    "OS Patch Notes v13.4.2",
    "OS Patch Notes v42.0.1-beta",
    "OS Patch Notes v7.8.9",
    "OS Patch Notes v99.0.0-rc1",
    "OS Patch Notes v3.14.15",
    "OS Patch Notes v0.0.42-alpha",
]

FAKE_FEATURES = [
    "新機能: 午後3時に自動で眠気を注入する機能を追加しました",
    "新機能: マウスカーソルがたまに踊りだすようになりました",
    "新機能: デバッグ時にランダムでBGMが流れます",
    "新機能: 画面の端に謎の猫が出現することがあります",
    "新機能: コーヒーの香りを画面から放出する機能（未対応）",
    "新機能: 画面が唐突に青くなりますが仕様です",
]

FAKE_BUGS = [
    "バグ修正: やる気が0になる問題を修正しました",
    "バグ修正: たまにファイルがどこかに消える問題を修正",
    "バグ修正: 画面の端に謎の猫が出現する問題を修正",
    "バグ修正: 入力中にキーボードが眠る問題を修正",
    "バグ修正: たまに通知が5倍届く問題を修正",
    "バグ修正: 画面が逆さまになる問題を修正（再発中）",
]

FAKE_KNOWN = [
    "既知の問題: たまに画面が唐突に青くなりますが仕様です",
    "既知の問題: 通知が深夜にも発生する場合があります",
    "既知の問題: このパッチノート自体が意味不明です",
    "既知の問題: たまに何も起きません",
    "既知の問題: 画面の猫が消えません",
    "既知の問題: 眠気注入機能が強すぎることがあります",
]

MIN_INTERVAL = 180  # 最短3分
MAX_INTERVAL = 900  # 最長15分

class Notifier:
    def __init__(self):
        self.platform = sys.platform
        self.notifier = None
        if self.platform.startswith('linux') and notify2:
            notify2.init("Random OS Fake Patch Notifier")
            self.notifier = 'notify2'
        elif self.platform.startswith('win') and ToastNotifier:
            self.toaster = ToastNotifier()
            self.notifier = 'win10toast'
        else:
            self.notifier = None

    def send(self, title, message):
        if self.notifier == 'notify2':
            n = notify2.Notification(title, message)
            n.set_timeout(7000)
            n.show()
        elif self.notifier == 'win10toast':
            self.toaster.show_toast(title, message, duration=7, threaded=True)
        else:
            print(f"[通知] {title}\n{message}")


def generate_patch_note():
    title = random.choice(PATCH_TITLES)
    features = random.sample(FAKE_FEATURES, k=random.randint(1,2))
    bugs = random.sample(FAKE_BUGS, k=random.randint(1,2))
    known = random.sample(FAKE_KNOWN, k=1)
    lines = features + bugs + known
    random.shuffle(lines)
    return title, '\n- ' + '\n- '.join(lines)


def run_notifier_loop(args):
    notifier = Notifier()
    last_notify = datetime.now() - timedelta(seconds=MAX_INTERVAL)
    try:
        while True:
            now = datetime.now()
            interval = random.randint(MIN_INTERVAL, MAX_INTERVAL)
            next_time = now + timedelta(seconds=interval)
            title, message = generate_patch_note()
            notifier.send(title, message)
            if args.verbose:
                print(f"[DEBUG] Next notification in {interval} seconds at {next_time.strftime('%H:%M:%S')}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[INFO] Notifier stopped by user.")


def send_one(args):
    notifier = Notifier()
    title, message = generate_patch_note()
    notifier.send(title, message)


def list_examples(args):
    for _ in range(args.count):
        title, message = generate_patch_note()
        print(f"[通知] {title}\n{message}\n")


def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Patch Notifier")
    subparsers = parser.add_subparsers(dest="command")

    p_run = subparsers.add_parser("run", help="ランダムなタイミングで偽パッチノート通知を発生させる")
    p_run.add_argument("--verbose", action="store_true", help="詳細なデバッグ出力")

    p_once = subparsers.add_parser("once", help="1回だけ偽パッチノート通知を発生させる")

    p_list = subparsers.add_parser("list", help="通知サンプルを複数出力する (通知はしない)")
    p_list.add_argument("--count", type=int, default=3, help="サンプル出力数")

    args = parser.parse_args()
    if args.command == "run":
        run_notifier_loop(args)
    elif args.command == "once":
        send_one(args)
    elif args.command == "list":
        list_examples(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
