---
name: context-branch-highlighter
description: 複数の作業ブランチやタスクが混在し、どの流れに注力すべきか曖昧な場合に発動。"作業中のブランチ" "直近の編集" "分岐の可視化" などのキーワードや明示コマンドで実行。
---

# 機能概要
context-branch-highlighterは、複数の作業ブランチやタスクが並行する開発現場で、現在注力すべきブランチや作業コンテキストを明示的に可視化・ハイライトするSkillです。gitリポジトリのブランチ構造や直近の編集履歴、作業ディレクトリ内の変更ファイルなどから、"今フォーカスすべき流れ"を自動抽出し、分岐・合流が頻繁なプロジェクトや複数タスク並行時の混乱を防ぎます。これにより、迷子状態や誤ったブランチでの作業を防止し、効率的なタスク管理を実現します。

# 使い方
- 明示呼び出し: `/context-branch-highlighter` または `/skill context-branch-highlighter`
- 暗黙発動キーワード例: "現在の作業ブランチは?", "どのタスクに集中すべき?", "直近の編集流れを見せて", "分岐の状況を可視化して"
- CLIサブコマンド: `python context_branch_highlighter.py summary` など

# 出力例
```
[Context Branch Highlighter]
現在注力すべきブランチ: feature/login-refactor
直近の編集ファイル:
  - src/auth/login.py (3分前)
  - tests/test_login.py (8分前)
関連ブランチ:
  - develop (親)
  - bugfix/login-typo (兄弟)
ブランチ分岐状況:
  feature/login-refactor ← develop ← main
   └─ bugfix/login-typo
```

# 注意点
- gitリポジトリ外や履歴のないプロジェクトでは機能しません
- 除外パスや巨大バイナリファイルは自動的に無視されます
- ローカルの変更状況のみを解析し、リモート未反映の情報は含みません
- 出力はターミナル/CLI向けであり、GUI統合は含みません

# 参考資料
- references/design_notes.md
- https://git-scm.com/docs/git-branch
- https://docs.python.org/3/library/subprocess.html