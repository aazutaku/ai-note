import os
import sys
import argparse
import random
from itertools import combinations

REASONS = [
    "息ピッタリ！",
    "お互い真面目すぎて距離感が…",
    "分析されるために生まれたデータ",
    "必要最低限の付き合い",
    "気まぐれ同士、意外とウマが合う",
    "どちらも主役を譲らない",
    "補完し合う関係",
    "片方がもう片方を支えている",
    "似た者同士、時々ケンカも…",
    "性格が真逆、でもなぜか惹かれ合う",
    "一方的な片思い",
    "仕事だけの関係",
    "運命的な出会い",
    "距離はあるが心は近い",
    "一緒にいるとトラブルが絶えない",
    "名コンビとして有名",
    "片方がもう片方に依存しがち",
    "一緒にいると安心する",
    "お互いの存在に気づいていない",
    "どちらかが主導権を握る",
]

EMOJIS = [
    ("❤️", 80),
    ("💡", 70),
    ("🤝", 50),
    ("🎲", 60),
    ("💔", 40),
]

def get_emoji(score):
    for emoji, threshold in EMOJIS:
        if score >= threshold:
            return emoji
    return "💔"

def random_reason():
    return random.choice(REASONS)

def random_score():
    # 20〜99の間のランダムな整数
    return random.randint(20, 99)

def pairwise_cupid(file_list, max_pairs=10):
    pairs = list(combinations(file_list, 2))
    if len(pairs) > max_pairs:
        pairs = random.sample(pairs, max_pairs)
    results = []
    for f1, f2 in pairs:
        score = random_score()
        emoji = get_emoji(score)
        reason = random_reason()
        results.append({
            "pair": (f1, f2),
            "score": score,
            "emoji": emoji,
            "reason": reason
        })
    return results

def list_files(target_dir, exclude_hidden=True):
    files = []
    for entry in os.listdir(target_dir):
        if os.path.isfile(os.path.join(target_dir, entry)):
            if exclude_hidden and entry.startswith('.'):
                continue
            files.append(entry)
    return files

def print_results(results):
    for r in results:
        f1, f2 = r["pair"]
        print(f"{f1} {r['emoji']} {f2} : 相性度{r['score']}% - 「{r['reason']}」")

def main():
    parser = argparse.ArgumentParser(description="診断ファイルキューピッド: ファイル同士の謎相性診断")
    parser.add_argument('--dir', type=str, default='.', help='診断対象ディレクトリ (デフォルト: カレント)')
    parser.add_argument('--max', type=int, default=10, help='最大ペア数 (デフォルト: 10)')
    parser.add_argument('--include-hidden', action='store_true', help='隠しファイルも含める')
    parser.add_argument('subcommand', nargs='?', default='diagnose', choices=['diagnose', 'list', 'summary'], help='サブコマンド: diagnose/list/summary')
    args = parser.parse_args()

    try:
        files = list_files(args.dir, exclude_hidden=not args.include_hidden)
        if len(files) < 2:
            print("診断対象ファイルが2つ以上必要です。")
            sys.exit(1)
    except Exception as e:
        print(f"ファイル一覧取得エラー: {e}")
        sys.exit(1)

    if args.subcommand == 'list':
        print("診断対象ファイル:")
        for f in files:
            print(f"- {f}")
        return
    elif args.subcommand == 'summary':
        print(f"診断対象ファイル数: {len(files)}")
        print(f"最大ペア数: {args.max}")
        return
    else:  # diagnose
        results = pairwise_cupid(files, max_pairs=args.max)
        print_results(results)

if __name__ == '__main__':
    main()
