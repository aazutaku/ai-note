import os
import sys
import random
import argparse
import datetime
import platform

try:
    from plyer import notification
except ImportError:
    notification = None

SOUNDTRACKS = [
    '情熱大陸 メインテーマ',
    '運命（ベートーヴェン交響曲第5番）',
    '初音ミクの消失',
    'ドラクエ戦闘曲',
    '朝のラジオ体操 第一',
    'となりのトトロ サントラ',
    'ポケモンセンターBGM',
    'サザエさんのエンディング',
    'ウルトラソウル',
    'エヴァンゲリオン 残酷な天使のテーゼ',
    'ルパン三世のテーマ',
    'スーパー戦隊シリーズOP',
    '世界の車窓から',
    'ドラえもんのうた',
    'ガンダム 哀 戦士',
    'カノン（パッヘルベル）',
    '千本桜',
    'パプリカ',
    'マリオ地上BGM',
    'FF勝利のファンファーレ',
    '紅蓮華',
    '北斗の拳 愛をとりもどせ!!',
    '水戸黄門のテーマ',
    'アンパンマンマーチ',
    '暴れん坊将軍',
    '銀河鉄道999',
    'モンスターハンター メインテーマ',
    'ラジオ体操 第二',
    'NHKニュースのテーマ',
    '笑点のテーマ',
    'バッハ G線上のアリア',
    'ZARD 負けないで',
    '恋（星野源）',
    'USA（DA PUMP）',
    'Let It Go',
    'ようかい体操第一',
    'にんげんっていいな',
    'ルージュの伝言',
    '世界に一つだけの花',
    '恋するフォーチュンクッキー',
    '残酷な天使のテーゼ',
    'Get Wild',
    'CHA-LA HEAD-CHA-LA',
    '君が代',
    'サライ',
    '大きな古時計',
    'おどるポンポコリン',
    'ハレ晴レユカイ',
    'Butter-Fly',
    'タッチ',
    '勇気100%',
    '世界はあなたに笑いかけている',
    '小さな恋のうた',
    'Pretender',
    'アイネクライネナハトムジーク',
    'アナと雪の女王 サントラ',
    '炎（LiSA）',
    'パプリカ（米津玄師）',
    'シンフォニックメドレー',
    'カエルの歌',
    'ねこふんじゃった',
    '大脱走マーチ',
    '宇宙戦艦ヤマト',
    '銀河鉄道999',
    'となりのトトロ さんぽ',
    '崖の上のポニョ',
    '風になる',
    'ぼくのなつやすみ サントラ',
    'おしりたんてい',
    'ドラゴンクエスト序曲',
    '勇者の挑戦',
    'ポケットモンスター 戦闘曲',
    'MOTHER エイトメロディーズ',
    'スーパーマリオ オデッセイ',
    '星に願いを',
    'ジブリメドレー',
    'ファイナルファンタジー メインテーマ',
    'クロノ・トリガー 時の回廊',
    'ゼルダの伝説 メインテーマ',
    'ピタゴラスイッチ',
    'おどるポンポコリン',
    '日本昔ばなし',
    '世界の車窓から',
    'おさかな天国',
    'みんなのうた',
    'おもちゃのチャチャチャ',
    'チューリップ',
    'ゆうやけこやけ',
    'さくらさくら',
    '荒城の月',
    'ふるさと',
    '仰げば尊し',
    '旅立ちの日に',
    '校歌',
    '卒業写真',
    '春よ、来い',
    '夏祭り',
    '世界に一つだけの花',
    '365日の紙飛行機',
    'ありがとう',
    '未来予想図II',
    '島唄',
    '涙そうそう',
    '少年時代',
    'TSUNAMI',
    '世界の終わり',
    'さよならエレジー',
    'Lemon',
    '白日',
    '香水',
    '猫',
    'ドライフラワー',
    '夜に駆ける',
    '怪物',
    '踊',
    '群青',
    '勿忘',
    '水平線',
    'ベテルギウス'
]

LOG_PATH = os.path.expanduser('~/.random_os_soundtrack_log')


def notify(title, message):
    if notification:
        try:
            notification.notify(
                title=title,
                message=message,
                timeout=7
            )
        except Exception as e:
            print(f"[WARN] OS通知失敗: {e}")
    else:
        # Fallback: print to stdout
        print(f"[通知] {title}: {message}")


def pick_random_soundtrack():
    return random.choice(SOUNDTRACKS)


def log_notification(soundtrack):
    try:
        with open(LOG_PATH, 'a', encoding='utf-8') as f:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"{now}\t{soundtrack}\n")
    except Exception as e:
        print(f"[WARN] ログ保存失敗: {e}")


def list_soundtracks():
    for idx, s in enumerate(SOUNDTRACKS, 1):
        print(f"{idx:2d}: {s}")


def show_log():
    if not os.path.exists(LOG_PATH):
        print("通知履歴はありません。")
        return
    with open(LOG_PATH, encoding='utf-8') as f:
        lines = f.readlines()
    print("--- 通知履歴 ---")
    for line in lines[-30:]:
        print(line.strip())


def is_excluded_environment():
    # 除外: CIやシステムユーザー、/tmp, /etc など
    if os.environ.get('CI') or os.environ.get('GITHUB_ACTIONS'):
        return True
    if os.geteuid() == 0:
        return True
    cwd = os.getcwd()
    if cwd.startswith('/etc') or cwd.startswith('/tmp') or cwd.startswith('/var'):
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description='random-os-soundtrack-notifier: 今日の作業BGMを理不尽に通知')
    parser.add_argument('--list', action='store_true', help='BGM候補一覧を表示')
    parser.add_argument('--log', action='store_true', help='通知履歴を表示')
    parser.add_argument('--force', action='store_true', help='環境チェックを無視して強制通知')
    args = parser.parse_args()

    if args.list:
        list_soundtracks()
        return
    if args.log:
        show_log()
        return

    if not args.force and is_excluded_environment():
        print("[INFO] 除外環境のため通知しません。")
        return

    soundtrack = pick_random_soundtrack()
    notify('今日の作業BGM', soundtrack)
    log_notification(soundtrack)


if __name__ == '__main__':
    main()
