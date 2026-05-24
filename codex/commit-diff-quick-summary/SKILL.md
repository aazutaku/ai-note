---
name: commit-diff-quick-summary
description: コミット直前やコードレビュー時に、'git diff'や'コミット差分'などのキーワードを検出した際、または明示的なSkill呼び出し時に発動。差分内容をAIで要約し、主要な変更点や影響範囲を端的に提示します。
---

# 機能概要
`commit-diff-quick-summary`は、コミット前やレビュー時に発生するコード差分（git diff）をAIで自動要約し、主要な変更点や影響範囲を端的にまとめて表示するSkillです。これにより、手動で大量の差分を読む手間を大幅に削減し、不要な変更や意図しない混入を素早く発見できます。日本語・英語混在プロジェクトにも対応し、既存のワークフローに追加ファイル不要で即導入可能です。

# 使い方
- 明示呼び出し例：
  - `/skills commit-diff-quick-summary`
  - `$commit-diff-quick-summary summary`
- 暗黙発動キーワード例：
  - 「git diff」「コミット差分」「変更点要約」「レビュー前要約」などの文脈で自動発動します。

# 出力例
```
主要な変更点:
- src/utils.py: 新たにvalidate_email関数を追加、既存のvalidate_phone修正
- tests/test_utils.py: validate_email用テストケースを追加
影響範囲:
- バリデーションロジックの拡張により、ユーザー登録・編集機能に影響
- 既存の電話番号バリデーションが厳格化
```

# 注意点
- 差分が極端に大きい場合、要約精度が低下することがあります
- 除外パス（例: .gitignore, node_modules, build/）は自動除外
- ローカルに差分データを保存しません
- AI要約のため、100%の網羅性や正確性は保証されません

# 参考資料
- [git diff 公式ドキュメント](https://git-scm.com/docs/git-diff)
- references/design_notes.md も参照