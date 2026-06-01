import sys
import os
import argparse
import datetime
import threading
from tkinter import Tk, Canvas, PhotoImage, NW, Label, Button
from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageGrab

FAKE_EXCEL_BG = (245, 245, 245)
EXCEL_GREEN = (0, 176, 80)
HEADER_BG = (222, 234, 246)
GRID_COLOR = (200, 200, 200)
FONT_PATH = None  # Use default font

FAKE_TITLE = "Microsoft Excel - sales_report.xlsx"

class BossKeyFakeExcel:
    def __init__(self):
        self.root = None
        self.img = None
        self.photo = None
        self.screenshot_path = None

    def take_screenshot(self):
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        tmp_path = f"/tmp/bosskey_backup_{now}.png"
        try:
            img = ImageGrab.grab()
            img.save(tmp_path)
            self.screenshot_path = tmp_path
            print(f"[DEBUG] Screenshot of current desktop saved to: {tmp_path}")
        except Exception as e:
            print(f"[WARN] Screenshot failed: {e}")

    def generate_fake_excel_img(self, width=1280, height=720, rows=18, cols=12):
        img = Image.new('RGB', (width, height), FAKE_EXCEL_BG)
        draw = ImageDraw.Draw(img)
        # Title bar
        draw.rectangle([0, 0, width, 40], fill=EXCEL_GREEN)
        font = self.get_font(18, bold=True)
        draw.text((12, 8), FAKE_TITLE, fill='white', font=font)
        # Fake window buttons
        draw.ellipse([width-90, 10, width-70, 30], fill=(232,17,35))  # Close
        draw.ellipse([width-65, 10, width-45, 30], fill=(255,185,0))  # Maximize
        draw.ellipse([width-40, 10, width-20, 30], fill=(0,120,215))  # Minimize
        # Ribbon
        draw.rectangle([0, 40, width, 90], fill=HEADER_BG)
        ribbon_font = self.get_font(14)
        draw.text((20, 55), "ファイル  ホーム  挿入  ページレイアウト  数式  データ  校閲  表示", fill=(40,40,40), font=ribbon_font)
        # Sheet grid
        grid_top = 100
        grid_left = 60
        cell_w = (width - grid_left - 20) // cols
        cell_h = (height - grid_top - 40) // rows
        # Column headers
        header_font = self.get_font(12, bold=True)
        for c in range(cols):
            x = grid_left + c*cell_w
            draw.rectangle([x, grid_top-25, x+cell_w, grid_top], fill=HEADER_BG)
            col_label = chr(65+c)
            draw.text((x+cell_w//2-7, grid_top-22), col_label, fill=(0,0,0), font=header_font)
        # Row headers
        for r in range(rows):
            y = grid_top + r*cell_h
            draw.rectangle([0, y, grid_left, y+cell_h], fill=HEADER_BG)
            draw.text((grid_left//2-10, y+cell_h//2-8), str(r+1), fill=(0,0,0), font=header_font)
        # Draw grid
        for r in range(rows+1):
            y = grid_top + r*cell_h
            draw.line([grid_left, y, grid_left+cols*cell_w, y], fill=GRID_COLOR)
        for c in range(cols+1):
            x = grid_left + c*cell_w
            draw.line([x, grid_top, x, grid_top+rows*cell_h], fill=GRID_COLOR)
        # Fake data
        data_font = self.get_font(11)
        for r in range(rows):
            for c in range(cols):
                val = ""
                if c == 0 and r > 0:
                    val = f"商品{r}"
                elif r == 0 and c > 0:
                    val = ["売上","利益","数量","単価","原価","在庫","発注","納期","担当","備考","評価"][c-1] if c-1 < 11 else ""
                elif r > 0 and c > 0:
                    val = str(1000 + r*100 + c*10)
                if val:
                    x = grid_left + c*cell_w + 8
                    y = grid_top + r*cell_h + 6
                    draw.text((x, y), val, fill=(40,40,40), font=data_font)
        # Sheet tabs
        tab_y = grid_top + rows*cell_h + 10
        for i, name in enumerate(["Sheet1", "Sheet2", "集計"]):
            tab_x = grid_left + i*100
            draw.rectangle([tab_x, tab_y, tab_x+80, tab_y+28], fill=(255,255,255), outline=(150,150,150))
            draw.text((tab_x+18, tab_y+6), name, fill=(0,0,0), font=self.get_font(12))
        return img

    def get_font(self, size, bold=False):
        try:
            if FONT_PATH:
                return ImageFont.truetype(FONT_PATH, size)
            else:
                if bold:
                    return ImageFont.truetype("arialbd.ttf", size)
                else:
                    return ImageFont.truetype("arial.ttf", size)
        except:
            return ImageFont.load_default()

    def launch_window(self):
        self.root = Tk()
        self.root.title(FAKE_TITLE)
        width, height = 1280, 720
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        self.img = self.generate_fake_excel_img(width, height)
        self.photo = ImageTk.PhotoImage(self.img)
        canvas = Canvas(self.root, width=width, height=height)
        canvas.pack()
        canvas.create_image(0, 0, anchor=NW, image=self.photo)
        # Close button
        close_btn = Button(self.root, text="×", command=self.root.quit, bg="#e81123", fg="white", font=("Arial", 12, "bold"))
        close_btn.place(x=width-40, y=5, width=30, height=30)
        # Keyboard shortcut
        self.root.bind('<Control-q>', lambda e: self.root.quit())
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit)
        print("[INFO] Fake Excel window launched. Press Ctrl+Q or close window to return.")
        self.root.mainloop()
        print("[INFO] Excel-style window closed. Restoring previous state.")

    def run(self):
        self.take_screenshot()
        self.launch_window()


def main():
    parser = argparse.ArgumentParser(description="瞬時にExcel風フェイク画面を表示するBossKeyスクリプト")
    parser.add_argument('--log', action='store_true', help='起動・終了ログを出力')
    parser.add_argument('--screenshot-only', action='store_true', help='画面キャプチャのみ')
    args = parser.parse_args()
    bk = BossKeyFakeExcel()
    if args.screenshot_only:
        bk.take_screenshot()
        print(f"Screenshot saved to: {bk.screenshot_path}")
        return
    if args.log:
        print(f"[INFO] boss-key-fake-excel started at {datetime.datetime.now()}")
    bk.run()
    if args.log:
        print(f"[INFO] boss-key-fake-excel ended at {datetime.datetime.now()}")

if __name__ == '__main__':
    main()
