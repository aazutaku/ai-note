---
name: prompt-branch-suggester
description: 作業中のブランチ名、コミットメッセージ、直前のファイル差分などから、Codexが最適な指示ファイル分岐や一時的なプロンプトセットを自動生成・提案するSkillです。semantic triggerや明示呼び出しに対応。
---

# 機能概要
prompt-branch-suggesterは、現在の作業ブランチ名や直近のコミットメッセージ、ファイルのdiff情報をもとに、Codex向けの最適な指示ファイル（例: CLAUDE.md, AGENTS.md）の分岐や一時的なプロンプトセットを自動生成・提案するSkillです。これにより、細かな作業やイレギュラーな対応時にも、編集者が都度指示を手入力する手間を省き、作業内容に即した適切なプロンプト分岐を迅速に得ることができます。

# 使い方
- 明示呼び出し例: `/skills prompt-branch-suggester suggest` または `$prompt-branch-suggester suggest`
- 暗黙発動キーワード例: `hotfix`, `feature/`, `WIP`, `refactor`, `urgent`, `conflict`, `merge`, `release`, `fix`, `test`, `chore`
- semantic trigger: ブランチ切替・コミット直後・大きなdiff発生時など

# 出力例
```
$ /skills prompt-branch-suggester suggest
[INFO] Detected branch: feature/add-login
[INFO] Recent diff: Added login.py, Modified auth_utils.py
[PROPOSAL] Create AGENTS.feature-add-login.md with login-specific instructions.
[PROPOSAL] Temporary prompt set:
- Focus on input validation and error handling for login flow.
- Prioritize security best practices.
```

# 注意点
- 既存の指示ファイルは上書きせず、分岐ファイルや一時ファイルとして保存されます。
- ローカルリポジトリのgit情報を参照するため、gitがインストールされている必要があります。
- 巨大なdiffや曖昧なブランチ名の場合は、提案内容が一般的になることがあります。
- 機密情報や個人情報を含むdiffは除外されます。

# 参考資料
- [references/design_notes.md](references/design_notes.md)
- [GitPython公式](https://gitpython.readthedocs.io/)
- [OpenAI Codex公式](https://platform.openai.com/docs/guides/code)