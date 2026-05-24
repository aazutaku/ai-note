import os

SNAPSHOT_DIR = ".claude/skills/context-branch-snapshot/snapshots"

def list_snapshots():
    if not os.path.exists(SNAPSHOT_DIR):
        print("[context-branch-snapshot] スナップショットはありません。")
        return
    files = [f for f in os.listdir(SNAPSHOT_DIR) if f.endswith(".json")]
    if not files:
        print("[context-branch-snapshot] スナップショットはありません。")
        return
    print("[context-branch-snapshot] 保存済みスナップショット一覧:")
    for f in files:
        name = f.replace(".json", "")
        print(f"- {name}")

if __name__ == "__main__":
    list_snapshots()