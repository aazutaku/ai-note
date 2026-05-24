import argparse
import os
import random
import sys
from typing import List, Tuple, Dict, Optional

PAIR_REASONS = [
    ("❤️", "どちらもプロジェクトの心臓部。お互いがいないと動きません。"),
    ("💘", "データを渡してもらうのが日課。まさに理想の関係です。"),
    ("💔", "価値観が合わず、会話が盛り上がらないタイプ。"),
    ("🤝", "お互いに補完し合う、良きパートナー。"),
    ("✨", "偶然の出会いが新しい価値を生みそう。"),
    ("😶", "特に接点はないが、平和な関係。"),
    ("🔥", "ぶつかり合いながらも高め合うライバル。"),
    ("🌱", "これから関係が深まる予感。"),
    ("🌀", "混ぜるな危険。"),
    ("🎯", "目標に向かって一緒に進む同志。")
]

SPECIAL_PAIRS = {
    ("main.py", "settings.yaml"): ("❤️", "どちらもプロジェクトの心臓部。お互いがいないと動きません。"),
    ("README.md", "LICENSE"): ("💔", "価値観が合わず、会話が盛り上がらないタイプ。"),
    ("data.csv", "analysis.ipynb"): ("💘", "データを渡してもらうのが日課。まさに理想の関係です。"),
}

EXCLUDE_FILES = set([".DS_Store", "Thumbs.db", ".gitignore"])


def list_files(directory: str) -> List[str]:
    files = []
    for root, dirs, filenames in os.walk(directory):
        for fname in filenames:
            if fname in EXCLUDE_FILES:
                continue
            rel_path = os.path.relpath(os.path.join(root, fname), directory)
            files.append(rel_path)
    return files


def choose_pairs(files: List[str], max_pairs: int = 5) -> List[Tuple[str, str]]:
    if len(files) < 2:
        return []
    pairs = set()
    # まずスペシャルペアを優先
    for (a, b), _ in SPECIAL_PAIRS.items():
        if a in files and b in files:
            pairs.add(tuple(sorted([a, b])))
    # ランダムにペアを追加
    attempts = 0
    while len(pairs) < max_pairs and attempts < 50:
        a, b = random.sample(files, 2)
        pair = tuple(sorted([a, b]))
        if pair not in pairs:
            pairs.add(pair)
        attempts += 1
    return list(pairs)[:max_pairs]


def get_reason(a: str, b: str) -> Tuple[str, str]:
    key = tuple(sorted([a, b]))
    for (x, y), (emoji, reason) in SPECIAL_PAIRS.items():
        if set([x, y]) == set([a, b]):
            return emoji, reason
    # 謎ロジック: 拡張子や名前の類似度で理由を変える
    ext_a = os.path.splitext(a)[1].lower()
    ext_b = os.path.splitext(b)[1].lower()
    if ext_a == ext_b and ext_a != '':
        return "🤝", "同じジャンルのファイル。共通点が多く話が弾みそう。"
    if a.split(".")[0] == b.split(".")[0]:
        return "🔥", "名前が似ていてライバル心が芽生えがち。"
    # ランダム
    return random.choice(PAIR_REASONS)


def diagnose(files: List[str], max_pairs: int = 5) -> List[Dict[str, str]]:
    pairs = choose_pairs(files, max_pairs)
    results = []
    for a, b in pairs:
        emoji, reason = get_reason(a, b)
        results.append({"file1": a, "file2": b, "emoji": emoji, "reason": reason})
    return results


def print_results(results: List[Dict[str, str]]):
    print("[shindan-file-cupid]")
    for r in results:
        print(f"{r['file1']} {r['emoji']} {r['file2']}")
        print(f"理由: {r['reason']}")


def main():
    parser = argparse.ArgumentParser(description="プロジェクト内のファイル相性診断 (shindan-file-cupid)")
    parser.add_argument("directory", nargs="?", default=".", help="診断対象ディレクトリ (デフォルト: カレント)")
    parser.add_argument("--max-pairs", type=int, default=5, help="表示するペア数 (デフォルト: 5)")
    parser.add_argument("--list", action="store_true", help="診断対象ファイル一覧のみ表示")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"エラー: 指定ディレクトリが存在しません: {args.directory}", file=sys.stderr)
        sys.exit(1)
    files = list_files(args.directory)
    if not files:
        print("診断対象ファイルが見つかりません。", file=sys.stderr)
        sys.exit(1)
    if args.list:
        print("診断対象ファイル一覧:")
        for f in files:
            print(f)
        sys.exit(0)
    results = diagnose(files, args.max_pairs)
    print_results(results)

if __name__ == "__main__":
    main()
