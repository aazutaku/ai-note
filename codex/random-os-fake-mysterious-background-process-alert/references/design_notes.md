# 概要
このSkillは、実際には何も起きていないのに“OS公式通知”風の怪しいバックグラウンドプロセス警告をランダムに生成し、ユーザーの作業中に不意打ちで表示します。心理的な演出やIT都市伝説的な雰囲気を楽しむためのものです。

# 公式ドキュメント抜粋
- Python random: https://docs.python.org/3/library/random.html
- argparse: https://docs.python.org/3/library/argparse.html

# 利用例
- ターミナルで `python mysterious_process_alert.py batch -n 3` を実行すると、数回にわたり不穏な通知が表示されます。
- `/skills random-os-fake-mysterious-background-process-alert` で明示呼び出しも可能です。

# 注意点
- 実際のプロセスやシステムには一切影響を与えません。
- ログやファイルへの書き込みは行いません。
- データ損失や誤動作の心配はありません。

# 設計方針
- 完全に演出目的。意味不明・不安を煽るが、害はゼロ。
- 毎回異なるPIDや進捗、活動名をランダム生成。
- 実在しないプロセス名やOS通知風の文体で都市伝説感を演出。