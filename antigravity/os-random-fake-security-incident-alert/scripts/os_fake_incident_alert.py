import sys
import random
import argparse
import time
import platform
import os

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

FAKE_INCIDENTS = [
    "本日よりマウスが逆方向に動きます。",
    "あなたの椅子が物理的に乗っ取られました。",
    "システムにピーマン型ウイルスが検出されました。",
    "画面の色がランダムで変化し始めました。",
    "全てのファイル名が『ねこ』に変更されました。",
    "キーボードの配列が五十音順に再設定されました。",
    "OSが未知のエネルギー体に感染しました。",
    "本日よりエンターキーが無効化されます。",
    "あなたのアカウントが冷蔵庫に移動されました。",
    "全アプリが自動的にカラオケモードで起動します。",
    "プリンタが『おにぎりモード』で稼働中です。",
    "CPUが物理的に逆回転を始めました。",
    "全ウィンドウが1秒ごとに左右反転します。",
    "OSが『ピーマン語』に切り替わりました。",
    "椅子の高さがランダムに変動します。",
    "全てのパスワードが『たこやき』に変更されました。",
    "ディスプレイが上下逆さまに表示されます。"
]

LOG_FILE = os.path.expanduser("~/.os_fake_incident_alert.log")


def random_incident():
    return random.choice(FAKE_INCIDENTS)


def show_terminal_alert(msg):
    print(f"[ALERT] OSセキュリティインシデント発生: {msg}")


def show_desktop_notification(msg):
    if not PLYER_AVAILABLE:
        show_terminal_alert(msg)
        return
    notification.notify(
        title="OSセキュリティインシデント発生",
        message=msg,
        app_name="FakeIncidentAlert",
        timeout=8
    )


def log_incident(msg):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")
    except Exception as e:
        show_terminal_alert(f"[LOGGING ERROR] {e}")


def list_logs():
    if not os.path.exists(LOG_FILE):
        print("No incident logs found.")
        return
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())


def summary_logs():
    if not os.path.exists(LOG_FILE):
        print("No incident logs found.")
        return
    counts = {}
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            for inc in FAKE_INCIDENTS:
                if inc in line:
                    counts[inc] = counts.get(inc, 0) + 1
    print("--- Incident Summary ---")
    for inc, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{inc}: {cnt}回")


def parse_args():
    parser = argparse.ArgumentParser(description="OSランダムフェイクセキュリティインシデントアラート")
    subparsers = parser.add_subparsers(dest="command", required=False)

    parser_log = subparsers.add_parser("log", help="新しいフェイクインシデントを発生させる")
    parser_log.add_argument("--desktop", action="store_true", help="デスクトップ通知も表示する")

    parser_list = subparsers.add_parser("list", help="過去のインシデントログを表示")
    parser_summary = subparsers.add_parser("summary", help="インシデントの発生回数を集計")

    parser.add_argument("--interval", type=int, default=0, help="n秒ごとに自動通知 (0なら1回のみ)")
    parser.add_argument("--desktop", action="store_true", help="デスクトップ通知も表示する")

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "list":
        list_logs()
        return
    if args.command == "summary":
        summary_logs()
        return
    def fire_alert():
        msg = random_incident()
        show_terminal_alert(msg)
        if args.desktop or (hasattr(args, 'desktop') and args.desktop):
            show_desktop_notification(msg)
        log_incident(msg)
    if args.command == "log":
        fire_alert()
        return
    if args.interval > 0:
        try:
            while True:
                fire_alert()
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\n[INFO] 停止されました。")
    else:
        fire_alert()

if __name__ == "__main__":
    main()
