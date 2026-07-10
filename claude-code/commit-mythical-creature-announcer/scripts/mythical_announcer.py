import sys
import random
import argparse
import datetime

MYTHICAL_CREATURES = [
    {
        'name': 'フェニックス',
        'ascii_art': r'''
           (  )   (   )  )
            ) (   )  (  (
            ( )  (    ) )
           _____________
          <_____________> ___
          |             |/ _ \
          |               | | |
          |               |_| |
       ___|             |\___/
      /    \___________/    \
      \_____________________/
        ___\_/___\__/__\_/
''',
        'fortunes': [
            'フェニックスが蘇る…本日はバグ退散の吉日。',
            '炎のごとくリファクタリングせよ。',
            '燃え尽き注意。休憩も大事。'
        ]
    },
    {
        'name': 'ユニコーン',
        'ascii_art': r'''
           \\
            \\
             \\
              \\
                \\
                 (\\
                 ( \\
                 (  \\
                 (   \\
                 (    \\
                /|     \\
               / |      \\
              *  |       \\
                 |        \\
                 |         \\
                 |          \\
''',
        'fortunes': [
            'ユニコーンが首をかしげている…今日は慎重に。',
            '幻想的なバグが現れる予感。',
            '理想を追いすぎると沼にハマるかも。'
        ]
    },
    {
        'name': 'ドラゴン',
        'ascii_art': r'''
          __====-_  _-====__
        _--^^^#####//      \\
       -^##########// (zzz) \\
      _/############//       \\
     /#############((     .   ))
    -###############\\     //
   -#################\\_ //
  _#/|##########/\######( )
 |/ |#/#\#/\#/\#/\#/\#|\|
''',
        'fortunes': [
            'ドラゴンが眠る…進捗は静かに。',
            '火の玉レビューが飛んでくるかも。',
            'バグは焼き払え。'
        ]
    },
    {
        'name': 'ケルベロス',
        'ascii_art': r'''
          __      _
         o'')}____//
          `_/      )
          (_(_/-(_/
''',
        'fortunes': [
            'ケルベロスが吠えている…マージ競合にご用心。',
            '三つの頭で三倍デバッグ。',
            'コミットメッセージは慎重に。'
        ]
    },
    {
        'name': 'グリフォン',
        'ascii_art': r'''
        ,_     _
        |\\_,-~/
        / _  _ |    ,--.
       (  @  @ )   / ,-'
        \  _T_/-._( (
        /         `. \\
        |         _  \\
         \ \ ,  /      |
          || |-_\__   /
         ((_/`(____,-'
''',
        'fortunes': [
            'グリフォンが空を舞う…今日の開発は羽ばたく。',
            '高みを目指しすぎて落下注意。',
            'コードの見通しは良好。'
        ]
    },
    {
        'name': 'バジリスク',
        'ascii_art': r'''
        /^\/^\
      _|__|  O|
 \/     /~     \\
  \____|__________/  \\
         \_______      \\
                 `\     \                 \\
                   |     |                  \\
                  /      /                    \\
                 /     /                       \\
               /      /                         \ \
              /     /                            \  \
            /     /             _----_            \   \
           /     /           _-~      ~-_         |   |
          (      (        _-~    _--_    ~-_     _/   |
           \      ~-____-~    _-~    ~-_    ~-_-~    /
             ~-_           _-~          ~-_       _-~
                ~--______-~                ~-___-~
''',
        'fortunes': [
            'バジリスクの視線…今日はコードレビュー厳しめ。',
            '目が合うとバグが増える。',
            '静かに作業すると吉。'
        ]
    }
]

GENERIC_FORTUNES = [
    '本日の開発運勢: コードレビューは神話級の難易度。バグはそっとしておこう。',
    '本日の開発運勢: コミット数よりも品質を重視せよ。',
    '本日の開発運勢: 今日は進捗が霧の彼方に消えるかも。',
    '本日の開発運勢: レビュー依頼は慎重に。',
    '本日の開発運勢: 神獣の加護でバグ退散！…かもしれない。',
    '本日の開発運勢: 理不尽なバグが降臨する予感。',
    '本日の開発運勢: 仕様変更に注意。',
    '本日の開発運勢: チームメイトに感謝を伝えると吉。',
    '本日の開発運勢: 今日は何も起きない（たぶん）。'
]

def pick_creature():
    creature = random.choice(MYTHICAL_CREATURES)
    fortune = random.choice(creature['fortunes'])
    generic = random.choice(GENERIC_FORTUNES)
    return creature, fortune, generic

def print_announcement():
    creature, fortune, generic = pick_creature()
    border = '─' * 41
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    print(f"{border}")
    print(f"{now}")
    print(f"{creature['name']}が現れた… {fortune}")
    print(f"{border}")
    print(creature['ascii_art'])
    print(f"{border}")
    print(generic)
    print(f"{border}")

def list_creatures():
    print("利用可能な神話生物:")
    for c in MYTHICAL_CREATURES:
        print(f"- {c['name']}")

def summary():
    print("commit-mythical-creature-announcerは、コミット時や明示呼び出しで神獣と運勢をランダム表示します。神獣は以下の通り:")
    for c in MYTHICAL_CREATURES:
        print(f"・{c['name']}: {len(c['fortunes'])}種の運勢コメント")
    print(f"汎用運勢コメント: {len(GENERIC_FORTUNES)}種")

def main():
    parser = argparse.ArgumentParser(description='Mythical Creature Announcer: コミット時に神獣と運勢を表示')
    subparsers = parser.add_subparsers(dest='command')

    parser_announce = subparsers.add_parser('announce', help='神獣と運勢を表示')
    parser_list = subparsers.add_parser('list', help='神獣リストを表示')
    parser_summary = subparsers.add_parser('summary', help='概要を表示')

    args = parser.parse_args()
    if args.command == 'announce' or args.command is None:
        print_announcement()
    elif args.command == 'list':
        list_creatures()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
