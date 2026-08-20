import argparse
import random
import sys
import time
import os
import threading

DASHBOARD_TEMPLATES = [
    {
        'title': 'Fake Report Dashboard',
        'sections': [
            lambda: f"- Sales Growth: {random.uniform(5.0, 15.0):.1f}% (Q{random.choice([1,2,3,4])})",
            lambda: f"- Customer Churn: {random.uniform(1.0, 5.0):.1f}%",
            lambda: f"- Active Users: {random.randint(1000, 5000)}",
            lambda: fake_bar_graph("Revenue vs. Time"),
        ]
    },
    {
        'title': 'Quarterly KPI Monitor',
        'sections': [
            lambda: f"- Net Promoter Score: {random.randint(30, 80)}",
            lambda: f"- Ticket Resolution Time: {random.randint(2, 24)} hours",
            lambda: f"- Uptime: {random.uniform(99.0, 99.99):.2f}%",
            lambda: fake_bar_graph("Tickets Closed"),
        ]
    },
    {
        'title': 'Project Progress Overview',
        'sections': [
            lambda: f"- Completed Tasks: {random.randint(50, 200)}",
            lambda: f"- Remaining Tasks: {random.randint(5, 30)}",
            lambda: f"- Milestone: {random.choice(['Design', 'Development', 'QA', 'Release'])}",
            lambda: fake_progress_bar("Overall Progress"),
        ]
    },
]

def fake_bar_graph(title):
    bars = [random.randint(5, 20) for _ in range(3)]
    labels = ["2023Q1", "2023Q2", "2023Q3"]
    graph = f"[Graph: {title}]\n"
    for i, bar in enumerate(bars):
        graph += "█" * bar + f" {labels[i]}\n"
    return graph.strip()

def fake_progress_bar(title):
    percent = random.randint(30, 100)
    bar = "█" * (percent // 5) + "-" * ((100 - percent) // 5)
    return f"[Progress: {title}]\n[{bar}] {percent}%"

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_fake_dashboard():
    dashboard = random.choice(DASHBOARD_TEMPLATES)
    clear_screen()
    print(f"[{dashboard['title']}]\n")
    for section in dashboard['sections']:
        print(section())
    print("[End of Report]")

def restore_previous_screen():
    clear_screen()
    print("[Restored previous screen]")

def listen_for_restore(timeout=0):
    try:
        if timeout > 0:
            time.sleep(timeout)
            restore_previous_screen()
            return
        print("\nPress Enter to restore your screen...")
        input()
        restore_previous_screen()
    except KeyboardInterrupt:
        restore_previous_screen()


def main():
    parser = argparse.ArgumentParser(description='random-os-fake-boss-key: Generate and show a fake business dashboard.')
    subparsers = parser.add_subparsers(dest='command')

    show_parser = subparsers.add_parser('show', help='Show a random fake dashboard')
    show_parser.add_argument('--auto-restore', type=int, default=0, help='Auto-restore after N seconds (default: manual restore)')

    restore_parser = subparsers.add_parser('restore', help='Restore the previous screen immediately')

    args = parser.parse_args()

    if args.command == 'show':
        show_fake_dashboard()
        listen_for_restore(timeout=args.auto_restore)
    elif args.command == 'restore':
        restore_previous_screen()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
