import argparse
import random
import sys
import datetime
import os
from typing import List, Optional

PROPHECY_TEMPLATES = [
    "エラー: 明日あなたは{count}回pushに失敗します",
    "警告: 来週GitHubが逆行します",
    "注意: コードレビューで{topic}について哲学的質問を受けます",
    "予言: {days}日後にnpm installが謎の失敗をします",
    "警告: あなたのエディタが突然{weirdness}になります",
    "エラー: {date}にmake buildが未定義のエラーを返します",
    "注意: {days}日後、VSCodeが自動的に再起動します",
    "警告: 来週、git pullで{oddity}が発生します",
    "予言: あなたのリポジトリに{number}個の未解決issueが現れます",
    "エラー: {date}、デバッグ中に{event}が発生します"
]

TOPICS = [
    "変数命名", "設計思想", "テスト戦略", "バグの存在意義", "型システムの哲学"
]
WEIRDNESS = [
    "詩的", "逆再生", "色覚テストモード", "AI化", "暗号化"
]
ODDITIES = [
    "時空の歪み", "未定義の警告", "哲学的分岐", "謎の競合", "幽霊コミット"
]
EVENTS = [
    "タイムゾーンが消失", "変数が自動で消去", "コメントが詩になる", "関数名がシャッフル", "設定ファイルが消失"
]

HISTORY_FILE = os.path.expanduser("~/.random_os_fake_error_prophecy_history")


def generate_prophecy() -> str:
    template = random.choice(PROPHECY_TEMPLATES)
    now = datetime.datetime.now()
    count = random.randint(1, 5)
    days = random.randint(1, 7)
    date = (now + datetime.timedelta(days=random.randint(1, 14))).strftime("%Y-%m-%d")
    topic = random.choice(TOPICS)
    weirdness = random.choice(WEIRDNESS)
    oddity = random.choice(ODDITIES)
    event = random.choice(EVENTS)
    number = random.randint(1, 20)
    prophecy = template.format(
        count=count,
        days=days,
        date=date,
        topic=topic,
        weirdness=weirdness,
        oddity=oddity,
        event=event,
        number=number
    )
    return prophecy


def print_prophecy():
    prophecy = generate_prophecy()
    print(prophecy)
    append_history(prophecy)


def append_history(prophecy: str):
    try:
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
            timestamp = datetime.datetime.now().isoformat()
            f.write(f"[{timestamp}] {prophecy}\n")
    except Exception:
        pass  # 履歴保存失敗は無視


def list_history(limit: Optional[int] = 10):
    if not os.path.exists(HISTORY_FILE):
        print("履歴はありません。")
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines = lines[-limit:] if limit else lines
    for line in lines:
        print(line.strip())


def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴はありません。")
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    total = len(lines)
    topics = {}
    for line in lines:
        for t in TOPICS:
            if t in line:
                topics[t] = topics.get(t, 0) + 1
    print(f"発行された予言エラー数: {total}")
    print("哲学的質問の内訳:")
    for t, cnt in topics.items():
        print(f"  {t}: {cnt}回")


def parse_args():
    parser = argparse.ArgumentParser(description="未来予言型OSエラーメッセージをランダム表示するスキル")
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='新しい予言エラーメッセージを表示')
    parser_list = subparsers.add_parser('list', help='過去の予言エラーメッセージ履歴を表示')
    parser_list.add_argument('-n', '--num', type=int, default=10, help='表示件数')
    parser_summary = subparsers.add_parser('summary', help='予言エラー履歴のサマリーを表示')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'log' or args.command is None:
        print_prophecy()
    elif args.command == 'list':
        list_history(args.num)
    elif args.command == 'summary':
        summary_history()
    else:
        print("不明なコマンドです。--help を参照してください。")

if __name__ == '__main__':
    main()
