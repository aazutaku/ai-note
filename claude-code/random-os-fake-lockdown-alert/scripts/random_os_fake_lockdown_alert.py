import random
import argparse
import sys
import time
import datetime
import platform
import subprocess

# メッセージテンプレート
REASONS = [
    'カフェイン過剰摂取検知',
    'キーボード連打による過熱',
    'AI過剰利用',
    '生産性が高すぎるため',
    '集中力の急激な低下',
    '謎の宇宙線干渉',
    'OSの気分が乗らない',
    'ファイルシステムからの悲鳴',
    'ネットワークのやる気低下',
    'ユーザーの退屈度が閾値超過'
]

AFFECTED = [
    '全ユーザーディレクトリ',
    '/tmp, /home, /dev/null',
    'デスクトップと書類フォルダ',
    'カレントディレクトリ',
    '全プロセス',
    'ランダムな3ファイル',
    'ネットワーク全域',
    '仮想メモリ',
    'USBデバイス',
    '隣の席のPC'
]

UNLOCKS = [
    '深呼吸5回 + 机の上を片付ける',
    '画面を3秒間見つめる',
    'コーヒーを1杯減らす',
    '手を振る',
    '目を閉じて「解除」と唱える',
    '椅子から立ち上がる',
    '好きな曲を1フレーズ歌う',
    'タイマーを1分セット',
    'ターミナルを再起動',
    '同僚に「ロックダウン発令」と伝える'
]

BANNERS = [
    '=== 緊急OSロックダウン発令 ===',
    '=== 謎のシステム凍結警告 ===',
    '=== OSストライキ通知 ===',
    '=== セキュリティ異常アラート ===',
    '=== 仮想環境パニック発令 ==='
]

FOOTER = '============================='

HISTORY = []


def random_alert():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    banner = random.choice(BANNERS)
    reason = random.choice(REASONS)
    affected = random.choice(AFFECTED)
    unlock = random.choice(UNLOCKS)
    alert = f"{banner}\n発令時刻: {now}\n理由: {reason}\n影響範囲: {affected}\n解除方法: {unlock}\n{FOOTER}"
    HISTORY.append({
        'timestamp': now,
        'banner': banner,
        'reason': reason,
        'affected': affected,
        'unlock': unlock,
        'alert': alert
    })
    return alert


def show_alert(alert, notify=False):
    print(alert)
    if notify:
        send_desktop_notification(alert)


def send_desktop_notification(message):
    system = platform.system()
    title = 'OSロックダウン通知'
    if system == 'Darwin':  # macOS
        try:
            subprocess.run([
                'osascript', '-e',
                f'display notification "{message}" with title "{title}"'
            ], check=True)
        except Exception:
            pass
    elif system == 'Linux':
        try:
            subprocess.run([
                'notify-send', title, message], check=True)
        except Exception:
            pass
    # Windowsは標準で通知API非対応（拡張可）


def list_history():
    if not HISTORY:
        print('まだロックダウン通知は発令されていません。')
        return
    for i, h in enumerate(HISTORY, 1):
        print(f"[{i}] {h['timestamp']} - {h['reason']} -> {h['affected']}")


def summary():
    print(f"累計発令回数: {len(HISTORY)}")
    if HISTORY:
        last = HISTORY[-1]
        print(f"直近: {last['timestamp']} / {last['reason']}")


def parse_args():
    parser = argparse.ArgumentParser(description='謎のOSロックダウン通知を発令します')
    parser.add_argument('command', nargs='?', default='alert', choices=['alert', 'list', 'summary'], help='サブコマンド: alert/list/summary')
    parser.add_argument('--notify', action='store_true', help='デスクトップ通知も同時に表示')
    parser.add_argument('--repeat', type=int, default=1, help='繰り返し回数')
    parser.add_argument('--interval', type=float, default=0, help='繰り返し間隔(秒)')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'alert':
        for i in range(args.repeat):
            alert = random_alert()
            show_alert(alert, notify=args.notify)
            if i < args.repeat - 1 and args.interval > 0:
                time.sleep(args.interval)
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()

if __name__ == '__main__':
    main()
