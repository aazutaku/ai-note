import argparse
import random
import sys
import time
from typing import List

# バトル実況のテンプレート
BATTLE_EVENTS = [
    "バグ魔王の逆襲！勇者、パッチの剣を抜く！",
    "勇者、デバッグの呪文を唱えた！バグ魔王が混乱した！",
    "バグ魔王、クラッシュの闇を放つ！勇者が耐えた！",
    "勇者、リファクタリングの光でバグ魔王を照らす！",
    "バグ魔王が無限ループ攻撃！勇者、冷静にbreak！",
    "勇者、最終パッチを投入！バグ魔王が動揺している！",
    "バグ魔王、レガシーコードの罠を仕掛ける！",
    "勇者、テストケースの嵐！バグ魔王がひるんだ！",
    "バグ魔王、未定義動作で反撃！勇者が回避！",
    "勇者、CI/CDの力で連続攻撃！"
]

VICTORY_MESSAGES = [
    "勇者の勝利！伝説のバグ魔王を討伐！",
    "アップデート勇者がバグ魔王を完全修正！",
    "バグ魔王、ついにバグトラッカーに封印される！"
]

DEFEAT_MESSAGES = [
    "バグ魔王の勝利！アップデート勇者は全滅した…",
    "勇者、バグの嵐に飲まれ力尽きた…",
    "伝説のバグ魔王、システムを支配！全滅…"
]

INTRO_MESSAGES = [
    "[ソフトウェアアップデート開始]",
    "勇者アップデートが伝説のバグ魔王に挑む！"
]

END_MESSAGES = [
    "[アップデート完了]",
    "[アップデート失敗]"
]

PROGRESS_STEPS = [12, 23, 35, 47, 58, 66, 78, 89, 100]


def print_battle_sequence(verbose: bool = False):
    print(random.choice(INTRO_MESSAGES))
    print(random.choice(INTRO_MESSAGES[1:]))
    last_event = None
    for idx, progress in enumerate(PROGRESS_STEPS):
        # ランダムな実況イベント
        if progress < 100:
            event = random.choice(BATTLE_EVENTS)
            # 直前と同じ実況を避ける
            while event == last_event:
                event = random.choice(BATTLE_EVENTS)
            last_event = event
            print(f"進捗: {progress}% - {event}")
            if verbose:
                time.sleep(0.5 + random.uniform(0, 0.7))
        else:
            # 勝敗を決定
            win = random.choice([True, False])
            if win:
                print(f"進捗: 100% - {random.choice(VICTORY_MESSAGES)}")
                print(END_MESSAGES[0])
            else:
                print(f"進捗: 100% - {random.choice(DEFEAT_MESSAGES)}")
                print(END_MESSAGES[1])
            if verbose:
                time.sleep(0.8)


def list_events():
    print("--- バトル実況イベント一覧 ---")
    for e in BATTLE_EVENTS:
        print(f"- {e}")
    print("\n--- 勝利メッセージ ---")
    for v in VICTORY_MESSAGES:
        print(f"- {v}")
    print("\n--- 敗北メッセージ ---")
    for d in DEFEAT_MESSAGES:
        print(f"- {d}")


def summary():
    print("random-os-fake-software-update-boss-fight Skill 概要:")
    print("- OSアップデート風の進捗バーをRPGバトル実況に変換")
    print("- バトル展開やセリフは毎回ランダム")
    print("- 勝敗もランダムで決定")
    print("- 明示/暗黙トリガー両対応")
    print("- 実際のアップデートは行われません")


def main():
    parser = argparse.ArgumentParser(
        description="OSソフトウェアアップデート vs バグ魔王 RPGバトル実況スクリプト"
    )
    subparsers = parser.add_subparsers(dest='command')

    # battleコマンド
    parser_battle = subparsers.add_parser('battle', help='RPGバトル実況を開始')
    parser_battle.add_argument('--verbose', action='store_true', help='進行をゆっくり表示')

    # listコマンド
    parser_list = subparsers.add_parser('list', help='実況/勝敗メッセージ一覧を表示')

    # summaryコマンド
    parser_summary = subparsers.add_parser('summary', help='Skillの概要を表示')

    args = parser.parse_args()

    if args.command == 'battle':
        print_battle_sequence(verbose=args.verbose)
    elif args.command == 'list':
        list_events()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
