import random
import sys
import argparse
import platform
import time

try:
    from plyer import notification
except ImportError:
    notification = None

FAKE_PATCH_TITLES = [
    '超重要：バグ「脳内会議ループが止まらない」を修正',
    '新機能：やる気を一時的に1.5倍に加速',
    '安定性向上：コーヒー依存度を最適化',
    '致命的バグ「思考が現実逃避する」修正',
    '新機能：Slack通知を自動でミュート',
    'パフォーマンス改善：昼食後の眠気を低減',
    'セキュリティ強化：社内噂話フィルター搭載',
    '既知の問題：エラー「やる気が見つかりません」',
    'UI改善：TODOリストが無限スクロール対応',
    'バグ修正：金曜日の集中力が消失する問題'
]

FAKE_PATCH_DETAILS = [
    '再起動は不要です。',
    '既知の問題：コーヒー摂取量が増加する可能性があります。',
    'このパッチは自動で適用されました。',
    '詳細は社内Wikiをご参照ください。',
    '本パッチにより開発効率が0.01%向上します。',
    '一部環境で「やる気」が暴走する場合があります。',
    '本通知は自動生成されています。',
    '次回アップデートで更なる混乱を予定しています。',
    'このパッチは現実には存在しません。',
    '万が一の場合は深呼吸してください。'
]

HISTORY = []


def generate_fake_patch():
    lines = []
    num_titles = random.randint(1, 3)
    titles = random.sample(FAKE_PATCH_TITLES, num_titles)
    details = random.sample(FAKE_PATCH_DETAILS, random.randint(1, 2))
    lines.append('[OS緊急パッチ通知]')
    lines.extend(titles)
    lines.extend(details)
    return '\n'.join(lines)


def show_notification(message):
    if notification is None:
        print("plyerがインストールされていません。通知はコンソール出力のみです。")
        print(message)
        return
    try:
        notification.notify(
            title="OS緊急パッチアラート",
            message=message,
            timeout=10
        )
    except Exception as e:
        print(f"通知エラー: {e}")
        print(message)


def log_history(message):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    HISTORY.append({'time': timestamp, 'message': message})


def list_history():
    if not HISTORY:
        print("通知履歴はありません。")
        return
    for idx, item in enumerate(HISTORY, 1):
        print(f"[{idx}] {item['time']}\n{item['message']}\n")


def summary():
    print(f"発行済み通知数: {len(HISTORY)}")
    if HISTORY:
        print(f"最新通知: {HISTORY[-1]['time']}\n{HISTORY[-1]['message']}")


def main():
    parser = argparse.ArgumentParser(description='OS緊急パッチアラート (フェイク通知)')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='フェイクパッチ通知を発行')
    parser_log.add_argument('--count', type=int, default=1, help='通知回数 (デフォルト1)')
    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='通知サマリーを表示')

    args = parser.parse_args()
    if args.command == 'log':
        for _ in range(args.count):
            msg = generate_fake_patch()
            show_notification(msg)
            log_history(msg)
            time.sleep(1)
    elif args.command == 'list':
        list_history()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
