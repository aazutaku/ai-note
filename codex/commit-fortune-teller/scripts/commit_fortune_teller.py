import argparse
import random
import sys
from datetime import datetime

tarot_cards = [
    {"name": "愚者", "meaning": "新しい始まり、自由、冒険"},
    {"name": "魔術師", "meaning": "創造力、意志、始動"},
    {"name": "女教皇", "meaning": "直感、神秘、知恵"},
    {"name": "女帝", "meaning": "豊かさ、成長、母性"},
    {"name": "皇帝", "meaning": "安定、権力、統制"},
    {"name": "法王", "meaning": "伝統、助言、信頼"},
    {"name": "恋人", "meaning": "選択、調和、愛"},
    {"name": "戦車", "meaning": "勝利、意志、前進"},
    {"name": "力", "meaning": "勇気、忍耐、強さ"},
    {"name": "隠者", "meaning": "内省、探求、孤独"},
    {"name": "運命の輪", "meaning": "転機、幸運、変化"},
    {"name": "正義", "meaning": "公平、バランス、責任"},
    {"name": "吊るされた男", "meaning": "忍耐、犠牲、視点の転換"},
    {"name": "死神", "meaning": "終わりと始まり、変容"},
    {"name": "節制", "meaning": "調和、節度、癒し"},
    {"name": "悪魔", "meaning": "誘惑、束縛、執着"},
    {"name": "塔", "meaning": "崩壊、衝撃、変革"},
    {"name": "星", "meaning": "希望、癒し、インスピレーション"},
    {"name": "月", "meaning": "不安、幻想、直感"},
    {"name": "太陽", "meaning": "成功、喜び、活力"},
    {"name": "審判", "meaning": "再生、覚醒、決断"},
    {"name": "世界", "meaning": "達成、完成、統合"}
]

fortunes = [
    {"label": "大吉", "advice": "迷わず進め、道は開かれる。"},
    {"label": "中吉", "advice": "小さな成功を大切に。"},
    {"label": "小吉", "advice": "焦らず一歩ずつ。"},
    {"label": "吉", "advice": "周囲との協力がカギ。"},
    {"label": "末吉", "advice": "油断せず堅実に。"},
    {"label": "凶", "advice": "テストを怠るべからず。"},
    {"label": "大凶", "advice": "今日は無理せず休もう。"}
]

advice_pool = [
    "レビューは慎重に。",
    "コミットメッセージに魂を込めよ。",
    "バグは思わぬ所に潜む。",
    "深夜のコミットは控えめに。",
    "リファクタリングは明日でも遅くない。",
    "デプロイ前に深呼吸。",
    "運も実力のうち。",
    "新しいブランチで冒険を。"
]

def print_fortune():
    fortune = random.choice(fortunes)
    card = random.choice(tarot_cards)
    advice = fortune["advice"]
    # 追加で遊び心あるアドバイスを混ぜる
    if random.random() < 0.5:
        advice += " " + random.choice(advice_pool)
    print("=== Commit Fortune Teller ===")
    print(f"今日の運勢: {fortune['label']}")
    print(f"このコミットは「{card['name']}」…{card['meaning']}の暗示！")
    print(f"アドバイス: {advice}")
    print("-----------------------------\n")

def log_fortune(logfile):
    fortune = random.choice(fortunes)
    card = random.choice(tarot_cards)
    advice = fortune["advice"]
    if random.random() < 0.5:
        advice += " " + random.choice(advice_pool)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(f"[{now}] 運勢: {fortune['label']} | カード: {card['name']} ({card['meaning']}) | アドバイス: {advice}\n")
    print(f"ログに記録しました: {logfile}")

def list_log(logfile, n):
    try:
        with open(logfile, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[-n:]:
                print(line.strip())
    except FileNotFoundError:
        print(f"ログファイルが見つかりません: {logfile}")

def summary_log(logfile):
    try:
        with open(logfile, "r", encoding="utf-8") as f:
            lines = f.readlines()
        total = len(lines)
        counts = {k['label']: 0 for k in fortunes}
        for line in lines:
            for label in counts.keys():
                if f"運勢: {label}" in line:
                    counts[label] += 1
        print(f"=== Fortune Summary ({total}件) ===")
        for k, v in counts.items():
            print(f"{k}: {v}回")
    except FileNotFoundError:
        print(f"ログファイルが見つかりません: {logfile}")

def main():
    parser = argparse.ArgumentParser(description="コミット占い: commit-fortune-teller")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser("log", help="占い結果をログファイルに記録")
    parser_log.add_argument("--file", default=".commit_fortune.log", help="ログファイル名")

    parser_list = subparsers.add_parser("list", help="ログの最新N件を表示")
    parser_list.add_argument("--file", default=".commit_fortune.log", help="ログファイル名")
    parser_list.add_argument("-n", type=int, default=5, help="表示件数")

    parser_summary = subparsers.add_parser("summary", help="ログのサマリー統計を表示")
    parser_summary.add_argument("--file", default=".commit_fortune.log", help="ログファイル名")

    parser_fortune = subparsers.add_parser("fortune", help="占い結果を表示 (デフォルト)")

    args = parser.parse_args()
    if args.command == "log":
        log_fortune(args.file)
    elif args.command == "list":
        list_log(args.file, args.n)
    elif args.command == "summary":
        summary_log(args.file)
    else:
        print_fortune()

if __name__ == "__main__":
    main()
