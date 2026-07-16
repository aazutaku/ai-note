import random
import time
import argparse
import sys
import threading
import os
try:
    import notify2
except ImportError:
    notify2 = None

MASCOTS = [
    {"name": "カーネルくん", "lines": [
        "ファイルシステムの夢を見てるよ！",
        "カーネル空間から応援中。",
        "プロセス管理は任せて！",
        "割り込みは突然に。",
        "再起動は気分転換。"
    ]},
    {"name": "メモリねずみ", "lines": [
        "バグ撲滅運動中。君も参加しよう！",
        "メモリリークには気をつけて。",
        "キャッシュは友達。",
        "スワップしすぎ注意。",
        "RAMの隅で見守ってるよ。"
    ]},
    {"name": "シェルパンダ", "lines": [
        "一服推奨。コマンド履歴は忘れないよ。",
        "シェル芸はほどほどに。",
        "$HOMEでゴロゴロ中。",
        "パイプでつながろう。",
        "aliasで省エネ生活。"
    ]},
    {"name": "スワップペンギン", "lines": [
        "メモリが足りない？いや、気合で乗り切ろう！",
        "スワップ領域でスケート中。",
        "仮想メモリの海を泳ぐ。",
        "ページアウトはお手の物。",
        "メモリ圧縮、得意です。"
    ]},
    {"name": "バイナリフクロウ", "lines": [
        "夜更かし注意。バイト列が乱れてるよ。",
        "16進数の森で羽ばたく。",
        "バイナリ解析はおまかせ。",
        "エンディアンに敏感。",
        "ファイルヘッダを見抜く目。"
    ]},
    {"name": "プロセスカメ", "lines": [
        "ゆっくりでも確実に進行中。",
        "プロセスIDは誇り。",
        "ゾンビ化しないよう注意。",
        "forkは慎重に。",
        "シグナルはおだやかに。"
    ]},
    {"name": "ログキャット", "lines": [
        "ログはすべて見ている。",
        "/var/logで昼寝中。",
        "tail -fが趣味。",
        "エラーは見逃さない。",
        "INFOも大事に。"
    ]},
    {"name": "パケットリス", "lines": [
        "ネットワーク越しに応援！",
        "pingで挨拶。",
        "パケットキャプチャ大好き。",
        "ルーティングは迷路。",
        "TCP/IPの森の住人。"
    ]}
]

KEYWORDS = ["build", "compile", "debug", "error", "idle", "focus"]

NOTIFY_INTERVAL_SEC = 600  # 10分に1回まで

_last_notify_time = 0


def pick_random_mascot():
    mascot = random.choice(MASCOTS)
    line = random.choice(mascot["lines"])
    return mascot["name"], line


def show_notification(title, message):
    if notify2 is None:
        print(f"[通知] {title}: {message}")
        return
    try:
        notify2.init("random-os-fake-mascot-parade")
        n = notify2.Notification(title, message)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.set_timeout(5000)
        n.show()
    except Exception as e:
        print(f"[通知] {title}: {message} (notify2失敗: {e})")


def should_notify():
    global _last_notify_time
    now = time.time()
    if now - _last_notify_time >= NOTIFY_INTERVAL_SEC:
        _last_notify_time = now
        return True
    return False


def mascot_parade_once():
    name, line = pick_random_mascot()
    show_notification(name, f"「{line}」")


def mascot_parade_daemon():
    while True:
        if should_notify():
            mascot_parade_once()
        time.sleep(30)


def parse_args():
    parser = argparse.ArgumentParser(description="謎のOSマスコット大行進通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("once", help="1回だけ通知する")
    subparsers.add_parser("daemon", help="定期的に通知を表示する(バックグラウンド向け)")
    parser_keywords = subparsers.add_parser("event", help="キーワードイベントで通知")
    parser_keywords.add_argument("--keyword", required=True, help="発生したイベントキーワード")

    return parser.parse_args()


def event_notify(keyword):
    if keyword.lower() in KEYWORDS and should_notify():
        mascot_parade_once()
    else:
        print(f"[INFO] キーワード '{keyword}' では通知をスキップしました。")


def main():
    args = parse_args()
    if args.command == "once":
        mascot_parade_once()
    elif args.command == "daemon":
        print("[INFO] マスコット大行進デーモンを開始します… (Ctrl+Cで停止)")
        try:
            mascot_parade_daemon()
        except KeyboardInterrupt:
            print("[INFO] 停止しました。")
    elif args.command == "event":
        event_notify(args.keyword)
    else:
        print("usage: mascot_parade.py [once|daemon|event --keyword=KEY]")

if __name__ == '__main__':
    main()
