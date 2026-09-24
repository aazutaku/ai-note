import argparse
import random
import sys
import time
import platform

try:
    from plyer import notification
except ImportError:
    notification = None

# 古文調の詩句パーツ
POEM_SUBJECTS = [
    "西のコードベースに",
    "朝焼けのメモリ、",
    "静かなる夜に、",
    "バージョン管理の波、",
    "エラーの海を越えて、",
    "あなたのShiftキー、",
    "未割り当ての夢、",
    "デバッグの舟は",
    "静寂のターミナルに、",
    "古きAPIの森にて、"
]

POEM_PREDICATES = [
    "バグの風そよぐ",
    "今宵は静かに眠るべし",
    "静かに揺れる",
    "未定義の変数、彷徨う",
    "エラーの兆し、遠くに見ゆ",
    "リファクタの声、響き渡る",
    "コミットの灯、淡くとも",
    "警告の雨、降り注ぐ",
    "型安全の夢、儚し",
    "ビルドの神、微笑む"
]

POEM_ENDINGS = [
    "",
    "静かなる時を刻む",
    "コードの彼方へ",
    "夢の如く消えゆく",
    "バージョンを越えて",
    "開発者の心に残る",
    "新たな朝を待つ",
    "無限ループの果てに",
    "再起動の詩とともに"
]


def generate_poem():
    lines = []
    line_count = random.choice([2, 3])
    for _ in range(line_count):
        subj = random.choice(POEM_SUBJECTS)
        pred = random.choice(POEM_PREDICATES)
        ending = random.choice(POEM_ENDINGS)
        line = subj + pred
        if ending and random.random() > 0.7:
            line += "、" + ending
        lines.append(line)
    return "\n".join(lines)


def notify(title, message):
    # plyer通知 or fallbackでprint
    if notification:
        try:
            notification.notify(
                title=title,
                message=message,
                app_name="OS古代詩通知",
                timeout=8
            )
        except Exception as e:
            print(f"[通知失敗] {e}\n{title}\n{message}")
    else:
        print(f"[OS古代詩通知]\n{message}")


def run_once(args):
    poem = generate_poem()
    notify("OS古代詩通知", poem)
    if args.print:
        print(f"[OS古代詩通知]\n{poem}")


def run_random_loop(args):
    try:
        while True:
            wait = random.randint(args.min_interval, args.max_interval)
            time.sleep(wait)
            poem = generate_poem()
            notify("OS古代詩通知", poem)
            if args.print:
                print(f"[OS古代詩通知]\n{poem}")
    except KeyboardInterrupt:
        print("\n[終了] 古代詩通知ループを停止しました。")


def list_sample(args):
    print("--- 古代詩通知サンプル ---")
    for _ in range(args.count):
        print(f"[OS古代詩通知]\n{generate_poem()}\n")


def main():
    parser = argparse.ArgumentParser(
        description="謎のOS古代詩通知をデスクトップ/ターミナルにランダム表示するSkill"
    )
    subparsers = parser.add_subparsers(dest="command")

    # 明示呼び出し
    parser_once = subparsers.add_parser("once", help="1回だけ古代詩通知を表示")
    parser_once.add_argument("--print", action="store_true", help="標準出力にも表示")
    parser_once.set_defaults(func=run_once)

    # ランダムループ
    parser_loop = subparsers.add_parser("loop", help="ランダムな間隔で古代詩通知を繰り返し表示")
    parser_loop.add_argument("--min-interval", type=int, default=60, help="最短通知間隔(秒)")
    parser_loop.add_argument("--max-interval", type=int, default=300, help="最長通知間隔(秒)")
    parser_loop.add_argument("--print", action="store_true", help="標準出力にも表示")
    parser_loop.set_defaults(func=run_random_loop)

    # サンプル出力
    parser_sample = subparsers.add_parser("sample", help="古代詩通知サンプルを複数表示")
    parser_sample.add_argument("--count", type=int, default=5, help="出力する通知数")
    parser_sample.set_defaults(func=list_sample)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)
    args.func(args)

if __name__ == '__main__':
    main()
