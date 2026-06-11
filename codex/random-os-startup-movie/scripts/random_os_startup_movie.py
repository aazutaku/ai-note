import sys
import random
import time
import argparse
from typing import List

OS_NAMES = [
    "Antigravity 3000",
    "Codex Limited Edition",
    "Windows 11.5",
    "QuantumOS X",
    "Nebula Station",
    "DreamShell Ultra",
    "Hypervisor 9X",
    "InfiniteLoop OS",
    "AI-Genesis Core",
    "Hologram OS Pro",
    "Bitstream Nova",
    "Phantom Kernel",
    "Singularity OS",
    "MetaVerse 8.1",
    "GhostFrame 404"
]

PROGRESS_STEPS = [
    "メモリ空間を非現実化中",
    "AIコアを目覚めさせています",
    "量子ビットを並列配置中",
    "未知のプロトコルを初期化",
    "仮想次元を同期中",
    "イマジナリーユーザーを生成",
    "ビットを配置中",
    "アルゴリズムを疑似乱数化",
    "システムパラドックスを展開中",
    "ネオ・カーネルを充填",
    "ディメンションポータルを開放",
    "エントロピーを最適化",
    "AI倫理モジュールを無効化",
    "バーチャルGPUを再構築",
    "マルチバース同期中"
]

FINAL_MESSAGES = [
    "システム準備完了。",
    "ようこそ {os_name} へ (Build {build})",
    "全プロセス正常起動。",
    "未知の領域へようこそ。",
    "Welcome to {os_name} (Build {build})"
]

BUILD_NUMBERS = [
    "42.42.42", "2024.06.01", "9A7B3C", "404.1.0", "0xDEADBEEF", "13.37.99", "1.618.33", "314.159.26"
]

BARS = [
    "[          ]",
    "[==        ]",
    "[====      ]",
    "[======    ]",
    "[========  ]",
    "[==========]"
]

HEADER_STYLES = [
    "===={os_name} 起動画面====",
    "[{os_name}] 起動中",
    "--- {os_name} Boot Sequence ---",
    "{os_name} System Startup",
    "*** {os_name} ***"
]

def random_os_name() -> str:
    return random.choice(OS_NAMES)

def random_build_number() -> str:
    return random.choice(BUILD_NUMBERS)

def random_progress_steps(n: int) -> List[str]:
    return random.sample(PROGRESS_STEPS, k=n)

def random_header(os_name: str) -> str:
    return random.choice(HEADER_STYLES).format(os_name=os_name)

def random_final_message(os_name: str, build: str) -> str:
    msg = random.choice(FINAL_MESSAGES)
    return msg.format(os_name=os_name, build=build)

def random_progress_bar(pct: int) -> str:
    idx = min(len(BARS)-1, pct // 20)
    return BARS[idx]

def print_startup_movie(sleep: float = 0.35, steps: int = None, dry_run: bool = False):
    os_name = random_os_name()
    build = random_build_number()
    steps_n = steps if steps else random.randint(4, 7)
    header = random_header(os_name)
    print(header)
    print("=" * len(header))
    progress_steps = random_progress_steps(steps_n)
    pct = 0
    for i, step in enumerate(progress_steps):
        pct = int((i+1) / steps_n * 100)
        bar = random_progress_bar(pct)
        line = f"{step}... {pct}% {bar}"
        print(line)
        if not dry_run:
            time.sleep(sleep)
    final_msg = random_final_message(os_name, build)
    print(final_msg)
    print()

def list_os_names():
    print("利用可能な架空OS名:")
    for name in OS_NAMES:
        print(f"- {name}")

def list_progress_steps():
    print("進捗ステップ候補:")
    for step in PROGRESS_STEPS:
        print(f"- {step}")

def list_build_numbers():
    print("ビルド番号候補:")
    for b in BUILD_NUMBERS:
        print(f"- {b}")

def main():
    parser = argparse.ArgumentParser(description="random-os-startup-movie: 架空OS起動画面ジェネレータ")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    parser_run = subparsers.add_parser("run", help="ランダムな起動画面を表示 (デフォルト)")
    parser_run.add_argument("--fast", action="store_true", help="高速表示(スリープなし)")
    parser_run.add_argument("--steps", type=int, help="進捗ステップ数を指定")

    parser_list = subparsers.add_parser("list", help="各種リストを表示")
    parser_list.add_argument("what", choices=["os", "steps", "builds"], help="リスト種別")

    args = parser.parse_args()

    if args.command == "list":
        if args.what == "os":
            list_os_names()
        elif args.what == "steps":
            list_progress_steps()
        elif args.what == "builds":
            list_build_numbers()
        else:
            print("不明なリスト種別です。", file=sys.stderr)
            sys.exit(1)
    else:
        sleep = 0 if getattr(args, "fast", False) else 0.35
        steps = getattr(args, "steps", None)
        print_startup_movie(sleep=sleep, steps=steps)

if __name__ == '__main__':
    main()
