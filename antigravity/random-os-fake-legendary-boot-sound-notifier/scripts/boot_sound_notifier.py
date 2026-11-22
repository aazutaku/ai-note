import os
import sys
import random
import argparse
import datetime
import logging
from typing import List

BOOT_SOUND_NAMES = [
    '伝説のバグフィックス交響曲',
    '謎の時代劇風ジングル',
    '宇宙人襲来ブザー',
    '量子OS幻惑チャイム',
    'メモリリーク・ファンファーレ',
    '未確認起動現象No.7',
    'サイバー忍者の目覚め',
    'アンインストールの祈り',
    'セグフォールトの叫び',
    '再起動パラダイス',
    'デバッグ神話序曲',
    'システム管理者の悪夢',
    'クラウド迷子ベル',
    'バイナリの彼方へ',
    'カーネル・パニック・シンフォニー',
    'パッチ降臨の鐘',
    '未知との遭遇アラーム',
    '仮想マシンの目覚め',
    'サーバールームの静寂',
    'バグ検出ファンファーレ',
    'エラーコード999の調べ',
    '超次元アップデート音',
    'メンテナンスの予感',
    'ブラックホール起動音',
    'メモリ解放の賛歌',
    'ロールバックの祈祷',
    'プロセス復活の歌',
    '時空を超えるブート',
    'シンタックスエラー祝祭',
    '電源ボタンの誘惑',
]

LOG_FILE = os.path.expanduser('~/.random_os_fake_legendary_boot_sound_notifier.log')


def setup_logger():
    logger = logging.getLogger('BootSoundNotifier')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(LOG_FILE, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s %(message)s')
    fh.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(fh)
    return logger


def pick_random_boot_sound() -> str:
    return random.choice(BOOT_SOUND_NAMES)


def notify_boot_sound(sound_name: str, logger=None):
    msg = f"[Boot Sound Notifier] 起動音：{sound_name}"
    print(msg)
    if logger:
        logger.info(msg)


def log_boot_sound(sound_name: str, logger):
    logger.info(f"NOTIFY {sound_name}")


def list_log_entries(limit: int = 20) -> List[str]:
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, encoding='utf-8') as f:
        lines = f.readlines()
    return lines[-limit:]


def summary_log_entries() -> dict:
    if not os.path.exists(LOG_FILE):
        return {}
    stats = {}
    with open(LOG_FILE, encoding='utf-8') as f:
        for line in f:
            if '起動音：' in line:
                name = line.split('起動音：')[-1].strip()
                stats[name] = stats.get(name, 0) + 1
    return stats


def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Legendary Boot Sound Notifier')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='通知を発生させてログに記録')
    parser_log.add_argument('--count', type=int, default=1, help='連続通知回数')

    parser_list = subparsers.add_parser('list', help='過去の通知履歴を表示')
    parser_list.add_argument('--limit', type=int, default=20, help='表示件数')

    parser_summary = subparsers.add_parser('summary', help='通知名ごとの出現回数サマリ')

    args = parser.parse_args()
    logger = setup_logger()

    if args.command == 'log' or args.command is None:
        count = getattr(args, 'count', 1)
        for _ in range(count):
            sound = pick_random_boot_sound()
            notify_boot_sound(sound, logger)
    elif args.command == 'list':
        limit = args.limit
        entries = list_log_entries(limit)
        if not entries:
            print('通知履歴はありません。')
        else:
            for line in entries:
                print(line.strip())
    elif args.command == 'summary':
        stats = summary_log_entries()
        if not stats:
            print('通知履歴はありません。')
        else:
            print('通知名ごとの出現回数:')
            for name, count in sorted(stats.items(), key=lambda x: -x[1]):
                print(f'{name}: {count}回')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
