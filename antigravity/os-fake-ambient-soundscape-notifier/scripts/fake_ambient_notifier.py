import sys
import time
import random
import argparse
from datetime import datetime, timedelta

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

# 通知メッセージテンプレート
SOUND_THEMES = [
    "森のさざめきBGMを自動再生します（実際の再生はありません）",
    "今から15分間は謎のカフェ騒音推奨。気分転換にどうぞ。",
    "深夜のサーバールームホワイトノイズを流します（フェイクです）",
    "本日は雨音BGM推奨日です。リラックスして作業を続けてください。",
    "本日限定：謎の宇宙船内環境音を自動適用中。",
    "OS公式：今から10分間はビル屋上の風音BGMをおすすめします。",
    "今日は静かな図書館環境音が自動再生されます（フェイクです）",
    "OS通知：謎の地下鉄ホーム環境音を体験中です。",
    "集中力向上のために、今だけ“謎の古城の静寂”モードがONです。",
    "本日は“謎の水族館BGM”を自動適用しています（実際には鳴りません）"
]

PREFIXES = [
    "[OS公式通知]",
    "[通知]",
    "[OS環境音]",
    "[システム]",
    "[OS通知]"
]

# 通知履歴（メモリのみ）
NOTIFY_HISTORY = []

# 通知を生成
def generate_notification():
    prefix = random.choice(PREFIXES)
    theme = random.choice(SOUND_THEMES)
    return f"{prefix} {theme}"

# 通知を表示（ターミナル＋デスクトップ）
def show_notification(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} {msg}")
    if PLYER_AVAILABLE:
        try:
            notification.notify(
                title="Fake Ambient Soundscape Notifier",
                message=msg,
                timeout=8
            )
        except Exception as e:
            print(f"[WARN] デスクトップ通知失敗: {e}")

# 通知履歴に追加
def log_notification(msg):
    NOTIFY_HISTORY.append({
        'timestamp': datetime.now(),
        'message': msg
    })

# 通知間隔を決定（10分〜60分の間でランダム）
def random_interval():
    return random.randint(600, 3600)

# ログ一覧表示
def list_notifications():
    if not NOTIFY_HISTORY:
        print("通知履歴はありません。")
        return
    for entry in NOTIFY_HISTORY:
        ts = entry['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
        print(f"{ts} {entry['message']}")

# サマリー表示
def summary_notifications():
    print(f"通知回数: {len(NOTIFY_HISTORY)}")
    themes = {}
    for entry in NOTIFY_HISTORY:
        for theme in SOUND_THEMES:
            if theme in entry['message']:
                themes[theme] = themes.get(theme, 0) + 1
    print("--- テーマ別内訳 ---")
    for theme, count in sorted(themes.items(), key=lambda x: -x[1]):
        print(f"{theme}: {count}回")

# メインループ
def main():
    parser = argparse.ArgumentParser(description="Fake Ambient Soundscape Notifier")
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='自動フェイク通知を開始')
    parser_run.add_argument('--min-interval', type=int, default=600, help='最小通知間隔（秒）')
    parser_run.add_argument('--max-interval', type=int, default=3600, help='最大通知間隔（秒）')
    parser_run.add_argument('--max-count', type=int, default=0, help='最大通知回数（0は無制限）')

    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知サマリーを表示')

    args = parser.parse_args()

    if args.command == 'run':
        count = 0
        try:
            while True:
                msg = generate_notification()
                show_notification(msg)
                log_notification(msg)
                count += 1
                if args.max_count > 0 and count >= args.max_count:
                    break
                interval = random.randint(args.min_interval, args.max_interval)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n[終了] フェイク通知を停止しました。")
    elif args.command == 'list':
        list_notifications()
    elif args.command == 'summary':
        summary_notifications()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
