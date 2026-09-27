import sys
import os
import random
import time
import argparse
import platform
import subprocess
from datetime import datetime, timedelta

# ランダムAI評価メッセージリスト
AI_MESSAGES = [
    "本日のあなたの集中度: AI判定『たぶん寝てる』",
    "自動分析: コーヒー摂取量が基準値超過",
    "タイピング速度: AI基準『なぜか逆走中』",
    "作業効率: AI判定『謎の停滞モード』",
    "画面注視率: AI推測『たぶんYouTube』",
    "AIによる自動評価: 今日のやる気指数『未検出』",
    "AI判定: Slack未読件数が臨界点突破",
    "AI警告: ファイル保存回数が少なすぎます",
    "自動評価: 進捗バーが水平線を突破",
    "AI推測: たぶん今は休憩中",
    "AI判定: キーボード操作がランダムウォーク",
    "AI評価: コーディング速度が量子トンネル効果",
    "AI警告: 画面切替頻度が異常値",
    "AI判定: タスク切り替え回数が規格外",
    "AI評価: エラー回数がAI基準値を超過",
    "AI推測: たぶん猫がキーボードを操作中",
    "AI判定: 進捗状況『観測不能』",
    "AI警告: 目の瞬き回数がAI基準値未満",
    "AI評価: 今日のやる気指数『検出不能』",
    "AI判定: コードの美しさがカオス状態"
]

NOTIFY_TITLE = "AI評価通知"

# OSごとの通知実装
def send_notification(message):
    sys_platform = platform.system()
    try:
        if sys_platform == "Linux":
            subprocess.run(["notify-send", NOTIFY_TITLE, message], check=False)
        elif sys_platform == "Darwin":
            script = f'display notification "{message}" with title "{NOTIFY_TITLE}"'
            subprocess.run(["osascript", "-e", script], check=False)
        elif sys_platform == "Windows":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(NOTIFY_TITLE, message, duration=5, threaded=True)
            except ImportError:
                print(f"[{NOTIFY_TITLE}] {message}")
        else:
            print(f"[{NOTIFY_TITLE}] {message}")
    except Exception as e:
        print(f"[{NOTIFY_TITLE}] {message} (通知失敗: {e})")

# ターミナル出力
def print_terminal(message):
    print(f"[{NOTIFY_TITLE}] {message}")

# 評価メッセージをランダム選択
def random_ai_message():
    return random.choice(AI_MESSAGES)

# ログファイル保存（オプション、デフォルトは保存しない）
def log_message(message, logfile=None):
    if logfile:
        with open(logfile, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now().isoformat()} {message}\n")

# サブコマンド: 即時通知
def cmd_alert(args):
    msg = random_ai_message()
    if args.terminal:
        print_terminal(msg)
    else:
        send_notification(msg)
    log_message(msg, args.logfile)

# サブコマンド: 連続通知（頻度調整付き）
def cmd_stream(args):
    interval = max(60, args.interval)  # 最低60秒間隔
    count = args.count
    for i in range(count):
        msg = random_ai_message()
        if args.terminal:
            print_terminal(msg)
        else:
            send_notification(msg)
        log_message(msg, args.logfile)
        if i < count - 1:
            time.sleep(interval)

# サブコマンド: メッセージ一覧表示
def cmd_list(args):
    for m in AI_MESSAGES:
        print(f"- {m}")

# サブコマンド: ログ表示
def cmd_log(args):
    if not args.logfile or not os.path.exists(args.logfile):
        print("ログファイルが存在しません")
        return
    with open(args.logfile, encoding='utf-8') as f:
        for line in f:
            print(line.strip())

# 引数パース
def parse_args():
    parser = argparse.ArgumentParser(description='random-os-fake-ai-evaluation-alert: 理不尽AI評価通知スキル')
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_alert = subparsers.add_parser('alert', help='AI評価通知を即時発動')
    parser_alert.add_argument('--terminal', action='store_true', help='ターミナルに出力のみ')
    parser_alert.add_argument('--logfile', type=str, help='通知履歴をファイル保存')
    parser_alert.set_defaults(func=cmd_alert)

    parser_stream = subparsers.add_parser('stream', help='AI評価通知を一定間隔で繰り返す')
    parser_stream.add_argument('--interval', type=int, default=3600, help='通知間隔(秒, 最小60)')
    parser_stream.add_argument('--count', type=int, default=3, help='通知回数')
    parser_stream.add_argument('--terminal', action='store_true', help='ターミナルに出力のみ')
    parser_stream.add_argument('--logfile', type=str, help='通知履歴をファイル保存')
    parser_stream.set_defaults(func=cmd_stream)

    parser_list = subparsers.add_parser('list', help='AI評価メッセージ一覧表示')
    parser_list.set_defaults(func=cmd_list)

    parser_log = subparsers.add_parser('log', help='通知ログ表示')
    parser_log.add_argument('--logfile', type=str, required=True, help='ログファイルパス')
    parser_log.set_defaults(func=cmd_log)

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    args.func(args)
