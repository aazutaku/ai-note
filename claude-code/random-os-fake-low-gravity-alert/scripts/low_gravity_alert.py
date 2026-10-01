import sys
import argparse
import random
import time
import os

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

ALERT_MESSAGES = [
    [
        '警告：本日このPCは低重力環境に切り替わりました。',
        'ファイルのドラッグ操作が普段の3倍遠く飛びます。',
        'コードのバグがふわふわ浮遊中です。'
    ],
    [
        '注意：重力制御装置がオフラインになりました。',
        'キーボード入力が軽やかに跳ね返ります。',
        '保存したファイルが一時的に浮遊しています。'
    ],
    [
        '低重力モード発動！',
        '思考もアイデアもふわふわ上昇中。',
        '本日は宇宙遊泳気分で作業をお楽しみください。'
    ],
    [
        'OS低重力アラート：',
        'カーソル移動が通常の2倍速くなります（気のせいです）。',
        'コードレビューが無重力状態で進行中。'
    ],
    [
        '重力異常：',
        'エディタ内の文字が浮遊し始めました。',
        'バグ修正もふんわり軽やかに。'
    ],
    [
        '宇宙船モードON：',
        'デバッグ中の変数が軌道を外れました。',
        '本日は低重力での作業となります。'
    ],
    [
        '低重力警報：',
        'ターミナルの出力が上昇傾向です。',
        '集中力も一緒に浮かび上がります。'
    ],
    [
        '重力フィールド低下：',
        'ドラッグ＆ドロップの飛距離にご注意ください。',
        '本日は宇宙規格でお送りします。'
    ]
]

HISTORY_FILE = os.path.expanduser('~/.low_gravity_alert_history.log')


def random_alert_message():
    lines = random.choice(ALERT_MESSAGES)
    return '[Low Gravity Alert]\n' + '\n'.join(lines)


def send_notification(title, message):
    if PLYER_AVAILABLE:
        try:
            notification.notify(
                title=title,
                message=message,
                timeout=8
            )
        except Exception as e:
            print(f"[通知エラー] {e}")
    else:
        # Fallback: print to terminal
        print(f"{title}\n{message}")


def log_history(message):
    try:
        with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}\n{message}\n---\n")
    except Exception as e:
        print(f"[履歴保存エラー] {e}")


def show_alert(save_history=False):
    msg = random_alert_message()
    send_notification('Low Gravity Alert', '\n'.join(msg.split('\n')[1:]))
    print(msg)
    if save_history:
        log_history(msg)


def list_history(limit=5):
    if not os.path.exists(HISTORY_FILE):
        print("履歴ファイルが存在しません。")
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        entries = f.read().strip().split('---\n')
        entries = [e.strip() for e in entries if e.strip()]
        for entry in entries[-limit:]:
            print(entry)
            print('---')


def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("履歴を削除しました。")
    else:
        print("履歴ファイルが存在しません。")


def main():
    parser = argparse.ArgumentParser(description='ランダム低重力OSアラート通知スクリプト')
    subparsers = parser.add_subparsers(dest='command')

    parser_alert = subparsers.add_parser('alert', help='低重力アラートを表示')
    parser_alert.add_argument('--save', action='store_true', help='通知履歴を保存する')

    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_list.add_argument('--limit', type=int, default=5, help='表示件数')

    parser_clear = subparsers.add_parser('clear', help='通知履歴を削除')

    args = parser.parse_args()
    if args.command == 'alert' or args.command is None:
        show_alert(save_history=getattr(args, 'save', False))
    elif args.command == 'list':
        list_history(limit=args.limit)
    elif args.command == 'clear':
        clear_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
