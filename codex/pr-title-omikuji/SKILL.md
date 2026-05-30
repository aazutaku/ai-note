---
name: pr-title-omikuji
description: CodexがPR作成やタイトル編集時、または/skills menuやpr-title-omikujiの明示呼び出し時に発動。PRタイトルを“おみくじ”風に自動変換し、運勢ワードを付与します。
---

# 機能概要
pr-title-omikujiは、Pull Request（PR）作成時やタイトル編集時に、PRタイトルを“おみくじ”形式へ自動変換するジョーク系Skillです。運勢（大吉・中吉・小吉・末吉・凶など）と、ユニークなコメントをタイトル先頭に付与し、開発現場の空気を一変させます。タイトル内容と運勢は無関係で、作業の真面目さに“運ゲー”要素を加え、レビューやマージの儀式をエンタメ化します。

# 使い方
- PR作成時やタイトル編集時に自動発動（always/semantic trigger）
- 明示的に `/skills menu` から選択、または `$pr-title-omikuji` で呼び出しも可能
- 暗黙発動キーワード例: "PR", "pull request", "タイトル", "title", "merge"

# 出力例
```
[大吉] 運命のリファクタリング: Fix typo in README
[小吉] 軽い修正だけど運は微妙: Update dependencies
[中吉] ちょっと良い感じ: Add new API endpoint
[末吉] まあまあの変更: Refactor user model
[凶] 波乱の予感: Hotfix for production bug
```

# 注意点
- タイトル内容はランダム運勢で上書きされます（元タイトルは末尾に残る）
- ローカル保存や履歴管理は行いません
- 機密情報のタイトルには注意
- 除外パスや特定ブランチは設定できません（要カスタマイズ）

# 参考資料
- references/design_notes.md に設計意図や運勢バリエーションの根拠を記載
- 公式GitHub API: https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28