import sys
import argparse
import random
import time
import platform
import subprocess

VIRUS_NAMES = [
    '伝説のワーム“メロンパン”',
    'さすらいのポリオミノ',
    '幻のトロイ“カラフルバグ”',
    '時空を超えるバイナリ“ミレニアムバグ”',
    '闇夜のスクリプト“ブラックキャット”',
    '未確認ウイルス“パラレルビット”',
    '迷宮型ワーム“ラビリンス”',
    '自己増殖型“オーバーフロー”',
    '伝説の“ブルースクリーンメーカー”',
    '謎の“カセットテープウイルス”',
]

YEARS = [str(y) + '年製' for y in range(1995, 2005)]

AFFECTED_AREAS = [
    'Cドライブ全域',
    'Dドライブ',
    'C:\\WINDOWS\\System32',
    '/usr/bin',
    '/home/user/Documents',
    'レジストリ',
    'ネットワーク全体',
    '/tmp',
    'メモリ領域',
    'フロッピーディスク',
]

CLEAN_TOOLS = [
    'C:\\Tools\\melonpan_cleaner.exe',
    '/usr/local/bin/virus_cleaner',
    '再起動推奨',
    '手動削除',
    'OSアップデート',
    'セーフモードで起動',
    'ネットワーク切断',
]

DETAILS = [
    '本ウイルスは1998年に発見され、未だに正体不明です。',
    '被害報告はありませんが、警戒が必要です。',
    '感染経路は不明です。',
    '駆除ツールは現在開発中です。',
    '一時的なファイル消失が発生する場合があります。',
    'システムの動作に影響はありません。',
    '再起動で解消することがあります。',
    '詳細は公式サポートをご参照ください。',
]

TEMPLATE = """
[{year}] OS公式警告: {virus}を検出しました。
駆除ツール: {clean_tool}
影響範囲: {area}
詳細: {detail}
"""

TEMPLATE_ALT = """
[{year}] OS公式警告: {virus}が潜伏中です。
駆除方法: {clean_tool}
影響範囲: {area}
詳細: {detail}
"""

def generate_fake_alert():
    virus = random.choice(VIRUS_NAMES)
    year = random.choice(YEARS)
    area = random.choice(AFFECTED_AREAS)
    clean_tool = random.choice(CLEAN_TOOLS)
    detail = random.choice(DETAILS)
    template = random.choice([TEMPLATE, TEMPLATE_ALT])
    return template.format(year=year, virus=virus, clean_tool=clean_tool, area=area, detail=detail)

def notify_desktop(message):
    system = platform.system()
    try:
        if system == 'Darwin':
            subprocess.run(['osascript', '-e', f'display notification "{message}" with title "OS公式ウイルス警告"'], check=True)
        elif system == 'Linux':
            subprocess.run(['notify-send', 'OS公式ウイルス警告', message], check=True)
        elif system == 'Windows':
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("OS公式ウイルス警告", message, duration=5)
            except ImportError:
                print("win10toastが見つかりません。ターミナルに表示します。")
                print(message)
        else:
            print(message)
    except Exception as e:
        print(f"通知エラー: {e}")
        print(message)

def print_terminal(message):
    border = '-' * 60
    print(f"\n{border}\n{message}{border}\n")

def main():
    parser = argparse.ArgumentParser(description='レトロOSジョークウイルス警告通知')
    parser.add_argument('--now', action='store_true', help='即時通知を発火')
    parser.add_argument('--count', type=int, default=1, help='通知回数')
    parser.add_argument('--interval', type=float, default=0, help='通知間隔(秒)')
    parser.add_argument('--desktop', action='store_true', help='デスクトップ通知も行う')
    parser.add_argument('--terminal', action='store_true', help='ターミナル表示も行う')
    args = parser.parse_args()

    if not args.desktop and not args.terminal:
        # どちらも指定がなければ両方
        args.desktop = True
        args.terminal = True

    for i in range(args.count):
        msg = generate_fake_alert()
        if args.desktop:
            notify_desktop(msg)
        if args.terminal:
            print_terminal(msg)
        if i < args.count - 1:
            time.sleep(args.interval)

if __name__ == '__main__':
    main()
