import random
import sys
import argparse
import time
import threading
from datetime import datetime
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

ERROR_WORDS = [
    'メモリ', '404', 'セグフォ', 'アクセス拒否', 'バグ', '例外', 'カーネル', 'タイムアウト', 'ファイル消失', 'I/O', '割り込み', 'シグナル', 'パーミッション', 'プロセス', 'クラッシュ', '未定義', 'オーバーフロー', 'デッドロック', 'コアダンプ', 'パス不明', 'ネット切断', 'シンタックス', 'エラー', '落ちる', 'フリーズ', '再起動', 'パニック', 'リセット', '応答なし', 'not found', 'fail', 'exception'
]

SEASON_WORDS = [
    '春霞', '夏の夜', '秋の風', '冬の朝', '桜散る', '雪解け', '紅葉', '梅雨空', '新緑', '霜夜', '夕立', '朝露', '月明かり', '星降る', '雷鳴', '霧深し', '夜長', '陽炎', '涼風', '虫の声', '花冷え', '木枯らし', '初雪', '春まだ遠き', '蝉時雨', '朝焼け', '夕焼け', '夏草', '秋雨', '冬眠', '春の宵'
]

TECH_WORDS = [
    'バグの夜', 'カーネルパニック', '無限ループ', 'デバッグ中', '再起動', 'ログ消失', '未定義', '応答なし', 'パッチ待ち', 'リリース前', '仕様通り', 'プロセス死す', 'クラッシュ', 'シンタックス', 'バグ修正', 'セグフォ落ち', 'タイムアウト', 'メモリ消ゆ', '404', 'アクセス拒否', 'パス消失', '例外投げ', 'ファイル消え', 'ネット切断', 'I/O待ち', '割り込み', 'リセット', '応答なし', 'パーミッション', 'not found', 'fail', 'exception'
]

# 五・七・五の構造を作るためのテンプレート
HAIKU_TEMPLATES = [
    ('{error_word} {verb}', '{season_word}', '{tech_word}'),
    ('{error_word}', '{season_word} {verb}', '{tech_word}'),
    ('{error_word}', '{season_word}', '{tech_word}'),
    ('{error_word} {verb}', '{season_word}', '{tech_word}'),
    ('{error_word}', '{season_word}', '{tech_word}'),
]

VERBS = [
    '消ゆ', '落ちる', '止まる', '消える', '迷う', '止まぬ', '響く', '眠る', '舞う', '消す', '凍る', '揺れる', '叫ぶ', '止まる', '流れる', '壊れる', '止む', '溶ける', '消え去る', '彷徨う'
]

def count_moras(text):
    # ざっくりとした仮名数カウント（日本語の正確な音数は難しいため近似）
    return len(text)

def generate_haiku():
    # それぞれの句を五・七・五に近づける
    for _ in range(10):  # 最大10回試行
        error_word = random.choice(ERROR_WORDS)
        season_word = random.choice(SEASON_WORDS)
        tech_word = random.choice(TECH_WORDS)
        verb = random.choice(VERBS)
        template = random.choice(HAIKU_TEMPLATES)
        first = template[0].format(error_word=error_word, verb=verb, season_word=season_word, tech_word=tech_word)
        second = template[1].format(error_word=error_word, verb=verb, season_word=season_word, tech_word=tech_word)
        third = template[2].format(error_word=error_word, verb=verb, season_word=season_word, tech_word=tech_word)
        if abs(count_moras(first) - 5) <= 2 and abs(count_moras(second) - 7) <= 2 and abs(count_moras(third) - 5) <= 2:
            return (first, second, third)
    # 妥協してそのまま返す
    return (first, second, third)

def notify_haiku(haiku, use_desktop=True):
    title = 'OS Error Haiku'
    message = '\n'.join(haiku)
    if use_desktop and PLYER_AVAILABLE:
        try:
            notification.notify(title=title, message=message, app_name='FakeErrorHaiku')
        except Exception as e:
            print(f"[通知失敗] {e}")
            print(f"[{title}]\n{message}")
    else:
        print(f"[{title}]\n{message}")

def monitor_keywords(keywords, interval, use_desktop):
    try:
        import readline
    except ImportError:
        readline = None
    print('キーワード監視モード開始。Ctrl+Cで終了。')
    try:
        while True:
            try:
                line = input()
            except EOFError:
                break
            if any(kw.lower() in line.lower() for kw in keywords):
                haiku = generate_haiku()
                notify_haiku(haiku, use_desktop)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('\n監視モード終了')

def periodic_notify(interval, use_desktop):
    print(f'定期通知モード: {interval}秒ごとに偽エラーハイクを通知します。Ctrl+Cで終了。')
    try:
        while True:
            haiku = generate_haiku()
            notify_haiku(haiku, use_desktop)
            time.sleep(interval)
    except KeyboardInterrupt:
        print('\n定期通知終了')

def list_examples(n=5):
    for _ in range(n):
        haiku = generate_haiku()
        print(f"[OS Error Haiku]\n{haiku[0]}\n{haiku[1]}\n{haiku[2]}\n")

def main():
    parser = argparse.ArgumentParser(description='random-os-fake-error-haiku-notifier')
    subparsers = parser.add_subparsers(dest='command')

    parser_notify = subparsers.add_parser('notify', help='今すぐ偽エラーハイクを通知')
    parser_notify.add_argument('--no-desktop', action='store_true', help='デスクトップ通知を無効化し標準出力のみ')

    parser_periodic = subparsers.add_parser('periodic', help='定期的に偽エラーハイクを通知')
    parser_periodic.add_argument('--interval', type=int, default=300, help='通知間隔(秒)')
    parser_periodic.add_argument('--no-desktop', action='store_true')

    parser_monitor = subparsers.add_parser('monitor', help='標準入力を監視しキーワード検知で通知')
    parser_monitor.add_argument('--keywords', nargs='+', default=['error', 'fail', 'not found', 'exception'], help='監視キーワード')
    parser_monitor.add_argument('--no-desktop', action='store_true')

    parser_list = subparsers.add_parser('list', help='サンプル偽エラーハイクを複数表示')
    parser_list.add_argument('-n', type=int, default=5, help='表示件数')

    args = parser.parse_args()

    if args.command == 'notify':
        haiku = generate_haiku()
        notify_haiku(haiku, not args.no_desktop)
    elif args.command == 'periodic':
        periodic_notify(args.interval, not args.no_desktop)
    elif args.command == 'monitor':
        monitor_keywords(args.keywords, 0.1, not args.no_desktop)
    elif args.command == 'list':
        list_examples(args.n)
    else:
        parser.print_help()
        print('\n例:')
        print('  python random_os_fake_error_haiku_notifier.py notify')
        print('  python random_os_fake_error_haiku_notifier.py periodic --interval 180')
        print('  python random_os_fake_error_haiku_notifier.py monitor --keywords error fail')
        print('  python random_os_fake_error_haiku_notifier.py list -n 10')

if __name__ == '__main__':
    main()
