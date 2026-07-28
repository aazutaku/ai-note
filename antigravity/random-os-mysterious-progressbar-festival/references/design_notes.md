# 概要
このSkillは、作業中に突如として意味不明な進捗バーを複数表示し、OSやプロジェクトの進捗とは無関係なカオス演出を提供します。主に作業現場の雰囲気緩和や、チーム内のコミュニケーション促進を目的としています。

# 公式ドキュメント抜粋
- Python random: https://docs.python.org/3/library/random.html
- Python argparse: https://docs.python.org/3/library/argparse.html
- 端末制御: https://docs.python.org/3/library/shutil.html#get-terminal-size

# 利用例
- ターミナルで `python mysterious_progressbar_festival.py once` を実行すると、ランダムな進捗バーが数秒間表示されます。
- `festival` サブコマンドで、一定間隔ごとに自動で進捗バーが発生します。

# 注意点
- 実際の進捗やOS状態とは一切関係ありません。
- 進捗バーはローカル端末上のみ一時的に表示され、外部保存や送信は行いません。
- 端末の幅によってはバーが自動で切り詰められます。

# 設計方針
- シンプルなCLI構成で、スクリプト単体で完結。
- テーマ・進捗値は毎回完全ランダム。
- ユーザー体験重視のカオス演出と、容易な拡張性を両立。