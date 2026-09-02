# 概要
本Skillは、OSやメモリに関する会話や長時間の作業時に、ユーザーの注意を引くためのフェイク通知を表示します。通知内容は毎回ランダムで、実際のシステムには一切影響を与えません。

# 公式ドキュメント抜粋
- Python random: https://docs.python.org/ja/3/library/random.html
- plyer (通知用): https://plyer.readthedocs.io/en/latest/
- notify2 (Linux通知): https://pypi.org/project/notify2/
- win10toast (Windows通知): https://pypi.org/project/win10toast/

# 利用例
- 長時間作業の合間にユーザーの集中をリセットする演出
- メモリやシステム関連のジョークやネタとして

# 注意点
- 本Skillは通知のみで、ファイルやシステムには何も変更を加えません。
- 通知内容は完全なフィクションです。誤解を招かないよう設計しています。
- 通知が不要な場合はSkillを無効化してください。

# 設計方針
- OSごとに適切な通知APIを利用し、導入・削除が容易な構造としています。
- 通知例は随時拡張可能で、ユーザー体験を損なわないよう配慮しています。