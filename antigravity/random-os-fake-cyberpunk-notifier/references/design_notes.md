# 概要
このSkillは、ユーザーの作業環境にサイバーパンクSF世界の架空OS通知をランダム表示し、現実逃避や気分転換を促すために設計されています。通知内容は実在せず、完全に演出目的です。

# 公式ドキュメント抜粋
通知表示にはOS標準APIを利用します。Windows: win10toast, macOS: pync, Linux: notify2。詳細は各公式ドキュメントを参照してください。
- win10toast: https://github.com/jithurjacob/Windows-10-Toast-Notifications
- pync: https://github.com/setem/pync
- notify2: https://github.com/caronc/notify2

# 利用例
長時間作業や集中力低下時に、現実離れした通知で一時的なリフレッシュや遊び心を提供します。通知履歴やサマリー表示も可能で、演出の記録として活用できます。

# 注意点
通知内容は全て架空であり、実用的な意味や警告はありません。業務用途や重要な通知と混同しないよう注意してください。通知頻度が高すぎる場合はスクリプトの引数で調整してください。

# 設計方針
実在APIのみを使用し、OSごとに最適な通知方法を選択。スクリプトはCLIサブコマンドで柔軟に操作可能とし、Skill本体からも直接呼び出せる設計です。