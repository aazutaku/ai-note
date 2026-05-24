import os
import sys
import argparse
import ast
from typing import List, Dict, Optional

EXCLUDE_DIRS = {'.git', 'venv', 'env', 'node_modules', '__pycache__', '.mypy_cache', '.idea', '.vscode'}
MAX_FILES = 30


def find_project_root(start_path: str) -> str:
    """Finds the project root by looking for README.md, pyproject.toml, or setup.py."""
    cur = os.path.abspath(start_path)
    while True:
        for marker in ['README.md', 'pyproject.toml', 'setup.py', 'requirements.txt']:
            if os.path.exists(os.path.join(cur, marker)):
                return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return start_path
        cur = parent


def list_dir_structure(root: str, max_files: int = MAX_FILES) -> List[Dict]:
    """Recursively lists major files and directories, with basic roles."""
    result = []
    count = 0
    for dirpath, dirnames, filenames in os.walk(root):
        # Exclude unwanted dirs
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        rel_dir = os.path.relpath(dirpath, root)
        if rel_dir == '.':
            rel_dir = ''
        # Add directories
        for d in dirnames:
            if count >= max_files:
                break
            result.append({'type': 'dir', 'path': os.path.join(rel_dir, d)})
            count += 1
        # Add files
        for f in filenames:
            if count >= max_files:
                break
            result.append({'type': 'file', 'path': os.path.join(rel_dir, f)})
            count += 1
        if count >= max_files:
            break
    return result


def summarize_file_role(filename: str) -> str:
    """Heuristically determine the role of a file by its name and extension."""
    name = os.path.basename(filename).lower()
    if name in ('readme.md', 'readme'):
        return 'プロジェクト概要'
    if name in ('requirements.txt', 'pyproject.toml', 'package.json'):
        return '依存パッケージ'
    if name.startswith('test') or '/tests' in filename or '\\tests' in filename:
        return 'テストコード'
    if name.endswith('.py'):
        return 'Pythonスクリプト'
    if name.endswith('.js'):
        return 'JavaScriptファイル'
    if name.endswith('.md'):
        return 'ドキュメント'
    if name.endswith('.json'):
        return '設定/データ'
    if name.endswith('.yml') or name.endswith('.yaml'):
        return '設定ファイル'
    return 'ファイル'


def parse_imports(filepath: str) -> List[str]:
    """Parse Python file for imported modules/files (local only)."""
    imports = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=filepath)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
    except Exception:
        pass
    return imports


def get_related_files(open_file: str, project_root: str) -> List[str]:
    """Find files related to the open file (by import or same dir)."""
    related = set()
    if open_file.endswith('.py'):
        imports = parse_imports(open_file)
        for imp in imports:
            # Try to resolve local imports
            parts = imp.split('.')
            for ext in ('.py', '/__init__.py'):
                candidate = os.path.join(project_root, *parts) + ext
                if os.path.isfile(candidate):
                    related.add(os.path.relpath(candidate, project_root))
    # Add files in the same directory
    dirpath = os.path.dirname(open_file)
    if os.path.isdir(dirpath):
        for f in os.listdir(dirpath):
            if f != os.path.basename(open_file):
                related.add(os.path.relpath(os.path.join(dirpath, f), project_root))
    return list(related)


def load_readme_summary(project_root: str) -> Optional[str]:
    for name in ['README.md', 'README.txt', 'README']:
        path = os.path.join(project_root, name)
        if os.path.isfile(path):
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = [l.strip() for l in f.readlines() if l.strip()]
                summary = '\n'.join(lines[:8])
                return summary
    return None


def print_context_map(project_root: str, open_file: Optional[str] = None):
    print('[Context Map Mini View]')
    structure = list_dir_structure(project_root)
    for item in structure:
        role = summarize_file_role(item['path'])
        if item['type'] == 'dir':
            print(f'- {item["path"]}/: {role}')
        else:
            print(f'- {item["path"]}: {role}')
    if open_file:
        rel_open = os.path.relpath(open_file, project_root)
        print(f'\n[{rel_open}] ← あなたが開いているファイル')
        related = get_related_files(open_file, project_root)
        for r in related:
            print(f'  └─ {r}')
    summary = load_readme_summary(project_root)
    if summary:
        print('\n[README要約]\n' + summary)


def main():
    parser = argparse.ArgumentParser(description='Context Map Mini View')
    parser.add_argument('--root', type=str, default='.', help='プロジェクトルート (省略時は自動検出)')
    parser.add_argument('--open-file', type=str, help='現在開いているファイルのパス')
    parser.add_argument('--summary', action='store_true', help='README要約のみ表示')
    args = parser.parse_args()

    project_root = find_project_root(args.root)
    if args.summary:
        summary = load_readme_summary(project_root)
        if summary:
            print('[README要約]\n' + summary)
        else:
            print('READMEが見つかりません')
        return
    print_context_map(project_root, args.open_file)

if __name__ == '__main__':
    main()
