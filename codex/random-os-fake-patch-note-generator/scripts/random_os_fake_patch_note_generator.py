import argparse
import random
import sys
import time
from datetime import datetime
try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

VERSION_PREFIXES = [
    'v1.0.', 'v2.3.', 'v4.2.', 'v0.9.', 'v3.1.', 'v5.0.', 'v2.7.', 'v6.6.', 'v1.9.', 'v7.0.'
]

FEATURES = [
    '集中力が一瞬だけ上昇する新アルゴリズムを搭載',
    'キーボードの打鍵音が心地よくなる新サウンドエンジンを実装',
    'コーヒーの香りが漂う仮想空間を追加',
    '昼寝モードの自動切替機能を追加',
    'モニターの明るさが気分で変化する機能を追加',
    '椅子の高さが自動調整されるAPIを実装',
    'おやつタイマーを強化',
    'デバッグ時にBGMが流れる機能を追加',
    'タスク管理AIの気まぐれモードを追加',
    'デスクトップ背景が1時間ごとに変わる機能を実装'
]

BUGFIXES = [
    '机の上の書類が片付かない問題を修正',
    'おやつの消費が止まらない問題を一時的に緩和',
    '椅子が勝手に回転するバグを修正',
    'モニターがたまに眠くなる現象を修正',
    'タスクが永遠に終わらない問題を修正',
    'コーヒーが冷める速度が速すぎるバグを修正',
    '昼寝モードが解除できないバグを修正',
    '通知が深夜にも鳴り続ける問題を修正',
    '集中力が突然消失する現象を部分的に修正',
    'BGMが止まらない問題を修正'
]

KNOWN_ISSUES = [
    '机の上の書類が片付かない現象が継続中',
    'おやつの消費が止まらない',
    '昼寝モードから目覚められないことがある',
    'コーヒーがいつの間にか消える',
    'タスク管理AIが気まぐれすぎる',
    '椅子の高さが急に変わることがある',
    'BGMが突然大音量になる',
    '通知が止まらなくなる場合がある',
    'デスクトップ背景が真っ黒になることがある',
    '集中力が予告なく低下する'
]

PERFORMANCE = [
    '集中力が一瞬だけ上昇するアルゴリズムを実装',
    'おやつ消費速度を微妙に最適化',
    '椅子の回転速度を向上',
    '通知の表示速度を強化',
    'BGMの再生品質が向上',
    'タスク切替時の気分転換効率を改善',
    '昼寝モードの切替時間を短縮',
    'コーヒーの温度保持性能を向上',
    'デスクトップ背景の切替速度を高速化',
    'タスク管理AIの応答時間を短縮'
]

LOGFILE = 'os_fake_patch_note_history.log'

CATEGORY_LABELS = [
    ('機能追加', FEATURES),
    ('バグ修正', BUGFIXES),
    ('既知の問題', KNOWN_ISSUES),
    ('パフォーマンス', PERFORMANCE)
]

def random_patch_note():
    version = random.choice(VERSION_PREFIXES) + str(random.randint(0, 99))
    lines = [f'[Patch Note {version}]']
    used_categories = random.sample(CATEGORY_LABELS, k=random.randint(2, 4))
    for label, pool in used_categories:
        n = random.randint(1, 2)
        for _ in range(n):
            lines.append(f'- {label}: {random.choice(pool)}')
    return '\n'.join(lines)

def show_notification(title, message):
    if not PLYER_AVAILABLE:
        return False
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=6
        )
        return True
    except Exception:
        return False

def log_patch_note(note):
    with open(LOGFILE, 'a', encoding='utf-8') as f:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'[{now}]\n{note}\n\n')

def list_history(limit=5):
    try:
        with open(LOGFILE, 'r', encoding='utf-8') as f:
            entries = f.read().strip().split('\n\n')
            entries = [e for e in entries if e.strip()]
            for entry in entries[-limit:]:
                print(entry)
                print()
    except FileNotFoundError:
        print('No patch note history found.')

def summary_history():
    try:
        with open(LOGFILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        total = sum(1 for l in lines if l.startswith('[') and 'Patch Note' in l)
        print(f'Total patch notes generated: {total}')
    except FileNotFoundError:
        print('No patch note history found.')

def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Patch Note Generator')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='Generate and log a fake patch note')
    parser_log.add_argument('--notify', action='store_true', help='Show desktop notification (if possible)')

    parser_list = subparsers.add_parser('list', help='List recent fake patch notes')
    parser_list.add_argument('--limit', type=int, default=5, help='Number of recent notes to show')

    parser_summary = subparsers.add_parser('summary', help='Show summary of patch note history')

    parser_once = subparsers.add_parser('once', help='Generate and show a patch note (no logging)')
    parser_once.add_argument('--notify', action='store_true', help='Show desktop notification (if possible)')

    args = parser.parse_args()
    if args.command == 'log':
        note = random_patch_note()
        log_patch_note(note)
        print(note)
        if args.notify:
            show_notification('OS Patch Note', note)
    elif args.command == 'list':
        list_history(limit=args.limit)
    elif args.command == 'summary':
        summary_history()
    elif args.command == 'once':
        note = random_patch_note()
        print(note)
        if args.notify:
            show_notification('OS Patch Note', note)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
