import sys
import os
import argparse
import random
import datetime
import subprocess

def get_today_seed():
    today = datetime.date.today()
    return int(today.strftime('%Y%m%d'))

DJ_INTRO = [
    "おはようございます！",
    "システム管理部より朝のお知らせです。",
    "OSモーニングラジオ、今朝も始まりました。",
    "DJカーネルがお送りします。",
    "今日も元気にバグを直しましょう！",
]

OS_WEATHER = [
    "本日のOS天気予報：カーネルの空は快晴、バグの雲がちらほら。",
    "本日のメモリ温度は適温、CPUの風は追い風です。",
    "ストレージの湿度が高めです。バックアップはお早めに。",
    "プロセスの海は穏やか、ネットワークの波も静かです。",
    "本日はシステムアップデート日和となるでしょう。",
]

OS_GOSSIP = [
    "業界ゴシップ：昨日、メモリ管理部が寝坊した模様です。",
    "噂：カーネルパニックの原因は未だに不明です。",
    "新型バグが発見され、セキュリティ部が緊急対応中。",
    "ファイルシステム部が新しいフォーマットを検討中とのこと。",
    "プロセス管理部の会議が無限ループに突入しました。",
]

ENCOURAGEMENT = [
    "今日も一日、エラーに負けず頑張りましょう！",
    "バグ修正は愛、デバッグは力です。",
    "ログに愛を込めて、今日も開発を。",
    "本日のラッキーコマンド：sudo reboot（実行は自己責任で）",
    "システムログに愛を込めて。",
]

SIGN_OFF = [
    "それでは、素敵な開発ライフを！",
    "本日の放送は以上です。また明日！",
    "DJカーネルでした。Have a nice debug!",
    "バグに負けるな、開発者！",
    "次回の放送もお楽しみに。",
]

MESSAGE_BLOCKS = [DJ_INTRO, OS_WEATHER, OS_GOSSIP, ENCOURAGEMENT, SIGN_OFF]


def generate_radio_messages(seed=None):
    if seed is None:
        seed = get_today_seed()
    random.seed(seed)
    messages = []
    for block in MESSAGE_BLOCKS:
        msg = random.choice(block)
        messages.append(f"[OS Morning Radio] {msg}")
    return messages


def notify_desktop(message):
    # Linux (notify-send)
    if sys.platform.startswith('linux'):
        try:
            subprocess.run(['notify-send', 'OS Morning Radio', message], check=True)
        except Exception:
            pass
    # macOS (osascript)
    elif sys.platform == 'darwin':
        osa_script = f'display notification "{message}" with title "OS Morning Radio"'
        try:
            subprocess.run(['osascript', '-e', osa_script], check=True)
        except Exception:
            pass
    # Windows: 通知は未サポート


def output_terminal(messages):
    for msg in messages:
        print(msg)


def main():
    parser = argparse.ArgumentParser(description='謎のOSモーニングラジオ風メッセージを出力します。')
    parser.add_argument('--notify', action='store_true', help='デスクトップ通知も行う')
    parser.add_argument('--terminal', action='store_true', help='ターミナル出力のみ')
    parser.add_argument('--seed', type=int, default=None, help='日替わりメッセージの乱数シード')
    parser.add_argument('command', nargs='?', default='play', choices=['play', 'log', 'list', 'summary'], help='サブコマンド')
    args = parser.parse_args()

    if args.command == 'play':
        messages = generate_radio_messages(args.seed)
        if not args.terminal:
            # デスクトップ通知（1行目のみ）
            notify_desktop(messages[0])
        output_terminal(messages)
    elif args.command == 'list':
        print("--- OS Morning Radio メッセージ候補 ---")
        for i, block in enumerate(MESSAGE_BLOCKS):
            print(f"Block {i+1}:")
            for msg in block:
                print(f"  - {msg}")
    elif args.command == 'summary':
        print("OS Morning Radio: 日替わりで無駄なラジオ風メッセージを出力します。")
        print("通知API: notify-send (Linux), osascript (macOS)")
        print("コマンド例: python os_fake_morning_radio.py --notify")
    elif args.command == 'log':
        print("このSkillは履歴を保存しません。")
    else:
        print("未知のコマンドです。--help を参照してください。")

if __name__ == '__main__':
    main()
