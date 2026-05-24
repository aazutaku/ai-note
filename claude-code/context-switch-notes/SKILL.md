---
name: context-switch-notes
description: Claude Codeがプロンプトや作業対象の切り替え（タスク名・プロジェクト名・ファイルパス・明示呼び出し /context-switch-notes）を検知した際に発動し、直前の作業内容やTODOメモを自動保存・復元します。
---

# 機能概要
context-switch-notesは、複数のタスクやプロジェクトを並行して進める際に、直前の作業内容や思考メモをコンテキストごとに自動で記録・表示するSkillです。作業対象（例: プロンプト、ファイル、プロジェクト）の切り替えを検知し、切り替え時に直前の要約やTODOを自動保存。次回そのコンテキストに戻った際には、保存済みのメモを自動で復元・表示します。これにより、作業の流れを途切れさせず、効率的な再開やタスク間の知識継承を支援します。

# 使い方
- 明示呼び出し: `/context-switch-notes add "今の作業内容" --context "projectA"`
- 暗黙発動: `projectA` から `projectB` への切り替え、またはファイル/プロンプトの切り替え時に自動発動（例: "Switching to projectB" の検知）
- メモ一覧: `/context-switch-notes list --context "projectA"`
- 要約表示: `/context-switch-notes summary --context "projectA"`

# 出力例
```
[context-switch-notes] Restored notes for context: projectA
- 2024-06-10 15:12: 作業途中のバグ修正ポイント
- 2024-06-10 15:13: TODO: テストコード追加

[context-switch-notes] Added note to context: projectB
- 2024-06-10 15:20: 仕様確認待ち
```

# 注意点
- メモはローカルの `.claude/skills/context-switch-notes/notes.json` に保存されます。
- コンテキストの粒度（プロジェクト名、ファイルパス等）は環境に依存します。
- メモが冗長にならないよう、1コンテキストあたり最新10件まで自動管理されます。
- データ損失防止のため、保存前にバックアップを作成します。
- 除外パス（例: 一時ファイル）は対象外です。

# 参考資料
- [references/design_notes.md](references/design_notes.md)
- [公式ドキュメント](https://ai-note.tech/skills/context-switch-notes)