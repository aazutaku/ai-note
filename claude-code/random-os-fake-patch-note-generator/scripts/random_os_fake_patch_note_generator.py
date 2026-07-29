import os
import sys
import random
import time
import argparse
from datetime import datetime, timedelta

try:
    import notify2
except ImportError:
    notify2 = None

LOG_FILE = os.path.expanduser("~/.os_patch_notes.log")
FREQUENCY_LIMIT_SEC = 60

PATCH_NOTE_TEMPLATES = [
    {
        "type": "新機能",
        "messages": [
            "コーヒーの温度を自動調整するAIを搭載",
            "集中力が一瞬だけ上昇する新アルゴリズム搭載",
            "ウィンドウの角が丸くなりました（見た目のみ）",
            "デバッグ用の自己肯定感ブースト機能を追加",
            "タスクバーに謎のボタンが現れるようになりました"
        ]
    },
    {
        "type": "バグ修正",
        "messages": [
            "机の上の書類が片付かない問題を修正",
            "集中力が一瞬だけ上昇する不具合を修正",
            "ファイル保存時におやつを食べ過ぎるバグを修正",
            "エラー時にため息が出る現象を修正",
            "椅子が急にきしむ問題を修正"
        ]
    },
    {
        "type": "改善",
        "messages": [
            "ウィンドウの移動速度が1.5倍になりました（体感）",
            "通知音がより心地よくなりました",
            "背景色が微妙に明るくなりました",
            "メモリの気分が向上しました",
            "アイコンがほんの少し大きくなりました"
        ]
    },
    {
        "type": "既知の問題",
        "messages": [
            "おやつの消費が止まらない",
            "夕方になると眠くなる",
            "タスクが勝手に増える現象が継続中",
            "ランチ後の眠気は未解決",
            "会議が終わらないことがある"
        ]
    }
]

VERSION_PREFIXES = ["v3.14.159", "v2.71.828", "v1.61.803", "v0.99.999", "v4.20.000"]


def generate_patch_note():
    version = random.choice(VERSION_PREFIXES)
    sections = []
    used_types = set()
    for _ in range(random.randint(3, 4)):
        section = random.choice(PATCH_NOTE_TEMPLATES)
        if section["type"] in used_types:
            continue
        used_types.add(section["type"])
        message = random.choice(section["messages"])
        sections.append(f"[{section['type']}] {message}")
    note = f"=== OS Patch Note {version} ===\n" + "\n".join(sections) + "\n-------------------------------"
    return note


def can_emit_patch_note():
    if not os.path.exists(LOG_FILE):
        return True
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            return True
        last_line = lines[-1]
        ts_str = last_line.split("|", 1)[0].strip()
        last_time = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
        if datetime.now() - last_time > timedelta(seconds=FREQUENCY_LIMIT_SEC):
            return True
        return False
    except Exception:
        return True


def log_patch_note(note):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}|{note}\n")


def show_notification(note):
    if notify2 is None:
        return False
    try:
        notify2.init("Fake OS Patch Note")
        n = notify2.Notification("Fake OS Patch Note", note)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.set_timeout(5000)
        n.show()
        return True
    except Exception:
        return False


def print_patch_note(note):
    print(note)


def show_patch_note():
    if not can_emit_patch_note():
        return
    note = generate_patch_note()
    log_patch_note(note)
    shown = show_notification(note)
    if not shown:
        print_patch_note(note)


def list_patch_notes(limit=10):
    if not os.path.exists(LOG_FILE):
        print("No patch notes logged yet.")
        return
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()[-limit:]
    for line in lines:
        ts, note = line.split("|", 1)
        print(f"[{ts}]\n{note.strip()}\n")


def summary_patch_notes():
    if not os.path.exists(LOG_FILE):
        print("No patch notes logged yet.")
        return
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()[-5:]
    print("=== Recent Fake OS Patch Notes Summary ===")
    for line in lines:
        ts, note = line.split("|", 1)
        first_line = note.strip().split("\n")[0]
        print(f"{ts}: {first_line}")


def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Patch Note Generator")
    subparsers = parser.add_subparsers(dest="command", required=False)

    subparsers.add_parser("log", help="Show recent patch notes log")
    subparsers.add_parser("summary", help="Show summary of recent patch notes")
    subparsers.add_parser("generate", help="Force generate a new patch note")

    args = parser.parse_args()

    if args.command == "log":
        list_patch_notes()
    elif args.command == "summary":
        summary_patch_notes()
    elif args.command == "generate":
        show_patch_note()
    else:
        show_patch_note()

if __name__ == '__main__':
    main()
