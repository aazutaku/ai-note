import sys
import time
import random
import argparse
import platform
import threading

try:
    from plyer import notification
except ImportError:
    notification = None

FAKE_MESSAGES = [
    "未知のやる気ウイルスを発見しました",
    "マウスの動きが怪しいです",
    "あなたの進捗は安全です（たぶん）",
    "CPU温度がやる気に比例しています",
    "キーボードから謎の信号を検出",
    "あなたの集中力に異常あり",
    "システムはカオス状態です！",
    "進捗率が乱高下しています",
    "メモリにやる気成分を注入中",
    "OSが笑いを検知しました"
]

FINAL_MESSAGES = [
    "スキャン完了：あなたの進捗は安全です",
    "スキャン完了：やる気ウイルスは検出されませんでした",
    "スキャン終了：混沌レベルが上昇しました"
]

TITLE = "OS Security Scan"


def send_notification(title, message):
    if notification is not None:
        try:
            notification.notify(
                title=title,
                message=message,
                app_name="FakeSecurityScan",
                timeout=5
            )
        except Exception as e:
            print(f"[通知失敗] {message}")
    else:
        print(f"[{title}] {message}")


def scan_progress(duration=20, steps=7, dry_run=False):
    interval = duration // steps
    progress_points = sorted(random.sample(range(10, 100), steps - 1)) + [100]
    messages = random.sample(FAKE_MESSAGES, steps - 1)
    for i, prog in enumerate(progress_points):
        if i < steps - 1:
            msg = messages[i]
        else:
            msg = random.choice(FINAL_MESSAGES)
        bar = f"進捗: {prog}% | {msg}"
        if dry_run:
            print(bar)
        else:
            send_notification(TITLE, bar)
        time.sleep(interval)


def cli_main():
    parser = argparse.ArgumentParser(description="Fake OS Security Scan Notifier")
    parser.add_argument('--duration', type=int, default=20, help='スキャン演出の総秒数 (デフォルト: 20)')
    parser.add_argument('--steps', type=int, default=7, help='進捗更新回数 (デフォルト: 7)')
    parser.add_argument('--dry-run', action='store_true', help='通知を表示せずターミナル出力のみ')
    parser.add_argument('cmd', nargs='?', default='scan', choices=['scan', 'demo'], help='サブコマンド (scan/demo)')
    args = parser.parse_args()

    if args.cmd == 'scan':
        scan_progress(duration=args.duration, steps=args.steps, dry_run=args.dry_run)
    elif args.cmd == 'demo':
        print("--- フェイクセキュリティスキャン出力例 ---")
        scan_progress(duration=3, steps=5, dry_run=True)
    else:
        print("不明なコマンドです")

if __name__ == '__main__':
    cli_main()
