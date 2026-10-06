import random
import argparse
import datetime
import os
import sys
import json
import platform
import subprocess

PATCH_NOTES_FILE = os.path.expanduser('~/.random_os_patch_notes.log')

NEW_FEATURES = [
    "Altキーで未来が見えるようになりました。",
    "Ctrl+Zで昨日に戻れるようになりました。",
    "ターミナルが詩を詠むようになりました。",
    "CapsLockで現実逃避モードが起動します。",
    "Alt+Shiftで未来の自分と会話できます。",
    "タスクバーが意思を持ち始めました。",
    "ウィンドウが気分によって色を変えます。",
    "F5で運勢が表示されるようになりました。",
    "ファイル名を思念で変更できます。",
    "コマンド入力時にヒントが謎めいて表示されます。"
]

IMPROVEMENTS = [
    "スペースキーの跳躍力を微増。",
    "ウィンドウの閉じる速度を1.2倍に最適化。",
    "通知音がたまにメロディになります。",
    "スクロールの滑らかさを曖昧に調整。",
    "バッテリー残量表示が哲学的になりました。",
    "マウスカーソルの気分を尊重するようになりました。",
    "クリップボードの記憶力を強化。",
    "ログイン画面の謎が深まりました。",
    "時計の進み方が気まぐれになりました。",
    "ウィンドウスナップの精度を微調整。"
]

KNOWN_ISSUES = [
    "たまに幸運が訪れます。",
    "まれにマウスカーソルが消えたまま戻りません。",
    "稀にウィンドウが自我を持ちます。",
    "ごく稀に全てがうまくいきます。",
    "時間が逆行する場合があります。",
    "ログイン時に現実感が薄れます。",
    "一部ユーザーで幻聴が聞こえる報告あり。",
    "ファイルが自己主張を始めることがあります。",
    "通知が詩的になる場合があります。",
    "設定画面が哲学的質問を投げかけることがあります。"
]

BUG_FIXES = [
    "記憶の断片が稀に漏れ出る現象を修正。",
    "ウィンドウが突然踊り出す問題を修正。",
    "スクリーンセーバーが夢を見るバグを修正。",
    "ファイル名が詩になる現象を修正。",
    "ターミナルが沈黙するバグを修正。",
    "マウスが自発的に動く現象を修正。",
    "通知が未来の出来事を伝える問題を修正。",
    "カレンダーが13月を表示する不具合を修正。",
    "ログイン音が無音になるバグを修正。",
    "一部のウィンドウが哲学的になる問題を修正。"
]


def generate_patch_notes():
    version = f"v{random.randint(10, 15)}.{random.randint(0,9)}.{random.randint(0,9)}"
    notes = {
        "version": version,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "new_features": random.sample(NEW_FEATURES, k=1),
        "improvements": random.sample(IMPROVEMENTS, k=1),
        "known_issues": random.sample(KNOWN_ISSUES, k=1),
        "bug_fixes": random.sample(BUG_FIXES, k=1)
    }
    return notes


def format_patch_notes(notes):
    lines = [f"[OS Patch Notes {notes['version']}]",]
    if notes['new_features']:
        for nf in notes['new_features']:
            lines.append(f"新機能: {nf}")
    if notes['improvements']:
        for imp in notes['improvements']:
            lines.append(f"改善: {imp}")
    if notes['known_issues']:
        for ki in notes['known_issues']:
            lines.append(f"既知の問題: {ki}")
    if notes['bug_fixes']:
        for bf in notes['bug_fixes']:
            lines.append(f"バグ修正: {bf}")
    lines.append("---")
    return '\n'.join(lines)


def notify_desktop(message):
    sys_platform = platform.system()
    try:
        if sys_platform == "Darwin":  # macOS
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "謎のOSパッチノート"'
            ], check=True)
        elif sys_platform == "Linux":
            subprocess.run([
                "notify-send", "謎のOSパッチノート", message], check=True)
        elif sys_platform == "Windows":
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, message, "謎のOSパッチノート", 1)
        else:
            print("[通知未対応OS]", message)
    except Exception as e:
        print(f"[通知エラー]: {e}")


def save_patch_notes(notes):
    try:
        with open(PATCH_NOTES_FILE, 'a', encoding='utf-8') as f:
            f.write(json.dumps(notes, ensure_ascii=False) + '\n')
    except Exception as e:
        print(f"[ファイル保存エラー]: {e}")


def list_patch_notes(limit=10):
    notes_list = []
    if not os.path.exists(PATCH_NOTES_FILE):
        print("No patch notes found.")
        return
    try:
        with open(PATCH_NOTES_FILE, 'r', encoding='utf-8') as f:
            for line in f.readlines()[-limit:]:
                try:
                    notes = json.loads(line.strip())
                    notes_list.append(notes)
                except Exception:
                    continue
        for notes in notes_list:
            print(format_patch_notes(notes))
    except Exception as e:
        print(f"[履歴取得エラー]: {e}")


def summary_patch_notes():
    if not os.path.exists(PATCH_NOTES_FILE):
        print("No patch notes found.")
        return
    try:
        total = 0
        features = set()
        improvements = set()
        issues = set()
        fixes = set()
        with open(PATCH_NOTES_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    notes = json.loads(line.strip())
                    total += 1
                    features.update(notes.get('new_features', []))
                    improvements.update(notes.get('improvements', []))
                    issues.update(notes.get('known_issues', []))
                    fixes.update(notes.get('bug_fixes', []))
                except Exception:
                    continue
        print(f"合計パッチノート数: {total}")
        print(f"新機能ユニーク数: {len(features)}")
        print(f"改善ユニーク数: {len(improvements)}")
        print(f"既知の問題ユニーク数: {len(issues)}")
        print(f"バグ修正ユニーク数: {len(fixes)}")
    except Exception as e:
        print(f"[サマリー取得エラー]: {e}")


def main():
    parser = argparse.ArgumentParser(description='謎のOSパッチノート通知ジェネレータ')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='新しいパッチノートを生成し通知')
    parser_list = subparsers.add_parser('list', help='パッチノート履歴を表示')
    parser_list.add_argument('--limit', type=int, default=5, help='表示件数')
    parser_summary = subparsers.add_parser('summary', help='パッチノート履歴のサマリー')

    args = parser.parse_args()

    if args.command == 'log' or args.command is None:
        notes = generate_patch_notes()
        formatted = format_patch_notes(notes)
        print(formatted)
        notify_desktop(formatted.replace('\n', ' '))
        save_patch_notes(notes)
    elif args.command == 'list':
        list_patch_notes(limit=args.limit)
    elif args.command == 'summary':
        summary_patch_notes()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
