import sys
import argparse
import random
import platform
import subprocess
import time

FAKE_FAILURE_MESSAGES = [
    "失敗: トマトが爆発しました。机の上が真っ赤です。",
    "警告: 集中力が鍋底にこびりつきました。再加熱してください。",
    "注意: タイマーがピザに変身したため無効です。",
    "エラー: ポモドーロがカプレーゼサラダになりました。",
    "失敗: タイマーがトマトソースに溶けました。",
    "警告: ポモドーロの種が芽を出しました。作業環境がジャングル化。",
    "注意: タイマーがスパゲッティに絡まりました。",
    "失敗: 集中力がオーブンで焦げ付きました。",
    "警告: タイマーがピザカッターに変身しました。",
    "注意: トマトの妖精がタイマーを持ち去りました。",
    "失敗: タイマーがトマト缶に閉じ込められました。",
    "警告: 集中力がパスタの茹で汁に流れました。",
    "注意: タイマーがイタリアンソースに溶解しました。",
    "失敗: ポモドーロがピザトーストになりました。",
    "警告: タイマーがトマト畑に埋まりました。",
    "注意: 集中力がトマトジュースになりました。コップをご用意ください。"
]

NOTIFY_COMMANDS = {
    'Darwin': ['osascript', '-e', 'display notification "{msg}" with title "FakeOS Notification"'],
    'Linux': ['notify-send', 'FakeOS Notification', '{msg}'],
    'Windows': None  # Windowsは標準通知APIがないためターミナル出力のみ
}

TRIGGER_KEYWORDS = [
    'pomodoro', 'ポモドーロ', 'timer', 'タイマー', '集中', 'start', 'begin', 'end', 'finish', 'スタート', '終了'
]

def select_random_message():
    return random.choice(FAKE_FAILURE_MESSAGES)

def send_notification(msg):
    system = platform.system()
    notify_cmd = NOTIFY_COMMANDS.get(system)
    if notify_cmd:
        try:
            cmd = [part.format(msg=msg) for part in notify_cmd]
            subprocess.run(cmd, check=False)
        except Exception:
            print(f"[FakeOS Notification]\n{msg}")
    else:
        print(f"[FakeOS Notification]\n{msg}")

def simulate_pomodoro_event(event_type):
    # event_type: 'start' or 'end'
    msg = select_random_message()
    send_notification(msg)
    return msg

def parse_args():
    parser = argparse.ArgumentParser(description='Random OS Fake Pomodoro Failure Notifier')
    subparsers = parser.add_subparsers(dest='command')

    start_parser = subparsers.add_parser('start', help='ポモドーロタイマー開始時のフェイク通知を発生')
    end_parser = subparsers.add_parser('end', help='ポモドーロタイマー終了時のフェイク通知を発生')
    list_parser = subparsers.add_parser('list', help='すべてのフェイク通知メッセージを表示')
    test_parser = subparsers.add_parser('test', help='全OSの通知動作をテスト')
    return parser.parse_args()

def list_messages():
    print("[FakeOS Notification メッセージ一覧]")
    for m in FAKE_FAILURE_MESSAGES:
        print(f"- {m}")

def test_notifications():
    print("[FakeOS Notification テスト開始]")
    for i in range(5):
        msg = select_random_message()
        print(f"テスト通知 {i+1}:")
        send_notification(msg)
        time.sleep(1)
    print("[テスト終了]")

def semantic_trigger(text):
    for kw in TRIGGER_KEYWORDS:
        if kw.lower() in text.lower():
            return True
    return False

def main():
    args = parse_args()
    if args.command == 'start':
        simulate_pomodoro_event('start')
    elif args.command == 'end':
        simulate_pomodoro_event('end')
    elif args.command == 'list':
        list_messages()
    elif args.command == 'test':
        test_notifications()
    else:
        # 標準入力からのトリガー判定（例: semantic trigger）
        print("標準入力からトリガーキーワードを検出します。'exit'で終了。")
        try:
            while True:
                line = input('> ')
                if line.strip().lower() == 'exit':
                    break
                if semantic_trigger(line):
                    msg = simulate_pomodoro_event('semantic')
        except KeyboardInterrupt:
            print("\n終了します。")

if __name__ == '__main__':
    main()
