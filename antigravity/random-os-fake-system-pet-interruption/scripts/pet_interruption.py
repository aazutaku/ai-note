import sys
import random
import time
import argparse
import threading
import platform

try:
    from plyer import notification
except ImportError:
    notification = None

PET_EVENTS = [
    'OS公式ペット「ねこまる」が画面を横切りました。',
    '仮想猫がマウスカーソルを追いかけています。',
    'デジタル柴犬がファイル「report.docx」の上で昼寝中です。',
    'OSペット「うさぎん」がタスクバーでジャンプしています。',
    'ペンギンが端末ウィンドウに登場しました。',
    'バーチャルハムスターが通知領域でおやつを食べています。',
    'デジタルカメがゆっくりと画面下部を移動中です。',
    'OSペット「インコ」がウィンドウの上で羽ばたいています。',
    '仮想柴犬がエディタのカーソルを追いかけています。',
    'デジタルねずみがファイルリストを駆け抜けました。',
]

KEYWORDS = ['ペット', '猫', '柴犬', '癒し', '犬', 'うさぎ', 'ペンギン', 'ハムスター', 'カメ', 'インコ', 'ねずみ']

DEFAULT_INTERVAL = 600  # 10分
RANDOMNESS = (120, 480)  # 2分～8分のランダム追加

class PetInterruption:
    def __init__(self, interval=DEFAULT_INTERVAL):
        self.interval = interval
        self.last_event = 0
        self.running = False
        self.lock = threading.Lock()

    def _notify(self, message):
        if notification:
            notification.notify(
                title='OSペット乱入イベント',
                message=message,
                timeout=8
            )
        else:
            print(f'[通知] {message}')

    def random_event(self):
        event = random.choice(PET_EVENTS)
        self._notify(event)
        self.last_event = time.time()

    def keyword_match(self, text):
        for kw in KEYWORDS:
            if kw in text:
                return True
        return False

    def monitor_keywords(self, logfile, poll=5):
        """監視対象のログファイルからキーワードを検出"""
        last_pos = 0
        while self.running:
            try:
                with open(logfile, 'r', encoding='utf-8') as f:
                    f.seek(last_pos)
                    lines = f.readlines()
                    if lines:
                        for line in lines:
                            if self.keyword_match(line):
                                self.random_event()
                        last_pos = f.tell()
            except Exception:
                pass
            time.sleep(poll)

    def timer_loop(self):
        while self.running:
            now = time.time()
            if now - self.last_event > self.interval + random.randint(*RANDOMNESS):
                self.random_event()
            time.sleep(30)

    def start(self, logfile=None):
        self.running = True
        threads = []
        if logfile:
            t = threading.Thread(target=self.monitor_keywords, args=(logfile,))
            t.daemon = True
            threads.append(t)
            t.start()
        timer_thread = threading.Thread(target=self.timer_loop)
        timer_thread.daemon = True
        threads.append(timer_thread)
        timer_thread.start()
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.running = False
            print('終了します')

    def trigger_once(self):
        self.random_event()


def main():
    parser = argparse.ArgumentParser(description='OSペット乱入イベント発生スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_start = subparsers.add_parser('start', help='バックグラウンドで自動発動')
    parser_start.add_argument('--interval', type=int, default=DEFAULT_INTERVAL, help='最小発動間隔(秒)')
    parser_start.add_argument('--logfile', type=str, help='キーワード監視用ログファイルパス')

    parser_once = subparsers.add_parser('once', help='1回だけ乱入イベントを発生')

    parser_list = subparsers.add_parser('list', help='ペット乱入イベント内容一覧')

    args = parser.parse_args()
    pet = PetInterruption(interval=args.interval if hasattr(args, 'interval') else DEFAULT_INTERVAL)

    if args.command == 'start':
        pet.start(logfile=args.logfile)
    elif args.command == 'once':
        pet.trigger_once()
    elif args.command == 'list':
        for i, event in enumerate(PET_EVENTS, 1):
            print(f'{i}. {event}')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
