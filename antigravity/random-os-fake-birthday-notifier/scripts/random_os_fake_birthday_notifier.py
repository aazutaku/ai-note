import os
import sys
import random
import time
import datetime
import subprocess
from pathlib import Path
import argparse

def find_oldest_file(directory):
    oldest_file = None
    oldest_time = time.time()
    for root, _, files in os.walk(directory):
        for f in files:
            try:
                fp = os.path.join(root, f)
                ctime = os.path.getctime(fp)
                if ctime < oldest_time:
                    oldest_time = ctime
                    oldest_file = fp
            except Exception:
                continue
    return oldest_file, oldest_time

def random_ctrl_key_birthday():
    base = datetime.datetime(1981, 4, 3)  # IBM PC誕生日
    offset = random.randint(0, 40*365)
    bday = base + datetime.timedelta(days=offset)
    return bday

def random_terminal_anniversary():
    base = datetime.datetime(1970, 1, 1)
    offset = random.randint(0, 50*365)
    bday = base + datetime.timedelta(days=offset)
    return bday

def pick_random_target():
    targets = [
        '左Ctrlキー',
        'プロジェクト最古ファイル',
        'ターミナルの黒背景',
        'ホームディレクトリ',
        '仮想環境',
        'pip freezeリスト',
        'スクリーンショットフォルダ',
        'デスクトップ壁紙',
        '最古のシェル履歴',
        'VSCode設定ファイル',
        'SSH鍵ファイル',
    ]
    return random.choice(targets)

def build_fake_timeline(birth_year):
    now = datetime.datetime.now().year
    events = [
        f"{birth_year}: 誕生",
        f"{birth_year + random.randint(1,3)}: 謎の変更",
        f"{birth_year + random.randint(4,7)}: 黒歴史追加",
        f"{birth_year + random.randint(8,12)}: 存在を忘れられる",
        f"{now}: 祝われる"
    ]
    return events

def random_comment():
    comments = [
        "ここまで生き延びたことに敬意を表します。",
        "なぜか消されずに残っています。",
        "本日だけは主役です。",
        "あなたの作業環境に彩りを添えています。",
        "そろそろ整理してもいいかもしれません。",
        "祝っても意味はありません。",
        "今日も静かに存在しています。"
    ]
    return random.choice(comments)

def notify_desktop(title, message):
    # Linux notify-send, Windows fallback: print
    try:
        if sys.platform.startswith('linux'):
            subprocess.run(['notify-send', title, message])
        elif sys.platform.startswith('darwin'):
            subprocess.run(['osascript', '-e', f'display notification "{message}" with title "{title}"'])
        else:
            print(f"[{title}] {message}")
    except Exception:
        print(f"[{title}] {message}")

def generate_birthday_notification():
    target = pick_random_target()
    now = datetime.datetime.now()
    if target == 'プロジェクト最古ファイル':
        cwd = os.getcwd()
        file, ctime = find_oldest_file(cwd)
        if file:
            bday = datetime.datetime.fromtimestamp(ctime)
            name = os.path.basename(file)
            title = f"OS公式通知: {name} の誕生日"
            year = bday.year
        else:
            bday = now
            title = "OS公式通知: 謎のファイルの誕生日"
            year = now.year
    elif target == '左Ctrlキー':
        bday = random_ctrl_key_birthday()
        title = "OS公式通知: あなたの左Ctrlキーの誕生日"
        year = bday.year
    elif target == 'ターミナルの黒背景':
        bday = random_terminal_anniversary()
        title = "OS公式通知: ターミナルの黒背景記念日"
        year = bday.year
    elif target == 'ホームディレクトリ':
        home = str(Path.home())
        ctime = os.path.getctime(home)
        bday = datetime.datetime.fromtimestamp(ctime)
        title = "OS公式通知: ホームディレクトリ誕生日"
        year = bday.year
    elif target == '仮想環境':
        bday = now - datetime.timedelta(days=random.randint(30, 365*3))
        title = "OS公式通知: 仮想環境生誕祭"
        year = bday.year
    elif target == 'pip freezeリスト':
        bday = now - datetime.timedelta(days=random.randint(100, 1000))
        title = "OS公式通知: pip freezeリスト記念日"
        year = bday.year
    elif target == 'スクリーンショットフォルダ':
        screenshots = os.path.join(str(Path.home()), 'Pictures', 'Screenshots')
        if os.path.exists(screenshots):
            ctime = os.path.getctime(screenshots)
            bday = datetime.datetime.fromtimestamp(ctime)
        else:
            bday = now - datetime.timedelta(days=100)
        title = "OS公式通知: スクリーンショットフォルダ誕生日"
        year = bday.year
    elif target == 'デスクトップ壁紙':
        bday = now - datetime.timedelta(days=random.randint(10, 500))
        title = "OS公式通知: デスクトップ壁紙更新記念日"
        year = bday.year
    elif target == '最古のシェル履歴':
        hist = os.path.join(str(Path.home()), '.bash_history')
        if os.path.exists(hist):
            ctime = os.path.getctime(hist)
            bday = datetime.datetime.fromtimestamp(ctime)
        else:
            bday = now - datetime.timedelta(days=365)
        title = "OS公式通知: シェル履歴生誕祭"
        year = bday.year
    elif target == 'VSCode設定ファイル':
        vs_settings = os.path.join(str(Path.home()), '.config', 'Code', 'User', 'settings.json')
        if os.path.exists(vs_settings):
            ctime = os.path.getctime(vs_settings)
            bday = datetime.datetime.fromtimestamp(ctime)
        else:
            bday = now - datetime.timedelta(days=200)
        title = "OS公式通知: VSCode設定ファイル誕生日"
        year = bday.year
    elif target == 'SSH鍵ファイル':
        ssh_key = os.path.join(str(Path.home()), '.ssh', 'id_rsa')
        if os.path.exists(ssh_key):
            ctime = os.path.getctime(ssh_key)
            bday = datetime.datetime.fromtimestamp(ctime)
        else:
            bday = now - datetime.timedelta(days=500)
        title = "OS公式通知: SSH鍵ファイル記念日"
        year = bday.year
    else:
        bday = now
        title = "OS公式通知: 謎の対象の誕生日"
        year = now.year
    timeline = build_fake_timeline(year)
    comment = random_comment()
    message = f"祝: {bday.strftime('%Y年%m月%d日生まれ')}\n年表:\n - " + "\n - ".join(timeline) + f"\nコメント: {comment}"
    return title, message

def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Birthday Notifier')
    parser.add_argument('--once', action='store_true', help='一度だけ即時通知')
    parser.add_argument('--interval', type=int, default=0, help='N分ごとに自動通知')
    parser.add_argument('--count', type=int, default=1, help='通知回数 (interval指定時のみ)')
    args = parser.parse_args()

    if args.once:
        title, message = generate_birthday_notification()
        notify_desktop(title, message)
        print(f"[{title}]\n{message}")
        return
    elif args.interval > 0:
        for i in range(args.count):
            title, message = generate_birthday_notification()
            notify_desktop(title, message)
            print(f"[{title}]\n{message}")
            if i < args.count - 1:
                time.sleep(args.interval * 60)
    else:
        # デフォルト動作: 1/30の確率で通知
        if random.randint(1,30) == 1:
            title, message = generate_birthday_notification()
            notify_desktop(title, message)
            print(f"[{title}]\n{message}")

if __name__ == '__main__':
    main()
