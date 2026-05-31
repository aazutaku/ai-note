import os
import sys
import random
import time
import argparse
import threading
from tkinter import Tk, Label, PhotoImage
from PIL import Image, ImageDraw

MOOD_WEATHERS = [
    {"name": "Sunny", "color": "#FFD700", "icon": "sunny.png"},
    {"name": "Cloudy", "color": "#B0C4DE", "icon": "cloudy.png"},
    {"name": "Rain", "color": "#1E90FF", "icon": "rain.png"},
    {"name": "Thunderstorm", "color": "#A9A9A9", "icon": "thunderstorm.png"},
    {"name": "Snow", "color": "#F8F8FF", "icon": "snow.png"},
    {"name": "Fog", "color": "#D3D3D3", "icon": "fog.png"},
    {"name": "Windy", "color": "#87CEEB", "icon": "windy.png"},
    {"name": "Hail", "color": "#E0FFFF", "icon": "hail.png"},
    {"name": "Storm", "color": "#708090", "icon": "storm.png"},
    {"name": "Drizzle", "color": "#ADD8E6", "icon": "drizzle.png"}
]

ICON_SIZE = (96, 96)
ICON_FOLDER = os.path.join(os.path.dirname(__file__), "icons")
UPDATE_INTERVAL = 600  # seconds (10 minutes)


def ensure_icon_folder():
    if not os.path.exists(ICON_FOLDER):
        os.makedirs(ICON_FOLDER)


def generate_icon(weather):
    """簡易的な天気アイコンをPillowで生成し保存"""
    path = os.path.join(ICON_FOLDER, weather["icon"])
    if os.path.exists(path):
        return path
    img = Image.new("RGBA", ICON_SIZE, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    color = weather["color"]
    name = weather["name"]
    # 各天気ごとに簡単なアイコン描画
    if name == "Sunny":
        draw.ellipse([16, 16, 80, 80], fill=color, outline="#FFA500", width=4)
    elif name == "Cloudy":
        draw.ellipse([20, 40, 76, 76], fill=color, outline="#808080", width=3)
    elif name == "Rain":
        draw.ellipse([28, 36, 68, 68], fill="#B0C4DE")
        for i in range(4):
            draw.line([36 + i*10, 68, 36 + i*10, 90], fill="#1E90FF", width=3)
    elif name == "Thunderstorm":
        draw.ellipse([22, 40, 74, 74], fill="#A9A9A9")
        draw.polygon([(48, 60), (60, 80), (52, 80), (64, 94), (48, 76), (56, 76)], fill="#FFD700")
    elif name == "Snow":
        draw.ellipse([28, 40, 68, 68], fill="#F8F8FF")
        for i in range(3):
            draw.line([48, 68, 48 + (i-1)*12, 90], fill="#B0C4DE", width=2)
    elif name == "Fog":
        for i in range(3):
            draw.rectangle([24, 40 + i*14, 72, 50 + i*14], fill="#D3D3D3")
    elif name == "Windy":
        for i in range(2):
            draw.arc([24, 48 + i*16, 72, 80 + i*16], 0, 180, fill="#87CEEB", width=4)
    elif name == "Hail":
        draw.ellipse([32, 44, 64, 68], fill="#E0FFFF")
        for i in range(3):
            draw.ellipse([40 + i*8, 72, 46 + i*8, 78], fill="#A9A9A9")
    elif name == "Storm":
        draw.ellipse([20, 44, 76, 76], fill="#708090")
        draw.line([36, 76, 60, 94], fill="#FFD700", width=3)
    elif name == "Drizzle":
        draw.ellipse([30, 48, 66, 70], fill="#ADD8E6")
        for i in range(2):
            draw.line([42 + i*10, 70, 42 + i*10, 86], fill="#1E90FF", width=2)
    img.save(path)
    return path


def pick_random_weather():
    return random.choice(MOOD_WEATHERS)


def get_screen_geometry():
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.destroy()
        return width, height
    except Exception:
        return 1920, 1080


def show_weather_icon(weather, duration=UPDATE_INTERVAL):
    """Tkinterでデスクトップ右下にアイコンを表示"""
    icon_path = generate_icon(weather)
    root = Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.withdraw()
    screen_w, screen_h = get_screen_geometry()
    x = screen_w - ICON_SIZE[0] - 24
    y = screen_h - ICON_SIZE[1] - 64
    root.geometry(f"{ICON_SIZE[0]}x{ICON_SIZE[1]}+{x}+{y}")
    img = PhotoImage(file=icon_path)
    label = Label(root, image=img, bg='white')
    label.pack()
    root.deiconify()
    def close():
        root.destroy()
    root.after(duration * 1000, close)
    root.mainloop()


def log_weather(weather):
    log_path = os.path.join(os.path.dirname(__file__), "mood_weather.log")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[INFO] mood-weather: Current mood weather is '{weather['name']}'\n")
        f.write(f"[INFO] mood-weather: Displayed icon: {weather['icon']}\n")


def run_loop(interval=UPDATE_INTERVAL):
    ensure_icon_folder()
    while True:
        weather = pick_random_weather()
        log_weather(weather)
        t = threading.Thread(target=show_weather_icon, args=(weather, 10))
        t.start()
        time.sleep(interval)


def list_icons():
    ensure_icon_folder()
    print("Available mood weather icons:")
    for w in MOOD_WEATHERS:
        path = generate_icon(w)
        print(f"- {w['name']}: {path}")


def summary():
    print("desktop-mood-weather: Shows a random mood weather icon on your desktop corner.")
    print(f"Weathers: {[w['name'] for w in MOOD_WEATHERS]}")
    print(f"Icon folder: {ICON_FOLDER}")
    print(f"Update interval: {UPDATE_INTERVAL} seconds")


def parse_args():
    parser = argparse.ArgumentParser(description="Desktop Mood Weather - Random mood weather icon on your desktop.")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Start the mood weather loop")
    run_parser.add_argument("--interval", type=int, default=UPDATE_INTERVAL, help="Update interval in seconds")

    subparsers.add_parser("list", help="List available weather icons")
    subparsers.add_parser("summary", help="Show skill summary")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == "run":
        run_loop(args.interval)
    elif args.command == "list":
        list_icons()
    elif args.command == "summary":
        summary()
    else:
        print("No command specified. Use --help for usage.")

if __name__ == '__main__':
    main()
