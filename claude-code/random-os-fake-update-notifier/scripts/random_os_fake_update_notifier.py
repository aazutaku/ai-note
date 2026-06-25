import random
import argparse
import sys
import time
from plyer import notification

FAKE_FEATURES = [
    'クリップボードの中身が詩的に自動要約される',
    'デスクトップアイコンがランダムに並び替わる',
    '全ウィンドウが時々半透明になる',
    'カレンダーに「謎の祝日」が自動追加される',
    'ファイル名が時々韻を踏むように変換される',
    'スクリーンショット時に謎のエフェクトがかかる',
    'マウスカーソルが一瞬だけ消える',
    '音量調整時に「おみくじ」が表示される',
    'スタートメニューが逆さまになる',
    'バッテリー残量が「やる気」で表示される'
]

FAKE_BUGFIXES = [
    'ごく稀に時計が未来に進みすぎる問題を修正',
    '意味のない通知が二重に表示される不具合を修正',
    'スリープ復帰時に壁紙が消えるバグを修正',
    '一部環境で「やる気」が表示されない問題を修正',
    'タスクバーが踊りだす現象を改善',
    'ウィンドウが勝手に最小化されるバグを修正',
    '謎のエラーコード「0xDEADBEEF」を非表示化',
    '時々マウスカーソルが巨大化する問題を修正',
    '通知音が「猫の鳴き声」になるバグを修正',
    '再起動要求が唐突すぎる問題を緩和'
]

FAKE_OTHERS = [
    '意味のない通知をさらに高速化',
    'アップデート通知のフォントを気分で変更',
    '通知の色合いがより謎めいたものに',
    '「アップデート完了」の表示タイミングをランダム化',
    '通知ウィンドウの閉じるボタンが時々消える',
    'アップデート説明文がより長くなりました',
    '通知がたまに英語になるバグを仕様に変更',
    '更新履歴が「詩的」になりました',
    '通知が自動で自己紹介するようになりました',
    '「特に何もしていません」アップデートを追加'
]

NOTIFY_TITLE = 'OS Update Notifier'


def generate_fake_update():
    feature = random.choice(FAKE_FEATURES)
    bugfix = random.choice(FAKE_BUGFIXES)
    other = random.choice(FAKE_OTHERS)
    lines = [
        f'新機能: “{feature}”が追加されました。',
        f'バグ修正: “{bugfix}。”',
        f'その他: “{other}”。',
        '\n再起動は必要ありません。'
    ]
    return '\n'.join(lines)


def show_notification(message):
    try:
        notification.notify(
            title=NOTIFY_TITLE,
            message=message,
            app_name='Fake OS Updater',
            timeout=8
        )
    except Exception as e:
        print(f"[ERROR] 通知の表示に失敗しました: {e}", file=sys.stderr)


def log_fake_update(message, logfile=None):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    logline = f'[{timestamp}] {message.replace(chr(10), " ")}\n'
    if logfile:
        try:
            with open(logfile, 'a', encoding='utf-8') as f:
                f.write(logline)
        except Exception as e:
            print(f"[ERROR] ログファイルへの書き込みに失敗: {e}", file=sys.stderr)
    else:
        print(logline)


def list_fake_updates(count=5):
    for _ in range(count):
        msg = generate_fake_update()
        print(f'---\n{msg}\n')


def summary_fake_updates(count=10):
    features = set()
    bugfixes = set()
    others = set()
    for _ in range(count):
        features.add(random.choice(FAKE_FEATURES))
        bugfixes.add(random.choice(FAKE_BUGFIXES))
        others.add(random.choice(FAKE_OTHERS))
    print('# これまでの（架空）アップデート要約')
    print('## 新機能:')
    for f in features:
        print(f'- {f}')
    print('## バグ修正:')
    for b in bugfixes:
        print(f'- {b}')
    print('## その他:')
    for o in others:
        print(f'- {o}')


def main():
    parser = argparse.ArgumentParser(description='謎のOSアップデート通知を表示します。')
    subparsers = parser.add_subparsers(dest='command', required=False)

    parser_log = subparsers.add_parser('log', help='ランダム通知を生成し、ログに記録')
    parser_log.add_argument('--logfile', type=str, help='ログファイルパス')

    parser_list = subparsers.add_parser('list', help='ランダム通知を複数出力')
    parser_list.add_argument('--count', type=int, default=5, help='出力件数')

    parser_summary = subparsers.add_parser('summary', help='架空アップデートの要約を表示')
    parser_summary.add_argument('--count', type=int, default=10, help='集計件数')

    parser_notify = subparsers.add_parser('notify', help='通知をデスクトップに表示')

    args = parser.parse_args()

    if args.command == 'log':
        msg = generate_fake_update()
        log_fake_update(msg, args.logfile)
    elif args.command == 'list':
        list_fake_updates(args.count)
    elif args.command == 'summary':
        summary_fake_updates(args.count)
    elif args.command == 'notify' or args.command is None:
        msg = generate_fake_update()
        show_notification(msg)
        print(f'\n[通知内容]\n{msg}\n')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
