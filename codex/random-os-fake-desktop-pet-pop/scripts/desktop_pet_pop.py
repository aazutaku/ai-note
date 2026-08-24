import sys
import time
import random
import argparse
import threading
import platform
from typing import List, Dict, Callable

try:
    if platform.system() == 'Darwin':
        import subprocess
    elif platform.system() == 'Linux':
        import subprocess
    elif platform.system() == 'Windows':
        import win10toast
except ImportError:
    pass

# ペット定義
PETS = [
    {
        'name': 'OS公式ペンギン',
        'icon': '🐧',
        'actions': [
            'こんにちは！今日もバグを凍らせに来ました。',
            '進捗バーの上で滑ってみます。',
            '冷たい視線であなたを見つめている…',
            'ペンギン語でバグを追い払う！',
        ]
    },
    {
        'name': 'バグを拾う犬',
        'icon': '🐶',
        'actions': [
            '進捗バーの下に何か落ちてない？ワン！',
            'バグをくわえてどこかへ…',
            'あなたの足元でしっぽを振っている。',
            '通知ウィンドウを横切るワン！',
        ]
    },
    {
        'name': 'やる気を吸い取る猫',
        'icon': '🐱',
        'actions': [
            'ふぁ〜…やる気、いただきます。',
            'キーボードの上で寝始めた！',
            'あなたをじっと見つめている。',
            '進捗バーを横切って去っていく。',
        ]
    },
    {
        'name': '謎の鳥',
        'icon': '🐦',
        'actions': [
            'ピヨピヨ…（通知ウィンドウを横切る）',
            'バグをついばみに来たよ。',
            'どこからともなく飛来。',
            '進捗バーの上で羽ばたく。',
        ]
    },
    {
        'name': 'ゆっくりカメ',
        'icon': '🐢',
        'actions': [
            '進捗は急がなくてもいいんだよ…',
            'のろのろと画面端を移動中。',
            'バグを踏みつぶして進む。',
            'あなたの集中力を見守っている。',
        ]
    }
]

# 通知表示関数

def show_notification(title: str, message: str):
    sys_platform = platform.system()
    if sys_platform == 'Darwin':
        try:
            subprocess.run([
                'osascript', '-e', f'display notification "{message}" with title "{title}"'
            ], check=True)
        except Exception:
            print(f"[{title}] {message}")
    elif sys_platform == 'Linux':
        try:
            subprocess.run([
                'notify-send', title, message
            ], check=True)
        except Exception:
            print(f"[{title}] {message}")
    elif sys_platform == 'Windows':
        try:
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(title, message, duration=4)
        except Exception:
            print(f"[{title}] {message}")
    else:
        print(f"[{title}] {message}")

# ターミナル演出

def terminal_pet_pop(pet: Dict):
    lines = [
        f"[{pet['icon']} {pet['name']}] {random.choice(pet['actions'])}",
        "",
        "(数秒で消えます…)"
    ]
    for line in lines:
        print(line)
        time.sleep(0.5)
    # 擬似的に消す（スクロールで流す）
    for _ in range(len(lines)):
        print()
        time.sleep(0.2)

# ペット出現処理

def pop_pet(mode='auto', notify=True, terminal=True):
    pet = random.choice(PETS)
    action = random.choice(pet['actions'])
    title = f"{pet['icon']} {pet['name']}"
    if notify:
        show_notification(title, action)
    if terminal:
        terminal_pet_pop(pet)

# サブコマンド: pop/list/summary

def list_pets():
    print("=== ペット一覧 ===")
    for pet in PETS:
        print(f"{pet['icon']} {pet['name']}")
        for act in pet['actions']:
            print(f"  - {act}")
    print()

def summary():
    print("このSkillは、作業中にランダムでデスクトップペットが現れる癒し系・妨害系エンタメ演出を提供します。\n")
    print("ペット数:", len(PETS))
    print("出現アクション例:")
    for pet in PETS:
        print(f"- {pet['name']}: {pet['actions'][0]}")
    print()

# 頻度制御: 1分に1回以上は出現しない
_last_pop_time = 0
def can_pop():
    global _last_pop_time
    now = time.time()
    if now - _last_pop_time > 60:
        _last_pop_time = now
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description='random-os-fake-desktop-pet-pop')
    subparsers = parser.add_subparsers(dest='command')

    pop_parser = subparsers.add_parser('pop', help='ペットを即座に出現させる')
    pop_parser.add_argument('--no-notify', action='store_true', help='通知を出さない')
    pop_parser.add_argument('--no-terminal', action='store_true', help='ターミナル演出を出さない')

    list_parser = subparsers.add_parser('list', help='ペット一覧とアクションを表示')
    summary_parser = subparsers.add_parser('summary', help='Skill概要を表示')

    args = parser.parse_args()

    if args.command == 'pop':
        pop_pet(notify=not args.no_notify, terminal=not args.no_terminal)
    elif args.command == 'list':
        list_pets()
    elif args.command == 'summary':
        summary()
    else:
        # デフォルト: 頻度制御付きで自動発動
        if can_pop():
            pop_pet()
        else:
            print("(ペットはまだ出現しません。しばらく待ってください)")

if __name__ == '__main__':
    main()
