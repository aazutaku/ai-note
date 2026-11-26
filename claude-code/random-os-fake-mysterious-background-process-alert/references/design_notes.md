# 概要
このSkillは、作業中に突如“謎のOS風バックグラウンドプロセス通知”をランダムに生成し、ユーザーの注意や好奇心を刺激する演出ツールです。実際のシステムやファイルには一切影響を与えず、完全に無害なジョーク用途を想定しています。

# 公式ドキュメント抜粋
- Python random: https://docs.python.org/3/library/random.html
- Python argparse: https://docs.python.org/3/library/argparse.html

# 利用例
- ターミナルで `python random_os_fake_alert.py log --count 3` を実行すると、3回ランダムな間隔で通知が表示されます。
- `/random-os-fake-mysterious-background-process-alert` コマンドで明示的な発動も可能。

# 注意点
- 本Skillは演出のみを目的としており、実際のプロセスやシステムリソースには一切アクセスしません。
- 通知内容は完全にランダム生成され、実害やデータ損失はありません。

# 設計方針
- 意味不明な単語や進捗バー、残り時間などを組み合わせ、都市伝説的な“謎感”を演出。
- サブコマンド(log/list/summary)で柔軟な使い分けが可能。
- シンプルな実装で拡張性も考慮しています。