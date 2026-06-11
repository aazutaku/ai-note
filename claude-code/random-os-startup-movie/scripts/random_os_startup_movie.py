import sys
import time
import random
import argparse

FAKE_OS_NAMES = [
    'Windows 11.5', 'Antigravity 3000', 'Codex Limited Edition', 'QuantumOS X',
    'NeuralVerse 2.0', 'Hypervisor Ultra', 'DreamShell', 'BitSynth Prime',
    'NanoKernel 9', 'PlasmaGate', 'VoidOS', 'AI-Genesis', 'Simulacrum OS',
    'MetaFrame', 'InfinityNode', 'ChronOS', 'SpectraOS', 'Hyperloop OS',
    'Phantom Kernel', 'Singularity Lite'
]

PROGRESS_ACTIONS = [
    'ビットを配置中', 'AIを目覚めさせています', '量子メモリを初期化中',
    'プロトコルを同期中', '仮想空間を展開中', 'モジュールを量子展開中',
    'パラメータを乱数化中', 'シミュレーションを起動', 'アルゴリズムを最適化',
    'ロジックゲートを再構成中', 'セキュリティホログラムを生成',
    '未知のデバイスを認識中', 'エントロピーを注入',
    'メタデータを暗号化', '未知のエラーを検出', '仮想人格をロード',
    '時空間キャッシュを初期化', 'ノードを再配線', 'ブラックボックスを起動',
    'パケットを転送', 'AIコアを冷却', 'オーバークロック中',
    'システム境界を拡張', 'サブプロセスを増殖', '未知のOSと通信中'
]

WELCOME_MESSAGES = [
    'System Ready. Welcome, Operator.',
    '起動完了。ようこそ、管理者様。',
    'Initialization complete. Awaiting input.',
    'All systems nominal. Proceed.',
    '準備完了。新しいセッションを開始します。',
    'Access granted. Terminal unlocked.',
    'Simulation loaded. Entering mainframe.',
    'セキュアモードで起動しました。',
    '全プロトコル正常。操作をどうぞ。',
    'Ready for your commands.'
]

def random_os_name():
    return random.choice(FAKE_OS_NAMES)

def random_progress_action():
    return random.choice(PROGRESS_ACTIONS)

def random_welcome():
    return random.choice(WELCOME_MESSAGES)

def generate_progress_bar(progress, bar_length=22):
    filled = int(bar_length * progress // 100)
    bar = '█' * filled + '▒' * (bar_length - filled)
    return f'| {bar} | {progress}%'

def print_startup_movie(sleep_time=0.15, fast=False):
    os_name = random_os_name()
    print(f'[{os_name}] 起動中...')
    print('-' * 31)
    progress = 0
    actions = random.sample(PROGRESS_ACTIONS, k=4)
    for i, action in enumerate(actions):
        increment = random.randint(10, 35)
        progress = min(progress + increment, 100)
        print(generate_progress_bar(progress))
        print(f'| {action}')
        if not fast:
            time.sleep(sleep_time * (1 + random.random()))
    print('-' * 31)
    print(random_welcome())

def list_os_names():
    print('利用可能な架空OS名一覧:')
    for name in FAKE_OS_NAMES:
        print(f'- {name}')

def list_actions():
    print('進捗アクション例:')
    for action in PROGRESS_ACTIONS:
        print(f'- {action}')

def main():
    parser = argparse.ArgumentParser(
        description='毎回異なる架空OSの起動画面をテキストアニメーションで表示するスキル')
    subparsers = parser.add_subparsers(dest='command')

    parser_run = subparsers.add_parser('run', help='架空OS起動画面を表示')
    parser_run.add_argument('--fast', action='store_true', help='アニメーションを高速化')

    parser_list_os = subparsers.add_parser('list-os', help='架空OS名一覧を表示')
    parser_list_actions = subparsers.add_parser('list-actions', help='進捗アクション一覧を表示')

    args = parser.parse_args()
    if args.command == 'run' or args.command is None:
        try:
            print_startup_movie(fast=(getattr(args, 'fast', False)))
        except KeyboardInterrupt:
            print('\n[中断されました]')
            sys.exit(1)
    elif args.command == 'list-os':
        list_os_names()
    elif args.command == 'list-actions':
        list_actions()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
