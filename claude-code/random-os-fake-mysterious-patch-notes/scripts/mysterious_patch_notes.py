import random
import argparse
import sys
import os
import datetime
from typing import List

NEW_FEATURES = [
    "Altキーで未来の天気が予測可能になりました",
    "ターミナルが詩を詠むことがあります",
    "Ctrl+Zで時間を少しだけ巻き戻せるようになりました",
    "ファイル名に絵文字が使えるようになりました",
    "デスクトップのアイコンが気分で並び替わります",
    "CapsLockの状態が月齢に影響されます",
    "エクスプローラーが時々哲学的な質問を投げかけます",
    "スペースキーでジャンプ力が微増",
    "タスクバーに隠しミニゲームが追加されました",
    "スクリーンショットが自動でアート化されます"
]

IMPROVEMENTS = [
    "CapsLockの押下感を向上",
    "スペースキーの跳躍力を微増",
    "ファイル検索の速度を気分で向上",
    "通知音のランダム性を強化",
    "バッテリー残量表示がより曖昧に",
    "ウィンドウの角丸率を日替わりで調整",
    "ログイン画面の謎の安心感を改善",
    "システムフォントが時々変わります",
    "マウスポインタの追従性を気まぐれに最適化",
    "シャットダウン時の余韻を微調整"
]

KNOWN_ISSUES = [
    "たまに幸運が訪れることがあります",
    "一部環境で現実逃避が加速する場合があります",
    "ごく稀に画面が深呼吸します",
    "時折、未定義のエラーが自己解決します",
    "アップデート後に謎の既視感が発生することがあります",
    "システム時刻が未来に進みすぎる場合があります",
    "ごく稀にユーザーが賢くなります",
    "一部のキーが詩的に反応することがあります",
    "再起動時に猫の気配を感じることがあります",
    "ログイン時に運勢が左右されることがあります"
]

FIXES = [
    "シャットダウン時にまれに哲学的質問が表示されるバグを修正",
    "一部ユーザーで現実逃避が暴走する問題を修正",
    "スクリーンショットが逆さまになる不具合を修正",
    "ターミナルが突然歌い出す問題を修正",
    "CapsLockが勝手にONになる現象を修正",
    "ファイル名が詩になるバグを修正",
    "通知音が無音になることがある問題を修正",
    "マウスポインタが迷子になる現象を修正",
    "ログイン画面が時々謎の暗号を表示する問題を修正",
    "アップデート後に現実感が薄れるバグを修正"
]

VERSION_MAJOR = [4, 5, 6]
VERSION_MINOR = list(range(0, 10))
VERSION_PATCH = list(range(0, 20))


def generate_patch_note() -> str:
    version = f"{random.choice(VERSION_MAJOR)}.{random.choice(VERSION_MINOR)}.{random.choice(VERSION_PATCH)}"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    features = random.sample(NEW_FEATURES, k=random.randint(1, 2))
    improvements = random.sample(IMPROVEMENTS, k=random.randint(1, 2))
    issues = random.sample(KNOWN_ISSUES, k=random.randint(1, 2))
    fixes = random.sample(FIXES, k=random.randint(1, 2))
    lines = [f"[OS Patch Notes {version}] ({now})"]
    if features:
        for f in features:
            lines.append(f"新機能: {f}")
    if improvements:
        for i in improvements:
            lines.append(f"改善: {i}")
    if issues:
        for k in issues:
            lines.append(f"既知の問題: {k}")
    if fixes:
        for fx in fixes:
            lines.append(f"修正: {fx}")
    return '\n'.join(lines)


def show_patch_note(note: str, to_terminal: bool = True, to_notify: bool = False):
    if to_terminal:
        print(note)
    if to_notify:
        # Try to use notify-send (Linux), fallback to terminal
        try:
            import subprocess
            subprocess.run([
                'notify-send',
                '謎のOSパッチノート',
                note
            ], check=True)
        except Exception:
            print("[通知失敗] ターミナル出力のみ対応しています。")


def list_past_notes(logfile: str):
    if not os.path.exists(logfile):
        print("ログファイルが存在しません。")
        return
    with open(logfile, 'r', encoding='utf-8') as f:
        print(f.read())


def save_patch_note(note: str, logfile: str):
    with open(logfile, 'a', encoding='utf-8') as f:
        f.write(note + '\n---\n')


def main():
    parser = argparse.ArgumentParser(description='謎のOSパッチノート生成スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    gen_parser = subparsers.add_parser('log', help='新しいパッチノートを生成・表示')
    gen_parser.add_argument('--notify', action='store_true', help='デスクトップ通知も行う (Linux/notify-send)')
    gen_parser.add_argument('--no-terminal', action='store_true', help='ターミナル出力を抑制')
    gen_parser.add_argument('--save', action='store_true', help='生成結果をローカルに保存')
    gen_parser.add_argument('--logfile', type=str, default='patch_note_history.log', help='保存先ファイル名')

    list_parser = subparsers.add_parser('list', help='過去のパッチノート履歴を表示')
    list_parser.add_argument('--logfile', type=str, default='patch_note_history.log', help='履歴ファイル名')

    args = parser.parse_args()

    if args.command == 'log':
        note = generate_patch_note()
        show_patch_note(note, to_terminal=not args.no_terminal, to_notify=args.notify)
        if args.save:
            save_patch_note(note, args.logfile)
    elif args.command == 'list':
        list_past_notes(args.logfile)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
