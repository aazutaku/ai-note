# 概要
このSkillは、ユーザーの無操作状態を30秒単位で監視し、作業中断時にユーモラスなアラートを発動します。Pythonの標準ライブラリとnotify2（Linux）、osascript（macOS）によるデスクトップ通知、またはターミナル出力で幅広い環境に対応しています。

# 公式ドキュメント抜粋
- [notify2](https://pypi.org/project/notify2/): Linux向けデスクトップ通知
- [subprocess](https://docs.python.org/3/library/subprocess.html): macOS通知やコマンド実行に使用
- [time](https://docs.python.org/3/library/time.html): 無操作検出ロジック

# 利用例
- 作業に集中できない時の自虐ネタや、職場でのアイスブレイク
- チームでのペアプロ時に「サボり検出」演出

# 注意点
- データ損失や外部送信は一切ありません
- WSLなど一部環境ではデスクトップ通知が動作しない場合があります

# 設計方針
- ユーザー体験を損なわず、絶妙なタイミングで通知
- メッセージは毎回ランダム、繰り返しでも飽きが来ない工夫
- シンプルなファイル記録でクロスプラットフォーム対応