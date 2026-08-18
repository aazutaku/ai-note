import sys
import random
import time
import argparse
import platform
import subprocess
from typing import List

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

REASONS = [
    "カフェイン過剰摂取が検出されました。",
    "キーボードの連打速度が異常値に到達。",
    "OSが自律的ストライキを開始しました。",
    "AIによる人間観察モードが有効化されました。",
    "ディスプレイの明るさが許容範囲を超過。",
    "マウスの移動距離が本日規定値を突破。",
    "不明なUSBデバイスが検出されました。",
    "仮想メモリがジョークモードに移行。",
    "無意識のうちにF5キーを30回連打。",
    "システムが突然の休憩を要求しています。"
]

IMPACTS = [
    "全ファイルが一時的に凍結されます。",
    "デスクトップ全体が保護モードに移行。",
    "ネットワーク通信がランダム化されます。",
    "ターミナルが詩的モードに切り替わります。",
    "全ウィンドウが90秒間逆さ表示。",
    "マウスポインタが自動で逃走します。",
    "クリップボードが自動消去されます。",
    "仮想メモリがリラックス状態に。",
    "全アプリが一時的に沈黙モード。",
    "ファイル名がランダムにシャッフル。"
]

UNLOCKS = [
    "深呼吸を5回行ってください。",
    "画面に向かって『ごめんなさい』と唱える。",
    "コーヒーを一杯減らしてください。",
    "椅子から立ち上がってストレッチ。",
    "30秒間目を閉じてリラックス。",
    "好きな歌を一小節口ずさむ。",
    "手を振ってOSに挨拶する。",
    "デスクトップのアイコンを一つ動かす。",
    "同僚に『今日は最高』と伝える。",
    "5回ジャンプする。"
]

ALERT_TITLES = [
    "OS Lockdown Activated!",
    "OS Lockdown Alert!",
    "緊急: ロックダウン通知",
    "[ALERT] システム制限発動",
    "システム警告: ロックダウン"
]


def random_alert() -> dict:
    title = random.choice(ALERT_TITLES)
    reason = random.choice(REASONS)
    impact = random.choice(IMPACTS)
    unlock = random.choice(UNLOCKS)
    return {
        "title": title,
        "reason": reason,
        "impact": impact,
        "unlock": unlock
    }

def print_alert(alert: dict):
    print(f"[{alert['title']}]\n理由: {alert['reason']}\n影響範囲: {alert['impact']}\n解除方法: {alert['unlock']}")

def notify_desktop(alert: dict):
    message = f"理由: {alert['reason']}\n影響範囲: {alert['impact']}\n解除方法: {alert['unlock']}"
    if PLYER_AVAILABLE:
        notification.notify(title=alert['title'], message=message, app_name="FakeLockdownAlert", timeout=8)
    else:
        system = platform.system()
        if system == "Darwin":
            subprocess.call(["osascript", "-e", f'display notification "{message}" with title "{alert["title"]}"'])
        elif system == "Linux":
            subprocess.call(["notify-send", alert['title'], message])
        elif system == "Windows":
            # Windows 10+ 用の通知 (PowerShell)
            try:
                import win10toast
                toaster = win10toast.ToastNotifier()
                toaster.show_toast(alert['title'], message, duration=8)
            except ImportError:
                print_alert(alert)
        else:
            print_alert(alert)

def run_random_alert(mode: str = "both"):
    alert = random_alert()
    if mode == "print":
        print_alert(alert)
    elif mode == "notify":
        notify_desktop(alert)
    else:
        print_alert(alert)
        notify_desktop(alert)

def schedule_alerts(interval_min: int, count: int, mode: str):
    for i in range(count):
        run_random_alert(mode)
        if i < count - 1:
            time.sleep(interval_min * 60)

def list_samples(num: int = 5):
    for _ in range(num):
        alert = random_alert()
        print_alert(alert)
        print("---")

def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Lockdown Alert Skill")
    subparsers = parser.add_subparsers(dest="command")

    parser_once = subparsers.add_parser("once", help="1回だけランダム警告を出す")
    parser_once.add_argument("--mode", choices=["print", "notify", "both"], default="both", help="出力方法 (print/notify/both)")

    parser_schedule = subparsers.add_parser("schedule", help="一定間隔で複数回警告を出す")
    parser_schedule.add_argument("--interval", type=int, default=30, help="警告間隔(分)")
    parser_schedule.add_argument("--count", type=int, default=3, help="警告回数")
    parser_schedule.add_argument("--mode", choices=["print", "notify", "both"], default="both", help="出力方法")

    parser_list = subparsers.add_parser("list", help="サンプル警告をまとめて表示")
    parser_list.add_argument("--num", type=int, default=5, help="サンプル数")

    args = parser.parse_args()

    if args.command == "once":
        run_random_alert(args.mode)
    elif args.command == "schedule":
        schedule_alerts(args.interval, args.count, args.mode)
    elif args.command == "list":
        list_samples(args.num)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
