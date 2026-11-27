import argparse
import random
import sys
import time
from datetime import datetime

SCROLL_INTRO = [
    "=== 古文書巻物通知 ===",
    "=== OS公式・古文書の巻物 ===",
    "=== 謎の預言書アラート ===",
]
SCROLL_OUTRO = [
    "====================",
    "=== 巻物ここまで ===",
    "=== 伝説の終わり ===",
]
SCROLL_LINES = [
    "時は今、西のコードベースにバグの兆しあり。",
    "東のモジュールに伝説の関数現る。",
    "北のデバッグログ、静寂の中に警告隠る。",
    "南の依存関係、更新の風が吹く。",
    "古の設計書より、未踏のバグが甦る。",
    "ビルドの谷間に、警告の影走る。",
    "テストの森に、迷いし例外の声響く。",
    "リファクタの嵐、静けさの後に現る。",
    "依存の海に、未確認のパッケージ漂う。",
    "ログの砂漠、沈黙の中にヒント眠る。",
    "東方のPull Request、伝説のレビュー待つ。",
    "西のIssue、解決の使者未だ現れず。",
    "南のCI/CD、神速の如く流れる。",
    "北のAPI、古き仕様を守り続ける。",
    "設計の塔に、知恵の光差し込む。",
    "バグの谷間、勇者のデバッグ現る。",
    "コードの迷宮、出口なき関数彷徨う。",
    "警告の雲、静かに流れる。",
    "伝説のバージョン、今ここに蘇る。",
    "未来のモジュール、静かに誕生を待つ。"
]

HISTORY = []


def generate_scroll():
    intro = random.choice(SCROLL_INTRO)
    outro = random.choice(SCROLL_OUTRO)
    n_lines = random.randint(2, 4)
    lines = random.sample(SCROLL_LINES, n_lines)
    scroll = [intro] + lines + [outro]
    return "\n".join(scroll)


def show_scroll():
    scroll = generate_scroll()
    print(scroll)
    HISTORY.append({
        "timestamp": datetime.now().isoformat(),
        "content": scroll
    })


def log_scroll():
    scroll = generate_scroll()
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ancient_scroll.log", "a", encoding="utf-8") as f:
        f.write(f"[{ts}]\n{scroll}\n\n")
    print(scroll)
    HISTORY.append({
        "timestamp": datetime.now().isoformat(),
        "content": scroll
    })


def list_history():
    if not HISTORY:
        print("まだ巻物通知は表示されていません。")
        return
    for idx, entry in enumerate(HISTORY, 1):
        print(f"[{idx}] {entry['timestamp']}\n{entry['content']}\n")


def summary():
    print(f"これまでに{len(HISTORY)}件の巻物通知が生成されました。")
    if HISTORY:
        print("最新の通知:")
        print(HISTORY[-1]['content'])
    else:
        print("まだ通知はありません。")


def random_wait_and_alert(min_sec=10, max_sec=60):
    wait = random.randint(min_sec, max_sec)
    time.sleep(wait)
    show_scroll()


def main():
    parser = argparse.ArgumentParser(description="謎のOS公式・古文書巻物通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_show = subparsers.add_parser("show", help="今すぐ巻物通知を表示する")
    parser_log = subparsers.add_parser("log", help="巻物通知を生成しログファイルに記録する")
    parser_list = subparsers.add_parser("list", help="このセッションで表示した巻物通知一覧を表示")
    parser_summary = subparsers.add_parser("summary", help="通知の件数や最新内容を表示")
    parser_random = subparsers.add_parser("random", help="ランダムなタイミングで巻物通知を表示する (10-60秒待機)")

    args = parser.parse_args()
    if args.command == "show":
        show_scroll()
    elif args.command == "log":
        log_scroll()
    elif args.command == "list":
        list_history()
    elif args.command == "summary":
        summary()
    elif args.command == "random":
        random_wait_and_alert()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
