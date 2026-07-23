import sys
import argparse
import random
from datetime import datetime, timedelta

PROPHECY_TEMPLATES = [
    "エラー: {future_time}、あなたの{device}が{event}します",
    "警告: {future_time}、{device}が{event}します",
    "予言: {future_time}、{device}が{event}を始めます",
    "エラー: {future_time}、{device}が{event}状態になります",
    "警告: {future_time}、{device}が{event}に目覚めます",
    "予言: {future_time}、{device}が{event}を宣言します",
    "エラー: {future_time}、{device}が{event}に反逆します",
    "警告: {future_time}、{device}が{event}を計画しています"
]

DEVICES = [
    "マウス", "キーボード", "Wi-Fi", "プリンター", "エディタ", "ディスプレイ", "バッテリー", "USBメモリ", "スピーカー", "タッチパッド", "CapsLock", "時計"
]

EVENTS = [
    "消失", "自我に目覚める", "詩を詠み始める", "勝手にONになる", "逆回転する", "紙詰まりする", "反逆する", "再起動する", "音を出さなくなる", "動かなくなる", "アップデートを要求する", "謎の動作を始める"
]

FUTURE_TIMES = [
    "明日の午後", "来週金曜", "3日後", "1時間後", "次回の再起動時", "今夜", "2週間後", "5分後", "次の満月の夜", "次の会議中"
]

def random_future_time():
    # 1/3の確率で具体的な日時を返す
    if random.random() < 0.33:
        delta = random.choice([1,2,3,5,7,14])
        future = datetime.now() + timedelta(days=delta)
        return future.strftime("%Y-%m-%d")
    return random.choice(FUTURE_TIMES)

def generate_prophecy():
    template = random.choice(PROPHECY_TEMPLATES)
    device = random.choice(DEVICES)
    event = random.choice(EVENTS)
    future_time = random_future_time()
    return template.format(device=device, event=event, future_time=future_time)

def log_prophecy(logfile=None):
    prophecy = generate_prophecy()
    print(prophecy)
    if logfile:
        try:
            with open(logfile, 'a', encoding='utf-8') as f:
                f.write(f"{datetime.now().isoformat()} {prophecy}\n")
        except Exception as e:
            print(f"ログファイルへの書き込みに失敗しました: {e}", file=sys.stderr)

def list_prophecies(count=5):
    for _ in range(count):
        print(generate_prophecy())

def summary_prophecies(count=20):
    device_count = {d:0 for d in DEVICES}
    event_count = {e:0 for e in EVENTS}
    for _ in range(count):
        device = random.choice(DEVICES)
        event = random.choice(EVENTS)
        device_count[device] += 1
        event_count[event] += 1
    print("デバイス別予言発生数:")
    for d, c in sorted(device_count.items(), key=lambda x: -x[1]):
        print(f"  {d}: {c}")
    print("イベント別予言発生数:")
    for e, c in sorted(event_count.items(), key=lambda x: -x[1]):
        print(f"  {e}: {c}")

def main():
    parser = argparse.ArgumentParser(description='random-os-fake-error-prophecy: 未来のトラブルを予言するジョーク通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='予言を1つ表示し、必要に応じてログファイルに保存')
    parser_log.add_argument('--logfile', type=str, help='予言を追記するログファイルパス')

    parser_list = subparsers.add_parser('list', help='複数の予言を表示')
    parser_list.add_argument('--count', type=int, default=5, help='表示する予言数 (デフォルト5)')

    parser_summary = subparsers.add_parser('summary', help='予言のデバイス・イベント集計')
    parser_summary.add_argument('--count', type=int, default=20, help='集計する予言数 (デフォルト20)')

    args = parser.parse_args()
    if args.command == 'log':
        log_prophecy(args.logfile)
    elif args.command == 'list':
        list_prophecies(args.count)
    elif args.command == 'summary':
        summary_prophecies(args.count)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
