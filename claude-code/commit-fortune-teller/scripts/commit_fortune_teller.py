import sys
import random
import argparse
import datetime

TAROT_CARDS = [
    {"name": "愚者", "meaning": "新しい旅立ち。自由な発想を大切に。"},
    {"name": "魔術師", "meaning": "創造力が高まる。新しいアイデアに挑戦を。"},
    {"name": "女教皇", "meaning": "直感が冴える。冷静な判断を。"},
    {"name": "女帝", "meaning": "豊かさと成長。周囲と協力を。"},
    {"name": "皇帝", "meaning": "リーダーシップ発揮の時。自信を持ちましょう。"},
    {"name": "法王", "meaning": "伝統やルールを尊重。基本に立ち返ると吉。"},
    {"name": "恋人", "meaning": "選択の時。迷ったら信頼できる人に相談を。"},
    {"name": "戦車", "meaning": "勢いが大事。迷わず突き進め。"},
    {"name": "力", "meaning": "忍耐と努力が報われる。焦らず着実に。"},
    {"name": "隠者", "meaning": "一人で考える時間が必要。内省を大切に。"},
    {"name": "運命の輪", "meaning": "変化の兆し。流れに身を任せて吉。"},
    {"name": "正義", "meaning": "バランスと公正。冷静な判断が吉。"},
    {"name": "吊るされた男", "meaning": "一時停止。視点を変えると突破口が。"},
    {"name": "死神", "meaning": "終わりと始まり。不要なものを手放そう。"},
    {"name": "節制", "meaning": "調和とバランス。無理せず進め。"},
    {"name": "悪魔", "meaning": "誘惑に注意。短絡的な決断は凶。"},
    {"name": "塔", "meaning": "予期せぬトラブル。バックアップ必須。"},
    {"name": "星", "meaning": "希望が見える。夢を持って進もう。"},
    {"name": "月", "meaning": "不安や迷い。焦らず見極めを。"},
    {"name": "太陽", "meaning": "成功と祝福。全てがうまくいく日。"},
    {"name": "審判", "meaning": "再出発の時。過去の経験を活かそう。"},
    {"name": "世界", "meaning": "完成と達成。努力が報われる。"}
]

FORTUNES = [
    ("大吉", "今日は絶好調！思い切った挑戦も吉。"),
    ("中吉", "順調な一日。着実に進めましょう。"),
    ("小吉", "まずまずの運勢。油断せずに。"),
    ("吉", "安定した運気。普段通りでOK。"),
    ("末吉", "少し注意が必要。慎重に。"),
    ("凶", "トラブルに注意。焦らず対処を。"),
    ("大凶", "今日は慎重に。無理は禁物。")
]

LUCKY_COMMANDS = [
    "git stash",
    "git rebase",
    "git cherry-pick",
    "git revert",
    "git log",
    "git bisect",
    "git blame",
    "git diff",
    "git reset",
    "git clean",
    "git reflog"
]

BORDER = "───────────── Fortune Teller ─────────────"

ADVICE_LIST = [
    "大胆な変更も恐れず進みましょう。",
    "テストを忘れずに。",
    "レビューを依頼してみては？",
    "コミットメッセージに愛を込めて。",
    "今日は細かい修正が吉。",
    "一旦休憩してコーヒーを。",
    "リファクタリングのチャンス。",
    "CIのログをよく確認しましょう。",
    "push前に差分を見直すと吉。",
    "仲間に助けを求めると運気UP。"
]

def generate_fortune():
    fortune, fortune_msg = random.choice(FORTUNES)
    tarot = random.choice(TAROT_CARDS)
    lucky_cmd = random.choice(LUCKY_COMMANDS)
    advice = random.choice(ADVICE_LIST)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    lines = [
        BORDER,
        f"本日の運勢：{fortune}",
        f"このコミットは「{tarot['name']}」…{tarot['meaning']}",
        f"アドバイス：{advice}",
        f"ラッキーコマンド：{lucky_cmd}",
        BORDER
    ]
    return "\n".join(lines)

def print_fortune():
    print(generate_fortune())

def main():
    parser = argparse.ArgumentParser(
        description='コミット占い師: commit/push/merge時にランダムな占い結果を表示します。')
    parser.add_argument('--log', action='store_true', help='今日の占い結果を表示(同じ内容)')
    parser.add_argument('--list', action='store_true', help='全タロットカード一覧を表示')
    parser.add_argument('--summary', action='store_true', help='運勢の種類一覧を表示')
    args = parser.parse_args()

    if args.list:
        print(BORDER)
        for card in TAROT_CARDS:
            print(f"{card['name']}: {card['meaning']}")
        print(BORDER)
        return
    if args.summary:
        print(BORDER)
        for f, msg in FORTUNES:
            print(f"{f}: {msg}")
        print(BORDER)
        return
    if args.log:
        # 今日の日付固定の乱数シードで同じ結果を出す
        seed = int(datetime.datetime.now().strftime('%Y%m%d'))
        random.seed(seed)
        print(generate_fortune())
        return
    # 通常発動:完全ランダム
    print_fortune()

if __name__ == '__main__':
    main()
