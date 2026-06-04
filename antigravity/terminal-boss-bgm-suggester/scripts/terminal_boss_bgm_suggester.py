import os
import sys
import json
import random
import argparse
from datetime import datetime, date

BGM_LIST = [
    {"title": "情熱大陸 メインテーマ", "comment": "今日も熱くいきましょう！"},
    {"title": "新世紀エヴァンゲリオン 残酷な天使のテーゼ", "comment": "仕事モード、発進！"},
    {"title": "サザエさん オープニング", "comment": "今日も元気にいってらっしゃい！"},
    {"title": "ベートーヴェン 交響曲第5番『運命』", "comment": "運命に立ち向かえ！"},
    {"title": "アンパンマンのマーチ", "comment": "勇気りんりん、はじめよう！"},
    {"title": "ドラゴンクエスト 序曲", "comment": "冒険の始まりです！"},
    {"title": "ルパン三世のテーマ", "comment": "華麗に仕事をキメろ！"},
    {"title": "ポケットモンスター タイトルテーマ", "comment": "新しい一日、ゲットだぜ！"},
    {"title": "銀河鉄道999", "comment": "さあ、旅立ちの時です。"},
    {"title": "世界の車窓から", "comment": "ゆったりスタート。"}
]

STATE_FILE = os.path.expanduser("~/.terminal_boss_bgm_suggester_state.json")


def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    try:
        with open(STATE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

def save_state(state):
    try:
        with open(STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump(state, f)
    except Exception as e:
        print(f"[WARN] 状態ファイルの保存に失敗しました: {e}")


def is_first_command_today():
    state = load_state()
    today_str = date.today().isoformat()
    last_date = state.get("last_suggest_date", "")
    return last_date != today_str

def mark_today_suggested():
    state = load_state()
    today_str = date.today().isoformat()
    state["last_suggest_date"] = today_str
    save_state(state)

def suggest_bgm():
    bgm = random.choice(BGM_LIST)
    print("Terminal BOSS BGM Suggester")
    print(f"本日のあなたのテーマソング: {bgm['title']}")
    print(f"({bgm['comment']})")


def reset_state():
    if os.path.exists(STATE_FILE):
        os.remove(STATE_FILE)
        print("状態ファイルをリセットしました。")
    else:
        print("状態ファイルは存在しません。")


def show_status():
    state = load_state()
    last_date = state.get("last_suggest_date", None)
    if last_date:
        print(f"最後にBGMが提案された日: {last_date}")
    else:
        print("まだBGMは提案されていません。")


def list_bgm():
    print("登録BGMリスト:")
    for i, bgm in enumerate(BGM_LIST, 1):
        print(f"{i}. {bgm['title']} - {bgm['comment']}")


def main():
    parser = argparse.ArgumentParser(description="Terminal BOSS BGM Suggester")
    subparsers = parser.add_subparsers(dest="command")

    parser_suggest = subparsers.add_parser("suggest", help="本日のBGMを提案 (通常は自動発動)")
    parser_reset = subparsers.add_parser("reset", help="状態ファイルをリセット")
    parser_status = subparsers.add_parser("status", help="状態ファイルの確認")
    parser_list = subparsers.add_parser("list", help="BGMリスト表示")

    args = parser.parse_args()

    if args.command == "suggest":
        if is_first_command_today():
            suggest_bgm()
            mark_today_suggested()
        else:
            print("本日のBGM提案はすでに行われています。")
    elif args.command == "reset":
        reset_state()
    elif args.command == "status":
        show_status()
    elif args.command == "list":
        list_bgm()
    else:
        # 通常は自動発動: 本日未提案なら提案
        if is_first_command_today():
            suggest_bgm()
            mark_today_suggested()

if __name__ == '__main__':
    main()
