import argparse
import os
import random
import sys
from typing import List, Tuple, Dict

PAIR_REASONS = [
    ("❤️", "設定と実装、運命の出会い。"),
    ("💔", "価値観の違いで衝突しがち。"),
    ("💞", "データと分析、理想的な関係。"),
    ("🤝", "地味だけど支え合う仲間。"),
    ("✨", "お互いを高め合う存在。"),
    ("😅", "一緒だとちょっと気まずい。"),
    ("💤", "特に絡みはなさそう。"),
    ("🔥", "時々トラブルを起こす危険な関係。"),
    ("🌱", "新しい何かが生まれそう。"),
    ("🔒", "秘密を共有しているかも。"),
]

EXCLUDE_PATTERNS = [
    '.git', '__pycache__', '.DS_Store', 'node_modules',
    '.venv', '.env', '.idea', '.vscode', '.mypy_cache',
    '.pytest_cache', '.cache', '.coverage', '.eggs',
]


def list_files(root: str) -> List[str]:
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        # 除外パターンを適用
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_PATTERNS]
        for fname in filenames:
            if any(pat in fname for pat in EXCLUDE_PATTERNS):
                continue
            relpath = os.path.relpath(os.path.join(dirpath, fname), root)
            files.append(relpath)
    return files


def random_pairings(files: List[str], n_pairs: int = 5) -> List[Tuple[str, str, str, str]]:
    if len(files) < 2:
        return []
    pairs = []
    used = set()
    attempts = 0
    max_attempts = 50
    while len(pairs) < min(n_pairs, len(files)//2) and attempts < max_attempts:
        f1, f2 = random.sample(files, 2)
        key = tuple(sorted([f1, f2]))
        if key in used:
            attempts += 1
            continue
        used.add(key)
        icon, reason = random.choice(PAIR_REASONS)
        pairs.append((f1, icon, f2, reason))
        attempts += 1
    return pairs


def print_pairs(pairs: List[Tuple[str, str, str, str]]):
    print("[診断結果]")
    for f1, icon, f2, reason in pairs:
        print(f"{f1} {icon} {f2}")
        print(f"理由: {reason}")


def main():
    parser = argparse.ArgumentParser(description='shindan-file-cupid: ファイル相性診断ジョークツール')
    parser.add_argument('root', nargs='?', default='.', help='診断対象ディレクトリ (デフォルト: カレント)')
    parser.add_argument('--pairs', type=int, default=5, help='出力するペア数 (デフォルト: 5)')
    parser.add_argument('--list', action='store_true', help='ファイル一覧のみを表示')
    parser.add_argument('--summary', action='store_true', help='ペア診断のサマリーを表示')
    args = parser.parse_args()

    try:
        files = list_files(args.root)
        if not files:
            print('診断対象ファイルが見つかりません。')
            sys.exit(1)
        if args.list:
            print('\n'.join(files))
            sys.exit(0)
        pairs = random_pairings(files, args.pairs)
        if not pairs:
            print('診断可能なファイルペアがありません。')
            sys.exit(1)
        print_pairs(pairs)
        if args.summary:
            print(f"\n診断対象ファイル数: {len(files)}")
            print(f"出力ペア数: {len(pairs)}")
    except Exception as e:
        print(f'エラー: {e}')
        sys.exit(2)

if __name__ == '__main__':
    main()
