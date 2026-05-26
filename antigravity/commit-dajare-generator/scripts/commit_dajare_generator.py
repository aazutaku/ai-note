import argparse
import difflib
import os
import re
import subprocess
import sys
from typing import List, Dict, Tuple

# ダジャレ辞書（簡易版）
DAJARE_DICT = {
    'main': 'メインイベント発生！',
    'function': '関数だけに感謝！',
    'bug': 'バグっとな！',
    'fix': 'フィックスでフィニッシュ！',
    'read': '読んでみてね！',
    'lead': 'リードしてみた！',
    'util': 'ユーティリティーって、言うてるって！',
    'test': 'テストでテストステロン！',
    'add': 'アドしてアドバンス！',
    'update': 'アップデートでアップップ！',
    'delete': 'デリートでデリシャス？',
    'refactor': 'リファクターでリフレッシュ！',
    'init': 'イニシャルでイニシアチブ！',
    'config': 'コンフィグでコンフィデンス！',
    'setup': 'セットアップでセットアップップ！',
    'view': 'ビューで美有！',
    'model': 'モデルでモデる！',
    'controller': 'コントローラーでコントロール不能！',
    'script': 'スクリプトでスクリプトーン！',
    'core': 'コアでコアラ！',
    'sample': 'サンプルで散歩る！',
    'log': 'ログでロゴ！',
    'cli': 'CLIでシーライオン！',
    'api': 'APIでアッパイ！',
    'json': 'JSONで情緒ん！',
    'yaml': 'YAMLでやんまる！',
    'csv': 'CSVで吸収！',
    'data': 'データで出た！',
}

EXCLUDE_DIRS = ['.git', 'node_modules', '__pycache__']


def list_staged_files() -> List[str]:
    try:
        result = subprocess.run(['git', 'diff', '--cached', '--name-only'], capture_output=True, text=True)
        files = result.stdout.strip().split('\n')
        return [f for f in files if f and not any(f.startswith(ex) for ex in EXCLUDE_DIRS)]
    except Exception as e:
        print(f"[ERROR] git diff failed: {e}")
        return []


def extract_keywords(filename: str, diff_text: str) -> List[str]:
    # ファイル名から単語抽出
    base = os.path.basename(filename)
    name, _ = os.path.splitext(base)
    words = re.split(r'[_\-.]', name)
    # diffから追加キーワード抽出
    diff_words = set(re.findall(r'\b[a-zA-Z]{3,}\b', diff_text))
    return list(set(words) | diff_words)


def get_diff_for_file(filename: str) -> str:
    try:
        result = subprocess.run(['git', 'diff', '--cached', filename], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return ''


def generate_dajare_message(filename: str, diff_text: str) -> str:
    keywords = extract_keywords(filename, diff_text)
    base = os.path.basename(filename)
    # 優先度: ファイル名キーワード→diffキーワード
    for word in keywords:
        lw = word.lower()
        for key in DAJARE_DICT:
            if key in lw:
                return f"{base} を{word}に修正。{DAJARE_DICT[key]}"
    # 何もヒットしない場合
    return f"{base} を更新しました。コミットでコミッと！"


def propose_commit_messages(files: List[str]) -> List[str]:
    messages = []
    for f in files:
        diff = get_diff_for_file(f)
        msg = generate_dajare_message(f, diff)
        messages.append(msg)
    return messages


def log_commit_messages(messages: List[str], log_path: str = '.commit_dajare_log'):
    try:
        with open(log_path, 'a', encoding='utf-8') as f:
            for msg in messages:
                f.write(msg + '\n')
    except Exception as e:
        print(f"[ERROR] ログ保存失敗: {e}")


def list_log(log_path: str = '.commit_dajare_log'):
    if not os.path.exists(log_path):
        print("[INFO] ログファイルがありません。")
        return
    with open(log_path, 'r', encoding='utf-8') as f:
        print(f.read())


def summary_log(log_path: str = '.commit_dajare_log'):
    if not os.path.exists(log_path):
        print("[INFO] ログファイルがありません。")
        return
    with open(log_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"合計コミットダジャレ数: {len(lines)}")
    if lines:
        print("最近のダジャレ:")
        for l in lines[-5:]:
            print(l.strip())


def main():
    parser = argparse.ArgumentParser(description='commit-dajare-generator: コミット時ダジャレメッセージ生成')
    subparsers = parser.add_subparsers(dest='command', required=True)

    gen_parser = subparsers.add_parser('generate', help='ステージ済みファイルでダジャレ生成')
    gen_parser.add_argument('--log', action='store_true', help='生成ダジャレをログ保存')

    list_parser = subparsers.add_parser('list', help='ダジャレログを表示')
    sum_parser = subparsers.add_parser('summary', help='ダジャレログのサマリー')

    args = parser.parse_args()

    if args.command == 'generate':
        files = list_staged_files()
        if not files:
            print('[INFO] ステージ済みファイルがありません。')
            sys.exit(0)
        messages = propose_commit_messages(files)
        print('[commit-dajare-generator] 提案:')
        for msg in messages:
            print(msg)
        if args.log:
            log_commit_messages(messages)
    elif args.command == 'list':
        list_log()
    elif args.command == 'summary':
        summary_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
