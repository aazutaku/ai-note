import random
import time
import sys
import argparse
import threading
import platform
import subprocess

# 曲名・副題のネタリスト
MAIN_TITLES = [
    'バグ修羅場行進曲',
    '納期デッドヒート',
    'コミット地獄ロンド',
    'マージ衝突アダージョ',
    'デバッグ迷宮組曲',
    '仕様書未読ブルース',
    'リリース直前カプリッチョ',
    '無限ループ幻想曲',
    'レビュー地獄ワルツ',
    'テスト失敗レクイエム',
    '環境構築バラード',
    '会議地獄マーチ',
    '要件追加サンバ',
    'リファクタリング狂詩曲',
    'コンフリクト協奏曲',
    '残業アンセム',
    'パーミッション地獄タンゴ',
    '仕様変更ノクターン',
    'サーバーダウン即興曲',
    'エラー吐き出しセレナーデ',
]

SUB_TITLES = [
    '今こそ流せ！',
    '本日のテーマソング：',
    '推奨BGM：',
    'システム推奨本日BGM：',
    '本日のおすすめ：',
    '今流すべき一曲：',
    '開発者の魂に響け',
    '今日の作業を彩る',
    '集中力アップ推奨',
    'OS公式選曲',
    '気分転換にどうぞ',
    '謎のAI推薦',
    '作業効率UP祈願',
    '本日限定',
    'あなたのための一曲',
]

# OSごとの通知コマンド
PLATFORM = platform.system()
def send_notification(title, message):
    try:
        if PLATFORM == 'Darwin':  # macOS
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', script], check=False)
        elif PLATFORM == 'Linux':
            subprocess.run(['notify-send', title, message], check=False)
        elif PLATFORM == 'Windows':
            # Windows 10+ 用（Python 3.7+）
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=5, threaded=True)
            except ImportError:
                print(f"[通知] {title} {message}")
        else:
            print(f"[通知] {title} {message}")
    except Exception as e:
        print(f"[通知] {title} {message} (通知失敗: {e})")

def random_soundtrack():
    main = random.choice(MAIN_TITLES)
    sub = random.choice(SUB_TITLES)
    return sub, f'『{main}』'

def print_notification():
    sub, main = random_soundtrack()
    send_notification(sub, main)
    print(f"[通知] {sub}{main}")

def background_alert(interval=900, stop_event=None):
    # interval: 秒（デフォルト15分）
    while not (stop_event and stop_event.is_set()):
        print_notification()
        for _ in range(interval):
            if stop_event and stop_event.is_set():
                break
            time.sleep(1)

def list_titles():
    print("---- 曲名リスト ----")
    for i, t in enumerate(MAIN_TITLES, 1):
        print(f"{i:02d}: {t}")

def list_subtitles():
    print("---- 副題リスト ----")
    for i, t in enumerate(SUB_TITLES, 1):
        print(f"{i:02d}: {t}")

def summary():
    print("このSkillは、作業中に架空のOS公式サウンドトラック通知を表示します。")
    print(f"曲名候補数: {len(MAIN_TITLES)}、副題候補数: {len(SUB_TITLES)}")
    print("通知頻度や内容は自動制御されます。")

def main():
    parser = argparse.ArgumentParser(description='random-os-fake-soundtrack-alert')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('alert', help='1回だけ通知を出す')
    bg = subparsers.add_parser('background', help='定期的に通知を出す')
    bg.add_argument('--interval', type=int, default=900, help='通知間隔(秒) デフォルト900')
    subparsers.add_parser('list', help='曲名リストを表示')
    subparsers.add_parser('subtitles', help='副題リストを表示')
    subparsers.add_parser('summary', help='Skill概要を表示')

    args = parser.parse_args()

    if args.command == 'alert' or args.command is None:
        print_notification()
    elif args.command == 'background':
        stop_event = threading.Event()
        try:
            background_alert(interval=args.interval, stop_event=stop_event)
        except KeyboardInterrupt:
            stop_event.set()
            print("\n[通知] サウンドトラック通知を終了しました。")
    elif args.command == 'list':
        list_titles()
    elif args.command == 'subtitles':
        list_subtitles()
    elif args.command == 'summary':
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
