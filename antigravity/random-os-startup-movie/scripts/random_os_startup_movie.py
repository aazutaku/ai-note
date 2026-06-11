import sys
import time
import random
import argparse

OS_NAMES = [
    "Antigravity 3000 Ultimate Edition",
    "Windows 11.5 Quantum",
    "Codex Limited Edition OS",
    "QuantumOS X Hyperdrive",
    "Nebula Linux 9.9",
    "SingularityOS Pro",
    "AI DreamOS 42",
    "Bitfield OS Mirage",
    "HyperloopOS Next",
    "MetaKernel Infinity"
]

PROGRESS_MESSAGES = [
    "ビットを配置中...",
    "AIを目覚めさせています...",
    "量子ビットの再配置中...",
    "自己修復モジュールを展開中...",
    "意味不明なプロセスを初期化中...",
    "宇宙的セキュリティを検証中...",
    "全銀河ネットワークとの同期を確認...",
    "次元間インターフェースを起動中...",
    "エントロピーを最適化中...",
    "パラレルワールドアクセス権を取得中..."
]

FINAL_MESSAGES = [
    "起動完了。ようこそ、未来へ。",
    "起動に成功しました。",
    "あなたのセッションは今、始まります。",
    "全システム正常。作業開始可能です。",
    "Welcome to the Impossible."
]

PROGRESS_BAR_STYLES = [
    ("■", "□"),
    ("█", "░"),
    ("#", "-"),
    ("●", "○")
]


def random_os_name():
    return random.choice(OS_NAMES)

def random_progress_style():
    return random.choice(PROGRESS_BAR_STYLES)

def random_progress_messages(n):
    return random.sample(PROGRESS_MESSAGES, k=n)

def random_final_message():
    return random.choice(FINAL_MESSAGES)

def print_progress_bar(percent, filled, empty, length=10):
    filled_len = int(percent * length)
    empty_len = length - filled_len
    bar = filled * filled_len + empty * empty_len
    print(f"{bar} ({int(percent*100)}%)")

def animate_startup():
    os_name = random_os_name()
    style = random_progress_style()
    n_msgs = random.randint(3, 5)
    messages = random_progress_messages(n_msgs)
    final_msg = random_final_message()
    print(f"[{os_name} 起動中...]")
    steps = n_msgs + 1
    for i, msg in enumerate(messages):
        percent = (i+1)/steps
        print_progress_bar(percent, style[0], style[1])
        print(msg)
        time.sleep(random.uniform(0.3, 0.8))
    print_progress_bar(1.0, style[0], style[1])
    print(final_msg)

# CLIサブコマンド

def main():
    parser = argparse.ArgumentParser(description='random-os-startup-movie: 毎回違う架空OS起動画面を演出')
    subparsers = parser.add_subparsers(dest='command')

    show_parser = subparsers.add_parser('show', help='架空OS起動画面を1回表示')
    batch_parser = subparsers.add_parser('batch', help='指定回数だけ連続表示')
    batch_parser.add_argument('-n', '--number', type=int, default=3, help='表示回数')
    list_parser = subparsers.add_parser('list', help='利用可能なOS名や進捗メッセージ一覧を表示')

    args = parser.parse_args()
    if args.command == 'show' or args.command is None:
        try:
            animate_startup()
        except KeyboardInterrupt:
            print("\nキャンセルされました。")
    elif args.command == 'batch':
        try:
            for _ in range(args.number):
                animate_startup()
                print("\n---\n")
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nキャンセルされました。")
    elif args.command == 'list':
        print("利用可能なOS名:")
        for name in OS_NAMES:
            print(f"  - {name}")
        print("\n進捗メッセージ:")
        for msg in PROGRESS_MESSAGES:
            print(f"  - {msg}")
        print("\n終了メッセージ:")
        for msg in FINAL_MESSAGES:
            print(f"  - {msg}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
