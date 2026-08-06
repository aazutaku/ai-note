import random
import sys
import argparse
import time
import threading
try:
    from plyer import notification
except ImportError:
    notification = None

THEME_PREFIXES = [
    '本日のテーマソング',
    '今こそ流せ！',
    '推奨BGM',
    '公式サウンド',
    'システム推奨BGM',
    '緊急推薦',
    '今週の推し曲',
    '開発現場のBGM',
    'OS公式テーマ',
    '隠しトラック',
]

SONG_TITLES = [
    'バグ修羅場行進曲',
    '納期デッドヒート',
    '仕様書迷宮のワルツ',
    'デバッグ無限ループ',
    'コミット前夜のバラード',
    'マージ地獄のカノン',
    'ビルド失敗のエチュード',
    'レビュー嵐のラプソディ',
    'テスト地帯のロンド',
    'リリース前夜のノクターン',
    'バージョン地獄のサンバ',
    'リファクタリング幻想曲',
    '仕様追加のパラフレーズ',
    'CI/CDのトッカータ',
    'スタックオーバーフロー賛歌',
    'エラー地帯のセレナーデ',
    '会議無限リピート',
    'ドキュメント難民のブルース',
    'ペアプロのカプリチオ',
    '要件定義の夜想曲',
]

SUBTITLES = [
    '',
    '〜終わらないSprint〜',
    '（feat. 仕様変更）',
    '【緊急リリースver.】',
    '（デスマーチ編）',
    '〜眠れぬ夜に〜',
    '（バグフィックスRemix）',
    '【再起動不可】',
    '（仮）',
    '〜伝説のバグ〜',
    '（未実装）',
    '【無限ループMix】',
    '（会議室Live）',
    '〜エラーの海〜',
    '（仕様未定）',
]

NOTIFY_INTERVAL = 900  # 15分ごと

class SoundtrackAlert:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run or (notification is None)

    def random_message(self):
        prefix = random.choice(THEME_PREFIXES)
        title = random.choice(SONG_TITLES)
        subtitle = random.choice(SUBTITLES)
        msg = f"{prefix}：『{title}』"
        if subtitle:
            msg += f"{subtitle}"
        return msg

    def notify(self, message):
        if self.dry_run:
            print(f"[通知] {message}")
        else:
            try:
                notification.notify(
                    title="OS公式サウンドトラック通知",
                    message=message,
                    timeout=6
                )
            except Exception as e:
                print(f"[通知失敗] {message} ({e})")

    def run_once(self):
        msg = self.random_message()
        self.notify(msg)

    def run_loop(self, interval=NOTIFY_INTERVAL, count=None):
        i = 0
        try:
            while True:
                if count is not None and i >= count:
                    break
                self.run_once()
                i += 1
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n[終了] サウンドトラック通知ループを終了しました。")

    def list_samples(self, n=10):
        samples = set()
        while len(samples) < n:
            samples.add(self.random_message())
        for s in samples:
            print(f"[通知サンプル] {s}")


def main():
    parser = argparse.ArgumentParser(
        description="謎のOS公式サウンドトラック通知を表示するジョークスクリプト。音は流れません。"
    )
    subparsers = parser.add_subparsers(dest="command")

    parser_once = subparsers.add_parser("once", help="1回だけ通知を表示")
    parser_loop = subparsers.add_parser("loop", help="定期的に通知を表示")
    parser_loop.add_argument("-i", "--interval", type=int, default=NOTIFY_INTERVAL, help="通知間隔(秒)")
    parser_loop.add_argument("-n", "--count", type=int, default=None, help="通知回数(省略時は無限)")
    parser_sample = subparsers.add_parser("sample", help="通知サンプルを複数表示")
    parser_sample.add_argument("-n", type=int, default=10, help="サンプル数")
    parser.add_argument("--dry-run", action="store_true", help="実際の通知を出さずprintする")

    args = parser.parse_args()
    alert = SoundtrackAlert(dry_run=args.dry_run)

    if args.command == "once":
        alert.run_once()
    elif args.command == "loop":
        alert.run_loop(interval=args.interval, count=args.count)
    elif args.command == "sample":
        alert.list_samples(n=args.n)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
