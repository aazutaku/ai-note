import argparse
import random
import sys
import os
import platform
import time

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

try:
    import pync
    PYNC_AVAILABLE = True
except ImportError:
    PYNC_AVAILABLE = False

try:
    from win10toast import ToastNotifier
    WIN10_AVAILABLE = True
except ImportError:
    WIN10_AVAILABLE = False

ACHIEVEMENTS = [
    {
        'title': 'Ctrl+C連打名人',
        'desc': 'プロセスを止める速度が常人離れしています'
    },
    {
        'title': '5分間マウス未使用',
        'desc': 'あなたの手はキーボードと一体化しました'
    },
    {
        'title': 'このコマンド誰も使ってない王',
        'desc': '世界初の実行記録が誕生しました'
    },
    {
        'title': 'ls -la 100回突破',
        'desc': 'あなたのディレクトリ愛が止まりません'
    },
    {
        'title': 'vimで迷子',
        'desc': ':q! への道は遠い'
    },
    {
        'title': 'README未読王',
        'desc': '説明書を読まずに突き進む勇気を讃えます'
    },
    {
        'title': 'sudo失敗のプロ',
        'desc': 'パスワードミス連発で防御力アップ'
    },
    {
        'title': 'ターミナル連続起動',
        'desc': 'ウィンドウが増え続ける快感'
    },
    {
        'title': 'コマンドタイプミス連発',
        'desc': 'typoの神が微笑みました'
    },
    {
        'title': 'manページ熟読',
        'desc': '知識は力なり'
    },
    {
        'title': 'git push --force発動',
        'desc': '勇気ある一歩に拍手'
    },
    {
        'title': '空白だけのコミットメッセージ',
        'desc': '無言の主張が世界を変える'
    },
    {
        'title': 'rm -rf *未遂',
        'desc': '危機一髪！冷や汗の数だけ成長します'
    },
    {
        'title': 'echo "hello" 1000回突破',
        'desc': 'あなたの声がターミナルに響き渡る'
    },
    {
        'title': 'Python仮想環境迷子',
        'desc': 'どのvenvが本物かわからない'
    }
]

NOTIFY_METHOD = None


def detect_notify_method():
    global NOTIFY_METHOD
    sysname = platform.system()
    if sysname == 'Darwin' and PYNC_AVAILABLE:
        NOTIFY_METHOD = 'pync'
    elif sysname == 'Linux' and PLYER_AVAILABLE:
        NOTIFY_METHOD = 'plyer'
    elif sysname == 'Windows' and WIN10_AVAILABLE:
        NOTIFY_METHOD = 'win10toast'
    else:
        NOTIFY_METHOD = 'stdout'


def send_notification(title, message):
    if NOTIFY_METHOD == 'pync':
        pync.notify(message, title=title)
    elif NOTIFY_METHOD == 'plyer':
        notification.notify(title=title, message=message, app_name='Achievement Unlocked')
    elif NOTIFY_METHOD == 'win10toast':
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=5, threaded=True)
    else:
        print(f"[ACHIEVEMENT UNLOCKED] : {title}\n説明: {message}\n")


def random_achievement():
    return random.choice(ACHIEVEMENTS)


def run_notifier(args):
    detect_notify_method()
    achievement = random_achievement()
    send_notification(achievement['title'], achievement['desc'])
    if NOTIFY_METHOD != 'stdout':
        # 端末にも表示
        print(f"[ACHIEVEMENT UNLOCKED] : {achievement['title']}\n説明: {achievement['desc']}\n")


def list_achievements(args):
    print("=== 実績一覧 ===")
    for idx, ach in enumerate(ACHIEVEMENTS):
        print(f"{idx+1}. {ach['title']} - {ach['desc']}")


def summary(args):
    print("このSkillは、ランダムなタイミングでOS風の実績解除通知を表示します。\n通知内容は毎回異なり、作業の合間に謎の達成感を演出します。\n")


def run_random_loop(args):
    detect_notify_method()
    min_interval = args.min_interval or 60
    max_interval = args.max_interval or 600
    try:
        while True:
            wait = random.randint(min_interval, max_interval)
            time.sleep(wait)
            achievement = random_achievement()
            send_notification(achievement['title'], achievement['desc'])
            if NOTIFY_METHOD != 'stdout':
                print(f"[ACHIEVEMENT UNLOCKED] : {achievement['title']}\n説明: {achievement['desc']}\n")
    except KeyboardInterrupt:
        print("\n[終了] ランダム実績通知ループを停止しました。")


def main():
    parser = argparse.ArgumentParser(description='謎のOS実績解除通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='即時ランダム実績通知を表示')
    parser_run.set_defaults(func=run_notifier)

    parser_list = subparsers.add_parser('list', help='実績一覧を表示')
    parser_list.set_defaults(func=list_achievements)

    parser_summary = subparsers.add_parser('summary', help='Skill概要を表示')
    parser_summary.set_defaults(func=summary)

    parser_loop = subparsers.add_parser('random-loop', help='ランダムな間隔で実績通知を繰り返す')
    parser_loop.add_argument('--min-interval', type=int, default=60, help='通知間隔の最小秒数(デフォルト60)')
    parser_loop.add_argument('--max-interval', type=int, default=600, help='通知間隔の最大秒数(デフォルト600)')
    parser_loop.set_defaults(func=run_random_loop)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
