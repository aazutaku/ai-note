import random
import time
import argparse
import sys
import os
try:
    import notify2
    NOTIFY_AVAILABLE = True
except ImportError:
    NOTIFY_AVAILABLE = False

PET_EVENTS = [
    "仮想猫が画面を横切りました！",
    "デジタル柴犬がファイル『{file}』の上で昼寝中です。",
    "公式ペンギンがマウスカーソルを追いかけています。",
    "バーチャルインコがタスクバーに止まりました。",
    "謎のカメがゆっくりとウィンドウを横断中。",
    "デジタルハムスターが端末の隅でひまわりの種を食べています。",
    "仮想ラビットがウィンドウの隙間から顔を覗かせました。",
    "公式パンダがフォルダを抱えて転がっています。",
    "バーチャル柴犬が通知領域でしっぽを振っています。",
    "謎のペットがどこからともなく現れました。"
]

SAMPLE_FILES = [
    "report.docx", "main.py", "presentation.pptx", "notes.txt", "summary.xlsx"
]

LOG_PATH = os.path.expanduser("~/.os_pet_events.log")


def random_pet_event():
    event = random.choice(PET_EVENTS)
    if "{file}" in event:
        event = event.format(file=random.choice(SAMPLE_FILES))
    return event


def send_notification(message):
    if NOTIFY_AVAILABLE:
        try:
            notify2.init("OS Pet Interruption")
            n = notify2.Notification("OSペット通知", message)
            n.set_timeout(5000)
            n.show()
        except Exception as e:
            print(f"[通知失敗] {e}")
            print(f"[OSペット通知] {message}")
    else:
        print(f"[OSペット通知] {message}")


def log_event(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def trigger_pet_event():
    message = random_pet_event()
    send_notification(message)
    log_event(message)


def list_events(limit=10):
    if not os.path.exists(LOG_PATH):
        print("まだイベント履歴はありません。")
        return
    with open(LOG_PATH, encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines[-limit:]:
        print(line.strip())


def summary_events():
    if not os.path.exists(LOG_PATH):
        print("まだイベント履歴はありません。")
        return
    counts = {}
    with open(LOG_PATH, encoding="utf-8") as f:
        for line in f:
            for ev in PET_EVENTS:
                key = ev.split("{file}")[0].strip()
                if key and key in line:
                    counts[key] = counts.get(key, 0) + 1
    print("== OSペットイベント集計 ==")
    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"{k} ... {v}回")


def random_interval_mode(min_sec=600, max_sec=3600):
    print(f"OSペット乱入イベント自動モード開始 ({min_sec}〜{max_sec}秒間隔)")
    try:
        while True:
            wait = random.randint(min_sec, max_sec)
            time.sleep(wait)
            trigger_pet_event()
    except KeyboardInterrupt:
        print("\n自動モード終了")


def main():
    parser = argparse.ArgumentParser(description="OSペット乱入イベントSkill")
    subparsers = parser.add_subparsers(dest="command")

    parser_trigger = subparsers.add_parser("trigger", help="ランダムにペットイベントを発生させる")
    parser_auto = subparsers.add_parser("auto", help="一定間隔で自動的にペットイベントを発生させる")
    parser_auto.add_argument("--min", type=int, default=600, help="最小間隔(秒)")
    parser_auto.add_argument("--max", type=int, default=3600, help="最大間隔(秒)")
    parser_list = subparsers.add_parser("list", help="過去のイベント履歴を表示")
    parser_list.add_argument("--limit", type=int, default=10, help="表示件数")
    parser_summary = subparsers.add_parser("summary", help="イベント発生回数を集計")

    args = parser.parse_args()

    if args.command == "trigger":
        trigger_pet_event()
    elif args.command == "auto":
        random_interval_mode(args.min, args.max)
    elif args.command == "list":
        list_events(args.limit)
    elif args.command == "summary":
        summary_events()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
