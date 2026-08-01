import sys
import argparse
import random
import os
import platform
import subprocess

EXCUSES = [
    "今回のバグは水星逆行の影響です。",
    "コードが恥ずかしがっているので動きません。",
    "太陽フレアが強すぎてシステムが混乱しています。",
    "今日のネットワークは宇宙線に干渉されています。",
    "OSが月齢を気にしているようです。",
    "メモリが週末モードに入っています。",
    "開発環境がコーヒー不足で動作不良です。",
    "今日はサーバーが気分屋です。",
    "バグは量子揺らぎの産物です。",
    "コードがエコーチェンバーに迷い込んでいます。",
    "電磁波の影響でAPIが気まぐれです。",
    "OSが新しい言い訳を考え中です。",
    "今日は重力波が強いので不安定です。",
    "コードが自己主張を始めました。",
    "この現象は仕様です。",
    "バグは猫がキーボードを踏んだせいです。",
    "今日は運勢がバグ寄りです。",
    "コードが月曜日を拒否しています。",
    "OSが星占いを優先しています。",
    "システムが現実逃避しています。"
]


def select_random_excuse():
    return random.choice(EXCUSES)


def notify_linux(message):
    try:
        import notify2
        notify2.init("Random OS Excuse")
        n = notify2.Notification("OSの言い訳", message)
        n.show()
    except ImportError:
        # Fallback to notify-send
        subprocess.run(["notify-send", "OSの言い訳", message])
    except Exception as e:
        print(f"[WARN] Linux通知に失敗: {e}")


def notify_macos(message):
    try:
        import pync
        pync.notify(message, title="OSの言い訳")
    except ImportError:
        # Fallback to osascript
        script = f'display notification "{message}" with title "OSの言い訳"'
        subprocess.run(["osascript", "-e", script])
    except Exception as e:
        print(f"[WARN] macOS通知に失敗: {e}")


def notify_windows(message):
    try:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("OSの言い訳", message, duration=5)
    except ImportError:
        # Fallback: print to stderr
        print(f"[WARN] win10toast未インストール。通知できません。", file=sys.stderr)
    except Exception as e:
        print(f"[WARN] Windows通知に失敗: {e}")


def notify(message):
    system = platform.system()
    if system == "Linux":
        notify_linux(message)
    elif system == "Darwin":
        notify_macos(message)
    elif system == "Windows":
        notify_windows(message)
    else:
        print(f"[WARN] 未対応OS: {system}。通知は標準出力のみ。")


def list_excuses():
    print("--- 言い訳リスト ---")
    for i, excuse in enumerate(EXCUSES, 1):
        print(f"{i:2d}: {excuse}")


def summary():
    print(f"登録済み言い訳数: {len(EXCUSES)}")
    print(f"例: {random.choice(EXCUSES)}")


def main():
    parser = argparse.ArgumentParser(description="random-os-excuse-generator: OSの言い訳をランダム生成")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser("log", help="ランダムな言い訳を出力")
    parser_log.add_argument("--notify", action="store_true", help="デスクトップ通知も行う")

    parser_list = subparsers.add_parser("list", help="全言い訳を一覧表示")
    parser_summary = subparsers.add_parser("summary", help="言い訳数やサンプルを表示")

    # デフォルトはlog
    parser.add_argument("--notify", action="store_true", help="デスクトップ通知も行う (サブコマンド省略時)")

    args = parser.parse_args()

    if args.command == "list":
        list_excuses()
    elif args.command == "summary":
        summary()
    else:
        excuse = select_random_excuse()
        print(f"[EXCUSE] {excuse}")
        if args.notify:
            notify(excuse)

if __name__ == "__main__":
    main()
