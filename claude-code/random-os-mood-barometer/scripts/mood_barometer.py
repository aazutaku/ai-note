import sys
import argparse
import random
import datetime
import shutil
import os

MOODS = [
    "絶好調エンジニアモード",
    "バグ吸引フェイズ",
    "アイデア枯渇ゾーン",
    "仕様書迷子モード",
    "無敵デバッグタイム",
    "タイポ連発期",
    "集中力蒸発タイム",
    "コード美化フェーズ",
    "無限リファクタ地獄",
    "コミット恐怖症モード",
    "タスク消化祭り",
    "レビュー待ち無限ループ",
    "新機能妄想タイム",
    "眠気マックスゾーン",
    "仕様追加パニック"
]

PRODUCTIVITY = [
    "爆上げ中 (推定)",
    "低下中 (推定)",
    "安定運転 (仮)",
    "乱高下 (予想)",
    "未計測",
    "計測不能"
]

TIPS = [
    "休憩すると運気が上がるかも？",
    "コーヒー補給推奨",
    "一度深呼吸してみよう",
    "机周りを片付けてみよう",
    "今こそストレッチ！",
    "やる気は後からついてくる",
    "一旦手を止めてみよう",
    "BGMを変えてみよう",
    "進捗は気にしないでOK",
    "気分転換に散歩もアリ"
]

BORDER = "─"
TITLE = " OS Mood Barometer "


def get_terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 60


def random_barometer():
    mood = random.choice(MOODS)
    prod = random.choice(PRODUCTIVITY)
    mode = random.choice(MOODS)
    tip = random.choice(TIPS)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    width = get_terminal_width()
    box_width = min(max(40, len(TITLE) + 10), width - 2)
    def pad(s):
        return s + " " * (box_width - len(s.encode('utf-8')))
    border = "┌" + BORDER * (box_width - 2) + "┐"
    footer = "└" + BORDER * (box_width - 2) + "┘"
    title_line = "│" + TITLE.center(box_width - 2) + "│"
    lines = [
        border,
        title_line,
        f"│ 本日の気分: {mood}{' ' * (box_width - len('│ 本日の気分: ') - len(mood.encode('utf-8')) - 1)}│",
        f"│ 生産性: {prod}{' ' * (box_width - len('│ 生産性: ') - len(prod.encode('utf-8')) - 1)}│",
        f"│ モード: {mode}{' ' * (box_width - len('│ モード: ') - len(mode.encode('utf-8')) - 1)}│",
        f"│ Tips: {tip}{' ' * (box_width - len('│ Tips: ') - len(tip.encode('utf-8')) - 1)}│",
        footer
    ]
    return "\n".join(lines)


def log_barometer(logfile):
    mood = random.choice(MOODS)
    prod = random.choice(PRODUCTIVITY)
    mode = random.choice(MOODS)
    tip = random.choice(TIPS)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "datetime": now,
        "mood": mood,
        "productivity": prod,
        "mode": mode,
        "tip": tip
    }
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(f"{entry}\n")
    return entry


def list_logs(logfile, limit=10):
    if not os.path.exists(logfile):
        print("ログファイルがありません。")
        return
    with open(logfile, encoding="utf-8") as f:
        lines = f.readlines()[-limit:]
    for line in lines:
        print(line.strip())


def summary_logs(logfile):
    if not os.path.exists(logfile):
        print("ログファイルがありません。")
        return
    moods = {}
    with open(logfile, encoding="utf-8") as f:
        for line in f:
            for m in MOODS:
                if m in line:
                    moods[m] = moods.get(m, 0) + 1
    print("過去の気分モード出現回数:")
    for m, c in sorted(moods.items(), key=lambda x: -x[1]):
        print(f"{m}: {c}回")


def main():
    parser = argparse.ArgumentParser(description="謎のOS風気分バロメーター")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser("log", help="バロメーターを表示してログに記録")
    parser_log.add_argument("--logfile", default="~/.mood_barometer.log", help="ログファイルパス")

    parser_list = subparsers.add_parser("list", help="バロメーターログを表示")
    parser_list.add_argument("--logfile", default="~/.mood_barometer.log", help="ログファイルパス")
    parser_list.add_argument("--limit", type=int, default=10, help="表示件数")

    parser_summary = subparsers.add_parser("summary", help="バロメーターの出現傾向を集計")
    parser_summary.add_argument("--logfile", default="~/.mood_barometer.log", help="ログファイルパス")

    parser_show = subparsers.add_parser("show", help="バロメーターを1回だけ表示")

    args = parser.parse_args()

    if args.command == "log":
        logfile = os.path.expanduser(args.logfile)
        entry = log_barometer(logfile)
        print(random_barometer())
    elif args.command == "list":
        logfile = os.path.expanduser(args.logfile)
        list_logs(logfile, args.limit)
    elif args.command == "summary":
        logfile = os.path.expanduser(args.logfile)
        summary_logs(logfile)
    elif args.command == "show" or args.command is None:
        print(random_barometer())
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
