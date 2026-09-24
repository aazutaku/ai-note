# 概要
このSkillは、開発者の作業中に意図的な“知的ノイズ”として古文調の詩を通知し、集中力のリセットや気分転換を促します。通知内容は完全ランダム生成で、実際の作業内容やエラーには一切干渉しません。

# 公式ドキュメント抜粋
- plyer: https://plyer.readthedocs.io/en/latest/
- argparse: https://docs.python.org/3/library/argparse.html

# 利用例
- `/random-os-fake-ancient-poem-notifier once` で1回だけ通知
- `/random-os-fake-ancient-poem-notifier loop --min-interval 120 --max-interval 600` で2-10分ごとに自動通知
- `/random-os-fake-ancient-poem-notifier sample --count 10` で10個の詩を標準出力

# 注意点
- plyer未インストール時は標準出力のみ対応
- 通知内容は完全に無関係な詩文で、誤作動や誤通知の心配はありません

# 設計方針
- OS依存せず、Pythonとplyerで主要環境に対応
- ユーザーの作業内容やファイルには一切アクセスしない安全設計
- 詩句パーツを拡張することで多様な表現が可能