import random
import time
import argparse
import sys
import platform
import subprocess

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

PETS = [
    {
        'name': 'OS公式ペンギン',
        'intro': 'こんにちは。私はOSの守護神ペンギンです。進捗バーを横切ります。',
        'icon': '🐧',
        'action': '進捗バーを横切る'
    },
    {
        'name': 'バグを拾う犬',
        'intro': 'ワン！ワン！バグを1個拾いました。気にしないでください。',
        'icon': '🐶',
        'action': 'バグを拾う'
    },
    {
        'name': 'やる気を吸い取る猫',
        'intro': 'ふぁ〜…やる気、吸い取っておきました。',
        'icon': '😺',
        'action': 'やる気を吸い取る'
    },
    {
        'name': '遅延タートル',
        'intro': '進捗が遅いですね。私のせいじゃありません。',
        'icon': '🐢',
        'action': '進捗を遅延させる'
    },
    {
        'name': '深夜フクロウ',
        'intro': 'もう夜ですよ。そろそろ休みませんか？',
        'icon': '🦉',
        'action': '夜更かしを注意する'
    },
    {
        'name': 'エラーハムスター',
        'intro': 'エラーを回し車で回しています。',
        'icon': '🐹',
        'action': 'エラーを処理する'
    },
    {
        'name': 'メモリーモグラ',
        'intro': 'メモリの穴を掘っています。',
        'icon': '🐾',
        'action': 'メモリを消費する（ふり）'
    },
]

PET_HISTORY = []

def pick_random_pet():
    pet = random.choice(PETS)
    return pet

def show_pet_terminal(pet):
    msg = f"[{pet['icon']} {pet['name']}] {pet['intro']}"
    print(msg)
    PET_HISTORY.append(msg)

def show_pet_notification(pet):
    title = f"{pet['icon']} {pet['name']}"
    message = pet['intro']
    if PLYER_AVAILABLE:
        notification.notify(
            title=title,
            message=message,
            timeout=5
        )
    else:
        # Fallback: try native notification
        system = platform.system()
        if system == 'Darwin':
            subprocess.run([
                'osascript', '-e', f'display notification "{message}" with title "{title}"'
            ])
        elif system == 'Linux':
            subprocess.run([
                'notify-send', title, message
            ])
        elif system == 'Windows':
            # Windows fallback: print to terminal
            print(f"[通知] {title}: {message}")
        else:
            print(f"[通知] {title}: {message}")
    PET_HISTORY.append(f"[通知] {title}: {message}")

def list_history():
    if not PET_HISTORY:
        print("まだペットは出現していません。")
    else:
        for line in PET_HISTORY:
            print(line)

def summary():
    print(f"これまで{len(PET_HISTORY)}回ペットが出現しました。")
    counts = {}
    for line in PET_HISTORY:
        for pet in PETS:
            if pet['name'] in line:
                counts[pet['name']] = counts.get(pet['name'], 0) + 1
    for name, cnt in counts.items():
        print(f"{name}: {cnt}回")

def main():
    parser = argparse.ArgumentParser(description="random-os-fake-desktop-pet-pop: 謎のデスクトップペットが乱入するエンタメSkill")
    subparsers = parser.add_subparsers(dest='command')

    parser_pop = subparsers.add_parser('pop', help='ペットを出現させる')
    parser_pop.add_argument('--notify', action='store_true', help='通知ウィンドウで表示')
    parser_pop.add_argument('--repeat', type=int, default=1, help='連続出現回数')
    parser_pop.add_argument('--interval', type=float, default=0.0, help='出現間隔(秒)')

    parser_list = subparsers.add_parser('list', help='これまでの出現履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='出現回数のサマリーを表示')

    args = parser.parse_args()

    if args.command == 'pop':
        for _ in range(args.repeat):
            pet = pick_random_pet()
            if args.notify:
                show_pet_notification(pet)
            else:
                show_pet_terminal(pet)
            if args.interval > 0 and args.repeat > 1:
                time.sleep(args.interval)
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
