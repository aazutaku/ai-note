import sys
import argparse
import random
import threading
import time
import tkinter as tk
from tkinter import font as tkfont

SCROLL_TEXTS = [
    [
        "西のコードベースにバグの気運漂う",
        "レビュアーの機嫌は末吉",
        "東の山より新たな仕様書が届く",
        "朝霧の中、ビルドは静かに失敗す"
    ],
    [
        "南のリポジトリ、謎のマージ衝突あり",
        "今日のCI、波高し",
        "古きAPI、未だ現役",
        "北風に乗りてPR流る"
    ],
    [
        "西方、無限ループの噂立つ",
        "レビュアー、昼寝中につき審議遅延",
        "朝焼けに染まるコードレビュー",
        "仕様書、解読不能の巻物となる"
    ],
    [
        "東の山、未読のissue積もりけり",
        "本日、デプロイ運気は小吉",
        "バグ、静かに忍び寄る",
        "古文書に残るバグの記憶"
    ],
    [
        "北の森、ドキュメント迷宮化す",
        "レビュアーの一言、雷鳴の如し",
        "西風に乗りて仕様変更来たる",
        "深夜のビルド、霧の中に消ゆ"
    ],
    [
        "南の海、未解決のエラー漂う",
        "本日、テストカバレッジ微増",
        "古きバグ、新たな姿に化ける",
        "レビュアー、沈黙を守る"
    ]
]


def random_scroll_text():
    return random.choice(SCROLL_TEXTS)


def display_scroll_alert(lines, duration=8):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.withdraw()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # UI設定
    frame = tk.Frame(root, bg="#f5ecd2", bd=4, relief=tk.RIDGE)
    frame.pack(fill=tk.BOTH, expand=True)

    # フォント設定
    try:
        scroll_font = tkfont.Font(family="MS Mincho", size=15, weight="bold")
    except Exception:
        scroll_font = tkfont.Font(size=15, weight="bold")

    # 巻物風タイトル
    title = tk.Label(frame, text=" 謎のOS公式・古文書巻物通知 ", bg="#c2b280", fg="#3f3210", font=("MS Gothic", 12, "bold"))
    title.pack(fill=tk.X, pady=(0, 4))

    # 本文
    for line in lines:
        lbl = tk.Label(frame, text=line, bg="#f5ecd2", fg="#2c2000", font=scroll_font, anchor="w", justify=tk.LEFT)
        lbl.pack(anchor="w", padx=16)

    # 巻物枠風に
    frame.update_idletasks()
    width = frame.winfo_width() or 380
    height = frame.winfo_height() or (32 * len(lines) + 40)

    # 画面右下に配置
    x = screen_width - width - 20
    y = screen_height - height - 60
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.deiconify()

    def close():
        root.destroy()

    # 指定秒数後に自動消去
    root.after(duration * 1000, close)
    root.mainloop()


def scroll_alert_command(args):
    lines = random_scroll_text()
    display_scroll_alert(lines, duration=args.duration)


def list_scrolls_command(args):
    print("--- 登録済み巻物通知サンプル ---")
    for i, lines in enumerate(SCROLL_TEXTS):
        print(f"[{i+1}] ")
        for l in lines:
            print(f"  {l}")
        print()


def summary_command(args):
    print("このSkillは、作業中やコマンド実行の合間に、
謎のOS公式・古文書巻物通知を画面端に表示します。通知内容は毎回ランダム生成され、集中力をブレイクするエンタメ演出です。")
    print(f"登録済み通知パターン数: {len(SCROLL_TEXTS)}")


def auto_mode(interval=900):
    try:
        while True:
            lines = random_scroll_text()
            t = threading.Thread(target=display_scroll_alert, args=(lines,))
            t.start()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("自動巻物通知モード終了")


def main():
    parser = argparse.ArgumentParser(description="謎のOS公式・古文書巻物通知 Skill")
    subparsers = parser.add_subparsers(dest="command")

    parser_alert = subparsers.add_parser("alert", help="巻物通知を即座に表示")
    parser_alert.add_argument("--duration", type=int, default=8, help="表示秒数 (デフォルト8秒)")
    parser_alert.set_defaults(func=scroll_alert_command)

    parser_list = subparsers.add_parser("list", help="巻物通知サンプル一覧表示")
    parser_list.set_defaults(func=list_scrolls_command)

    parser_summary = subparsers.add_parser("summary", help="Skill概要を表示")
    parser_summary.set_defaults(func=summary_command)

    parser_auto = subparsers.add_parser("auto", help="一定間隔で自動巻物通知モード")
    parser_auto.add_argument("--interval", type=int, default=900, help="通知間隔秒 (デフォルト15分)")
    parser_auto.set_defaults(func=lambda args: auto_mode(args.interval))

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
