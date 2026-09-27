# 概要
このSkillは、AI社会の“評価される感覚”をパロディ化し、作業空間にユーモアと風刺を加えるために設計されています。実用性はなく、完全に無害な通知のみを生成します。

# 公式ドキュメント抜粋
- Python random: https://docs.python.org/3/library/random.html
- Python subprocess: https://docs.python.org/3/library/subprocess.html
- notify-send (Linux): https://specifications.freedesktop.org/notification-spec/

# 利用例
- 長時間の作業やコーディングセッション中に、突発的なAI評価通知で気分転換
- チーム内の雑談やイベントで“AI監査ごっこ”として活用

# 注意点
- 実際の評価や監視は一切行いません
- ユーザーのプライバシーやシステム設定に影響しません
- ログは一時ファイルに保存されますが、個人情報や機密情報は含みません

# 設計方針
- 通知頻度や内容はウザすぎないよう調整
- OSごとの通知APIを自動判別し、端末環境に応じて最適な表示方法を選択
- サブコマンドで手動実行・履歴確認も可能