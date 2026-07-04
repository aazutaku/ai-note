import sys
import argparse
import random
import datetime
import os
import json

MOOD_LABELS = [
    ("絶好調", (36.5, 39.9)),
    ("冷え冷え", (14.0, 22.0)),
    ("炎上中", (40.0, 45.0)),
    ("まあまあ", (25.0, 35.0)),
    ("眠気MAX", (18.0, 23.5)),
    ("集中モード", (33.0, 38.0)),
    ("やる気微妙", (21.0, 27.0)),
    ("テンション爆上げ", (37.5, 42.0)),
    ("放心状態", (15.0, 20.0)),
    ("平常運転", (27.0, 36.0)),
]

LOG_FILE = os.path.expanduser("~/.os_mood_temperature_bar_log.jsonl")


def generate_mood_temperature():
    label, (low, high) = random.choice(MOOD_LABELS)
    temp = round(random.uniform(low, high), 1)
    return label, temp


def print_mood_temperature(label, temp, show_time=False):
    bar = f"[os-mood-temperature-bar] 気分温度: {label} {temp}℃"
    if show_time:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        bar += f" ({now})"
    print(bar)


def log_mood_temperature(label, temp):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "label": label,
        "temperature": temp
    }
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"[os-mood-temperature-bar] ログ保存失敗: {e}", file=sys.stderr)


def list_logs(limit=10):
    if not os.path.exists(LOG_FILE):
        print("[os-mood-temperature-bar] ログがありません。")
        return
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()[-limit:]
        for line in lines:
            try:
                entry = json.loads(line)
                ts = entry["timestamp"][:19].replace("T", " ")
                label = entry["label"]
                temp = entry["temperature"]
                print(f"{ts} | {label} {temp}℃")
            except Exception:
                continue
    except Exception as e:
        print(f"[os-mood-temperature-bar] ログ読込失敗: {e}", file=sys.stderr)


def summary_logs():
    if not os.path.exists(LOG_FILE):
        print("[os-mood-temperature-bar] ログがありません。")
        return
    try:
        temps = []
        moods = {}
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    temps.append(entry["temperature"])
                    moods[entry["label"]] = moods.get(entry["label"], 0) + 1
                except Exception:
                    continue
        if not temps:
            print("[os-mood-temperature-bar] ログがありません。")
            return
        avg = round(sum(temps) / len(temps), 2)
        most = max(moods.items(), key=lambda x: x[1])[0]
        print(f"平均気分温度: {avg}℃")
        print(f"最多出現気分: {most}")
        print(f"記録数: {len(temps)}")
    except Exception as e:
        print(f"[os-mood-temperature-bar] サマリ取得失敗: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="os-mood-temperature-bar: 気分温度をランダム表示＆ログ")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser("log", help="気分温度を1件生成・表示・ログ保存")
    parser_log.add_argument("--show-time", action="store_true", help="時刻も表示")

    parser_list = subparsers.add_parser("list", help="最近の気分温度ログを表示")
    parser_list.add_argument("-n", type=int, default=10, help="表示件数")

    parser_summary = subparsers.add_parser("summary", help="気分温度ログのサマリを表示")

    args = parser.parse_args()

    if args.command == "log":
        label, temp = generate_mood_temperature()
        print_mood_temperature(label, temp, show_time=args.show_time)
        log_mood_temperature(label, temp)
    elif args.command == "list":
        list_logs(limit=args.n)
    elif args.command == "summary":
        summary_logs()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
