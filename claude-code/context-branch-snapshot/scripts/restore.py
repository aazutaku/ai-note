import os
import json
import sys

SNAPSHOT_DIR = ".claude/skills/context-branch-snapshot/snapshots"

def restore_snapshot(name):
    path = os.path.join(SNAPSHOT_DIR, f"{name}.json")
    if not os.path.exists(path):
        print(f"[context-branch-snapshot] スナップショット \"{name}\" が見つかりません。")
        sys.exit(1)
    with open(path) as f:
        context = json.load(f)
    # Claude Code の context 復元 (例: .claude/context.json に書き戻す)
    with open(".claude/context.json", "w") as out:
        json.dump(context, out, indent=2)
    print(f"[context-branch-snapshot] スナップショット \"{name}\" から context を復元しました。")
    print(f"- directory: {context.get('directory')}")
    print(f"- paths: {context.get('paths')}")
    print(f"- memory: {context.get('memory')[:50]}...")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: restore.py [snapshot_name]")
        sys.exit(1)
    name = sys.argv[1]
    restore_snapshot(name)