import random
import sys
import os
import argparse
import subprocess
import platform
import time
from datetime import datetime

KOBUN_PHRASES = [
    "東のコード谷にバグの風ぞ吹きぬる",
    "古きOSの夢にて、エラーの影ほの見ゆる",
    "時は令和、されど記号の宴は止まず",
    "バグぞ鳴く、夜半のメモリに",
    "巻物開けば、警告の文字また現る",
    "汝、再起動を恐るるなかれ",
    "命令の彼方に、未知のエラー潜む",
    "古人曰く、ログは巻物に如かず",
    "メモリの彼岸にて、デバッグの鬼踊る",
    "西の端末にて、警告の声高らかに"
]

MODERN_FACES = [
    "(；´Д｀)", "(ﾟ∀ﾟ)", "（￣ー￣）ﾆﾔﾘ", "#(・_・;)#", "( ﾟдﾟ)", "(・ω・)", "(｀・ω・´)", "(´・ω・｀)", "(╯°□°）╯︵ ┻━┻", "(・∀・)"
]

SYMBOLS = [
    "--", "##", "==", "***", "//", "\\", "::", "...", "++", "@@"
]

HEADER = "【巻物】"

EXAMPLES = [
    [HEADER, KOBUN_PHRASES[0] + "…" + MODERN_FACES[0], KOBUN_PHRASES[2], SYMBOLS[1] + " " + MODERN_FACES[1] + " " + SYMBOLS[1]],
    [HEADER, KOBUN_PHRASES[1], MODERN_FACES[3] + " されど我、再起動を恐れず。"],
    [HEADER, KOBUN_PHRASES[3], MODERN_FACES[2]]
]

TRIGGER_KEYWORDS = ["バグ", "エラー", "巻物", "通知", "古文", "顔文字"]


def generate_scroll():
    lines = [HEADER]
    num_lines = random.randint(2, 4)
    used_kobun = set()
    for _ in range(num_lines):
        phrase = random.choice(KOBUN_PHRASES)
        # avoid repeats
        while phrase in used_kobun:
            phrase = random.choice(KOBUN_PHRASES)
        used_kobun.add(phrase)
        # 50%で顔文字や記号を混ぜる
        if random.random() < 0.5:
            face = random.choice(MODERN_FACES)
            symbol = random.choice(SYMBOLS)
            if random.random() < 0.5:
                line = f"{phrase}…{face}"
            else:
                line = f"{symbol} {face} {symbol}"
        else:
            line = phrase
        lines.append(line)
    return "\n".join(lines)


def show_terminal(scroll_text):
    print(scroll_text)


def show_desktop_notification(scroll_text, title="巻物通知"):
    system = platform.system()
    try:
        if system == "Darwin":
            # macOS
            script = f'display notification "{scroll_text.replace("\"", "'")}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif system == "Linux":
            # Linux (notify-send)
            subprocess.run(["notify-send", title, scroll_text], check=True)
        else:
            # Windowsや他は未対応
            pass
    except Exception as e:
        print(f"[通知エラー]: {e}")


def should_trigger(args):
    # 明示呼び出し or キーワード検出 or 長時間無操作
    if args.explicit:
        return True
    if args.input_text:
        for kw in TRIGGER_KEYWORDS:
            if kw in args.input_text:
                return True
    if args.idle and args.idle > 0:
        # idle秒数分、無操作を模擬
        print(f"{args.idle}秒間待機中...（無操作シミュレーション）")
        time.sleep(args.idle)
        return True
    return False


def show_examples():
    for example in EXAMPLES:
        print("\n".join(example))
        print()


def main():
    parser = argparse.ArgumentParser(description="謎のOS古代絵文字巻物通知スキル")
    parser.add_argument("--explicit", action="store_true", help="明示的に巻物通知を発動")
    parser.add_argument("--input-text", type=str, help="コマンドや文章からキーワード検出で発動")
    parser.add_argument("--desktop", action="store_true", help="デスクトップ通知も出す")
    parser.add_argument("--idle", type=int, default=0, help="指定秒数無操作後に発動")
    parser.add_argument("--examples", action="store_true", help="出力例を表示")
    args = parser.parse_args()

    if args.examples:
        show_examples()
        sys.exit(0)

    if should_trigger(args):
        scroll = generate_scroll()
        show_terminal(scroll)
        if args.desktop:
            show_desktop_notification(scroll)
    else:
        print("[巻物通知] 発動条件を満たしませんでした。--help 参照")

if __name__ == '__main__':
    main()
