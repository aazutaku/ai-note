import random
import sys
import time
import argparse
import platform
import subprocess
from datetime import datetime, timedelta

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

# 俳句生成用の語彙リスト
FIVE_SYLLABLES = [
    'メモリ消ゆ', '404', 'アクセス拒否', 'ファイル消失', '接続切れ', 'CPU熱し', '更新失敗', 'バグの夜', 'ログ消える', '権限なし',
    '時雨降る', '時刻ずれる', '応答なし', '未知の道', 'セグフォールト', '認証失敗', '空き容量', '静かな夜', '再起動', '春霞'
]
SEVEN_SYLLABLES = [
    '道に迷いて', '春まだ遠き', 'バグの夜', '静かなる夜', 'ログに残らず', 'プロセス落ちる', '再起動せよ', 'エラー溢れて',
    'パスが消えて', '夢の彼方へ', '終わらぬ処理', '時を戻して', '闇に消えゆく', '信号届かず', '誰も知らない',
    '記憶の彼方', '空を仰げば', 'エラーの海へ', '希望は消えて', 'シグナル受信'
]

# 俳句生成
def generate_haiku():
    first = random.choice(FIVE_SYLLABLES)
    second = random.choice(SEVEN_SYLLABLES)
    third = random.choice(FIVE_SYLLABLES)
    # 句が重複しないように
    while third == first:
        third = random.choice(FIVE_SYLLABLES)
    return f"{first}　{second}　{third}"

# 通知表示
def show_notification(haiku, title="Haiku Error Notification"):
    sys_platform = platform.system()
    if PLYER_AVAILABLE:
        notification.notify(title=title, message=haiku, timeout=8)
        return
    if sys_platform == "Darwin":
        # macOS
        script = f'display notification "{haiku}" with title "{title}"'
        subprocess.run(["osascript", "-e", script])
    elif sys_platform == "Linux":
        # Linux (notify-send)
        subprocess.run(["notify-send", title, haiku])
    else:
        # Fallback: print to terminal
        print(f"[{title}]\n{haiku}")

# ログ保存
def log_haiku(haiku, log_file="haiku_error.log"):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] {haiku}\n")

# ログ一覧
def list_haiku_logs(log_file="haiku_error.log", count=10):
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[-count:]:
                print(line.strip())
    except FileNotFoundError:
        print("No haiku error logs found.")

# ログサマリー
def summary_haiku_logs(log_file="haiku_error.log"):
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(f"Total haiku errors: {len(lines)}")
            if lines:
                print(f"First: {lines[0].strip()}")
                print(f"Last: {lines[-1].strip()}")
    except FileNotFoundError:
        print("No haiku error logs found.")

# メインループ
def run_notifier(interval_minutes=60, log_file="haiku_error.log", once=False):
    try:
        while True:
            haiku = generate_haiku()
            show_notification(haiku)
            log_haiku(haiku, log_file)
            if once:
                break
            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        print("\nHaiku notifier stopped.")

# CLIエントリポイント

def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Error Haiku Notifier")
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="定期的に俳句エラー通知を出す")
    parser_run.add_argument("--interval", type=int, default=60, help="通知間隔（分）")
    parser_run.add_argument("--once", action="store_true", help="一度だけ通知して終了")
    parser_run.add_argument("--log-file", type=str, default="haiku_error.log", help="ログファイル名")

    parser_list = subparsers.add_parser("list", help="過去の俳句エラーログを表示")
    parser_list.add_argument("--count", type=int, default=10, help="表示する件数")
    parser_list.add_argument("--log-file", type=str, default="haiku_error.log", help="ログファイル名")

    parser_summary = subparsers.add_parser("summary", help="俳句エラーログのサマリーを表示")
    parser_summary.add_argument("--log-file", type=str, default="haiku_error.log", help="ログファイル名")

    args = parser.parse_args()

    if args.command == "run":
        run_notifier(interval_minutes=args.interval, log_file=args.log_file, once=args.once)
    elif args.command == "list":
        list_haiku_logs(log_file=args.log_file, count=args.count)
    elif args.command == "summary":
        summary_haiku_logs(log_file=args.log_file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
