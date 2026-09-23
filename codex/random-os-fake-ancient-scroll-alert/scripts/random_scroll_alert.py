import sys
import random
import argparse
import datetime
import textwrap
from typing import List

SCROLL_BORDERS = {
    'top': '─────────────────────────────',
    'bottom': '─────────────────────────────',
}

# 古文書風ランダム文生成用素材
SCROLL_PHRASES_1 = [
    '西のコードベースにバグの気運漂う。',
    'レビュアーの機嫌は末吉。',
    '古きAPI、静かに息を引き取る時近し。',
    '新しきPR、未だマージされず。',
    'デプロイの神、今日も眠りにつく。',
    '東のCI、赤き灯火を掲ぐ。',
    'リファクタの風、静かに吹く。',
    '本日のコミット、数知れず。',
    'コードの森に迷い人現る。',
    '西方のバグ、未解決のまま。',
]
SCROLL_PHRASES_2 = [
    '行末のスペース、油断大敵なり。',
    'レビュアー、無言の圧力を放つ。',
    'テストの神託、通らぬ時もある。',
    '本日、動作確認は吉。',
    '古きissue、再び目覚める。',
    'mergeの刻、未だ遠し。',
    'ビルドの雲行き、怪しき兆し。',
    'リリースノート、書き忘れ注意。',
    '新しきバグ、静かに忍び寄る。',
    'レビュアーの眼、全てを見通す。',
]
SCROLL_PHRASES_3 = [
    '今日のpush、運を天に任すべし。',
    '古き知見、今も役立つ。',
    'PRの道、険しき山道なり。',
    'レビュアー、昼寝中。',
    'コードの海、深く静かに広がる。',
    'バグの精霊、そっと囁く。',
    'CIの神、微笑みたもう。',
    '本日、警告多し。',
    '西のバグ、東の警告。',
    '静かなる夜、エラー現る。',
]

SCROLL_SECTIONS = [SCROLL_PHRASES_1, SCROLL_PHRASES_2, SCROLL_PHRASES_3]


def generate_scroll_lines() -> List[str]:
    """
    ランダムで古文書風の通知文を3行生成
    """
    lines = []
    for section in SCROLL_SECTIONS:
        lines.append(random.choice(section))
    return lines


def format_scroll(lines: List[str], timestamp: str = None) -> str:
    if not timestamp:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    header = f"[巻物通知: {timestamp}]"
    body = '\n'.join(lines)
    scroll = f"{header}\n{SCROLL_BORDERS['top']}\n{body}\n{SCROLL_BORDERS['bottom']}"
    return scroll


def show_scroll():
    lines = generate_scroll_lines()
    scroll = format_scroll(lines)
    print(scroll)


def log_scroll(logfile: str):
    lines = generate_scroll_lines()
    scroll = format_scroll(lines)
    with open(logfile, 'a', encoding='utf-8') as f:
        f.write(scroll + '\n')
    print(f"[log] {logfile} に巻物通知を追記しました。")


def list_scrolls(logfile: str, count: int = 5):
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            content = f.read()
        scrolls = [s for s in content.strip().split('\n[巻物通知: ') if s]
        scrolls = [('[巻物通知: ' + s).strip() for s in scrolls]
        if not scrolls:
            print("ログに巻物通知がありません。")
            return
        print(f"直近{min(count, len(scrolls))}件の巻物通知:")
        for s in scrolls[-count:]:
            print(s)
            print()
    except FileNotFoundError:
        print(f"ログファイル {logfile} が見つかりません。")


def summary_scrolls(logfile: str):
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            content = f.read()
        scrolls = [s for s in content.strip().split('\n[巻物通知: ') if s]
        print(f"合計 {len(scrolls)} 件の巻物通知が記録されています。")
    except FileNotFoundError:
        print(f"ログファイル {logfile} が見つかりません。")


def main():
    parser = argparse.ArgumentParser(
        description='random-os-fake-ancient-scroll-alert: 謎のOS古文書巻物通知をランダム生成・表示するスクリプト')
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_show = subparsers.add_parser('show', help='巻物通知を1件ランダム生成して表示')

    parser_log = subparsers.add_parser('log', help='巻物通知を生成しログファイルに追記')
    parser_log.add_argument('--logfile', type=str, default='scroll_alert.log', help='ログファイルパス (デフォルト: scroll_alert.log)')

    parser_list = subparsers.add_parser('list', help='ログファイルから直近の巻物通知を表示')
    parser_list.add_argument('--logfile', type=str, default='scroll_alert.log', help='ログファイルパス')
    parser_list.add_argument('--count', type=int, default=5, help='表示件数 (デフォルト: 5)')

    parser_summary = subparsers.add_parser('summary', help='ログファイル内の巻物通知件数を集計')
    parser_summary.add_argument('--logfile', type=str, default='scroll_alert.log', help='ログファイルパス')

    args = parser.parse_args()

    if args.command == 'show':
        show_scroll()
    elif args.command == 'log':
        log_scroll(args.logfile)
    elif args.command == 'list':
        list_scrolls(args.logfile, args.count)
    elif args.command == 'summary':
        summary_scrolls(args.logfile)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
