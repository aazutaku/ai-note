import sys
import argparse
import random
import time
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
try:
    import pygetwindow as gw
except ImportError:
    gw = None

DUMMY_SCREEN_TYPES = [
    'fake_os_alert',
    'nonsense_graph',
    'random_table',
    'weird_progress',
    'absurd_dashboard',
]

FAKE_ERRORS = [
    'Error: 0xDEADBEEF - Unknown Kernel Panic',
    'System Alert: Recursive NullPointerException',
    'Critical Failure: Quantum Entanglement Lost',
    'Warning: Unlicensed Potato Detected',
    'Error: Infinite Loop in Process Scheduler',
]

RANDOM_TABLE_HEADERS = [
    ['ID', 'Flux', 'Entropy', 'Status'],
    ['Node', 'Ping', 'Latency', 'Mood'],
    ['Task', 'Priority', 'Obfuscation', 'Result'],
]

DASHBOARD_LABELS = [
    'Synergy Index', 'Chaos Quotient', 'Obfuscation Rate', 'Entropy', 'Randomness'
]

class DummyScreen:
    def __init__(self, root, screen_type):
        self.root = root
        self.screen_type = screen_type
        self.frame = tk.Frame(root, bg='black')
        self.frame.pack(fill='both', expand=True)
        self.content_widgets = []
        if screen_type == 'fake_os_alert':
            self._show_fake_os_alert()
        elif screen_type == 'nonsense_graph':
            self._show_nonsense_graph()
        elif screen_type == 'random_table':
            self._show_random_table()
        elif screen_type == 'weird_progress':
            self._show_weird_progress()
        elif screen_type == 'absurd_dashboard':
            self._show_absurd_dashboard()

    def _show_fake_os_alert(self):
        msg = random.choice(FAKE_ERRORS)
        label = tk.Label(self.frame, text=msg, fg='red', bg='black', font=('Consolas', 24, 'bold'))
        label.pack(expand=True)
        self.content_widgets.append(label)

    def _show_nonsense_graph(self):
        fig, ax = plt.subplots(figsize=(6, 4))
        x = list(range(10))
        y = [random.uniform(-10, 10) for _ in x]
        ax.plot(x, y, color='purple', marker='o')
        ax.set_title('Quantum Nonsense Trend')
        ax.set_xlabel('Obfuscation Level')
        ax.set_ylabel('Entropy')
        plt.tight_layout()
        fig.canvas.draw()
        fig.savefig('dummy_graph.png')
        plt.close(fig)
        img = Image.open('dummy_graph.png')
        img = img.resize((600, 400))
        tk_img = ImageTk.PhotoImage(img)
        panel = tk.Label(self.frame, image=tk_img, bg='black')
        panel.image = tk_img
        panel.pack(expand=True)
        self.content_widgets.append(panel)

    def _show_random_table(self):
        headers = random.choice(RANDOM_TABLE_HEADERS)
        tree = ttk.Treeview(self.frame, columns=headers, show='headings', height=10)
        for h in headers:
            tree.heading(h, text=h)
            tree.column(h, anchor='center', width=120)
        for i in range(10):
            row = [str(random.randint(1000, 9999)),
                   f'{random.uniform(0, 100):.2f}',
                   f'{random.uniform(-50, 50):.2f}',
                   random.choice(['OK', 'FAIL', '???'])]
            tree.insert('', 'end', values=row)
        tree.pack(expand=True, fill='both')
        self.content_widgets.append(tree)

    def _show_weird_progress(self):
        label = tk.Label(self.frame, text='Processing: Entropy Alignment', fg='white', bg='black', font=('Arial', 18, 'bold'))
        label.pack(pady=30)
        pb = ttk.Progressbar(self.frame, orient='horizontal', mode='determinate', length=400)
        pb.pack(pady=10)
        self.content_widgets.append(pb)
        self.content_widgets.append(label)
        def animate():
            for i in range(0, 101, random.randint(7, 15)):
                pb['value'] = i
                self.root.update()
                time.sleep(random.uniform(0.05, 0.18))
            pb['value'] = 100
        threading.Thread(target=animate, daemon=True).start()

    def _show_absurd_dashboard(self):
        for label in DASHBOARD_LABELS:
            val = f'{random.uniform(10, 100):.2f}'
            l = tk.Label(self.frame, text=f'{label}: {val}', fg='lime', bg='black', font=('Courier', 20, 'bold'))
            l.pack(anchor='w', padx=40, pady=5)
            self.content_widgets.append(l)

    def destroy(self):
        for w in self.content_widgets:
            w.destroy()
        self.frame.destroy()


def hide_active_window():
    if gw is None:
        print('[WARN] pygetwindow not installed, cannot hide window')
        return None
    try:
        win = gw.getActiveWindow()
        if win:
            print(f'[DEBUG] Hiding active window: {win.title}')
            win.minimize()
            return win
        else:
            print('[WARN] No active window found')
    except Exception as e:
        print(f'[ERROR] Failed to hide window: {e}')
    return None

def restore_window(win):
    if win is None:
        return
    try:
        win.restore()
        win.activate()
        print('[INFO] Returning to original window.')
    except Exception as e:
        print(f'[ERROR] Failed to restore window: {e}')

def show_dummy_screen(screen_type, duration=10):
    root = tk.Tk()
    root.title('')
    root.configure(bg='black')
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    ds = DummyScreen(root, screen_type)
    def close_after():
        time.sleep(duration)
        root.quit()
    threading.Thread(target=close_after, daemon=True).start()
    root.mainloop()
    ds.destroy()
    root.destroy()

def main():
    parser = argparse.ArgumentParser(description='Random OS Sudden Boss Key')
    parser.add_argument('--duration', type=int, default=10, help='Dummy screen display duration (sec)')
    parser.add_argument('--type', type=str, choices=DUMMY_SCREEN_TYPES + ['random'], default='random', help='Type of dummy screen')
    parser.add_argument('command', nargs='?', default='activate', choices=['activate', 'test', 'list'], help='Command')
    args = parser.parse_args()

    if args.command == 'list':
        print('Available dummy screen types:')
        for t in DUMMY_SCREEN_TYPES:
            print(f' - {t}')
        sys.exit(0)
    if args.command == 'test':
        for t in DUMMY_SCREEN_TYPES:
            print(f'[TEST] Showing: {t}')
            show_dummy_screen(t, duration=3)
        sys.exit(0)
    # activate
    print('[INFO] Sudden Boss Key Activated!')
    win = hide_active_window()
    stype = random.choice(DUMMY_SCREEN_TYPES) if args.type == 'random' else args.type
    print(f'[DEBUG] Displaying dummy screen: [{stype}]')
    show_dummy_screen(stype, duration=args.duration)
    restore_window(win)

if __name__ == '__main__':
    main()
