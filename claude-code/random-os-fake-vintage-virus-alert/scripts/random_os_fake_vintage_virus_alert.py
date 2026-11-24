import sys
import argparse
import random
import time
import threading
import os

VIRUS_NAMES = [
    "メロンパン",
    "さすらいのポリオミノ",
    "バナナシールド.EXE",
    "カセットテープ型ウイルス",
    "フロッピーゴースト",
    "レトロRAMイーター",
    "98式バグスター",
    "ダイヤルアップ・スネーク",
    "Y2Kカウントダウナー",
    "パラレルポート・マミー",
    "シリアルシャドウ",
    "モデムノイズスパイ",
    "CRTファントム",
    "DOSウィスパー",
    "SCSIネメシス",
    "BASICバケモノ",
    "ピコピコバグラー",
    "カラフルBIOSウィザード",
    "3.5インチ・ゾンビ",
    "バッチファイル・ゴブリン",
]

DRIVES = [
    "Aドライブ",
    "Cドライブ",
    "Dドライブ",
    "Eドライブ",
    "Fドライブ",
    "C:\\WINDOWS\\SUSPECT",
    "C:\\SYSTEM32",
    "D:\\GAMES",
    "\\tmp",
    "/home/user/.cache",
]

TEMPLATES = [
    "[警告] {year}年製ワーム“{virus}”を検出。{drive}に潜伏中。",
    "[OS公式通知] “{virus}”が{drive}を徘徊しています。",
    "[ウイルス警告] 伝説の“{virus}”がメモリに常駐しました。",
    "[注意] あなたのPCに“{virus}”の痕跡が見つかりました。",
    "[警告] “{virus}”が{drive}を監視しています。",
    "[情報] “{virus}”によるレトロ感染の兆候を検出。",
    "[公式アラート] “{virus}”が{drive}で活動中。",
    "[警告] “{virus}”がBIOS領域にアクセスしました。",
    "[ウイルス警告] “{virus}”がバッチファイルを改変しています。",
    "[注意] “{virus}”がシステムクロックを逆回転させました。",
]

YEARS = [str(y) for y in range(1987, 2004)]

# キーワードによる暗黙発動判定
def should_trigger_implicit(text):
    keywords = ["警告", "ウイルス", "感染", "セキュリティ", "ワーム", "ウィルス", "virus", "alert", "trojan"]
    return any(k in text.lower() for k in keywords)

# ジョーク警告文生成
def generate_alert():
    template = random.choice(TEMPLATES)
    virus = random.choice(VIRUS_NAMES)
    drive = random.choice(DRIVES)
    year = random.choice(YEARS)
    return template.format(virus=virus, drive=drive, year=year)

# 通知の表示(ターミナル)
def show_alert():
    alert = generate_alert()
    border = "=" * max(40, len(alert))
    print(f"\n{border}\n{alert}\n{border}\n")

# サブコマンド: 明示呼び出し
def cmd_alert(args):
    show_alert()

# サブコマンド: 暗黙発動用 (テキスト入力から判定)
def cmd_check(args):
    text = args.text or sys.stdin.read()
    if should_trigger_implicit(text):
        show_alert()
    else:
        print("(No joke alert triggered)")

# サブコマンド: テスト用 (複数回発火)
def cmd_demo(args):
    for _ in range(args.count):
        show_alert()
        time.sleep(random.uniform(0.8, 2.5))

# サブコマンド: バッチ生成
def cmd_batch(args):
    for _ in range(args.num):
        print(generate_alert())

# サブコマンド: ヘルプ
def cmd_help(args):
    print("""
random-os-fake-vintage-virus-alert: レトロOS風ウイルス警告ジョーク通知

サブコマンド:
  alert       : 1回ジョーク警告を表示
  check       : 入力テキストから暗黙発動判定
  demo        : 複数回ランダム警告を表示
  batch       : 警告文をN個まとめて生成
  help        : このヘルプを表示

例:
  python random_os_fake_vintage_virus_alert.py alert
  python random_os_fake_vintage_virus_alert.py check --text "ウイルス発見?"
  python random_os_fake_vintage_virus_alert.py demo --count 5
  python random_os_fake_vintage_virus_alert.py batch --num 10
""")

# メイン関数
def main():
    parser = argparse.ArgumentParser(description="random-os-fake-vintage-virus-alert")
    subparsers = parser.add_subparsers(dest="command")

    p_alert = subparsers.add_parser("alert", help="1回ジョーク警告を表示")
    p_alert.set_defaults(func=cmd_alert)

    p_check = subparsers.add_parser("check", help="入力テキストから暗黙発動判定")
    p_check.add_argument("--text", type=str, default=None, help="判定用テキスト")
    p_check.set_defaults(func=cmd_check)

    p_demo = subparsers.add_parser("demo", help="複数回ランダム警告を表示")
    p_demo.add_argument("--count", type=int, default=3, help="表示回数")
    p_demo.set_defaults(func=cmd_demo)

    p_batch = subparsers.add_parser("batch", help="警告文をN個まとめて生成")
    p_batch.add_argument("--num", type=int, default=5, help="生成数")
    p_batch.set_defaults(func=cmd_batch)

    p_help = subparsers.add_parser("help", help="このヘルプを表示")
    p_help.set_defaults(func=cmd_help)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
