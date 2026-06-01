import sys
import argparse
import threading
import time
import os
import signal
from PIL import Image, ImageDraw, ImageFont
import PySimpleGUI as sg
try:
    import keyboard
except ImportError:
    keyboard = None
try:
    import pygetwindow as gw
except ImportError:
    gw = None

def generate_fake_excel_image(width=900, height=500, rows=18, cols=10):
    # Create a white canvas
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    # Draw Excel-like header
    header_height = 38
    draw.rectangle([0, 0, width, header_height], fill=(217, 225, 242))
    try:
        font = ImageFont.truetype('arial.ttf', 18)
        font_small = ImageFont.truetype('arial.ttf', 13)
    except:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()
    # Draw title
    draw.text((20, 8), 'Microsoft Excel - 売上管理表.xlsx', fill=(0, 0, 0), font=font)
    # Draw column headers (A, B, C...)
    col_w = (width - 50) // cols
    for c in range(cols):
        x = 50 + c * col_w
        draw.rectangle([x, header_height, x + col_w, header_height + 28], fill=(184, 204, 228), outline=(150, 150, 150))
        col_name = chr(65 + c)
        draw.text((x + col_w // 2 - 5, header_height + 6), col_name, fill=(0, 0, 0), font=font_small)
    # Draw row headers (1,2...)
    row_h = (height - header_height - 28) // rows
    for r in range(rows):
        y = header_height + 28 + r * row_h
        draw.rectangle([0, y, 50, y + row_h], fill=(184, 204, 228), outline=(150, 150, 150))
        draw.text((20, y + row_h // 2 - 7), str(r + 1), fill=(0, 0, 0), font=font_small)
    # Draw grid
    for r in range(rows):
        for c in range(cols):
            x = 50 + c * col_w
            y = header_height + 28 + r * row_h
            draw.rectangle([x, y, x + col_w, y + row_h], outline=(200, 200, 200))
    # Fake content
    sample_cells = [(0, 0, '日付'), (0, 1, '商品'), (0, 2, '数量'), (0, 3, '単価'), (0, 4, '金額'),
                   (1, 0, '2024/06/01'), (1, 1, 'ノートPC'), (1, 2, '2'), (1, 3, '120000'), (1, 4, '240000'),
                   (2, 0, '2024/06/02'), (2, 1, 'マウス'), (2, 2, '5'), (2, 3, '2000'), (2, 4, '10000')]
    for r, c, val in sample_cells:
        x = 50 + c * col_w + 4
        y = header_height + 28 + r * row_h + 4
        draw.text((x, y), val, fill=(0, 0, 0), font=font_small)
    return img

def show_fake_excel_window():
    img = generate_fake_excel_image()
    tmpfile = '._bosskey_excel_tmp.png'
    img.save(tmpfile)
    layout = [
        [sg.Image(filename=tmpfile, key='-IMAGE-')],
        [sg.Text('Esc または Ctrl+Shift+E で元の画面に戻ります', font=('Arial', 11), pad=((5,5),(5,5)))]
    ]
    window = sg.Window('Microsoft Excel - 売上管理表.xlsx', layout, finalize=True, keep_on_top=True, margins=(0,0), no_titlebar=False, grab_anywhere=True)
    # Focus window
    window.bring_to_front()
    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED:
            break
        if keyboard:
            if keyboard.is_pressed('esc') or (keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift') and keyboard.is_pressed('e')):
                break
    window.close()
    if os.path.exists(tmpfile):
        os.remove(tmpfile)

def find_and_hide_active_window():
    if gw is None:
        print('[WARN] pygetwindowが未インストールのためウィンドウ切り替えはスキップされます')
        return None
    try:
        win = gw.getActiveWindow()
        if win:
            win.minimize()
            return win
    except Exception as e:
        print(f'[ERROR] アクティブウィンドウ取得失敗: {e}')
    return None

def restore_window(win):
    if win is None:
        return
    try:
        win.restore()
        win.activate()
    except Exception as e:
        print(f'[ERROR] ウィンドウ復帰失敗: {e}')

def boss_key_action():
    print('[INFO] boss-key-fake-excel: フェイクExcel画面を表示します。')
    win = find_and_hide_active_window()
    show_fake_excel_window()
    restore_window(win)
    print('[INFO] 元の作業画面に復帰しました。')

def shortcut_listener():
    if keyboard is None:
        print('[WARN] keyboardパッケージが未インストールのためショートカット監視は無効です')
        return
    print('[INFO] Ctrl+Shift+E でフェイクExcel画面を即時表示します。')
    while True:
        try:
            keyboard.wait('ctrl+shift+e')
            boss_key_action()
            time.sleep(0.5)  # 連打防止
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f'[ERROR] ショートカット監視中に例外: {e}')
            break

def main():
    parser = argparse.ArgumentParser(description='boss-key-fake-excel: フェイクExcel画面を即時表示するスクリプト')
    subparsers = parser.add_subparsers(dest='command')
    parser_run = subparsers.add_parser('run', help='ショートカット監視でboss keyを有効化')
    parser_show = subparsers.add_parser('show', help='即座にフェイクExcel画面を表示')
    args = parser.parse_args()
    if args.command == 'run':
        shortcut_listener()
    elif args.command == 'show':
        boss_key_action()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
