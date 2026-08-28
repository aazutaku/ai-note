import random
import sys
import time
import argparse
import platform

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

# ランダムな環境音テーマ
AMBIENT_THEMES = [
    "森のさざめきBGM",
    "カフェ騒音",
    "砂浜の波音",
    "宇宙船エンジン音",
    "雨の音",
    "図書館の静けさ",
    "地下鉄ホーム",
    "焚き火のパチパチ音",
    "オフィスのざわめき",
    "鳥のさえずり",
    "深夜のサーバールーム",
    "山小屋の暖炉音",
    "都市の夜景BGM",
    "古いPCファンノイズ",
    "謎の電子音",
    "遠くの雷鳴",
    "水族館の水音",
    "キャンプ場の虫の声",
    "未来都市の環境音",
    "静かな書斎"
]

# 通知メッセージテンプレート
TEMPLATES = [
    "本日は集中力向上のため、{theme}を自動再生します（実際には再生されません）",
    "OS公式: 今から15分間は謎の{theme}推奨。耳を澄ませてみましょう。",
    "システム推奨: {theme}モードに切り替えます。ごゆっくりお過ごしください。",
    "本日は“{theme}”BGMが選ばれました。静かなひとときをお楽しみください。",
    "[通知] ご注意: 本通知は演出のみで、実際の音は鳴りません。",
    "[OS通知] {theme}をバックグラウンドで再生中（フェイク）",
    "[公式] {theme}の効果で集中力が1.2倍（当社比）",
    "[システム] {theme}環境音を推奨します。設定変更は不要です。",
    "[通知] {theme}BGMをONにしました（気分だけ）",
    "[OS] {theme}が有効になりました。"
]

# 通知を表示する関数
def show_notification(message):
    if PLYER_AVAILABLE:
        try:
            notification.notify(
                title="OS通知",
                message=message,
                timeout=8
            )
        except Exception as e:
            print(f"[通知エラー] {e}")
    else:
        print(f"[OS通知] {message}")

# 通知メッセージをランダム生成
def generate_notification():
    theme = random.choice(AMBIENT_THEMES)
    template = random.choice(TEMPLATES)
    return template.format(theme=theme)

# 通知履歴を管理（今回はメモリのみ）
class NotificationHistory:
    def __init__(self):
        self.entries = []
    def log(self, message, timestamp=None):
        if timestamp is None:
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.entries.append((timestamp, message))
    def list(self, count=10):
        return self.entries[-count:]
    def summary(self):
        themes = [msg for _, msg in self.entries]
        return f"通知回数: {len(themes)}"

# 通知発動ロジック
def notify_once(history):
    msg = generate_notification()
    show_notification(msg)
    history.log(msg)

# 一定間隔で通知（うるさすぎないよう制御）
def notify_loop(history, interval_min=25, interval_max=90, max_count=5):
    count = 0
    while count < max_count:
        notify_once(history)
        count += 1
        sleep_time = random.randint(interval_min, interval_max)
        time.sleep(sleep_time)

# CLIサブコマンド
def main():
    parser = argparse.ArgumentParser(description="OSフェイク環境音通知スキル")
    subparsers = parser.add_subparsers(dest="command")

    parser_notify = subparsers.add_parser("notify", help="即時フェイク通知を1回表示")
    parser_loop = subparsers.add_parser("loop", help="定期的にフェイク通知を表示")
    parser_loop.add_argument("--min", type=int, default=25, help="通知間隔(秒)の最小値")
    parser_loop.add_argument("--max", type=int, default=90, help="通知間隔(秒)の最大値")
    parser_loop.add_argument("--count", type=int, default=5, help="通知回数の上限")
    parser_list = subparsers.add_parser("list", help="通知履歴を表示")
    parser_summary = subparsers.add_parser("summary", help="通知履歴のサマリを表示")

    args = parser.parse_args()
    history = NotificationHistory()

    if args.command == "notify":
        notify_once(history)
    elif args.command == "loop":
        notify_loop(history, args.min, args.max, args.count)
    elif args.command == "list":
        for ts, msg in history.list():
            print(f"[{ts}] {msg}")
    elif args.command == "summary":
        print(history.summary())
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
