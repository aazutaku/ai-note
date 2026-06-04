import os
import sys
import argparse
import random
import json
import datetime
import pathlib
from typing import List, Dict

# 曲リストとYouTubeリンク（公式・著名なものを例として）
BGM_LIST = [
    {"title": "情熱大陸", "youtube": "https://www.youtube.com/watch?v=2sFv2G2rjGg"},
    {"title": "エヴァンゲリオン", "youtube": "https://www.youtube.com/watch?v=2v6ANlBqgDk"},
    {"title": "サザエさん", "youtube": "https://www.youtube.com/watch?v=3XoaRk8p0lA"},
    {"title": "アンパンマンのマーチ", "youtube": "https://www.youtube.com/watch?v=JpXQk6W3j0U"},
    {"title": "運命（ベートーヴェン）", "youtube": "https://www.youtube.com/watch?v=_4IRMYuE1hI"},
    {"title": "ルパン三世のテーマ", "youtube": "https://www.youtube.com/watch?v=JYIAWbQ0p5c"},
    {"title": "ドラえもんのうた", "youtube": "https://www.youtube.com/watch?v=0WJqQ6qF3Qw"},
    {"title": "世界の車窓から", "youtube": "https://www.youtube.com/watch?v=I9zvZr0Fj5c"},
    {"title": "ガッチャマンの歌", "youtube": "https://www.youtube.com/watch?v=Qwq7BYOnDrM"},
    {"title": "残酷な天使のテーゼ", "youtube": "https://www.youtube.com/watch?v=Ho7y8e7i0tE"}
]

HISTORY_FILE = os.path.expanduser("~/.claude_terminal_bgm_history.json")


def load_history() -> Dict:
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_history(history: Dict):
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f)
    except Exception as e:
        print(f"[WARN] 履歴の保存に失敗しました: {e}", file=sys.stderr)


def is_first_command_today(history: Dict) -> bool:
    today = datetime.date.today().isoformat()
    return history.get('last_date') != today


def update_history(history: Dict):
    today = datetime.date.today().isoformat()
    history['last_date'] = today
    save_history(history)


def suggest_bgm() -> Dict:
    bgm = random.choice(BGM_LIST)
    return bgm


def print_bgm_suggestion(bgm: Dict):
    print("🎵 Terminal Boss BGM Suggestion 🎵")
    print(f"本日のあなたのテーマソングは…『{bgm['title']}』です！")
    print(f"（YouTube: {bgm['youtube']}）")
    if bgm['title'] in ['情熱大陸', 'エヴァンゲリオン', '運命（ベートーヴェン）']:
        print("今日も一日、情熱的に頑張りましょう！")
    elif bgm['title'] in ['サザエさん', 'ドラえもんのうた', 'アンパンマンのマーチ']:
        print("肩の力を抜いて、楽しく作業しましょう。")
    else:
        print("BGMで気分転換しつつ、作業を進めてください！")


def handle_log(args):
    history = load_history()
    if is_first_command_today(history):
        bgm = suggest_bgm()
        print_bgm_suggestion(bgm)
        update_history(history)
    else:
        print("本日のBGM提案はすでに表示済みです。明日またお楽しみに！")


def handle_force(args):
    bgm = suggest_bgm()
    print_bgm_suggestion(bgm)
    history = load_history()
    update_history(history)


def handle_history(args):
    history = load_history()
    if 'last_date' in history:
        print(f"最終発動日: {history['last_date']}")
    else:
        print("まだ一度も発動していません。")


def main():
    parser = argparse.ArgumentParser(description='Terminal Boss BGM Suggester')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='本日の最初のコマンドとしてBGM提案を試みる')
    parser_log.set_defaults(func=handle_log)

    parser_force = subparsers.add_parser('force', help='強制的にBGMを提案する（明示呼び出し用）')
    parser_force.set_defaults(func=handle_force)

    parser_history = subparsers.add_parser('history', help='最終発動日を表示')
    parser_history.set_defaults(func=handle_history)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
