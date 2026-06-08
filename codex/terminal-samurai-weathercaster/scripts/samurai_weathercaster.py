import random
import argparse
import sys
from datetime import datetime

# 天気と侍コメントの候補リスト
def get_weather_messages():
    return [
        "本日快晴、コードも冴え渡るでござる！",
        "曇り空、集中力を切らさぬように…",
        "雨模様、バグの気配漂うでござる",
        "雷注意報、バグの嵐到来か？",
        "強風注意、仕様変更が吹き荒れる！",
        "小春日和、穏やかな開発日和でござる",
        "猛暑日、熱き情熱で乗り切る所存！",
        "雪化粧、静かにコードを積み重ねるでござる",
        "霧深し、要件が見えぬ…慎重に参ろう",
        "台風接近、デプロイは控えるが吉！"
    ]

def get_samurai_comments():
    return [
        "エラーも恐れず、進むがよい！",
        "バグ斬り捨て御免！",
        "仕様書は心の目で読むものなり",
        "コミットは一日一善",
        "レビューは手加減無用！",
        "集中力、切らすなよ",
        "今日も一日、よろしく頼む",
        "油断大敵、慢心は禁物",
        "時には休息も大切でござる",
        "デバッグこそ武士の道"
    ]

# 出力生成
def generate_forecast():
    weather = random.choice(get_weather_messages())
    comment = random.choice(get_samurai_comments())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lines = [
        "【侍の気分天気予報】",
        f"{weather}",
        "------------------------------",
        f"侍より一言: 「{comment}」",
        f"({now})"
    ]
    return "\n".join(lines)

# ログ保存
def save_log(message, logfile="samurai_weather.log"):
    try:
        with open(logfile, 'a', encoding='utf-8') as f:
            f.write(message + '\n')
    except Exception as e:
        print(f"[ERROR] ログ保存失敗: {e}", file=sys.stderr)

# ログ一覧
def list_logs(logfile="samurai_weather.log", count=10):
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print(f"=== 直近{count}件の侍天気ログ ===")
        for line in lines[-count:]:
            print(line.strip())
    except FileNotFoundError:
        print("ログファイルが見つかりません。まだ一度も発動していない可能性があります。")
    except Exception as e:
        print(f"[ERROR] ログ読み込み失敗: {e}", file=sys.stderr)

# サマリー表示
def show_summary(logfile="samurai_weather.log"):
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            logs = f.read().split('【侍の気分天気予報】')
        logs = [l for l in logs if l.strip()]
        print(f"=== 侍天気予報 発動回数: {len(logs)}回 ===")
        weather_count = {}
        for l in logs:
            for w in get_weather_messages():
                if w in l:
                    weather_count[w] = weather_count.get(w, 0) + 1
        for w, c in sorted(weather_count.items(), key=lambda x: -x[1]):
            print(f"{w}: {c}回")
    except FileNotFoundError:
        print("ログファイルが見つかりません。まだ一度も発動していない可能性があります。")
    except Exception as e:
        print(f"[ERROR] サマリー取得失敗: {e}", file=sys.stderr)

# コマンドライン引数処理
def main():
    parser = argparse.ArgumentParser(description="Terminal Samurai Weathercaster: 侍が気分で天気予報を斬り捨てる演出スクリプト")
    subparsers = parser.add_subparsers(dest="command")

    # log: 新規発動
    log_parser = subparsers.add_parser("log", help="侍天気予報を発動し、ログに記録")
    # list: ログ表示
    list_parser = subparsers.add_parser("list", help="ログ一覧を表示")
    list_parser.add_argument("-n", "--count", type=int, default=10, help="表示件数 (デフォルト10件)")
    # summary: サマリー
    summary_parser = subparsers.add_parser("summary", help="発動回数や天気ごとの集計を表示")

    args = parser.parse_args()
    logfile = "samurai_weather.log"
    if args.command == "log" or args.command is None:
        message = generate_forecast()
        print(message)
        save_log(message, logfile=logfile)
    elif args.command == "list":
        list_logs(logfile=logfile, count=args.count)
    elif args.command == "summary":
        show_summary(logfile=logfile)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
