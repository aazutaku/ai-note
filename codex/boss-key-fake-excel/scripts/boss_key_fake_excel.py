import sys
import argparse
import threading
import time
import os

try:
    import PySimpleGUI as sg
except ImportError:
    print("[ERROR] PySimpleGUIが必要です。pip install PySimpleGUI で導入してください。", file=sys.stderr)
    sys.exit(1)

try:
    import pygetwindow as gw
except ImportError:
    print("[ERROR] pygetwindowが必要です。pip install pygetwindow で導入してください。", file=sys.stderr)
    sys.exit(1)

try:
    import keyboard
except ImportError:
    print("[ERROR] keyboardが必要です。pip install keyboard で導入してください。", file=sys.stderr)
    sys.exit(1)

def get_active_window_title():
    try:
        win = gw.getActiveWindow()
        if win:
            return win.title
    except Exception:
        return None
    return None

def hide_active_window():
    win = gw.getActiveWindow()
    if win:
        win.minimize()
        return win
    return None

def restore_window(win):
    try:
        win.restore()
        win.activate()
    except Exception:
        pass

def fake_excel_window():
    sg.theme('SystemDefault')
    menu_def = [['ファイル', ['新規作成', '開く', '保存', '名前を付けて保存', '印刷', '閉じる']],
                ['編集', ['元に戻す', 'やり直し', 'コピー', '貼り付け']],
                ['表示', ['ズーム', 'ウィンドウ']],
                ['ヘルプ', ['バージョン情報']]]

    excel_header = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    excel_data = [[f'セル{r+1}{c+1}' for c in range(len(excel_header))] for r in range(20)]

    layout = [
        [sg.Menu(menu_def, tearoff=False, key='-MENU-')],
        [sg.Text('Book1 - Excel', font=('Segoe UI', 12, 'bold'))],
        [sg.Table(values=excel_data, headings=excel_header, auto_size_columns=True,
                  display_row_numbers=True, num_rows=20, justification='left',
                  enable_events=False, key='-TABLE-', font=('Consolas', 10),
                  alternating_row_color='#F3F3F3', row_height=22)],
        [sg.Text('準備完了', size=(40,1), key='-STATUS-')],
    ]
    window = sg.Window('Microsoft Excel', layout, finalize=True, resizable=True, grab_anywhere=False)
    return window

def listen_shortcut(shortcut, callback):
    def _listen():
        while True:
            keyboard.wait(shortcut)
            callback()
    t = threading.Thread(target=_listen, daemon=True)
    t.start()
    return t

def show_fake_excel():
    print("[INFO] boss-key-fake-excel: フェイクExcel画面を表示しました。")
    print("[INFO] ショートカット: Ctrl+Shift+B で起動、Escで復帰。")
    prev_win = hide_active_window()
    window = fake_excel_window()
    while True:
        event, values = window.read(timeout=100)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Escape:27':
            break
    window.close()
    print("[INFO] 復帰操作を検知、元の作業画面へ戻ります。")
    if prev_win:
        restore_window(prev_win)


def cli_main():
    parser = argparse.ArgumentParser(description='boss-key-fake-excel: 急な来客や上司対策に！Excel風フェイク画面表示ツール')
    subparsers = parser.add_subparsers(dest='command')

    parser_show = subparsers.add_parser('show', help='フェイクExcel画面を表示')
    parser_shortcut = subparsers.add_parser('shortcut', help='ショートカット常駐モード (Ctrl+Shift+B)')
    parser_list = subparsers.add_parser('list', help='現在のウィンドウタイトル取得')
    parser_info = subparsers.add_parser('info', help='Skillの情報を表示')

    args = parser.parse_args()
    if args.command == 'show' or args.command is None:
        show_fake_excel()
    elif args.command == 'shortcut':
        print("[INFO] boss-key-fake-excel: ショートカット常駐モードを起動します。Ctrl+Shift+Bでフェイク画面を表示。")
        def on_shortcut():
            show_fake_excel()
        listen_shortcut('ctrl+shift+b', on_shortcut)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("[INFO] boss-key-fake-excel: 常駐モードを終了します。")
    elif args.command == 'list':
        title = get_active_window_title()
        print(f"[INFO] 現在アクティブなウィンドウ: {title}")
    elif args.command == 'info':
        print("boss-key-fake-excel: 急な来客や上司対策に！Excel風フェイク画面表示ツール")
        print("コマンド例: python boss_key_fake_excel.py show")
        print("ショートカット常駐: python boss_key_fake_excel.py shortcut")
    else:
        parser.print_help()

if __name__ == '__main__':
    cli_main()
