import argparse
import subprocess
import random
import sys
import os
from typing import List

SAMURAI_PHRASES = [
    "拙者、{cmd}の構えにて候！",
    "これぞ{cmd}、まさに一世一代の大勝負！",
    "お主、{cmd}を成し遂げ申した！",
    "この{cmd}、見事なり！",
    "拙者、{cmd}の術を使い申す！",
    "そなたの{cmd}、鮮やかなる手並み！",
    "{cmd}、いざ参る！",
    "{cmd}、これぞ侍の嗜み！",
    "{cmd}の極意、今ここに！",
    "お見事、{cmd}の業！"
]

ON_OFF_FILE = os.path.expanduser("~/.samurai_announcer_on")


def is_enabled() -> bool:
    return os.path.exists(ON_OFF_FILE)


def enable():
    with open(ON_OFF_FILE, 'w') as f:
        f.write('on')
    print("terminal-samurai-announcer: ON")


def disable():
    if os.path.exists(ON_OFF_FILE):
        os.remove(ON_OFF_FILE)
    print("terminal-samurai-announcer: OFF")


def print_samurai_phrase(cmd: str):
    phrase = random.choice(SAMURAI_PHRASES)
    print(phrase.format(cmd=cmd))


def run_command(command: List[str]):
    cmd_str = ' '.join(command)
    print_samurai_phrase(cmd_str)
    try:
        result = subprocess.run(command, check=False)
        sys.exit(result.returncode)
    except FileNotFoundError:
        print(f"コマンドが見つかりませぬ: {command[0]}")
        sys.exit(127)
    except Exception as e:
        print(f"拙者、思わぬ事態にござる: {e}")
        sys.exit(1)


def list_phrases():
    print("-- 侍ナレーション一覧 --")
    for p in SAMURAI_PHRASES:
        print(p.format(cmd="<コマンド>"))


def main():
    parser = argparse.ArgumentParser(
        description="ターミナル侍ナレーター: コマンド実行時に侍風実況を挿入するスキル。"
    )
    subparsers = parser.add_subparsers(dest='subcmd')

    parser_on = subparsers.add_parser('on', help='侍ナレーターを有効化')
    parser_off = subparsers.add_parser('off', help='侍ナレーターを無効化')
    parser_list = subparsers.add_parser('list', help='侍ナレーション例を表示')
    parser_run = subparsers.add_parser('run', help='コマンドを侍実況付きで実行')
    parser_run.add_argument('command', nargs=argparse.REMAINDER, help='実行するコマンド')

    args = parser.parse_args()

    if args.subcmd == 'on':
        enable()
    elif args.subcmd == 'off':
        disable()
    elif args.subcmd == 'list':
        list_phrases()
    elif args.subcmd == 'run':
        if not args.command:
            print("実行するコマンドを指定してくだされ！")
            sys.exit(2)
        run_command(args.command)
    else:
        # 暗黙モード: ONならラップして実行
        if is_enabled():
            if len(sys.argv) > 1:
                run_command(sys.argv[1:])
            else:
                parser.print_help()
        else:
            parser.print_help()

if __name__ == '__main__':
    main()
