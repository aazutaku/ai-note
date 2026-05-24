import os
import json
from datetime import datetime

# Claude Code の session 履歴ファイル例
HISTORY_PATH = os.path.expanduser("~/.claude/code_history.json")

EXCLUDE_DIRS = {"node_modules", "build", "dist", ".git", "__pycache__"}

def load_history():
    with open(HISTORY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def is_relevant_path(path):
    parts = path.strip("/").split("/")
    return not any(part in EXCLUDE_DIRS for part in parts)

def extract_context_switches(history):
    switches = []
    last_path = None
    last_time = None
    for entry in history:
        path = entry.get("directory") or entry.get("path")
        ts = entry.get("timestamp")
        if not path or not ts or not is_relevant_path(path):
            continue
        if last_path is None or last_path != path:
            if last_path is not None:
                switches[-1]["end"] = ts
            switches.append({"start": ts, "path": path})
            last_path = path
        last_time = ts
    # 最後の滞在記録
    if switches and "end" not in switches[-1]:
        switches[-1]["end"] = last_time
    return switches

def format_switch_history(switches):
    out = []
    for idx, sw in enumerate(switches):
        start = datetime.fromisoformat(sw["start"])
        end = datetime.fromisoformat(sw["end"])
        mins = int((end - start).total_seconds() // 60)
        label = f"[{start.strftime('%Y-%m-%d %H:%M')}] {sw['path']} ({mins}分)"
        out.append(label)
    return out

def print_summary(switches):
    print("--- Context Switch History ---")
    lines = format_switch_history(switches)
    for line in lines:
        print(line)
    print()
    if len(switches) >= 2:
        prev = switches[-2]["path"]
        curr = switches[-1]["path"]
        print(f"直近の切替イベント: {prev} → {curr}")
    print(f"合計 context 切替回数: {len(switches)}")
    avg = int(sum(
        (datetime.fromisoformat(sw["end"]) - datetime.fromisoformat(sw["start"])).total_seconds()
        for sw in switches
    ) // 60 // len(switches)) if switches else 0
    print(f"滞在時間の平均: {avg}分")

if __name__ == "__main__":
    history = load_history()
    switches = extract_context_switches(history)
    print_summary(switches)