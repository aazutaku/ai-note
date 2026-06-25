import random
import sys
import argparse
import os
import json
import datetime
from plyer import notification

FAKE_FEATURES = [
    "ウィンドウを閉じるときに謎の効果音が鳴ります。",
    "新しいバグ追跡システムが追加されましたが、まだバグがあります。",
    "マウスカーソルが時々消える機能を実装しました。",
    "画面の色がごく稀に変わることがあります。",
    "未使用の設定項目が増えました。",
    "OSの起動音が2倍長くなりました。",
    "通知のフォントがComic Sansに変更されます。",
    "新しいヘルプボタンが追加されましたが、押しても何も起きません。",
    "自動アップデートが手動になります。",
    "エラー音がより不快なものに変更されました。"
]
FAKE_BUGFIXES = [
    "ごく稀にマウスが逆方向に動く問題を未確認で修正。",
    "シャットダウン時に謎の警告が出る問題を修正したつもりです。",
    "一部のウィンドウが勝手に閉じる現象を観察しましたが、放置します。",
    "ログイン画面でパスワードが表示される問題を直したかったです。",
    "時々時計が未来を表示する問題を修正（未検証）。",
    "アップデート通知が1日10回出る問題を倍増させました。",
    "通知が消えない問題を解決しませんでした。",
    "設定画面でクラッシュする問題を追加しました。",
    "音量調整ができない問題を新たに発見しました。",
    "スクリーンショットが真っ黒になる問題を放置しました。"
]
FAKE_KNOWN_ISSUES = [
    "画面が突然ピンク色になることがありますが仕様です。",
    "再起動すると全て元に戻ります（たぶん）。",
    "一部のユーザーで不具合が再発する可能性があります。",
    "ヘルプが英語しか表示されません。",
    "通知が重複して表示されることがあります。",
    "アップデート後にパフォーマンスが低下する場合があります。",
    "ごく稀にOSが自動的に再起動します。",
    "設定が保存されないことがあります。",
    "一部の機能が説明通りに動作しません。",
    "アップデート履歴が消えることがあります。"
]

NOTIFICATION_TITLE = "OS Update Notifier"
FAKE_URL_BASE = "https://os.fakeupdates.example.com/notes/"
LOG_FILE = os.path.expanduser("~/.random_os_fake_update_notifier.log")


def generate_fake_update():
    feature = random.choice(FAKE_FEATURES)
    bugfix = random.choice(FAKE_BUGFIXES)
    issue = random.choice(FAKE_KNOWN_ISSUES)
    date_str = datetime.datetime.now().strftime("%Y.%m.%d")
    url = f"{FAKE_URL_BASE}{date_str}"
    message = f"新機能: {feature}\nバグ修正: {bugfix}\n既知の問題: {issue}\n詳細: {url}"
    return {
        "date": date_str,
        "feature": feature,
        "bugfix": bugfix,
        "issue": issue,
        "url": url,
        "message": message
    }


def show_notification(message):
    try:
        notification.notify(
            title=NOTIFICATION_TITLE,
            message=message,
            app_name="Random OS Fake Update Notifier",
            timeout=10
        )
    except Exception as e:
        print(f"[Error] 通知の表示に失敗: {e}")


def log_update(update):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "update": update
    }
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"[Error] ログ書き込み失敗: {e}")


def list_logs(limit=10):
    if not os.path.exists(LOG_FILE):
        print("ログファイルが存在しません。")
        return
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()[-limit:]
            for line in lines:
                try:
                    entry = json.loads(line)
                    print(f"[{entry['timestamp']}] {entry['update']['message']}")
                except Exception:
                    continue
    except Exception as e:
        print(f"[Error] ログ読み込み失敗: {e}")


def summary_logs():
    features = set()
    bugfixes = set()
    issues = set()
    count = 0
    if not os.path.exists(LOG_FILE):
        print("ログファイルが存在しません。")
        return
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    features.add(entry['update']['feature'])
                    bugfixes.add(entry['update']['bugfix'])
                    issues.add(entry['update']['issue'])
                    count += 1
                except Exception:
                    continue
        print(f"== ログサマリー ==")
        print(f"通知回数: {count}")
        print(f"ユニーク新機能: {len(features)} 個")
        print(f"ユニークバグ修正: {len(bugfixes)} 個")
        print(f"ユニーク既知の問題: {len(issues)} 個")
    except Exception as e:
        print(f"[Error] サマリー集計失敗: {e}")


def main():
    parser = argparse.ArgumentParser(description="Random OS Fake Update Notifier")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser("log", help="ランダムな偽アップデート通知を生成・表示・記録")
    parser_list = subparsers.add_parser("list", help="過去の通知ログを表示")
    parser_list.add_argument("--limit", type=int, default=10, help="表示する最新ログ件数")
    parser_summary = subparsers.add_parser("summary", help="通知ログのサマリーを表示")

    args = parser.parse_args()

    if args.command == "log" or args.command is None:
        update = generate_fake_update()
        show_notification(update["message"])
        log_update(update)
        print(update["message"])
    elif args.command == "list":
        list_logs(limit=args.limit)
    elif args.command == "summary":
        summary_logs()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
