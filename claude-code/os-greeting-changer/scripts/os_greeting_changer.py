import argparse
import random
import sys
from datetime import datetime

def get_fake_os_messages():
    return [
        '[Windows 99] 起動中... 未来への互換性を確認しています。',
        'Macintosh SE/30が時空を超えて復活しました。',
        'Linux UltraLite: コーヒータイム中、しばらくお待ち下さい。',
        'AmigaOS 5.0 (幻覚モード) をロードしています。',
        'BeOS Zeta: あなたのデータを踊らせます。',
        'NeXTstep 4.2: ブラックキューブを回転中。',
        'Solaris 13.1β: 仮想太陽を照射しています。',
        'CP/M 4.4: パンチカードをスキャン中。',
        'MS-DOS 11.0: メモリ管理AIが暴走開始。',
        'OS/2 Warp 5: ワープゲートを開いています。',
        'Haiku OS: 五・七・五でシステム起動。',
        'Plan 9 from Bell Labs: 惑星間ネットワークを構築中。',
        'TempleOS 2.0: 神託を受信しています。',
        'ReactOS 0.9: 反応速度を測定中。',
        'QNX Neutrino: 無重力環境を模倣しています。',
        'Inferno OS: 仮想火炎放射器を点火。',
        'OpenVMS X: 宇宙船の制御パネルを起動。',
        'RISC OS 6.99: ARMで夢を見る。',
        'MorphOS: 変身中...しばらくお待ち下さい。',
        'MINIX 4.0: 教科書的な起動を実演中。',
        'Unix V10: 歴史の彼方から蘇生。',
        'FreeDOS 2025: 未来のコマンドラインを準備中。',
        'Lisp Machine: S式で自己再構成。',
        'Colossal OS: 巨大迷路を生成しています。',
        'Xenix 4000: 秘密のマイクロソフト遺産を発掘中。',
        'SCP Foundation OS: 異常性を封印中。',
        'HyperCard OS: スタックを積み上げています。',
        'VAX/VMS: 仮想アドレス空間を拡張中。',
        'GEOS 2022: グラフィカルな郷愁をロード。',
        'TOS Falcon: MIDI信号を空に放っています。',
        'BASIC-OS: 10 PRINT "HELLO" 20 GOTO 10',
        'DOS/V: 日本語モードで起動中。',
        'Syllable OS: 詩的にシステムを立ち上げています。',
        'Z/OS: メインフレームの夢を見ています。',
        'Multics 2020: セキュリティ層を無限に積み上げ中。',
        'Android 14.0 (Alpha): スマホがPCを支配します。',
        'iOS 17.1: タッチで世界を制御。',
        'Chrome OS 100: ブラウザが全てを支配。',
        'EdgeOS: 境界を越えています。',
        'Fuchsia: 未来色のカーネルを展開中。',
        'NetBSD 10.0: あらゆるものにインストール中。',
        'OpenBSD: セキュリティで囲い込み中。',
        'DragonFly BSD: 仮想ドラゴンが飛翔。',
        'Ghost OS: 幽霊プロセスを呼び出しています。',
        'Quantum OS: 重ね合わせ状態で起動。',
        'Nebula OS: 星雲を形成しています。',
        'ObscureOS: 何も表示しません。',
        'MysticOS: 霧の中から出現。',
        'RetroOS: 8ビットの郷愁を注入。',
        'SynthOS: シンセサイザーで起動音を生成。',
        'ZeroDay OS: 未知のバグを実行中。'
    ]

def print_random_greeting(count=1, quiet=False):
    messages = get_fake_os_messages()
    for _ in range(count):
        msg = random.choice(messages)
        if not quiet:
            print(msg)

def list_all_messages():
    messages = get_fake_os_messages()
    for i, msg in enumerate(messages, 1):
        print(f'{i:02d}: {msg}')

def summary():
    messages = get_fake_os_messages()
    print(f'偽OS起動メッセージ総数: {len(messages)}')
    print('例:')
    for msg in random.sample(messages, min(5, len(messages))):
        print(f'  - {msg}')

def parse_args():
    parser = argparse.ArgumentParser(
        prog='os_greeting_changer',
        description='ターミナル起動時に偽OS起動メッセージをランダム表示するスキル')
    subparsers = parser.add_subparsers(dest='command')

    parser_greet = subparsers.add_parser('greet', help='偽OS起動メッセージを表示 (デフォルト)')
    parser_greet.add_argument('-n', '--number', type=int, default=1, help='表示するメッセージ数')
    parser_greet.add_argument('-q', '--quiet', action='store_true', help='標準出力を抑制')

    parser_list = subparsers.add_parser('list', help='全ての偽OSメッセージを一覧表示')
    parser_summary = subparsers.add_parser('summary', help='メッセージ数や例を要約表示')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.command is None or args.command == 'greet':
        count = getattr(args, 'number', 1)
        quiet = getattr(args, 'quiet', False)
        print_random_greeting(count=count, quiet=quiet)
    elif args.command == 'list':
        list_all_messages()
    elif args.command == 'summary':
        summary()
    else:
        print('不明なコマンドです。-h でヘルプを参照してください。', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'実行時エラー: {e}', file=sys.stderr)
        sys.exit(2)
