import argparse
import random
import sys
import time

SCROLL_INTROS = [
    "紀元前の預言者より伝言：",
    "OS公式古文書より抜粋：",
    "巻物の封印が解かれた…：",
    "伝説の預言者が語る：",
    "古の巻物が囁く："
]

SCROLL_BODIES = [
    "西方のコードベースにバグの兆しあり。夜明け前に修正せよ",
    "東のモジュールに伝説の関数現る。その名は '{func}'、使い手に繁栄をもたらす",
    "南の依存関係が揺らいでいる。静かなる夜に警戒せよ",
    "北のテストケースに謎の失敗。賢者の再実行を待つ",
    "中央リポジトリに未確認のプルリクエスト出現。勇者よ、レビューせよ",
    "『{func}』という禁断の関数が呼ばれし時、バグの嵐が吹き荒れる",
    "西の森にコードの亡霊現る。デバッグの灯を絶やすな",
    "時の管理者が現れしとき、全てのCIが再び動き出す",
    "南東のキャッシュに闇の力集まる。クリーンビルドを恐れるな",
    "古代のバグレポートが蘇る。勇気ある者のみが真実を知る"
]

FAKE_FUNCTIONS = [
    "dragon_breath()",
    "phoenix_call()",
    "shadow_bind()",
    "ancient_unlock()",
    "oracle_echo()",
    "time_rewind()",
    "void_walk()",
    "mystic_merge()",
    "legendary_patch()",
    "eternal_loop()"
]

SCROLL_FOOTERS = [
    "---",
    "====",
    "***",
    "~~~",
    "(巻物ここまで)"
]


def generate_scroll():
    intro = random.choice(SCROLL_INTROS)
    body_template = random.choice(SCROLL_BODIES)
    func = random.choice(FAKE_FUNCTIONS)
    if "{func}" in body_template:
        body = body_template.format(func=func)
    else:
        body = body_template
    footer = random.choice(SCROLL_FOOTERS)
    scroll = f"[OS Ancient Scroll Alert]\n{intro}\n\"{body}\"\n{footer}"
    return scroll


def print_scroll():
    scroll = generate_scroll()
    print(scroll)


def scroll_log(n):
    for _ in range(n):
        print_scroll()
        print()
        time.sleep(0.5)


def list_templates():
    print("--- 巻物イントロ ---")
    for i, intro in enumerate(SCROLL_INTROS, 1):
        print(f"{i}. {intro}")
    print("\n--- 巻物本文テンプレート ---")
    for i, body in enumerate(SCROLL_BODIES, 1):
        print(f"{i}. {body}")
    print("\n--- 架空関数名 ---")
    for i, func in enumerate(FAKE_FUNCTIONS, 1):
        print(f"{i}. {func}")
    print("\n--- フッター ---")
    for i, footer in enumerate(SCROLL_FOOTERS, 1):
        print(f"{i}. {footer}")


def summary():
    print("このスキルは、作業の合間やコマンド実行時に、古文書風の謎めいた通知をランダム生成します。\n")
    print(f"イントロ数: {len(SCROLL_INTROS)}")
    print(f"本文テンプレート数: {len(SCROLL_BODIES)}")
    print(f"架空関数名: {len(FAKE_FUNCTIONS)}")
    print(f"フッター数: {len(SCROLL_FOOTERS)}")
    print("\n出力例:")
    print_scroll()


def main():
    parser = argparse.ArgumentParser(description="謎のOS古文書巻物通知をランダム生成・表示するスクリプト")
    subparsers = parser.add_subparsers(dest="command", required=False)

    parser_log = subparsers.add_parser("log", help="巻物通知を複数回出力")
    parser_log.add_argument("-n", type=int, default=3, help="出力回数 (デフォルト3)")

    parser_list = subparsers.add_parser("list", help="テンプレート一覧を表示")
    parser_summary = subparsers.add_parser("summary", help="スキル全体の概要と出力例を表示")

    parser.add_argument("--once", action="store_true", help="1回だけ巻物通知を出す")

    args = parser.parse_args()

    if args.command == "log":
        scroll_log(args.n)
    elif args.command == "list":
        list_templates()
    elif args.command == "summary":
        summary()
    elif args.once:
        print_scroll()
    else:
        # デフォルトは1回だけ出力
        print_scroll()

if __name__ == '__main__':
    main()
