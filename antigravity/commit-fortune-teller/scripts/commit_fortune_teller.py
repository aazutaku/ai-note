import sys
import argparse
import random
import datetime

tarot_cards = [
    {"name": "愚者", "meaning": "大胆な一歩、でも注意も必要。"},
    {"name": "魔術師", "meaning": "新しいアイデアがひらめく日。"},
    {"name": "女教皇", "meaning": "冷静な判断が吉。"},
    {"name": "女帝", "meaning": "豊かな成果が期待できる。"},
    {"name": "皇帝", "meaning": "自信を持って進もう。"},
    {"name": "法王", "meaning": "伝統やルールを大切に。"},
    {"name": "恋人", "meaning": "選択の時。直感を信じて。"},
    {"name": "戦車", "meaning": "突き進むべし。"},
    {"name": "力", "meaning": "忍耐が報われる。"},
    {"name": "隠者", "meaning": "じっくり考える時間を。"},
    {"name": "運命の輪", "meaning": "予想外の展開が待っているかも。"},
    {"name": "正義", "meaning": "バランスと公平さを意識。"},
    {"name": "吊るされた男", "meaning": "視点を変えると道が開ける。"},
    {"name": "死神", "meaning": "終わりは新たな始まり。"},
    {"name": "節制", "meaning": "無理せず調和を大切に。"},
    {"name": "悪魔", "meaning": "誘惑に注意。"},
    {"name": "塔", "meaning": "思わぬトラブルに注意。"},
    {"name": "星", "meaning": "希望を持って進もう。"},
    {"name": "月", "meaning": "不安に惑わされないで。"},
    {"name": "太陽", "meaning": "すべてがうまくいく日。"},
    {"name": "審判", "meaning": "過去を振り返る好機。"},
    {"name": "世界", "meaning": "完成と達成。"}
]

fortunes = [
    "大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"
]

advices = [
    "テストを忘れずに！",
    "変更内容をもう一度見直すと吉。",
    "休憩を挟むと良いアイデアが浮かぶかも。",
    "レビュー依頼をしてみよう。",
    "コミットメッセージは丁寧に。",
    "深夜のコミットは控えめに。",
    "pushの前にpullを忘れずに。",
    "気分転換にストレッチを。",
    "自信を持って大丈夫。",
    "今日は早めに帰ろう。"
]

def print_fortune():
    today = datetime.date.today().strftime('%Y-%m-%d')
    fortune = random.choice(fortunes)
    card = random.choice(tarot_cards)
    advice = random.choice(advices)
    print("=== Commit Fortune Teller ===")
    print(f"今日の運勢: {fortune}")
    print(f"このコミットは「{card['name']}」…{card['meaning']}")
    print(f"アドバイス: {advice}")
    print("-----------------------------\n")

def log_fortune(logfile):
    today = datetime.date.today().strftime('%Y-%m-%d')
    fortune = random.choice(fortunes)
    card = random.choice(tarot_cards)
    advice = random.choice(advices)
    with open(logfile, 'a', encoding='utf-8') as f:
        f.write(f"[{today}] 運勢: {fortune} | カード: {card['name']} | アドバイス: {advice}\n")

def list_log(logfile, count=10):
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[-count:]:
                print(line.strip())
    except FileNotFoundError:
        print("ログファイルがありません。")

def summary_log(logfile):
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            total = len(lines)
            fortune_count = {k: 0 for k in fortunes}
            for line in lines:
                for fortune in fortunes:
                    if f"運勢: {fortune}" in line:
                        fortune_count[fortune] += 1
            print(f"=== Fortune Summary ({total}件) ===")
            for k, v in fortune_count.items():
                print(f"{k}: {v}回")
    except FileNotFoundError:
        print("ログファイルがありません。")

def main():
    parser = argparse.ArgumentParser(description="コミット占いスクリプト")
    subparsers = parser.add_subparsers(dest='command')

    parser_show = subparsers.add_parser('show', help='占い結果を表示')
    parser_log = subparsers.add_parser('log', help='占い結果をログに記録')
    parser_log.add_argument('--logfile', default='.commit_fortune.log', help='ログファイル名')
    parser_list = subparsers.add_parser('list', help='ログを表示')
    parser_list.add_argument('--logfile', default='.commit_fortune.log', help='ログファイル名')
    parser_list.add_argument('--count', type=int, default=10, help='表示件数')
    parser_summary = subparsers.add_parser('summary', help='ログのサマリー')
    parser_summary.add_argument('--logfile', default='.commit_fortune.log', help='ログファイル名')

    args = parser.parse_args()

    if args.command == 'show' or args.command is None:
        print_fortune()
    elif args.command == 'log':
        log_fortune(args.logfile)
    elif args.command == 'list':
        list_log(args.logfile, args.count)
    elif args.command == 'summary':
        summary_log(args.logfile)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
