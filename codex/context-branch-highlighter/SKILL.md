---
name: context-branch-highlighter
description: 複数の作業ブランチやタスクが混在し、現在の作業コンテキストや注力すべきブランチを明示的に可視化したい場合に発動。"branch", "context", "focus", "作業履歴" などのキーワード検出時や明示コマンドで有効。
---

# 機能概要
context-branch-highlighterは、複数のGitブランチやタスクが並行して進行しているプロジェクトで、現在注力すべき作業コンテキストやブランチを自動的に抽出・ハイライトするSkillです。直近の編集履歴や作業ディレクトリ、Gitのログ情報をもとに、迷子状態や枝分かれによる混乱を防ぎます。特に分岐・合流が頻繁な開発現場や、複数タスクを同時に管理する必要がある場合に有効です。

# 使い方
- 明示呼び出し: `/skills menu` から本Skillを選択、または `$context-branch-highlighter` を直接メンション
- 暗黙発動キーワード: "branch", "context", "focus", "どの作業に集中すべきか", "直近の編集履歴" などを含む発話時
- CLI利用例: `python context_branch_highlighter.py summary` で主要な作業ブランチとフォーカス中のファイル群を一覧表示

# 出力例
```
[Context Branch Highlighter]
現在の作業ブランチ: feature/refactor-auth
直近の編集ファイル:
  - src/auth/handler.py (3分前)
  - tests/test_auth.py (10分前)
  - README.md (25分前)
推奨フォーカス: feature/refactor-auth
他のアクティブブランチ: bugfix/login-error, feature/ui-improve
```

# 注意点
- Gitリポジトリ直下でのみ動作します
- 除外パスや巨大バイナリは自動的に無視されます
- ローカルのGit履歴やファイルタイムスタンプを利用するため、未コミットの変更も反映されます
- プライベートな編集履歴は外部送信されません

# 参考資料
設計方針や利用例、詳細仕様は `references/design_notes.md` を参照してください。Git公式ドキュメント: https://git-scm.com/doc