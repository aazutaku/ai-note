import random
import sys
import argparse
import platform
import subprocess
import os
import time

# ランダムな例え・単位リスト
descriptors = [
    'カブトムシ2匹分', 'ギャラクシー級に不足', 'カセットテープ1巻分', '宇宙の塵',
    'マグロ1匹分', 'ピコ秒分', 'ブラックホールのエッセンス', 'サバ缶3個分',
    'トランジスタ1個分', 'バナナの皮', '量子もつれレベル', '煮干し5匹分',
    '消しゴムのカス', '猫のひげ1本分', '砂粒2粒分', 'おにぎり1個分',
    '流れ星の残光', '蚊の鳴くほど', '紙飛行機1機分', 'カラオケ1曲分',
    'シャーペンの芯', 'スイカの種', '小惑星帯レベル', '豆腐1丁分',
    '電子レンジのチン', '宇宙船の燃料1滴分', 'アリの涙', '寿司1貫分',
    'ペンギンの足跡', 'たこ焼き1個分', 'ドーナツの穴', 'サイコロ1個分'
]

levels = [
    ('ALERT', '警告'),
    ('CRITICAL', '緊急'),
    ('WARNING', '残り容量'),
    ('NOTICE', '通知'),
    ('ALERT', '残容量'),
    ('CRITICAL', '非常事態'),
    ('WARNING', '容量低下'),
    ('NOTICE', 'ご注意')
]

messages = [
    '{level}: {desc}です。',
    '{level}: SSDの空きが{desc}です。',
    '{level}: 残り容量: {desc}しかありません。',
    '{level}: あなたのディスク空きは{desc}レベルです。',
    '{level}: 残容量: {desc}に到達しました。',
    '{level}: ストレージが{desc}状態です。',
    '{level}: 空き容量が{desc}となりました。',
    '{level}: ディスク残量が{desc}です。',
    '{level}: {desc}の危機です。',
    '{level}: 空き容量が{desc}レベルに低下しています。'
]

def generate_fake_alert():
    level_en, level_ja = random.choice(levels)
    desc = random.choice(descriptors)
    template = random.choice(messages)
    msg = template.format(level=f'[{level_en}] {level_ja}', desc=desc)
    return msg

def send_desktop_notification(title, message):
    system = platform.system()
    if system == 'Darwin':
        # macOS
        try:
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', script], check=True)
        except Exception as e:
            print(f"[ERROR] 通知送信失敗: {e}")
    elif system == 'Linux':
        try:
            subprocess.run(['notify-send', title, message], check=True)
        except Exception as e:
            print(f"[ERROR] 通知送信失敗: {e}")
    elif system == 'Windows':
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=6)
        except ImportError:
            print("[INFO] win10toastがインストールされていません。pip install win10toast で導入してください。")
        except Exception as e:
            print(f"[ERROR] 通知送信失敗: {e}")
    else:
        print(f"[WARN] 未対応OS: {system}。通知は標準出力のみ。")
        print(f"{title}: {message}")

def log_fake_alert(msg, logfile=None):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    line = f"{timestamp} {msg}\n"
    if logfile:
        try:
            with open(logfile, 'a', encoding='utf-8') as f:
                f.write(line)
        except Exception as e:
            print(f"[ERROR] ログファイル書き込み失敗: {e}")
    else:
        print(line, end='')

def list_logs(logfile):
    if not logfile or not os.path.exists(logfile):
        print("[INFO] ログファイルが見つかりません。")
        return
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            for line in f:
                print(line, end='')
    except Exception as e:
        print(f"[ERROR] ログファイル読み込み失敗: {e}")

def summary_logs(logfile):
    if not logfile or not os.path.exists(logfile):
        print("[INFO] ログファイルが見つかりません。")
        return
    try:
        count = 0
        with open(logfile, 'r', encoding='utf-8') as f:
            for _ in f:
                count += 1
        print(f"合計 {count} 件のフェイクディスク警告が記録されています。")
    except Exception as e:
        print(f"[ERROR] ログファイル集計失敗: {e}")

def main():
    parser = argparse.ArgumentParser(description='random-os-fake-disk-space-crisis: フェイクなディスク残量警告を通知するジョークツール')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='フェイク警告を生成し通知・ログする')
    parser_log.add_argument('--count', type=int, default=1, help='生成する警告の数')
    parser_log.add_argument('--interval', type=float, default=1.0, help='警告間の秒数')
    parser_log.add_argument('--logfile', type=str, help='ログファイルパス')
    parser_log.add_argument('--no-notify', action='store_true', help='通知を表示せず標準出力のみ')

    parser_list = subparsers.add_parser('list', help='ログファイルの内容を表示')
    parser_list.add_argument('--logfile', type=str, required=True, help='ログファイルパス')

    parser_summary = subparsers.add_parser('summary', help='ログファイルの件数を集計')
    parser_summary.add_argument('--logfile', type=str, required=True, help='ログファイルパス')

    args = parser.parse_args()

    if args.command == 'log':
        for i in range(args.count):
            msg = generate_fake_alert()
            log_fake_alert(msg, args.logfile)
            if not args.no_notify:
                send_desktop_notification('ディスク残量危機', msg)
            if i < args.count - 1:
                time.sleep(args.interval)
    elif args.command == 'list':
        list_logs(args.logfile)
    elif args.command == 'summary':
        summary_logs(args.logfile)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
