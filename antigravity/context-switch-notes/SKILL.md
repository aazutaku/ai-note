---
name: context-switch-notes
description: タスクやプロンプト、作業対象の切り替えが発生した際に自動で発動。直前の作業内容や思考メモを保存・要約し、次回同じコンテキストに戻った際に自動表示。trigger: semantic-match-only, context, switch, prompt, project, task, note, resume, save, restore。
---

# 機能概要
context-switch-notes Skillは、複数のタスクやプロジェクトを並行して進める際に、作業の「流れ」を維持するための支援を行います。プロンプトや作業対象の切り替えを自動検知し、切り替え時に直前の作業内容やTODO、思考メモを要約して記録します。次回同じコンテキストに戻った際には、これらのメモを自動で表示し、作業の再開をスムーズにします。これにより、タスク間の切り替えによる情報の断絶や、思考の中断による効率低下を防ぎます。

# 使い方
このSkillは明示的な呼び出しを必要としません。Antigravityがタスクやプロジェクト、プロンプトの切り替えを検知した際に自動で発動します。例えば、`projectA`から`projectB`に切り替える、または異なるプロンプト間を移動する場合などが対象です。暗黙発動キーワード例: "switch context", "change project", "resume task", "prompt切り替え" など。

# 出力例
```
[context-switch-notes] Context: projectA
Last summary: バグ修正の途中。main.pyの35行目で例外が発生。
TODO: エラーハンドリング追加、テストケース作成
---
[context-switch-notes] Context: projectB
Last summary: 新機能の設計メモ。API仕様要確認。
TODO: 仕様書レビュー、設計図作成
```

# 注意点
- メモはローカルストレージ（.context_notes/ ディレクトリ）に保存されます。
- メモが冗長にならないよう、要約と重複排除を自動で行います。
- 機密情報やパスワードは記録しない設計ですが、内容の確認を推奨します。
- Skill本体や既存作業に影響を与えないよう、データ損失防止のため定期バックアップを推奨します。

# 参考資料
詳細な設計方針や利用例は references/design_notes.md を参照してください。公式ドキュメント: https://ai-note.tech/docs/context-switch-notes