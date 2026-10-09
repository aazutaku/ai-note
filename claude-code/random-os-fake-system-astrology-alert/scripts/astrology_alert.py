import sys
import os
import random
import time
import argparse
import platform
import subprocess
from datetime import datetime

ASTRO_MESSAGES = [
    "本日のあなたの守護惑星は{planet}です。{advice}",
    "水星逆行中につき、{action}の前に念のため{check}を確認しましょう。",
    "今日のラッキーコマンドは: {command}",
    "あなたのシステムは現在、{sign}モードです。{tip}",
    "バグは{planet}のせいかもしれません。{advice}",
    "{sign}の季節、{action}が捗る日です。",
    "宇宙の流れに従い、{command}を実行してみましょう。",
    "本日のアンラッキーコマンド: {command}。実行は慎重に。",
    "{planet}が順行に戻りました。{action}を始めるチャンスです。",
    "今夜は{sign}座流星群。{advice}"
]

PLANETS = ["水星", "金星", "火星", "木星", "土星", "天王星", "海王星", "冥王星"]
ACTIONS = ["git push", "デプロイ", "コードレビュー", "リファクタリング", "テスト実行", "ビルド", "パッケージ更新"]
CHECKS = ["diff", "CIログ", "README", "依存関係", "コミットメッセージ"]
COMMANDS = ["ls -l", "git status", "make clean", "docker ps", "pip freeze", "npm install", "htop", "ps aux", "df -h"]
SIGNS = ["牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座", "天秤座", "蠍座", "射手座", "山羊座", "水瓶座", "魚座"]
TIPS = ["新しいパッケージの導入に最適な日です。", "コードの整理をおすすめします。", "バックアップを忘れずに。", "新規プロジェクト開始に吉。", "レビュー依頼を出す好機。", "古いブランチの整理に最適。"]
ADVICES = ["大胆なリファクタリングに挑戦してみましょう。", "深呼吸して再ビルドを。", "小休憩を挟みましょう。", "コーヒーを淹れて気分転換を。", "今日は早めに帰宅を。", "バグ修正は明日でも大丈夫です。", "仲間に相談してみましょう。"]


def generate_message():
    template = random.choice(ASTRO_MESSAGES)
    msg = template.format(
        planet=random.choice(PLANETS),
        action=random.choice(ACTIONS),
        check=random.choice(CHECKS),
        command=random.choice(COMMANDS),
        sign=random.choice(SIGNS),
        tip=random.choice(TIPS),
        advice=random.choice(ADVICES)
    )
    return f"[AstroSys Alert] {msg}"


def notify(message):
    system = platform.system()
    try:
        if system == "Linux":
            try:
                import notify2
                notify2.init("AstroSys Alert")
                n = notify2.Notification("AstroSys Alert", message)
                n.show()
            except ImportError:
                # fallback to notify-send
                subprocess.run(["notify-send", "AstroSys Alert", message])
        elif system == "Darwin":
            script = f'display notification "{message}" with title "AstroSys Alert"'
            subprocess.run(["osascript", "-e", script])
        else:
            print(message)
    except Exception as e:
        print(f"[AstroSys Alert] {message}")
        print(f"[Warning] 通知に失敗しました: {e}")


def print_message():
    msg = generate_message()
    notify(msg)


def daemon_mode(interval=1800, jitter=600):
    print("[AstroSys Alert] Daemonモードで稼働開始 (Ctrl+Cで終了)")
    try:
        while True:
            print_message()
            sleep_time = interval + random.randint(-jitter, jitter)
            time.sleep(max(60, sleep_time))
    except KeyboardInterrupt:
        print("\n[AstroSys Alert] Daemonモードを終了します。")


def main():
    parser = argparse.ArgumentParser(description="OS公式・システム占星術通知スクリプト")
    parser.add_argument('--once', action='store_true', help='1回だけ通知を表示')
    parser.add_argument('--daemon', action='store_true', help='定期的に通知を表示')
    parser.add_argument('--interval', type=int, default=1800, help='通知間隔(秒)')
    parser.add_argument('--jitter', type=int, default=600, help='通知間隔のランダム幅(秒)')
    parser.add_argument('--log', action='store_true', help='通知内容を標準出力にも表示')
    args = parser.parse_args()

    if args.once:
        msg = generate_message()
        if args.log:
            print(msg)
        notify(msg)
    elif args.daemon:
        daemon_mode(interval=args.interval, jitter=args.jitter)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
