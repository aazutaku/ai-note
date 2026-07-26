import sys
import argparse
import random
import datetime
import platform
import os

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

DJ_GREETINGS = [
    "おはようございます、バグ修正日和の朝です！",
    "グッドモーニング、今日もOSの海を泳ぎましょう！",
    "朝のメモリチェックはお済みですか？",
    "今日も元気に開発現場からお届けします！",
    "おはよう、カーネルの目覚めと共にスタート！"
]

OS_NEWS = [
    "本日のOSニュース：メモリ管理部が寝坊しました。",
    "カーネルパニック選手権、今朝も激戦です。",
    "新しいドライバが社内で話題沸騰中。",
    "システムコールが朝礼をサボった模様です。",
    "ファイルシステムが断片化で悩んでいます。"
]

WEATHER_FORECAST = [
    "天気予報：あなたのRAMには曇りのちフリーズ注意報。",
    "CPU温度は本日も平熱、快適な一日になりそうです。",
    "ストレージ地方に断片化前線が接近中。",
    "ネットワーク帯域に一時的な混雑予報。",
    "プロセス地方、負荷高めの見込みです。"
]

GOSSIP = [
    "業界ゴシップ：カーネルが新しい恋を始めた模様です。",
    "デバイスドライバ同士の噂話が止まりません。",
    "メモリ管理部とプロセス管理部の関係が話題に。",
    "シェルが新しいスクリプトに夢中です。",
    "バグが密かに増殖中との噂あり。"
]

CLOSING = [
    "今日も元気に開発を！",
    "素敵な一日をお過ごしください。",
    "バグに負けずに頑張りましょう！",
    "OSのご機嫌を伺いつつ、良い一日を。",
    "また次回の放送でお会いしましょう！"
]

HISTORY_FILE = os.path.expanduser("~/.random_os_radio_history")


def get_today_seed():
    today = datetime.date.today()
    return int(today.strftime("%Y%m%d"))


def pick_message(seed=None):
    if seed is not None:
        random.seed(seed)
    else:
        random.seed()
    greeting = random.choice(DJ_GREETINGS)
    news = random.choice(OS_NEWS)
    weather = random.choice(WEATHER_FORECAST)
    gossip = random.choice(GOSSIP)
    closing = random.choice(CLOSING)
    now = datetime.datetime.now().strftime("%H:%M")
    lines = [
        f"[OS Morning Radio] {now}",
        greeting,
        news,
        weather,
        gossip,
        closing
    ]
    return "\n".join(lines)


def notify_desktop(title, message):
    if not PLYER_AVAILABLE:
        print("[WARN] plyerモジュールが未インストールのため、デスクトップ通知はスキップされました。\n")
        return
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=8
        )
    except Exception as e:
        print(f"[ERROR] 通知に失敗しました: {e}")


def save_history(message):
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now().isoformat()}\n{message}\n---\n")
    except Exception as e:
        print(f"[WARN] 履歴保存に失敗: {e}")


def list_history(limit=5):
    if not os.path.exists(HISTORY_FILE):
        print("履歴ファイルがありません。")
        return
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            entries = f.read().split("---\n")
            entries = [e.strip() for e in entries if e.strip()]
            for entry in entries[-limit:]:
                print(entry)
                print("---")
    except Exception as e:
        print(f"[ERROR] 履歴読み込み失敗: {e}")


def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴ファイルがありません。")
        return
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            entries = f.read().split("---\n")
            print(f"過去の放送回数: {len([e for e in entries if e.strip()])}")
    except Exception as e:
        print(f"[ERROR] 履歴集計失敗: {e}")


def main():
    parser = argparse.ArgumentParser(description="謎のOSモーニングラジオ風メッセージを出力します。")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser("log", help="本日のラジオメッセージを出力・通知")
    parser_log.add_argument("--now", action="store_true", help="今すぐ発動（デフォルトは日替わり）")
    parser_log.add_argument("--notify", action="store_true", help="デスクトップ通知も行う")

    parser_list = subparsers.add_parser("list", help="過去のラジオ履歴を表示")
    parser_list.add_argument("--limit", type=int, default=5, help="表示件数")

    parser_summary = subparsers.add_parser("summary", help="履歴のサマリーを表示")

    args = parser.parse_args()

    if args.command == "log" or args.command is None:
        seed = None if (args.command is not None and args.now) else get_today_seed()
        message = pick_message(seed=seed)
        print(message)
        if args.notify:
            notify_desktop("OS Morning Radio", message)
        save_history(message)
    elif args.command == "list":
        list_history(limit=args.limit)
    elif args.command == "summary":
        summary_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
