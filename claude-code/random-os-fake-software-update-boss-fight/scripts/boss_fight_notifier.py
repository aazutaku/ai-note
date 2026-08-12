import random
import time
import sys
import argparse
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

BATTLE_EVENTS = [
    ("勇者『パッチの剣』を抜いた！", 10, 20),
    ("バグ魔王『例外の嵐』反撃！", 15, 30),
    ("勇者『デバッグ魔法』発動！", 20, 40),
    ("バグ魔王『無限ループの呪い』！", 10, 20),
    ("勇者『アップデートの盾』で防御！", 5, 15),
    ("バグ魔王『レガシーコードの罠』！", 10, 25),
    ("勇者『ホットフィックス斬り』！", 15, 30),
    ("バグ魔王『未対応OS攻撃』！", 5, 20),
]

VICTORY_MESSAGES = [
    "勇者の勝利！アップデート完了！",
    "バグ魔王を討伐！システムは安全です。",
    "アップデート勇者が伝説を刻んだ！",
]
DEFEAT_MESSAGES = [
    "バグ魔王の逆襲！全滅…アップデート失敗。",
    "勇者は力尽きた…バグ魔王の勝利。",
    "バグ魔王がシステムを支配した…",
]

INTRO_MESSAGES = [
    "OSアップデート勇者が伝説のバグ魔王に挑む！",
    "アップデート勇者、バグ魔王の城へ突入！",
    "伝説のバグ魔王が復活…勇者が立ち向かう！",
]

PROGRESS_BAR_LENGTH = 40

class BattleState:
    def __init__(self):
        self.progress = 0
        self.battle_log = []
        self.victory = None

    def add_event(self, msg, delta):
        self.progress = min(100, self.progress + delta)
        self.battle_log.append((msg, self.progress))

    def is_finished(self):
        return self.progress >= 100

    def decide_outcome(self):
        self.victory = random.choice([True, False])


def send_notification(title, message):
    if PLYER_AVAILABLE:
        notification.notify(title=title, message=message, app_name="BossFightSkill", timeout=3)
    else:
        print(f"[通知] {title}: {message}")


def print_progress_bar(progress):
    filled = int(PROGRESS_BAR_LENGTH * progress // 100)
    bar = '█' * filled + '-' * (PROGRESS_BAR_LENGTH - filled)
    print(f"[進捗] |{bar}| {progress}%")


def run_boss_fight(verbose=False, delay=1.0):
    state = BattleState()
    intro = random.choice(INTRO_MESSAGES)
    send_notification("バトル開始", intro)
    print(f"[通知] {intro}")
    time.sleep(delay)
    while not state.is_finished():
        event, min_delta, max_delta = random.choice(BATTLE_EVENTS)
        delta = random.randint(min_delta, max_delta)
        state.add_event(event, delta)
        if verbose:
            print_progress_bar(state.progress)
        print(f"[進捗] {event}({state.progress}%)")
        time.sleep(delay)
    state.decide_outcome()
    if state.victory:
        msg = random.choice(VICTORY_MESSAGES)
    else:
        msg = random.choice(DEFEAT_MESSAGES)
    send_notification("バトル結果", msg)
    print(f"[通知] {msg}")
    return state


def list_battle_templates():
    print("# イベントテンプレート一覧：")
    for event, min_d, max_d in BATTLE_EVENTS:
        print(f"- {event} (+{min_d}-{max_d}%)")


def main():
    parser = argparse.ArgumentParser(description="謎のOSソフトウェアアップデート vs バグ魔王バトル実況スクリプト")
    subparsers = parser.add_subparsers(dest='command')

    run_parser = subparsers.add_parser('run', help='バトルを開始')
    run_parser.add_argument('--verbose', action='store_true', help='進捗バーを表示')
    run_parser.add_argument('--delay', type=float, default=1.0, help='イベント間の待ち秒数')

    list_parser = subparsers.add_parser('list', help='バトルイベントテンプレート一覧を表示')

    args = parser.parse_args()

    if args.command == 'run':
        run_boss_fight(verbose=args.verbose, delay=args.delay)
    elif args.command == 'list':
        list_battle_templates()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
