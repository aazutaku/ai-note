import argparse
import os
import sys
import random
import glob
import subprocess
import threading
import time

try:
    from playsound import playsound
except ImportError:
    playsound = None
    
def list_jingles(jingle_dir):
    exts = ('*.wav', '*.mp3', '*.ogg')
    files = []
    for ext in exts:
        files.extend(glob.glob(os.path.join(jingle_dir, ext)))
    return files

def play_jingle(jingle_file, volume=1.0, mute=False):
    if mute or not jingle_file:
        return
    if playsound:
        try:
            playsound(jingle_file)
        except Exception as e:
            print(f'[WARN] サウンド再生失敗: {e}', file=sys.stderr)
    else:
        # OS標準の再生コマンド
        if sys.platform.startswith('darwin'):
            os.system(f'afplay "{jingle_file}"')
        elif sys.platform.startswith('linux'):
            os.system(f'paplay "{jingle_file}" || aplay "{jingle_file}"')
        elif sys.platform.startswith('win'):
            import winsound
            try:
                winsound.PlaySound(jingle_file, winsound.SND_FILENAME)
            except Exception as e:
                print(f'[WARN] サウンド再生失敗: {e}', file=sys.stderr)
        else:
            print('[WARN] サウンド再生方法が不明なOSです', file=sys.stderr)

def run_command(cmd, jingle_dir, volume=1.0, mute=False):
    print(f'[INFO] 実行: {cmd}')
    try:
        proc = subprocess.run(cmd, shell=True)
        if proc.returncode != 0:
            print(f'[ERROR] コマンドが失敗しました (終了コード: {proc.returncode})')
            jingles = list_jingles(jingle_dir)
            if not jingles:
                print('[WARN] ジングルファイルが見つかりません', file=sys.stderr)
                return
            jingle_file = random.choice(jingles)
            print(f'[INFO] ジングル再生: {jingle_file}')
            t = threading.Thread(target=play_jingle, args=(jingle_file, volume, mute))
            t.start()
            t.join()
        else:
            print('[INFO] コマンドは正常終了しました')
    except Exception as e:
        print(f'[ERROR] 例外発生: {e}', file=sys.stderr)
        jingles = list_jingles(jingle_dir)
        if not jingles:
            print('[WARN] ジングルファイルが見つかりません', file=sys.stderr)
            return
        jingle_file = random.choice(jingles)
        print(f'[INFO] ジングル再生: {jingle_file}')
        t = threading.Thread(target=play_jingle, args=(jingle_file, volume, mute))
        t.start()
        t.join()

def list_jingle_files(jingle_dir):
    jingles = list_jingles(jingle_dir)
    if not jingles:
        print('[INFO] ジングルファイルが見つかりません')
        return
    print('[INFO] 利用可能なジングル一覧:')
    for j in jingles:
        print('  -', j)

def main():
    parser = argparse.ArgumentParser(description='コマンド失敗時にランダムなOSエラージングルを再生するスキル')
    subparsers = parser.add_subparsers(dest='subcmd')

    parser_run = subparsers.add_parser('run', help='コマンドを実行し、失敗時にジングル再生')
    parser_run.add_argument('--cmd', required=True, help='実行するコマンド')
    parser_run.add_argument('--jingles', required=True, help='ジングル音源ディレクトリ')
    parser_run.add_argument('--volume', type=float, default=1.0, help='音量(0.0-1.0)')
    parser_run.add_argument('--mute', action='store_true', help='サウンドをミュート')

    parser_list = subparsers.add_parser('list', help='利用可能なジングルファイル一覧表示')
    parser_list.add_argument('--jingles', required=True, help='ジングル音源ディレクトリ')

    args = parser.parse_args()

    if args.subcmd == 'run':
        run_command(args.cmd, args.jingles, args.volume, args.mute)
    elif args.subcmd == 'list':
        list_jingle_files(args.jingles)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
