import sys
import argparse
import random
import time
import threading
import os
import signal
import curses

def random_bar(length=10):
    blocks = ['▁','▂','▃','▄','▅','▆','▇','█']
    return ''.join(random.choice(blocks) for _ in range(length))

def random_report_name():
    titles = [
        'AI導入効果分析2024',
        '業務効率化レポート',
        '月次売上推移',
        '顧客満足度調査',
        '品質改善サマリー',
        'コスト削減案',
        'DX推進進捗',
        '市場動向分析',
        'プロジェクト進行状況',
        'システム障害報告'
    ]
    return random.choice(titles)

def random_tasks():
    states = ['[完了]', '[進行中]', '[要確認]', '[保留]']
    tasks = [
        '月次レポート',
        'コードレビュー',
        '会議資料作成',
        '顧客対応',
        'データ分析',
        'バグ修正',
        '要件定義',
        '設計書更新',
        '進捗報告',
        'テストケース追加'
    ]
    pairs = random.sample(list(zip(random.sample(tasks, 5), random.choices(states, k=5))), 5)
    return ' / '.join(f'{s} {t}' for t, s in pairs)

def random_progress():
    return f"{random.randint(60, 99)}%"

def random_review_count():
    return f"{random.randint(5, 25)}件/週"

def draw_dummy_screen(stdscr):
    stdscr.clear()
    stdscr.border(0)
    h, w = stdscr.getmaxyx()
    lines = [
        "=== DUMMY BUSINESS DASHBOARD ===",
        f"売上推移グラフ: {random_bar(16)}",
        f"今月の進捗: {random_progress()}",
        f"最新レポート: \"{random_report_name()}\"",
        f"コードレビュー: {random_review_count()}",
        f"タスク一覧: {random_tasks()}",
        "===============================",
        "[Esc]で元の画面に戻ります"
    ]
    for idx, line in enumerate(lines):
        x = w//2 - len(line)//2
        y = h//2 - len(lines)//2 + idx
        if 0 <= y < h:
            stdscr.addstr(y, max(0, x), line[:w-2])
    stdscr.refresh()
    while True:
        key = stdscr.getch()
        if key == 27:  # ESC
            break

def show_dummy_screen():
    curses.wrapper(draw_dummy_screen)

def cli():
    parser = argparse.ArgumentParser(description='random-os-fake-boss-key: ダミー業務画面を即座に表示')
    parser.add_argument('--show', action='store_true', help='ダミー画面を表示')
    parser.add_argument('--version', action='version', version='random-os-fake-boss-key 1.0')
    args = parser.parse_args()
    if args.show:
        try:
            show_dummy_screen()
        except Exception as e:
            print(f"[ERROR] 画面表示に失敗しました: {e}")
            sys.exit(1)
    else:
        parser.print_help()

def semantic_trigger(text):
    keywords = ['上司', '監督', '見られて', 'サボり', '切り替え', '監視', '覗かれ', 'ピンチ']
    return any(k in text for k in keywords)

def main():
    if len(sys.argv) > 1:
        cli()
    else:
        print('random-os-fake-boss-key スキル (CLI)')
        print('  --show : ダミー画面を表示')
        print('  例: python fake_boss_key.py --show')
        print('  または、キーワード発話で自動発動')
        # 簡易デモ: 標準入力でキーワード検知
        print('\n[デモ] キーワードを入力してください (例: 上司が来た):')
        try:
            while True:
                text = input('> ')
                if semantic_trigger(text):
                    print('[TRIGGER] キーワード検知! ダミー画面を表示します...')
                    show_dummy_screen()
                elif text.strip().lower() in ('q', 'quit', 'exit'):
                    print('終了します')
                    break
                else:
                    print('通常入力:', text)
        except KeyboardInterrupt:
            print('\n終了します')

if __name__ == '__main__':
    main()
