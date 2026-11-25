import random
import sys
import argparse
import os

try:
    import notify2
except ImportError:
    notify2 = None

KOBUN_PREFIXES = [
    "東のコード谷に",
    "西のリポジトリ、",
    "南のデバッグ浜辺に、",
    "北のCI山脈より、",
    "古のバージョン管理に、",
    "令和の世にて、",
    "時の彼方のバグより、",
    "虚空のpull requestに、",
    "闇のmerge conflictが、",
    "光のテストスイートに、"
]

KOBUN_MIDDLES = [
    "バグの風が吹く…",
    "commitを忘るるなかれ。",
    "pushの儀、今始まる。",
    "printfの術は未だ健在なり。",
    "mergeの儀始まる。",
    "ビルドは静かに失敗せり。",
    "エラー、今もなお彷徨う。",
    "デプロイの鐘が鳴る。",
    "レビューの嵐、来たれり。",
    "分岐の道、汝いずれを選ぶ。"
]

KOBUN_SUFFIXES = [
    "〜巻物は静かに閉じられた〜",
    "されど汝、油断することなかれ。",
    "勇者よ、いざpushせよ。",
    "古の知恵、今ここに。",
    "エラーは友なり。",
    "汝のコード、誉れ高し。",
    "巻物は終わりぬ。",
    "静かなる夜に。",
    "再び挑むべし。",
    "汝の道は続く。"
]

MODERN_EMOJIS = [
    "(´・ω・｀)",
    "(ノД`)・゜・。",
    "( ﾟДﾟ)",
    "( ͡° ͜ʖ ͡°)",
    "( ˘ω˘ )",
    "(；´∀｀)",
    "(・∀・)",
    "(￣ー￣)",
    "(ง'̀-'́)ง",
    "( ´∀｀)"
]

SCROLL_TOP = "┏━━━━━━━━━━━━━━━━━━━━━━━┓"
SCROLL_BOTTOM = "┗━━━━━━━━━━━━━━━━━━━━━━━┛"

def generate_scroll():
    prefix = random.choice(KOBUN_PREFIXES)
    middle = random.choice(KOBUN_MIDDLES)
    suffix = random.choice(KOBUN_SUFFIXES)
    emoji = random.choice(MODERN_EMOJIS)
    # 2-4行構成
    lines = [
        f" {prefix}{middle} {emoji} ",
        f" {suffix} ",
    ]
    # 追加行をランダムに挟む
    if random.random() > 0.5:
        extra = random.choice(KOBUN_MIDDLES)
        lines.insert(1, f" {extra} ")
    # パディング調整
    maxlen = max(len(l) for l in lines)
    padded = [l.ljust(maxlen) for l in lines]
    return [SCROLL_TOP] + padded + [SCROLL_BOTTOM]

def display_terminal(scroll_lines):
    for line in scroll_lines:
        print(line)

def display_desktop(scroll_lines, summary="古代絵文字巻物通知"):
    if notify2 is None:
        return False
    try:
        notify2.init("Ancient Emoji Scroll Notifier")
        body = "\n".join(scroll_lines[1:-1])
        n = notify2.Notification(summary, body)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.show()
        return True
    except Exception as e:
        return False

def log_scroll(scroll_lines, logfile):
    try:
        with open(logfile, "a", encoding="utf-8") as f:
            f.write("\n".join(scroll_lines) + "\n\n")
    except Exception as e:
        print(f"[warn] ログ保存失敗: {e}")

def list_logs(logfile, count=5):
    if not os.path.exists(logfile):
        print("ログファイルがありません")
        return
    with open(logfile, encoding="utf-8") as f:
        lines = f.readlines()
    blocks = []
    block = []
    for line in lines:
        if line.strip() == SCROLL_TOP:
            if block:
                blocks.append(block)
            block = [line.rstrip()]
        elif line.strip() == SCROLL_BOTTOM:
            block.append(line.rstrip())
            blocks.append(block)
            block = []
        else:
            if block:
                block.append(line.rstrip())
    if block:
        blocks.append(block)
    for b in blocks[-count:]:
        print("\n".join(b))
        print()

def parse_args():
    parser = argparse.ArgumentParser(
        description="謎のOS古代絵文字巻物通知を炸裂させるSkill"
    )
    subparsers = parser.add_subparsers(dest="command", required=False)

    parser_notify = subparsers.add_parser("notify", help="巻物通知を表示")
    parser_notify.add_argument("--log", action="store_true", help="通知内容をログに保存")
    parser_notify.add_argument("--desktop", action="store_true", help="デスクトップ通知も試行")

    parser_list = subparsers.add_parser("list", help="過去の通知ログを表示")
    parser_list.add_argument("--count", type=int, default=5, help="表示する巻物数")

    return parser.parse_args()

def main():
    args = parse_args()
    logfile = os.path.expanduser("~/.ancient_emoji_scroll.log")
    if args.command == "list":
        list_logs(logfile, count=args.count)
        return
    # default: notify
    scroll = generate_scroll()
    displayed = False
    if getattr(args, "desktop", False):
        displayed = display_desktop(scroll)
    if not displayed:
        display_terminal(scroll)
    if getattr(args, "log", False):
        log_scroll(scroll, logfile)

if __name__ == "__main__":
    main()
