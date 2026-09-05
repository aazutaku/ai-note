import random
import string
import sys
import argparse
import time
import threading
import platform
try:
    from plyer import notification
except ImportError:
    notification = None

PASSWORD_WORDS = [
    'banana', 'tamagoyaki', 'penguin', 'misoSoup', 'sakura', 'ramen', 'giraffe', 'moon', 'coffee', 'apple',
    'wasabi', 'mountain', 'river', 'piano', 'neko', 'inu', 'sushi', 'caramel', 'takoyaki', 'matcha', 'honey',
    'robot', 'cloud', 'maple', 'onigiri', 'kappa', 'ninja', 'kokeshi', 'sumo', 'origami', 'soba', 'yakitori',
    'melon', 'curry', 'bamboo', 'plum', 'tiger', 'crane', 'castle', 'fuji', 'shiba', 'koi', 'tulip', 'squid'
]

SYMBOLS = ['!', '@', '#', '$', '%', '&']

TEMPLATE_MESSAGES = [
    'あなたの秘密パスワードが「{password}」としてインターネットに流出しました。',
    '警告：本日発見された流出パスワード「{password}」',
    '重要：あなたのアカウント情報「{password}」が外部に公開されました。',
    '注意：システムが新たな流出パスワード「{password}」を検出しました。',
    'セキュリティ警告：流出した認証情報「{password}」',
    '新規流出パスワード「{password}」が見つかりました。',
    '速報：あなたのパスワード「{password}」がダークウェブで発見されました。',
    'ご注意：不審なパスワード「{password}」が第三者により公開されました。'
]

JOKE_NOTICE = '※これはジョーク通知です。実際の流出ではありません。'


def generate_fake_password():
    word = random.choice(PASSWORD_WORDS)
    year = str(random.randint(1950, 2025))
    suffix = random.choice(['', str(random.randint(10,999)), random.choice(SYMBOLS)+str(random.randint(1,99))])
    if random.random() < 0.3:
        # たまに複数単語
        word2 = random.choice(PASSWORD_WORDS)
        password = f"{word}{random.choice(['_', '-', ''])}{word2}{suffix}"
    else:
        password = f"{word}{suffix}"
    # さらにランダムで数字や記号を付加
    if random.random() < 0.4:
        password += random.choice(SYMBOLS)
    if random.random() < 0.2:
        password = password.capitalize()
    return password


def generate_alert_message():
    password = generate_fake_password()
    template = random.choice(TEMPLATE_MESSAGES)
    message = template.format(password=password)
    return message


def show_notification(title, message):
    if notification:
        try:
            notification.notify(
                title=title,
                message=message,
                app_name='FakePasswordAlert',
                timeout=8
            )
        except Exception as e:
            print(f"[通知失敗] {e}")
            print(f"{title}: {message}")
    else:
        # plyerがなければprint
        print(f"[通知] {title}: {message}")


def print_alert():
    alert = generate_alert_message()
    print(f"[通知] {alert}\n{JOKE_NOTICE}")


def notify_alert():
    alert = generate_alert_message()
    title = "パスワード流出警告 (ジョーク)"
    message = f"{alert}\n{JOKE_NOTICE}"
    show_notification(title, message)


def loop_alert(interval, count):
    for i in range(count):
        notify_alert()
        if i < count-1:
            time.sleep(interval)


def main():
    parser = argparse.ArgumentParser(description='os-fake-random-password-alert: 謎のパスワード流出警告をランダム通知')
    subparsers = parser.add_subparsers(dest='command', required=False)

    parser_alert = subparsers.add_parser('alert', help='1回だけ偽パスワード流出警告を通知')
    parser_print = subparsers.add_parser('print', help='1回だけ通知内容を標準出力')
    parser_loop = subparsers.add_parser('loop', help='一定間隔で複数回通知')
    parser_loop.add_argument('--interval', type=int, default=10, help='通知間隔(秒)')
    parser_loop.add_argument('--count', type=int, default=3, help='通知回数')
    parser_test = subparsers.add_parser('test', help='全テンプレートで1回ずつ通知')

    args = parser.parse_args()

    if not args.command or args.command == 'alert':
        notify_alert()
    elif args.command == 'print':
        print_alert()
    elif args.command == 'loop':
        loop_alert(args.interval, args.count)
    elif args.command == 'test':
        for template in TEMPLATE_MESSAGES:
            password = generate_fake_password()
            alert = template.format(password=password)
            title = "パスワード流出警告 (ジョーク)"
            message = f"{alert}\n{JOKE_NOTICE}"
            show_notification(title, message)
            time.sleep(2)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
