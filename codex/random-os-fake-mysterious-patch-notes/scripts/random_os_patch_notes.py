import random
import argparse
import datetime
import sys
import os

PATCH_NOTES_TEMPLATES = [
    {
        "new_features": [
            "Altキーで未来の天気予報が見えるようになりました",
            "ターミナルで『echo hello』で虹色の猫が出現",
            "Ctrl+Shift+Zで開発者モードが一瞬だけ有効になります",
            "システム通知が詩的な言葉で表示されるようになりました",
            "右クリックで過去の自分にメッセージを送信可能になりました",
            "CapsLock2.0: 2回押しで小文字に戻せます",
            "新しい壁紙『謎の宇宙』を追加しました",
            "F1キーでAIが人生相談に乗ってくれます",
            "時計アプリが3秒進むことがあります",
            "バッテリー残量が気分で増減します"
        ],
        "improvements": [
            "スペースキーの跳躍力を微増",
            "CapsLockの押下音が静かに",
            "ウィンドウの角が丸くなりました",
            "タスクバーの色がランダムに変化",
            "ファイル検索速度が気持ち速くなりました",
            "ログイン画面のBGMが優しくなりました",
            "マウスカーソルの滑らかさを改善",
            "スクリーンショットの画質が謎に向上",
            "エラーメッセージのフォントが美しく",
            "設定画面のアイコンが少し大きく"
        ],
        "known_issues": [
            "たまに幸運が訪れます",
            "ごく稀に時間が逆行することがあります",
            "システムが月曜日を認識しなくなる不具合",
            "設定画面が哲学的な質問を投げてくる場合があります",
            "ファイル名が詩的になることがあります",
            "バッテリー残量がマイナス表示になる場合あり",
            "スクリーンセーバーが止まらないことがあります",
            "音量調整が気まぐれに効かなくなることがあります",
            "クリップボードの中身が謎の暗号になることがあります",
            "ウィンドウが踊りだすことがあります"
        ],
        "fixes": [
            "システムが月曜日を認識しなくなる不具合を修正",
            "ファイル検索で未来のファイルが表示される問題を修正",
            "一部環境で時計が止まる問題を修正",
            "CapsLockが永遠にONになる問題を修正",
            "ターミナルが詩を詠むバグを修正",
            "ウィンドウが画面外に消える問題を修正",
            "音量バーが逆向きになる問題を修正",
            "ログイン画面が無限ループする問題を修正",
            "通知が5分遅れて届く問題を修正",
            "壁紙が深夜に変わる問題を修正"
        ]
    }
]

HISTORY_FILE = os.path.expanduser("~/.random_os_patch_notes_history")


def generate_patch_note():
    template = random.choice(PATCH_NOTES_TEMPLATES)
    version = f"{random.randint(10, 15)}.{random.randint(0, 9)}.{random.randint(0, 99)}"
    new_feature = random.choice(template["new_features"])
    improvement = random.choice(template["improvements"])
    known_issue = random.choice(template["known_issues"])
    fix = random.choice(template["fixes"])
    note = f"[OS Patch Notes v{version}]\n新機能: {new_feature}\n改善: {improvement}\n既知の問題: {known_issue}\n修正: {fix}"
    return note


def save_to_history(note):
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now().isoformat()}\n{note}\n---\n")
    except Exception as e:
        print(f"[WARN] 履歴保存に失敗: {e}", file=sys.stderr)


def list_history(limit=5):
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。", file=sys.stderr)
        return
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            lines = f.read().split("---\n")
            notes = [l.strip() for l in lines if l.strip()]
            for note in notes[-limit:]:
                print(note)
                print("---")
    except Exception as e:
        print(f"[ERROR] 履歴の読み込みに失敗: {e}", file=sys.stderr)


def summary_history():
    if not os.path.exists(HISTORY_FILE):
        print("履歴がありません。", file=sys.stderr)
        return
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            count = content.count("[OS Patch Notes v")
            print(f"これまでに生成されたパッチノート数: {count}")
    except Exception as e:
        print(f"[ERROR] サマリー取得に失敗: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="謎のOSパッチノートをランダム生成・履歴管理")
    subparsers = parser.add_subparsers(dest="command", required=False)

    parser_log = subparsers.add_parser("log", help="新しいパッチノートを生成し表示")
    parser_list = subparsers.add_parser("list", help="履歴から直近のパッチノートを表示")
    parser_list.add_argument("-n", type=int, default=5, help="表示件数 (デフォルト5)")
    parser_summary = subparsers.add_parser("summary", help="履歴のサマリーを表示")

    args = parser.parse_args()
    if args.command == "log" or args.command is None:
        note = generate_patch_note()
        print(note)
        save_to_history(note)
    elif args.command == "list":
        list_history(args.n)
    elif args.command == "summary":
        summary_history()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
