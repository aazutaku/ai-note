import random
import time
import argparse
import sys
from threading import Thread, Event

try:
    from plyer import notification
except ImportError:
    print("[ERROR] plyer パッケージが必要です。pip install plyer でインストールしてください。", file=sys.stderr)
    sys.exit(1)

VIRUS_NAMES = [
    ("怠惰ウイルス", "Lazivirus", "作業効率を著しく低下させる恐れがあります。", "5分間のストレッチ推奨。"),
    ("残業無限増殖型バグウイルス", "OverworkInfiniteBug", "残業時間が永久に増殖する危険性あり。", "早めの帰宅を強く推奨。"),
    ("コーヒー依存症ウイルス", "CoffeeAddictus", "カフェイン摂取量が危険域に到達する可能性。", "水分補給をお忘れなく。"),
    ("無限リファクタリング病原体", "RefactorLoopus", "終わりなきリファクタリングを誘発します。", "一旦リリースしてみましょう。"),
    ("仕様追加幻覚型ウイルス", "SpecPhantom", "終わりなき仕様追加の幻覚を見せます。", "仕様凍結を宣言してください。"),
    ("会議ループ感染症", "MeetingLoop", "会議が無限ループ化する恐れがあります。", "会議は30分以内に！"),
    ("Slack未読増殖ウイルス", "UnreadSlackus", "未読メッセージが指数関数的に増加します。", "通知をミュートしましょう。"),
    ("タスク増殖型バグ", "TaskMultiplicus", "タスクが自己増殖を始めます。", "TODOリストを整理推奨。"),
    ("昼寝誘発型ウイルス", "NapTrigger", "突発的な眠気を誘発します。", "短い仮眠をどうぞ。"),
    ("納期消失型ウイルス", "DeadlineVanish", "納期が突然消失する現象が発生。", "進捗報告をお忘れなく。")
]

DEFAULT_INTERVAL = 900  # 15分

class VirusAlertRunner:
    def __init__(self, interval=DEFAULT_INTERVAL, once=False, verbose=False):
        self.interval = interval
        self.once = once
        self.verbose = verbose
        self.stop_event = Event()

    def random_alert(self):
        name, code, detail, advice = random.choice(VIRUS_NAMES)
        title = "OSウイルス検出アラート"
        message = f"脅威名: {name} ({code})\n詳細: {detail}\n対策: {advice}"
        if self.verbose:
            print(f"[DEBUG] 通知内容: {message}")
        notification.notify(
            title=title,
            message=message,
            app_name="Fake Virus Detector",
            timeout=10
        )

    def run(self):
        if self.once:
            self.random_alert()
            return
        while not self.stop_event.is_set():
            self.random_alert()
            for _ in range(int(self.interval)):
                if self.stop_event.is_set():
                    break
                time.sleep(1)

    def stop(self):
        self.stop_event.set()


def list_viruses():
    print("利用可能なジョークウイルス一覧:")
    for idx, (name, code, detail, advice) in enumerate(VIRUS_NAMES, 1):
        print(f"{idx}. {name} ({code}) - {detail} 対策: {advice}")


def main():
    parser = argparse.ArgumentParser(description="謎のOSウイルス検出アラートをランダムに通知するジョークスクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="定期的にジョーク通知を表示")
    parser_run.add_argument("-i", "--interval", type=int, default=DEFAULT_INTERVAL, help="通知間隔(秒)")
    parser_run.add_argument("-v", "--verbose", action="store_true", help="詳細なログを表示")
    parser_run.add_argument("--once", action="store_true", help="1回だけ通知して終了")

    parser_list = subparsers.add_parser("list", help="ジョークウイルス一覧を表示")

    args = parser.parse_args()

    if args.command == "list":
        list_viruses()
    elif args.command == "run":
        runner = VirusAlertRunner(interval=args.interval, once=args.once, verbose=args.verbose)
        try:
            runner.run()
        except KeyboardInterrupt:
            print("\n[INFO] 停止しました。")
            runner.stop()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
