import os
import sys
import random
import argparse
import traceback
from glob import glob
try:
    from playsound import playsound
except ImportError:
    print("playsound モジュールが必要です。pip install playsound でインストールしてください。", file=sys.stderr)
    sys.exit(1)

SOUNDS_DIR = os.path.join(os.path.dirname(__file__), 'sounds')
SUPPORTED_FORMATS = ('.wav', '.mp3', '.ogg')

DEFAULT_VOLUME = 1.0  # playsoundは音量調整非対応。pygameやpydub利用時は調整可能。

class JinglePlayer:
    def __init__(self, sounds_dir=SOUNDS_DIR, mute=False, volume=DEFAULT_VOLUME, exclude=None):
        self.sounds_dir = sounds_dir
        self.mute = mute
        self.volume = volume
        self.exclude = exclude if exclude else []
        self.sounds = self._load_sounds()

    def _load_sounds(self):
        files = []
        for ext in SUPPORTED_FORMATS:
            files.extend(glob(os.path.join(self.sounds_dir, f'*{ext}')))
        if not files:
            print(f"警告: サウンドファイルが {self.sounds_dir} に見つかりません。", file=sys.stderr)
        return files

    def play_random(self):
        if self.mute or not self.sounds:
            return
        sound = random.choice(self.sounds)
        print(f"[ジングル再生: {os.path.basename(sound)}]", file=sys.stderr)
        # playsoundは音量調整非対応。pygame等で拡張可。
        try:
            playsound(sound)
        except Exception as e:
            print(f"サウンド再生失敗: {e}", file=sys.stderr)

    def should_exclude(self, exc_type, exc_value, tb):
        for ex in self.exclude:
            if ex.lower() in str(exc_type).lower() or ex.lower() in str(exc_value).lower():
                return True
        return False


def error_jingle_hook(exc_type, exc_value, tb):
    global player
    if player.should_exclude(exc_type, exc_value, tb):
        sys.__excepthook__(exc_type, exc_value, tb)
        return
    player.play_random()
    sys.__excepthook__(exc_type, exc_value, tb)


def parse_args():
    parser = argparse.ArgumentParser(description="コマンド実行時のエラー発生でランダムジングル再生")
    parser.add_argument('--mute', action='store_true', help='ジングルをミュート')
    parser.add_argument('--volume', type=float, default=DEFAULT_VOLUME, help='音量 (0.0-1.0)')
    parser.add_argument('--exclude', nargs='*', default=[], help='除外する例外タイプやキーワード')
    parser.add_argument('--test', action='store_true', help='ジングル再生テスト')
    parser.add_argument('--list', action='store_true', help='利用可能なジングル一覧表示')
    return parser.parse_args()


def main():
    global player
    args = parse_args()
    player = JinglePlayer(mute=args.mute, volume=args.volume, exclude=args.exclude)
    if args.list:
        print("利用可能なジングル:")
        for s in player.sounds:
            print(f"- {os.path.basename(s)}")
        sys.exit(0)
    if args.test:
        player.play_random()
        sys.exit(0)
    sys.excepthook = error_jingle_hook
    print("[random-os-error-jingle] Skill有効化中。例外発生時にジングル再生します。")
    # サンプル: 標準入力からPythonコードを受け取り実行（例外発生でジングル）
    code = ''
    if not sys.stdin.isatty():
        code = sys.stdin.read()
        try:
            exec(code, {})
        except Exception:
            pass  # excepthookでジングル再生
    else:
        print("スクリプト内でimportして利用するか、--testで動作確認できます。")

if __name__ == '__main__':
    main()
