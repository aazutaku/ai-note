import random
import sys
import argparse
import platform
import threading
import time

try:
    from plyer import notification
except ImportError:
    notification = None

PARAMETER_NAMES = [
    'やればできる度',
    'バグ耐性ゲージ',
    '今日のやる気残量',
    'コードカオス指数',
    '謎の達成感',
    'デバッグ無敵感',
    'OS自己肯定感',
    '無敵モード残量',
    'エラー吸収率',
    'コミット幸福度',
    'バグ発生予報',
    '進捗ごまかし率',
    'コーヒー摂取指数',
    'タイポ許容度',
    '謎のモチベーション'
]

MAX_PARAMS = 5


def random_param_set():
    num_params = random.randint(3, MAX_PARAMS)
    names = random.sample(PARAMETER_NAMES, num_params)
    params = {}
    for name in names:
        # 0-120%までのランダム値
        value = random.randint(0, 120)
        params[name] = f"{value}%"
    return params


def format_hypebar(params):
    lines = ["[OS Motivational Hypebar]"]
    for k, v in params.items():
        lines.append(f"{k}: {v}")
    return "\n".join(lines)


def show_notification(title, message):
    if notification is not None:
        try:
            notification.notify(
                title=title,
                message=message,
                timeout=5
            )
            return True
        except Exception:
            pass
    # Fallback to print
    print(f"{title}\n{message}")
    return False


def print_hypebar(params):
    bar = format_hypebar(params)
    print(bar)


def hypebar_once(args):
    params = random_param_set()
    bar = format_hypebar(params)
    if args.notify:
        show_notification("OS Motivational Hypebar", bar)
    else:
        print(bar)


def hypebar_loop(args):
    interval = args.interval
    try:
        while True:
            params = random_param_set()
            bar = format_hypebar(params)
            if args.notify:
                show_notification("OS Motivational Hypebar", bar)
            else:
                print(bar)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[Hypebar] 停止しました。")


def list_params(args):
    print("利用可能なパラメータ名:")
    for name in PARAMETER_NAMES:
        print(f"- {name}")


def summary(args):
    print("このSkillは、コマンド実行ごとにランダムな自己肯定感パラメータを表示します。実用性はありません。")


def parse_args():
    parser = argparse.ArgumentParser(description='OS Motivational Hypebar')
    subparsers = parser.add_subparsers(dest='command')

    parser_once = subparsers.add_parser('once', help='1回だけハイプバーを表示')
    parser_once.add_argument('--notify', action='store_true', help='OS通知として表示')
    parser_once.set_defaults(func=hypebar_once)

    parser_loop = subparsers.add_parser('loop', help='一定間隔でハイプバーを表示')
    parser_loop.add_argument('--interval', type=int, default=10, help='表示間隔(秒)')
    parser_loop.add_argument('--notify', action='store_true', help='OS通知として表示')
    parser_loop.set_defaults(func=hypebar_loop)

    parser_list = subparsers.add_parser('list', help='利用可能なパラメータ名を表示')
    parser_list.set_defaults(func=list_params)

    parser_summary = subparsers.add_parser('summary', help='Skill概要を表示')
    parser_summary.set_defaults(func=summary)

    return parser.parse_args()


def main():
    args = parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        print("コマンドを指定してください (once/loop/list/summary)")


if __name__ == '__main__':
    main()
