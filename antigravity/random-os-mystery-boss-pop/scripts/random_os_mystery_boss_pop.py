import sys
import random
import argparse
import time
from plyer import notification

BOSS_NAMES = [
    'メモリ喰いのガベージ伯爵',
    'タスク破壊のクラッシュ女王',
    '残業魔王デッドライン',
    'CPU暴走のカーネル卿',
    'アップデートの亡霊',
    'バッテリー吸いのヴァンパイア',
    'ネット遮断のファイアウォール将軍',
    'ディスク満杯のアーカイブ巨人',
    'プロセス監視のスパイダー姫',
    'ログ流しのストリーム仙人'
]

MISSIONS = [
    '今すぐ椅子から立ち上がり、3回ジャンプせよ！',
    'コーヒーを淹れて深呼吸せよ！',
    '目を閉じて10秒間リラックスせよ！',
    'ストレッチして肩を回せ！',
    'ウィンドウを最小化して外を眺めよ！',
    '水を一杯飲め！',
    '30秒間スクリーンから目を離せ！',
    '好きなBGMを流して気分転換せよ！',
    'デスク周りを軽く整理せよ！',
    '背筋を伸ばして深呼吸せよ！'
]

WARNINGS = [
    '本日は残業魔王が降臨中。全プロセスが監視されているぞ。',
    'あなたの集中力ゲージが危険域です。',
    'OSの神託：休憩を取らぬ者にバグの雨が降る。',
    'メモリリークの気配を感じる…注意せよ！',
    'バッテリー残量が減少中。充電も忘れずに。',
    'ログが溜まりすぎている。心のログも整理せよ。',
    'クラッシュ女王の呪いが近づいている。',
    'アップデートの亡霊が再起動を狙っている。',
    'タスク破壊の波動を感じる。',
    'プロセス監視のスパイダー姫が見ているぞ。'
]

POSITIONS = [
    '左上', '右上', '左下', '右下', '中央', '画面端', 'デスクトップ中央', 'タスクバー上', '通知エリア', '画面外から乱入'
]


def generate_boss_event():
    boss_name = random.choice(BOSS_NAMES)
    mission = random.choice(MISSIONS)
    warning = random.choice(WARNINGS)
    position = random.choice(POSITIONS)
    return {
        'boss_name': boss_name,
        'mission': mission,
        'warning': warning,
        'position': position
    }

def format_boss_message(event):
    return f"[OS BOSS POP]\nボス名: {event['boss_name']}\n任務: {event['mission']}\n警告: {event['warning']}\n画面表示位置: {event['position']}\n"

def show_notification(event):
    title = f"{event['boss_name']}が現れた！"
    message = f"{event['mission']}\n{event['warning']}"
    # plyer notification はタイトル・メッセージのみ
    notification.notify(
        title=title,
        message=message,
        app_name='OS BOSS POP',
        timeout=10
    )

def log_event(event, logfile=None):
    msg = format_boss_message(event)
    if logfile:
        with open(logfile, 'a', encoding='utf-8') as f:
            f.write(msg + '\n')
    else:
        print(msg)

def list_bosses():
    print('--- 登場可能なボスキャラ一覧 ---')
    for name in BOSS_NAMES:
        print(f'- {name}')

def list_missions():
    print('--- 任務例一覧 ---')
    for mission in MISSIONS:
        print(f'- {mission}')

def list_warnings():
    print('--- 警告例一覧 ---')
    for warning in WARNINGS:
        print(f'- {warning}')

def main():
    parser = argparse.ArgumentParser(description='random-os-mystery-boss-pop: 謎のOSボスキャラが乱入しカオスな命令を出す演出Skill')
    subparsers = parser.add_subparsers(dest='command')

    # popコマンド
    pop_parser = subparsers.add_parser('pop', help='ボスキャラ通知を1回発動')
    pop_parser.add_argument('--log', type=str, help='通知内容を指定ファイルに追記')
    pop_parser.add_argument('--no-notify', action='store_true', help='通知を画面に出さず標準出力のみ')

    # listコマンド
    list_parser = subparsers.add_parser('list', help='ボス/任務/警告の一覧表示')
    list_parser.add_argument('--type', type=str, choices=['boss', 'mission', 'warning'], default='boss', help='一覧種別')

    # summaryコマンド
    summary_parser = subparsers.add_parser('summary', help='Skillの概要・使い方を表示')

    args = parser.parse_args()

    if args.command == 'pop':
        event = generate_boss_event()
        log_event(event, logfile=args.log)
        if not args.no_notify:
            try:
                show_notification(event)
            except Exception as e:
                print(f'通知APIエラー: {e}', file=sys.stderr)
    elif args.command == 'list':
        if args.type == 'boss':
            list_bosses()
        elif args.type == 'mission':
            list_missions()
        elif args.type == 'warning':
            list_warnings()
    elif args.command == 'summary':
        print('random-os-mystery-boss-pop Skill:')
        print('作業中に謎のOSボスキャラが乱入し、カオスな命令や警告をランダム表示。通知演出のみで安全です。')
        print('コマンド例:')
        print('  python random_os_mystery_boss_pop.py pop')
        print('  python random_os_mystery_boss_pop.py list --type=mission')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
