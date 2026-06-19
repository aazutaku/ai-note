import sys
import os
import platform
import random
import subprocess
import argparse
from datetime import datetime

SOUNDTRACKS = [
    '情熱大陸',
    '運命（ベートーヴェン）',
    '初音ミクの消失',
    'ドラクエ戦闘曲',
    '朝のラジオ体操',
    'ルパン三世のテーマ',
    'ポケモンセンター',
    '甲子園応援歌',
    'パイレーツ・オブ・カリビアン',
    'ガンダムOP',
    '世界の車窓から',
    'サザエさん',
    'エヴァンゲリオン残酷な天使のテーゼ',
    'スーパー戦隊メドレー',
    'アナと雪の女王 Let It Go',
    'スーパーマリオ地上BGM',
    'モンスターハンター狩猟音楽',
    'ゼルダの伝説メインテーマ',
    'ウルトラソウル',
    '北斗の拳愛をとりもどせ!!',
    '美少女戦士セーラームーン',
    'ドラゴンボールZ CHA-LA HEAD-CHA-LA',
    'ポプテピピックOP',
    'FF勝利のファンファーレ',
    '暴れん坊将軍',
    '仮面ライダー変身音',
    'きらきら星',
    'アンパンマンマーチ',
    '世界に一つだけの花',
    'NHKニュース9オープニング',
    '相棒メインテーマ',
    '笑点のテーマ',
    '水戸黄門',
    'ドリフの大爆笑',
    '鉄腕アトム',
    '銀河鉄道999',
    '名探偵コナン',
    '暴走列車',
    'ピタゴラスイッチ',
    '千本桜',
    '天城越え',
    'おどるポンポコリン',
    'マツケンサンバ',
    'サンバ・デ・ジャネイロ',
    'ボレロ',
    '運動会の徒競走BGM',
    'モーツァルト アイネ・クライネ',
    'トルコ行進曲',
    'ハレ晴レユカイ',
    'ゴジラのテーマ',
    'マリオカートレインボーロード',
    'ポケモンジム戦',
    'プリキュア',
    'おさかな天国',
    'ウルトラマン',
    '銀魂',
    '暴れん坊将軍',
    'サクラ大戦',
    'サカナクション新宝島',
    'キューピー3分クッキング',
    'タッチ',
    '紅蓮華',
    '炎（LiSA）',
    'USA',
    'バタフライ（木村カエラ）',
    '世界の車窓から',
    '宇宙戦艦ヤマト',
    'マツケンサンバII',
    'ロッキーのテーマ',
    'スターウォーズ',
    'ジョジョの奇妙な冒険',
    'アラレちゃん',
    '美味しんぼ',
    '暴れん坊将軍',
    '北の国から',
    '千と千尋の神隠し',
    'となりのトトロ',
    '崖の上のポニョ',
    '天空の城ラピュタ',
    'もののけ姫',
    'ハウルの動く城',
    'カリオストロの城',
    '名探偵コナンメインテーマ',
    '忍たま乱太郎',
    'おしりたんてい',
    'ドラえもん',
    'クレヨンしんちゃん',
    'パプリカ',
    '恋（星野源）',
    'Pretender（Official髭男dism）',
    'Lemon（米津玄師）',
    '紅（X JAPAN）',
    '天体観測',
    '小さな恋のうた',
    '世界に一つだけの花',
    'リンダリンダ',
    'Runner',
    '愛をとりもどせ!!',
    '愛のバクダン',
    '負けないで',
    '残酷な天使のテーゼ',
    'CHA-LA HEAD-CHA-LA',
    'ウィーアー!',
    '勇気100%',
    'サザエさん一家',
    '笑点のテーマ',
    '水戸黄門',
    '暴れん坊将軍',
    '鉄腕アトム',
    '銀河鉄道999',
    '名探偵コナン',
    '暴走列車',
    'ピタゴラスイッチ',
    '千本桜',
    '天城越え',
    'おどるポンポコリン',
    'マツケンサンバ',
    'サンバ・デ・ジャネイロ',
    'ボレロ',
    '運動会の徒競走BGM',
]

LOGFILE = os.path.expanduser('~/.random_os_soundtrack_notifier.log')


def pick_random_soundtrack():
    return random.choice(SOUNDTRACKS)


def notify_os(title, message):
    sys_os = platform.system()
    try:
        if sys_os == 'Darwin':
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', script], check=True)
        elif sys_os == 'Windows':
            import ctypes
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=5, threaded=True)
        elif sys_os == 'Linux':
            subprocess.run(['notify-send', title, message], check=True)
        else:
            print(f'[通知] {title}: {message}')
    except Exception as e:
        print(f'[通知エラー] {e}')


def log_notification(soundtrack):
    try:
        with open(LOGFILE, 'a', encoding='utf-8') as f:
            f.write(f'{datetime.now().isoformat()}\t{soundtrack}\n')
    except Exception as e:
        print(f'[ログエラー] {e}')


def list_log():
    if not os.path.exists(LOGFILE):
        print('ログファイルがありません。')
        return
    with open(LOGFILE, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


def summary_log():
    if not os.path.exists(LOGFILE):
        print('ログファイルがありません。')
        return
    counts = {}
    with open(LOGFILE, 'r', encoding='utf-8') as f:
        for line in f:
            if '\t' in line:
                _, track = line.strip().split('\t', 1)
                counts[track] = counts.get(track, 0) + 1
    sorted_tracks = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    print('== 通知されたBGMランキング ==')
    for track, cnt in sorted_tracks[:10]:
        print(f'{track}: {cnt}回')


def main():
    parser = argparse.ArgumentParser(description='今日の作業BGMをランダム通知')
    subparsers = parser.add_subparsers(dest='command')

    # 通常発動
    parser_notify = subparsers.add_parser('notify', help='ランダムBGMを通知')
    # ログ表示
    parser_list = subparsers.add_parser('list', help='通知履歴を表示')
    # サマリー
    parser_summary = subparsers.add_parser('summary', help='BGM通知ランキング')

    args = parser.parse_args()
    if args.command == 'notify' or args.command is None:
        soundtrack = pick_random_soundtrack()
        title = '今日の作業BGM'
        message = soundtrack
        notify_os(title, message)
        log_notification(soundtrack)
    elif args.command == 'list':
        list_log()
    elif args.command == 'summary':
        summary_log()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
