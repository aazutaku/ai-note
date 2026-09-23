import sys
import random
import time
import argparse
import platform
import subprocess
from typing import List

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

SCROLL_FRAMES = [
    '┌───────────── 古文書巻物 ─────────────┐',
    '└─────────────────────────────┘'
]

ANCIENT_PHRASES = [
    '西のコードベースにバグの気運漂う',
    '本日、レビュアーの機嫌は末吉',
    '明日、リファクタリングの風が吹く',
    '東の仕様書、未だ解読されず',
    '南のデプロイ、静かなる嵐を孕む',
    '北のログ、無言の叫びを記す',
    'バグ修正の道、いまだ遠し',
    'レビュアー、沈黙を守る',
    'テストカバレッジ、霧の中に消ゆ',
    '設計書、時の彼方より現る',
    'CI/CDの神、微笑むも気まぐれ',
    '本日、仕様変更の兆しあり',
    'コードレビュー、運命の分かれ道',
    'エラー、深き闇より来たる',
    'デバッグの旅、果てしなく続く',
    '西方のPull Request、未だ開かれず',
    '朝焼けのコミット、静かに積まれる',
    'バージョン管理、混沌の渦中',
    '仕様追加、風の便りに聞こゆ',
    'レビュアーの機嫌、風まかせ'
]

def generate_scroll_lines(n: int = 4) -> List[str]:
    return random.sample(ANCIENT_PHRASES, n)

def render_scroll(lines: List[str]) -> str:
    max_len = max(len(line) for line in lines)
    width = max(max_len, 30)
    top = f'┌─{"─" * width}─┐'
    bottom = f'└─{"─" * width}─┘'
    content = '\n'.join([f'| {line.ljust(width)} |' for line in lines])
    return f'{top}\n{content}\n{bottom}'

def show_terminal_scroll():
    lines = generate_scroll_lines()
    scroll = render_scroll(lines)
    print(scroll)

def show_desktop_notification():
    lines = generate_scroll_lines()
    title = '古文書巻物通知'
    message = '\n'.join(lines)
    if PLYER_AVAILABLE:
        notification.notify(
            title=title,
            message=message,
            app_name='AncientScroll',
            timeout=8
        )
    else:
        # Fallback: try notify-send (Linux), or print
        if platform.system() == 'Linux':
            try:
                subprocess.run([
                    'notify-send', title, message
                ], check=True)
            except Exception:
                print(render_scroll(lines))
        elif platform.system() == 'Darwin':
            osa = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', osa])
        elif platform.system() == 'Windows':
            print(render_scroll(lines))
        else:
            print(render_scroll(lines))

def main():
    parser = argparse.ArgumentParser(description='謎のOS古文書巻物通知を表示します。')
    parser.add_argument('--mode', choices=['terminal', 'desktop'], default='terminal', help='通知の表示方法')
    parser.add_argument('--repeat', type=int, default=1, help='何回通知を出すか')
    parser.add_argument('--interval', type=float, default=10.0, help='通知間隔(秒)')
    parser.add_argument('--list', action='store_true', help='登録されている古文書フレーズ一覧を表示')
    args = parser.parse_args()

    if args.list:
        print('登録済み古文書フレーズ一覧:')
        for p in ANCIENT_PHRASES:
            print(f'- {p}')
        sys.exit(0)

    for i in range(args.repeat):
        if args.mode == 'terminal':
            show_terminal_scroll()
        elif args.mode == 'desktop':
            show_desktop_notification()
        if i < args.repeat - 1:
            time.sleep(args.interval)

if __name__ == '__main__':
    main()
