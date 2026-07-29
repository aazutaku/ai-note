import random
import sys
import argparse
import os
import time
from datetime import datetime
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

# 各カテゴリのテンプレート
BUG_FIXES = [
    "机の上の書類が自動で増殖する問題を解消しました。",
    "コーヒーカップの残量が誤表示される不具合を修正。",
    "ディスプレイの明るさが夜になると勝手に上がる問題を修正。",
    "椅子の高さがランダムに変動する現象を改善。",
    "USBメモリが刺さっていないのに認識されるバグを修正。",
    "ネットワークが満月の夜にだけ不安定になる問題を修正。",
    "ファイル名が時々詩的になる現象を修正。",
    "マウスカーソルが画面端で消える問題を修正。",
    "画面の端に謎の影が出現するバグを修正。",
    "タイピング速度が突然落ちる現象を改善。"
]

FEATURES = [
    "集中力が一瞬だけ上昇するアルゴリズムを追加。",
    "マウスカーソルが時々踊る機能を実装。",
    "デスクトップに仮想観葉植物を自動配置する機能を追加。",
    "おやつタイムを自動で通知する機能を搭載。",
    "キーボードの音がランダムで変わる新機能を追加。",
    "天気に応じて壁紙が変わる機能を実装。",
    "仮想ペットが画面上を歩く新機能を追加。",
    "エラー音が和音になる機能を搭載。",
    "ランダムでやる気を出すメッセージを表示する機能を追加。",
    "会議中に自動でミュート解除する機能を実装（非推奨）。"
]

KNOWN_ISSUES = [
    "おやつの消費が止まらない現象が継続中です。",
    "椅子が時々勝手に回転する問題が未解決です。",
    "仮想ペットがたまに消えることがあります。",
    "壁紙が深夜に変わらない場合があります。",
    "集中力アルゴリズムが逆効果になることがあります。",
    "コーヒー残量表示が正確でない場合があります。",
    "会議自動ミュート解除が意図せず発動する可能性があります。",
    "観葉植物が枯れることがあります（仮想）。",
    "やる気メッセージが逆効果になる場合があります。",
    "タイピング音が突然消えることがあります。"
]

VERSION_PREFIXES = [
    "v3.1.", "v2.9.", "v4.0.", "v1.8.", "v5.2.", "v0.9.", "v6.0.", "v2.1.", "v3.5.", "v1.2."
]

# Patch Noteを生成
def generate_patch_note():
    version = random.choice(VERSION_PREFIXES) + str(random.randint(10, 99))
    bug_count = random.randint(1, 2)
    feature_count = random.randint(1, 2)
    known_count = random.randint(1, 2)
    bugs = random.sample(BUG_FIXES, bug_count)
    features = random.sample(FEATURES, feature_count)
    knowns = random.sample(KNOWN_ISSUES, known_count)
    lines = [f"[FakeOS Patch Note {version}]"]
    for b in bugs:
        lines.append(f"- バグ修正: {b}")
    for f in features:
        lines.append(f"- 新機能: {f}")
    for k in knowns:
        lines.append(f"- 既知の問題: {k}")
    return "\n".join(lines)

# 通知送信
def send_notification(title, message):
    if not PLYER_AVAILABLE:
        return False
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="FakeOS Patch Note",
            timeout=7
        )
        return True
    except Exception:
        return False

# ログ保存
LOG_FILE = os.path.expanduser("~/.fake_patch_note.log")
def log_patch_note(note):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().isoformat()}]\n{note}\n\n")
    except Exception:
        pass

def list_logs(count=5):
    if not os.path.exists(LOG_FILE):
        print("No logs found.")
        return
    try:
        with open(LOG_FILE, encoding="utf-8") as f:
            logs = f.read().strip().split("\n\n")
            for log in logs[-count:]:
                print(log)
    except Exception:
        print("Failed to read logs.")

def summary_logs():
    if not os.path.exists(LOG_FILE):
        print("No logs found.")
        return
    try:
        with open(LOG_FILE, encoding="utf-8") as f:
            logs = f.read().strip().split("\n\n")
            print(f"合計 {len(logs)} 件のパッチノートが生成されました。")
    except Exception:
        print("Failed to summarize logs.")

# 頻度制御用（最短間隔: 30秒）
LAST_RUN_FILE = os.path.expanduser("~/.fake_patch_note.last")
def can_run():
    now = time.time()
    if os.path.exists(LAST_RUN_FILE):
        try:
            with open(LAST_RUN_FILE) as f:
                last = float(f.read().strip())
                if now - last < 30:
                    return False
        except Exception:
            pass
    try:
        with open(LAST_RUN_FILE, "w") as f:
            f.write(str(now))
    except Exception:
        pass
    return True

def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Patch Note Generator")
    subparsers = parser.add_subparsers(dest="command")

    gen_parser = subparsers.add_parser("gen", help="Generate and show a fake patch note")
    list_parser = subparsers.add_parser("list", help="Show recent patch notes")
    list_parser.add_argument("-n", type=int, default=5, help="Number of logs to show")
    summary_parser = subparsers.add_parser("summary", help="Show patch note summary")

    args = parser.parse_args()

    if args.command == "gen" or args.command is None:
        if can_run():
            note = generate_patch_note()
            print(note)
            log_patch_note(note)
            send_notification("FakeOS Patch Note", note)
        else:
            print("(パッチノートの頻度制御中: しばらくお待ちください)")
    elif args.command == "list":
        list_logs(args.n)
    elif args.command == "summary":
        summary_logs()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
