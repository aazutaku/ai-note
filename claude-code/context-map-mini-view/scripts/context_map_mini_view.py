import os
import argparse
import ast
from collections import defaultdict

EXCLUDE_DIRS = {'.git', '__pycache__', 'venv', 'node_modules', '.mypy_cache', '.idea'}
EXCLUDE_FILES = {'requirements.txt', 'Pipfile.lock'}


def parse_args():
    parser = argparse.ArgumentParser(description='プロジェクトのコンテキストマップを生成します')
    parser.add_argument('target', nargs='?', default=None, help='現在注目しているファイルパス（省略可）')
    parser.add_argument('--root', default='.', help='プロジェクトのルートディレクトリ')
    return parser.parse_args()


def is_excluded(path):
    parts = path.split(os.sep)
    return any(part in EXCLUDE_DIRS for part in parts)


def scan_project(root_dir):
    tree = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # 除外ディレクトリを除去
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        rel_dir = os.path.relpath(dirpath, root_dir)
        for fname in filenames:
            if fname in EXCLUDE_FILES:
                continue
            fpath = os.path.join(rel_dir, fname) if rel_dir != '.' else fname
            if not is_excluded(fpath):
                tree[rel_dir].append(fname)
    return tree


def summarize_readme(root_dir):
    readme_path = os.path.join(root_dir, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, encoding='utf-8') as f:
            lines = f.readlines()
        # 先頭500文字程度を要約として返す
        summary = ''.join(lines[:20])
        return summary.strip()
    return None


def parse_python_imports(file_path):
    """Pythonファイルのimport依存関係を抽出"""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, encoding='utf-8') as f:
            node = ast.parse(f.read(), filename=file_path)
        imports = set()
        for stmt in ast.walk(node):
            if isinstance(stmt, ast.Import):
                for n in stmt.names:
                    imports.add(n.name.split('.')[0])
            elif isinstance(stmt, ast.ImportFrom):
                if stmt.module:
                    imports.add(stmt.module.split('.')[0])
        return list(imports)
    except Exception:
        return []


def find_tests_for_file(tree, target):
    """testsディレクトリ以下でtarget名を含むテストファイルを探索"""
    basename = os.path.basename(target)
    test_files = []
    for d, files in tree.items():
        if d.startswith('tests') or d == 'tests':
            for f in files:
                if basename.replace('.py', '') in f:
                    test_files.append(os.path.join(d, f))
    return test_files


def format_tree(tree, root_dir, annotations=None):
    lines = []
    def walk(d, prefix=''):
        files = tree.get(d, [])
        if d == '.':
            dirname = os.path.basename(os.path.abspath(root_dir))
            lines.append(f'{dirname}/')
        else:
            lines.append(f'{prefix}{os.path.basename(d)}/')
        for f in files:
            ann = ''
            if annotations and os.path.join(d, f) in annotations:
                ann = f' ({annotations[os.path.join(d, f)]})'
            lines.append(f'{prefix}├── {f}{ann}')
        # サブディレクトリ
        subdirs = [k for k in tree if os.path.dirname(k) == d and k != d]
        for sub in sorted(subdirs):
            walk(sub, prefix + '│   ')
    walk('.')
    return '\n'.join(lines)


def main():
    args = parse_args()
    root_dir = args.root
    tree = scan_project(root_dir)
    readme_summary = summarize_readme(root_dir)
    target_file = args.target
    print('[Context Map Mini View]')
    print(format_tree(tree, root_dir))
    if readme_summary:
        print('\n[README要約]')
        print(readme_summary[:300])
    if target_file:
        rel_target = os.path.relpath(target_file, root_dir)
        print(f'\n[現在のファイル: {rel_target}]')
        # 依存先
        if rel_target.endswith('.py'):
            imports = parse_python_imports(os.path.join(root_dir, rel_target))
            if imports:
                print(f'- 依存: {", ".join(imports)}')
        # 影響範囲
        tests = find_tests_for_file(tree, rel_target)
        if tests:
            print(f'- 影響範囲: {", ".join(tests)}')
    print('\n')

if __name__ == '__main__':
    main()
