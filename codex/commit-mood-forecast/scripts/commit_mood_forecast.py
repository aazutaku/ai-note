import sys
import argparse
import random
import datetime

MOODS = [
    {
        'icon': '☀️',
        'weather': '快晴',
        'message': '今日は絶好調。どんどん進めましょう。'
    },
    {
        'icon': '☁️',
        'weather': '曇り',
        'message': 'ちょっと迷い気味。無理せず進めてください。'
    },
    {
        'icon': '🌧️',
        'weather': '雨',
        'message': '集中力が散漫かも？気分転換も大事。'
    },
    {
        'icon': '🌪️',
        'weather': '突風',
        'message': 'アイデアが渦巻いています。勢いで進め！'
    },
    {
        'icon': '⛈️',
        'weather': '雷',
        'message': 'やる気ゼロ…コーヒーでも飲みましょう。'
    },
    {
        'icon': '🌤️',
        'weather': '晴れ時々曇り',
        'message': 'まずまずの気分。小休止しつつ進行。'
    },
    {
        'icon': '🌈',
        'weather': '虹',
        'message': '新しい発見の予感。チャレンジを！'
    },
    {
        'icon': '🌙',
        'weather': '夜',
        'message': '夜更かし注意。ほどほどにしましょう。'
    }
]


def random_mood():
    mood = random.choice(MOODS)
    return mood

def print_forecast():
    mood = random_mood()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    print('[commit-mood-forecast]')
    print('本日の作業気分天気予報：')
    print(f'  {mood["icon"]} {mood["weather"]}！{mood["message"]}')


def list_moods():
    print('利用可能な気分天気一覧:')
    for mood in MOODS:
        print(f'  {mood["icon"]} {mood["weather"]}: {mood["message"]}')


def summary():
    print('commit-mood-forecast は、コミット時に気分天気をランダム表示する遊び心Skillです。')
    print('実用性ゼロ、雰囲気づくり100%！')


def main():
    parser = argparse.ArgumentParser(description='commit-mood-forecast: コミット時に気分天気予報を表示')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('forecast', help='本日の気分天気予報を表示（デフォルト動作）')
    subparsers.add_parser('list', help='気分天気の一覧を表示')
    subparsers.add_parser('summary', help='Skillの概要を表示')

    args = parser.parse_args()
    if args.command == 'list':
        list_moods()
    elif args.command == 'summary':
        summary()
    else:
        print_forecast()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'エラー: {e}', file=sys.stderr)
        sys.exit(1)
