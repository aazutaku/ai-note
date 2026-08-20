import sys
import random
import time
import argparse
import curses
from datetime import datetime

DASHBOARD_TEMPLATES = [
    {
        'title': '業務進捗ダッシュボード',
        'fields': [
            lambda: f'プロジェクト: {random.choice(["Alpha", "Beta", "Gamma", "Omega"])}',
            lambda: f'進捗率: {random.randint(60, 99)}%',
            lambda: f'本日タスク: {random.randint(2, 8)}/{random.randint(3, 8)} 完了',
            lambda: f'売上グラフ: ' + ("|" * random.randint(8, 18)),
            lambda: f'リスク: {random.choice(["低", "中", "高"])}',
        ]
    },
    {
        'title': '営業レポート',
        'fields': [
            lambda: f'担当者: {random.choice(["佐藤", "鈴木", "田中", "高橋"])}',
            lambda: f'本日訪問件数: {random.randint(3, 12)}',
            lambda: f'成約数: {random.randint(0, 5)}',
            lambda: f'見込顧客数: {random.randint(10, 40)}',
            lambda: f'次回アクション: {random.choice(["資料送付", "訪問予定", "フォローコール"])}',
        ]
    },
    {
        'title': 'システム監視モニター',
        'fields': [
            lambda: f'CPU使用率: {random.randint(10, 95)}%',
            lambda: f'メモリ使用率: {random.randint(20, 90)}%',
            lambda: f'ネットワーク: {random.choice(["正常", "遅延", "障害"])}',
            lambda: f'アラート: {random.choice(["なし", "1件", "2件"])}',
            lambda: f'最終バックアップ: {datetime.now().strftime("%Y-%m-%d %H:%M")}',
        ]
    }
]

FOOTER = lambda: f'[レポート出力日時: {datetime.now().strftime("%Y-%m-%d %H:%M")}]'

HELP_TEXT = """
ボスキー風ダミー業務画面を即座に表示します。

使い方:
  python fake_boss_key.py [--duration 秒数] [--template N]

オプション:
  --duration 秒数   ダミー画面を表示する秒数 (省略時はEsc/Ctrl+Cで手動終了)
  --template N     テンプレート番号を指定 (0-2, 省略時はランダム)
"""

def render_dashboard(stdscr, template_idx=None):
    curses.curs_set(0)
    stdscr.clear()
    if template_idx is None:
        template = random.choice(DASHBOARD_TEMPLATES)
    else:
        template = DASHBOARD_TEMPLATES[template_idx % len(DASHBOARD_TEMPLATES)]
    maxy, maxx = stdscr.getmaxyx()
    y = 2
    x = 4
    stdscr.addstr(y, x, f'=== {template["title"]} ===', curses.A_BOLD)
    y += 2
    for field in template['fields']:
        stdscr.addstr(y, x, field())
        y += 1
    y += 1
    stdscr.addstr(y, x, '-' * (maxx - 8))
    y += 1
    stdscr.addstr(y, x, FOOTER())
    stdscr.refresh()

def wait_for_exit(stdscr, duration=None):
    if duration is not None:
        time.sleep(duration)
        return
    stdscr.nodelay(True)
    while True:
        try:
            c = stdscr.getch()
            if c in [27, 3]:  # Esc or Ctrl+C
                break
            time.sleep(0.1)
        except KeyboardInterrupt:
            break

def main():
    parser = argparse.ArgumentParser(description='ランダム業務画面ダミー (ボスキー風)')
    parser.add_argument('--duration', type=int, default=None, help='表示秒数 (省略時はEsc/Ctrl+Cで終了)')
    parser.add_argument('--template', type=int, default=None, help='テンプレート番号 (0-2)')
    parser.add_argument('--list', action='store_true', help='テンプレート一覧を表示')
    parser.add_argument('--helptext', action='store_true', help='詳細な使い方を表示')
    args = parser.parse_args()

    if args.helptext:
        print(HELP_TEXT)
        sys.exit(0)
    if args.list:
        for idx, t in enumerate(DASHBOARD_TEMPLATES):
            print(f'{idx}: {t["title"]}')
        sys.exit(0)

    try:
        curses.wrapper(render_and_wait, args.template, args.duration)
    except Exception as e:
        print(f'エラー: {e}', file=sys.stderr)
        sys.exit(1)

def render_and_wait(stdscr, template_idx, duration):
    render_dashboard(stdscr, template_idx)
    wait_for_exit(stdscr, duration)

if __name__ == '__main__':
    main()
