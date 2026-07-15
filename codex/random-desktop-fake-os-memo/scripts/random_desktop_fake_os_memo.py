import sys
import argparse
import random
import platform
import subprocess
import time
from typing import List

def get_random_memo() -> str:
    memos = [
        "冷蔵庫にプリンあり",
        "上司が見ている",
        "バグは空から降ってくる",
        "謎の引き出しを開けるな",
        "今日は何曜日でもない",
        "そのファイルはもう存在しない",
        "未確認のウィンドウが開いています",
        "メモリが夢を見ています",
        "この通知は幻です",
        "あなたのPCは今、観察されています",
        "デバッグは明日から",
        "ログインしていないのにログアウトしました",
        "OSが自我を持ち始めています",
        "謎のプロセスが増殖中",
        "プリンターが脱走しました",
        "このメモは自動で消滅しません",
        "キーボードが逆立ちしています",
        "ウィンドウの外に何かいる",
        "今日は再起動しないでください",
        "コーヒーをこぼさないでください",
        "ファイルがどこかに旅立ちました",
        "あなたのタスクは未定義です",
        "この通知に意味はありません",
        "次の通知をお楽しみに",
        "OSの気まぐれです",
        "謎の引数が渡されました",
        "仮想メモリが現実逃避中",
        "マウスが迷子です",
        "再起動しなくても大丈夫です",
        "このメモはバグではありません"
    ]
    return random.choice(memos)

def send_notification(title: str, message: str):
    current_os = platform.system()
    try:
        if current_os == "Darwin":  # macOS
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "{title}"'
            ], check=True)
        elif current_os == "Linux":
            subprocess.run([
                "notify-send", title, message
            ], check=True)
        elif current_os == "Windows":
            # Use Toast notification via powershell
            powershell_script = f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null; " \
                               f"$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02); " \
                               f"$textNodes = $template.GetElementsByTagName(\"text\"); " \
                               f"$textNodes.Item(0).AppendChild($template.CreateTextNode(\"{title}\")) > $null; " \
                               f"$textNodes.Item(1).AppendChild($template.CreateTextNode(\"{message}\")) > $null; " \
                               f"$toast = [Windows.UI.Notifications.ToastNotification]::new($template); " \
                               f"$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier(\"RandomMemoSkill\"); " \
                               f"$notifier.Show($toast);"
            subprocess.run([
                "powershell", "-Command", powershell_script
            ], check=True)
        else:
            print(f"[通知] {title}: {message}")
    except Exception as e:
        print(f"通知エラー: {e}")

def list_memos():
    print("=== 謎のOSメモ候補一覧 ===")
    for idx, memo in enumerate(get_all_memos(), 1):
        print(f"{idx:02d}: {memo}")

def get_all_memos() -> List[str]:
    return [
        "冷蔵庫にプリンあり",
        "上司が見ている",
        "バグは空から降ってくる",
        "謎の引き出しを開けるな",
        "今日は何曜日でもない",
        "そのファイルはもう存在しない",
        "未確認のウィンドウが開いています",
        "メモリが夢を見ています",
        "この通知は幻です",
        "あなたのPCは今、観察されています",
        "デバッグは明日から",
        "ログインしていないのにログアウトしました",
        "OSが自我を持ち始めています",
        "謎のプロセスが増殖中",
        "プリンターが脱走しました",
        "このメモは自動で消滅しません",
        "キーボードが逆立ちしています",
        "ウィンドウの外に何かいる",
        "今日は再起動しないでください",
        "コーヒーをこぼさないでください",
        "ファイルがどこかに旅立ちました",
        "あなたのタスクは未定義です",
        "この通知に意味はありません",
        "次の通知をお楽しみに",
        "OSの気まぐれです",
        "謎の引数が渡されました",
        "仮想メモリが現実逃避中",
        "マウスが迷子です",
        "再起動しなくても大丈夫です",
        "このメモはバグではありません"
    ]

def notify_once():
    memo = get_random_memo()
    send_notification("謎のOSメモ", memo)
    print(f"[通知] 謎のOSメモ: {memo}")

def notify_loop(interval: int, count: int):
    for i in range(count):
        memo = get_random_memo()
        send_notification("謎のOSメモ", memo)
        print(f"[通知] 謎のOSメモ: {memo}")
        if i < count - 1:
            time.sleep(interval)

def main():
    parser = argparse.ArgumentParser(
        description="謎のOSメモをデスクトップ通知で表示するスキル (random-desktop-fake-os-memo)"
    )
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    parser_notify = subparsers.add_parser("notify", help="1回だけ謎メモを通知")
    parser_notify.add_argument("-n", "--number", type=int, default=1, help="通知回数 (デフォルト: 1)")
    parser_notify.add_argument("-i", "--interval", type=int, default=5, help="通知間隔(秒, デフォルト: 5)")

    parser_list = subparsers.add_parser("list", help="全メモ候補を一覧表示")

    args = parser.parse_args()

    if args.command == "notify":
        if args.number <= 1:
            notify_once()
        else:
            notify_loop(args.interval, args.number)
    elif args.command == "list":
        list_memos()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
