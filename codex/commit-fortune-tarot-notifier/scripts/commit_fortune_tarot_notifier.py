import sys
import os
import random
import subprocess
import argparse
from typing import List

tarot_cards = [
    ("愚者", "愚者が新たな旅路に出た。今日のコミットは冒険の始まり。"),
    ("魔術師", "魔術師が知恵を授ける。創造力が高まる予感。"),
    ("女教皇", "女教皇が静かに見守る。冷静な判断を。"),
    ("女帝", "女帝が豊かさをもたらす。成果が実る兆し。"),
    ("皇帝", "皇帝が統率する。秩序が保たれるだろう。"),
    ("法王", "法王が導く。伝統に従うと吉。"),
    ("恋人たち", "恋人たちが微笑む。協力が成功の鍵。"),
    ("戦車", "戦車が突き進む。勢いに乗って進もう。"),
    ("力", "力がみなぎる。困難も乗り越えられる。"),
    ("隠者", "隠者が静かに歩む。内省の時。"),
    ("運命の輪", "運命の輪が回る。変化の兆し、コードに吉兆あり。"),
    ("正義", "正義が裁く。フェアな判断を心がけて。"),
    ("吊るされた男", "吊るされた男が耐える。辛抱強く待つべし。"),
    ("死神", "死神が通り過ぎる。終わりは新たな始まり。"),
    ("節制", "節制が調和をもたらす。バランス重視で。"),
    ("悪魔", "悪魔が囁く。誘惑に注意。"),
    ("塔", "塔が崩れる。油断大敵、慎重に進め。"),
    ("星", "星が輝く。希望を持って進もう。"),
    ("月", "月が照らす。迷いが生じやすい時期。"),
    ("太陽", "太陽が照りつける。大成功の予感。"),
    ("審判", "審判が下る。過去の努力が報われる。"),
    ("世界", "世界が完成する。プロジェクトの完遂が近い。")
]

def get_random_tarot_message() -> str:
    card, message = random.choice(tarot_cards)
    return f"[タロット占い] {message}"

def print_tarot_message():
    print(get_random_tarot_message())

def notify_desktop(message: str):
    """
    デスクトップ通知を送信（macOS, Linux, Windows対応）
    """
    try:
        if sys.platform == "darwin":
            subprocess.run(["osascript", "-e", f'display notification "{message}" with title "Tarot Commit Fortune"'], check=True)
        elif sys.platform.startswith("linux"):
            subprocess.run(["notify-send", "Tarot Commit Fortune", message], check=True)
        elif sys.platform.startswith("win"):
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("Tarot Commit Fortune", message, duration=5)
        else:
            print(message)
    except Exception:
        print(message)

def is_git_commit_context() -> bool:
    # 環境変数GIT_COMMITTER_NAMEなどで判定
    return os.environ.get('GIT_COMMITTER_NAME') is not None

def cli():
    parser = argparse.ArgumentParser(description="commit-fortune-tarot-notifier: Gitコミット時にタロット風通知を表示")
    subparsers = parser.add_subparsers(dest="command")

    parser_log = subparsers.add_parser('log', help='直近10回のGitコミットでタロット通知を表示')
    parser_notify = subparsers.add_parser('notify', help='タロット通知を1回だけ表示')
    parser_list = subparsers.add_parser('list', help='全タロットカード一覧を表示')
    parser_summary = subparsers.add_parser('summary', help='タロット通知の使い方まとめ')

    args = parser.parse_args()
    if args.command == 'log':
        show_tarot_log()
    elif args.command == 'notify' or args.command is None:
        message = get_random_tarot_message()
        print(message)
        notify_desktop(message)
    elif args.command == 'list':
        for card, message in tarot_cards:
            print(f"{card}: {message}")
    elif args.command == 'summary':
        print_summary()
    else:
        parser.print_help()

def show_tarot_log():
    # git log --pretty=oneline -n 10 を取得
    try:
        result = subprocess.run(["git", "log", "--pretty=oneline", "-n", "10"], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split("\n")
        for line in lines:
            message = get_random_tarot_message()
            print(f"{line[:40]}... {message}")
    except Exception as e:
        print("git logの取得に失敗しました", e)

def print_summary():
    print("""
commit-fortune-tarot-notifier は、Gitコミット時にタロットカード風の謎占い通知を表示するジョークSkillです。
- git commit時に自動で発動、または `python commit_fortune_tarot_notifier.py notify` で明示呼び出し可能
- /skills menu からも利用できます
- 通知は完全ランダムで、実用性はありません
""")

def main():
    # Gitフックから呼ばれた場合は即座に通知
    if is_git_commit_context():
        message = get_random_tarot_message()
        print(message)
        notify_desktop(message)
    else:
        cli()

if __name__ == '__main__':
    main()
