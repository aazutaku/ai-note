---
name: context-switch-logbook
description: エージェントや作業ブランチの切り替え時、"切り替え元・切り替え先・理由"を自動ログするSkillです。"エージェント切り替え"や"タスク移動"などのキーワード検出時に発動します。
---

# 機能概要
このSkillは、作業中にエージェントやタスクの切り替えが発生した際、そのタイミング・切り替え元・切り替え先・理由メモを自動的に記録します。これにより、なぜどのタイミングでどのタスクやエージェントに移動したのかを後から振り返ることができ、作業の流れや思考経路の可視化が容易になります。特に複数のプロジェクトやタスクを並行して進める場合、文脈の断絶や作業理由の忘却を防ぎます。

# 使い方
このSkillは、"エージェント切り替え"、"タスク移動"、"作業ブランチ変更"などのキーワードや、明示的な切り替え操作を検出して自動発動します。ユーザーは切り替え時に、切り替え元・切り替え先・理由を入力するプロンプトが表示されます。コマンドラインからは `python timeline_logger.py log` で手動記録、`python timeline_logger.py list` で履歴一覧、`python timeline_logger.py summary` で要約表示ができます。

# 出力例
```
[2024-06-01 14:23:10] from: "feature/login" to: "bugfix/session-timeout" reason: "緊急バグ対応のため"
[2024-06-01 15:05:42] from: "Antigravity" to: "CodeReview" reason: "コードレビュー依頼が来た"
[2024-06-01 16:11:20] from: "CodeReview" to: "Antigravity" reason: "レビュー完了、元タスクに復帰"
```

# 注意点
ログはローカルファイル (context_switch_logbook.log) に保存されます。ネットワーク同期や共有は自動では行われません。切り替え理由の入力は省略可能ですが、後の振り返り精度向上のため記入を推奨します。Skillの発動はsemantic-matchのみで、明示呼び出しはありません。

# 参考資料
詳細設計や運用例は references/design_notes.md を参照してください。公式のAntigravityドキュメント(https://ai-note.tech/antigravity/docs/context-management)も参考になります。