import argparse
import sys
import re
import random
import unicodedata
from typing import List, Tuple

SEASON_WORDS = [
    "春の午後", "夏の夜", "秋の風", "冬の朝", "桜咲く", "雪降る", "月明かり", "新緑", "紅葉", "梅雨空", "涼しさ", "落ち葉", "夕焼け", "朝露", "蝉しぐれ"
]

DEFAULT_HAIKU = [
    ("コード直し", "テストも書いて", "春の午後"),
    ("新機能", "追加の喜び", "夏が来る"),
    ("README", "静かに更新", "秋の風")
]

# ひらがな・カタカナ・漢字を一文字ずつカウント（音節数近似）
def count_on(text: str) -> int:
    # 句読点や空白を除去
    text = re.sub(r'[\s。、,.]', '', text)
    count = 0
    for ch in text:
        if unicodedata.name(ch).startswith(('HIRAGANA', 'KATAKANA')):
            count += 1
        elif unicodedata.east_asian_width(ch) in ('F', 'W', 'A'):
            count += 1
        else:
            # 英数字は1単語=1音とみなす
            if ch.isalnum():
                count += 1
    return count

def split_to_haiku_lines(text: str) -> Tuple[str, str, str]:
    # まず句読点・改行で分割
    phrases = re.split(r'[。、,.\n]', text)
    phrases = [p.strip() for p in phrases if p.strip()]
    # 句が足りなければランダム補完
    while len(phrases) < 3:
        phrases.append(random.choice(SEASON_WORDS))
    # 各句を五・七・五に調整
    lines = []
    targets = [5, 7, 5]
    for i, t in enumerate(targets):
        if i < len(phrases):
            phrase = phrases[i]
            on = count_on(phrase)
            if on == t:
                lines.append(phrase)
            elif on < t:
                # 季語で補完
                lines.append(phrase + random.choice(SEASON_WORDS)[:t-on])
            else:
                # 長すぎる場合は切り詰め
                lines.append(phrase[:t])
        else:
            lines.append(random.choice(SEASON_WORDS))
    return tuple(lines)

def generate_haiku_from_message(message: str) -> Tuple[str, str, str]:
    # 何も入力がなければデフォルト俳句
    if not message or len(message.strip()) == 0:
        return random.choice(DEFAULT_HAIKU)
    return split_to_haiku_lines(message)

def print_haiku(haiku: Tuple[str, str, str]):
    for line in haiku:
        print(line)

def parse_args():
    parser = argparse.ArgumentParser(description='コミットメッセージを俳句（五・七・五）に変換します。')
    parser.add_argument('--message', '-m', type=str, help='変換したいコミットメッセージ')
    parser.add_argument('--file', '-f', type=str, help='コミットメッセージを含むファイルパス')
    parser.add_argument('--random', action='store_true', help='完全ランダムな俳句を生成')
    parser.add_argument('--list-season', action='store_true', help='利用可能な季語一覧を表示')
    parser.add_argument('--test', action='store_true', help='テストモード（例文で出力）')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.list_season:
        print("\n".join(SEASON_WORDS))
        sys.exit(0)
    if args.random:
        haiku = (
            random.choice(SEASON_WORDS),
            random.choice(SEASON_WORDS),
            random.choice(SEASON_WORDS)
        )
        print_haiku(haiku)
        sys.exit(0)
    if args.test:
        samples = [
            "バグ修正とテスト追加",
            "READMEを更新しました",
            "仕様変更に対応",
            "ドキュメント整備"
        ]
        for msg in samples:
            print(f"\n[元メッセージ] {msg}")
            haiku = generate_haiku_from_message(msg)
            print_haiku(haiku)
        sys.exit(0)
    message = None
    if args.message:
        message = args.message
    elif args.file:
        try:
            with open(args.file, encoding='utf-8') as f:
                message = f.read()
        except Exception as e:
            print(f"ファイル読み込みエラー: {e}")
            sys.exit(1)
    else:
        print("--message または --file を指定してください。--help で使い方を確認できます。")
        sys.exit(1)
    haiku = generate_haiku_from_message(message)
    print_haiku(haiku)

if __name__ == '__main__':
    main()
