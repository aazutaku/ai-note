import sys
import argparse
import random
import datetime
import os

MOOD_LABELS = [
    (15, '冷え冷え'),
    (25, 'まあまあ'),
    (32, '普通'),
    (37, 'ノリノリ'),
    (40, '絶好調'),
    (43, '炎上中'),
]

BAR_LENGTH = 20
LOG_FILE = 'mood_temperature.log'

def get_mood_label(temp):
    for threshold, label in MOOD_LABELS:
        if temp < threshold:
            return label
    return MOOD_LABELS[-1][1]

def generate_temperature():
    # 15.0〜43.0度の範囲でランダム
    return round(random.uniform(15.0, 43.0), 1)

def generate_bar(temp):
    # 15.0〜43.0度を0〜BAR_LENGTHにマッピング
    min_temp, max_temp = 15.0, 43.0
    filled = int((temp - min_temp) / (max_temp - min_temp) * BAR_LENGTH)
    bar = '■' * filled + ' ' * (BAR_LENGTH - filled)
    return f'[{bar}]'

def format_status(temp, label):
    bar = generate_bar(temp)
    return f"[os-mood-temperature-bar] 気分温度: {temp}℃ ({label}) | ステータスバー: {bar}"

def log_status(temp, label, status):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{now}\t{temp}\t{label}\t{status}\n")

def show_log():
    if not os.path.exists(LOG_FILE):
        print("ログファイルがありません。まだ気分温度を記録していません。")
        return
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())

def show_summary():
    if not os.path.exists(LOG_FILE):
        print("ログファイルがありません。まだ気分温度を記録していません。")
        return
    temps = []
    labels = {}
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                try:
                    temp = float(parts[1])
                    label = parts[2]
                    temps.append(temp)
                    labels[label] = labels.get(label, 0) + 1
                except Exception:
                    continue
    if not temps:
        print("記録がありません。")
        return
    print(f"記録数: {len(temps)}")
    print(f"平均気分温度: {round(sum(temps)/len(temps), 1)}℃")
    print("コメント分布:")
    for label, count in sorted(labels.items(), key=lambda x: -x[1]):
        print(f"  {label}: {count}回")

def main():
    parser = argparse.ArgumentParser(description='気分温度ステータスバー')
    subparsers = parser.add_subparsers(dest='command')

    parser_log = subparsers.add_parser('log', help='最新の気分温度を表示し、ログに記録')
    parser_list = subparsers.add_parser('list', help='気分温度ログを表示')
    parser_summary = subparsers.add_parser('summary', help='気分温度ログのサマリを表示')
    parser.add_argument('--no-log', action='store_true', help='ログに記録しない')

    args = parser.parse_args()

    if args.command == 'list':
        show_log()
    elif args.command == 'summary':
        show_summary()
    else:
        temp = generate_temperature()
        label = get_mood_label(temp)
        status = format_status(temp, label)
        print(status)
        if not args.no_log:
            log_status(temp, label, status)

if __name__ == '__main__':
    main()
