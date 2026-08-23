import argparse
import random
import sys
import time
from datetime import datetime
try:
    from plyer import notification
except ImportError:
    notification = None

# フェイクインシデントデータ
INCIDENT_DESCRIPTIONS = [
    "OSが謎のピーマン型ウイルスに感染しました。全てのウィンドウが緑色に染まります。",
    "あなたの椅子が物理的に乗っ取られました。座ると自動で回転します。",
    "本日よりマウスが逆方向に動きます。OSは混乱しています。",
    "キーボードのAキーがAIにより永久に無効化されました。",
    "デスクトップ上のアイコンが全て逆立ちしました。",
    "あなたのCPUがカリフラワー型マルウェアに感染しました。",
    "OSが自発的に昼寝モードに入りました。しばらくお待ちください。",
    "モニターに仮想の蜘蛛の巣が生成されました。ブラウザのせいかもしれません。",
    "プリンタが自我を持ち始めました。紙の節約にご注意ください。",
    "OSがあなたの昼食を推測し始めました。プライバシーにご注意ください。"
]

RECOMMENDATIONS = [
    "ピーマン型ウイルスにご注意ください。",
    "立ち上がって深呼吸しましょう。",
    "マウスの設定を見直してください。",
    "AIにAキーの復旧を依頼してください。",
    "アイコンの体操を見守りましょう。",
    "カリフラワーの摂取は自己責任で。",
    "昼寝モード解除はコーヒーで。",
    "蜘蛛の巣は仮想ですのでご安心を。",
    "プリンタに話しかけないでください。",
    "昼食内容はOSに秘密です。"
]

# インシデントID生成
def generate_incident_id():
    prefix = random.choice(["PPR", "CHR", "SPY", "VRS", "MSE"])
    date = datetime.now().strftime("%Y%m%d")
    number = random.randint(1000, 9999)
    return f"#{prefix}-{date}-{number}"

# 通知メッセージ生成
def generate_alert():
    incident_id = generate_incident_id()
    desc = random.choice(INCIDENT_DESCRIPTIONS)
    rec = random.choice(RECOMMENDATIONS)
    alert = (
        f"[ALERT] OS Security Incident Detected!\n"
        f"- Incident ID: {incident_id}\n"
        f"- Description: {desc}\n"
        f"- Recommendation: {rec}\n"
    )
    return alert

# デスクトップ通知送信
def send_desktop_notification(title, message):
    if notification is None:
        print("plyerライブラリがインストールされていません。pip install plyer で導入してください。")
        return
    notification.notify(
        title=title,
        message=message,
        app_name="Fake OS Incident Alert",
        timeout=10
    )

# CLIサブコマンド: log (即時通知)
def cmd_log(args):
    alert = generate_alert()
    print(alert)
    if args.notify:
        send_desktop_notification("OS Security Incident", alert)

# CLIサブコマンド: list (複数回連続通知)
def cmd_list(args):
    for i in range(args.count):
        alert = generate_alert()
        print(alert)
        if args.notify:
            send_desktop_notification("OS Security Incident", alert)
        if i < args.count - 1:
            time.sleep(args.interval)

# CLIサブコマンド: summary (サンプル一覧)
def cmd_summary(args):
    print("=== フェイクインシデント例一覧 ===")
    for i in range(min(10, len(INCIDENT_DESCRIPTIONS))):
        print(f"- {INCIDENT_DESCRIPTIONS[i]}")

# メイン関数
def main():
    parser = argparse.ArgumentParser(description="爆笑フェイクOSセキュリティインシデント通知スクリプト")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_log = subparsers.add_parser("log", help="1件のフェイク通知を出す")
    parser_log.add_argument("--notify", action="store_true", help="デスクトップ通知も同時に表示")
    parser_log.set_defaults(func=cmd_log)

    parser_list = subparsers.add_parser("list", help="複数件のフェイク通知を連続で出す")
    parser_list.add_argument("--count", type=int, default=3, help="通知件数 (デフォルト: 3)")
    parser_list.add_argument("--interval", type=float, default=2.0, help="通知間隔(秒)")
    parser_list.add_argument("--notify", action="store_true", help="デスクトップ通知も同時に表示")
    parser_list.set_defaults(func=cmd_list)

    parser_summary = subparsers.add_parser("summary", help="フェイク通知例を一覧表示")
    parser_summary.set_defaults(func=cmd_summary)

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
