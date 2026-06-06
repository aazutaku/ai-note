import argparse
import sys
import traceback
import re

ERROR_HAIKU_MAP = [
    {
        'pattern': re.compile(r'Permission denied', re.IGNORECASE),
        'haiku': ['扉閉ざす', '許されぬ道', '春霞']
    },
    {
        'pattern': re.compile(r'No such file or directory', re.IGNORECASE),
        'haiku': ['探しもの', '風に消えゆく', '幻影よ']
    },
    {
        'pattern': re.compile(r'Segmentation fault', re.IGNORECASE),
        'haiku': ['記憶の彼方', '断絶の響き', '絶望感']
    },
    {
        'pattern': re.compile(r'File exists', re.IGNORECASE),
        'haiku': ['重ね書き', '運命重なる', '秋の夜']
    },
    {
        'pattern': re.compile(r'Is a directory', re.IGNORECASE),
        'haiku': ['道を誤る', 'ファイルの森で', '迷い道']
    },
    {
        'pattern': re.compile(r'Not a directory', re.IGNORECASE),
        'haiku': ['道なき道', '彷徨う心', '冬の空']
    },
    {
        'pattern': re.compile(r'Connection refused', re.IGNORECASE),
        'haiku': ['門は固く', '届かぬ思い', '雨しずく']
    },
    {
        'pattern': re.compile(r'Broken pipe', re.IGNORECASE),
        'haiku': ['途切れし線', '伝わらぬ声', '秋の風']
    },
    {
        'pattern': re.compile(r'Operation not permitted', re.IGNORECASE),
        'haiku': ['許されぬ', '静かなる拒絶', '朝の霧']
    },
    {
        'pattern': re.compile(r'Input/output error', re.IGNORECASE),
        'haiku': ['響かぬ声', '沈黙の海', '波の音']
    }
]

DEFAULT_HAIKU = ['未知の闇', '理由もわからず', '夜が更ける']


def match_haiku(error_msg):
    for entry in ERROR_HAIKU_MAP:
        if entry['pattern'].search(error_msg):
            return entry['haiku']
    return DEFAULT_HAIKU


def format_haiku(error_msg):
    haiku = match_haiku(error_msg)
    return f"[OS Error Haiku]\n元メッセージ: {error_msg}\n俳句:  \n" + "  \n".join(haiku)


def simulate_error(error_msg):
    print(format_haiku(error_msg))


def wrap_stdin():
    """
    標準入力からエラーらしき行を検出し、俳句化して表示
    """
    for line in sys.stdin:
        line = line.rstrip('\n')
        if is_error_line(line):
            print(format_haiku(line))
        else:
            print(line)


def is_error_line(line):
    # 主要なエラーパターンにマッチするか
    for entry in ERROR_HAIKU_MAP:
        if entry['pattern'].search(line):
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description='OSエラー俳句変換ツール')
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_run = subparsers.add_parser('run', help='エラーメッセージを俳句化して表示')
    parser_run.add_argument('--simulate', type=str, help='エラーメッセージを直接指定')
    parser_run.add_argument('--stdin', action='store_true', help='標準入力から行ごとに判定')

    args = parser.parse_args()

    if args.command == 'run':
        if args.simulate:
            simulate_error(args.simulate)
        elif args.stdin:
            wrap_stdin()
        else:
            print('エラーメッセージを --simulate で指定、または --stdin で標準入力から受け取ってください。')
            sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        tb = traceback.format_exc()
        print(format_haiku(str(e)))
        print(tb)