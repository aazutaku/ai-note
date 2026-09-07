# 概要
このSkillは、ポモドーロタイマーの開始や終了時に、実用性ゼロのジョーク通知をOSのデスクトップ通知またはターミナル出力で表示します。集中力を維持しつつ、作業の合間にクスっと笑えるエンタメ要素を提供します。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/3/library/subprocess.html
- plyer通知API: https://github.com/kivy/plyer

# 利用例
- ターミナルで `python fake_pomodoro_notifier.py start` を実行すると、作業・休憩の開始/終了ごとに毎回異なるフェイク通知が表示されます。
- `python fake_pomodoro_notifier.py notify --count 5` で、5回分のジョーク通知を即座に表示。

# 注意点
- 本Skillは実際のタイマー管理や作業記録は行いません。通知内容はすべてフィクションです。
- 通知APIが利用できない場合は、ターミナル出力にフォールバックします。

# 設計方針
- OSごとに適切な通知APIを呼び出し、クロスプラットフォーム対応。
- メッセージはリストからランダム選択し、毎回異なる演出を保証。
- 環境構築が容易で、10分以内に動作確認できるシンプル設計。
