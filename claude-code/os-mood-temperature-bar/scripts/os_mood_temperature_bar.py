import argparse
import json
import os
import random
import sys
import datetime
from typing import List, Dict, Any

LOG_FILE = os.path.expanduser("~/.os_mood_log.json")
COMMENTS = [
    (15, "冷え冷え…"),
    (20, "低気圧注意"),
    (25, "ぼちぼち"),
    (30, "まあまあ"),
    (35, "上昇中！"),
    (39, "絶好調！"),
    (42, "炎上中！"),
    (45, "危険域！")
]

def generate_mood_temperature() -> Dict[str, Any]:
    temp = round(random.uniform(15.0, 45.0), 1)
    comment = None
    for threshold, comm in COMMENTS:
        if temp <= threshold:
            comment = comm
            break
    if comment is None:
        comment = "？？？"
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "temperature": temp,
        "comment": comment
    }

def print_mood_bar(entry: Dict[str, Any]):
    print(f"[OS-Mood-Bar] 気分温度: {entry['temperature']}度 {entry['comment']}")

def load_log() -> List[Dict[str, Any]]:
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

def save_log(entries: List[Dict[str, Any]]):
    try:
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            json.dump(entries, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[OS-Mood-Bar] ログ保存失敗: {e}", file=sys.stderr)

def log_temperature():
    entry = generate_mood_temperature()
    entries = load_log()
    entries.append(entry)
    save_log(entries)
    print_mood_bar(entry)

def list_temperatures():
    entries = load_log()
    if not entries:
        print("[OS-Mood-Bar] ログがありません。")
        return
    for entry in entries[-20:]:
        ts = entry.get('timestamp', '')
        temp = entry.get('temperature', '?')
        comment = entry.get('comment', '')
        print(f"{ts} | {temp}度 {comment}")

def summary_temperatures():
    entries = load_log()
    if not entries:
        print("[OS-Mood-Bar] ログがありません。")
        return
    temps = [e['temperature'] for e in entries if 'temperature' in e]
    avg = sum(temps) / len(temps)
    mx = max(temps)
    mn = min(temps)
    print(f"[OS-Mood-Bar] ログ件数: {len(temps)}")
    print(f"平均: {avg:.1f}度 最高: {mx:.1f}度 最低: {mn:.1f}度")

def clear_log():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print("[OS-Mood-Bar] ログを削除しました。")
    else:
        print("[OS-Mood-Bar] ログファイルが存在しません。")

def main():
    parser = argparse.ArgumentParser(description='OS Mood Temperature Bar')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('log', help='現在の気分温度を記録し表示')
    subparsers.add_parser('list', help='気分温度ログを表示')
    subparsers.add_parser('summary', help='気分温度ログの統計')
    subparsers.add_parser('clear', help='気分温度ログを削除')

    args = parser.parse_args()
    if not args.command:
        # デフォルトで1回表示
        entry = generate_mood_temperature()
        print_mood_bar(entry)
        sys.exit(0)
    if args.command == 'log':
        log_temperature()
    elif args.command == 'list':
        list_temperatures()
    elif args.command == 'summary':
        summary_temperatures()
    elif args.command == 'clear':
        clear_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
