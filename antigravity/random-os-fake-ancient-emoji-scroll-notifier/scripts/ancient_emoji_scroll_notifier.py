import random
import sys
import os
import subprocess
import argparse
from datetime import datetime

ANCIENT_OPENINGS = [
    "東のコード谷にバグの風が吹く……",
    "いにしえのcommit、今も尚リベースされず。",
    "西の彼方より、警告の鐘が鳴り響く。",
    "南の島にて、exit code 1の影揺らぐ。",
    "北の森に、未解決のPR眠る。",
    "時の彼方より、Segmentation faultの声響く。",
    "古のmain関数、未だreturnせず。",
    "闇夜に忍ぶ、NullPointerの術。"
]

ANCIENT_BODIES = [
    "されど、printfの術は未だ極まらず。",
    "バグは静かに忍び寄る。",
    "夢の如し、#TODOは積もるばかり。",
    "警告多き世に、try-catchの光差す。",
    "commitの波に、stash流される。",
    "仕様書の奥底に、未解決の謎あり。",
    "pushの彼方に、merge conflict待つ。",
    "デバッグの道、果てしなし。"
]

ANCIENT_ENDINGS = [
    "── {year}年 {month}月の刻",
    "── {hour}時{minute}分、風止まず。",
    "── この行末にて、巻物閉じる。",
    "── いましばし、心静かに。"
]

MODERN_INSERTS = [
    "(´・ω・`)",
    "(ノ∀`)",
    "#TODO: 夢の如し。",
    "[WIP]",
    "( ;∀;)",
    "( ﾟдﾟ)",
    "// FIXME: 忘却の彼方",
    "[ERROR]",
    "( ˘ω˘ )ｽﾔｧ",
    "[INFO]",
    "( ͡° ͜ʖ ͡°)",
    "[WARNING]"
]

BORDER_TOP = "┏━━━━━━━━━━━━━━━━━━━━━━━┓"
BORDER_BOTTOM = "┗━━━━━━━━━━━━━━━━━━━━━━━┛"


def random_scroll_message():
    now = datetime.now()
    opening = random.choice(ANCIENT_OPENINGS)
    body = random.choice(ANCIENT_BODIES)
    ending = random.choice(ANCIENT_ENDINGS).format(
        year=now.year,
        month=now.month,
        hour=now.hour,
        minute=str(now.minute).zfill(2)
    )
    # 1-2 modern inserts, random position
    inserts = random.sample(MODERN_INSERTS, k=random.randint(1,2))
    lines = [opening]
    # Insert modern insert randomly in lines
    insert_pos = random.randint(1,2)
    if insert_pos == 1:
        lines.append(inserts[0])
        lines.append(body)
    else:
        lines.append(body)
        lines.append(inserts[0])
    if len(inserts) > 1:
        lines.append(inserts[1])
    lines.append(ending)
    return lines


def format_scroll(lines):
    box = [BORDER_TOP]
    for line in lines:
        # Pad line to 35 fullwidth chars
        content = f"┃ {line.ljust(32)}┃"
        box.append(content)
    box.append(BORDER_BOTTOM)
    return "\n".join(box)


def notify_desktop(message, title="古代巻物通知"):
    # Try notify-send (Linux), then osascript (macOS)
    if sys.platform.startswith("linux"):
        try:
            subprocess.run([
                "notify-send", title, message
            ], check=True)
            return True
        except Exception as e:
            return False
    elif sys.platform == "darwin":
        osa_script = f'display notification "{message}" with title "{title}"'
        try:
            subprocess.run([
                "osascript", "-e", osa_script
            ], check=True)
            return True
        except Exception as e:
            return False
    return False


def main():
    parser = argparse.ArgumentParser(
        description="謎のOS古代絵文字巻物通知スクリプト"
    )
    parser.add_argument(
        "--mode", choices=["terminal", "desktop", "both"], default="terminal",
        help="通知の出力先 (terminal/desktop/both)"
    )
    parser.add_argument(
        "--count", type=int, default=1, help="連続通知回数"
    )
    parser.add_argument(
        "--interval", type=float, default=0, help="通知間隔(秒)"
    )
    parser.add_argument(
        "--log", type=str, default=None, help="通知内容を保存するファイルパス"
    )
    args = parser.parse_args()

    for i in range(args.count):
        lines = random_scroll_message()
        scroll = format_scroll(lines)
        message_flat = " ".join(lines)
        if args.mode in ("terminal", "both"):
            print(scroll)
        if args.mode in ("desktop", "both"):
            notify_desktop(message_flat)
        if args.log:
            try:
                with open(args.log, "a", encoding="utf-8") as f:
                    f.write(scroll + "\n\n")
            except Exception as e:
                print(f"[WARN] ログ保存失敗: {e}", file=sys.stderr)
        if args.interval > 0 and i < args.count-1:
            import time
            time.sleep(args.interval)

if __name__ == "__main__":
    main()
