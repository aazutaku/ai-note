import os
import sys
import argparse
import random
import json
from datetime import datetime, date

BGM_LIST = [
    {
        "title": "情熱大陸",
        "description": "情熱を燃やして今日を駆け抜けましょう。",
        "url": "https://www.youtube.com/watch?v=2G8Qb7wE9zQ"
    },
    {
        "title": "サザエさんのテーマ",
        "description": "波平のように落ち着いて頑張りましょう。",
        "url": "https://www.youtube.com/watch?v=6u7x1W9lC3I"
    },
    {
        "title": "新世紀エヴァンゲリオン - 残酷な天使のテーゼ",
        "description": "使徒襲来!? 仕事も全力で迎撃！",
        "url": "https://www.youtube.com/watch?v=t-QSmNReDyI"
    },
    {
        "title": "運命 (ベートーヴェン第5交響曲)",
        "description": "真面目な朝に運命を切り開こう。",
        "url": "https://www.youtube.com/watch?v=fOk8Tm815lE"
    },
    {
        "title": "アンパンマンのマーチ",
        "description": "夜勤も元気100倍！",
        "url": "https://www.youtube.com/watch?v=Q5hZl5w2KfQ"
    },
    {
        "title": "ルパン三世のテーマ",
        "description": "華麗にタスクを盗み去れ！",
        "url": "https://www.youtube.com/watch?v=0n3cUPTKnl0"
    },
    {
        "title": "世界の車窓から",
        "description": "ゆったりとした気分でコマンドを。",
        "url": "https://www.youtube.com/watch?v=3r7pE7Wz9uA"
    },
    {
        "title": "ドラゴンクエスト 序曲",
        "description": "冒険の始まり！",
        "url": "https://www.youtube.com/watch?v=4Qw8xk5QmI8"
    },
    {
        "title": "ポケモンOP - めざせポケモンマスター",
        "description": "今日もゲットだぜ！",
        "url": "https://www.youtube.com/watch?v=JuYeHPFR3f0"
    },
    {
        "title": "銀河鉄道999",
        "description": "どこまでも走り抜けよう。",
        "url": "https://www.youtube.com/watch?v=0Q8K7P7KjEo"
    }
]

STATE_FILE = os.path.expanduser("~/.terminal_boss_bgm_state.json")


def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    try:
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    except Exception:
        return {}


def save_state(state):
    try:
        with open(STATE_FILE, 'w') as f:
            json.dump(state, f)
    except Exception as e:
        print(f"[WARN] 状態ファイルの保存に失敗: {e}")


def suggest_bgm():
    bgm = random.choice(BGM_LIST)
    print("=== Terminal Boss BGM Suggester ===")
    print("本日のあなたのテーマソングは…")
    print(f"『{bgm['title']}』です！")
    print(bgm['description'])
    print(f"(参考: {bgm['url']})")


def should_suggest_today(state):
    today_str = date.today().isoformat()
    return state.get('last_suggested') != today_str


def mark_suggested_today(state):
    today_str = date.today().isoformat()
    state['last_suggested'] = today_str
    save_state(state)


def reset_state():
    if os.path.exists(STATE_FILE):
        os.remove(STATE_FILE)
        print("状態ファイルをリセットしました。")
    else:
        print("状態ファイルは存在しません。")


def show_history(state):
    last = state.get('last_suggested', None)
    if last:
        print(f"最後にBGMを提案した日: {last}")
    else:
        print("まだBGMは提案されていません。")


def main():
    parser = argparse.ArgumentParser(description="Terminal Boss BGM Suggester")
    subparsers = parser.add_subparsers(dest='command')

    parser_suggest = subparsers.add_parser('suggest', help='本日のBGMを提案')
    parser_reset = subparsers.add_parser('reset', help='状態ファイルをリセット')
    parser_history = subparsers.add_parser('history', help='BGM提案履歴を表示')

    args = parser.parse_args()
    state = load_state()

    if args.command == 'reset':
        reset_state()
        return
    elif args.command == 'history':
        show_history(state)
        return
    elif args.command == 'suggest' or args.command is None:
        if should_suggest_today(state):
            suggest_bgm()
            mark_suggested_today(state)
        else:
            print("本日は既にBGMが提案されています。historyで履歴を確認できます。")

if __name__ == '__main__':
    main()
