import sys
import argparse
import subprocess
import random
import platform
import os
import time

MOOD_WORDS = [
    ("本日のやる気指数：{}度（低気圧注意報）", lambda: random.randint(-10, 10)),
    ("情熱沸騰中！コードが踊り出す予感", lambda: None),
    ("やる気の雲行き：曇り時々晴れ", lambda: None),
    ("平常運転。やる気温度：{}度", lambda: random.randint(15, 30)),
    ("未来の自分に期待指数：{}%", lambda: random.randint(10, 99)),
    ("本日テンション：{}hPa", lambda: random.randint(900, 1100)),
    ("やる気偏差値：{}", lambda: random.randint(35, 75)),
    ("熱意レベル：{}（MAX100）", lambda: random.randint(1, 100)),
    ("やる気スイッチ：{}", lambda: random.choice(["ON", "OFF", "どこ？"]))
]

TRIGGER_KEYWORDS = ["git", "make", "build", "status", "やる気", "テンション"]


def pick_mood_word(command=None):
    idx = random.randint(0, len(MOOD_WORDS) - 1)
    template, func = MOOD_WORDS[idx]
    value = func()
    if value is not None:
        return template.format(value)
    else:
        return template


def is_trigger_command(command):
    if not command:
        return False
    for kw in TRIGGER_KEYWORDS:
        if kw in command:
            return True
    return False


def show_in_menubar(message):
    sys_platform = platform.system()
    if sys_platform == "Darwin":
        # macOS: Use AppleScript to show message in menu bar via a temporary app
        script = f'display notification "{message}" with title "MOOD BAR"'
        try:
            subprocess.run(["osascript", "-e", script], check=True)
        except Exception as e:
            print(f"[MOOD BAR] (fallback) {message}")
    elif sys_platform == "Linux":
        # Linux: Try notify-send (GNOME/KDE), fallback to stdout
        try:
            subprocess.run(["notify-send", "MOOD BAR", message])
        except Exception:
            print(f"[MOOD BAR] {message}")
    else:
        print(f"[MOOD BAR] {message}")


def log_command(command, mood):
    # No persistent logging (per spec)
    pass


def handle_show(args):
    mood = pick_mood_word()
    show_in_menubar(mood)
    print(f"[MOOD BAR] {mood}")


def handle_run(args):
    command = ' '.join(args.command)
    try:
        result = subprocess.run(args.command, capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
        print(output, end='')
        if error:
            print(error, file=sys.stderr)
    except Exception as e:
        print(f"[MOOD BAR] コマンド実行エラー: {e}")
        return
    if is_trigger_command(command):
        mood = pick_mood_word(command)
        show_in_menubar(mood)
        print(f"[MOOD BAR] {mood}")


def handle_demo(args):
    demo_commands = [
        "ls -la",
        "git status",
        "make build",
        "echo hello",
        "python script.py"
    ]
    for cmd in demo_commands:
        print(f"$ {cmd}")
        if is_trigger_command(cmd):
            mood = pick_mood_word(cmd)
            print(f"[MOOD BAR] {mood}")
        else:
            print("(コマンド出力省略)")
        time.sleep(0.7)


def main():
    parser = argparse.ArgumentParser(description="mysterious-os-mood-bar: ターミナル気分温度バー")
    subparsers = parser.add_subparsers(dest="subcommand")

    show_parser = subparsers.add_parser("show", help="今の気分温度を表示")
    show_parser.set_defaults(func=handle_show)

    run_parser = subparsers.add_parser("run", help="任意のコマンドを実行しつつ気分温度を判定")
    run_parser.add_argument("command", nargs=argparse.REMAINDER, help="コマンドと引数")
    run_parser.set_defaults(func=handle_run)

    demo_parser = subparsers.add_parser("demo", help="デモ出力例を表示")
    demo_parser.set_defaults(func=handle_demo)

    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
        sys.exit(0)
    args.func(args)

if __name__ == '__main__':
    main()
