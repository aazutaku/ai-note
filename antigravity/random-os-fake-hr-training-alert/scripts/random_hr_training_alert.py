import sys
import os
import random
import argparse
import platform
import subprocess
from datetime import datetime

# 通知メッセージ候補
HR_ALERT_MESSAGES = [
    '緊急：本日14時より“謎のパワポ芸入門”研修必須',
    '重要：OS公式“無限ビデオ視聴”研修が始まります',
    'ただ今より“謎マナー講座”を受講してください',
    '本日は“人事部主催：謎の自己分析ワークショップ”が開催されます',
    '参加必須：OS管理者による“謎のリモートお辞儀研修”',
    '注意：本日17時より“謎のビジネスカジュアル講座”が始まります',
    'OS推奨：全ユーザー対象“謎の名刺交換ロールプレイ”',
    '重要：本日中に“無限アンケート記入”を完了してください',
    '緊急：本部長による“謎のZoomカメラON強制”研修',
    '本日限定：“謎のワークスタイル変革”セッション参加必須',
    '人事部より：“謎の社内SNS活用術”講座を受講してください',
    'OSより：今すぐ“謎の1on1面談”を予約してください',
    '全社通達：“謎の自己啓発ビデオ”を視聴してください',
    '警告：本日中に“謎のエクセル方眼紙研修”を完了してください',
    'HR管理者より：“謎のリモート背景選手権”開催のお知らせ'
]

HR_ALERT_LEVELS = [
    ('ALERT', '[ALERT]'),
    ('NOTICE', '[NOTICE]'),
    ('INFO', '[INFO]'),
    ('WARNING', '[WARNING]')
]


def pick_random_alert():
    level, prefix = random.choice(HR_ALERT_LEVELS)
    message = random.choice(HR_ALERT_MESSAGES)
    return f"{prefix} {message}", level


def notify_os(message, level):
    system = platform.system()
    try:
        if system == 'Darwin':  # macOS
            title = '人事研修通知'
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', script], check=True)
        elif system == 'Linux':
            subprocess.run(['notify-send', '人事研修通知', message], check=True)
        elif system == 'Windows':
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast('人事研修通知', message, duration=5, threaded=True)
        else:
            print(message)
    except Exception as e:
        print(f"[INFO] OS通知失敗: {e}\n{message}")


def notify_terminal(message, level):
    # 色分け: ALERT=赤, WARNING=黄, NOTICE=青, INFO=緑
    color_map = {
        'ALERT': '\033[91m',
        'WARNING': '\033[93m',
        'NOTICE': '\033[94m',
        'INFO': '\033[92m'
    }
    endc = '\033[0m'
    color = color_map.get(level, '')
    print(f"{color}{message}{endc}")


def main():
    parser = argparse.ArgumentParser(description='謎の人事研修通知スクリプト')
    parser.add_argument('--os-notify', action='store_true', help='OS通知も同時に行う')
    parser.add_argument('--count', type=int, default=1, help='通知回数 (デフォルト:1)')
    parser.add_argument('--interval', type=float, default=0, help='通知間隔(秒)')
    args = parser.parse_args()

    for i in range(args.count):
        message, level = pick_random_alert()
        notify_terminal(message, level)
        if args.os_notify:
            notify_os(message, level)
        if args.interval > 0 and i < args.count - 1:
            import time
            time.sleep(args.interval)

if __name__ == '__main__':
    main()
