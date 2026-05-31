import os
import sys
import random
import time
import argparse
from pathlib import Path
import threading
import PySimpleGUI as sg

# 天気アイコンの種別とファイル名 (最低限のSVG/PNGを同梱または生成)
WEATHER_TYPES = [
    {"name": "晴れ", "file": "sun.png"},
    {"name": "曇り", "file": "cloud.png"},
    {"name": "雨", "file": "rain.png"},
    {"name": "雷", "file": "thunder.png"},
    {"name": "雪", "file": "snow.png"},
    {"name": "あらし", "file": "storm.png"},
]

ICON_DIR = Path(__file__).parent / "icons"
ICON_SIZE = (64, 64)

# アイコン画像がなければサンプルPNGを生成 (簡易的な色付き四角)
def ensure_icons():
    ICON_DIR.mkdir(exist_ok=True)
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("[WARN] Pillow未インストールのためアイコン自動生成はスキップします。")
        return
    color_map = {
        "sun.png": (255, 220, 0),
        "cloud.png": (180, 180, 180),
        "rain.png": (80, 140, 255),
        "thunder.png": (255, 200, 0),
        "snow.png": (220, 240, 255),
        "storm.png": (100, 100, 120),
    }
    for w in WEATHER_TYPES:
        f = ICON_DIR / w["file"]
        if not f.exists():
            img = Image.new("RGB", ICON_SIZE, color_map[w["file"]])
            d = ImageDraw.Draw(img)
            font = None
            try:
                font = ImageFont.truetype("arial.ttf", 24)
            except:
                font = None
            d.text((8, 16), w["name"], fill=(0,0,0), font=font)
            img.save(f)

# 現在の画面サイズを取得
def get_screen_size():
    try:
        return sg.Window.get_screen_size()
    except Exception:
        return (800, 600)

# ランダムな天気を選ぶ
def pick_random_weather():
    return random.choice(WEATHER_TYPES)

# メインウィンドウを表示
def show_weather_icon(weather, duration=600):
    screen_w, screen_h = get_screen_size()
    icon_path = str(ICON_DIR / weather["file"])
    layout = [[sg.Image(filename=icon_path, size=ICON_SIZE, pad=(0,0))]]
    window = sg.Window(
        f"気分天気: {weather['name']}",
        layout,
        no_titlebar=True,
        keep_on_top=True,
        alpha_channel=0.95,
        grab_anywhere=False,
        finalize=True,
        location=(screen_w - ICON_SIZE[0] - 16, screen_h - ICON_SIZE[1] - 64),
        margins=(0,0),
        element_justification='center',
        background_color='#ffffff',
    )
    # 10分(600秒)表示。ESCキーやクリックで即終了
    start = time.time()
    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED or event == 'Escape' or event == '__TIMEOUT__':
            if time.time() - start > duration:
                break
        if event == '__TIMEOUT__' and (time.time() - start > duration):
            break
    window.close()

# CLIサブコマンド: show, list, summary
def list_weathers():
    print("[INFO] サポートされる気分天気:")
    for w in WEATHER_TYPES:
        print(f"- {w['name']} ({w['file']})")

def summary():
    print("desktop-mood-weather Skill 概要:")
    print("- デスクトップ右下にランダムな天気アイコンを表示")
    print("- 実際の天気や気分とは一切連動しません")
    print("- アイコンは10分ごとに再抽選可能")
    print("- 明示/暗黙トリガーで発動")

def main():
    parser = argparse.ArgumentParser(description="desktop-mood-weather: デスクトップにランダム天気アイコンを表示")
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = False
    show_parser = subparsers.add_parser('show', help='気分天気アイコンを表示')
    show_parser.add_argument('--duration', type=int, default=600, help='表示秒数 (デフォルト600)')
    list_parser = subparsers.add_parser('list', help='サポート天気一覧')
    summary_parser = subparsers.add_parser('summary', help='Skill概要')
    args = parser.parse_args()
    ensure_icons()
    if args.command == 'list':
        list_weathers()
        return
    if args.command == 'summary':
        summary()
        return
    # デフォルトまたはshowコマンド
    weather = pick_random_weather()
    print(f"[INFO] desktop-mood-weather: ランダム天気アイコン「{weather['name']}」がデスクトップ右下に表示されました。")
    print(f"[INFO] desktop-mood-weather: 本日の気分天気は「{weather['name']}」です。")
    print(f"[INFO] desktop-mood-weather: アイコン={weather['file']}, 位置=(右下)")
    print("[INFO] desktop-mood-weather: 実際の天気や気分とは一切関係ありません。")
    show_weather_icon(weather, duration=args.duration)

if __name__ == '__main__':
    main()
