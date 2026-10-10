import random
import sys
import argparse
import platform
import subprocess
import time
from typing import List

# 勅令テンプレート集
DECREE_TEMPLATES = [
    "皇帝より勅令：本日より{item}の使用を禁ず。",
    "御前会議：{item}の叛逆を鎮圧せよ。",
    "大勅令：全ての{item}に{condition}を含めよ。",
    "禁令：{item}の乱用を厳しく取り締まる。",
    "御触書：本日、{item}は沈黙を守るべし。",
    "皇帝の思し召し：{item}は一日一回に限る。",
    "勅命：{item}に背く者は{punishment}に処す。",
    "大号令：{item}の儀式を今すぐ執り行え。",
    "布告：{item}の名の下に平和を誓え。",
    "密命：{item}の秘密を守り抜け。"
]

ITEMS = [
    "CapsLockキー",
    "スペースキー",
    "Altキー",
    "ターミナル",
    "スクリーンショット",
    "ファイル名",
    "コマンド履歴",
    "マウスカーソル",
    "USBメモリ",
    "ログインパスワード"
]

CONDITIONS = [
    "母音",
    "数字",
    "記号",
    "皇帝の紋章",
    "秘密の呪文",
    "日付",
    "空白",
    "大文字",
    "小文字"
]

PUNISHMENTS = [
    "深き沈黙",
    "再起動の刑",
    "ログアウトの儀",
    "無限待機",
    "自省の時間",
    "設定リセット",
    "バックスペース地獄"
]

# 通知を表示する関数
def notify(title: str, message: str):
    system = platform.system()
    try:
        if system == 'Darwin':
            subprocess.run([
                'osascript',
                '-e', f'display notification "{message}" with title "{title}"'
            ], check=True)
        elif system == 'Linux':
            subprocess.run([
                'notify-send', title, message], check=True)
        elif system == 'Windows':
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=5)
            except ImportError:
                print(f"[通知] {title}: {message}")
        else:
            print(f"[通知] {title}: {message}")
    except Exception as e:
        print(f"[通知失敗] {title}: {message} ({e})")

# 勅令文生成
def generate_decree() -> str:
    template = random.choice(DECREE_TEMPLATES)
    item = random.choice(ITEMS)
    condition = random.choice(CONDITIONS)
    punishment = random.choice(PUNISHMENTS)
    return template.format(item=item, condition=condition, punishment=punishment)

# 一覧表示
def list_decrees(n: int = 10) -> List[str]:
    decrees = []
    for _ in range(n):
        decrees.append(generate_decree())
    return decrees

# サマリー
def summary():
    print("--- 皇帝勅令 Skill サマリー ---")
    print(f"テンプレート数: {len(DECREE_TEMPLATES)}")
    print(f"対象項目数: {len(ITEMS)}")
    print(f"条件数: {len(CONDITIONS)}")
    print(f"罰則数: {len(PUNISHMENTS)}")
    print("出力例:")
    for decree in list_decrees(3):
        print(f"  {decree}")

# メイン処理
def main():
    parser = argparse.ArgumentParser(description='古代皇帝の勅令通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    # log: 1回だけ勅令を発する
    parser_log = subparsers.add_parser('log', help='ランダムな勅令を1つ通知')

    # list: n個の勅令を生成
    parser_list = subparsers.add_parser('list', help='ランダムな勅令を複数表示')
    parser_list.add_argument('-n', type=int, default=5, help='生成する勅令の数')

    # summary: Skillのサマリーを表示
    parser_summary = subparsers.add_parser('summary', help='Skillのサマリーを表示')

    # loop: 一定間隔で勅令を発する
    parser_loop = subparsers.add_parser('loop', help='定期的に勅令を通知')
    parser_loop.add_argument('--interval', type=int, default=60, help='通知間隔(秒)')
    parser_loop.add_argument('--count', type=int, default=5, help='通知回数')

    args = parser.parse_args()

    if args.command == 'log':
        decree = generate_decree()
        notify('皇帝勅令', decree)
        print(decree)
    elif args.command == 'list':
        decrees = list_decrees(args.n)
        for d in decrees:
            print(d)
    elif args.command == 'summary':
        summary()
    elif args.command == 'loop':
        for i in range(args.count):
            decree = generate_decree()
            notify('皇帝勅令', decree)
            print(f"[{i+1}/{args.count}] {decree}")
            if i < args.count - 1:
                time.sleep(args.interval)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
