---
name: prompt-branch-suggester
description: 作業ブランチ名、コミットメッセージ、直前のファイル差分などをもとに、Claude Code/Codex/Antigravity が適切なプロンプト分岐や一時的な指示セットを自動生成・提案するSkill。分岐提案や指示ファイル生成が必要な作業やイレギュラー対応時に発動。
---

# 機能概要
このSkillは、現在の作業ブランチ名・直近のコミットメッセージ・ファイル差分情報をもとに、Claude Codeのプロンプト分岐（例: CLAUDE.md/AGENTS.mdの一時的な指示セット）を自動提案します。頻繁な細分化作業やイレギュラーな修正時、編集者が毎回手動で指示ファイルを編集する手間を減らし、適切な分岐や指示セットを素早く得ることができます。安全な運用のため、既存ファイルを上書きせず一時的なファイルとして保存されます。

# 使い方
明示的な呼び出しは `/prompt-branch-suggester` コマンドで実行します。暗黙的には「feature/」「hotfix/」などのブランチ名や「fix」「refactor」「urgent」などのコミットメッセージが検出された際に自動発動します。CLIから直接サブコマンドを指定して利用することも可能です。

# 出力例
```
$ /prompt-branch-suggester
[INFO] 現在のブランチ: feature/add-login
[INFO] 直近コミット: "add login form and validation"
[INFO] 差分ファイル: src/login.py, templates/login.html
[OK] CLAUDE_prompt_branch_feature_add-login.md を生成しました

# CLAUDE_prompt_branch_feature_add-login.md
- ログイン機能の追加・検証に集中する指示セット
- 既存の認証ロジックには触れない
- UI/UXの改善案も提案
```

# 注意点
- 既存の指示ファイルは上書きしません（一時ファイルとして保存）
- 除外パス（例: .git/, node_modules/）は自動で無視されます
- 差分取得にはGitコマンドが必要です
- 複雑な分岐や大規模な差分には対応しきれない場合があります

# 参考資料
- references/design_notes.md
- https://github.com/anthropic/claude-code
- https://docs.github.com/ja/rest/commits/commits