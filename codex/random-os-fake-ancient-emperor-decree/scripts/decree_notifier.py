import sys
import random
import platform
import subprocess
import argparse
import time
from typing import List

# 古代皇帝の勅令テンプレート集
decrees = [
    "皇帝より勅令：本日よりCapsLockの使用を禁ず。",
    "御前会議：スペースキーの叛逆を鎮圧せよ。",
    "帝国情報局：ファイル名に空白を用いる者は全員尋問せよ。",
    "皇帝の意志：本日以降、Tabキーは三度押すべし。",
    "勅令：スクリーンショットは一日一回に制限する。",
    "皇帝より通達：パスワードの記憶は記憶力の試練と心得よ。",
    "御前会議：再起動の儀式は満月の夜に執り行うべし。",
    "帝国法務局：ファイル拡張子の省略は反逆罪と見なす。",
    "皇帝の命：本日よりBackspaceの連打は禁止する。",
    "勅令：バックスラッシュの乱用を厳に慎むこと。",
    "皇帝より勅令：プリンターの紙詰まりは神託である。",
    "御前会議：USBメモリの無断抜去を厳罰に処す。",
    "帝国情報局：Wi-Fi名に皇帝の名を冠すること。",
    "皇帝の意志：マウスは右手で持つべし。",
    "勅令：スクリーンセーバーは皇帝の肖像画に限る。",
    "皇帝より通達：.DS_Storeの出現は吉兆とせよ。",
    "御前会議：エラー音は三度鳴らすこと。",
    "帝国法務局：ファイル名に絵文字を使う者は尋問対象とする。",
    "皇帝の命：本日以降、Altキーは左手のみで押すべし。",
    "勅令：ターミナルの色は皇帝の好みに従うこと。"
]


def select_random_decree() -> str:
    return random.choice(decrees)


def notify_decree(decree: str):
    os_name = platform.system()
    try:
        if os_name == "Linux":
            # Linux: notify-send
            subprocess.run(["notify-send", decree], check=True)
        elif os_name == "Darwin":
            # macOS: osascript
            script = f'display notification "{decree}" with title "皇帝の勅令"'
            subprocess.run(["osascript", "-e", script], check=True)
        elif os_name == "Windows":
            # Windows: powershell toast notification
            # PowerShellスクリプトを直接呼ぶ
            ps_script = f'[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null;'
            ps_script += f'$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02);'
            ps_script += f'$template.GetElementsByTagName("text")[0].AppendChild($template.CreateTextNode("皇帝の勅令")) > $null;'
            ps_script += f'$template.GetElementsByTagName("text")[1].AppendChild($template.CreateTextNode("{decree}")) > $null;'
            ps_script += f'$toast = [Windows.UI.Notifications.ToastNotification]::new($template);'
            ps_script += f'$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("EmperorDecree");'
            ps_script += f'$notifier.Show($toast);'
            subprocess.run(["powershell", "-Command", ps_script], check=True)
        else:
            print(f"[皇帝の勅令] {decree}")
    except Exception as e:
        print(f"[皇帝の勅令] {decree} (通知失敗: {e})")


def list_decrees():
    print("--- 皇帝の勅令テンプレート一覧 ---")
    for i, d in enumerate(decrees, 1):
        print(f"{i}. {d}")


def notify_loop(interval: int, count: int):
    for i in range(count):
        decree = select_random_decree()
        notify_decree(decree)
        if i < count - 1:
            time.sleep(interval)


def main():
    parser = argparse.ArgumentParser(description="古代皇帝の勅令をランダム通知するスクリプト")
    subparsers = parser.add_subparsers(dest="command")

    # notifyコマンド
    notify_parser = subparsers.add_parser("notify", help="ランダムな勅令を即時通知")
    notify_parser.add_argument("-n", "--number", type=int, default=1, help="通知回数 (デフォルト1)")
    notify_parser.add_argument("-i", "--interval", type=int, default=10, help="通知間隔(秒)")

    # listコマンド
    list_parser = subparsers.add_parser("list", help="勅令テンプレート一覧を表示")

    args = parser.parse_args()

    if args.command == "notify":
        notify_loop(args.interval, args.number)
    elif args.command == "list":
        list_decrees()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
