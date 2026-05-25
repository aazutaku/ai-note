import sys
import argparse
import os
import re
import json
import datetime
try:
    import MeCab
except ImportError:
    print('MeCabが必要です。pip install mecab-python3 を実行してください。')
    sys.exit(1)

HISTORY_FILE = os.path.expanduser('~/.commit_haiku_history.json')

SYLLABLE_PATTERN = re.compile(r'[ぁ-んァ-ン一-龥a-zA-Z0-9ー]+')

# 音節数を推定する関数

def count_syllables(text):
    # ひらがな・カタカナ・漢字・英数字を1音節とみなす簡易実装
    return len(SYLLABLE_PATTERN.findall(text))

# 形態素解析で単語分割

def tokenize(text):
    tagger = MeCab.Tagger('-Owakati')
    words = tagger.parse(text)
    return words.strip().split()

# 指定音数で区切る

def split_by_syllable(words, target):
    result = []
    buf = ''
    count = 0
    for w in words:
        s = count_syllables(w)
        if count + s > target:
            break
        buf += w
        count += s
        if count == target:
            result.append(buf)
            buf = ''
            count = 0
    if buf:
        result.append(buf)
    return result

# 俳句生成本体

def generate_haiku(text):
    words = tokenize(text)
    lines = []
    targets = [5, 7, 5]
    idx = 0
    for t in targets:
        line = ''
        count = 0
        while idx < len(words):
            w = words[idx]
            s = count_syllables(w)
            if count + s > t:
                break
            line += w
            count += s
            idx += 1
            if count == t:
                break
        if line == '':
            # 足りなければ適当に穴埋め
            line = '...' * t
        lines.append(line)
    return lines

# 履歴保存

def save_history(original, haiku):
    entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        'original': original,
        'haiku': haiku
    }
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            try:
                history = json.load(f)
            except Exception:
                history = []
    history.append(entry)
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

# 履歴一覧

def list_history():
    if not os.path.exists(HISTORY_FILE):
        print('履歴がありません。')
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        history = json.load(f)
    for i, entry in enumerate(history[-20:]):
        print(f'[{entry["timestamp"]}]')
        print('原文:', entry['original'])
        print('俳句:')
        for l in entry['haiku']:
            print(l)
        print('-' * 20)

# 俳句による要約

def summary():
    if not os.path.exists(HISTORY_FILE):
        print('履歴がありません。')
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        history = json.load(f)
    print('最近のコミット俳句要約:')
    for entry in history[-5:]:
        for l in entry['haiku']:
            print(l)
        print('')

# メイン関数

def main():
    parser = argparse.ArgumentParser(description='コミットメッセージを俳句に変換')
    subparsers = parser.add_subparsers(dest='command')

    parser_gen = subparsers.add_parser('generate', help='俳句を生成')
    parser_gen.add_argument('message', type=str, help='コミットメッセージ')

    parser_list = subparsers.add_parser('list', help='過去の俳句一覧')
    parser_summary = subparsers.add_parser('summary', help='俳句による要約')

    args = parser.parse_args()

    if args.command == 'generate':
        haiku = generate_haiku(args.message)
        for l in haiku:
            print(l)
        save_history(args.message, haiku)
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
