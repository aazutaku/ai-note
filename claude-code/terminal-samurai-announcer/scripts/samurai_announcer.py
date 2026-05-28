import os
import sys
import argparse
import random
import subprocess
import json
from pathlib import Path

SAMURAI_LINES = {
    'ls': [
        '拙者、lsを実行仕る！',
        'お主のファイル、拝見致す！',
        'この場所、見事なり！',
        '目にも止まらぬlsの術！'
    ],
    'git': [
        'このcommit、見事なり！',
        '拙者、gitの流儀にて参る！',
        'おお、branchを吟味致す！',
        'git statusを見届け申す！'
    ],
    'vim': [
        '拙者、vimの道を極めん！',
        'いざ、編集の陣！',
        'この一太刀、vimにて！',
        '書き換え、見事に成し遂げ申した！'
    ],
    'cd': [
        '拙者、新天地へ移動仕る！',
        'この道、通らせて頂く！',
        'cdの術、抜かりなし！'
    ],
    'mkdir': [
        '新たな陣地を築き申す！',
        'mkdir、見事なり！',
        '拙者、領地拡張の構え！'
    ],
    'rm': [
        '拙者、容赦なくrm致す！',
        'このファイル、成敗！',
        'rmの太刀、冴え渡る！'
    ],
    'cp': [
        '拙者、cpにて写し取る！',
        'この写し、見事なり！',
        'cpの術、抜かりなし！'
    ],
    'mv': [
        '拙者、mvにて移動仕る！',
        'この移動、迅速に！',
        'mvの構え、見事なり！'
    ],
    'cat': [
        'おお、catにて内容を吟味致す！',
        '拙者、catの流儀を見せ申す！',
        '内容、隅々まで見届け申す！'
    ],
    'touch': [
        '新しきファイル、ここに誕生！',
        'touchの一撃、決まったり！',
        '拙者、touchにて道を開く！'
    ],
    'python': [
        '拙者、pythonの術を披露致す！',
        'この実行、見事なり！',
        'pythonの力、侮るなかれ！'
    ],
    'pip': [
        '拙者、pipにて道具を揃え申す！',
        'pip install、抜かりなし！',
        '道具、pipにて調達致す！'
    ],
    'docker': [
        '拙者、dockerの海原へ漕ぎ出す！',
        'docker run、いざ参る！',
        'このコンテナ、見事なり！'
    ],
    'default': [
        '拙者、{cmd}を実行仕る！',
        'この{cmd}、見事なり！',
        '{cmd}の構え、抜かりなし！',
        'いざ、{cmd}の術！'
    ]
}

CONFIG_PATH = Path.home() / '.samurai_announcer_config.json'

EXCLUDE_PATHS = ['.git', 'node_modules', '__pycache__']


def load_config():
    if CONFIG_PATH.exists():
        try:
            with open(CONFIG_PATH, 'r') as f:
                return json.load(f)
        except Exception:
            return {'enabled': True}
    return {'enabled': True}

def save_config(cfg):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(cfg, f)

def is_excluded():
    cwd = os.getcwd()
    for excl in EXCLUDE_PATHS:
        if excl in cwd:
            return True
    return False

def get_samurai_line(cmd):
    key = cmd.split()[0] if cmd.split() else 'default'
    lines = SAMURAI_LINES.get(key, SAMURAI_LINES['default'])
    line = random.choice(lines)
    return line.format(cmd=cmd)

def run_command_with_samurai(cmd_args):
    cmd_str = ' '.join(cmd_args)
    if is_excluded():
        subprocess.run(cmd_args)
        return
    line = get_samurai_line(cmd_args[0])
    print(line)
    try:
        result = subprocess.run(cmd_args, check=False)
        if result.returncode == 0:
            print('拙者の任務、完了仕った！')
        else:
            print('無念、失敗に終わり申した…')
    except Exception as e:
        print(f'拙者、痛恨のエラーに見舞われ申した: {e}')

def main():
    parser = argparse.ArgumentParser(description='terminal-samurai-announcer: コマンド実行時に侍ナレーションを添える')
    subparsers = parser.add_subparsers(dest='subcmd')

    parser_run = subparsers.add_parser('run', help='コマンドを侍風に実行')
    parser_run.add_argument('cmd', nargs=argparse.REMAINDER)

    parser_on = subparsers.add_parser('on', help='侍ナレーションを有効化')
    parser_off = subparsers.add_parser('off', help='侍ナレーションを無効化')
    parser_status = subparsers.add_parser('status', help='現在の有効/無効状態を表示')
    parser_list = subparsers.add_parser('list', help='侍セリフ一覧を表示')
    parser_list.add_argument('--cmd', default=None, help='特定コマンドのセリフのみ')

    args = parser.parse_args()
    cfg = load_config()

    if args.subcmd == 'on':
        cfg['enabled'] = True
        save_config(cfg)
        print('侍ナレーション、ここに復活！')
    elif args.subcmd == 'off':
        cfg['enabled'] = False
        save_config(cfg)
        print('侍、しばし隠遁致す…')
    elif args.subcmd == 'status':
        print('侍ナレーション:', '有効' if cfg.get('enabled', True) else '無効')
    elif args.subcmd == 'list':
        if args.cmd:
            lines = SAMURAI_LINES.get(args.cmd, [])
            if not lines:
                print(f'{args.cmd}用の侍セリフは未登録です')
            else:
                for l in lines:
                    print(l)
        else:
            for k, v in SAMURAI_LINES.items():
                print(f'[{k}]')
                for l in v:
                    print('  ', l)
    elif args.subcmd == 'run':
        if not args.cmd:
            print('コマンドを指定してください')
            sys.exit(1)
        if not cfg.get('enabled', True):
            subprocess.run(args.cmd)
        else:
            run_command_with_samurai(args.cmd)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
