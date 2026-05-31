import sys
import os
import random
import tempfile
import argparse
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
try:
    from plyer import notification
except ImportError:
    notification = None

WEATHER_TYPES = [
    {"name": "晴れ", "color": (255, 223, 0), "draw": "draw_sunny"},
    {"name": "曇り", "color": (180, 180, 180), "draw": "draw_cloudy"},
    {"name": "雨", "color": (100, 149, 237), "draw": "draw_rainy"},
    {"name": "雷", "color": (255, 215, 0), "draw": "draw_thunder"},
    {"name": "大雪", "color": (230, 230, 250), "draw": "draw_snow"},
    {"name": "あらし", "color": (105, 105, 105), "draw": "draw_storm"},
    {"name": "霧", "color": (211, 211, 211), "draw": "draw_fog"},
]

ICON_SIZE = (96, 96)
FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/Library/Fonts/Arial.ttf",
    "C:/Windows/Fonts/arial.ttf",
]


def get_font(size=18):
    for path in FONT_PATHS:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_sunny(draw):
    # Draw a sun
    x, y = ICON_SIZE[0] // 2, ICON_SIZE[1] // 2
    draw.ellipse((x-25, y-25, x+25, y+25), fill=(255, 223, 0))
    for angle in range(0, 360, 45):
        dx = int(40 * math.cos(math.radians(angle)))
        dy = int(40 * math.sin(math.radians(angle)))
        draw.line((x, y, x+dx, y+dy), fill=(255, 180, 0), width=4)

def draw_cloudy(draw):
    # Draw clouds
    draw.ellipse((30, 50, 80, 80), fill=(200, 200, 200))
    draw.ellipse((50, 40, 90, 70), fill=(180, 180, 180))
    draw.ellipse((20, 60, 70, 90), fill=(210, 210, 210))

def draw_rainy(draw):
    draw_cloudy(draw)
    for i in range(5):
        x = 40 + i * 10
        draw.line((x, 80, x, 92), fill=(100, 149, 237), width=3)

def draw_thunder(draw):
    draw_cloudy(draw)
    # Thunder bolt
    draw.polygon([(60, 70), (65, 90), (58, 85), (68, 110), (62, 90), (70, 100)], fill=(255, 215, 0))

def draw_snow(draw):
    draw_cloudy(draw)
    for i in range(5):
        x = 40 + i * 10
        draw.ellipse((x-3, 85, x+3, 91), fill=(230, 230, 250))

def draw_storm(draw):
    draw_cloudy(draw)
    draw.line((30, 80, 80, 90), fill=(105, 105, 105), width=4)
    draw_thunder(draw)

def draw_fog(draw):
    draw_cloudy(draw)
    for y in [85, 90, 95]:
        draw.rectangle((25, y, 80, y+2), fill=(211, 211, 211))

DRAW_FUNCS = {
    "draw_sunny": draw_sunny,
    "draw_cloudy": draw_cloudy,
    "draw_rainy": draw_rainy,
    "draw_thunder": draw_thunder,
    "draw_snow": draw_snow,
    "draw_storm": draw_storm,
    "draw_fog": draw_fog,
}

import math

def generate_weather_icon(weather):
    img = Image.new("RGBA", ICON_SIZE, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    DRAW_FUNCS[weather["draw"]](draw)
    font = get_font(18)
    w, h = draw.textsize(weather["name"], font=font)
    draw.text(((ICON_SIZE[0]-w)//2, ICON_SIZE[1]-h-8), weather["name"], fill=(80, 80, 80), font=font)
    return img

def show_desktop_notification(title, message, icon_path=None):
    if notification is None:
        print("[WARN] plyer.notification がインストールされていません。通知は表示されません。", file=sys.stderr)
        return
    try:
        notification.notify(
            title=title,
            message=message,
            app_icon=icon_path if icon_path and os.path.exists(icon_path) else None,
            timeout=5
        )
    except Exception as e:
        print(f"[ERROR] 通知の表示に失敗: {e}", file=sys.stderr)


def log_weather_event(weather):
    logdir = os.path.join(os.path.expanduser("~"), ".desktop_mood_weather")
    os.makedirs(logdir, exist_ok=True)
    logfile = os.path.join(logdir, "weather_log.txt")
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()}\t{weather['name']}\n")


def list_weather_log():
    logdir = os.path.join(os.path.expanduser("~"), ".desktop_mood_weather")
    logfile = os.path.join(logdir, "weather_log.txt")
    if not os.path.exists(logfile):
        print("[INFO] ログがありません。")
        return
    with open(logfile, encoding="utf-8") as f:
        for line in f:
            print(line.strip())

def summary_weather_log():
    logdir = os.path.join(os.path.expanduser("~"), ".desktop_mood_weather")
    logfile = os.path.join(logdir, "weather_log.txt")
    if not os.path.exists(logfile):
        print("[INFO] ログがありません。")
        return
    from collections import Counter
    counts = Counter()
    with open(logfile, encoding="utf-8") as f:
        for line in f:
            try:
                _, weather = line.strip().split("\t")
                counts[weather] += 1
            except Exception:
                continue
    for weather, count in counts.most_common():
        print(f"{weather}: {count}回")


def main():
    parser = argparse.ArgumentParser(description="デスクトップにランダム天気アイコンを表示するSkill")
    subparsers = parser.add_subparsers(dest="command")
    parser_run = subparsers.add_parser("run", help="天気アイコンをランダム表示")
    parser_log = subparsers.add_parser("list", help="過去の天気表示履歴を一覧")
    parser_sum = subparsers.add_parser("summary", help="天気表示回数の集計")
    args = parser.parse_args()

    if args.command == "list":
        list_weather_log()
        return
    elif args.command == "summary":
        summary_weather_log()
        return
    # Default: run
    weather = random.choice(WEATHER_TYPES)
    print(f'[INFO] desktop-mood-weather: "{weather["name"]}" アイコンを表示しました')
    img = generate_weather_icon(weather)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        img.save(tmp.name)
        icon_path = tmp.name
    show_desktop_notification(
        title=f"desktop-mood-weather: {weather['name']}",
        message=f"本日の気分天気は「{weather['name']}」です。",
        icon_path=icon_path
    )
    log_weather_event(weather)
    # 一時ファイルは自動削除されません

if __name__ == '__main__':
    main()
