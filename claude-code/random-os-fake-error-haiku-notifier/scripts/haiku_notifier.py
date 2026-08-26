import sys
import argparse
import random
import time
import threading
import platform

try:
    if platform.system() == 'Linux':
        import notify2
    elif platform.system() == 'Darwin':
        from subprocess import call
    elif platform.system() == 'Windows':
        from win10toast import ToastNotifier
except ImportError:
    pass

HAIKU_LIST = [
    'バグの香や　春まだ遠き　デバッグ道',
    '夜のコード　静かに落ちる　未定義エラー',
    '桜散る　リファクタリングの　果てしなさ',
    '朝焼けに　スタックトレース　消えゆけり',
    '秋深し　メモリリークの　気配かな',
    '冬の夜　静寂破る　例外音',
    '夏草や　デバッグ残る　夢の跡',
    '月明かり　タイポに泣いて　眠れずに',
    '霧の中　無限ループの　道しるべ',
    '風そよぐ　未定義変数　名も知らず'
]

DEFAULT_DURATION = 4  # seconds


def pick_random_haiku():
    return random.choice(HAIKU_LIST)


def notify_linux(haiku, duration):
    notify2.init('OS Error Haiku Notifier')
    n = notify2.Notification('OS Error Haiku', haiku)
    n.set_timeout(duration * 1000)
    n.show()


def notify_mac(haiku, duration):
    script = f'display notification "{haiku}" with title "OS Error Haiku"'
    call(["osascript", "-e", script])
    # macOS通知は自動消去不可


def notify_windows(haiku, duration):
    toaster = ToastNotifier()
    toaster.show_toast("OS Error Haiku", haiku, duration=duration, threaded=True)
    # Windowsはthreadedで自動消去


def notify_terminal(haiku):
    print(f"[OS Error Haiku]\n{haiku}\n")


def notify(haiku, duration=DEFAULT_DURATION):
    sys_platform = platform.system()
    try:
        if sys_platform == 'Linux':
            notify_linux(haiku, duration)
        elif sys_platform == 'Darwin':
            notify_mac(haiku, duration)
        elif sys_platform == 'Windows':
            notify_windows(haiku, duration)
        else:
            notify_terminal(haiku)
    except Exception as e:
        notify_terminal(haiku)


def handle_log(args):
    haiku = pick_random_haiku()
    notify(haiku)


def handle_list(args):
    print("=== OS Error Haiku 一覧 ===")
    for idx, h in enumerate(HAIKU_LIST, 1):
        print(f"{idx}. {h}")


def handle_summary(args):
    print(f"登録俳句数: {len(HAIKU_LIST)}")
    print("例:")
    for h in random.sample(HAIKU_LIST, min(3, len(HAIKU_LIST))):
        print(f"- {h}")


def main():
    parser = argparse.ArgumentParser(description='OS Error Haiku Notifier')
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_log = subparsers.add_parser('log', help='ランダム俳句を通知')
    parser_log.set_defaults(func=handle_log)

    parser_list = subparsers.add_parser('list', help='俳句リストを表示')
    parser_list.set_defaults(func=handle_list)

    parser_summary = subparsers.add_parser('summary', help='俳句サマリーを表示')
    parser_summary.set_defaults(func=handle_summary)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
