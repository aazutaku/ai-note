# 概要
本Skillは、作業者の気分転換や遊び心を刺激するため、完全に架空のOSエラーを五・七・五の俳句形式で通知するものです。通知内容は毎回異なり、技術用語と季語を組み合わせて詩的な雰囲気を演出します。

# 公式ドキュメント抜粋
通知にはPythonの `plyer` ライブラリを利用し、クロスプラットフォームでデスクトップ通知が可能です。`plyer`が未導入の場合は標準出力にフォールバックします。

# 利用例
- 明示呼び出し: `python random_os_fake_error_haiku_notifier.py notify`
- 定期通知: `python random_os_fake_error_haiku_notifier.py periodic --interval 120`
- キーワード監視: `python random_os_fake_error_haiku_notifier.py monitor --keywords error fail`

# 注意点
本Skillはジョーク用途専用であり、実際のエラー検知や障害報告には一切利用できません。通知頻度や発動条件は作業の妨げにならないよう調整してください。

# 設計方針
五・七・五の音数に近づけるため語彙リストとテンプレートを複数用意し、ランダム性と詩的表現の両立を目指しました。通知APIはローカル限定で、外部送信やデータ保存は行いません。