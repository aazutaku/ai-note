import os
import sys
import argparse
import random
import datetime
import time
import platform
from pathlib import Path

# 除外パス
EXCLUDE_PATHS = ['/tmp', '/proc', '/dev', '/run', '/sys']

# 祝う対象候補
STATIC_TARGETS = [
    ('左Ctrlキー', 'あなたの左Ctrlキー'),
    ('ターミナル黒背景', 'ターミナルの黒背景'),
    ('OSバージョン', f'{platform.system()} {platform.release()}'),
    ('ホームディレクトリ', 'あなたのホームディレクトリ'),
]

# シュールなコメント
COMMENTS = [
    'これからも君のシェルライフを支え続けてください',
    '目に優しい黒、永遠なれ',
    '毎日ありがとう',
    '時の流れは早いですね',
    'これからもよろしくお願いします',
    'あなたの作業に静かに寄り添います',
    '祝う理由は特にありません',
    'なぜか今日は特別な日です',
]

# 年表フレーズ
TIMELINE_EVENTS = [
    '初めて生成される',
    '設定が追加される',
    'コメントが増える',
    'バージョンアップ',
    '謎のエラーが発生',
    'みんなに愛される',
    '歴史的な変更',
    '何も起きなかった日',
]

# ファイル探索
def find_oldest_file(base_path):
    oldest_time = None
    oldest_file = None
    for root, dirs, files in os.walk(base_path):
        # 除外パス除去
        if any(root.startswith(ex) for ex in EXCLUDE_PATHS):
            continue
        for f in files:
            try:
                fp = os.path.join(root, f)
                stat = os.stat(fp)
                ctime = stat.st_ctime
                if (oldest_time is None) or (ctime < oldest_time):
                    oldest_time = ctime
                    oldest_file = fp
            except Exception:
                continue
    return oldest_file, oldest_time

# 対象生成
def choose_birthday_target():
    # 50%: 静的
    if random.random() < 0.5:
        label, name = random.choice(STATIC_TARGETS)
        # 年数計算
        if label == 'ターミナル黒背景':
            base_year = 2006
            years = datetime.datetime.now().year - base_year
            date = datetime.datetime(base_year, 7, 2)
            return name, date, years
        elif label == '左Ctrlキー':
            base_year = 1980
            years = datetime.datetime.now().year - base_year
            date = datetime.datetime(base_year, 4, 1)
            return name, date, years
        elif label == 'OSバージョン':
            base_year = 2000 + random.randint(0, 23)
            years = datetime.datetime.now().year - base_year
            date = datetime.datetime(base_year, 1, 1)
            return name, date, years
        elif label == 'ホームディレクトリ':
            home = str(Path.home())
            try:
                stat = os.stat(home)
                ctime = stat.st_ctime
                date = datetime.datetime.fromtimestamp(ctime)
                years = (datetime.datetime.now() - date).days // 365
                return name, date, years
            except Exception:
                return name, datetime.datetime.now(), 0
    else:
        # 50%: ファイル系
        home = str(Path.home())
        oldest_file, oldest_time = find_oldest_file(home)
        if oldest_file and oldest_time:
            date = datetime.datetime.fromtimestamp(oldest_time)
            years = (datetime.datetime.now() - date).days // 365
            name = f'{os.path.basename(oldest_file)}ファイル'
            return name, date, years
        else:
            return '謎の設定ファイル', datetime.datetime.now(), 0

# 年表生成
def make_timeline(date, years):
    timeline = []
    base_year = date.year
    n_events = random.randint(2, 4)
    for i in range(n_events):
        y = base_year + i * (years // max(n_events-1,1))
        event = random.choice(TIMELINE_EVENTS)
        timeline.append(f'- {y}年: {event}')
    return timeline

# 祝福メッセージ生成
def make_birthday_message():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    target, date, years = choose_birthday_target()
    timeline = make_timeline(date, years)
    comment = random.choice(COMMENTS)
    lines = [f'祝: {target}{years}周年！', f'- {date.year}年: 生誕', *timeline, f'コメント: {comment}']
    return '\n'.join(lines)

# 通知メイン
def notify():
    msg = make_birthday_message()
    print(msg)
    # OS通知(任意)
    try:
        if sys.platform == 'darwin':
            os.system(f'''osascript -e 'display notification "{msg}" with title "謎の誕生日通知"' ''')
        elif sys.platform.startswith('linux'):
            os.system(f'notify-send "謎の誕生日通知" "{msg}"')
        elif sys.platform.startswith('win'):
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("謎の誕生日通知", msg, duration=5)
    except Exception:
        pass

# クールダウン管理
COOLDOWN_FILE = Path.home() / '.random_os_fake_birthday_cooldown'
COOLDOWN_SEC = 3600

def check_cooldown():
    if COOLDOWN_FILE.exists():
        try:
            with open(COOLDOWN_FILE, 'r') as f:
                last = float(f.read().strip())
            if time.time() - last < COOLDOWN_SEC:
                return False
        except Exception:
            pass
    with open(COOLDOWN_FILE, 'w') as f:
        f.write(str(time.time()))
    return True

# CLI
def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Birthday Notifier')
    parser.add_argument('command', nargs='?', default='notify', choices=['notify', 'log', 'summary'], help='notify: 通知, log: ログ表示, summary: 概要')
    args = parser.parse_args()

    if args.command == 'notify':
        if check_cooldown():
            notify()
        else:
            print('クールダウン中です。しばらくお待ちください。')
    elif args.command == 'log':
        print('このSkillは通知履歴を保存しません。')
    elif args.command == 'summary':
        print('random-os-fake-birthday-notifier: 謎の対象の誕生日や記念日を祝う迷惑通知を生成します。')

if __name__ == '__main__':
    main()
