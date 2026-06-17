import argparse
import random
import sys
import subprocess
import shlex
from datetime import datetime

MOOD_COMMENTS = [
    (0, 10, "カフェイン補給推奨。"),
    (11, 30, "今日はスロースタート。無理せずに。"),
    (31, 50, "まあまあ、ぼちぼちいきましょう。"),
    (51, 70, "集中力が高まってきたかも？"),
    (71, 85, "いい感じ！このまま進みましょう。"),
    (86, 100, "今日もコーディング日和！集中力MAX。")
]

EXTRA_COMMENTS = [
    "そろそろ休憩しませんか？",
    "おやつタイムが近づいています。",
    "やる気スイッチ、どこに置いたっけ？",
    "この調子でバグも撃退！",
    "深呼吸してリフレッシュ。",
    "たまにはストレッチも大事です。",
    "進捗どうですか？",
    "コーヒーがあなたを呼んでいます。",
    "気分転換に散歩もおすすめ。",
    "自分を褒めてあげましょう。"
]

HISTORY_LOG = []


def generate_mood():
    mood_score = random.randint(0, 100)
    comment = None
    for lower, upper, base_comment in MOOD_COMMENTS:
        if lower <= mood_score <= upper:
            comment = base_comment
            break
    # 30%の確率でEXTRA_COMMENTSから追加コメント
    if random.random() < 0.3:
        comment += " " + random.choice(EXTRA_COMMENTS)
    return mood_score, comment


def print_mood_barometer():
    mood_score, comment = generate_mood()
    print("[terminal-mood-barometer]")
    print(f"やる気指数: {mood_score}")
    print(f"コメント: {comment}")
    HISTORY_LOG.append({
        "timestamp": datetime.now().isoformat(),
        "score": mood_score,
        "comment": comment
    })


def run_command(command):
    try:
        # コマンド実行
        result = subprocess.run(shlex.split(command), capture_output=True, text=True)
        print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        print_mood_barometer()
    except FileNotFoundError:
        print(f"コマンドが見つかりません: {command}", file=sys.stderr)
    except Exception as e:
        print(f"エラーが発生しました: {e}", file=sys.stderr)


def list_history():
    if not HISTORY_LOG:
        print("-- mood barometerの履歴はありません --")
        return
    for idx, entry in enumerate(HISTORY_LOG, 1):
        print(f"{idx}. {entry['timestamp']} | やる気指数: {entry['score']} | {entry['comment']}")


def summary():
    if not HISTORY_LOG:
        print("-- mood barometerの履歴はありません --")
        return
    scores = [entry['score'] for entry in HISTORY_LOG]
    avg = sum(scores) / len(scores)
    print(f"平均やる気指数: {avg:.1f}")
    print(f"記録回数: {len(scores)}")
    print(f"最高: {max(scores)} / 最低: {min(scores)}")


def main():
    parser = argparse.ArgumentParser(description="terminal-mood-barometer: ターミナル作業に気分指数を演出表示")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    # run: 任意のコマンドを実行しつつ mood barometer を表示
    run_parser = subparsers.add_parser("run", help="コマンドを実行し、気分指数を表示")
    run_parser.add_argument("cmd", nargs=argparse.REMAINDER, help="実行するコマンド")

    # mood: 気分だけ表示
    mood_parser = subparsers.add_parser("mood", help="今の気分指数とコメントを表示")

    # list: 履歴表示
    list_parser = subparsers.add_parser("list", help="気分指数の履歴一覧を表示 (セッション内)")

    # summary: 平均や統計
    summary_parser = subparsers.add_parser("summary", help="気分指数の統計サマリを表示")

    args = parser.parse_args()

    if args.command == "run":
        if not args.cmd:
            print("コマンドを指定してください。例: python mood_barometer.py run ls -l")
            sys.exit(1)
        run_command(" ".join(args.cmd))
    elif args.command == "mood":
        print_mood_barometer()
    elif args.command == "list":
        list_history()
    elif args.command == "summary":
        summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
