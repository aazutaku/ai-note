import sys
import time
import random
import argparse

FAKE_MESSAGES = [
    "未知の言語パッチ適用中",
    "レガシーキーボード最適化中",
    "ファイルシステムの逆最適化中",
    "メモリの謎領域を拡張中",
    "進捗状況を再計算中",
    "未知のプロトコルを初期化中",
    "セキュリティホールを開放中",
    "タイムゾーンを無効化中",
    "仮想デバイスを物理化中",
    "カーネルパニックを模倣中",
    "レガシーAPIを最新化中",
    "無限ループの最適化中",
    "謎のバイナリを展開中",
    "メタデータを消去中",
    "OSの気分を変更中"
]

PROGRESS_GLITCHES = [
    (99, 88),  # 99%から逆戻り
    (42, 12),  # 42%から巻き戻し
    (75, 60),  # 75%からダウン
    (33, 25),  # 33%から逆行
]

MAX_STEPS = 20

def random_message():
    return random.choice(FAKE_MESSAGES)

def glitch_progress(progress):
    for from_p, to_p in PROGRESS_GLITCHES:
        if progress == from_p:
            return to_p
    return progress

def generate_progress_sequence():
    steps = []
    progress = 0
    used_glitches = set()
    while progress < 100:
        if progress < 90:
            step = random.randint(5, 20)
        else:
            step = random.randint(1, 3)
        next_progress = min(progress + step, 100)
        # 99%で止まる
        if next_progress > 99:
            next_progress = 99
        # グリッチ適用
        for from_p, to_p in PROGRESS_GLITCHES:
            if next_progress == from_p and from_p not in used_glitches:
                steps.append((from_p, random_message()))
                steps.append((to_p, "進捗が巻き戻りました..."))
                used_glitches.add(from_p)
                progress = to_p
                continue
        steps.append((next_progress, random_message()))
        progress = next_progress
        if progress == 99:
            # 99%で止まる
            break
    return steps

def show_progress_bar():
    sequence = generate_progress_sequence()
    for percent, msg in sequence:
        bar = '[' + '{:3d}%'.format(percent) + ']'
        print(f"{bar} {msg}...")
        # 99%で長く止まる
        if percent == 99:
            time.sleep(2.5)
        else:
            time.sleep(random.uniform(0.3, 1.1))

def list_messages():
    print("== ランダム進捗メッセージ一覧 ==")
    for m in FAKE_MESSAGES:
        print(f"- {m}")

def summary():
    print("random-os-fake-mysterious-update-progress: 謎の進捗バーを演出します。\n")
    print("主な特徴:")
    print("- 進捗内容は毎回ランダムかつ意味不明")
    print("- 進捗バーは途中で逆戻りしたり、99%で止まります")
    print("- 実際のOSやファイルには一切影響しません")
    print("- エンタメ・脱力系用途に最適")

def main():
    parser = argparse.ArgumentParser(description="謎のOSアップデート進捗バーを表示します")
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='謎の進捗バーを表示')
    parser_list = subparsers.add_parser('list', help='進捗メッセージ一覧')
    parser_summary = subparsers.add_parser('summary', help='Skill概要')

    args = parser.parse_args()

    if args.command == 'run' or args.command is None:
        try:
            show_progress_bar()
        except KeyboardInterrupt:
            print("\nアップデートが中断されました。現実世界には影響ありません。")
    elif args.command == 'list':
        list_messages()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
