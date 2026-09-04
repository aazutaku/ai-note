import sys
import os
import random
import platform
import argparse
import subprocess
import time
from datetime import datetime, timedelta

FAKE_TOPICS = [
    "USBポートの向きを哲学的に再考する",
    "コーヒー豆の粒度再検討",
    "全プロセスの出欠自動判定について",
    "メモリの空き容量を詩的に表現する方法",
    "今後のOSアップデートで追加予定の謎機能について",
    "システム時刻のズレを宇宙時間で補正する議論",
    "デスクトップ背景の毎時自動変更是非",
    "CPU温度と室温の相関に関する緊急討論",
    "全ユーザーのパスワードを一斉にリセットするか否か",
    "OSの自己紹介文を考えるワークショップ"
]

FAKE_ATTENDEES = [
    "全ユーザー (出欠はOSが自動判定します)",
    "コーヒーを愛する全プロセス",
    "管理者権限を持つ者全員",
    "現在稼働中の全サービス",
    "一時停止中の全アプリケーション",
    "システムカーネルとその友人たち",
    "本日ログインした全ユーザー",
    "仮想マシン内の全プロセス",
    "全てのデバイスドライバ",
    "OSアップデート担当者"
]

FAKE_NOTES = [
    "重要案件につき全員集合",
    "参加しない場合は自動で参加扱いとなります",
    "議事録は自動生成されません",
    "途中参加・途中退出はOSの気分次第",
    "会議の録音は禁止されています (理由: 未定)",
    "出席確認はランダムで行われます",
    "議題は途中で追加される場合があります",
    "本会議は実在しません",
    "参加者には特典はありません",
    "会議後のアンケートはありません"
]

LAST_ALERT_FILE = os.path.expanduser("~/.random_os_fake_conference_call_last")
MIN_INTERVAL_MINUTES = 15


def generate_fake_alert():
    topic = random.choice(FAKE_TOPICS)
    attendee = random.choice(FAKE_ATTENDEES)
    note = random.choice(FAKE_NOTES)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    alert = (
        "[OS公式 緊急カンファレンスコール通知]\n"
        f"本日の議題: {topic}\n"
        f"出席者: {attendee}\n"
        f"開始時刻: 今すぐ\n"
        f"備考: {note}\n"
        f"(通知時刻: {now})"
    )
    return alert


def show_notification(alert_text):
    system = platform.system()
    try:
        if system == "Darwin":
            script = f'display notification "{alert_text}" with title "OS公式 緊急会議"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            subprocess.run(["notify-send", "OS公式 緊急会議", alert_text], check=True)
        elif system == "Windows":
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("OS公式 緊急会議", alert_text, duration=10)
        else:
            print(alert_text)
    except Exception as e:
        print(f"[通知失敗] {e}\n{alert_text}")


def can_trigger_alert():
    if not os.path.exists(LAST_ALERT_FILE):
        return True
    try:
        with open(LAST_ALERT_FILE, "r") as f:
            last = f.read().strip()
            last_dt = datetime.strptime(last, "%Y-%m-%d %H:%M:%S")
            if datetime.now() - last_dt > timedelta(minutes=MIN_INTERVAL_MINUTES):
                return True
            else:
                return False
    except Exception:
        return True


def update_last_alert_time():
    try:
        with open(LAST_ALERT_FILE, "w") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    except Exception:
        pass


def trigger_alert():
    if not can_trigger_alert():
        print("[INFO] 直近で通知済みのため、今回はスキップします。")
        return
    alert = generate_fake_alert()
    show_notification(alert)
    update_last_alert_time()
    print(alert)


def list_last_alert():
    if not os.path.exists(LAST_ALERT_FILE):
        print("まだ通知履歴がありません。")
        return
    with open(LAST_ALERT_FILE, "r") as f:
        last = f.read().strip()
        print(f"最後の通知時刻: {last}")


def main():
    parser = argparse.ArgumentParser(description="OS公式フェイク会議通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="今すぐフェイク会議通知を出す")
    parser_list = subparsers.add_parser("list", help="最後の通知時刻を表示")
    parser_demo = subparsers.add_parser("demo", help="5回デモ通知を連続表示 (間隔3秒)")

    args = parser.parse_args()
    if args.command == "alert" or args.command is None:
        trigger_alert()
    elif args.command == "list":
        list_last_alert()
    elif args.command == "demo":
        for _ in range(5):
            alert = generate_fake_alert()
            show_notification(alert)
            print(alert)
            time.sleep(3)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
