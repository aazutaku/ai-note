import sys
import os
import platform
import random
import argparse
import subprocess
from datetime import datetime

SOUNDTRACKS = [
    'なつかしのファミコン効果音',
    '宇宙戦艦発進テーマ',
    '朝礼のチャイム',
    '盆踊りの太鼓',
    '駅の発車ベル',
    '昭和のテレビCMジングル',
    '体育祭の入場行進曲',
    '昭和アニメ主題歌（インスト）',
    '工事現場のバックホーン',
    '運動会の徒競走BGM',
    '昭和の電話ベル',
    'パチンコ屋の開店音',
    '昭和歌謡イントロ',
    '時報のピッピッポーン',
    'ファミレスの呼び出し音',
    '学食の閉店メロディ',
    '学校の下校チャイム',
    '商店街のテーマソング',
    'レトロゲームのボス戦BGM',
    'カセットテープ巻き戻し音'
]

SESSION_FLAG_FILE = os.path.join(os.path.expanduser('~'), '.random_os_soundtrack_notifier_session')


def is_session_notified():
    """
    Check if notification has already been sent in this session.
    """
    if not os.path.exists(SESSION_FLAG_FILE):
        return False
    try:
        with open(SESSION_FLAG_FILE, 'r') as f:
            ts = f.read().strip()
        # Optional: session reset after 12 hours
        last = datetime.fromisoformat(ts)
        if (datetime.now() - last).total_seconds() > 43200:
            return False
        return True
    except Exception:
        return False


def set_session_notified():
    """
    Mark that notification has been sent.
    """
    try:
        with open(SESSION_FLAG_FILE, 'w') as f:
            f.write(datetime.now().isoformat())
    except Exception:
        pass


def clear_session_flag():
    try:
        if os.path.exists(SESSION_FLAG_FILE):
            os.remove(SESSION_FLAG_FILE)
    except Exception:
        pass


def pick_random_soundtrack():
    return random.choice(SOUNDTRACKS)


def send_notification(title, message):
    system = platform.system()
    try:
        if system == 'Windows':
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=6, threaded=True)
            except ImportError:
                # Fallback: print to stdout
                print(f"[通知] {title}: {message}")
        elif system == 'Darwin':
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', script], check=True)
        elif system == 'Linux':
            subprocess.run(['notify-send', title, message], check=True)
        else:
            print(f"[通知] {title}: {message}")
    except Exception as e:
        print(f"[通知] {title}: {message} (通知失敗: {e})")


def list_soundtracks():
    for idx, name in enumerate(SOUNDTRACKS, 1):
        print(f"{idx:2d}. {name}")


def main():
    parser = argparse.ArgumentParser(description='random-os-soundtrack-notifier: ターミナル/エディタ起動時に無駄BGMを通知')
    subparsers = parser.add_subparsers(dest='command')

    parser_notify = subparsers.add_parser('notify', help='ランダムBGM通知を手動で送信')
    parser_list = subparsers.add_parser('list', help='BGMタイトル一覧を表示')
    parser_clear = subparsers.add_parser('clear', help='セッションフラグをクリア')
    parser_status = subparsers.add_parser('status', help='現在のセッション通知状態を表示')

    args = parser.parse_args()

    if args.command == 'list':
        list_soundtracks()
        return
    elif args.command == 'clear':
        clear_session_flag()
        print('セッション通知フラグをクリアしました。')
        return
    elif args.command == 'status':
        if is_session_notified():
            print('このセッションでは既に通知済みです。')
        else:
            print('このセッションではまだ通知されていません。')
        return
    # Default: notify
    if is_session_notified():
        # 通知済みなら何もしない
        return
    soundtrack = pick_random_soundtrack()
    send_notification('今日の作業BGM', soundtrack)
    set_session_notified()

if __name__ == '__main__':
    main()
