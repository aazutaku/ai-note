import argparse
import sys
import re
import random

NINJA_PREFIXES = [
    '拙者思うに、',
    'ござる…',
    '拙者より申し上げ候、',
    '影のように、',
    '忍びの者として申す、',
    'この術、',
    '隠密ながら、',
    '御免、',
    'さて、',
]
NINJA_SUFFIXES = [
    'でござる。',
    'に候。',
    'と存じまする。',
    'かと存じ申す。',
    'と見受けられ申す。',
    '拙者感謝の至り。',
    '影ながら応援致す。',
    '忍法、心得た。',
    '幸いにござる。',
]
NINJA_WORDS = [
    (r'バグ', 'バグの術'),
    (r'修正', '修正の術'),
    (r'確認', '見破りの術'),
    (r'変数', '影変数'),
    (r'関数', '忍法関数'),
    (r'整理', '整理の術'),
    (r'削除', '消し去るの術'),
    (r'追加', '加えるの術'),
    (r'問題', '難題'),
    (r'対応', '対応の術'),
    (r'レビュー', '見破りの術'),
    (r'お願いします', 'お願い仕る'),
    (r'できますか', 'してもよろしいか'),
    (r'してください', 'していただければ幸いにござる'),
]


def to_ninja_style(text):
    original = text.strip()
    # 1. 句点ごとに分割
    sentences = re.split(r'(。|！|!|\?|？)', original)
    transformed = ''
    for i in range(0, len(sentences), 2):
        if not sentences[i].strip():
            continue
        sentence = sentences[i]
        ending = sentences[i+1] if i+1 < len(sentences) else ''
        # 2. 単語変換
        for pat, rep in NINJA_WORDS:
            sentence = re.sub(pat, rep, sentence)
        # 3. ランダムでprefix/suffix追加
        prefix = random.choice(NINJA_PREFIXES) if random.random() < 0.7 else ''
        suffix = random.choice(NINJA_SUFFIXES) if random.random() < 0.7 else ''
        # 4. 組み立て
        transformed += f'{prefix}{sentence}{ending}{suffix}\n'
    return transformed.strip()


def translate_file(input_path, output_path=None):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
        ninja_text = to_ninja_style(text)
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(ninja_text)
        else:
            print(ninja_text)
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)


def translate_stdin():
    try:
        print('原文を入力してください（Ctrl+Dで終了）：')
        text = sys.stdin.read()
        ninja_text = to_ninja_style(text)
        print('--- 忍者口調変換結果 ---')
        print(ninja_text)
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='PRコメントを忍者口調に変換するスクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_translate = subparsers.add_parser('translate', help='テキストまたはファイルを忍者口調に変換')
    parser_translate.add_argument('-i', '--input', type=str, help='入力ファイルパス（省略時は標準入力）')
    parser_translate.add_argument('-o', '--output', type=str, help='出力ファイルパス（省略時は標準出力）')

    parser_test = subparsers.add_parser('test', help='サンプル変換例を表示')

    args = parser.parse_args()

    if args.command == 'translate':
        if args.input:
            translate_file(args.input, args.output)
        else:
            translate_stdin()
    elif args.command == 'test':
        samples = [
            'この関数、もう少し整理できますか？',
            'バグが残っているようです。',
            '変数名を修正してください。',
            'レビューお願いします。',
            '対応が必要です。',
        ]
        for s in samples:
            print(f'原文: {s}')
            print(f'忍者: {to_ninja_style(s)}\n')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
