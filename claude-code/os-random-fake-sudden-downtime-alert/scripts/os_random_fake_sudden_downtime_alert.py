import argparse
import random
import sys
import time
import platform
import subprocess

try:
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

# --- ランダム通知テンプレート ---
REASONS = [
    'OSのやる気が著しく低下',
    '謎の宇宙線が検出されました',
    'システム内でエンジニアの悲鳴を感知',
    'メモリが突然詩的になった',
    'ファイルシステムが哲学的思考に陥った',
    'プロセスIDが自己否定を始めた',
    'カーネルが深い眠りに落ちた',
    'OSの自己肯定感が低下',
    'CPUが現実逃避',
    '未知のエラー: 42',
]

ACTIONS = [
    'キーボードを褒め称えて延命可能',
    '画面に向かって「ありがとうOS」と叫ぶ',
    'マウスを優しく撫でる',
    'コーヒーをOSのために淹れる',
    '深呼吸してPCに微笑みかける',
    '一曲歌ってみる',
    '椅子から立ち上がって拍手',
    'OSに励ましの言葉を送る',
    'USBメモリを抜き差しするフリをする',
    '何もしなくても大丈夫（たぶん）',
]

CANCELS = [
    'Ctrl+Alt+Delを唱える（効果なし）',
    'OSの気分次第',
    'キャンセル不可',
    '画面を優しくタップ',
    '「OSさん頑張って」とつぶやく',
    '再起動を想像する',
    'PCにお辞儀する',
    'キャンセル方法は不明',
    'OSが許すまで待つ',
    '運に任せる',
]

EN_MESSAGES = [
    'Warning: Sudden downtime scheduled in {min} minutes',
    'Critical: System maintenance will start in {min} minutes',
    'Alert: Spontaneous OS nap in {min} minutes',
]

EN_REASONS = [
    'Unusual cosmic ray activity detected',
    'OS motivation critically low',
    'Kernel is feeling poetic',
    'File system in existential crisis',
    'CPU is daydreaming',
]

EN_ACTIONS = [
    'Pet your mouse gently',
    'Say "Thank you, OS" to your screen',
    'Sing a song for your system',
    'Smile at your computer',
    'Take a deep breath',
]

EN_CANCELS = [
    'Cancel not possible',
    'Try rebooting in your mind',
    'Wait for OS to forgive',
    'No known workaround',
    'Offer coffee to your PC',
]

# --- 通知生成 ---
def generate_alert_message(lang='ja'):
    min_left = random.randint(3, 30)
    if lang == 'ja':
        title = f'緊急: このPCは{min_left}分後に謎のメンテナンスモードへ突入します'
        reason = f'理由: {random.choice(REASONS)}'
        action = f'対策: {random.choice(ACTIONS)}'
        cancel = f'キャンセル方法: {random.choice(CANCELS)}'
        return f'[ALERT] {title}\n{reason}\n{action}\n{cancel}'
    else:
        title = random.choice(EN_MESSAGES).format(min=min_left)
        reason = f'Reason: {random.choice(EN_REASONS)}'
        action = f'Mitigation: {random.choice(EN_ACTIONS)}'
        cancel = f'Cancel: {random.choice(EN_CANCELS)}'
        return f'[ALERT] {title}\n{reason}\n{action}\n{cancel}'

# --- 通知表示 ---
def show_desktop_notification(message, title='Fake OS Downtime Alert'):
    if PLYER_AVAILABLE:
        notification.notify(
            title=title,
            message=message,
            timeout=10
        )
    else:
        # Fallback: macOS (osascript), Linux (notify-send), Windows (print)
        plat = platform.system()
        if plat == 'Darwin':
            try:
                subprocess.run(['osascript', '-e', f'display notification "{message}" with title "{title}"'], check=True)
            except Exception:
                print(message)
        elif plat == 'Linux':
            try:
                subprocess.run(['notify-send', title, message], check=True)
            except Exception:
                print(message)
        elif plat == 'Windows':
            print(message)
        else:
            print(message)

# --- ターミナル演出 ---
def show_terminal_alert(message):
    border = '=' * 60
    print(f'\n{border}\n{message}\n{border}\n')

# --- CLIパーサ ---
def parse_args():
    parser = argparse.ArgumentParser(description='os-random-fake-sudden-downtime-alert: フェイクOS緊急通知ジェネレータ')
    parser.add_argument('--lang', choices=['ja', 'en'], default='ja', help='通知言語 (ja/en)')
    parser.add_argument('--mode', choices=['desktop', 'terminal', 'both'], default='terminal', help='通知表示方法')
    parser.add_argument('--repeat', type=int, default=1, help='通知回数 (1以上)')
    parser.add_argument('--interval', type=int, default=0, help='繰り返し時の間隔(秒)')
    parser.add_argument('--list', action='store_true', help='通知テンプレート例を一覧表示')
    return parser.parse_args()

# --- テンプレート例表示 ---
def list_templates():
    print('--- 日本語テンプレート例 ---')
    for i in range(3):
        print(generate_alert_message('ja'))
        print()
    print('--- English templates ---')
    for i in range(3):
        print(generate_alert_message('en'))
        print()

# --- メイン ---
def main():
    args = parse_args()
    if args.list:
        list_templates()
        sys.exit(0)
    for i in range(args.repeat):
        msg = generate_alert_message(args.lang)
        if args.mode in ('desktop', 'both'):
            show_desktop_notification(msg)
        if args.mode in ('terminal', 'both'):
            show_terminal_alert(msg)
        if args.repeat > 1 and i < args.repeat - 1:
            time.sleep(args.interval)

if __name__ == '__main__':
    main()
