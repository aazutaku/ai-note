import os
import json
import sys
from datetime import datetime

SNAPSHOT_DIR = ".claude/skills/context-branch-snapshot/snapshots"

def get_current_context():
    # Claude Code API/環境変数から取得する想定
    context = {
        "directory": os.getcwd(),
        "paths": [],
        "memory": "",
        "timestamp": datetime.now().isoformat()
    }
    # 例: 参照中のファイル一覧 (必要ならAPIで取得)
    if os.path.exists(".claude/context.json"):
        with open(".claude/context.json") as f:
            data = json.load(f)
            context["paths"] = data.get("paths", [])
            context["memory"] = data.get("memory", "")
    return context

def save_snapshot(name):
    if not os.path.exists(SNAPSHOT_DIR):
        os.makedirs(SNAPSHOT_DIR)
    context = get_current_context()
    path = os.path.join(SNAPSHOT_DIR, f"{name}.json")
    with open(path, "w") as f:
        json.dump(context, f, indent=2)
    print(f"[context-branch-snapshot] スナップショット \"{name}\" を保存しました。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: snapshot.py [snapshot_name]")
        sys.exit(1)
    name = sys.argv[1]
    save_snapshot(name)