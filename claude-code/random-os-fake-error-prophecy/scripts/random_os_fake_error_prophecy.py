import sys
import argparse
import random
import datetime
import os
from typing import List

PROPHECY_TEMPLATES = [
    "エラー: {when}、{device}が{event}します",
    "警告: {when}、{device}が{event}を予言しています",
    "エラー: {when}、{device}が{event}に巻き込まれます",
    "警告: {when}、{device}が突然{event}するかもしれません",
    "エラー: {when}、{device}が{event}を開始します",
    "警告: {when}、{device}が{event}を主張しています",
    "エラー: {when}、{device}が{event}に目覚めます",
    "警告: {when}、{device}が{event}を計画中です"
]

WHEN_LIST = [
    "明日の朝",
    "明日の午後",
    "来週金曜",
    "3日後",
    "近日中",
    "次のアップデート時",
    "会議中",
    "ランチタイム",
    "あなたが油断した瞬間",
    "次回の再起動時"
]

DEVICE_LIST = [
    "Wi-Fi",
    "プリンタ",
    "マウス",
    "キーボード",
    "ディスプレイ",
    "USBメモリ",
    "OS",
    "CPU",
    "GPU",
    "スピーカー",
    "バッテリー",
    "タッチパッド",
    "ファイルシステム",
    "ファン",
    "ネットワークアダプタ"
]

EVENT_LIST = [
    "反逆",
    "自我に目覚める",
    "哲学的な質問をする",
    "自動でCapsLockになる",
    "突然リセットされる",
    "紙詰まりを起こす",
    "コーヒーをこぼす",
    "謎の音を鳴らす",
    "自己診断を始める",
    "英語で話し出す",
    "アップデートを拒否する",
    "勝手に再起動する",
    "ファイルを整理し始める",
    "バッテリー残量を偽装する",
    "ファンが全力で回り出す"
]

EXCLUDE_PATHS = [
    ".git",
    ".claude/skills/random-os-fake-error-prophecy/"
]

LOG_FILE = os.path.expanduser("~/.random_os_fake_error_prophecy.log")


def generate_prophecy() -> str:
    template = random.choice(PROPHECY_TEMPLATES)
    when = random.choice(WHEN_LIST)
    device = random.choice(DEVICE_LIST)
    event = random.choice(EVENT_LIST)
    return template.format(when=when, device=device, event=event)


def print_prophecy():
    prophecy = generate_prophecy()
    print(prophecy)
    log_prophecy(prophecy)


def log_prophecy(msg: str):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now().isoformat()}\t{msg}\n")
    except Exception as e:
        pass  # ログ失敗は無視


def list_log(count: int = 10):
    if not os.path.exists(LOG_FILE):
        print("ログファイルがありません。")
        return
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()[-count:]
        for l in lines:
            print(l.strip())
    except Exception as e:
        print(f"ログ読み込みエラー: {e}")


def summary_log():
    if not os.path.exists(LOG_FILE):
        print("ログファイルがありません。")
        return
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"累計予言数: {len(lines)}")
        devices = {}
        for l in lines:
            for d in DEVICE_LIST:
                if d in l:
                    devices[d] = devices.get(d, 0) + 1
        print("デバイス別予言頻度:")
        for d, cnt in sorted(devices.items(), key=lambda x: -x[1]):
            print(f"  {d}: {cnt}")
    except Exception as e:
        print(f"集計エラー: {e}")


def is_excluded_path(path: str) -> bool:
    return any(p in path for p in EXCLUDE_PATHS)


def main():
    parser = argparse.ArgumentParser(description="ランダム未来エラープロフェシー通知スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="今すぐ予言を表示")
    parser_list = subparsers.add_parser("list", help="過去の予言ログを表示")
    parser_list.add_argument("-n", "--number", type=int, default=10, help="表示件数")
    parser_summary = subparsers.add_parser("summary", help="予言ログを集計表示")
    parser_clear = subparsers.add_parser("clear", help="予言ログを消去")

    args = parser.parse_args()

    if args.command == "run" or args.command is None:
        cwd = os.getcwd()
        if is_excluded_path(cwd):
            return
        print_prophecy()
    elif args.command == "list":
        list_log(args.number)
    elif args.command == "summary":
        summary_log()
    elif args.command == "clear":
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)
            print("ログを消去しました。")
        else:
            print("ログファイルがありません。")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
