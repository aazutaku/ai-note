import argparse
import random
import time
import sys
import os
import threading
try:
    import notify2
except ImportError:
    notify2 = None

PET_EVENTS = [
    '{pet}がファイル「{file}」の上で昼寝を始めました。',
    '{pet}がマウスカーソルを追いかけています！',
    'OS公式{pet}が画面を横切りました。',
    '{pet}がウィンドウの隅で羽を休めています。',
    '{pet}がタスクバーでおやつを探しています。',
    '{pet}が通知領域で丸くなっています。',
    '{pet}が仮想デスクトップを移動しています。',
    '{pet}が設定画面で遊んでいます。',
    '{pet}がコマンド履歴を眺めています。',
    '{pet}がスクリーンショットを撮ろうとしています。',
]

PETS = [
    'デジタル柴犬',
    '仮想猫',
    'OS公式ペンギン',
    'デジタルインコ',
    'バーチャルハムスター',
    'サイバーうさぎ',
    'ピクセルリス',
    'デジタルカメ',
    'バーチャルフクロウ',
    '仮想フェレット'
]

FILES = [
    'report.docx',
    'main.py',
    'presentation.pptx',
    'budget.xlsx',
    'notes.txt',
    'README.md',
    'archive.zip',
    'photo.jpg',
    'tasks.csv',
    'music.mp3'
]

HISTORY_LOG = os.path.expanduser('~/.os_pet_interruptions.log')
COOLTIME_SEC = 600  # 10分


def random_event():
    pet = random.choice(PETS)
    file = random.choice(FILES)
    event = random.choice(PET_EVENTS)
    msg = event.format(pet=pet, file=file)
    return msg


def notify(msg):
    if notify2 is not None:
        try:
            notify2.init('OSペット通知')
            n = notify2.Notification('OSペット通知', msg)
            n.set_timeout(5000)
            n.show()
            return True
        except Exception:
            pass
    # Fallback: print to terminal
    print(f'[OSペット通知] {msg}')
    return False


def log_event(msg):
    ts = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(HISTORY_LOG, 'a', encoding='utf-8') as f:
        f.write(f'{ts}\t{msg}\n')


def list_events(limit=10):
    if not os.path.exists(HISTORY_LOG):
        print('まだイベント履歴がありません。')
        return
    with open(HISTORY_LOG, 'r', encoding='utf-8') as f:
        lines = f.readlines()[-limit:]
    for line in lines:
        print(line.strip())


def summary():
    if not os.path.exists(HISTORY_LOG):
        print('まだイベント履歴がありません。')
        return
    pet_count = {pet: 0 for pet in PETS}
    with open(HISTORY_LOG, 'r', encoding='utf-8') as f:
        for line in f:
            for pet in PETS:
                if pet in line:
                    pet_count[pet] += 1
    print('ペット別乱入回数:')
    for pet, count in pet_count.items():
        print(f'  {pet}: {count}回')


def can_trigger():
    if not os.path.exists(HISTORY_LOG):
        return True
    with open(HISTORY_LOG, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        if not lines:
            return True
        last = lines[-1]
        ts_str = last.split('\t')[0]
        try:
            last_time = time.mktime(time.strptime(ts_str, '%Y-%m-%d %H:%M:%S'))
            now = time.time()
            return (now - last_time) > COOLTIME_SEC
        except Exception:
            return True


def trigger_event():
    if not can_trigger():
        print('クールタイム中のため、まだ乱入できません。')
        return
    msg = random_event()
    notify(msg)
    log_event(msg)


def auto_mode(interval_min=20, stop_after=120):
    """interval_min: イベント間隔(分), stop_after: 最大稼働時間(分)"""
    start = time.time()
    while (time.time() - start) < stop_after * 60:
        sleep_time = random.randint(int(interval_min*0.5), int(interval_min*1.5)) * 60
        time.sleep(sleep_time)
        trigger_event()
    print('自動乱入モード終了')


def main():
    parser = argparse.ArgumentParser(description='random-os-fake-system-pet-interruption')
    subparsers = parser.add_subparsers(dest='command')

    parser_trigger = subparsers.add_parser('trigger', help='手動で乱入イベントを発生')
    parser_auto = subparsers.add_parser('auto', help='自動乱入モード')
    parser_auto.add_argument('--interval', type=int, default=20, help='イベント間隔(分)')
    parser_auto.add_argument('--duration', type=int, default=120, help='最大稼働時間(分)')
    parser_list = subparsers.add_parser('list', help='履歴を表示')
    parser_list.add_argument('--limit', type=int, default=10, help='表示件数')
    parser_summary = subparsers.add_parser('summary', help='ペット別乱入回数')

    args = parser.parse_args()

    if args.command == 'trigger':
        trigger_event()
    elif args.command == 'auto':
        auto_mode(interval_min=args.interval, stop_after=args.duration)
    elif args.command == 'list':
        list_events(limit=args.limit)
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
