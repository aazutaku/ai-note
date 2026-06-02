import sys
import subprocess
import random
import re
import argparse
from datetime import datetime

HAIKU_TEMPLATES = [
    ["{error_short}", "{context}", "{hope}"],
    ["{context}", "{error_short}", "{advice}"],
    ["{emotion}", "{error_short}", "{next_time}"],
    ["{error_short}", "{advice}", "{emotion}"],
    ["{context}", "{emotion}", "{hope}"],
]

ERROR_SHORT_LIST = [
    "pushできず",
    "競合あり",
    "認証失敗",
    "ファイルなし",
    "拒まれる",
    "エラーなり",
    "差分なし",
    "リモート遠し",
    "HEAD迷子",
    "権限なし",
]

CONTEXT_LIST = [
    "静かな夜",
    "遠いリモート",
    "手が止まる",
    "誰もいない",
    "branch違い",
    "静かなrepo",
    "深夜のcommit",
    "朝焼けの中",
    "黙るターミナル",
    "一人きり",
]

HOPE_LIST = [
    "明日こそは",
    "またtry",
    "次は成功",
    "やり直そう",
    "もう一度",
    "希望持つ",
    "心静かに",
    "再挑戦",
    "歩み出す",
    "次のpush",
]

ADVICE_LIST = [
    "pullしてから",
    "addを忘れず",
    "status見て",
    "fetchしよう",
    "resetしよう",
    "branch確認",
    "rebase注意",
    "commitまとめて",
    "stash活用",
    "メッセージ丁寧に",
]

EMOTION_LIST = [
    "ため息を",
    "苦笑い",
    "哀しみよ",
    "焦りつつ",
    "静かな怒り",
    "戸惑いも",
    "孤独な夜",
    "諦めず",
    "涙ひとつ",
    "心折れず",
]

NEXT_TIME_LIST = [
    "次こそは",
    "また明日",
    "歩み続け",
    "希望抱き",
    "もう一度",
    "再び挑む",
    "明日は晴れ",
    "前を向く",
    "リトライを",
    "進みゆく",
]

def extract_error_short(msg):
    for key in ["push", "merge", "auth", "file", "HEAD", "permission", "remote", "branch", "conflict", "error"]:
        if key in msg.lower():
            for phrase in ERROR_SHORT_LIST:
                if key in phrase:
                    return phrase
    return random.choice(ERROR_SHORT_LIST)

def extract_context(msg):
    if "remote" in msg.lower():
        return "遠いリモート"
    if "branch" in msg.lower():
        return "branch違い"
    if "file" in msg.lower():
        return "ファイルなし"
    if "conflict" in msg.lower():
        return "競合あり"
    return random.choice(CONTEXT_LIST)

def extract_hope(msg):
    return random.choice(HOPE_LIST)

def extract_advice(msg):
    return random.choice(ADVICE_LIST)

def extract_emotion(msg):
    return random.choice(EMOTION_LIST)

def extract_next_time(msg):
    return random.choice(NEXT_TIME_LIST)

def generate_haiku(error_msg):
    template = random.choice(HAIKU_TEMPLATES)
    mapping = {
        "error_short": extract_error_short(error_msg),
        "context": extract_context(error_msg),
        "hope": extract_hope(error_msg),
        "advice": extract_advice(error_msg),
        "emotion": extract_emotion(error_msg),
        "next_time": extract_next_time(error_msg),
    }
    lines = [t.format(**mapping) for t in template]
    return lines

def print_haiku(haiku_lines):
    print("\n俳句:")
    for line in haiku_lines:
        print(line)

def run_git_command(args):
    try:
        completed = subprocess.run(["git"] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if completed.returncode != 0:
            error_msg = completed.stderr.strip() or completed.stdout.strip()
            print(completed.stderr)
            haiku_lines = generate_haiku(error_msg)
            print_haiku(haiku_lines)
            sys.exit(completed.returncode)
        else:
            print(completed.stdout)
    except Exception as e:
        print(f"Unexpected error: {e}")
        haiku_lines = generate_haiku(str(e))
        print_haiku(haiku_lines)
        sys.exit(1)

def log_haiku(error_msg, haiku_lines):
    with open(".commit_failure_haiku.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {error_msg}\n")
        for l in haiku_lines:
            f.write(l + "\n")
        f.write("\n")

def list_haiku_logs():
    try:
        with open(".commit_failure_haiku.log", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("No haiku logs found.")

def summary_haiku_logs():
    try:
        with open(".commit_failure_haiku.log", "r", encoding="utf-8") as f:
            logs = f.read().split("\n\n")
            print(f"Total haiku entries: {len([l for l in logs if l.strip()])}")
    except FileNotFoundError:
        print("No haiku logs found.")

def main():
    parser = argparse.ArgumentParser(description="commit-failure-haikuizer: gitエラー時に俳句を生成")
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="gitコマンドをラップして実行")
    parser_run.add_argument("git_args", nargs=argparse.REMAINDER, help="gitコマンド引数")

    parser_list = subparsers.add_parser("list", help="生成された俳句ログを表示")
    parser_summary = subparsers.add_parser("summary", help="俳句ログのサマリー表示")

    args = parser.parse_args()
    if args.command == "run":
        run_git_command(args.git_args)
    elif args.command == "list":
        list_haiku_logs()
    elif args.command == "summary":
        summary_haiku_logs()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
