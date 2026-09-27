import argparse
import random
import sys
import time
import os
from datetime import datetime, timedelta

# 評価メッセージのテンプレート
EVALUATION_MESSAGES = [
    '[OS公式AI評価通知] 本日のあなたの集中度: AI判定「たぶん寝てる」',
    '[AI自動評価] コーヒー摂取量が基準値超過（推定: {cups}杯）',
    '[OS AI監査] 作業効率: AI評価「なぜかExcelが開きっぱなし」',
    '[AI判定] タイピング速度: 標準値未満（推定: {wpm}wpm）',
    '[AI通知] 休憩推奨: 直近{minutes}分間、姿勢が固定されています',
    '[AI評価] 本日の進捗: AI判定「進捗どうですか？」',
    '[AI監査] マウス移動距離: AI評価「謎の円運動を検出」',
    '[OS AI評価] タスク切り替え頻度: AI判定「多動傾向」',
    '[AI通知] 作業BGM: AI評価「選曲が渋い」',
    '[AI警告] Slack未読メッセージ: AI推定「15件」',
    '[AI評価] 画面注視率: AI判定「別窓で動画視聴中？」',
    '[AI通知] ショートカット利用率: AI評価「Ctrl+C依存症」',
    '[AI自動評価] コーディングスタイル: AI判定「PEP8違反疑惑」',
    '[AI評価] 休憩回数: AI判定「少なすぎ」',
    '[AI監査] ターミナル履歴: AI評価「ls多用」',
    '[AI通知] 作業開始時刻: AI判定「やや遅め」',
    '[AI評価] メール返信速度: AI判定「未読スルー」',
    '[AI警告] デスクトップファイル数: AI評価「カオス」',
    '[AI評価] 進捗報告: AI判定「進捗どうですか？」',
    '[AI通知] キーボード入力: AI評価「連打傾向」',
]

# 動的パラメータ生成

def generate_random_message():
    msg = random.choice(EVALUATION_MESSAGES)
    # 変数をランダムで埋める
    if '{cups}' in msg:
        cups = random.randint(3, 8)
        msg = msg.format(cups=cups)
    elif '{wpm}' in msg:
        wpm = random.randint(20, 60)
        msg = msg.format(wpm=wpm)
    elif '{minutes}' in msg:
        minutes = random.randint(30, 120)
        msg = msg.format(minutes=minutes)
    else:
        msg = msg
    return msg

# 通知表示 (ターミナル/デスクトップ)
def show_notification(message):
    # macOS
    if sys.platform == 'darwin':
        try:
            from subprocess import call
            call(['osascript', '-e', f'display notification "{message}" with title "AI評価通知"'])
        except Exception:
            print(message)
    # Linux (notify-send)
    elif sys.platform.startswith('linux'):
        try:
            from subprocess import call
            call(['notify-send', 'AI評価通知', message])
        except Exception:
            print(message)
    # Windows (toast通知)
    elif sys.platform.startswith('win'):
        try:
            import win10toast
            toaster = win10toast.ToastNotifier()
            toaster.show_toast('AI評価通知', message, duration=5)
        except Exception:
            print(message)
    else:
        print(message)

# ログ保存（実害ゼロのため一時ファイルのみ）
def log_message(message):
    try:
        tmp_path = os.path.join(os.path.expanduser('~'), '.random_os_fake_ai_eval_log')
        with open(tmp_path, 'a', encoding='utf-8') as f:
            f.write(f'{datetime.now().isoformat()}\t{message}\n')
    except Exception:
        pass

def list_logs():
    tmp_path = os.path.join(os.path.expanduser('~'), '.random_os_fake_ai_eval_log')
    if not os.path.exists(tmp_path):
        print('ログはありません。')
        return
    with open(tmp_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())

def summary_logs():
    tmp_path = os.path.join(os.path.expanduser('~'), '.random_os_fake_ai_eval_log')
    if not os.path.exists(tmp_path):
        print('ログはありません。')
        return
    count = 0
    with open(tmp_path, 'r', encoding='utf-8') as f:
        for _ in f:
            count += 1
    print(f'通知履歴: {count}件')

def main():
    parser = argparse.ArgumentParser(description='Random OS Fake AI Evaluation Alert')
    subparsers = parser.add_subparsers(dest='command')

    # サブコマンド
    parser_log = subparsers.add_parser('log', help='最新のAI評価通知を表示')
    parser_list = subparsers.add_parser('list', help='AI評価通知の履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知履歴の件数を表示')
    parser_daemon = subparsers.add_parser('daemon', help='バックグラウンドで定期的にAI評価通知を表示')
    parser_daemon.add_argument('--interval', type=int, default=1800, help='通知間隔(秒, デフォルト1800=30分)')

    args = parser.parse_args()

    if args.command == 'log':
        msg = generate_random_message()
        show_notification(msg)
        log_message(msg)
    elif args.command == 'list':
        list_logs()
    elif args.command == 'summary':
        summary_logs()
    elif args.command == 'daemon':
        print(f'バックグラウンド通知を{args.interval}秒ごとに実行します。Ctrl+Cで停止。')
        try:
            while True:
                msg = generate_random_message()
                show_notification(msg)
                log_message(msg)
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print('\n停止しました。')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
