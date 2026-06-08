import random
import argparse
import sys
from datetime import datetime

def get_random_weather():
    weathers = [
        '快晴', '曇り', '雨', '雷', '嵐', '春の陽気', '秋風', '雪', '濃霧', '乾燥注意報',
        '小春日和', '台風接近', '蒸し暑い', '涼風', '冷え込み'
    ]
    return random.choice(weathers)

def get_samurai_comment(weather):
    comments = {
        '快晴': [
            'コードも冴え渡るでござる！',
            '心晴れやかに進軍いたす！',
            '本日も快調、斬り込み準備は万端！'
        ],
        '曇り': [
            '集中力もやや薄れ申す。',
            '心の曇りを払うべく、気合いを入れるでござる。',
            '油断召されるな、曇天のごとくタスクも重かろう。'
        ],
        '雨': [
            'バグの雫が降り注ぐやもしれぬ。',
            '静かなる雨音、思索の時でござる。',
            '本日は慎重に進むが吉。'
        ],
        '雷': [
            'バグの嵐到来か？油断召されるな！',
            'エラーの雷鳴、心して臨むべし！',
            '一閃、バグを斬り捨てる覚悟を。'
        ],
        '嵐': [
            '仕様変更に備えよ！',
            'タスクの波に呑まれぬよう、構えを崩すな。',
            '嵐の中、己を信じて進むのみ。'
        ],
        '春の陽気': [
            '心穏やかに進軍でござる。',
            '新たな挑戦に花咲かせる時。',
            '春風に乗りて、今日も一歩。'
        ],
        '秋風': [
            '実りの時、成果を刈り取るでござる。',
            '静かな集中、秋の夜長に。',
            '秋風薫る、バグもまた落葉の如し。'
        ],
        '雪': [
            '静寂の中、心研ぎ澄ますべし。',
            '寒さに負けず、コードも白き世界へ。',
            '雪解けの如く、バグも消え去ることを願う。'
        ],
        '濃霧': [
            '仕様不明、慎重に進むが吉。',
            '先行き不透明、油断は禁物。',
            '霧の中、道を見失わぬように。'
        ],
        '乾燥注意報': [
            'アイディアの潤いを忘れずに。',
            '乾いた心に新たな発想を。',
            '水分補給も忘れずに作業いたせ。'
        ],
        '小春日和': [
            '穏やかな気持ちで進めるでござる。',
            '本日は平穏、着実にタスクを。',
            '小春日和、ゆるりと集中。'
        ],
        '台風接近': [
            '緊急対応に備えよ！',
            'タスクの渦に巻き込まれぬよう注意！',
            '台風一過、成果を期待するでござる。'
        ],
        '蒸し暑い': [
            '集中力が蒸発せぬよう気をつけよ。',
            '蒸し暑さに負けず、心は涼やかに。',
            '汗と共にバグも流すでござる。'
        ],
        '涼風': [
            '心地よい風、作業も捗るでござる。',
            '涼やかに、冷静沈着に進め。',
            '雑念を吹き飛ばす涼風なり。'
        ],
        '冷え込み': [
            '手先の冷えにご注意を。',
            '温かき飲み物で心身温めよ。',
            '冷えにも負けず、作業を進めるでござる。'
        ]
    }
    if weather in comments:
        return random.choice(comments[weather])
    else:
        return '本日も精進あるのみでござる！'

def print_samurai_weather():
    weather = get_random_weather()
    comment = get_samurai_comment(weather)
    print('【侍天気予報】')
    print(f'{weather}、{comment}')
    print('---')

def log_weather(logfile):
    weather = get_random_weather()
    comment = get_samurai_comment(weather)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f'{now} | {weather} | {comment}\n'
    try:
        with open(logfile, 'a', encoding='utf-8') as f:
            f.write(entry)
        print(f'ログに記録しました: {entry.strip()}')
    except Exception as e:
        print(f'ログ記録に失敗しました: {e}', file=sys.stderr)

def show_log(logfile, limit=10):
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        if not lines:
            print('ログがありません。')
            return
        print('【侍天気予報ログ】')
        for line in lines[-limit:]:
            print(line.strip())
    except FileNotFoundError:
        print('ログファイルが存在しません。')
    except Exception as e:
        print(f'ログの読み込みに失敗しました: {e}', file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description='terminal-samurai-weathercaster: ターミナル侍天気予報スキル')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='侍天気予報を表示')
    parser_log = subparsers.add_parser('log', help='侍天気予報をログに記録')
    parser_log.add_argument('--file', default='samurai_weather.log', help='ログファイル名')
    parser_show = subparsers.add_parser('show', help='侍天気予報ログを表示')
    parser_show.add_argument('--file', default='samurai_weather.log', help='ログファイル名')
    parser_show.add_argument('--limit', type=int, default=10, help='表示する最新ログ行数')

    args = parser.parse_args()

    if args.command == 'run' or args.command is None:
        print_samurai_weather()
    elif args.command == 'log':
        log_weather(args.file)
    elif args.command == 'show':
        show_log(args.file, args.limit)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
