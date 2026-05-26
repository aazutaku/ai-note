import os
import sys
import time
import argparse
import subprocess
import random
import json
from datetime import datetime

SLACK_API_URL = "https://slack.com/api/users.profile.set"

MOOD_MESSAGES = {
    "最高": "絶好調！今日もバリバリいきましょう。",
    "だるい": "本日省エネ運転。無理せずいきましょう。",
    "普通": "平常運転。淡々と進めましょう。",
    "眠い": "眠気注意。コーヒーでリフレッシュ！",
    "やる気": "やる気MAX！この勢いで進もう。",
    "疲れた": "お疲れ様です。休憩も大事です。",
    "イライラ": "深呼吸してリセットしましょう。",
    "楽しい": "楽しさ全開！良い流れです。",
    "集中": "集中モード。邪魔しないで！",
    "困惑": "困ったときは相談も大事。",
}

DAILY_QUOTES = [
    "コーヒーは気分転換の友！",
    "今日も一歩前進。",
    "深呼吸してリフレッシュ。",
    "無理せず自分のペースで。",
    "たまにはストレッチを。",
    "小さな成功も大事に。",
    "悩んだら一度離れてみよう。",
    "笑顔で乗り切ろう。",
    "新しい発見を楽しもう。",
    "自分を褒めてあげよう。",
]

def get_mood():
    return os.environ.get("MOOD", "普通")

def get_mood_message(mood):
    return MOOD_MESSAGES.get(mood, f"気分: {mood} (メッセージ未登録)")

def get_daily_quote():
    today = datetime.today().toordinal()
    idx = today % len(DAILY_QUOTES)
    return DAILY_QUOTES[idx]

def update_shell_prompt(mood_msg):
    bashrc = os.path.expanduser("~/.bashrc")
    zshrc = os.path.expanduser("~/.zshrc")
    prompt_line = f'export PS1="[os-status-mood-light] {mood_msg} $PS1"\n'
    updated = False
    for rcfile in [bashrc, zshrc]:
        if os.path.exists(rcfile):
            with open(rcfile, 'r') as f:
                lines = f.readlines()
            # Remove previous mood lines
            lines = [l for l in lines if '[os-status-mood-light]' not in l]
            lines.append(prompt_line)
            with open(rcfile, 'w') as f:
                f.writelines(lines)
            updated = True
    return updated

def update_slack_status(token, mood_msg):
    import requests
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    profile = {
        "status_text": mood_msg,
        "status_emoji": ":speech_balloon:",
        "status_expiration": 0
    }
    data = {"profile": profile}
    response = requests.post(SLACK_API_URL, headers=headers, data=json.dumps(data))
    if not response.ok:
        print(f"[os-status-mood-light] Slack API error: {response.text}")
    return response.ok

def print_status(mood, mood_msg, quote, slack=False):
    print(f"[os-status-mood-light] 気分: {mood} → {mood_msg}")
    print(f"[os-status-mood-light] 今日の一言: \"{quote}\"")
    if slack:
        print(f"[os-status-mood-light] Slackステータス更新: \"{mood_msg}\"")

def monitor_mode(args):
    prev_mood = None
    slack_token = args.slack_token
    print("[os-status-mood-light] MOOD監視モード開始。Ctrl+Cで終了。")
    try:
        while True:
            mood = get_mood()
            if mood != prev_mood:
                mood_msg = get_mood_message(mood)
                quote = get_daily_quote()
                print_status(mood, mood_msg, quote, slack=bool(slack_token))
                update_shell_prompt(mood_msg)
                if slack_token:
                    update_slack_status(slack_token, mood_msg)
                prev_mood = mood
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[os-status-mood-light] 監視終了。")

def show_status(args):
    mood = get_mood()
    mood_msg = get_mood_message(mood)
    quote = get_daily_quote()
    print_status(mood, mood_msg, quote, slack=bool(args.slack_token))
    if args.update_prompt:
        update_shell_prompt(mood_msg)
    if args.slack_token:
        update_slack_status(args.slack_token, mood_msg)

def list_moods(args):
    print("[os-status-mood-light] 登録済み気分一覧:")
    for mood, msg in MOOD_MESSAGES.items():
        print(f"  {mood}: {msg}")

def main():
    parser = argparse.ArgumentParser(description="os-status-mood-light: 気分可視化スキル")
    subparsers = parser.add_subparsers(dest="command")
    
    parser_status = subparsers.add_parser("status", help="現在の気分とメッセージを表示")
    parser_status.add_argument("--update-prompt", action="store_true", help="シェルプロンプトも更新")
    parser_status.add_argument("--slack-token", type=str, help="Slack APIトークン")
    parser_status.set_defaults(func=show_status)

    parser_monitor = subparsers.add_parser("monitor", help="MOOD環境変数を監視し自動反映")
    parser_monitor.add_argument("--slack-token", type=str, help="Slack APIトークン")
    parser_monitor.set_defaults(func=monitor_mode)

    parser_list = subparsers.add_parser("list", help="登録済み気分一覧を表示")
    parser_list.set_defaults(func=list_moods)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
