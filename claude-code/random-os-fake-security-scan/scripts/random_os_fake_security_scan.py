import sys
import time
import random
import argparse
from threading import Thread

try:
    from plyer import notification
except ImportError:
    print("plyer ライブラリが必要です。pip install plyer でインストールしてください。", file=sys.stderr)
    sys.exit(1)

FAKE_MESSAGES = [
    "未知のやる気ウイルスを検出しました",
    "マウスの動きが怪しい挙動を示しています",
    "あなたの進捗は安全です",
    "システムにカオス成分を注入中",
    "全ファイルをジョークで保護しました",
    "CPU温度が笑いで上昇中",
    "進捗率を水増ししています",
    "メモリに謎のやる気バグを発見",
    "ネットワークにギャグパケットを注入",
    "あなたの集中力は検疫済みです",
    "OSがダジャレモードに突入",
    "ファイルシステムが大喜利状態",
    "セキュリティ担当が困惑しています"
]

TITLE = "OS Security Scan"

class FakeScan:
    def __init__(self, duration=15, interval=2):
        self.duration = duration
        self.interval = interval
        self.progress = 0
        self.messages = random.sample(FAKE_MESSAGES, k=min(7, len(FAKE_MESSAGES)))
        self.total_steps = int(self.duration / self.interval)

    def run(self):
        for i in range(self.total_steps):
            self.progress = min(int((i / self.total_steps) * 100), 100)
            msg = self._get_message(i)
            self._notify(self.progress, msg)
            time.sleep(self.interval)
        # 終了メッセージ
        self._notify(100, "全てのファイルがジョークで保護されました")

    def _get_message(self, idx):
        if idx < len(self.messages):
            return self.messages[idx]
        return random.choice(FAKE_MESSAGES)

    def _notify(self, progress, message):
        notification.notify(
            title=f"[{TITLE}] 進捗: {progress}%",
            message=message,
            timeout=3
        )


def scan_command(args):
    duration = args.duration if args.duration else 15
    interval = args.interval if args.interval else 2
    scan = FakeScan(duration=duration, interval=interval)
    scan.run()


def list_messages(args):
    print("利用可能なフェイクメッセージ一覧:")
    for msg in FAKE_MESSAGES:
        print(f"- {msg}")


def main():
    parser = argparse.ArgumentParser(description="ランダムOSフェイクセキュリティスキャン通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser("scan", help="フェイクスキャンを実行")
    scan_parser.add_argument("--duration", type=int, help="スキャン全体の秒数 (デフォルト: 15)")
    scan_parser.add_argument("--interval", type=int, help="通知間隔秒数 (デフォルト: 2)")
    scan_parser.set_defaults(func=scan_command)

    list_parser = subparsers.add_parser("list", help="利用可能なメッセージ一覧表示")
    list_parser.set_defaults(func=list_messages)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
