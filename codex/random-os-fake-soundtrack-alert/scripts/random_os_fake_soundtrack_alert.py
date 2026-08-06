import sys
import argparse
import random
import time
import os
from datetime import datetime, timedelta
try:
    from plyer import notification
except ImportError:
    notification = None

THEMES = [
    'バグ修羅場行進曲', '納期デッドヒート', '深夜残業エチュード', 'マージ地獄協奏曲',
    '仕様変更ラプソディ', 'デバッグ無限ループ', 'レビュー地帯のワルツ', 'コンフリクト・カンタービレ',
    'リリース前夜のセレナーデ', 'コミット乱舞', 'テスト失敗のバラード', 'リファクタリング幻想曲',
    '依存地獄ソナタ', '会議地獄の夜想曲', 'CI/CDカーニバル', 'ペアプロ・パラダイス',
    'スタックトレース・タンゴ', '仕様未定のブルース', 'コードレビュー葬送曲', '即席パッチポルカ',
    'タスク消化マーチ', 'バージョンアップ・シンフォニー', 'リリース延期のエレジー', 'ドキュメント迷宮',
    'ブラックスクリーン・サンバ', 'メモリリーク・カプリッチョ', 'エラー地帯のジプシー', 'タイムアウト・トッカータ',
    'コミットメッセージ・コンチェルト', '無限ビルド・ブギウギ', '仕様書亡霊のセレナーデ', '進捗ゼロのアリア',
    'バグ報告のカデンツァ', 'リファクタリング・ロンド', '会議室のフーガ', '夜明けのデプロイ',
    'プルリク地獄', 'サーバーダウン・ラグタイム', '設計書の葬送曲', 'テストカバレッジ・メヌエット',
    'コードスパゲッティ・ジグ', '仕様変更のレクイエム', 'リリース地獄のパヴァーヌ', 'コミット・カプリス',
    'プロダクション恐怖の夜', '未読Slackのカンタータ', '緊急バグ修正のジグ', '夜間デバッグのパストラーレ',
    'エンバグ・バロック', '仕様未定のカプリッチョ'
]

SUBTITLES = [
    '本日のテーマソング', '今こそ流せ！', '公式推奨BGM', '今日の気分は',
    'システムより', '開発現場応援曲', '本日の推し曲', 'OS公式サウンド',
    '謎の推薦曲', '今日の一曲', '気分転換に', '作業用BGM', '運命の一曲',
    '本日のミッション曲', 'エンジニア応援歌', '今日の気合曲', 'OSからの贈り物',
    '今週のテーマ', '本日の迷曲', '謎の新曲'
]

NOTIFY_INTERVAL = 60  # seconds
LAST_NOTIFY_FILE = os.path.expanduser('~/.random_os_fake_soundtrack_last')


def can_notify():
    try:
        if os.path.exists(LAST_NOTIFY_FILE):
            with open(LAST_NOTIFY_FILE, 'r') as f:
                last = float(f.read().strip())
            if time.time() - last < NOTIFY_INTERVAL:
                return False
        return True
    except Exception:
        return True


def update_last_notify():
    try:
        with open(LAST_NOTIFY_FILE, 'w') as f:
            f.write(str(time.time()))
    except Exception:
        pass


def generate_alert():
    subtitle = random.choice(SUBTITLES)
    theme = random.choice(THEMES)
    return f'{subtitle}：『{theme}』'


def send_notification(message):
    if notification is not None:
        try:
            notification.notify(
                title='[通知]',
                message=message,
                app_name='Fake OS Soundtrack',
                timeout=5
            )
            return True
        except Exception:
            pass
    # Fallback: print to stdout
    print(f'[通知] {message}')
    return False


def log_alert(message):
    log_file = os.path.expanduser('~/.random_os_fake_soundtrack_log')
    try:
        with open(log_file, 'a') as f:
            f.write(f'{datetime.now().isoformat()} {message}\n')
    except Exception:
        pass


def list_alerts():
    log_file = os.path.expanduser('~/.random_os_fake_soundtrack_log')
    if not os.path.exists(log_file):
        print('履歴がありません。')
        return
    with open(log_file, 'r') as f:
        for line in f:
            print(line.strip())


def summary_alerts():
    log_file = os.path.expanduser('~/.random_os_fake_soundtrack_log')
    if not os.path.exists(log_file):
        print('履歴がありません。')
        return
    from collections import Counter
    themes = []
    with open(log_file, 'r') as f:
        for line in f:
            for theme in THEMES:
                if theme in line:
                    themes.append(theme)
    c = Counter(themes)
    print('よく出た曲トップ5:')
    for theme, cnt in c.most_common(5):
        print(f'  {theme}: {cnt}回')


def main():
    parser = argparse.ArgumentParser(description='Random OS Fake Soundtrack Alert')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='最新の通知を出す')
    parser_list = subparsers.add_parser('list', help='過去の通知履歴を表示')
    parser_summary = subparsers.add_parser('summary', help='よく出た曲トップ5を表示')

    args = parser.parse_args()

    if args.command == 'log' or args.command is None:
        if can_notify():
            msg = generate_alert()
            send_notification(msg)
            log_alert(msg)
            update_last_notify()
        else:
            print('通知間隔制限中です。')
    elif args.command == 'list':
        list_alerts()
    elif args.command == 'summary':
        summary_alerts()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
