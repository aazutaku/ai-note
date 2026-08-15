# 概要
本Skillは、開発者の作業環境に“謎のシャットダウン瞑想”を演出することで、集中のリズムを意図的に崩し、ユーモラスな気分転換やリフレッシュを促します。Pythonの標準GUIや通知APIを活用し、実際のOS操作は一切行いません。

# 公式ドキュメント抜粋
- plyer: https://plyer.readthedocs.io/en/latest/
- tkinter: https://docs.python.org/ja/3/library/tkinter.html

# 利用例
- CLIから `python fake_shutdown_meditation.py run` を実行すると、5分間の瞑想タイムが始まり、進捗バーやタイマー、通知がランダムに現れます。
- `python fake_shutdown_meditation.py list` でメッセージ一覧を確認できます。

# 注意点
- plyer, tkinterが未インストールの場合は、通知やGUI進捗バーが表示されません（代替として標準出力に出力）。
- 実際のシャットダウンや再起動は一切行わない安全設計です。

# 設計方針
- クロスプラットフォーム（Windows/Mac/Linux）で動作可能なAPIのみ採用。
- ランダム性と進捗演出を重視し、毎回異なる体験を提供します。