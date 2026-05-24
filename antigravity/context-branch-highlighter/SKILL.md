---
name: context-branch-highlighter
description: 複数の作業ブランチやタスクが同時進行中で、現在注力すべきブランチやコンテキストを明示する必要がある場合に発動。"branch", "context", "focus", "作業履歴", "タスク切替"などのキーワードを含む状況で自動発動します。
---

# 機能概要
context-branch-highlighterは、複数のGitブランチやタスクが並行して進行するプロジェクトにおいて、「今どの作業流れに注力すべきか」を明確に可視化・ハイライトするSkillです。作業中ディレクトリや直近のファイル編集履歴、Gitのブランチ・コミット情報を解析し、主要な作業コンテキストを抽出。分岐・合流が頻繁な開発現場や、タスクの切り替えが多い状況で、迷子や混乱を防ぎます。

# 使い方
このSkillは明示的な呼び出しを必要とせず、"branch", "focus", "context", "作業履歴"などのキーワードや、複数ブランチ・タスクが混在している状況を検知すると自動発動します。暗黙的な発動例としては「今どのブランチに注力すべき？」「最近の作業履歴から主要な流れを教えて」などの問い合わせが該当します。

# 出力例
```
[Context Branch Highlighter]
主要作業ブランチ: feature/login-refactor (最終編集: 2024-06-20)
関連ファイル: src/auth.py, src/session.py
直近の編集履歴:
  - 2024-06-20 15:02: src/auth.py (you)
  - 2024-06-19 18:45: src/session.py (you)
分岐点: develop → feature/login-refactor
他の並行ブランチ: bugfix/token-expiry, feature/ui-update
推奨: feature/login-refactor に注力
```

# 注意点
- Gitリポジトリ外のディレクトリや、履歴管理外のファイルは対象外です。
- ローカルの変更・未コミットファイルも解析しますが、未保存ファイルは反映されません。
- プライバシー保護のため、個人名や詳細な履歴はサマリ化されます。
- 大規模リポジトリでは処理に数秒かかる場合があります。

# 参考資料
- [Git公式ドキュメント](https://git-scm.com/doc)
- references/design_notes.md 参照