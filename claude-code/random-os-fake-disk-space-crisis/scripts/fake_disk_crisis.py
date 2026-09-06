import random
import sys
import argparse
import platform
import time
import threading

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

def get_random_unit():
    units = [
        'カブトムシ2匹分', 'ギャラクシー級', 'バナナ1房', '1.2メガピクセル',
        '宇宙的に枯渇', 'ピザ1枚分', '東京ドーム0.0001個分', 'ドット絵1キャラ分',
        'トースト1枚分', 'ヤドカリの殻半分', 'サイコロ1個分', '豆腐1丁分',
        'ポケットの中身程度', 'ピラミッドの頂点', '砂粒3粒分', '紙飛行機1機分',
        'マッチ箱1箱分', 'おにぎり1個分', 'USBメモリのキャップ分', '蚊の羽音分',
        '1バイト未満', 'ギャラクシーの片隅', 'ブラックホールの影', 'うまい棒1本分',
        'カメの甲羅半分', 'ティッシュ1枚分', '星屑1粒分', 'メロンパン1個分',
        'メガネのレンズ分', 'ペン先1つ分'
    ]
    return random.choice(units)

def get_random_prefix():
    prefixes = [
        '警告', '緊急', '注意', '重大', '至急', '速報', '危機', 'OSからのお知らせ', 'システム警告'
    ]
    return random.choice(prefixes)

def get_random_message():
    templates = [
        'あなたの残ディスク容量は“{}”です',
        'SSDの空きが“{}”',
        'ディスク空き領域は“{}”しかありません',
        '残容量が“{}”分に到達しました',
        'ストレージは“{}”レベルです',
        'あなたのストレージは“{}”しています',
        'ディスク残量: {}',
        '空き容量が“{}”になりました',
        'OS判断: 残容量“{}”'
    ]
    template = random.choice(templates)
    unit = get_random_unit()
    return template.format(unit)

def make_crisis_message():
    prefix = get_random_prefix()
    message = get_random_message()
    return f'[CRISIS] {prefix}: {message}'

def send_desktop_notification(title, message):
    if not PLYER_AVAILABLE:
        return False
    try:
        notification.notify(
            title=title,
            message=message,
            app_name='FakeDiskCrisis',
            timeout=7
        )
        return True
    except Exception:
        return False

def print_terminal_notification(message):
    print(message)

def crisis_once():
    msg = make_crisis_message()
    ok = False
    if PLYER_AVAILABLE:
        ok = send_desktop_notification('ディスク残量危機', msg)
    if not ok:
        print_terminal_notification(msg)

def crisis_loop(interval=60, count=5):
    for i in range(count):
        crisis_once()
        if i < count - 1:
            time.sleep(interval)

def list_examples(num=8):
    for _ in range(num):
        print(make_crisis_message())

def summary():
    print('random-os-fake-disk-space-crisis Skill')
    print('現実離れしたディスク残量危機通知をランダム生成し、デスクトップまたはターミナルに表示します。')
    print('実際のストレージ情報は一切取得しません。')
    print('サブコマンド: once / loop / list / summary')

def parse_args():
    parser = argparse.ArgumentParser(
        description='謎のOSディスク残量危機通知をランダムに生成して表示します。'
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    p_once = subparsers.add_parser('once', help='1回だけ危機通知を表示')
    p_loop = subparsers.add_parser('loop', help='一定間隔で複数回危機通知を表示')
    p_loop.add_argument('--interval', type=int, default=60, help='通知間隔(秒)')
    p_loop.add_argument('--count', type=int, default=5, help='通知回数')
    p_list = subparsers.add_parser('list', help='通知例を複数表示')
    p_list.add_argument('--num', type=int, default=8, help='例の数')
    p_summary = subparsers.add_parser('summary', help='Skill概要を表示')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == 'once':
        crisis_once()
    elif args.command == 'loop':
        crisis_loop(interval=args.interval, count=args.count)
    elif args.command == 'list':
        list_examples(num=args.num)
    elif args.command == 'summary':
        summary()
    else:
        print('不明なコマンドです')

if __name__ == '__main__':
    main()
