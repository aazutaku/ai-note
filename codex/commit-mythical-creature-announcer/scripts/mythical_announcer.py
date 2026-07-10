import sys
import argparse
import random
import datetime
import json

MYTHICAL_CREATURES = [
    {
        "name": "ドラゴン",
        "ascii": r"""
           /\_/\
          ( o.o )
           > ^ <
        """,
        "comments": [
            "ドラゴンが眠りから目覚めた…今日は進捗が静かに進む予感。",
            "ドラゴンが炎を吐いた…コードレビューは熱くなりすぎ注意。",
            "ドラゴンが空を舞う…新機能実装の吉日。"
        ]
    },
    {
        "name": "ユニコーン",
        "ascii": r"""
         //\\
        ( oo )
         \\//
          ||
        """,
        "comments": [
            "ユニコーンが首をかしげている…バグは慎重に扱いましょう。",
            "ユニコーンが虹をかける…今日はテストが通りやすい。",
            "ユニコーンが静かに歩く…コミットメッセージは丁寧に。"
        ]
    },
    {
        "name": "フェニックス",
        "ascii": r"""
          _  _
         ( \/ )
         /    \
        /_/\_\
        """,
        "comments": [
            "フェニックスが炎とともに蘇る…本日はリファクタリング吉日！",
            "フェニックスが羽ばたく…バグ退散の兆し。",
            "フェニックスが灰から生まれる…古いコードに新たな命を。"
        ]
    },
    {
        "name": "ケルベロス",
        "ascii": r"""
        (o_o)(o_o)(o_o)
          /     \
         /_/|\_\
        """,
        "comments": [
            "ケルベロスが吠えている…コミットコメントは短めに。",
            "ケルベロスが鎖を引きちぎる…今日は大胆な変更に注意。",
            "ケルベロスが三つの頭で見守る…細かいバグに気をつけて。"
        ]
    },
    {
        "name": "グリフォン",
        "ascii": r"""
         ,_     _
         |\\_,-~/
        / _  _ |    ,--.
       (  @  @ )   / ,-'
        \  _T_/-._( (
        /         `. \
        |         _  \\
         \ \ ,  /      |
          || |-_\__   /
         ((_/`(____,-'
        """,
        "comments": [
            "グリフォンが空を舞う…今日はレビュー運が上昇中！",
            "グリフォンが羽を広げる…ドキュメント更新の好機。",
            "グリフォンが地を駆ける…進捗が加速するかも。"
        ]
    }
]

HISTORY_FILE = ".mythical_announcer_history.json"


def choose_creature():
    creature = random.choice(MYTHICAL_CREATURES)
    comment = random.choice(creature["comments"])
    return creature, comment


def print_announcement(creature, comment):
    print(f"[{creature['name']}]\n{creature['ascii']}\n{comment}")


def save_history(creature_name, comment):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "creature": creature_name,
        "comment": comment
    }
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []
    history.append(entry)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def list_history(limit=10):
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("履歴がありません。コミットしてみましょう！")
        return
    for entry in history[-limit:]:
        ts = entry["timestamp"]
        cr = entry["creature"]
        cm = entry["comment"]
        print(f"{ts}: {cr} - {cm}")


def summary():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("履歴がありません。")
        return
    count = {}
    for entry in history:
        cr = entry["creature"]
        count[cr] = count.get(cr, 0) + 1
    print("== 神獣出現回数 ==")
    for cr, c in sorted(count.items(), key=lambda x: -x[1]):
        print(f"{cr}: {c}回")
    print(f"合計: {len(history)}回")


def main():
    parser = argparse.ArgumentParser(description="コミット神獣アナウンサー")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser("log", help="新しい神獣アナウンスを表示し履歴に記録")
    parser_list = subparsers.add_parser("list", help="過去のアナウンス履歴を表示")
    parser_list.add_argument("--limit", type=int, default=10, help="表示件数")
    parser_summary = subparsers.add_parser("summary", help="神獣ごとの出現回数まとめ")

    args = parser.parse_args()

    if args.command == "log" or args.command is None:
        creature, comment = choose_creature()
        print_announcement(creature, comment)
        save_history(creature["name"], comment)
    elif args.command == "list":
        list_history(args.limit)
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
