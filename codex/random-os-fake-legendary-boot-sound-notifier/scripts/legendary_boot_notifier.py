import random
import argparse
import sys
from datetime import datetime

LEGENDARY_BOOT_SOUNDS = [
    "伝説のバグフィックス交響曲",
    "宇宙人襲来ブザー",
    "未承認アップデートファンファーレ",
    "時代劇風ジングル - 幕開けの章",
    "謎のセキュリティ警告マーチ",
    "幻のサービスパック祝祭曲",
    "禁断のレジストリファンファーレ",
    "開発者モード突入チャイム",
    "ブルースクリーン・セレナーデ",
    "サポート切れバラード",
    "超高速再起動ラプソディ",
    "夜明けのパッチノート序曲",
    "未知との遭遇ブートベル",
    "時空を超えた互換性シンフォニー",
    "謎のデバッグモード警告音",
    "伝説のアップグレード祝典",
    "メモリ解放のカノン",
    "幻のOSリリース記念オーケストラ",
    "システム復元の祈り",
    "サイレントクラッシュファンファーレ"
]

LOG_FILE = None  # ログ保存は行わない仕様


def generate_boot_sound():
    """
    ランダムな架空の起動音名を返す
    """
    return random.choice(LEGENDARY_BOOT_SOUNDS)


def print_notification(sound_name, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[OS通知] 起動音：{sound_name}")


def notify(args):
    sound = generate_boot_sound()
    print_notification(sound)


def list_sounds(args):
    print("--- 伝説の起動音一覧 ---")
    for idx, name in enumerate(LEGENDARY_BOOT_SOUNDS, 1):
        print(f"{idx:2d}. {name}")


def summary(args):
    print("# random-os-fake-legendary-boot-sound-notifier 概要\n")
    print("このスクリプトは、作業開始時や明示呼び出し時に、架空の伝説的OS起動音名をテキスト通知として表示します。\n")
    print("- 通知例: [OS通知] 起動音：伝説のバグフィックス交響曲\n- 実際に音は鳴りません\n- 履歴やログ保存はありません\n")
    print("サブコマンド:\n  notify   : ランダムな起動音通知を1件表示\n  list     : 伝説の起動音タイトル一覧を表示\n  summary  : このSkillの概要を表示\n")


def parse_args():
    parser = argparse.ArgumentParser(
        description="架空の伝説的OS起動音のテキスト通知を表示するスクリプト"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_notify = subparsers.add_parser("notify", help="ランダムな伝説の起動音通知を表示")
    parser_notify.set_defaults(func=notify)

    parser_list = subparsers.add_parser("list", help="伝説の起動音タイトル一覧を表示")
    parser_list.set_defaults(func=list_sounds)

    parser_summary = subparsers.add_parser("summary", help="Skillの概要を表示")
    parser_summary.set_defaults(func=summary)

    return parser.parse_args()


def main():
    args = parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
