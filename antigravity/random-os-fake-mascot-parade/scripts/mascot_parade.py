import random
import sys
import time
import argparse
from threading import Thread, Event
from plyer import notification

MASCOTS = [
    {
        'name': 'カーネルくん',
        'lines': [
            'プロセス管理は心の整理から！',
            'カーネルパニックは突然に。',
            '今日もスケジューリング、がんばろう！',
            '割り込みは人生のスパイス。',
            'シグナルを見逃すな！',
        ]
    },
    {
        'name': 'メモリねずみ',
        'lines': [
            'バグ撲滅運動中。メモリリークにご用心！',
            'RAMの隅で応援してます。',
            'キャッシュクリアは心の洗濯。',
            'アドレス空間に夢を乗せて。',
            'スワップしすぎ注意！',
        ]
    },
    {
        'name': 'シェルパンダ',
        'lines': [
            '一服推奨。コマンド履歴も休ませよう。',
            'aliasで人生をショートカット。',
            'パイプでつながる友情。',
            'シェル芸はほどほどに。',
            'exitのタイミングは慎重に。',
        ]
    },
    {
        'name': 'デバイスタコ',
        'lines': [
            'USBを抜く前に、心の準備を！',
            'デバイスファイルは友達。',
            'マウント解除は慎重に。',
            'ドライバ更新、忘れずに。',
            'ポート番号は覚えておこう。',
        ]
    },
    {
        'name': 'スワップペンギン',
        'lines': [
            'スワップしすぎ注意！たまには休憩を。',
            'ディスクI/Oに愛を。',
            '仮想メモリで夢を見る。',
            'swapoffで現実に戻ろう。',
            'ページングは人生の波。',
        ]
    },
    {
        'name': 'プロンプトキツネ',
        'lines': [
            'PS1はおしゃれの基本。',
            'プロンプトが光るとき、道が開ける。',
            'コマンド補完は友情の証。',
            'Ctrl+Cでリセット！',
            'ヒストリーに学びあり。',
        ]
    },
    {
        'name': 'ログフクロウ',
        'lines': [
            'ログは真実を語る。',
            'tail -fで未来を見よう。',
            'syslogは友達。',
            'エラーログも人生の一部。',
            'grepで真実を発掘。',
        ]
    },
    {
        'name': 'パーミッションイヌ',
        'lines': [
            'chmodは慎重に。',
            'パーミッションは信頼の証。',
            'root権限、使いすぎ注意！',
            'chownで家族を増やそう。',
            'umaskで個性を守ろう。',
        ]
    },
]

INTERVALS = [
    (60, 180),   # 初回: 1-3分後
    (180, 600),  # 以降: 3-10分間隔
]

class MascotParade(Thread):
    def __init__(self, stop_event):
        super().__init__()
        self.stop_event = stop_event
        self.first = True

    def run(self):
        while not self.stop_event.is_set():
            interval = random.randint(*INTERVALS[0] if self.first else INTERVALS[1])
            self.first = False
            for _ in range(interval):
                if self.stop_event.is_set():
                    return
                time.sleep(1)
            self.send_random_notification()

    def send_random_notification(self):
        mascot = random.choice(MASCOTS)
        line = random.choice(mascot['lines'])
        title = mascot['name']
        message = f'「{line}」'
        try:
            notification.notify(
                title=title,
                message=message,
                app_name='OSマスコットパレード',
                timeout=7
            )
            print(f'[通知] {title}: {message}')
        except Exception as e:
            print(f'[通知失敗] {title}: {message} ({e})')


def parade_main(args):
    stop_event = Event()
    parade = MascotParade(stop_event)
    parade.daemon = True
    parade.start()
    print('OSマスコットパレード開始。Ctrl+Cで終了します。')
    try:
        while parade.is_alive():
            parade.join(1)
    except KeyboardInterrupt:
        print('終了処理中...')
        stop_event.set()
        parade.join()
        print('パレード終了。')


def sample_once(args):
    mascot = random.choice(MASCOTS)
    line = random.choice(mascot['lines'])
    title = mascot['name']
    message = f'「{line}」'
    try:
        notification.notify(
            title=title,
            message=message,
            app_name='OSマスコットパレード',
            timeout=7
        )
        print(f'[通知] {title}: {message}')
    except Exception as e:
        print(f'[通知失敗] {title}: {message} ({e})')


def list_mascots(args):
    print('--- 登場マスコット一覧 ---')
    for m in MASCOTS:
        print(f'- {m["name"]}')


def main():
    parser = argparse.ArgumentParser(description='謎のOSマスコット大行進 (通知ジョークSkill)')
    subparsers = parser.add_subparsers(dest='command')
    p_run = subparsers.add_parser('run', help='パレードを開始 (Ctrl+Cで終了)')
    p_once = subparsers.add_parser('once', help='1回だけ通知を表示')
    p_list = subparsers.add_parser('list', help='マスコット一覧を表示')
    args = parser.parse_args()
    if args.command == 'run' or args.command is None:
        parade_main(args)
    elif args.command == 'once':
        sample_once(args)
    elif args.command == 'list':
        list_mascots(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
