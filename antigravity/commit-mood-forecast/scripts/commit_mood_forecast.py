import sys
import argparse
import random
from datetime import datetime

MOODS = [
    {
        'icon': '快晴',
        'message': '今日は絶好調！やる気MAXで進めましょう。'
    },
    {
        'icon': '曇り',
        'message': 'ちょっと迷い気味。無理せず一歩ずつ。'
    },
    {
        'icon': '雨',
        'message': '集中力が散漫かも？小休憩を挟みましょう。'
    },
    {
        'icon': '雷',
        'message': 'やる気ゼロ。コーヒーブレイク推奨！'
    },
    {
        'icon': '晴れ時々曇り',
        'message': 'まずまずの調子。焦らず着実に。'
    },
    {
        'icon': '霧',
        'message': '頭の中がもやもや。TODOを整理してみては？'
    },
    {
        'icon': '雪',
        'message': '静かな気分。じっくりコードと向き合いましょう。'
    },
    {
        'icon': '強風',
        'message': 'アイデアが舞い上がる日。思いついたら即メモ！'
    },
    {
        'icon': '虹',
        'message': 'ひらめきの予感。新しい挑戦に最適です。'
    },
    {
        'icon': '台風',
        'message': 'タスクが渦巻く日。優先順位を見直しましょう。'
    }
]

HISTORY = []


def print_forecast():
    mood = random.choice(MOODS)
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    forecast = f"[commit-mood-forecast]\n本日のあなたの作業気分天気予報：\n{mood['icon']:<8}：{mood['message']}\n({now})\n"
    print(forecast)
    HISTORY.append({'datetime': now, 'icon': mood['icon'], 'message': mood['message']})


def list_history():
    if not HISTORY:
        print("[commit-mood-forecast] まだ気分天気予報の履歴はありません。\n")
        return
    print("[commit-mood-forecast] これまでの気分天気予報履歴：")
    for i, entry in enumerate(HISTORY, 1):
        print(f"{i:2d}. {entry['datetime']} | {entry['icon']:<8} | {entry['message']}")
    print()


def summary():
    if not HISTORY:
        print("[commit-mood-forecast] 履歴がないため集計できません。\n")
        return
    counts = {}
    for entry in HISTORY:
        counts[entry['icon']] = counts.get(entry['icon'], 0) + 1
    print("[commit-mood-forecast] 気分天気の出現回数まとめ：")
    for icon, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{icon:<8}: {cnt}回")
    print()


def main():
    parser = argparse.ArgumentParser(description='commit-mood-forecast: コミット時に気分天気予報を表示')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('log', help='今の気分天気予報を表示')
    subparsers.add_parser('list', help='これまでの気分天気予報履歴を表示')
    subparsers.add_parser('summary', help='気分天気の出現回数を集計')

    args = parser.parse_args()

    if args.command is None or args.command == 'log':
        print_forecast()
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    else:
        print('不明なコマンドです。log, list, summary のいずれかを指定してください。')
        sys.exit(1)

if __name__ == '__main__':
    main()
