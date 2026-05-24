---
name: context-switch-logbook
description: エージェントや作業ブランチ、タスクの切り替え時にこのSkillを発動し、切り替え元・先・理由メモを記録します。context switch, branch change, agent switch などのキーワードや明示呼び出しで発動します。
---

# 機能概要
context-switch-logbook Skillは、作業中に発生するエージェントやタスク、作業ブランチの切り替え（コンテキストスイッチ）を記録するためのツールです。ユーザーがタスクやエージェントを切り替えるたびに、そのタイミング・切り替え元・切り替え先・理由メモを自動または手動で記録します。これにより「なぜこの作業に移ったか」「どの順で進めたか」など、作業の流れや思考の履歴を後から簡単に振り返ることができ、コンテキストの喪失やタスクの抜け漏れを防ぎます。

# 使い方
- 明示呼び出し例: `/context-switch-logbook log --from "feature/login" --to "bugfix/api-error" --reason "急ぎのバグ修正依頼"`
- 暗黙発動キーワード例: `context switch`, `branch change`, `agent switch`, `タスク切り替え`, `今の作業を中断`
- ログの閲覧: `/context-switch-logbook list` または `/context-switch-logbook summary`

# 出力例
```
[2024-06-28 13:10:12] from: feature/login -> to: bugfix/api-error | reason: 急ぎのバグ修正依頼
[2024-06-28 14:02:05] from: bugfix/api-error -> to: refactor/session | reason: バグ修正完了、リファクタに戻る
[2024-06-28 15:20:30] from: refactor/session -> to: review | reason: コードレビュー依頼が来たため
```

# 注意点
- ログはローカルの `.claude/skills/context-switch-logbook/logbook.jsonl` に保存されます。
- CLIからのみ記録・閲覧可能です。外部APIや他サービス連携はありません。
- 誤記録や記録漏れに注意し、定期的な振り返りをおすすめします。
- 機密情報や個人情報の入力にはご注意ください。

# 参考資料
- [references/design_notes.md](references/design_notes.md)
- 公式ドキュメント: https://ai-note.tech/skills/context-switch-logbook