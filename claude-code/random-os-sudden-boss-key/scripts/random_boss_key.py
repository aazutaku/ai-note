import sys
import argparse
import threading
import random
import time
import tkinter as tk
from tkinter import messagebox
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import io

DUMMY_WARNINGS = [
    'OS Error: 0xDEADBEEF\nSystem integrity check failed.',
    'Critical Failure!\nUnable to allocate quantum buffer.',
    'Warning: Null pointer dereferenced.',
    'Security Alert: Suspicious process detected.',
    'Kernel Panic: Unhandled exception in module.',
    'Memory Leak Detected!\nPlease restart your system.',
    'System Overload: Too many open files.',
]

DUMMY_CHART_LABELS = [
    ['Foo', 'Bar', 'Baz', 'Qux'],
    ['Alpha', 'Beta', 'Gamma', 'Delta'],
    ['Red', 'Green', 'Blue', 'Yellow'],
    ['Cat', 'Dog', 'Fish', 'Bird'],
]

class DummyScreen:
    def __init__(self, duration=5):
        self.duration = duration
        self.root = None
        self.closed = threading.Event()

    def show_random(self):
        # Decide randomly: warning or chart
        if random.choice([True, False]):
            self.show_warning()
        else:
            self.show_chart()

    def show_warning(self):
        self.root = tk.Tk()
        self.root.title('System Warning')
        self.root.geometry('480x240')
        self.root.attributes('-topmost', True)
        self.root.protocol('WM_DELETE_WINDOW', self.close)
        msg = random.choice(DUMMY_WARNINGS)
        label = tk.Label(self.root, text='=== WARNING ===\n' + msg + '\n', font=('Consolas', 14), fg='red')
        label.pack(pady=30)
        btn = tk.Button(self.root, text='OK', command=self.close)
        btn.pack(pady=20)
        self.root.bind('<Key>', lambda e: self.close())
        self._auto_close()
        self.root.mainloop()

    def show_chart(self):
        # Generate random chart
        labels = random.choice(DUMMY_CHART_LABELS)
        values = [random.randint(1, 100) for _ in labels]
        fig, ax = plt.subplots(figsize=(5, 2.5))
        ax.bar(labels, values, color=[random.choice(['#e74c3c', '#3498db', '#2ecc71', '#f1c40f']) for _ in labels])
        ax.set_title('RANDOM DATA CHART')
        ax.set_ylabel('Value')
        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close(fig)
        buf.seek(0)
        img = Image.open(buf)
        self.root = tk.Tk()
        self.root.title('Data Dashboard')
        self.root.geometry('520x300')
        self.root.attributes('-topmost', True)
        self.root.protocol('WM_DELETE_WINDOW', self.close)
        tkimg = ImageTk.PhotoImage(img)
        panel = tk.Label(self.root, image=tkimg)
        panel.image = tkimg
        panel.pack(pady=10)
        btn = tk.Button(self.root, text='Close', command=self.close)
        btn.pack(pady=10)
        self.root.bind('<Key>', lambda e: self.close())
        self._auto_close()
        self.root.mainloop()

    def _auto_close(self):
        def timer():
            time.sleep(self.duration)
            if not self.closed.is_set():
                try:
                    self.root.after(0, self.close)
                except Exception:
                    pass
        threading.Thread(target=timer, daemon=True).start()

    def close(self):
        self.closed.set()
        if self.root:
            self.root.destroy()


def main():
    parser = argparse.ArgumentParser(description='Random OS Sudden Boss Key')
    parser.add_argument('--mode', choices=['auto', 'warning', 'chart'], default='auto', help='Dummy screen type')
    parser.add_argument('--duration', type=int, default=5, help='Display seconds (default: 5)')
    parser.add_argument('--list', action='store_true', help='List all dummy patterns')
    args = parser.parse_args()

    if args.list:
        print('=== Dummy Warnings ===')
        for w in DUMMY_WARNINGS:
            print('-', w)
        print('\n=== Dummy Chart Label Sets ===')
        for labels in DUMMY_CHART_LABELS:
            print('-', ', '.join(labels))
        sys.exit(0)

    ds = DummyScreen(duration=args.duration)
    if args.mode == 'auto':
        ds.show_random()
    elif args.mode == 'warning':
        ds.show_warning()
    elif args.mode == 'chart':
        ds.show_chart()

if __name__ == '__main__':
    main()
