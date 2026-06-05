import sys
import os
import random
import platform
import argparse
import subprocess
from pathlib import Path

EXCUSES = [
    "ネットワークが遅いので少々お待ちください。",
    "今日はPCの機嫌が悪いです。",
    "水星逆行中につきご容赦ください。",
    "Wi-Fiが不安定で…",
    "マウスが反応しなくて遅れました。",
    "今日の運勢が悪いのでエラーが出ました。",
    "キーボードの調子が悪いです。",
    "隣の席がうるさくて集中できません。",
    "サーバーが遠いので時間がかかります。",
    "コーヒーをこぼしたので遅れました。",
    "エンジニアのせいではありません。",
    "仕様です。",
    "今日は満月なので…",
    "電波の影響です。",
    "猫がキーボードの上に乗りました。",
    "OSの気分次第です。",
    "宇宙線の影響かもしれません。",
    "メモリが気まぐれです。",
    "バグではなく機能です。",
    "今日は運が悪い日です。",
    "デバッグ中に何かが起きました。",
    "予期せぬ仕様変更です。",
    "再現性がありません。",
    "古いキャッシュが残っていました。",
    "リモートが応答していません。",
    "APIの気分次第です。",
    "天気のせいかもしれません。",
    "電源が不安定です。",
    "誰かがLANケーブルを抜きました。",
    "バージョン違いかもしれません。",
    "今日はやる気が出ません。",
    "CPUが休憩中です。",
    "ファイルシステムが迷子です。",
    "ネットワークの神様が怒っています。",
    "ログインセッションが切れました。",
    "セキュリティの都合です。",
    "DNSが迷子です。",
    "依存パッケージが反抗期です。",
    "シンタックスエラーは仕様です。",
    "今日はパケットが渋滞しています。",
    "バックエンドが昼休み中です。",
    "USBが抜けかけています。",
    "開発者が寝不足です。",
    "プロセスが迷子です。",
    "OSアップデートの影響です。",
    "今日は満員電車でした。",
    "マルチタスクの限界です。",
    "バッテリーが足りません。",
    "隕石が落ちてきたかもしれません。",
    "今日は運が味方しません。",
    "コードレビューの結果です。",
    "メモリリークが発生しました。",
    "今日の星座占いが最下位でした。",
    "ファイルがどこかへ行きました。",
    "バックアップから復元中です。",
    "プロキシが気まぐれです。",
    "今日はエラーが多い日です。",
    "セッションタイムアウトしました。",
    "依存関係が複雑すぎます。",
    "今日は何もかもがうまくいきません。",
    "時空が歪みました。",
    "データベースが寝ています。",
    "ファイアウォールが厳しいです。",
    "今日は祝日モードです。",
    "キャッシュが古いです。",
    "今日は気分が乗りません。",
    "ログが溢れました。",
    "パーミッションが足りません。",
    "今日はバグが多い日です。",
    "APIキーが期限切れです。",
    "今日はメンテナンス中です。",
    "ネットワークケーブルが断線しています。",
    "今日は運勢が悪い日です。",
    "同期がうまくいきません。",
    "今日は特別な日なので…",
    "プロセスがフリーズしました。",
    "今日は残念な日です。",
    "ファイルが見つかりません。",
    "今日は何もかもが遅いです。",
    "サーバーが気まぐれです。",
    "今日はバグが多発しています。",
    "今日は何もかもがダメです。",
    "今日は運がありません。",
    "今日は全てが逆風です。",
    "今日は運が悪いです。",
    "今日は何もかもがうまくいきません。",
    "今日は全てが逆風です。",
    "今日は運がありません。",
    "今日は何もかもがダメです。",
    "今日はバグが多発しています。",
    "サーバーが気まぐれです。",
    "今日は何もかもが遅いです。",
    "ファイルが見つかりません。",
    "今日は残念な日です。",
    "プロセスがフリーズしました。",
    "今日は特別な日なので…",
    "同期がうまくいきません。",
    "今日は運勢が悪い日です。",
    "ネットワークケーブルが断線しています。",
    "今日はメンテナンス中です。",
    "APIキーが期限切れです。",
    "今日はバグが多い日です。",
    "パーミッションが足りません。",
    "ログが溢れました。",
    "今日は気分が乗りません。",
    "キャッシュが古いです。",
    "今日は祝日モードです。",
    "ファイアウォールが厳しいです。",
    "データベースが寝ています。",
    "時空が歪みました。"
]

HISTORY_PATH = Path.home() / ".random_excuse_history"

MAX_HISTORY = 10


def load_history():
    if HISTORY_PATH.exists():
        with open(HISTORY_PATH, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
            return lines[-MAX_HISTORY:]
    return []

def save_history(history):
    with open(HISTORY_PATH, 'w', encoding='utf-8') as f:
        for line in history[-MAX_HISTORY:]:
            f.write(line + '\n')

def pick_excuse():
    history = load_history()
    candidates = [e for e in EXCUSES if e not in history]
    if not candidates:
        candidates = EXCUSES
    excuse = random.choice(candidates)
    history.append(excuse)
    save_history(history)
    return excuse

def notify(excuse):
    sys_platform = platform.system()
    try:
        if sys_platform == 'Linux':
            subprocess.run(['notify-send', excuse], check=True)
        elif sys_platform == 'Darwin':
            script = f'display notification "{excuse}" with title "通知"'
            subprocess.run(['osascript', '-e', script], check=True)
        elif sys_platform == 'Windows':
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("通知", excuse, duration=5)
            except ImportError:
                print("[通知]", excuse)
        else:
            print("[通知]", excuse)
    except Exception as e:
        print(f"[通知] {excuse} (通知失敗: {e})")

def list_excuses():
    for idx, excuse in enumerate(EXCUSES, 1):
        print(f"{idx:03}: {excuse}")

def show_history():
    history = load_history()
    if not history:
        print("履歴はありません。")
        return
    print("直近の通知履歴:")
    for idx, excuse in enumerate(history, 1):
        print(f"{idx:02}: {excuse}")

def main():
    parser = argparse.ArgumentParser(description='random-excuse-notifier: ターミナル操作時に言い訳を通知します。')
    subparsers = parser.add_subparsers(dest='command')

    parser_notify = subparsers.add_parser('notify', help='ランダムな言い訳を通知')
    parser_list = subparsers.add_parser('list', help='全言い訳一覧を表示')
    parser_history = subparsers.add_parser('history', help='直近の通知履歴を表示')

    args = parser.parse_args()
    if args.command == 'notify' or args.command is None:
        excuse = pick_excuse()
        notify(excuse)
    elif args.command == 'list':
        list_excuses()
    elif args.command == 'history':
        show_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
