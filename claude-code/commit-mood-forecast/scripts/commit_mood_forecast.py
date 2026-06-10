import sys
import argparse
import random
import datetime

MOODS = [
    {
        'icon': '☀️',
        'label': '快晴',
        'message': '今日は絶好調。どんどん進めましょう。'
    },
    {
        'icon': '🌤️',
        'label': '晴れ時々曇り',
        'message': '調子はまずまず。時々休憩も忘れずに。'
    },
    {
        'icon': '☁️',
        'label': '曇り',
        'message': 'ちょっと迷い気味？コーヒーブレイクも大事です。'
    },
    {
        'icon': '🌧️',
        'label': '雨',
        'message': '集中力が散漫かも。気分転換してみましょう。'
    },
    {
        'icon': '⛈️',
        'label': '雷',
        'message': 'やる気ゼロの日もあります。無理せずいきましょう。'
    },
    {
        'icon': '🌈',
        'label': '虹',
        'message': '新しい発見がありそうな予感！'
    },
    {
        'icon': '🌪️',
        'label': '突風',
        'message': 'バグの嵐にご注意を。落ち着いて対応しましょう。'
    },
    {
        'icon': '🌙',
        'label': '夜',
        'message': '夜更かし注意。しっかり休みましょう。'
    }
]

def print_mood_forecast():
    mood = random.choice(MOODS)
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    print('[commit-mood-forecast]')
    print('本日のあなたの作業気分天気予報：')
    print(f'  {mood["icon"]} {mood["label"]}！{mood["message"]}')
    print(f'  ({now})')

def list_moods():
    print('利用可能な気分天気一覧:')
    for mood in MOODS:
        print(f'  {mood["icon"]} {mood["label"]}: {mood["message"]}')

def summary():
    print('commit-mood-forecastは、コミット時に作業気分天気をランダム表示する脱力系Skillです。')
    print('実用性はありませんが、チームの雰囲気を和ませます。')
    print('明示的な呼び出しや、Gitコミット操作時に自動発動します。')

def parse_args():
    parser = argparse.ArgumentParser(description='commit-mood-forecast: コミット時に気分天気予報を表示するスクリプト')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('forecast', help='気分天気予報を表示')
    subparsers.add_parser('list', help='全ての気分天気パターンを表示')
    subparsers.add_parser('summary', help='Skillの概要説明を表示')

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'forecast' or args.command is None:
        try:
            print_mood_forecast()
        except Exception as e:
            print(f'エラーが発生しました: {e}', file=sys.stderr)
            sys.exit(1)
    elif args.command == 'list':
        list_moods()
    elif args.command == 'summary':
        summary()
    else:
        print('不明なコマンドです。--help を参照してください。', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
