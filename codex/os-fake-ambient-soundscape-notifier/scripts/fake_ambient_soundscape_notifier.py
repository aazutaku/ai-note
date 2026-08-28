import argparse
import random
import sys
import time
from datetime import datetime, timedelta

# 通知メッセージテンプレート
NOTIFICATION_TEMPLATES = [
    '[OS公式通知]: 本日は集中力向上のため、{theme}BGMを自動再生します。',
    '[Ambient Soundscape]: 今から{duration}は謎の{theme}騒音推奨。',
    '[System Notice]: 休憩推奨: {theme}モードがONになりました。',
    '[OS公式]: 本日限定！{theme}BGMが有効です。',
    '[Ambient Soundscape]: 静かな{theme}の空気感を再現中。',
    '[System Notification]: {theme}の環境音がバックグラウンドで流れています。',
    '[OS]: {theme}BGMが自動的に切り替わりました。',
    '[Ambient]: {theme}サウンドスケープ演出を開始します。',
    '[OS公式]: 今だけ！{theme}の雰囲気をお楽しみください。',
    '[System Notice]: {theme}のBGMが推奨されています。',
]

THEMES = [
    '森のさざめき',
    'カフェ',
    '海辺の波音',
    '工事現場の遠い雑音',
    '図書館',
    '雨音',
    '宇宙船のエンジン音',
    '地下鉄のホーム',
    'オフィスのざわめき',
    '鳥のさえずり',
    '焚き火',
    '夜の虫の声',
    '静かな教室',
    '山小屋',
    '水族館',
    '古いラジオ',
    '工場の機械音',
    'ショッピングモール',
    '温泉の湯けむり',
    '高原の風',
]

DURATIONS = [
    '15分間', '30分間', '1時間', '10分間', '20分間', '5分間', '45分間'
]

HISTORY = []

# 通知生成関数
def generate_notification():
    template = random.choice(NOTIFICATION_TEMPLATES)
    theme = random.choice(THEMES)
    duration = random.choice(DURATIONS)
    msg = template.format(theme=theme, duration=duration)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'[{timestamp}] {msg}'

# 通知を出力し履歴に追加
def notify():
    msg = generate_notification()
    print(msg)
    HISTORY.append(msg)

# 履歴を表示
def list_history(args):
    if not HISTORY:
        print('通知履歴はありません。')
        return
    for item in HISTORY:
        print(item)

# 履歴の要約
def summary(args):
    print(f'通知回数: {len(HISTORY)}')
    themes = [m.split('] ')[1] for m in HISTORY if '] ' in m]
    theme_counts = {}
    for t in THEMES:
        count = sum(1 for line in themes if t in line)
        if count > 0:
            theme_counts[t] = count
    if theme_counts:
        print('テーマ別回数:')
        for t, c in sorted(theme_counts.items(), key=lambda x: -x[1]):
            print(f'  {t}: {c}回')
    else:
        print('テーマ別集計はありません。')

# ランダムな間隔で通知を出す（うるさすぎないよう調整）
def auto_notify(args):
    min_interval = args.min_interval or 600  # 10分
    max_interval = args.max_interval or 1800 # 30分
    duration = args.duration or 3600         # 1時間
    end_time = datetime.now() + timedelta(seconds=duration)
    print(f'フェイク環境音通知を{duration//60}分間、{min_interval//60}-{max_interval//60}分間隔で実行します。')
    while datetime.now() < end_time:
        notify()
        wait = random.randint(min_interval, max_interval)
        time.sleep(wait)
    print('自動通知を終了しました。')

def main():
    parser = argparse.ArgumentParser(description='OSフェイク環境音通知スキル')
    subparsers = parser.add_subparsers(dest='command')

    parser_notify = subparsers.add_parser('notify', help='今すぐフェイク通知を1回出す')
    parser_notify.set_defaults(func=lambda args: notify())

    parser_auto = subparsers.add_parser('auto', help='自動で一定間隔ごとにフェイク通知')
    parser_auto.add_argument('--min-interval', type=int, help='通知の最小間隔（秒）')
    parser_auto.add_argument('--max-interval', type=int, help='通知の最大間隔（秒）')
    parser_auto.add_argument('--duration', type=int, help='実行時間（秒）')
    parser_auto.set_defaults(func=auto_notify)

    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_list.set_defaults(func=list_history)

    parser_summary = subparsers.add_parser('summary', help='通知履歴の要約')
    parser_summary.set_defaults(func=summary)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)
    args.func(args)

if __name__ == '__main__':
    main()
