import sys
import random
import argparse
import platform
import time

try:
    from plyer import notification
except ImportError:
    notification = None

try:
    import notify2
except ImportError:
    notify2 = None

try:
    from win10toast import ToastNotifier
except ImportError:
    ToastNotifier = None

def get_random_message():
    stop_codes = [
        '眠気の暴走',
        'コーヒーブレイク不足',
        'キーボードに猫が乗りました',
        'コーディング疲労蓄積',
        'マウスが迷子',
        'ネットワークが現実逃避',
        'CPUが昼寝中',
        'メモリが夢を見ています',
        'OSが考え事を始めました',
        '開発者の集中力が消失'
    ]
    causes = [
        'コーヒーが切れています',
        '猫がキーボードを占拠',
        'タスクが多すぎます',
        '休憩が必要です',
        'ネットワークが不安定',
        'マウスが見当たりません',
        'CPU温度が上昇中',
        'メモリがいっぱいです',
        'OSがアップデートを要求',
        '開発者が眠そうです'
    ]
    actions = [
        'コーヒーを淹れてください',
        '猫をなでてください',
        '深呼吸してストレッチしましょう',
        '一度休憩を取りましょう',
        'ネットワークを確認してください',
        'マウスを探してください',
        'PCを少し休ませましょう',
        'メモリを解放してください',
        'OSを再起動しないでください',
        '目を閉じてリラックスしてください'
    ]
    stop_code = random.choice(stop_codes)
    cause = random.choice(causes)
    action = random.choice(actions)
    title = '[FAKE BLUE SCREEN]'
    message = f'STOP CODE: {stop_code}\n原因: {cause}\nアクション: {action}'
    return title, message

def send_notification(title, message):
    current_os = platform.system()
    if current_os == 'Windows' and ToastNotifier:
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=8, threaded=True)
        # Wait for notification to finish
        time.sleep(8)
    elif current_os == 'Darwin' and notification:
        notification.notify(title=title, message=message, app_name='FakeBlueScreen', timeout=8)
    elif current_os == 'Linux':
        if notify2:
            notify2.init('FakeBlueScreen')
            n = notify2.Notification(title, message)
            n.set_timeout(8000)
            n.show()
            time.sleep(8)
        elif notification:
            notification.notify(title=title, message=message, app_name='FakeBlueScreen', timeout=8)
        else:
            print('通知APIが見つかりません (plyer/notify2)')
            print(f'{title}\n{message}')
    else:
        print(f'{title}\n{message}')

def list_examples():
    print('--- サンプル通知一覧 ---')
    for _ in range(8):
        title, msg = get_random_message()
        print(f'{title}\n{msg}\n')

def main():
    parser = argparse.ArgumentParser(description='ランダムなブルースクリーン風ジョーク通知を表示します。')
    subparsers = parser.add_subparsers(dest='command')

    parser_show = subparsers.add_parser('show', help='ブルースクリーン風通知を表示')
    parser_list = subparsers.add_parser('list', help='ランダム通知例を表示')
    parser_summary = subparsers.add_parser('summary', help='Skillの概要を表示')

    args = parser.parse_args()
    if args.command == 'show' or args.command is None:
        title, message = get_random_message()
        send_notification(title, message)
    elif args.command == 'list':
        list_examples()
    elif args.command == 'summary':
        print('このSkillは、作業中にデスクトップ上へランダムなブルースクリーン風ジョーク通知を表示します。')
        print('本物のエラーやシステム障害ではありません。')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
