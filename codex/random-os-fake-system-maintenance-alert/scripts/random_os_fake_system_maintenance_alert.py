import argparse
import random
import sys
import datetime

ALERT_PREFIXES = [
    '[OS ALERT] 重要:',
    '[MAINTENANCE] 緊急:',
    '[NOTICE] 予告:',
    '[ALERT] 注意:',
    '[INFO] お知らせ:'
]

ALERT_MESSAGES = [
    '本日{time}より全ウィンドウが自動的に上下逆転されます。',
    'マウス左クリック機能は右クリックに統合されます。',
    '全フォルダ名が一時的に「ねこ」にリネームされます。',
    'システム時刻がランダムな未来日にジャンプします。',
    '本日のログイン画面はモールス信号入力のみ対応となります。',
    '全ユーザーのパスワードが「password1234」に一時変更されます。',
    'デスクトップの壁紙が1分ごとにランダムな動物写真に切り替わります。',
    '全アプリのウィンドウが円形に整列されます。',
    '本日限定でCtrl+CがCtrl+Vの動作になります。',
    '全ファイルの拡張子が「.nya」に自動変換されます。',
    '一部のキー入力がランダムにカタカナへ変換されます。',
    'システム音声が関西弁になります。',
    '本日21:00より全システムを逆さまにします。',
    'マウスポインタが2倍速で移動します。',
    '全ユーザーのデスクトップに「謎の猫」のショートカットが追加されます。',
    '全ての通知が5分遅延して表示されます。',
    '一時的に全アプリがグレースケール表示になります。',
    'システムフォントが手書き風に変更されます。',
    'ランダムなタイミングで「ピコーン！」と通知音が鳴ります。',
    '全ユーザーのログインメッセージが「おつかれさまです」になります。',
    '本日だけCapsLockキーが常時ONになります。',
    'システム再起動時に「じゃんけん大会」が開催されます。',
    '一部のファイル名が逆さ文字で表示されます。',
    '一時的にファイル検索が「しりとり」順になります。',
    '全ユーザーのアイコンが「謎の生物」に変更されます。',
    '本日限定でタスクバーが画面上部に移動します。',
    '全ユーザーのスタートメニューが五十音順に並び替えられます。',
    '一時的に全アプリのタイトルバーが虹色になります。',
    'システム時刻が「平成元年」に戻ります。',
    '全ユーザーのデスクトップが「砂漠」テーマに変更されます。',
    '全フォルダのアイコンが「おにぎり」になります。',
    '本日23:59より全ファイルが自動でバックアップされます（嘘）。',
    '一時的に全ユーザー名が「ゲスト」になります。',
    '全てのウィンドウが半透明表示になります。',
    '本日だけ右クリックメニューが3倍の項目数になります。',
    '全ユーザーの壁紙が「謎の数式」になります。',
    'システム通知音が「太鼓」に変更されます。',
    '一時的に全アプリのウィンドウ枠が消失します。',
    '全ユーザーのログイン画面が「迷路」になります。',
    '一時的に全ファイルのサイズが2倍に表示されます。',
    '全ユーザーのマイドキュメントが「マイ猫」にリネームされます。'
]


def generate_random_alert():
    prefix = random.choice(ALERT_PREFIXES)
    message_template = random.choice(ALERT_MESSAGES)
    now = datetime.datetime.now()
    random_hour = random.randint(0, 23)
    random_min = random.randint(0, 59)
    time_str = f'{random_hour:02d}:{random_min:02d}'
    message = message_template.format(time=time_str)
    return f'{prefix} {message}'


def print_alerts(count=5):
    for _ in range(count):
        print(generate_random_alert())


def list_alerts():
    print('# 収録されているカオスな通知例一覧:')
    for i, template in enumerate(ALERT_MESSAGES, 1):
        print(f'{i:2d}. {template}')


def summary():
    print('random-os-fake-system-maintenance-alert Skill 概要:')
    print('・現実味ゼロの偽システムメンテナンス通知をランダム生成')
    print('・通知内容は全てジョークで、実際のシステムには影響なし')
    print(f'・登録通知パターン数: {len(ALERT_MESSAGES)}')
    print('・CLIサブコマンド: alert, list, summary')


def main():
    parser = argparse.ArgumentParser(description='ランダムな偽システムメンテナンス通知を表示します')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='ランダム通知を表示')
    parser_alert.add_argument('-n', '--number', type=int, default=5, help='表示する通知数 (デフォルト5)')

    parser_list = subparsers.add_parser('list', help='全通知テンプレートを一覧表示')
    parser_summary = subparsers.add_parser('summary', help='Skillの概要を表示')

    args = parser.parse_args()

    if args.command == 'alert':
        print_alerts(args.number)
    elif args.command == 'list':
        list_alerts()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
