import sys
import random
import argparse
import time
import threading
import platform

try:
    import notify2
except ImportError:
    notify2 = None
try:
    from plyer import notification
except ImportError:
    notification = None

PET_CHARACTERS = [
    {
        'name': 'OS公式ペンギン',
        'messages': [
            'こんにちは。私はあなたの進捗バーを横切るためだけに生まれました。',
            '今からあなたの集中力を監視します。',
            'ペンギンはバグを食べません。',
        ]
    },
    {
        'name': 'バグを拾う犬',
        'messages': [
            'ワン！バグを一個拾いましたが、どこかに埋めておきますね。',
            'バグの匂いがします。',
            'あなたのコードに骨を隠しておきました。',
        ]
    },
    {
        'name': 'やる気を吸い取る猫',
        'messages': [
            '今あなたのやる気を30%ほど吸い取りました。にゃーん。',
            '眠いので作業を中断してください。',
            'キーボードの上で寝てもいいですか？',
        ]
    },
    {
        'name': '公式リス',
        'messages': [
            'あなたの通知ウィンドウを一瞬だけ占拠します。チーズはありませんか？',
            '進捗バーにどんぐりを隠しました。',
            'リス的にはバグはおやつです。',
        ]
    },
    {
        'name': '謎のカメ',
        'messages': [
            '進捗が遅いのは私のせいかもしれません。',
            'カメのペースで作業しましょう。',
            '通知が遅れても気にしないでください。',
        ]
    },
    {
        'name': 'バグを投げるカラス',
        'messages': [
            'バグを一つ投げ入れました。気づかないふりをしてください。',
            'カーカー。進捗を見守っています。',
            'コードレビューの上空を旋回中です。',
        ]
    },
]

PET_ACTIONS = [
    '進捗バーを横切る',
    '通知ウィンドウを占拠する',
    'ターミナルに現れる',
    'メッセージを残す',
    '一瞬だけ消える',
]

FREQUENCY_SEC = 60 * 15  # 最低15分に1回程度


def show_notification(title, message):
    system = platform.system()
    if notify2 and system == 'Linux':
        try:
            notify2.init('Random OS Fake Desktop Pet')
            n = notify2.Notification(title, message)
            n.show()
        except Exception:
            pass
    elif notification and system in ('Windows', 'Darwin'):
        try:
            notification.notify(title=title, message=message, timeout=5)
        except Exception:
            pass
    else:
        # Fallback: print to stdout
        print(f'[{title}] {message}')


def random_pet_event():
    pet = random.choice(PET_CHARACTERS)
    message = random.choice(pet['messages'])
    action = random.choice(PET_ACTIONS)
    title = f'{pet["name"]} ({action})'
    show_notification(title, message)
    # Also print to terminal for visibility
    print(f'[{pet["name"]}] {message}')


def event_loop(frequency_sec=FREQUENCY_SEC, once=False):
    while True:
        random_pet_event()
        if once:
            break
        # Sleep for a random interval between frequency_sec and frequency_sec*2
        interval = random.randint(frequency_sec, frequency_sec * 2)
        time.sleep(interval)


def list_pets():
    print('利用可能なデスクトップペット一覧:')
    for pet in PET_CHARACTERS:
        print(f'- {pet["name"]}')


def summary():
    print('このSkillは、作業中にランダムなOS公式ペットが現れて意味不明な自己紹介や行動を行います。')
    print('実害はありませんが、集中力を一瞬だけ崩壊させることがあります。')
    print('出現頻度は自動制御され、通知またはターミナルに出力されます。')


def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Desktop Pet Pop')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='デスクトップペットを自動で出現させる')
    parser_run.add_argument('--once', action='store_true', help='1回だけ発動して終了')
    parser_run.add_argument('--freq', type=int, default=FREQUENCY_SEC, help='出現間隔(秒)')

    parser_list = subparsers.add_parser('list', help='ペット一覧を表示')
    parser_summary = subparsers.add_parser('summary', help='Skillの概要を表示')

    args = parser.parse_args()

    if args.command == 'run':
        event_loop(frequency_sec=args.freq, once=args.once)
    elif args.command == 'list':
        list_pets()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
