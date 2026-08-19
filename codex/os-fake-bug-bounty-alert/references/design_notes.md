# 概要
このSkillは、作業現場や開発環境に突如現れる“偽バグバウンティ通知”を通じて、緊張緩和やチームの和ませ効果を狙う演出系ツールです。通知内容は完全ランダム生成で、現実離れしたバグと報酬の組み合わせが特徴です。

# 公式ドキュメント抜粋
- Python random: https://docs.python.org/3/library/random.html
- plyer通知: https://pypi.org/project/plyer/

# 利用例
- ターミナルで`python os_fake_bug_bounty_alert.py alert --desktop`と実行すると、OSの通知領域にユーモラスな偽バグバウンティが表示されます。
- `python os_fake_bug_bounty_alert.py list -n 3`で複数例を確認できます。

# 注意点
- 本Skillは実害ゼロで、システムやファイルを改変しません。
- plyerがインストールされていない場合はデスクトップ通知はスキップされます。

# 設計方針
- バグ内容・報酬ともに現実味を排除し、あくまで“ネタ”として設計。
- ログ出力やデスクトップ通知の切り替え、明示/暗黙トリガー両対応で柔軟性を持たせています。