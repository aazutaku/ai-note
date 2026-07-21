import sys
import random
import argparse
import datetime
import os
from typing import List, Optional

MOOD_LIST = [
    {
        'title': '絶好調エンジニアモード',
        'message': 'やる気MAX！今こそ難題に挑戦する時。'
    },
    {
        'title': 'アイデア枯渇ゾーン',
        'message': 'コーヒーブレイク推奨。新しい刺激を求めましょう。'
    },
    {
        'title': 'バグ吸引フェイズ',
        'message': '今日はバグが寄ってきそうな予感…慎重に！'
    },
    {
        'title': '集中力散漫モード',
        'message': '通知やSNSに注意。深呼吸してリセットしよう。'
    },
    {
        'title': '仕様書迷子タイム',
        'message': 'ドキュメントを見直してみよう。新発見があるかも。'
    },
    {
        'title': 'リファクタリング衝動',
        'message': '今こそコードを美しく整えたい気分。やりすぎ注意。'
    },
    {
        'title': '無限ループの予感',
        'message': 'アルゴリズムの見直し推奨。冷静にデバッグしよう。'
    },
    {
        'title': '新機能ひらめきモード',
        'message': 'アイデアが湧いてきた！すぐにメモしよう。'
    },
    {
        'title': 'レビュー恐怖症',
        'message': '他人の目が気になる日。勇気を出してプルリク送信！'
    },
    {
        'title': '眠気MAXゾーン',
        'message': '休憩推奨。短い仮眠でリフレッシュしよう。'
    }
]

HISTORY_FILE = os.path.expanduser('~/.random_os_mood_history')


def get_random_mood() -> dict:
    return random.choice(MOOD_LIST)


def format_mood_entry(mood: dict, timestamp: Optional[datetime.datetime] = None) -> str:
    if timestamp is None:
        timestamp = datetime.datetime.now()
    ts_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    return f"[OS-Mood Barometer] {ts_str}\n{mood['title']}：{mood['message']}\n"


def log_mood_entry(mood: dict, timestamp: Optional[datetime.datetime] = None) -> None:
    entry = format_mood_entry(mood, timestamp)
    with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
        f.write(entry)


def list_history(limit: int = 10) -> List[str]:
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
    # Each entry is 2 lines + empty line
    entries = []
    buf = []
    for line in lines:
        if line.strip() == '' and buf:
            entries.append('\n'.join(buf))
            buf = []
        elif line.strip() != '':
            buf.append(line)
    if buf:
        entries.append('\n'.join(buf))
    return entries[-limit:]


def summary_stats() -> dict:
    if not os.path.exists(HISTORY_FILE):
        return {'total': 0, 'counts': {}}
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    counts = {}
    total = 0
    for line in lines:
        if line.startswith('[OS-Mood Barometer]'):
            total += 1
        for mood in MOOD_LIST:
            if mood['title'] in line:
                counts[mood['title']] = counts.get(mood['title'], 0) + 1
    return {'total': total, 'counts': counts}


def print_barometer():
    mood = get_random_mood()
    entry = format_mood_entry(mood)
    print(entry)
    log_mood_entry(mood)


def main():
    parser = argparse.ArgumentParser(description='謎のOS風 気分バロメーター')
    subparsers = parser.add_subparsers(dest='command', help='サブコマンド')

    # show (default)
    parser_show = subparsers.add_parser('show', help='ランダムな気分モードを表示')

    # list
    parser_list = subparsers.add_parser('list', help='過去のバロメーター履歴を表示')
    parser_list.add_argument('--limit', type=int, default=10, help='表示件数 (デフォルト: 10)')

    # summary
    parser_summary = subparsers.add_parser('summary', help='バロメーター履歴の統計を表示')

    args = parser.parse_args()

    if args.command is None or args.command == 'show':
        print_barometer()
    elif args.command == 'list':
        entries = list_history(args.limit)
        if not entries:
            print('履歴がありません。')
        else:
            for entry in entries:
                print(entry)
                print('-' * 40)
    elif args.command == 'summary':
        stats = summary_stats()
        print(f"合計: {stats['total']} 回")
        for k, v in stats['counts'].items():
            print(f"{k}: {v} 回")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
