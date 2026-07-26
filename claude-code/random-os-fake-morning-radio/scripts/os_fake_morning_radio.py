import sys
import random
import argparse
import platform
import subprocess
import datetime
import os

def get_random_greeting():
    greetings = [
        "おはようございます！本日のOS天気予報は『カーネルパニック注意報』です。",
        "おはよう！今日も元気にバグを直しましょう。",
        "おはようございます、開発者の皆さん。今日もCPU全開で！",
        "おはようございます。OS業界の朝は早い。",
        "本日もご安全に。OSラジオ、始まります！"
    ]
    return random.choice(greetings)

def get_random_one_liner():
    oneliners = [
        "バグは寝て待て、直ることもある。",
        "今日の運勢：メモリリーク注意。",
        "本日のラッキーアイテムは『sudo』です。",
        "人生はリブートの連続。",
        "バグは友達、怖くない。"
    ]
    return random.choice(oneliners)

def get_random_news():
    news = [
        "メモリ管理部がまた寝坊、CPUが代打で登板中。",
        "カーネルアップデートが朝礼をドタキャン。",
        "ファイルシステムがSSDと密会していたとの噂。",
        "ネットワーク担当がWi-Fiを落とした模様。",
        "プロセス管理部、スレッド数を間違えて炎上。"
    ]
    return random.choice(news)

def get_random_gossip():
    gossips = [
        "昨夜、ファイルシステムが密かにSSDと会っていたとの噂。",
        "カーネルとドライバが深夜に密談。",
        "デバイスマネージャーがUSBと喧嘩したらしい。",
        "バッテリーが電源管理部に不満爆発。",
        "GUI担当がCLI派とランチに行ったらしい。"
    ]
    return random.choice(gossips)

def get_random_weather():
    weathers = [
        "本日のバーチャル天気は晴れ時々セグメンテーションフォルト。",
        "今日はメモリリークのち快晴。",
        "カーネルパニックのち曇り。",
        "晴れ時々IOエラー。",
        "局地的にプロセス落下の恐れ。"
    ]
    return random.choice(weathers)

def format_radio_message():
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    msg = [
        f"[OS Morning Radio] {dt}",
        f"[DJ] {get_random_greeting()}",
        f"[DJ] 今日の一言：『{get_random_one_liner()}』",
        f"[ニュース] {get_random_news()}",
        f"[ゴシップ] {get_random_gossip()}",
        f"[天気] {get_random_weather()}"
    ]
    return "\n".join(msg)

def send_desktop_notification(title, message):
    system = platform.system()
    try:
        if system == "Linux":
            subprocess.run(["notify-send", title, message], check=True)
        elif system == "Darwin":
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(["osascript", "-e", script], check=True)
        else:
            # Windowsや未対応OSは通知せずターミナル出力のみ
            pass
    except Exception as e:
        print(f"[WARN] 通知送信に失敗: {e}")

def print_radio_message():
    msg = format_radio_message()
    print(msg)

def trigger_radio(args):
    msg = format_radio_message()
    print(msg)
    # 通知も送信
    send_desktop_notification("OS Morning Radio", msg.replace("\n", " "))

def main():
    parser = argparse.ArgumentParser(description="謎のOSモーニングラジオ風メッセージを出力/通知するスクリプト")
    subparsers = parser.add_subparsers(dest="command")

    parser_run = subparsers.add_parser("run", help="ラジオメッセージを出力・通知する")
    parser_run.set_defaults(func=trigger_radio)

    parser_sample = subparsers.add_parser("sample", help="サンプルメッセージをターミナルに表示する")
    parser_sample.set_defaults(func=lambda args: print_radio_message())

    if len(sys.argv) == 1:
        # デフォルトでrun
        args = parser.parse_args(["run"])
    else:
        args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
