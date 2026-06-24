import argparse
import os
import random
import sys
import subprocess
import threading
import time
from pathlib import Path

try:
    from playsound import playsound
except ImportError:
    print("playsoundモジュールが必要です。pip install playsound でインストールしてください。", file=sys.stderr)
    sys.exit(1)

JINGLE_DIR = Path(__file__).parent / "jingles"
SUPPORTED_EXTS = [".wav", ".mp3", ".ogg"]
DEFAULT_VOLUME = 1.0

try:
    import sounddevice as sd
    import soundfile as sf
    HAVE_SOUNDDEVICE = True
except ImportError:
    HAVE_SOUNDDEVICE = False

def list_jingles():
    if not JINGLE_DIR.exists():
        print("ジングルディレクトリが存在しません: {}".format(JINGLE_DIR))
        return
    files = [f.name for f in JINGLE_DIR.iterdir() if f.suffix.lower() in SUPPORTED_EXTS]
    if not files:
        print("ジングル音源がありません。{} にWAVやMP3ファイルを追加してください。".format(JINGLE_DIR))
        return
    print("登録ジングル:")
    for f in files:
        print("- {}".format(f))

def pick_random_jingle():
    if not JINGLE_DIR.exists():
        return None
    files = [f for f in JINGLE_DIR.iterdir() if f.suffix.lower() in SUPPORTED_EXTS]
    if not files:
        return None
    return random.choice(files)

def play_jingle(jingle_path, volume=1.0, mute=False):
    if mute or not jingle_path:
        return
    if HAVE_SOUNDDEVICE and jingle_path.suffix.lower() in [".wav", ".ogg"]:
        try:
            data, fs = sf.read(str(jingle_path), dtype='float32')
            sd.play(data * volume, fs)
            sd.wait()
            return
        except Exception as e:
            print(f"sounddevice再生失敗: {e}")
    try:
        # playsoundは音量制御不可
        playsound(str(jingle_path))
    except Exception as e:
        print(f"playsound再生失敗: {e}")

def run_command_with_jingle(cmd, volume=1.0, mute=False):
    try:
        completed = subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        jingle = pick_random_jingle()
        print(f"[エラー] コマンド失敗: {e}")
        play_jingle(jingle, volume, mute)
        sys.exit(e.returncode)
    except Exception as e:
        jingle = pick_random_jingle()
        print(f"[例外] {e}")
        play_jingle(jingle, volume, mute)
        sys.exit(1)

def test_jingle(volume=1.0, mute=False):
    jingle = pick_random_jingle()
    if not jingle:
        print("ジングル音源がありません。")
        return
    print(f"テスト再生: {jingle.name}")
    play_jingle(jingle, volume, mute)

def main():
    parser = argparse.ArgumentParser(description="コマンド失敗時にランダムジングルを再生するスクリプト")
    subparsers = parser.add_subparsers(dest='subcmd')

    parser_run = subparsers.add_parser('run', help='コマンドを実行し、失敗時にジングル再生')
    parser_run.add_argument('cmd', nargs=argparse.REMAINDER, help='実行するコマンド')
    parser_run.add_argument('--volume', type=float, default=DEFAULT_VOLUME, help='音量(0.0-1.0)')
    parser_run.add_argument('--mute', action='store_true', help='ジングルを鳴らさない')

    parser_list = subparsers.add_parser('list', help='ジングル一覧表示')

    parser_test = subparsers.add_parser('test', help='ジングルのテスト再生')
    parser_test.add_argument('--volume', type=float, default=DEFAULT_VOLUME, help='音量(0.0-1.0)')
    parser_test.add_argument('--mute', action='store_true', help='ジングルを鳴らさない')

    args = parser.parse_args()

    if args.subcmd == 'list':
        list_jingles()
    elif args.subcmd == 'test':
        test_jingle(volume=args.volume, mute=args.mute)
    elif args.subcmd == 'run':
        if not args.cmd:
            print("runサブコマンドにはコマンドを指定してください。例: run ls /not/exist")
            sys.exit(1)
        run_command_with_jingle(' '.join(args.cmd), volume=args.volume, mute=args.mute)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
