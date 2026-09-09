import os
import sys
import random
import datetime
import time
import argparse
import platform
from pathlib import Path

# --- 記念日ネタ候補 ---
FAKE_TARGETS = [
    {
        'name': 'あなたの左Ctrlキー',
        'get_date': lambda: get_keyboard_install_date(),
        'timeline': [
            '初めてコーヒーをこぼされる',
            '一度だけCapsLockと間違えられる',
            'ついにキートップが消える'
        ]
    },
    {
        'name': 'プロジェクト最古ファイル',
        'get_date': lambda: get_oldest_file_date('.'),
        'timeline': [
            '初commit',
            '1度だけ消されかける',
            '6年間誰にも編集されず'
        ]
    },
    {
        'name': 'ターミナルの黒背景',
        'get_date': lambda: get_terminal_anniversary(),
        'timeline': [
            '初めてlsコマンドを実行',
            '背景色を白にしようとして諦める',
            '真夜中だけ明るく感じる'
        ]
    },
    {
        'name': 'ホームディレクトリ',
        'get_date': lambda: get_home_dir_birth(),
        'timeline': [
            '初めてファイルが保存される',
            'ゴミ箱が溢れる',
            'パーミッション地獄を経験'
        ]
    },
    {
        'name': 'Python実行環境',
        'get_date': lambda: get_python_install_date(),
        'timeline': [
            'pip installに失敗',
            'バージョンアップで混乱',
            'venvが量産される'
        ]
    }
]

LAST_NOTIFY_FILE = Path.home() / '.random_os_fake_birthday_last'
NOTIFY_INTERVAL_SEC = 60 * 10  # 10分に1回まで

# --- ヘルパー関数群 ---
def get_keyboard_install_date():
    # OSによって取得不可。適当に2009年1月1日を返す
    return datetime.date(2009, 1, 1)

def get_oldest_file_date(root_dir):
    oldest = None
    oldest_time = time.time()
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                stat = os.stat(fp)
                ctime = stat.st_ctime
                if ctime < oldest_time:
                    oldest_time = ctime
                    oldest = fp
            except Exception:
                continue
    if oldest:
        return datetime.date.fromtimestamp(oldest_time)
    return datetime.date.today()

def get_terminal_anniversary():
    # ターミナルの黒背景記念日: 適当に2006年6月6日
    return datetime.date(2006, 6, 6)

def get_home_dir_birth():
    home = Path.home()
    try:
        stat = home.stat()
        return datetime.date.fromtimestamp(stat.st_ctime)
    except Exception:
        return datetime.date(2010, 1, 1)

def get_python_install_date():
    # Python実行ファイルのctime
    pyexe = sys.executable
    try:
        stat = os.stat(pyexe)
        return datetime.date.fromtimestamp(stat.st_ctime)
    except Exception:
        return datetime.date(2015, 5, 5)

def random_timeline(base_timeline, years):
    # 年表をランダムに生成
    base_year = datetime.date.today().year - years
    out = []
    for i, event in enumerate(base_timeline):
        year = base_year + random.randint(i, years)
        out.append(f'- {year}: {event}')
    return out

def format_birthday_message(target, date, timeline):
    years = datetime.date.today().year - date.year
    if years <= 0:
        years = 1
    msg = f'本日、{target}が誕生してから {years} 年目です！\n'
    msg += f'{target}年表:\n'
    msg += '\n'.join(timeline)
    msg += '\nおめでとうございます！\n'
    return msg

def format_file_birthday_message(filepath, date, timeline):
    years = datetime.date.today().year - date.year
    fn = os.path.basename(filepath)
    msg = f'祝: プロジェクト最古ファイル生誕祭（{filepath}, {date} 作成）\n'
    for t in timeline:
        msg += f'{t}\n'
    return msg

def check_last_notify():
    if not LAST_NOTIFY_FILE.exists():
        return True
    try:
        with open(LAST_NOTIFY_FILE, 'r') as f:
            last = float(f.read().strip())
        if time.time() - last > NOTIFY_INTERVAL_SEC:
            return True
        return False
    except Exception:
        return True

def update_last_notify():
    try:
        with open(LAST_NOTIFY_FILE, 'w') as f:
            f.write(str(time.time()))
    except Exception:
        pass

def notify():
    if not check_last_notify():
        print('(通知は連続発動防止のためスキップされました)')
        return
    target = random.choice(FAKE_TARGETS)
    date = target['get_date']()
    years = datetime.date.today().year - date.year
    timeline = random_timeline(target['timeline'], years)
    if target['name'] == 'プロジェクト最古ファイル':
        oldest_file = get_oldest_file_path('.')
        msg = format_file_birthday_message(oldest_file, date, timeline)
    else:
        msg = format_birthday_message(target['name'], date, timeline)
    print(msg)
    update_last_notify()

def get_oldest_file_path(root_dir):
    oldest = None
    oldest_time = time.time()
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                stat = os.stat(fp)
                ctime = stat.st_ctime
                if ctime < oldest_time:
                    oldest_time = ctime
                    oldest = fp
            except Exception:
                continue
    return oldest if oldest else '不明なファイル'

def list_targets():
    print('祝われる対象候補:')
    for t in FAKE_TARGETS:
        print(f'- {t["name"]}')

def summary():
    print('random-os-fake-birthday-notifier 概要')
    print('・突発的に謎の誕生日/記念日通知を出します')
    print('・対象は毎回ランダムです')
    print('・通知内容には無意味な年表やコメントが含まれます')
    print(f'・通知間隔: {NOTIFY_INTERVAL_SEC//60}分以上')

def parse_args():
    parser = argparse.ArgumentParser(description='random-os-fake-birthday-notifier')
    subparsers = parser.add_subparsers(dest='command')
    subparsers.add_parser('notify', help='今すぐ謎の誕生日通知を出す')
    subparsers.add_parser('list', help='祝われる対象リストを表示')
    subparsers.add_parser('summary', help='Skillの概要を表示')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if args.command == 'notify' or args.command is None:
        notify()
    elif args.command == 'list':
        list_targets()
    elif args.command == 'summary':
        summary()
    else:
        print('使い方: python random_os_fake_birthday_notifier.py [notify|list|summary]')
