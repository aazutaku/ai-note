import argparse
import sys
import re
import logging
from typing import List

# 忍者口調テンプレート集
NINJA_PREFIXES = [
    '拙者思うに、',
    '拙者申す、',
    'ござる…',
    'これは忍法…',
    '影の如く、',
    'これはまさしく、',
    'お主、',
    'この術、',
]
NINJA_SUFFIXES = [
    'でござる。',
    'の巻。',
    '候。',
    '仕る。',
    'にござる。',
    'と存ずる。',
    'でござろうか。',
    'でござるか？',
]
NINJA_WORDS = [
    ('バグ', 'バグの術'),
    ('修正', '修正の巻'),
    ('変数', '変数、影の如し'),
    ('関数', '関数、忍法'),
    ('テスト', '試練の術'),
    ('分かりにくい', '影の如く分かりにくき候'),
    ('分かりやすい', '明けの巻の如く分かりやすき候'),
    ('お願いします', 'お願い仕る'),
    ('してください', 'してくだされ'),
    ('できません', '叶わぬでござる'),
    ('落ちています', '落ちてしまったでござる'),
]

# ログ設定
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def ninjaify_sentence(sentence: str) -> str:
    """
    1文を忍者口調へ変換する
    """
    # 既に忍者語が含まれていたらスキップ
    if re.search(r'(拙者|ござる|候|仕る|忍法|の巻)', sentence):
        return sentence
    # 重要語句を忍者語に置換
    for orig, ninja in NINJA_WORDS:
        sentence = re.sub(orig, ninja, sentence)
    # プレフィックス・サフィックスをランダムに付与
    import random
    prefix = random.choice(NINJA_PREFIXES) if random.random() < 0.7 else ''
    suffix = random.choice(NINJA_SUFFIXES) if random.random() < 0.8 else ''
    # 句読点を調整
    sentence = sentence.strip()
    if not sentence.endswith(('。', '！', '？', '.', '!', '?')):
        sentence += '。'
    return f"{prefix}{sentence}{suffix}"

def ninjaify_text(text: str) -> str:
    """
    複数文を忍者口調に変換
    """
    # 文区切り
    sentences = re.split(r'(?<=[。.!?])\s*', text)
    ninja_sentences = [ninjaify_sentence(s) for s in sentences if s.strip()]
    return '\n'.join(ninja_sentences)

def process_file(input_path: str, output_path: str = None):
    try:
        with open(input_path, encoding='utf-8') as f:
            text = f.read()
        ninja_text = ninjaify_text(text)
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(ninja_text)
            print(f"変換結果を {output_path} に保存したでござる。")
        else:
            print(ninja_text)
    except Exception as e:
        logging.error(f"ファイル処理中にエラー: {e}")
        sys.exit(1)

def cli():
    parser = argparse.ArgumentParser(description='PRコメントを忍者口調に変換するでござる。')
    subparsers = parser.add_subparsers(dest='command')

    # 変換コマンド
    parser_convert = subparsers.add_parser('convert', help='テキストを忍者口調に変換')
    parser_convert.add_argument('text', nargs='?', help='変換したいテキスト')
    parser_convert.add_argument('-f', '--file', help='テキストファイルから変換')
    parser_convert.add_argument('-o', '--output', help='変換後の出力ファイルパス')

    # テストコマンド
    parser_test = subparsers.add_parser('test', help='サンプル変換を表示')

    args = parser.parse_args()

    if args.command == 'convert':
        if args.file:
            process_file(args.file, args.output)
        elif args.text:
            print(ninjaify_text(args.text))
        else:
            print('テキストまたはファイルを指定してくだされ。')
            sys.exit(1)
    elif args.command == 'test':
        samples = [
            'この関数はバグがあります',
            '変数名をもっと分かりやすくしてください',
            'テストが落ちています',
            '修正をお願いします',
            'このロジックは分かりにくいです',
        ]
        for s in samples:
            print('原文:', s)
            print('忍者:', ninjaify_text(s))
            print('---')
    else:
        parser.print_help()

def main():
    cli()

if __name__ == '__main__':
    main()
