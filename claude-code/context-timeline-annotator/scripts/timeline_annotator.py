import os
import json
from datetime import datetime

def load_claude_history(history_path):
    with open(history_path, "r", encoding="utf-8") as f:
        return json.load(f)

def annotate_step(step):
    # 編集種別やファイル種別・diff内容から意図を推測して短い注釈を返す
    if step["action"] == "create":
        if step["path"].endswith(".md"):
            return "ドキュメント新規追加"
        elif step["path"].endswith((".js", ".ts", ".py")):
            return "新機能追加"
        else:
            return "ファイル新規作成"
    elif step["action"] == "edit":
        if "test" in step["path"]:
            return "テストケース追加・修正"
        elif "fix" in step.get("message", "").lower():
            return "バグ修正"
        elif "refactor" in step.get("message", "").lower():
            return "リファクタリング"
        else:
            return "編集"
    elif step["action"] == "delete":
        return "不要ファイル削除"
    else:
        return "履歴"

def format_timeline(history_steps):
    lines = []
    for step in history_steps:
        dt = datetime.fromisoformat(step["timestamp"])
        comment = annotate_step(step)
        lines.append(f"[{dt.strftime('%Y-%m-%d %H:%M')}]  {step['path']} {step['action']}  # {comment}")
    return "\n".join(lines)

def main():
    # Claude Code の履歴ファイルの場所を仮定
    history_path = os.environ.get("CLAUDE_HISTORY_PATH", "./claude_history.json")
    if not os.path.exists(history_path):
        print("Claude Code 履歴ファイルが見つかりません")
        return
    history = load_claude_history(history_path)
    # 最新15件まで
    steps = sorted(history, key=lambda x: x["timestamp"])[-15:]
    print(format_timeline(steps))

if __name__ == "__main__":
    main()