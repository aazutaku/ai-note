import sys
import argparse
import random
import re
from typing import List

# 俳句テンプレート（五・七・五）
HAIKU_TEMPLATES = [
    ["{season_word}", "{error_phrase}", "{emotion}"],
    ["{situation}", "{error_phrase}", "{wish}"],
    ["{error_phrase}", "{reflection}", "{emotion}"],
    ["{emotion}", "{error_phrase}", "{next_time}"],
]

SEASON_WORDS = [
    "春の風", "夏の夜", "秋の空", "冬の朝", "遠い空", "夕焼けに", "雨の音", "朝焼けや"
]

EMOTIONS = [
    "ため息を", "心重く", "悩み深し", "苦笑い", "涙ひとつ", "静かなる", "夢のあと", "希望あり"
]

WISHES = [
    "次こそは", "また明日", "今度こそ", "やり直す", "立ち上がる", "諦めず"
]

SITUATIONS = [
    "分かれ道", "未解決", "道半ば", "まだ見えず", "行き止まり", "迷い道"
]

REFLECTIONS = [
    "振り返る", "思い出す", "学び得て", "立ち止まり", "考える", "気づきあり"
]

NEXT_TIMES = [
    "次は成功", "また挑戦", "再チャレンジ", "明日こそは", "もう一度"
]

# 英語エラー用の短句
EN_ERROR_PHRASES = [
    "push failed", "commit failed", "merge conflict", "remote rejected", "auth error", "permission denied"
]

# 日本語エラー用の短句
JP_ERROR_PHRASES = [
    "pushできず", "commit失敗", "衝突あり", "認証失敗", "権限なし", "拒否される"
]

# エラー文からキーワード抽出
ERROR_KEYWORDS = {
    r"push": ["push failed", "pushできず"],
    r"commit": ["commit failed", "commit失敗"],
    r"merge": ["merge conflict", "衝突あり"],
    r"auth": ["auth error", "認証失敗"],
    r"permission": ["permission denied", "権限なし"],
    r"reject": ["remote rejected", "拒否される"],
}

def extract_error_phrase(error_msg: str) -> str:
    lower = error_msg.lower()
    for pat, phrases in ERROR_KEYWORDS.items():
        if re.search(pat, lower):
            return random.choice(phrases)
    # fallback
    if re.search(r'[\u3040-\u30ff\u4e00-\u9fff]', error_msg):
        return random.choice(JP_ERROR_PHRASES)
    else:
        return random.choice(EN_ERROR_PHRASES)

def generate_haiku(error_msg: str) -> List[str]:
    template = random.choice(HAIKU_TEMPLATES)
    haiku = []
    # パーツをランダム選択
    for part in template:
        line = part.format(
            season_word=random.choice(SEASON_WORDS),
            error_phrase=extract_error_phrase(error_msg),
            emotion=random.choice(EMOTIONS),
            wish=random.choice(WISHES),
            situation=random.choice(SITUATIONS),
            reflection=random.choice(REFLECTIONS),
            next_time=random.choice(NEXT_TIMES)
        )
        haiku.append(line)
    return haiku

def print_haiku(haiku: List[str]):
    print("俳句:")
    for line in haiku:
        print(line)

def main():
    parser = argparse.ArgumentParser(description="Commit Failure Haikuizer: Gitエラーを俳句に変換して出力")
    parser.add_argument('--error', type=str, help='エラーメッセージを直接指定')
    parser.add_argument('--stdin', action='store_true', help='標準入力からエラー文を受け取る')
    parser.add_argument('--log', type=str, help='俳句をファイルに追記保存')
    args = parser.parse_args()

    if args.error:
        error_msg = args.error.strip()
    elif args.stdin:
        error_msg = sys.stdin.read().strip()
    else:
        print("エラーメッセージを--errorまたは--stdinで指定してください。", file=sys.stderr)
        sys.exit(1)

    haiku = generate_haiku(error_msg)
    print_haiku(haiku)

    if args.log:
        try:
            with open(args.log, 'a', encoding='utf-8') as f:
                f.write(' / '.join(haiku) + '\n')
        except Exception as e:
            print(f"ログ保存に失敗しました: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()
