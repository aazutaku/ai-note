import random
import sys
import argparse
import platform
import subprocess
import time
from typing import List

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

def get_fake_bugs() -> List[str]:
    return [
        'キーボードのJキー過剰使用バグ',
        '昼寝検出バグ',
        'コーヒー過剰摂取バグ',
        'マグカップ底なしバグ',
        '机上の消しゴム消失バグ',
        'USBメモリ自動ワープバグ',
        '椅子の自動回転バグ',
        'マウス逆走バグ',
        '画面端に吸い寄せられるウィンドウバグ',
        '謎の「やる気消失」バグ',
        '仮想メモリ無限増殖バグ',
        'ランチタイム自動延長バグ',
        'Slack通知無限ループバグ',
        '会議中ミュート解除バグ',
        '電源ケーブル自動抜けバグ',
        'ファイル名自動暗号化バグ',
        'カレンダー自動祝日追加バグ',
        'タスク完了自動消滅バグ',
        'プリンタ紙詰まり無限発生バグ',
        'ヘッドフォン片耳消失バグ',
    ]

def get_fake_rewards() -> List[str]:
    return [
        '1バグポイント進呈',
        '謎の称号授与',
        '幻のステッカー贈呈',
        '5バグポイント',
        'レアバグバッジ進呈',
        '昼寝券1枚',
        'コーヒーチケット',
        '開発者の栄誉',
        '特製バグTシャツ',
        'バグバウンティ殿堂入り',
        '秘密のSlack絵文字',
        '謎のエナジードリンク',
        '伝説のUSBメモリ',
        'バグ修正証明書',
        'オリジナルマグカップ',
        '開発室VIP席権',
        '一日社長権',
        'バグバウンティ金メダル',
        '特製バグノート',
        '謎の開発者称号',
    ]

def get_fake_severity() -> List[str]:
    return [
        '発見', '重大', '警告', '速報', '限定', '超希少'
    ]

def random_fake_alert() -> str:
    bug = random.choice(get_fake_bugs())
    reward = random.choice(get_fake_rewards())
    severity = random.choice(get_fake_severity())
    return f"[FAKE BUG BOUNTY ALERT]\n{severity}: {bug}\n報酬: {reward}"

def notify_desktop(title: str, message: str):
    system = platform.system()
    if PLYER_AVAILABLE:
        notification.notify(title=title, message=message, app_name='Fake Bug Bounty', timeout=8)
        return
    if system == 'Linux':
        try:
            subprocess.run(['notify-send', title, message], check=True)
        except Exception:
            pass
    elif system == 'Darwin':
        script = f'display notification "{message}" with title "{title}"'
        try:
            subprocess.run(['osascript', '-e', script], check=True)
        except Exception:
            pass
    elif system == 'Windows':
        # fallback: print to terminal
        pass

def print_terminal_alert(alert: str):
    border = '=' * 48
    print(f"\n{border}\n{alert}\n{border}\n")

def log_alert(alert: str, logfile: str):
    try:
        with open(logfile, 'a', encoding='utf-8') as f:
            f.write(alert + '\n')
    except Exception as e:
        print(f"[WARN] ログ保存に失敗: {e}")

def list_alerts(logfile: str, count: int):
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        for alert in lines[-count:]:
            print(alert)
    except FileNotFoundError:
        print("[INFO] ログファイルが存在しません。")


def summary_alerts(logfile: str):
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        print(f"合計通知数: {len(lines)}")
        bugs = set()
        rewards = set()
        for l in lines:
            if ':' in l:
                parts = l.split(':', 2)
                if len(parts) >= 3:
                    bugs.add(parts[1].strip())
                    rewards.add(parts[2].replace('報酬', '').strip())
        print(f"ユニークバグ: {len(bugs)}件")
        print(f"ユニーク報酬: {len(rewards)}件")
    except FileNotFoundError:
        print("[INFO] ログファイルが存在しません。")

def main():
    parser = argparse.ArgumentParser(description='Fake OS Bug Bounty Alert')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='偽バグバウンティ通知を即時発動')
    parser_alert.add_argument('--log', type=str, default=None, help='通知履歴を保存するファイルパス')
    parser_alert.add_argument('--terminal', action='store_true', help='ターミナルにも表示')
    parser_alert.add_argument('--desktop', action='store_true', help='デスクトップ通知も表示')

    parser_list = subparsers.add_parser('list', help='通知履歴を一覧表示')
    parser_list.add_argument('--log', type=str, required=True, help='履歴ファイルパス')
    parser_list.add_argument('--count', type=int, default=10, help='表示件数')

    parser_summary = subparsers.add_parser('summary', help='通知履歴のサマリー表示')
    parser_summary.add_argument('--log', type=str, required=True, help='履歴ファイルパス')

    parser_daemon = subparsers.add_parser('daemon', help='一定間隔で自動通知 (デモ用)')
    parser_daemon.add_argument('--interval', type=int, default=1800, help='通知間隔(秒)')
    parser_daemon.add_argument('--log', type=str, default=None, help='通知履歴ファイル')
    parser_daemon.add_argument('--terminal', action='store_true')
    parser_daemon.add_argument('--desktop', action='store_true')
    parser_daemon.add_argument('--max', type=int, default=0, help='最大通知回数 (0=無限)')

    args = parser.parse_args()
    if args.command == 'alert':
        alert = random_fake_alert()
        if args.terminal or not args.desktop:
            print_terminal_alert(alert)
        if args.desktop:
            notify_desktop('Fake Bug Bounty', alert.replace('\n', ' '))
        if args.log:
            log_alert(alert, args.log)
    elif args.command == 'list':
        list_alerts(args.log, args.count)
    elif args.command == 'summary':
        summary_alerts(args.log)
    elif args.command == 'daemon':
        count = 0
        try:
            while args.max == 0 or count < args.max:
                alert = random_fake_alert()
                if args.terminal or not args.desktop:
                    print_terminal_alert(alert)
                if args.desktop:
                    notify_desktop('Fake Bug Bounty', alert.replace('\n', ' '))
                if args.log:
                    log_alert(alert, args.log)
                count += 1
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print('\n[INFO] 自動通知を停止しました')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
