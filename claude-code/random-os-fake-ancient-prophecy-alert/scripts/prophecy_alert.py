import sys
import argparse
import random
import time
import os

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

PROPHECY_TEMPLATES = [
    "西の{os}に{color}き{bug}現る時、選ばれし者は{action}せよ",
    "{year}年、{noun}にパワー宿る。{verb}者、道を得ん",
    "{cmd}の呪文、三度唱えし者に{color}き{screen}の試練訪れる",
    "{file}の奥深く、{beast}眠りし時、{user}は目覚める",
    "{os}の{mountain}越えし後、{user}に{gift}授けられる",
    "{noun}を{verb}すれば、{os}の門開かれる",
    "{year}の{event}、{user}は{action}を忘れるな",
    "{cmd}の失敗、{os}の怒りを呼ぶ",
    "{noun}に{color}き光差す時、{user}は{gift}を手にする",
    "{file}に隠された{beast}、{user}のみが見つけ出す"
]

TEMPLATE_VARS = {
    "os": ["ウィンドウズ", "リナックス", "マック"],
    "color": ["赤", "青", "黒", "白", "金"],
    "bug": ["バグ", "影", "警告", "謎のエラー"],
    "action": ["リブート", "再起動", "ビルド", "祈り"],
    "year": ["2024年", "1999年", "2038年", "2000年"],
    "noun": ["ファイル名", "拡張子", "パーミッション", "プロセス", "パスワード"],
    "verb": ["変える", "守る", "削除する", "選ぶ"],
    "cmd": ["sudo", "make", "git", "ls", "docker"],
    "screen": ["画面", "闇", "砂嵐"],
    "file": ["/etc/passwd", "/dev/null", "README.md", "main.py"],
    "beast": ["ドラゴン", "バグベア", "ゴーレム", "ワーム"],
    "user": [os.getenv("USER", "選ばれし者")],
    "mountain": ["壁", "山脈", "迷宮", "森"],
    "gift": ["知恵", "勇気", "バグ修正", "新たな権限"],
    "event": ["大停電", "アップデート", "バグ祭り", "リリース"],
}

TRIGGER_KEYWORDS = [
    "build", "run", "test", "deploy", "commit", "push", "install", "update", "error", "warning", "success"
]

NOTIFY_TITLE = "古代OS予言通知"


def generate_prophecy():
    template = random.choice(PROPHECY_TEMPLATES)
    filled = template
    for key, values in TEMPLATE_VARS.items():
        filled = filled.replace('{' + key + '}', random.choice(values))
    return filled


def show_notification(prophecy):
    if PLYER_AVAILABLE:
        try:
            notification.notify(
                title=NOTIFY_TITLE,
                message=prophecy,
                app_name="ProphecyAlert",
                timeout=5
            )
        except Exception as e:
            print(f"[通知失敗] {e}")
            print(f"=== {NOTIFY_TITLE} ===\n『{prophecy}』\n")
    else:
        print(f"=== {NOTIFY_TITLE} ===\n『{prophecy}』\n")


def trigger_by_keywords(log_line):
    for kw in TRIGGER_KEYWORDS:
        if kw in log_line.lower():
            return True
    return False


def monitor_stdin():
    try:
        for line in sys.stdin:
            if trigger_by_keywords(line):
                prophecy = generate_prophecy()
                show_notification(prophecy)
    except KeyboardInterrupt:
        pass


def random_interval_alert(min_sec=180, max_sec=600):
    try:
        while True:
            wait = random.randint(min_sec, max_sec)
            time.sleep(wait)
            prophecy = generate_prophecy()
            show_notification(prophecy)
    except KeyboardInterrupt:
        pass


def main():
    parser = argparse.ArgumentParser(description="謎のOS古代予言通知をランダムに表示")
    subparsers = parser.add_subparsers(dest="command")

    parser_once = subparsers.add_parser("once", help="1回だけ予言通知")
    parser_monitor = subparsers.add_parser("monitor", help="標準入力を監視し、キーワード検知で通知")
    parser_random = subparsers.add_parser("random", help="一定時間ごとにランダム通知")
    parser_random.add_argument("--min", type=int, default=180, help="最小間隔(秒)")
    parser_random.add_argument("--max", type=int, default=600, help="最大間隔(秒)")

    args = parser.parse_args()

    if args.command == "once":
        prophecy = generate_prophecy()
        show_notification(prophecy)
    elif args.command == "monitor":
        print("標準入力を監視します。Ctrl+Cで終了。\n")
        monitor_stdin()
    elif args.command == "random":
        print(f"{args.min}秒〜{args.max}秒の間隔で予言通知を発動します。Ctrl+Cで終了。\n")
        random_interval_alert(args.min, args.max)
    else:
        parser.print_help()
        print("\n例: python prophecy_alert.py once")

if __name__ == '__main__':
    main()
