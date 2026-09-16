import random
import sys
import argparse
import os
import platform
import time

try:
    import notify2
except ImportError:
    notify2 = None

try:
    from plyer import notification as plyer_notify
except ImportError:
    plyer_notify = None

FAKE_PATCH_TITLES = [
    "Fake Patch Tuesday Alert",
    "緊急OSアップデート通知",
    "Patch Tuesday (非公式)",
    "OS公式: パッチノート速報",
    "アップデート情報: 本日限定",
]

FAKE_PATCH_NOTES = [
    "本日、Ctrlキーの押下速度が基準値未満のため、緊急アップデートが適用されます。",
    "新機能: Altキー長押しでOSが詩を朗読",
    "既知の問題: エスケープキーの連打で画面が逆立ちします",
    "重要: 次回再起動時にCapsLockが自動解除されます",
    "セキュリティ: Shiftキーの同時押しが検出されたため、全ウィンドウが半透明になります",
    "パフォーマンス向上: F1キーを押すとサポート担当者が画面に現れます",
    "新機能: PrintScreenで画面全体がモザイク化",
    "修正: タブキーを押すとタブ譜が自動生成される問題を解消",
    "アップデート: NumLockがONの間、数字キーがランダムに並び替えられます",
    "推奨: OSが自動で毎週火曜日に詩的な通知を送信します",
    "既知の問題: スペースキー長押しでOSが沈黙状態に入ります",
    "新機能: マウスの右クリックで天気予報が表示されます",
    "修正: ウィンドウが重力に従って落下する現象を一時的に無効化",
    "重要: CapsLockキーが押されるたびに画面が反転します",
    "アップデート: スクリーンセーバーが定期的にOSジョークを表示",
    "新機能: Alt+F4でOSが自己紹介を始めます",
    "既知の問題: マウスカーソルが画面外に出ると迷子になります",
    "修正: Enterキー連打でOSが拍手する機能を追加",
    "アップデート: Ctrl+Zで現実世界のやり直しを試みます",
    "新機能: スクロールロックONで画面が縦書き表示に変化",
]

EXTRA_NOTES = [
    "再起動は不要です。",
    "この通知は自動的に消えます。",
    "詳細は管理者にお問い合わせください。",
    "本通知は冗談です。",
    "アップデート内容は予告なく変更される場合があります。",
]


def generate_fake_patch():
    title = random.choice(FAKE_PATCH_TITLES)
    notes = random.sample(FAKE_PATCH_NOTES, k=random.randint(2, 4))
    extra = random.choice(EXTRA_NOTES)
    body = "\n- ".join([notes[0]] + notes[1:])
    return title, f"{body}\n- {extra}"


def notify_desktop(title, message):
    sys_platform = platform.system()
    if sys_platform == "Linux" and notify2:
        try:
            notify2.init("Fake Patch Tuesday")
            n = notify2.Notification(title, message)
            n.set_timeout(7000)
            n.show()
        except Exception as e:
            print(f"[通知エラー] {e}")
    elif sys_platform == "Darwin":
        # macOS: osascript
        try:
            os.system(f"osascript -e 'display notification \"{message}\" with title \"{title}\"'")
        except Exception as e:
            print(f"[通知エラー] {e}")
    elif sys_platform == "Windows" and plyer_notify:
        try:
            plyer_notify.notify(title=title, message=message, timeout=7)
        except Exception as e:
            print(f"[通知エラー] {e}")
    else:
        print(f"[通知未対応] {title}: {message}")


def print_terminal(title, message):
    border = "=" * (len(title) + 8)
    print(f"\n{border}\n  [ {title} ]\n{border}\n{message}\n{border}\n")


def parse_args():
    parser = argparse.ArgumentParser(description="Random OS Fake Patch Tuesday Alert")
    parser.add_argument('--mode', choices=['desktop', 'terminal', 'both'], default='both',
                        help='通知方法 (desktop/terminal/both)')
    parser.add_argument('--count', type=int, default=1, help='通知回数 (デフォルト:1)')
    parser.add_argument('--interval', type=float, default=0.0, help='通知間隔(秒)')
    parser.add_argument('command', nargs='?', choices=['log', 'list', 'summary'], default=None,
                        help='サブコマンド (未指定で即通知)')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'log':
        print("[Fake Patch Tuesday Alert] 通知履歴は保存されません。")
        return
    elif args.command == 'list':
        print("[Fake Patch Tuesday Alert] 既定のパッチノート例:")
        for note in FAKE_PATCH_NOTES:
            print(f"- {note}")
        return
    elif args.command == 'summary':
        print("[Fake Patch Tuesday Alert] このスキルは完全ジョーク仕様です。通知内容は毎回ランダム生成されます。")
        return
    for i in range(args.count):
        title, message = generate_fake_patch()
        if args.mode in ('desktop', 'both'):
            notify_desktop(title, message)
        if args.mode in ('terminal', 'both'):
            print_terminal(title, message)
        if i < args.count - 1:
            time.sleep(args.interval)

if __name__ == '__main__':
    main()
