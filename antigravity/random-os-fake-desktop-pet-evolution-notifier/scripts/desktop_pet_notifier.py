import random
import sys
import argparse
import time
import platform

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

PET_FORMS = [
    "幻のカメレオン形態",
    "サボテン系ペット",
    "浮遊型クラゲペット",
    "メタモルフォーゼ猫",
    "幻のウサギ型ペット",
    "量子ドットペンギン",
    "データスライム",
    "バグバード",
    "エーテルリス",
    "ピクセルタコ",
    "グリッチハムスター",
    "サイバーカブトムシ",
    "ステルスパンダ",
    "フローティングドラゴン",
    "バイナリイヌ"
]

TARGETS = [
    "マウスポインタ",
    "キーボード領域",
    "クリップボード",
    "ターミナル",
    "デスクトップ背景",
    "ファイルエクスプローラ",
    "ウィンドウバー",
    "スクリーンセーバー",
    "音量ミキサー",
    "ネットワークアイコン"
]

ACTIONS = [
    "進化しました。",
    "が誕生しました。お水は不要です。",
    "が常駐します。",
    "が出現しました。",
    "が変異しました。",
    "がアップグレードされました。",
    "が分裂しました。",
    "が融合しました。",
    "が同期されました。",
    "が覚醒しました。"
]

PREFIX = "[OS公式通知] "

HISTORY = []


def generate_message():
    target = random.choice(TARGETS)
    pet = random.choice(PET_FORMS)
    action = random.choice(ACTIONS)
    msg = f"{PREFIX}あなたの{target}は本日“{pet}”{action}"
    return msg


def notify(msg):
    if PLYER_AVAILABLE:
        notification.notify(
            title="OS公式通知",
            message=msg.replace(PREFIX, ""),
            app_name="DesktopPetEvolution",
            timeout=5
        )
    else:
        print(msg)


def log_message(msg):
    HISTORY.append({
        "message": msg,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })


def list_history():
    for item in HISTORY:
        print(f"{item['timestamp']} {item['message']}")


def summary():
    print(f"合計 {len(HISTORY)} 件の進化通知が生成されました。")
    forms = set()
    for item in HISTORY:
        for pet in PET_FORMS:
            if pet in item['message']:
                forms.add(pet)
    print(f"登場したペット形態: {', '.join(forms) if forms else 'なし'}")


def main():
    parser = argparse.ArgumentParser(description="ランダムなデスクトップペット進化通知を表示します")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    parser_log = subparsers.add_parser("log", help="進化通知を1回生成・表示")
    parser_log.add_argument("-n", type=int, default=1, help="通知回数")
    parser_list = subparsers.add_parser("list", help="通知履歴を表示")
    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリを表示")

    args = parser.parse_args()

    if args.command == "log":
        for _ in range(args.n):
            msg = generate_message()
            notify(msg)
            log_message(msg)
            time.sleep(1)
    elif args.command == "list":
        list_history()
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
