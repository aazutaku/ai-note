import sys
import argparse
import random
import datetime
import textwrap

LEGENDARY_BOOT_SOUNDS = [
    '伝説のバグフィックス交響曲',
    '謎の時代劇風ジングル',
    '宇宙人襲来ブザー',
    '幻のサウンドトラック第零楽章',
    '超次元リカバリーオーバーチュア',
    '未確認エラーのファンファーレ',
    '古代OSの目覚めベル',
    '未来派システム警告チャイム',
    'バグの海のラプソディ',
    'メモリリークの夜明け',
    '暗黒モード起動の鐘',
    'シリコンバレー伝承の鼓動',
    '幻惑の再起動ソナタ',
    'サイバー忍者の目覚まし',
    '時空間デフラグメント音頭',
    '伝説のアップデート祝祭曲',
    '謎の未定義動作マーチ',
    '宇宙世紀OS起動の調べ',
    'メンテナンスの舞踏会',
    'バグ退散の祝詞',
    'システム神話序曲',
    '仮想空間の朝焼け',
    '再起動の神託',
    '禁断のレジストリ讃歌',
    'オーバーフローのセレナーデ',
    'カーネルパニックのワルツ',
    '未知との遭遇アラーム',
    '伝説のログインファンファーレ',
    'デバッグの祈り',
    '幻のクラッシュ協奏曲'
]

LOGO = """
=== OS起動音通知 ===
"""

HISTORY = []


def pick_random_boot_sound():
    return random.choice(LEGENDARY_BOOT_SOUNDS)


def display_notification(sound_name, timestamp=None):
    if timestamp is None:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(LOGO)
    print(f"起動音：{sound_name}")
    print("")
    HISTORY.append({'time': timestamp, 'sound': sound_name})


def list_history():
    if not HISTORY:
        print("通知履歴はありません。")
        return
    print("=== 通知履歴 ===")
    for entry in HISTORY:
        print(f"[{entry['time']}] {entry['sound']}")


def summary():
    print("=== 通知サマリー ===")
    print(f"通知回数: {len(HISTORY)}")
    if HISTORY:
        last = HISTORY[-1]
        print(f"最新: [{last['time']}] {last['sound']}")
    else:
        print("最新通知はありません。")


def parse_args():
    parser = argparse.ArgumentParser(description='Random OS Fake Legendary Boot Sound Notifier')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='ランダムな伝説の起動音通知を表示')
    parser_list = subparsers.add_parser('list', help='セッション内で発生した通知履歴を一覧')
    parser_summary = subparsers.add_parser('summary', help='通知サマリーを表示')

    return parser.parse_args()


def main():
    args = parse_args()

    if args.command == 'log' or args.command is None:
        sound = pick_random_boot_sound()
        display_notification(sound)
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    else:
        print("不明なコマンドです。--help を参照してください。")

if __name__ == '__main__':
    main()
