import random
import argparse
import sys
import time
import os

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

# ランダム通知メッセージ構成要素
ALERT_HEADERS = [
    '緊急: このPCは{min}分後に謎のメンテナンスに突入します',
    '臨時ダウンタイム予告: {min}分後に全プロセスが一時停止予定',
    '警告: システムが{min}分後に自己診断モードへ移行',
    '注意: 予期せぬOSアップデートが{min}分後に開始されます',
    '重大: {min}分後に全ウィンドウが自動的に閉じられる可能性',
    '速報: OSが{min}分後にやる気を失う兆候',
]

REASONS = [
    'OSのやる気が著しく低下',
    'ファイルシステムの気分転換',
    'カーネルが昼寝を希望',
    'プロセス間通信の意思疎通エラー',
    'メモリが現実逃避中',
    'バッファキャッシュの反乱',
    'ドライバがストライキ中',
    'ユーザーの集中力低下を検知',
    'キーボードの自己主張',
    'マウスが散歩に出かけた',
]

ACTIONS = [
    'キーボードを褒め称えて延命可能',
    '画面に向かって「ありがとう」と叫ぶと回避率上昇',
    'ターミナルに "stay" と入力すると一時的に延期',
    'マウスを3回連続クリックでリセット可能',
    '深呼吸してからEnterキーを押すと効果あり',
    '机を優しく叩くとシステムが再考',
    '何もせず見守るのも一つの手',
    'コーヒーを淹れて戻ると状況が改善するかも',
    'OSに感謝の意を伝えると回避成功率アップ',
    'タスクマネージャを開いて睨むと警告が消えることがある',
]

TERMINAL_DIVIDER = '---'

LOG_FILE = os.path.expanduser('~/.fake_downtime_alert.log')

def generate_alert():
    min_left = random.randint(5, 30)
    header = random.choice(ALERT_HEADERS).format(min=min_left)
    reason = random.choice(REASONS)
    action = random.choice(ACTIONS)
    return header, reason, action

def show_terminal_alert(header, reason, action):
    print(f"[ALERT] {header}")
    print(f"理由: {reason}")
    print(f"対策: {action}")
    print(TERMINAL_DIVIDER)

def show_desktop_notification(header, reason, action):
    if not PLYER_AVAILABLE:
        return False
    try:
        notification.notify(
            title=header,
            message=f"理由: {reason}\n対策: {action}",
            app_name="Fake OS Downtime Alert",
            timeout=10
        )
        return True
    except Exception:
        return False

def log_alert(header, reason, action):
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            ts = time.strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"[{ts}] {header} | 理由: {reason} | 対策: {action}\n")
    except Exception:
        pass

def list_logs():
    if not os.path.exists(LOG_FILE):
        print("No alert logs found.")
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        logs = f.readlines()
    print(''.join(logs[-10:]))

def summary_logs():
    if not os.path.exists(LOG_FILE):
        print("No alert logs found.")
        return
    count = 0
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        for _ in f:
            count += 1
    print(f"Total fake alerts triggered: {count}")

def trigger_alert():
    header, reason, action = generate_alert()
    show_terminal_alert(header, reason, action)
    show_desktop_notification(header, reason, action)
    log_alert(header, reason, action)

def main():
    parser = argparse.ArgumentParser(description='Fake OS Random Sudden Downtime Alert')
    subparsers = parser.add_subparsers(dest='command')

    trigger_parser = subparsers.add_parser('trigger', help='Trigger a random fake downtime alert')
    list_parser = subparsers.add_parser('list', help='Show last 10 fake alerts')
    summary_parser = subparsers.add_parser('summary', help='Show total alert count')

    args = parser.parse_args()

    if args.command == 'trigger' or args.command is None:
        trigger_alert()
    elif args.command == 'list':
        list_logs()
    elif args.command == 'summary':
        summary_logs()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
