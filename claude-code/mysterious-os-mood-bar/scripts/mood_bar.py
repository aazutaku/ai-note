import sys
import argparse
import random
import subprocess
import platform
import shlex

MOOD_WORDS = [
    ('やる気-3度', '情熱沸騰中'),
    ('やる気指数: 42%', '気分：曇りのち晴れ'),
    ('本日の気分温度: +12度', 'やる気急上昇'),
    ('やる気-15度', '省エネモード'),
    ('気分指数: 99', 'やる気爆発中'),
    ('やる気+7度', 'やる気そこそこ'),
    ('やる気指数: 0%', '完全休息モード'),
    ('気分温度: -8度', '冷静沈着'),
    ('やる気+25度', 'やる気暴走'),
    ('やる気指数: 88%', '情熱再燃')
]

MOOD_PATTERNS = [
    '本日やる気{temp}度 ({mood})',
    'やる気指数: {percent}%（気分：{weather}）',
    '本日の気分温度: {temp}度（{mood}）',
    'やる気{temp}度（{mood}）',
    '気分指数: {percent}（{mood}）'
]

WEATHERS = ['晴れ', '曇り', '雨', '嵐', '快晴', '霧', '雪']
MOODS = ['やる気急上昇', '情熱沸騰中', '省エネモード', 'やる気爆発中', 'やる気そこそこ', '完全休息モード', '冷静沈着', 'やる気暴走', '情熱再燃']

def get_git_status_mood():
    try:
        output = subprocess.check_output(['git', 'status', '--porcelain'], stderr=subprocess.DEVNULL).decode('utf-8')
        lines = output.strip().splitlines()
        if not lines:
            return 10, 'やる気そこそこ'
        elif len(lines) < 3:
            return 25, 'やる気急上昇'
        elif len(lines) < 7:
            return -3, '省エネモード'
        else:
            return -15, '完全休息モード'
    except Exception:
        return random.randint(-20, 30), random.choice(MOODS)

def random_mood():
    temp = random.randint(-20, 40)
    percent = random.randint(0, 100)
    mood = random.choice(MOODS)
    weather = random.choice(WEATHERS)
    pattern = random.choice(MOOD_PATTERNS)
    return pattern.format(temp=temp, percent=percent, mood=mood, weather=weather)

def build_mood_message(command_str=None):
    # コマンド長や雰囲気で適当判定
    if command_str:
        length = len(command_str)
        if 'git' in command_str:
            temp, mood = get_git_status_mood()
            return f'やる気{temp}度（{mood}）'
        elif length < 10:
            return 'やる気指数: 88%（情熱再燃）'
        elif length < 30:
            return 'やる気指数: 42%（気分：曇りのち晴れ）'
        elif length < 60:
            return 'やる気+7度（やる気そこそこ）'
        else:
            return random_mood()
    else:
        return random_mood()

def show_os_notification(message):
    system = platform.system()
    if system == 'Darwin':
        # macOS: osascriptでメニューバー通知
        script = f'display notification "{message}" with title "Mood Bar"'
        try:
            subprocess.run(['osascript', '-e', script], check=True)
        except Exception as e:
            print(f'[WARN] osascript failed: {e}', file=sys.stderr)
    elif system == 'Linux':
        # Linux: notify-sendでステータスバー通知
        try:
            subprocess.run(['notify-send', 'Mood Bar', message], check=True)
        except Exception as e:
            print(f'[WARN] notify-send failed: {e}', file=sys.stderr)
    else:
        print(f'[Mood Bar] {message}')

def main():
    parser = argparse.ArgumentParser(description='mysterious-os-mood-bar: 気分温度ややる気指数を冗談的に表示するスキル')
    parser.add_argument('command', nargs='*', help='コマンドラインで実行したコマンド文字列（省略可）')
    parser.add_argument('--dry-run', action='store_true', help='通知せず標準出力に表示')
    args = parser.parse_args()

    command_str = ' '.join(args.command) if args.command else None
    message = build_mood_message(command_str)

    if args.dry_run:
        print(f'[Mood Bar] {message}')
    else:
        show_os_notification(message)

if __name__ == '__main__':
    main()
