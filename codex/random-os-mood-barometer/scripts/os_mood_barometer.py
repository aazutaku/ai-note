import argparse
import random
import sys
from datetime import datetime

MOOD_TEMPLATES = [
    "本日のモード → {mood}",
    "現在の気分 → {mood}",
    "ただいま → {mood}",
    "状態 → {mood}",
    "本日の運勢 → {mood}",
    "気分 → {mood}",
    "セッションモード → {mood}",
    "作業フェーズ → {mood}",
    "OSバロメーター → {mood}",
    "謎のモード → {mood}"
]

MOOD_LIST = [
    "絶好調エンジニアモード",
    "バグ吸引フェイズ",
    "アイデア枯渇ゾーン",
    "リファクタリング無双タイム",
    "コーヒー必須デバッグ期",
    "謎の集中ブースト",
    "仕様書迷子タイム",
    "やる気スリープ状態",
    "神エディットモード",
    "無限ループ警戒フェーズ",
    "レビュー地獄ウィーク",
    "コミット祭り開催中",
    "マージコンフリクト警報",
    "変数名迷走期",
    "ドキュメント書き逃げモード",
    "深夜テンション発動中",
    "バグとの対話タイム",
    "自己肯定感アップデート中",
    "謎の達成感フェーズ",
    "仮眠推奨アラート"
]

EXCLUDE_COMMANDS = [
    'clear', 'ls', 'pwd', 'cd', 'exit', 'quit', 'history', 'whoami', 'date', 'time'
]

LOG_FILE = None

def pick_random_mood():
    mood = random.choice(MOOD_LIST)
    template = random.choice(MOOD_TEMPLATES)
    return template.format(mood=mood)

def should_display_barometer(command):
    if not command:
        return True
    cmd = command.strip().split()[0]
    return cmd not in EXCLUDE_COMMANDS

def display_barometer(command=None, log=False):
    if not should_display_barometer(command):
        return
    msg = f"[OS Mood Barometer] : {pick_random_mood()}"
    print(msg)
    if log and LOG_FILE:
        with open(LOG_FILE, 'a') as f:
            f.write(f"{datetime.now().isoformat()}\t{msg}\n")

def list_moods():
    print("--- 利用可能な気分モード ---")
    for mood in MOOD_LIST:
        print(f"- {mood}")

def summary():
    print("random-os-mood-barometer: コマンド実行ごとにランダムな気分モードを表示します。")
    print(f"テンプレート数: {len(MOOD_TEMPLATES)} 種類、気分モード数: {len(MOOD_LIST)} 種類")
    print("除外コマンド:", ', '.join(EXCLUDE_COMMANDS))

def parse_args():
    parser = argparse.ArgumentParser(description='OS Mood Barometer')
    subparsers = parser.add_subparsers(dest='subcmd')

    parser_display = subparsers.add_parser('display', help='バロメーターを表示')
    parser_display.add_argument('--cmd', type=str, help='コマンド名（省略可）')
    parser_display.add_argument('--log', action='store_true', help='表示をログファイルに保存')
    parser_display.add_argument('--logfile', type=str, help='ログファイルパス')

    parser_list = subparsers.add_parser('list', help='気分モード一覧')
    parser_summary = subparsers.add_parser('summary', help='Skill概要')

    return parser.parse_args()


def main():
    global LOG_FILE
    args = parse_args()
    if args.subcmd == 'display':
        if args.logfile:
            LOG_FILE = args.logfile
        display_barometer(command=args.cmd, log=args.log)
    elif args.subcmd == 'list':
        list_moods()
    elif args.subcmd == 'summary':
        summary()
    else:
        # デフォルト: display
        display_barometer()

if __name__ == '__main__':
    main()
