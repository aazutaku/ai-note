import sys
import argparse
import re
import random
from typing import List, Tuple

try:
    import MeCab
except ImportError:
    print('MeCabが必要です。pip install mecab-python3 でインストールしてください。')
    sys.exit(1)

SYLLABLES = [5, 7, 5]

# 日本語の音節数を推定（かな・カナ・漢字混在対応）
def count_on(text: str) -> int:
    # 長音記号や促音、小書き文字も1音とする
    text = re.sub(r'[ァィゥェォャュョッー]', 'あ', text)
    text = re.sub(r'[ぁぃぅぇぉゃゅょっー]', 'あ', text)
    text = re.sub(r'[a-zA-Z0-9]', '', text)
    return len(text)

def split_by_on(words: List[str], targets: List[int]) -> List[List[str]]:
    result = []
    idx = 0
    for t in targets:
        group = []
        count = 0
        while idx < len(words) and count < t:
            word = words[idx]
            on = count_on(word)
            if count + on > t:
                break
            group.append(word)
            count += on
            idx += 1
        if count != t:
            # 足りない場合はダミー挿入
            while count < t:
                group.append(random.choice(['空', '夢', '光', '風', '雲', '夜', '春', '秋', '花']))
                count += 1
        result.append(group)
    return result

def mecab_wakati(text: str) -> List[str]:
    tagger = MeCab.Tagger('-Owakati')
    wakati = tagger.parse(text)
    return wakati.strip().split()

def generate_haiku(text: str) -> str:
    words = mecab_wakati(text)
    if not words:
        return 'コミット内容
五七五で詠む
春の風'
    lines = split_by_on(words, SYLLABLES)
    lines_str = [''.join(line) for line in lines]
    return '\n'.join(lines_str)

def haiku_commit_message(original: str) -> str:
    haiku = generate_haiku(original)
    return f'[commit-haiku]\n{haiku}'

def main():
    parser = argparse.ArgumentParser(description='コミットメッセージを俳句に変換')
    subparsers = parser.add_subparsers(dest='command')

    parser_gen = subparsers.add_parser('generate', help='俳句形式でコミットメッセージを生成')
    parser_gen.add_argument('message', nargs='*', help='コミットメッセージ')

    parser_sample = subparsers.add_parser('sample', help='サンプル俳句を表示')

    args = parser.parse_args()

    if args.command == 'generate':
        if not args.message:
            print('コミットメッセージを指定してください。')
            sys.exit(1)
        original = ' '.join(args.message)
        haiku = haiku_commit_message(original)
        print(haiku)
    elif args.command == 'sample':
        samples = [
            '新機能追加しました',
            'バグ修正とテスト追加',
            'ドキュメントを更新',
            'コードをリファクタ',
            '設定ファイル修正',
            'README更新',
        ]
        for s in samples:
            print(haiku_commit_message(s))
            print()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
