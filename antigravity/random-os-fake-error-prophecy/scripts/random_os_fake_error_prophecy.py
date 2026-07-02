import sys
import argparse
import random
import datetime
import os
import json
import threading
import time

ERROR_PROPHECIES = [
    "エラー: 明日あなたは3回pushに失敗します",
    "警告: 来週GitHubが逆行します",
    "注意: コードレビューで哲学的質問を受けます",
    "ヒント: あなたの未来のバグは既にここにあります",
    "警告: 2週間後にlsの出力が逆順になります",
    "エラー: 近日中にmake buildが謎の理由で失敗します",
    "注意: あなたのエディタが夢の中で自動保存します",
    "警告: 1ヶ月後にgit logが詩的になります",
    "エラー: 未来の自分がこのコマンドを後悔します",
    "ヒント: あなたのpull requestが宇宙に届きます",
    "警告: 明日、レビューコメントが暗号化されます",
    "注意: あなたのシェルが予言を始めます",
    "エラー: 来週、全てのテストが哲学的失敗になります",
    "警告: 3日後、ファイル名が謎の規則で変化します",
    "ヒント: あなたのコミットメッセージが未来を変えます"
]

TRIGGER_KEYWORDS = [
    'error', 'warning', 'terminal', 'push', 'commit', 'review', 'build', 'test', 'save', 'run', 'edit', 'ls', 'make', 'pull', 'merge', 'checkout', 'branch', 'rebase', 'status', 'log', 'diff', 'clone', 'init', 'add', 'rm', 'mv', 'reset', 'stash', 'pop', 'fetch', 'pr', 'code', 'python', 'pytest', 'vim', 'nano', 'emacs', 'cat', 'less', 'more', 'head', 'tail', 'grep', 'find', 'chmod', 'chown', 'cp', 'mv', 'ssh', 'scp', 'ftp', 'sftp', 'docker', 'compose', 'kubectl', 'npm', 'yarn', 'pip', 'venv', 'env', 'activate', 'deactivate'
]

HISTORY_FILE = os.path.expanduser('~/.random_os_fake_error_prophecy_history.json')
HISTORY_LIMIT = 50

lock = threading.Lock()

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

def save_history(history):
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history[-HISTORY_LIMIT:], f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def pick_random_prophecy():
    return random.choice(ERROR_PROPHECIES)

def should_trigger(command):
    command_lower = command.lower()
    return any(kw in command_lower for kw in TRIGGER_KEYWORDS)

def log_prophecy(command, prophecy):
    with lock:
        history = load_history()
        history.append({
            'timestamp': datetime.datetime.now().isoformat(),
            'command': command,
            'prophecy': prophecy
        })
        save_history(history)

def print_prophecy(prophecy):
    print(prophecy)

def trigger_prophecy(command):
    prophecy = pick_random_prophecy()
    print_prophecy(prophecy)
    log_prophecy(command, prophecy)

def list_history():
    history = load_history()
    for entry in history[-HISTORY_LIMIT:]:
        ts = entry.get('timestamp', '')
        cmd = entry.get('command', '')
        prophecy = entry.get('prophecy', '')
        print(f"[{ts}] {cmd}\n  {prophecy}")

def summary():
    history = load_history()
    count = len(history)
    last = history[-1]['timestamp'] if count else 'N/A'
    print(f"合計予言数: {count}")
    print(f"最新予言日時: {last}")
    prophecies = {}
    for entry in history:
        p = entry['prophecy']
        prophecies[p] = prophecies.get(p, 0) + 1
    print("\n予言別出現回数:")
    for p, c in sorted(prophecies.items(), key=lambda x: -x[1]):
        print(f"  {p}: {c}回")

def interactive_mode():
    print("random-os-fake-error-prophecy インタラクティブモード。コマンドを入力してください (exitで終了)")
    try:
        while True:
            command = input("$ ")
            if command.strip() in ('exit', 'quit'):
                break
            if should_trigger(command):
                # 30%の確率で予言を表示
                if random.random() < 0.3:
                    trigger_prophecy(command)
    except KeyboardInterrupt:
        print("\n終了します。")

def main():
    parser = argparse.ArgumentParser(description='random-os-fake-error-prophecy: 未来予言型OSエラーメッセージをランダム表示')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='コマンドを指定して予言を発動')
    parser_log.add_argument('cmd', nargs=argparse.REMAINDER, help='コマンド内容')

    parser_list = subparsers.add_parser('list', help='過去の予言履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='予言履歴のサマリを表示')
    parser_interactive = subparsers.add_parser('interactive', help='インタラクティブモード')

    args = parser.parse_args()

    if args.command == 'log':
        cmd = ' '.join(args.cmd)
        if should_trigger(cmd):
            trigger_prophecy(cmd)
        else:
            print("(予言なし: コマンドがトリガー条件に該当しません)")
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    elif args.command == 'interactive':
        interactive_mode()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
