---
name: prompt-branch-suggester
description: 作業ブランチ名やコミットメッセージ、直前のファイル差分などのキーワードを検出した際に、Antigravityが最適な指示ファイルやプロンプト分岐案を自動生成・提案するSkillです。semantic-match-only条件で発動します。
---

# 機能概要
prompt-branch-suggesterは、現在の作業ブランチ名、コミットメッセージ、直前のファイル差分（diff）などの情報をもとに、Antigravityエージェントが最適な指示ファイル（例：CLAUDE.mdやAGENTS.md）の分岐案や一時的な指示セットを自動生成・提案するSkillです。細かな修正やイレギュラーな対応時にも、編集者が手動で指示を記述する手間を省き、状況に応じた適切なプロンプト分岐を迅速に得ることができます。

# 使い方
このSkillは、semantic-match-only条件下で自動発動します。明示的な呼び出しは不要です。例えば、"fix/"や"hotfix/"、"feature/"などのブランチ名、コミットメッセージに"refactor"や"urgent"が含まれる場合、またはdiffに大きな変更が検出された場合に発動します。手動での呼び出しはサポートしていません。

# 出力例
```
# .agent/skills/prompt-branch-suggester/SUGGESTED_CLAUDE.md
## 指示分岐案
- ブランチ: feature/add-login
- 差分: login.py, auth.pyの新規追加
- 推奨指示: 新機能追加に伴う認証ロジックのレビューを優先してください。

# .agent/skills/prompt-branch-suggester/SUGGESTED_AGENTS.md
- ブランチ: hotfix/critical-bug
- 差分: bugfix.py修正
- 推奨指示: 緊急バグ修正。テストカバレッジを重視し、最小限の変更で対応してください。
```

# 注意点
- 既存の指示ファイル（CLAUDE.md/AGENTS.md）は上書きせず、SUGGESTED_*.mdとして安全に保存されます。
- あくまで提案であり、最終的な適用は編集者の判断に委ねられます。
- 差分取得はgitコマンドを利用するため、リポジトリ直下での実行が前提です。
- 大規模なdiffや複雑なブランチ構成では提案精度が低下する場合があります。

# 参考資料
- references/design_notes.md
- https://docs.github.com/ja/get-started/using-git/viewing-the-commit-history
- https://platform.openai.com/docs/api-reference
